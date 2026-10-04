#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

#define N 5
#define NM 3125
#define NS (1<<N)

typedef struct { unsigned char x[N]; } Map;
typedef struct { Map a,b; } Pair;

static Map maps[NM];
static unsigned char img[NM][NS];
static uint64_t hist[16];
static Pair ext[512];
static int ext_n=0;

static int pc(unsigned x){ return __builtin_popcount(x); }

static void init_maps(void){
    for(int z=0; z<NM; ++z){
        int t=z;
        for(int i=0;i<N;i++){ maps[z].x[i]=(unsigned char)(t%N); t/=N; }
        for(int s=0;s<NS;s++){
            unsigned r=0;
            for(int i=0;i<N;i++) if(s&(1<<i)) r |= 1u<<maps[z].x[i];
            img[z][s]=(unsigned char)r;
        }
    }
}

/* Distances from subsets to a singleton under the two maps, via reverse BFS.
   Returns m_3 if the full state set synchronizes, else -1. */
static int m3_for_pair(int ia,int ib){
    int pred_head[NS], next[2*NS], from[2*NS];
    int ec=0;
    for(int i=0;i<NS;i++) pred_head[i]=-1;
    for(int s=1;s<NS;s++){
        int t=img[ia][s]; from[ec]=s; next[ec]=pred_head[t]; pred_head[t]=ec++;
        t=img[ib][s]; from[ec]=s; next[ec]=pred_head[t]; pred_head[t]=ec++;
    }
    signed char d[NS]; memset(d,-1,sizeof(d));
    unsigned char q[NS]; int qh=0,qt=0;
    for(int i=0;i<N;i++){ int s=1<<i; d[s]=0; q[qt++]=(unsigned char)s; }
    while(qh<qt){
        int t=q[qh++];
        for(int e=pred_head[t]; e!=-1; e=next[e]){
            int s=from[e];
            if(d[s]<0){ d[s]=d[t]+1; q[qt++]=(unsigned char)s; }
        }
    }
    if(d[NS-1]<0) return -1;
    int best=100;
    for(int s=1;s<NS;s++) if(pc((unsigned)s)==3 && d[s]<best) best=d[s];
    return best;
}

static uint64_t encode_pair(const Pair *p){
    uint64_t z=0,mul=1;
    for(int i=0;i<N;i++){ z += p->a.x[i]*mul; mul*=N; }
    for(int i=0;i<N;i++){ z += p->b.x[i]*mul; mul*=N; }
    return z;
}

static Pair relabel(const Pair *p, const int perm[N], int swap){
    /* perm maps old labels to new labels. Conjugate t to perm o t o perm^{-1}. */
    int inv[N]; for(int i=0;i<N;i++) inv[perm[i]]=i;
    Pair r;
    const Map *u = swap ? &p->b : &p->a;
    const Map *v = swap ? &p->a : &p->b;
    for(int j=0;j<N;j++){
        int old=inv[j]; r.a.x[j]=(unsigned char)perm[u->x[old]]; r.b.x[j]=(unsigned char)perm[v->x[old]];
    }
    return r;
}

static void next_perm(int *a,int n,int *ok){
    int i=n-2; while(i>=0 && a[i]>a[i+1]) i--;
    if(i<0){*ok=0;return;} int j=n-1; while(a[j]<a[i]) j--;
    int t=a[i];a[i]=a[j];a[j]=t;
    for(int l=i+1,r=n-1;l<r;l++,r--){t=a[l];a[l]=a[r];a[r]=t;}
}

static uint64_t canonical(const Pair *p, Pair *bestp){
    uint64_t best=UINT64_MAX; Pair bp=*p;
    for(int sw=0;sw<2;sw++){
        int perm[N]={0,1,2,3,4},ok=1;
        while(ok){
            Pair r=relabel(p,perm,sw); uint64_t c=encode_pair(&r);
            if(c<best){best=c;bp=r;}
            next_perm(perm,N,&ok);
        }
    }
    if(bestp) *bestp=bp;
    return best;
}

static int subset_image_map(const Map *m,int s){ int r=0; for(int i=0;i<N;i++) if(s&(1<<i)) r|=1<<m->x[i]; return r; }

