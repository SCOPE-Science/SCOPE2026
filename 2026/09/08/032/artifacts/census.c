#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static uint64_t gg(uint64_t a, uint64_t b){ while(b){uint64_t t=a%b;a=b;b=t;} return a; }

int main(void){
    const int N = 5000000;
    int *spf = malloc(((size_t)N+1)*sizeof(int));
    if(!spf){fprintf(stderr,"oom\n");return 1;}
    for(int i=0;i<=N;i++) spf[i]=i;
    for(int i=2;(int64_t)i*i<=N;i++) if(spf[i]==i)
        for(int64_t j=(int64_t)i*i;j<=N;j+=i) if(spf[(int)j]==(int)j) spf[(int)j]=i;
    uint64_t total_comp=0;
    long least[11]; for(int k=0;k<=10;k++) least[k]=-1;
    int *freq = calloc((size_t)N+1, sizeof(int));
    long long maxm=-1; long maxn=-1; long maxlam=-1; long maxkmin=-1;
    for(int n=4;n<=N;n++){
        if(spf[n]==n) continue;
        total_comp++;
        int x=n;
        uint64_t lam=1;
        while(x>1){
            int p=spf[x]; int e=0;
            while(x%p==0){x/=p;e++;}
            uint64_t pw;
            if(p==2){
                if(e==1) pw=1;
                else if(e==2) pw=2;
                else pw=(1ULL<<(e-2));
            } else {
                uint64_t pe=1; for(int i=0;i<e-1;i++) pe*=(uint64_t)p;
                pw=pe*(uint64_t)(p-1);
            }
            uint64_t g=gg(lam,pw);
            lam=lam/g*pw;
        }
        uint64_t m=(uint64_t)(n-1)/lam;
        uint64_t kmin=(uint64_t)n - m*lam;
        freq[m]++;
        if((long long)m>maxm){maxm=m;maxn=n;maxlam=(long)lam;maxkmin=(long)kmin;}
        for(int k=1;k<=10;k++) if(least[k]<0 && n>k && ((uint64_t)(n-k))%lam==0) least[k]=n;
    }
    printf("total_composites=%llu\n", (unsigned long long)total_comp);
    printf("maxm=%lld n*=%ld lambda=%ld kmin=%ld\n", maxm, maxn, maxlam, maxkmin);
    uint64_t mhist_cap=0;
    for(int i=0;i<=N;i++) if(freq[i]) mhist_cap=i;
    printf("m_range_max=%llu\n",(unsigned long long)mhist_cap);
    int distinct=0; uint64_t sum=0;
    for(uint64_t i=0;i<=N;i++){ if(freq[i]){distinct++; sum+=freq[i];} }
    printf("distinct_m=%d sum=%llu\n", distinct, (unsigned long long)sum);
    FILE *f=fopen("mhist.csv","w");
    for(uint64_t i=0;i<=N;i++) if(freq[i]) fprintf(f,"%llu,%d\n",(unsigned long long)i, freq[i]);
    fclose(f);
    FILE *g1=fopen("c1_list.txt","w"), *g3=fopen("c3_list.txt","w");
    uint64_t c1=0,c3=0;
    for(int n=4;n<=N;n++){
        if(spf[n]==n) continue;
        int x=n; uint64_t lam=1;
        while(x>1){ int p=spf[x],e=0; while(x%p==0){x/=p;e++;}
            uint64_t pw;
            if(p==2){ if(e==1)pw=1; else if(e==2)pw=2; else pw=(1ULL<<(e-2)); }
            else { uint64_t pe=1; for(int i=0;i<e-1;i++)pe*=(uint64_t)p; pw=pe*(uint64_t)(p-1); }
            uint64_t g2=gg(lam,pw); lam=lam/g2*pw; }
        if(((uint64_t)(n-1))%lam==0){ c1++; if(c1<=40) fprintf(g1,"%d\n",n); }
        if(n>3 && ((uint64_t)(n-3))%lam==0){ c3++; if(c3<=40) fprintf(g3,"%d\n",n); }
    }
    fclose(g1); fclose(g3);
    printf("C1_count=%llu\n",(unsigned long long)c1);
    printf("C3_count=%llu\n",(unsigned long long)c3);
    for(int k=1;k<=10;k++) printf("least_C%d=%ld\n",k,least[k]);
    printf("factor_n*:");
    { int x=(int)maxn; while(x>1){int p=spf[x],e=0;while(x%p==0){x/=p;e++;} printf(" %d^%d",p,e);} printf("\n"); }
    free(spf); free(freq);
    return 0;
}
