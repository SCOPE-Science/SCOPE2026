// Exhaustive fixed-cardinality enumeration of open-neighborhood covers of the Coxeter graph.
// Compile: c++ -std=c++17 -O2 verification_enumerate.cpp -o verify_exact && ./verify_exact
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  vector<uint32_t> triples;
  for(int a=1;a<=7;++a)for(int b=a+1;b<=7;++b)for(int c=b+1;c<=7;++c)
    if((a^b^c)!=0) triples.push_back((1u<<a)|(1u<<b)|(1u<<c));
  assert(triples.size()==28);
  uint32_t adj[28]={};
  for(int i=0;i<28;i++)for(int j=i+1;j<28;j++)if((triples[i]&triples[j])==0){adj[i]|=1u<<j;adj[j]|=1u<<i;}
  for(int i=0;i<28;i++)assert(__builtin_popcount(adj[i])==3);
  constexpr uint32_t ALL=(1u<<28)-1;
  const int k=10;
  uint32_t comb=(1u<<k)-1;
  uint64_t inspected=0;
  vector<uint32_t> winners;
  do {
    uint32_t sel=comb, covered=0;
    while(sel){unsigned i=__builtin_ctz(sel);covered|=adj[i];sel&=sel-1;}
    if(covered==ALL)winners.push_back(comb);
    ++inspected;
    uint32_t smallest=comb&-comb, next=comb+smallest;
    comb=(((next^comb)>>2)/smallest)|next;
  } while(comb<=ALL);
  sort(winners.begin(),winners.end());
  assert(inspected==13123110ull && winners.size()==28);
  cout<<"graph_vertices=28 graph_edges=42 degree=3\n";
  cout<<"subsets_of_size_10="<<inspected<<" total_dominating="<<winners.size()<<"\n";
  cout<<"minimum_masks=";
  for(size_t i=0;i<winners.size();++i)cout<<(i?",":"")<<winners[i];
  cout<<"\nCOMPLETE_ENUMERATION_OK\n";
}
