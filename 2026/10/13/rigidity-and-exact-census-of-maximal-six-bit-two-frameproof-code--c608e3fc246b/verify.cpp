#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using Word = unsigned;
using Mask = uint64_t;
Mask banned[64][64];
long long nodes8=0,nodes9=0;
set<array<Word,8>> found8;
static bool exposed(Word victim,Word a,Word b) {
    return (((a^victim)&(b^victim)) != 0);
}
void enumerate(Mask candidates, vector<Word>& code,int target) {
    if(target==8)++nodes8; else ++nodes9;
    if((int)code.size()==target) {
        if(target==8) {
            array<Word,8> arr{};
            for(unsigned i=0;i<8;i++)arr[i]=code[i];
            found8.insert(arr);
        } else throw 1;
        return;
    }
    if(__builtin_popcountll(candidates)<target-(int)code.size())return;
    while(candidates) {
        auto w=(Word)__builtin_ctzll(candidates);
        candidates &= candidates-1;
        Mask next=candidates;
        for(auto x:code)next &= ~banned[w][x];
        code.push_back(w);
        enumerate(next,code,target);
        code.pop_back();
    }
}
int main() {
    for(Word a=0;a<64;a++)for(Word b=0;b<64;b++)for(Word c=0;c<64;c++) {
        if(a==b || b==c || c==a)continue;
        if(!(exposed(a,b,c)&&exposed(b,a,c)&&exposed(c,a,b)))banned[a][b]|=(Mask(1)<<c);
    }
    vector<Word> code{0};
    try {enumerate(~Mask(1),code,8);enumerate(~Mask(1),code,9);}
    catch(int) {cerr<<"Unexpected nine-word code\n"; return 1;}
    if(found8.size()!=30){cerr<<"Unexpected count: "<<found8.size()<<"\n";return 1;}
    for(const auto& C:found8) {
        for(auto a:C)for(auto b:C){
            bool has=false;for(auto c:C)if(c==(a^b))has=true;
            if(!has){cerr<<"Nonlinear code\n";return 1;}
        }
    }
    cout<<"VERIFY_OK zero_containing=30 max=8 all_linear=true nodes8="<<nodes8<<" nodes9="<<nodes9<<"\n";
}
