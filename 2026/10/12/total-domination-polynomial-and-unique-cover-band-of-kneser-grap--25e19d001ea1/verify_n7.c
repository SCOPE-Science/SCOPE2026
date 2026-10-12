/* Exhaustive, independent cardinality check for KG(7,2), C99. */
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
int main(void) {
    const int n = 7;
    const uint64_t expected[22] = {
        0,0,0,105,1785,12432,45227,109455,200025,292775,352485,
        352695,293930,203490,116280,54264,20349,5985,1330,210,21,1
    };
    int m=0,u[21],v[21];
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) { u[m]=i;v[m]=j;++m; }
    uint32_t cover[21]; int count=0;
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) {
        uint32_t mask=0;
        for(int e=0;e<m;e++)
            if(u[e]==i || v[e]==i || u[e]==j || v[e]==j)
                mask |= 1u<<e;
        cover[count++]=mask;
    }
    uint64_t observed[22]={0};
    for(uint32_t mask=0;mask<(1u<<m);mask++) {
        int accepted=1;
        for(int i=0;i<count;i++) if((mask & ~cover[i])==0) {
            accepted=0;break;
        }
        if(accepted) observed[__builtin_popcount(mask)]++;
    }
    for(int k=0;k<=m;k++) if(observed[k]!=expected[k]) {
        fprintf(stderr,"FAIL k=%d observed=%"PRIu64" predicted=%"PRIu64"\n",
                k,observed[k],expected[k]);
        return 1;
    }
    puts("VERIFY_N7_OK all_2097152_subsets_and_22_coefficients");
    return 0;
}
