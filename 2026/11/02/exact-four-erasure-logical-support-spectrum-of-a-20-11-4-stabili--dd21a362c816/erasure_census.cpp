#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
static constexpr int N=20,R=9;
static const array<string,R> pauli={
"YZIIZZIZIXZXZXZYZXXX",
"IYZIIIIZIZYIZYYZZZZI",
"ZIXZZZZZIXXIZYYIZIXI",
"ZIIYZIIIIZIZYIZYYZZZ",
"ZZZIYIZIZYZIYXIIXXYX",
"ZZZIIYZIIIIZIZYIZYYZ",
"IIIZIZYIZYYZZZZIIYZI",
"IIZZIZIXZXZXZYZXXXYZ",
"ZIIIIZIZYIZYYZZZZIIY"};
uint64_t xs[R],zs[R];
int rank64(array<uint64_t,R> v) {
  uint64_t piv[40]={};int rank=0;
  for(uint64_t x:v){
    while(x){int b=63-__builtin_clzll(x);
      if(piv[b])x^=piv[b];else{piv[b]=x;++rank;break;}}
  }
  return rank;
}
int rank9(uint32_t E){
  uint16_t piv[9]={};int rank=0;
  for(int j=0;j<N;++j){if(!(E&(1u<<j)))continue;
    for(int kind=0;kind<2;++kind){uint16_t x=0;
      for(int r=0;r<R;++r)
        if(((kind==0?zs[r]:xs[r])>>j)&1) x|=(1u<<r);
      while(x){int b=31-__builtin_clz(x);
        if(piv[b]) x^=piv[b];else{piv[b]=x;++rank;break;}}
    }
  }
  return rank;
}
int outside_rank(uint32_t E){
  uint64_t mask= ((uint64_t)((1u<<N)-1)) & ~(uint64_t)E;
  array<uint64_t,R> v{};
  for(int r=0;r<R;++r) v[r]=(xs[r]&mask)|((zs[r]&mask)<<N);
  return rank64(v);
}
int main(){
  for(int r=0;r<R;++r){
    if(pauli[r].size()!=N)throw runtime_error("bad length");
    xs[r]=zs[r]=0;
    for(int j=0;j<N;++j){char x=pauli[r][j];
      if(x=='X'||x=='Y')xs[r]|=1u<<j;
      if(x=='Z'||x=='Y')zs[r]|=1u<<j;
    }
  }
  array<uint64_t,R> rows{};
  for(int r=0;r<R;++r) rows[r]=xs[r]|(zs[r]<<N);
  if(rank64(rows)!=R)throw runtime_error("not full-rank");
  array<int,N+1> stabilizer_weight{};
  for(int mask=0;mask<(1<<R);++mask){uint64_t x=0,z=0;
    for(int i=0;i<R;++i)if(mask&(1<<i)){x^=xs[i];z^=zs[i];}
    ++stabilizer_weight[__builtin_popcountll(x|z)];
  }
  if(stabilizer_weight[0]!=1 || stabilizer_weight[12]!=50 ||
     stabilizer_weight[14]!=220 || stabilizer_weight[16]!=195 ||
     stabilizer_weight[18]!=20 || stabilizer_weight[20]!=26)
     throw runtime_error("stabilizer spectrum mismatch");
  for(int i=1;i<12;++i)if(stabilizer_weight[i])
     throw runtime_error("unexpected low-weight stabilizer");
  for(int i=0;i<R;++i)for(int j=0;j<R;++j)
    if(((__builtin_popcountll(xs[i]&zs[j])+__builtin_popcountll(zs[i]&xs[j]))&1)!=0)
      throw runtime_error("noncommuting");
  array<uint64_t,N+1> good{},bad{};
  array<uint64_t,N+1> logical_dimension_total{};
  vector<uint32_t> bad4;
  array<uint64_t,9> four_logical_dimension_hist{};
  for(uint32_t E=0;E<(1u<<N);++E){
    int e=__builtin_popcount(E), syn=rank9(E), r_out=outside_rank(E);
    int logical=2*e-syn-(R-r_out);
    if(logical<0)throw runtime_error("invalid kernel quotient dimension");
    if(logical==0)++good[e];else {++bad[e]; if(e==4) bad4.push_back(E);}
    if(e==4) { if(logical>=9)throw runtime_error("large logical kernel"); ++four_logical_dimension_hist[logical]; }
    logical_dimension_total[e]+=logical;
  }
  uint64_t size_sum=0;
  cout<<"ERASURE_TABLE\n";
  for(int e=0;e<=N;++e){size_sum+=good[e]+bad[e];
    cout<<e<<" "<<good[e]<<" "<<bad[e]<<" "<<logical_dimension_total[e]<<"\n";}
  if(size_sum!=(1u<<N))throw runtime_error("not exhaustive");
  array<int,(1u<<N)> cover{};
  for(uint32_t B:bad4) {
    for(int i=0;i<N;++i) if(!(B&(1u<<i))) ++cover[B|(1u<<i)];
  }
  array<int,10> multi{};
  for(uint32_t E=0;E<(1u<<N);++E)
    if(__builtin_popcount(E)==5){int c=cover[E];if(c<10)++multi[c]; else throw runtime_error("large covering multiplicity");}
  cout<<"FOUR_ERASURE_KERNEL_HIST";for(size_t i=0;i<four_logical_dimension_hist.size();++i)cout<<" "<<i<<":"<<four_logical_dimension_hist[i];cout<<"\n";
  cout<<"FIVE_ERASURE_4SUPPORT_COVER";
  for(int i=0;i<10;++i) cout<<" "<<i<<":"<<multi[i];
  cout<<"\n";
  cout<<"ERASURE_CENSUS_OK\n";
}
