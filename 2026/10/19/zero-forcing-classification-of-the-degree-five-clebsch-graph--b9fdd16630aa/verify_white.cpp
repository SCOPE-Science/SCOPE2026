#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static constexpr int N=16, FULL=(1<<N)-1;
struct Outcome { bool forcing;int rounds;int initially_forced;};
static const array<int,5> generators={1,2,4,8,15};
Outcome check_white(int whites){
  int t=0, wave=0;
  while(whites){
    int remove=0;
    for(int x=0;x<N;++x){
      if(whites&(1<<x)) continue;
      int neighbor_count=0,last=-1;
      for(int g:generators){
        int y=x^g;
        if(whites&(1<<y)){++neighbor_count;last=y;}
      }
      if(neighbor_count==1) remove|=1<<last;
    }
    if(remove==0) return {false,t,wave};
    if(t==0) wave=__builtin_popcount((unsigned)remove);
    whites&=~remove;++t;
    if(t>N) assert(false);
  }
  return {true,t,wave};
}
int main(){
  long long by_size[17]={}, by_round[17][18]={};
  array<bool,1<<N> forcing{};
  long long minimal[17]={};
  long long checked=0;
  for(int b=0;b<=FULL;++b){
    auto o=check_white(FULL^b);
    forcing[b]=o.forcing;
    if(o.forcing){int k=__builtin_popcount((unsigned)b);by_size[k]++;by_round[k][o.rounds]++;}
    ++checked;
  }
  for(int b=0;b<=FULL;++b){
    if(!forcing[b])continue;
    bool minimal_here=true;
    for(int x=0;x<N;++x)if(b&(1<<x)){
      if(forcing[b^(1<<x)]){minimal_here=false;break;}
    }
    if(minimal_here)minimal[__builtin_popcount((unsigned)b)]++;
  }
  const long long expect[17]={0,0,0,0,0,0,0,0,0,0,3872,3632,1760,560,120,16,1};
  const long long expmin[17]={0,0,0,0,0,0,0,0,0,0,3872};
  for(int k=0;k<=16;++k){
    assert(by_size[k]==expect[k]);assert(minimal[k]==expmin[k]);
  }
  assert(by_round[10][2]==3872);
  assert(by_round[11][1]==272&&by_round[11][2]==3360);
  assert(by_round[12][1]==1280&&by_round[12][2]==480);
  assert(by_round[13][1]==560&&by_round[14][1]==120);
  assert(by_round[15][1]==16&&by_round[16][0]==1);
  long long cnt=0;for(int k=0;k<=16;++k)cnt+=by_size[k];assert(cnt==9961);
  cout<<"VERIFY_CPP_OK vertex_sets="<<checked<<" forcing_sets="<<cnt<<"\n";
  cout<<"VERIFY_CPP_OK polynomial=10:3872,11:3632,12:1760,13:560,14:120,15:16,16:1\n";
  cout<<"VERIFY_CPP_OK inclusion_minimal_sets=3872 all_size_10=true\n";
  cout<<"VERIFY_CPP_OK propagation_time_minimum_sets=2 all_3872=true\n";
}