/* Forward BFS from a given subset; choose lexicographically a-before-b among shortest words. */
static int shortest_merge_word(const Pair *p,int start,char *out){
    int dist[NS],par[NS]; char edge[NS]; for(int i=0;i<NS;i++){dist[i]=-1;par[i]=-1;edge[i]=0;}
    int q[NS],qh=0,qt=0; dist[start]=0;q[qt++]=start; int goal=-1;
    while(qh<qt){ int s=q[qh++]; if(pc((unsigned)s)==1){goal=s;break;}
        int ts[2]={subset_image_map(&p->a,s),subset_image_map(&p->b,s)};
        for(int k=0;k<2;k++) if(dist[ts[k]]<0){dist[ts[k]]=dist[s]+1;par[ts[k]]=s;edge[ts[k]]=(char)('a'+k);q[qt++]=ts[k];}
    }
    if(goal<0) return -1;
    int L=dist[goal]; out[L]=0; int cur=goal;
    for(int i=L-1;i>=0;i--){out[i]=edge[cur];cur=par[cur];} return L;
}

static int reset_word(const Pair *p,char *out){ return shortest_merge_word(p,NS-1,out); }

int main(void){
    init_maps();
    uint64_t sync=0; int maxm=-1;
    for(int ia=0;ia<NM;ia++) for(int ib=0;ib<NM;ib++){
        int m=m3_for_pair(ia,ib); if(m<0) continue; sync++; hist[m]++;
        if(m>maxm){maxm=m;ext_n=0;}
        if(m==maxm && m>=0){
            if(ext_n<(int)(sizeof(ext)/sizeof(ext[0]))){ext[ext_n].a=maps[ia]; ext[ext_n].b=maps[ib]; ext_n++;}
        }
    }
    /* Because max can increase late, ext[] above contains only pairs seen after the last max increase.
       Re-enumerate to collect all maximum pairs exactly. */
    ext_n=0;
    for(int ia=0;ia<NM;ia++) for(int ib=0;ib<NM;ib++){
        int m=m3_for_pair(ia,ib); if(m==maxm){ ext[ext_n].a=maps[ia]; ext[ext_n].b=maps[ib]; ext_n++; }
    }

    uint64_t cans[512]; int can_n=0; Pair canon_rep=ext[0]; uint64_t minc=UINT64_MAX;
    for(int i=0;i<ext_n;i++){
        Pair bp; uint64_t c=canonical(&ext[i],&bp); if(c<minc){minc=c;canon_rep=bp;}
        int seen=0; for(int j=0;j<can_n;j++) if(cans[j]==c){seen=1;break;} if(!seen)cans[can_n++]=c;
    }
    /* orbit of canonical representative */
    uint64_t orbit[512]; int orbit_n=0;
    for(int sw=0;sw<2;sw++){
        int perm[N]={0,1,2,3,4},ok=1;
        while(ok){ Pair r=relabel(&canon_rep,perm,sw); uint64_t c=encode_pair(&r); int seen=0; for(int j=0;j<orbit_n;j++)if(orbit[j]==c){seen=1;break;} if(!seen)orbit[orbit_n++]=c; next_perm(perm,N,&ok); }
    }

    printf("TOTAL_PAIRS %d\n", NM*NM);
    printf("SYNCHRONIZING %llu\n",(unsigned long long)sync);
    printf("M3_HIST"); for(int i=0;i<=maxm;i++) if(hist[i]) printf(" %d:%llu",i,(unsigned long long)hist[i]); printf("\n");
    printf("MAX_M3 %d\n",maxm);
    printf("EXTREMAL_ORDERED %d\n",ext_n);
    printf("EXTREMAL_ORBITS %d\n",can_n);
    printf("CANONICAL_A"); for(int i=0;i<N;i++)printf("%s%d",i?",":" ",canon_rep.a.x[i]);printf("\n");
    printf("CANONICAL_B"); for(int i=0;i<N;i++)printf("%s%d",i?",":" ",canon_rep.b.x[i]);printf("\n");
    printf("CANONICAL_ORBIT_SIZE %d\n",orbit_n);
    char w[128]; int rl=reset_word(&canon_rep,w); printf("RESET %d %s\n",rl,w);
    for(int s=1;s<NS;s++) if(pc((unsigned)s)==3){ int L=shortest_merge_word(&canon_rep,s,w); printf("TRIPLE"); for(int i=0;i<N;i++)if(s&(1<<i))printf(" %d",i); printf(" %d %s\n",L,w); }
    return 0;
}
