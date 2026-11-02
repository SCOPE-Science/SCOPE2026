#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

// Directly evaluates successive local threshold updates of the physical graph.
static uint32_t sweep(uint32_t x, int n) {
    for(int i=0;i<n;++i) {
        const int left = (x >> ((i+n-1)%n))&1;
        const int self = (x >> i)&1;
        const int right = (x >> ((i+1)%n))&1;
        const int after = (left+self+right >= (self ? 3 : 1));
        if(after) x |= uint32_t(1)<<i;
        else x &= ~(uint32_t(1)<<i);
    }
    return x;
}
static int predicted_preimages(uint32_t y,int n) {
    const int a=y&1;
    if(int((y>>(n-2))&1)!=a) return 1;
    for(int i=1;i<n-2;i++)
        if(int((y>>i)&1)!=a) return i+1;
    return n;
}
static uint32_t rotation(uint32_t y,int n) {
    const uint32_t mask=(uint32_t(1)<<(n-1))-1;
    uint32_t a=((y>>1)&mask)|((y&1)<<(n-2));
    return a|((a&1)<<(n-1));
}
int main(){
    for(int n=3;n<=18;n++) {
        const uint32_t num=uint32_t(1)<<n;
        vector<uint32_t> next(num);
        vector<uint32_t> count(num,0);
        int distinct=0;
        for(uint32_t x=0;x<num;x++) {
            uint32_t y=sweep(x,n);
            next[x]=y;
            if(!count[y])++distinct;
            count[y]++;
        }
        assert(distinct==int(num/2));
        for(uint32_t x=0;x<num;x++){
            const bool inS=((x&1)==((x>>(n-1))&1));
            if(inS){
                assert(next[x]==rotation(x,n));
                assert(count[x]==(unsigned)predicted_preimages(x,n));
            } else assert(count[x]==0);
            assert(next[next[x]]==rotation(next[x],n));
        }
        vector<int> marked(num,0); map<int,int> census;
        uint64_t allbasins=0;
        for(uint32_t x=0;x<num;x++){
            if(!count[x] || marked[x])continue;
            uint32_t cur=x; int length=0, basin=0;
            do{
                assert(!marked[cur]);marked[cur]=1;
                ++length;basin+=count[cur];cur=next[cur];
            }while(cur!=x);
            assert((n-1)%length==0);
            census[length]++;
            allbasins+=basin;
        }
        assert(allbasins==num);
        assert(census[1]==2);
        printf("n=%d states=%u recurrent=%d cycles=%d basin_total=%llu\n",n,num,distinct, [&](){int z=0;for(auto &p:census)z+=p.second;return z;}(), (unsigned long long)allbasins);
    }
    puts("PASS: orbit structure and preimage formulas match independent direct updates.");
}
