// Direct independent census in the generalized Petersen representation P(10,3).
// Compile: g++ -O2 -std=c++17 verify_gp.cpp -o verify_gp && ./verify_gp
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using U = unsigned;
int main() {
    std::array<U,20> neigh{};
    auto edge = [&](int a,int b){neigh[a] |= 1u << b; neigh[b] |= 1u << a;};
    for(int i=0; i<10; ++i) {
        edge(i,(i+1)%10); edge(i,i+10); edge(i+10,10+(i+3)%10);
    }
    constexpr U full=(1u<<20)-1;
    // Explicit isomorphism: 2-subsets first, then 3-subsets of {0,...,4},
    // in lexicographic order, mapped to P(10,3) vertex labels.
    constexpr std::array<int,20> map={0,2,13,19,11,17,8,4,15,6,1,10,9,3,12,16,14,18,7,5};
    U side=0; for(int i=0;i<10;i++)side|=1u<<map[i];
    // Reconstruct 2- and 3-subsets and check the stated isomorphism edge-by-edge.
    std::array<U,20> masks{}; int index=0;
    for(int a=0;a<5;a++)for(int b=a+1;b<5;b++) masks[index++]=(1u<<a)|(1u<<b);
    for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)for(int c=b+1;c<5;c++)
        masks[index++]=(1u<<a)|(1u<<b)|(1u<<c);
    assert(index==20);
    for(int i=0;i<20;i++)for(int j=0;j<20;j++){
        bool incident=__builtin_popcount(masks[i])!=__builtin_popcount(masks[j])
            && ((masks[i]&masks[j])==masks[i] || (masks[i]&masks[j])==masks[j]);
        bool adjacent=bool(neigh[map[i]] & (1u<<map[j]));
        assert(incident==adjacent);
    }
    unsigned good=0, unbalanced=0, checked=0;
    for(U s=0; s<=full; ++s) {
        if(__builtin_popcount(s)!=8)continue;
        ++checked;
        U black=s;
        for(;;){
            bool progress=false;
            for(int v=0;v<20;v++)if(black&(1u<<v)) {
                U w=neigh[v]&(~black)&full;
                if(w && (w&(w-1u))==0){black|=w;progress=true;break;}
            }
            if(!progress) break;
        }
        if(black==full) {good++;if(__builtin_popcount(s&side)!=4) unbalanced++;}
    }
    assert(checked==125970 && good==13520 && unbalanced==0);
    std::cout<<"VERIFY_OK GP(10,3) checked_8_subsets="<<checked
             <<" forcing_sets="<<good<<" all_4_plus_4="<<(unbalanced==0)<<"\n";
}
