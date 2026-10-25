/* Exact finite verification of edge-addition monotonicity thresholds.
   C99; compile: cc -O2 -std=c99 -Wall -Wextra verify.c -o verify
   No external libraries are needed.  All matrix entries and determinants are integers. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 7
#define MAXE 21
#define CACHE 32768

typedef struct {int u,v;} Edge;
typedef struct {int valid; int64_t det, q_num, c_num;} Norm;

static int64_t iabs(int64_t v){return v<0?-v:v;}
static int64_t det_int(const int64_t a[MAXV][MAXV],int n){
    if(n==0)return 1;
    if(n==1)return a[0][0];
    int64_t out=0;int64_t minor[MAXV][MAXV];
    for(int j=0;j<n;j++){
        if(a[0][j]==0)continue;
        for(int r=1;r<n;r++)for(int c=0,d=0;c<n;c++){
            if(c!=j)minor[r-1][d++]=a[r][c];
        }
        int64_t t=a[0][j]*det_int(minor,n-1);
        out+=(j&1)?-t:t;
    }
    return out;
}
static int is_connected(int n,const Edge *e,int m){
    int seen=1,old;
    do{
        old=seen;
        for(int k=0;k<m;k++){
            if(seen&(1<<e[k].u))seen|=1<<e[k].v;
            if(seen&(1<<e[k].v))seen|=1<<e[k].u;
        }
    }while(seen!=old);
    return seen==((1<<n)-1);
}
static Norm projection_norms(int n,const Edge *edges,int m){
    Norm out={0,0,0,0};
    if(!is_connected(n,edges,m))return out;
    int z=n-1;int64_t L[MAXV][MAXV]={{0}},adj[MAXV][MAXV]={{0}};
    for(int j=0;j<m;j++){
        int u=edges[j].u,v=edges[j].v;
        if(u<z)L[u][u]++;
        if(v<z)L[v][v]++;
        if(u<z && v<z){L[u][v]--;L[v][u]--;}
    }
    int64_t d=det_int(L,z);
    if(d<=0){fprintf(stderr,"Nonpositive tree determinant\n");exit(2);}
    for(int r=0;r<z;r++)for(int c=0;c<z;c++){
        int64_t minor[MAXV][MAXV]={{0}};
        for(int i=0,ii=0;i<z;i++){
            if(i==c)continue;
            for(int j=0,jj=0;j<z;j++){
                if(j==r)continue;
                minor[ii][jj++]=L[i][j];
            }
            ii++;
        }
        int64_t x=det_int(minor,z-1);
        adj[r][c]=((r+c)&1)?-x:x;
    }
    int64_t q_max=0,c_max=0;
    for(int j=0;j<m;j++){
        int64_t q_sum=0,c_sum=0;
        for(int i=0;i<m;i++){
            int a=edges[i].u,b=edges[i].v;
            int u=edges[j].u,v=edges[j].v;
            int64_t q=0;
            if(a<z && u<z)q+=adj[a][u];
            if(a<z && v<z)q-=adj[a][v];
            if(b<z && u<z)q-=adj[b][u];
            if(b<z && v<z)q+=adj[b][v];
            q_sum+=iabs(q);
            c_sum+=iabs((i==j?d:0)-q);
        }
        if(q_sum>q_max)q_max=q_sum;
        if(c_sum>c_max)c_max=c_sum;
    }
    out.valid=1;out.det=d;out.q_num=q_max;out.c_num=c_max;
    return out;
}
static int64_t gcd_ll(int64_t a,int64_t b){
    while(b){int64_t t=a%b;a=b;b=t;}
    return a;
}
static void print_norm(const char *name, Norm v){
    int64_t g=gcd_ll(v.c_num,v.det),h=gcd_ll(v.q_num,v.det);
    printf("%s cut=%lld/%lld cycle=%lld/%lld\n",name,
      (long long)(v.q_num/h),(long long)(v.det/h),
      (long long)(v.c_num/g),(long long)(v.det/g));
}
static Norm graph_by_mask(int n,int mask,const Edge *pairs,int m){
    Edge edges[MAXE];int len=0;
    for(int k=0;k<m;k++)if((mask>>k)&1)edges[len++]=pairs[k];
    return projection_norms(n,edges,len);
}
int main(void){
    int64_t total_additions=0;int64_t total_graphs=0;int q_decreases=0;
    for(int n=2;n<=6;n++){
        Edge pairs[MAXE];int m=0;
        for(int u=0;u<n;u++)for(int v=u+1;v<n;v++){
            pairs[m].u=u;pairs[m].v=v;m++;
        }
        int cap=1<<m;
        Norm *cache=(Norm*)calloc((size_t)cap,sizeof(Norm));
        if(!cache){fprintf(stderr,"Allocation failure\n");return 2;}
        int64_t connected=0, additions=0, qdrops=0, cdrops=0;
        for(int mask=0;mask<cap;mask++){
            cache[mask]=graph_by_mask(n,mask,pairs,m);
            connected+=cache[mask].valid;
        }
        for(int mask=0;mask<cap;mask++){
            if(!cache[mask].valid)continue;
            for(int k=0;k<m;k++){
                if(mask&(1<<k))continue;
                Norm a=cache[mask],b=cache[mask|(1<<k)];
                if(!b.valid){fprintf(stderr,"Edge insertion disconnected\n");return 2;}
                additions++;
                if(a.q_num*b.det>b.q_num*a.det){qdrops++;}
                if(a.c_num*b.det>b.c_num*a.det){cdrops++;}
            }
        }
        total_graphs+=connected;total_additions+=additions;q_decreases+=(qdrops>0);
        printf("n=%d labelled-connected=%lld edge-insertions=%lld cut-decreases=%lld cycle-decreases=%lld\n",
            n,(long long)connected,(long long)additions,(long long)qdrops,(long long)cdrops);
        free(cache);
        if(cdrops!=0 || (n<5 && qdrops!=0) || (n==5 && qdrops==0))return 1;
    }
    printf("TOTAL labelled-connected=%lld edge-insertions=%lld\n",(long long)total_graphs,(long long)total_additions);
    Edge w[]={ {0,1},{0,4},{1,2},{1,3},{1,4},{1,6},{2,3},{3,4},{3,5},{4,5},{5,6} };
    Norm a=projection_norms(7,w,11);
    Edge h[12];for(int i=0;i<11;i++)h[i]=w[i];h[11]=(Edge){1,5};
    Norm b=projection_norms(7,h,12);
    print_norm("seven-before",a);print_norm("seven-after",b);
    if(a.c_num*b.det<=b.c_num*a.det){fprintf(stderr,"Witness lacks decrease\n");return 1;}
    if(a.c_num*153!=313*a.det || b.c_num*27!=55*b.det ||
       a.q_num*153!=284*a.det || b.q_num*9!=16*b.det)return 1;
    printf("ALL EXACT CHECKS PASSED; drop=4/459; threshold=7 vertices.\n");
    return 0;
}
