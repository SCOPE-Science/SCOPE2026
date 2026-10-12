// Standalone exhaustive binary n=5 second-order covering lower-bound checker.
// Enumerates EVERY 17-element complement after normalizing one vertex to zero.
// Adding forbidden vertices cannot repair a failing pair; DFS safely prunes.
#include <stdint.h>
#include <stdio.h>
static unsigned long long nodes=0;
static int found=0;
static uint32_t witness=0;
static inline bool admissible(uint32_t forbidden){
    unsigned internal[32], vertices[32]; int k=0;
    for(uint32_t z=forbidden; z; z &= z-1){
        unsigned x=__builtin_ctz(z), mask=0;
        vertices[k++]=x;
        for(unsigned i=0;i<5;i++)mask |= ((forbidden>>(x^(1u<<i)))&1u)<<i;
        internal[x]=mask;
        if(mask==31)return false;
    }
    for(int a=0;a<k;a++)for(int b=a+1;b<k;b++)
        if((internal[vertices[a]]|internal[vertices[b]])==31)return false;
    return true;
}
static void enumerate(int next,uint32_t forbidden,int count){
    nodes++;
    if(count==17){found=1;witness=forbidden;return;}
    if(next==32||count+32-next<17)return;
    uint32_t with = forbidden | (1u<<next);
    if(admissible(with)){enumerate(next+1,with,count+1);if(found)return;}
    enumerate(next+1,forbidden,count);
}
int main(){
    enumerate(1,1u,1);
    if(found){printf("UNEXPECTED_COUNTEREXAMPLE %08x\n",witness);return 1;}
    if(nodes!=16829638ULL){printf("UNEXPECTED_NODES %llu\n",nodes);return 1;}
    printf("VERIFY_OK n=5: %llu exhaustive recursion nodes, no admissible 17-set\n",nodes);
    return 0;
}
