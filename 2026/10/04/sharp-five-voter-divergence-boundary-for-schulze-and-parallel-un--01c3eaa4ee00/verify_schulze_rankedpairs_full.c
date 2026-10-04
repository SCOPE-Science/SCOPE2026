#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define M 4
#define NORD 24
#define NPAIR 6
#define CACHE 46656

static int orders[NORD][M];
static int contrib[NORD][NPAIR];
static int paira[NPAIR]={0,0,0,1,1,2};
static int pairb[NPAIR]={1,2,3,2,3,3};
static int cperm[NORD][M];
static int nperm=0;
static unsigned char cache_ready[CACHE];
static unsigned char cache_s[CACHE], cache_r[CACHE];

static void genperm_rec(int d,int used,int *p){
    if(d==M){
        for(int i=0;i<M;i++) orders[nperm][i]=p[i];
        nperm++;
        return;
    }
    for(int x=0;x<M;x++) if(!(used&(1<<x))){
        p[d]=x; genperm_rec(d+1,used|(1<<x),p);
    }
}
static int pos_in_order(int oi,int x){
    for(int k=0;k<M;k++) if(orders[oi][k]==x) return k;
    return -1;
}
static int encmargin(const int d[NPAIR]){
    int z=0, mul=1;
    for(int e=0;e<NPAIR;e++){
        int digit=(d[e]+5)/2; // -5,-3,-1,1,3,5 -> 0..5
        z += digit*mul; mul*=6;
    }
    return z;
}
static int path_exists(uint16_t E,int start,int goal){
    int stack[4], top=0; unsigned seen=0;
    stack[top++]=start; seen|=1u<<start;
    while(top){
        int x=stack[--top]; if(x==goal) return 1;
        for(int e=0;e<NPAIR;e++){
            int a=paira[e],b=pairb[e];
            int u=-1,v=-1;
            if(E&(1u<<(2*e))){u=a;v=b;}
            else if(E&(1u<<(2*e+1))){u=b;v=a;}
            else continue;
            if(u==x && !(seen&(1u<<v))){seen|=1u<<v; stack[top++]=v;}
        }
    }
    return 0;
}
static int edge_index_dir(int a,int b){
    for(int e=0;e<NPAIR;e++){
        if(paira[e]==a && pairb[e]==b) return 2*e;
        if(paira[e]==b && pairb[e]==a) return 2*e+1;
    }
    return -1;
}

static void rp_group_dfs(const int *ga,const int *gb,int gsz,int idx,uint16_t E,unsigned char *wmask){
    if(idx==gsz){
        unsigned incoming=0;
        for(int e=0;e<NPAIR;e++){
            if(E&(1u<<(2*e))) incoming|=1u<<pairb[e];
            if(E&(1u<<(2*e+1))) incoming|=1u<<paira[e];
        }
        *wmask |= (unsigned char)(((1u<<M)-1u) & ~incoming);
        return;
    }
    (void)ga;(void)gb;(void)E;(void)wmask;
}

static void perm_process(const int *ga,const int *gb,int gsz,int depth,unsigned used,uint16_t E,uint16_t *outs,int *nout){
    if(depth==gsz){
        for(int k=0;k<*nout;k++) if(outs[k]==E) return;
        outs[(*nout)++]=E; return;
    }
    for(int i=0;i<gsz;i++) if(!(used&(1u<<i))){
        int a=ga[i],b=gb[i];
        uint16_t E2=E;
        if(!path_exists(E,b,a)) E2 |= (uint16_t)(1u<<edge_index_dir(a,b));
        perm_process(ga,gb,gsz,depth+1,used|(1u<<i),E2,outs,nout);
    }
}

static unsigned char rp_winners(const int d[NPAIR]){
    int ga[6],gb[6],gsz; uint16_t states[128],newstates[128]; int ns=1;
    states[0]=0;
    int strengths[3]={5,3,1};
    for(int si=0;si<3;si++){
        int s=strengths[si]; gsz=0;
        for(int e=0;e<NPAIR;e++){
            int val=d[e];
            if(val==s){ga[gsz]=paira[e];gb[gsz]=pairb[e];gsz++;}
            else if(val==-s){ga[gsz]=pairb[e];gb[gsz]=paira[e];gsz++;}
        }
        if(gsz==0) continue;
        int nnew=0;
        for(int st=0;st<ns;st++){
            uint16_t outs[64]; int no=0;
            perm_process(ga,gb,gsz,0,0,states[st],outs,&no);
            for(int j=0;j<no;j++){
                int dup=0; for(int k=0;k<nnew;k++) if(newstates[k]==outs[j]){dup=1;break;}
                if(!dup) newstates[nnew++]=outs[j];
            }
        }
        memcpy(states,newstates,(size_t)nnew*sizeof(uint16_t)); ns=nnew;
    }
    unsigned char W=0;
    for(int st=0;st<ns;st++){
        unsigned incoming=0; uint16_t E=states[st];
        for(int e=0;e<NPAIR;e++){
            if(E&(1u<<(2*e))) incoming|=1u<<pairb[e];
            if(E&(1u<<(2*e+1))) incoming|=1u<<paira[e];
        }
        W |= (unsigned char)(((1u<<M)-1u)&~incoming);
    }
    return W;
}

