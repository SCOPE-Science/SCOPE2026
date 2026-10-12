#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static int N, M;
static uint64_t compm[63], supm[64];
static int subset_of_v[63];
static uint64_t total, divcnt, propercnt, properdiv, nodummydiv;
static uint64_t revgames, ss_split, bz_split;
static unsigned long long factv[7] = {1,1,2,6,24,120,720};

static inline int popc32(unsigned x){ return __builtin_popcount(x); }

static int is_proper_by_winners(uint64_t W){
    unsigned full = (1U<<N)-1U;
    for(unsigned S=0; S<(1U<<N); S++){
        if(((W>>S)&1ULL) && ((W>>(full^S))&1ULL)) return 0;
    }
    return 1;
}

static int is_proper_by_minwins(uint64_t chosen){
    int vals[63], k=0;
    for(int v=0; v<M; v++) if((chosen>>v)&1ULL) vals[k++]=subset_of_v[v];
    for(int i=0;i<k;i++) for(int j=i+1;j<k;j++) if((vals[i]&vals[j])==0) return 0;
    return 1;
}

static void process(uint64_t W, uint64_t chosen){
    total++;
    unsigned long long bz[6]={0,0,0,0,0,0};
    unsigned long long ss[6]={0,0,0,0,0,0};
    for(int i=0;i<N;i++){
        unsigned bi=1U<<i;
        for(unsigned S=0; S<(1U<<N); S++) if(!(S&bi)){
            if(!((W>>S)&1ULL) && ((W>>(S|bi))&1ULL)){
                int k=popc32(S);
                bz[i]++;
                ss[i]+=factv[k]*factv[N-k-1];
            }
        }
    }
    int div=0, hasrev=0, hasss=0, hasbz=0;
    for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){
        int b=(bz[i]>bz[j])-(bz[i]<bz[j]);
        int s=(ss[i]>ss[j])-(ss[i]<ss[j]);
        if(b!=s){
            div=1;
            if(b && s && b==-s) hasrev=1;
            else if(b==0 && s!=0) hasss=1;
            else if(s==0 && b!=0) hasbz=1;
        }
    }
    int p1=is_proper_by_winners(W);
    int p2=is_proper_by_minwins(chosen);
    if(p1!=p2){ fprintf(stderr,"properness cross-check failed\n"); exit(2); }
    if(p1) propercnt++;
    if(div){
        divcnt++;
        if(p1) properdiv++;
        if(hasrev) revgames++;
        if(hasss) ss_split++;
        if(hasbz) bz_split++;
        int nodummy=1;
        for(int i=0;i<N;i++) if(bz[i]==0) nodummy=0;
        if(nodummy) nodummydiv++;
    }
}

static void rec(uint64_t cand, uint64_t chosen, uint64_t W){
    if(!cand){ if(chosen) process(W,chosen); return; }
    int v=__builtin_ctzll(cand);
    uint64_t bit=1ULL<<v;
    rec(cand^bit, chosen, W);
    rec((cand^bit)&~compm[v], chosen|bit, W|supm[subset_of_v[v]]);
}

static void setup_and_run(int n){
    N=n; M=(1<<n)-1;
    memset(compm,0,sizeof(compm)); memset(supm,0,sizeof(supm)); memset(subset_of_v,0,sizeof(subset_of_v));
    total=divcnt=propercnt=properdiv=nodummydiv=0;
    revgames=ss_split=bz_split=0;
    int arr[63], deg[64];
    unsigned lim=1U<<n;
    for(int s=1;s<(int)lim;s++){
        int d=0;
        for(int t=1;t<(int)lim;t++) if(t!=s && (((s&t)==s)||((s&t)==t))) d++;
        deg[s]=d; arr[s-1]=s;
        uint64_t u=0;
        for(unsigned T=0;T<lim;T++) if((T&(unsigned)s)==(unsigned)s) u|=1ULL<<T;
        supm[s]=u;
    }
    for(int i=0;i<M;i++) for(int j=i+1;j<M;j++) if(deg[arr[j]]>deg[arr[i]]){
        int z=arr[i]; arr[i]=arr[j]; arr[j]=z;
    }
    for(int v=0;v<M;v++) subset_of_v[v]=arr[v];
    for(int i=0;i<M;i++){
        int s=arr[i]; uint64_t mask=0;
        for(int j=0;j<M;j++) if(i!=j){
            int t=arr[j];
            if(((s&t)==s)||((s&t)==t)) mask|=1ULL<<j;
        }
        compm[i]=mask;
    }
    uint64_t cand = (M==64) ? ~0ULL : ((1ULL<<M)-1ULL);
    rec(cand,0,0);
}

