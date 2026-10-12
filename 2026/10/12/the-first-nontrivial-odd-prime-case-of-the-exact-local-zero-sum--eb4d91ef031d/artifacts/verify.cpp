// Exact exhaustive residue-multiset verification for the five-term local zero-sum invariant.
// g++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <iostream>
using namespace std;
constexpr int N=5, P2=25, L=11;
constexpr uint32_t MASK=(1u<<25)-1;
constexpr uint32_t TARGET=(1u<<5)|(1u<<10)|(1u<<15)|(1u<<20);
const int RES[20]={1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24};
uint64_t count_by_length[L+1]={};
array<int,L> witness={};
array<int,10> first_bad10={};
bool have_witness=false;
uint32_t shift25(uint32_t v,int r){return ((v<<r)|(v>>(25-r)))&MASK;}
void traverse(int start,int depth,const array<uint32_t,N+1>& have){
    ++count_by_length[depth];
    if(depth==10&&!have_witness){
        for(int i=0;i<10;++i)first_bad10[i]=witness[i];
        have_witness=true;
    }
    if(depth==L)return;
    for(int i=start;i<20;++i){
        array<uint32_t,N+1> next=have;
        for(int j=N;j>0;--j)next[j]|=shift25(have[j-1],RES[i]);
        if(next[N]&TARGET)continue;
        witness[depth]=RES[i];
        traverse(i,depth+1,next);
    }
}
int main(){
    array<uint32_t,N+1> have={};have[0]=1;
    traverse(0,0,have);
    const uint64_t expected[]={1,20,210,1540,8855,35700,78700,89100,58350,21600,3900,0};
    for(int i=0;i<=L;++i)if(count_by_length[i]!=expected[i])return 1;
    if(!have_witness||count_by_length[11])return 2;
    cout<<"VERIFY_OK CXX counts=";
    for(int i=0;i<=L;++i){if(i)cout<<",";cout<<count_by_length[i];}
    cout<<" witness10=";
    for(int i=0;i<10;++i){if(i)cout<<",";cout<<first_bad10[i];}
    cout<<"\n";
}
