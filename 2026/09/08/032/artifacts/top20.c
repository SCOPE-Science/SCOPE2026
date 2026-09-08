#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// Independent pass: trial-division factorization (no spf), top-20 by m, plus threshold counts.
static uint64_t gg(uint64_t a, uint64_t b){ while(b){uint64_t t=a%b;a=b;b=t;} return a; }
static uint64_t lam_of(int n, int *pr, int np){
    int x=n; uint64_t lam=1; int tmp=x;
    for(int i=0;i<np && (int64_t)pr[i]*pr[i]<=tmp;i++){
        int p=pr[i]; if(tmp%p) continue; int e=0;
        while(tmp%p==0){tmp/=p;e++;}
        uint64_t pw;
        if(p==2){ if(e==1)pw=1; else if(e==2)pw=2; else pw=(1ULL<<(e-2)); }
        else { uint64_t pe=1; for(int j=0;j<e-1;j++)pe*=(uint64_t)p; pw=pe*(uint64_t)(p-1); }
        uint64_t g=gg(lam,pw); lam=lam/g*pw;
    }
    if(tmp>1){ uint64_t pw=(uint64_t)(tmp-1); uint64_t g=gg(lam,pw); lam=lam/g*pw; }
    return lam;
}
int main(void){
    const int N=5000000;
    // prime list to 3000 via simple sieve
    static char is[3000]; for(int i=2;i<3000;i++) is[i]=1;
    for(int i=2;i*i<3000;i++) if(is[i]) for(int j=i*i;j<3000;j+=i) is[j]=0;
    int pr[500]; int np=0; for(int i=2;i<3000;i++) if(is[i]) pr[np++]=i;
    // primality test needs primes to sqrt(5M)=2237 <3000 ok
    long topn[20]; long long topm[20]; long topl[20];
    for(int i=0;i<20;i++){topn[i]=-1;topm[i]=-1;topl[i]=-1;}
    uint64_t c1=0; long long maxm=-1; long maxn=-1;
    for(int n=4;n<=N;n++){
        int prime=1;
        for(int i=0;i<np && (int64_t)pr[i]*pr[i]<=n;i++) if(n%pr[i]==0){prime=0;break;}
        if(prime) continue;
        uint64_t lam=lam_of(n,pr,np);
        uint64_t m=(uint64_t)(n-1)/lam;
        if(((uint64_t)(n-1))%lam==0) c1++;
        if((long long)m>maxm){maxm=m;maxn=n;}
        if((long long)m>topm[19]){
            int k=19; while(k>0 && (long long)m>topm[k-1]){topm[k]=topm[k-1];topn[k]=topn[k-1];topl[k]=topl[k-1];k--;}
            topm[k]=m;topn[k]=n;topl[k]=(long)lam;
        }
    }
    printf("maxm=%lld maxn=%ld c1=%llu\n",maxm,maxn,(unsigned long long)c1);
    for(int i=0;i<20;i++) printf("top%d: n=%ld m=%lld lam=%ld\n",i+1,topn[i],topm[i],topl[i]);
    return 0;
}
