/* Independent coefficient-space exhaustive count for prime coefficient fields.
   Compile: cc -O3 -std=c11 -o check_prime_census check_prime_census.c
   Run: ./check_prime_census 21 2
   This does not use Fourier transforms or the arithmetic product formula.
*/
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int prime(int p) {
    if (p < 2) return 0;
    for (int d=2; d*d<=p; ++d) if (p%d == 0) return 0;
    return 1;
}

int main(int argc, char **argv) {
    if (argc!=3) { fprintf(stderr,"usage: %s odd_order prime_field_size\n",argv[0]); return 2; }
    int n=atoi(argv[1]), p=atoi(argv[2]);
    if (n<3 || n>25 || n%2==0 || !prime(p) || n%p==0) {
        fprintf(stderr,"expected odd n between 3 and 25 and prime p coprime to n\n"); return 2;
    }
    uint64_t cases=1;
    for(int i=0; i<n; ++i) {
        if(cases>100000000ULL/(uint64_t)p) {
            fprintf(stderr,"the full enumeration would exceed 100 million coefficient vectors\n"); return 2;
        }
        cases*=p;
    }
    int *a=calloc((size_t)n,sizeof(int)), *out=calloc((size_t)n,sizeof(int));
    if(!a || !out) { fprintf(stderr,"allocation failed\n"); return 2; }
    uint64_t count=0;
    for(uint64_t index=0; index<cases; ++index) {
        uint64_t t=index;
        for(int i=0; i<n; ++i) { a[i]=(int)(t%(uint64_t)p); t/=(uint64_t)p; out[i]=0; }
        for(int i=0; i<n; ++i) if(a[i])
            for(int j=0; j<n; ++j) if(a[j]) {
                int k=(2*j-i+n)%n;
                out[k]+=a[i]*a[j];
                out[k]%=p;
            }
        int okay=1;
        for(int i=0; i<n; ++i) if(out[i]!=a[i]) { okay=0; break; }
        count+=(uint64_t)okay;
    }
    printf("n=%d prime_field=%d elements=%" PRIu64 " idempotents=%" PRIu64 "\n",n,p,cases,count);
    free(a); free(out); return 0;
}
