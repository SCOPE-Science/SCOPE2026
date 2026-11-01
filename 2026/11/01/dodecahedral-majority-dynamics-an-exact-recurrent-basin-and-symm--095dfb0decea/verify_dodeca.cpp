#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
static constexpr unsigned NN=1u<<20;
static constexpr int adjacency[20][3]={{1,10,19},{0,2,8},{1,3,6},{2,4,19},{3,5,17},{4,6,15},{2,5,7},{6,8,14},{1,7,9},{8,10,13},{0,9,11},{10,12,18},{11,13,16},{9,12,14},{7,13,15},{5,14,16},{12,15,17},{4,16,18},{11,17,19},{0,3,18}};
static inline uint32_t independent_update(uint32_t s){
 uint32_t t=0;
 for(int v=0;v<20;v++){
  uint32_t a=(s>>adjacency[v][0])&1u,b=(s>>adjacency[v][1])&1u,c=(s>>adjacency[v][2])&1u;
  t|=((a&b)|(a&c)|(b&c))<<v;
 }
 return t;
}
int main(){
 ifstream fi("transition_u32le.bin",ios::binary);if(!fi){cerr<<"MISSING_TRANSITION\n";return 1;}
 vector<uint32_t> a(NN);for(unsigned x=0;x<NN;x++){
  uint32_t v=0;for(unsigned k=0;k<4;k++){int ch=fi.get();if(ch==EOF){cerr<<"SHORT_TRANSITION\n";return 1;}v|=(uint32_t(uint8_t(ch))<<(8*k));}a[x]=v;
  if(v>=NN || v!=independent_update(x)){cerr<<"MISMATCH "<<x<<"\n";return 1;}
 }
 if(fi.get()!=EOF){cerr<<"LONG_TRANSITION\n";return 1;}
 array<array<uint64_t,2>,8> cells{};
 uint64_t fix_states=0,two_states=0;
 for(uint32_t x=0;x<NN;x++){
   uint32_t y=x;unsigned t=0;
   while(t<=7 && a[a[y]]!=y){y=a[y];t++;}
   if(t>7){cerr<<"BOUND_FAIL "<<x<<"\n";return 1;}
   unsigned cyc=(a[y]!=y);
   cells[t][cyc]++;
   if(t==0){if(cyc)two_states++;else fix_states++;}
   if(t==7 && a[a[x]]==x){cerr<<"NONSHARP?";return 1;}
 }
 const array<uint64_t,8> Efixed={118,4710,14700,27320,61600,60960,15840,2880};
 const array<uint64_t,8> Etwo ={19358,351490,344880,105000,33960,5760,0,0};
 for(unsigned t=0;t<8;t++){
  if(cells[t][0]!=Efixed[t]||cells[t][1]!=Etwo[t]){cerr<<"WRONG_ENTRANCE "<<t<<"\n";return 1;}
 }
 if(fix_states!=118 || two_states!=19358 || two_states%2){cerr<<"WRONG_PERIODIC";return 1;}
 cout<<"VERIFY_ALL_1048576_TRANSITIONS_AND_BASINS_OK\n";
 cout<<"FIXED=118 TWO_ORBITS="<<two_states/2<<" MAX_TRANSIENT=7 BASIN_FIXED=188128 BASIN_TWO=860448\n";
 for(unsigned t=0;t<8;t++)cout<<"LAYER="<<t<<" fixed="<<cells[t][0]<<" two="<<cells[t][1]<<"\n";
}
