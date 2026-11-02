#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static uint64_t valid_indexed(int k){
    int n=1+k+k*(k-1)/2;
    assert(n<=29);
    uint64_t count=0;
    uint64_t x=(1ULL<<k)-1;
    while(x<(1ULL<<n)){
        uint64_t ext=(x<<k)|(x>>(n-k));
        bool seen[128]={false};
        bool good=true;
        for(int pos=0;pos<n;++pos){
            unsigned w=(ext>>pos)&((1U<<k)-1);
            if(__builtin_popcount(w)>2 || seen[w]) {good=false;break;}
            seen[w]=true;
        }
        if(good) ++count;
        uint64_t c=x&-x, r=x+c;
        x=(((r^x)>>2)/c)|r;
    }
    assert(count%n==0);
    return count/n;
}
int main(){
    for(int k=2;k<=7;++k){
        uint64_t actual=valid_indexed(k), expected=1ULL<<((k-1)/2);
        cout<<"CIRCULAR_WEIGHT_FILTER "<<k<<" "<<actual<<"\n";
        assert(actual==expected);
    }
    cout<<"VERIFY_LARGE_OK\n";
}