static unsigned char schulze_winners(const int d[NPAIR]){
    int p[M][M]={{0}};
    for(int e=0;e<NPAIR;e++){
        int a=paira[e],b=pairb[e],v=d[e];
        if(v>0) p[a][b]=v; else p[b][a]=-v;
    }
    for(int k=0;k<M;k++) for(int i=0;i<M;i++) if(i!=k)
      for(int j=0;j<M;j++) if(j!=i && j!=k){
        int z=p[i][k]<p[k][j]?p[i][k]:p[k][j]; if(z>p[i][j]) p[i][j]=z;
      }
    unsigned char W=0;
    for(int i=0;i<M;i++){
        int ok=1; for(int j=0;j<M;j++) if(i!=j && p[j][i]>p[i][j]){ok=0;break;}
        if(ok) W|=1u<<i;
    }
    return W;
}

static void ensure_cache(const int d[NPAIR],unsigned char *S,unsigned char *R){
    int key=encmargin(d);
    if(!cache_ready[key]){
        cache_s[key]=schulze_winners(d);
        cache_r[key]=rp_winners(d);
        cache_ready[key]=1;
    }
    *S=cache_s[key]; *R=cache_r[key];
}

static void relabel_margin(const int d[NPAIR],const int p[M],int out[NPAIR]){
    int mat[M][M]={{0}}, mm[M][M]={{0}};
    for(int e=0;e<NPAIR;e++){
        int a=paira[e],b=pairb[e]; mat[a][b]=d[e];mat[b][a]=-d[e];
    }
    for(int i=0;i<M;i++) for(int j=0;j<M;j++) mm[p[i]][p[j]]=mat[i][j];
    for(int e=0;e<NPAIR;e++) out[e]=mm[paira[e]][pairb[e]];
}
static int lexcmp(const int a[NPAIR],const int b[NPAIR]){
    for(int i=0;i<NPAIR;i++){if(a[i]<b[i])return -1;if(a[i]>b[i])return 1;}return 0;
}
static void canon_margin(const int d[NPAIR],int best[NPAIR]){
    for(int i=0;i<NPAIR;i++) best[i]=99;
    for(int pi=0;pi<NORD;pi++){
        int z[NPAIR]; relabel_margin(d,cperm[pi],z);
        if(lexcmp(z,best)<0) memcpy(best,z,sizeof(z));
    }
}
static int type_id(const int c[NPAIR]){
    const int A[NPAIR]={-3,-3,1,-1,-1,-1};
    const int B[NPAIR]={-3,-1,1,1,-1,-1};
    if(!memcmp(c,A,sizeof(A))) return 1;
    if(!memcmp(c,B,sizeof(B))) return 2;
    return 0;
}

static void enumerate_n(int n,unsigned long long hist[5][5][2],unsigned long long *diff,
                        unsigned long long typecnt[3]){
    unsigned long long total=1; for(int i=0;i<n;i++) total*=NORD;
    for(unsigned long long code=0; code<total; code++){
        unsigned long long q=code; int d[NPAIR]={0};
        for(int v=0;v<n;v++){
            int oi=(int)(q%NORD); q/=NORD;
            for(int e=0;e<NPAIR;e++) d[e]+=contrib[oi][e];
        }
        unsigned char S,R; ensure_cache(d,&S,&R);
        int ss=__builtin_popcount((unsigned)S), rs=__builtin_popcount((unsigned)R);
        hist[ss][rs][S==R]++;
        if(S!=R){
            (*diff)++;
            if(n==5){
                if((R & ~S)!=0 || (R==S)) {fprintf(stderr,"bad containment\n"); exit(4);} // R subset S
                int c[NPAIR]; canon_margin(d,c); int t=type_id(c);
                if(!t){fprintf(stderr,"unknown divergent margin type\n");exit(5);} typecnt[t]++;
            }
        }
    }
}

int main(void){
    int p[M]; nperm=0; genperm_rec(0,0,p);
    for(int i=0;i<NORD;i++) for(int j=0;j<M;j++) cperm[i][j]=orders[i][j];
    for(int oi=0;oi<NORD;oi++){
        for(int e=0;e<NPAIR;e++) contrib[oi][e]=(pos_in_order(oi,paira[e])<pos_in_order(oi,pairb[e]))?1:-1;
    }
    unsigned long long h1[5][5][2]={0},h3[5][5][2]={0},h5[5][5][2]={0};
    unsigned long long d1=0,d3=0,d5=0,tc[3]={0};
    enumerate_n(1,h1,&d1,tc); enumerate_n(3,h3,&d3,tc); enumerate_n(5,h5,&d5,tc);
    if(d1||d3||d5!=51840ULL) return 10;
    if(tc[1]!=11520ULL || tc[2]!=40320ULL) return 11;
    if(h5[1][1][1]!=6858144ULL || h5[2][2][1]!=275760ULL || h5[3][3][1]!=591120ULL ||
       h5[4][4][1]!=185760ULL || h5[3][2][0]!=51840ULL) return 12;
    printf("VERIFY_OK\n");
    printf("n1_diff %llu\n",d1);
    printf("n3_diff %llu\n",d3);
    printf("n5_profiles 7962624\n");
    printf("n5_diff %llu probability 5/768\n",d5);
    printf("n5_hist eq_1_1 %llu eq_2_2 %llu eq_3_3 %llu eq_4_4 %llu diff_S3_R2 %llu\n",
      h5[1][1][1],h5[2][2][1],h5[3][3][1],h5[4][4][1],h5[3][2][0]);
    printf("margin_type_A %llu canonical -3,-3,1,-1,-1,-1\n",tc[1]);
    printf("margin_type_B %llu canonical -3,-1,1,1,-1,-1\n",tc[2]);
    return 0;
}
