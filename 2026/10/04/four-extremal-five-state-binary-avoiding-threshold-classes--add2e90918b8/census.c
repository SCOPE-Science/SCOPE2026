#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define N 5
#define NF 3125
#define NS 32

static uint8_t tr[NF][N];
static uint8_t im[NF][NS];

static void init_tables(void){
    for(int f=0; f<NF; ++f){
        int x=f;
        for(int q=0;q<N;q++){ tr[f][q]=(uint8_t)(x%N); x/=N; }
        for(int s=0;s<NS;s++){
            int t=0;
            for(int q=0;q<N;q++) if(s&(1<<q)) t |= 1<<tr[f][q];
            im[f][s]=(uint8_t)t;
        }
    }
}

static int is_singleton(int s){ return s && !(s&(s-1)); }

/* BFS in the power automaton from Q.  distq[q] is the first layer
   containing a reachable subset that omits q, or -1 if q is unavoidably present. */
static int power_stats(int a,int b,int distq[N]){
    int dist[NS]; uint8_t queue[NS];
    for(int i=0;i<NS;i++) dist[i]=-1;
    for(int q=0;q<N;q++) distq[q]=-1;
    int h=0,t=0,sync=0;
    queue[t++]=31; dist[31]=0;
    while(h<t){
        int s=queue[h++], d=dist[s];
        if(is_singleton(s)) sync=1;
        for(int q=0;q<N;q++) if(distq[q]<0 && !(s&(1<<q))) distq[q]=d;
        int u=im[a][s], v=im[b][s];
        if(dist[u]<0){dist[u]=d+1; queue[t++]=(uint8_t)u;}
        if(dist[v]<0){dist[v]=d+1; queue[t++]=(uint8_t)v;}
    }
    return sync;
}

static int threshold(int a,int b){
    int d[N]; if(!power_stats(a,b,d)) return -1;
    int m=0; for(int q=0;q<N;q++) if(d[q]>m) m=d[q];
    return m;
}

static int encode(const uint8_t f[N]){
    int x=0,p=1; for(int q=0;q<N;q++){x+=f[q]*p;p*=N;} return x;
}

static void canonical(int a,int b,int *ca,int *cb){
    int p[N]={0,1,2,3,4};
    int besta=NF+1,bestb=NF+1;
    while(1){
        int inv[N]; for(int i=0;i<N;i++) inv[p[i]]=i;
        uint8_t fa[N],fb[N];
        for(int j=0;j<N;j++){
            fa[j]=p[tr[a][inv[j]]];
            fb[j]=p[tr[b][inv[j]]];
        }
        int ea=encode(fa),eb=encode(fb);
        if(ea<besta || (ea==besta && eb<bestb)){besta=ea;bestb=eb;}
        if(eb<besta || (eb==besta && ea<bestb)){besta=eb;bestb=ea;}
        int i=N-2; while(i>=0 && p[i]>=p[i+1]) i--;
        if(i<0) break;
        int j=N-1; while(p[j]<=p[i]) j--;
        int z=p[i];p[i]=p[j];p[j]=z;
        for(int l=i+1,r=N-1;l<r;l++,r--){z=p[l];p[l]=p[r];p[r]=z;}
    }
    *ca=besta; *cb=bestb;
}

int main(void){
    init_tables();
    long long sync_count=0,hist[16]={0},ext_count=0;
    int maxthr=-1;
    int cap=1024, ne=0;
    int *ea=(int*)malloc(cap*sizeof(int)), *eb=(int*)malloc(cap*sizeof(int));
    if(!ea||!eb) return 2;

    for(int a=0;a<NF;a++) for(int b=0;b<NF;b++){
        int th=threshold(a,b);
        if(th<0) continue;
        sync_count++;
        if(th<16) hist[th]++;
        if(th>maxthr){maxthr=th;ext_count=0;ne=0;}
        if(th==maxthr){
            ext_count++;
            if(ne==cap){cap*=2;ea=(int*)realloc(ea,cap*sizeof(int));eb=(int*)realloc(eb,cap*sizeof(int)); if(!ea||!eb) return 3;}
            ea[ne]=a;eb[ne]=b;ne++;
        }
    }

    int repa[16],repb[16],repc[16],nr=0;
    for(int i=0;i<ne;i++){
        int ca,cb; canonical(ea[i],eb[i],&ca,&cb);
        int j; for(j=0;j<nr;j++) if(repa[j]==ca && repb[j]==cb){repc[j]++;break;}
        if(j==nr){repa[nr]=ca;repb[nr]=cb;repc[nr]=1;nr++;}
    }

    /* sort representatives by (encoded a, encoded b) for deterministic output */
    for(int i=0;i<nr;i++) for(int j=i+1;j<nr;j++)
        if(repa[j]<repa[i] || (repa[j]==repa[i] && repb[j]<repb[i])){
            int z=repa[i];repa[i]=repa[j];repa[j]=z;
            z=repb[i];repb[i]=repb[j];repb[j]=z;
            z=repc[i];repc[i]=repc[j];repc[j]=z;
        }

    printf("ordered_pairs=%d\n",NF*NF);
    printf("synchronizing=%lld\n",sync_count);
    printf("max_1_avoiding_threshold=%d\n",maxthr);
    printf("extremal_ordered_labeled=%lld\n",ext_count);
    for(int d=0;d<16;d++) if(hist[d]) printf("hist_%d=%lld\n",d,hist[d]);
    printf("extremal_orbits=%d\n",nr);
    for(int r=0;r<nr;r++){
        int d[N]; power_stats(repa[r],repb[r],d);
        printf("orbit_%d_count=%d a=(%d,%d,%d,%d,%d) b=(%d,%d,%d,%d,%d) avoid=(%d,%d,%d,%d,%d)\n",
            r+1,repc[r],
            tr[repa[r]][0],tr[repa[r]][1],tr[repa[r]][2],tr[repa[r]][3],tr[repa[r]][4],
            tr[repb[r]][0],tr[repb[r]][1],tr[repb[r]][2],tr[repb[r]][3],tr[repb[r]][4],
            d[0],d[1],d[2],d[3],d[4]);
    }
    free(ea);free(eb);return 0;
}