static uint64_t winners_from_minwins(const int *fam, int nf, int n){
    uint64_t W=0; unsigned lim=1U<<n;
    for(int j=0;j<nf;j++) for(unsigned S=0;S<lim;S++) if((S&(unsigned)fam[j])==(unsigned)fam[j]) W|=1ULL<<S;
    return W;
}

static void verify_witness(void){
    const int fam[4]={7,27,57,58}; /* ABC, ABDE, ADEF, BDEF */
    const int expected_bz[6]={10,10,6,6,6,4};
    const int expected_ss_num[6]={168,168,96,108,108,72};
    const int expected_spec[6][6]={
        {0,0,1,5,4,0},
        {0,0,1,5,4,0},
        {0,0,1,3,2,0},
        {0,0,0,3,3,0},
        {0,0,0,3,3,0},
        {0,0,0,2,2,0}
    };
    uint64_t W=winners_from_minwins(fam,4,6);
    if(!is_proper_by_winners(W)){ fprintf(stderr,"witness not proper\n"); exit(3); }
    int bz[6]={0}, ssnum[6]={0}, spec[6][6]={{0}};
    for(int i=0;i<6;i++){
        unsigned bi=1U<<i;
        for(unsigned S=0;S<64;S++) if(!(S&bi)){
            if(!((W>>S)&1ULL) && ((W>>(S|bi))&1ULL)){
                int k=popc32(S); bz[i]++; spec[i][k]++;
                ssnum[i]+=(int)(factv[k]*factv[5-k]);
            }
        }
    }
    for(int i=0;i<6;i++){
        if(bz[i]!=expected_bz[i] || ssnum[i]!=expected_ss_num[i]){ fprintf(stderr,"witness value mismatch\n"); exit(4); }
        for(int k=0;k<6;k++) if(spec[i][k]!=expected_spec[i][k]){ fprintf(stderr,"witness spectrum mismatch\n"); exit(5); }
    }
    /* C and D are incomparable in desirability: AB+C wins but AB+D loses; AEF+D wins but AEF+C loses. */
    unsigned AB=(1U<<0)|(1U<<1), AEF=(1U<<0)|(1U<<4)|(1U<<5);
    unsigned C=1U<<2, D=1U<<3;
    if(!((W>>(AB|C))&1ULL) || ((W>>(AB|D))&1ULL)) exit(6);
    if(!((W>>(AEF|D))&1ULL) || ((W>>(AEF|C))&1ULL)) exit(7);
}

int main(void){
    const uint64_t expect_total[7]={0,1,4,18,166,7579,7828352};
    const uint64_t expect_div[7]={0,0,0,0,0,0,2540340};
    for(int n=1;n<=6;n++){
        setup_and_run(n);
        if(total!=expect_total[n] || divcnt!=expect_div[n]){
            fprintf(stderr,"count mismatch n=%d total=%llu div=%llu\n",n,(unsigned long long)total,(unsigned long long)divcnt); return 10;
        }
        if(n<6 && (revgames||ss_split||bz_split)) return 11;
        if(n==6){
            if(propercnt!=1422563ULL || properdiv!=573960ULL) return 12;
            if(revgames!=0 || ss_split!=2540340ULL || bz_split!=0) return 13;
            if(nodummydiv!=2540340ULL) return 14;
        }
        printf("n=%d total=%llu divergent=%llu proper=%llu proper_divergent=%llu\n",
            n,(unsigned long long)total,(unsigned long long)divcnt,
            (unsigned long long)propercnt,(unsigned long long)properdiv);
    }
    verify_witness();
    printf("VERIFY_OK\n");
    printf("n6_relation_type: every divergence is a strict Shapley-Shubik refinement of a Banzhaf tie; reversals=0; Banzhaf-only splits=0\n");
    printf("n6_dummy_free_divergences=2540340\n");
    printf("witness_minimal_winners=ABC,ABDE,ADEF,BDEF\n");
    printf("witness_raw_banzhaf=10,10,6,6,6,4\n");
    printf("witness_shapley_numerators_over_720=168,168,96,108,108,72\n");
    return 0;
}
