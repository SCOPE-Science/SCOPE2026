// Independent exact matching-extension and alternating-cycle packing verifier.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
using Edge=pair<int,int>;
using Matching=vector<Edge>;
static array<uint32_t,28> adj{};
static vector<Matching> all;
static unordered_map<uint32_t,uint32_t> cache;
static uint32_t calls=0;

static void dfs(uint32_t free,Matching& current){
  if(!free){all.push_back(current);return;}
  int v=__builtin_ctz(free);
  uint32_t opts=adj[v]&free;
  while(opts){int u=__builtin_ctz(opts);opts&=opts-1;
    current.emplace_back(min(u,v),max(u,v));
    dfs(free^(1u<<v)^(1u<<u),current);
    current.pop_back();
  }
}
static uint32_t completions(uint32_t free){
  if(!free) return 1;
  if(__builtin_popcount(free)&1) return 0;
  auto it=cache.find(free);if(it!=cache.end())return it->second;
  ++calls;
  int v=__builtin_ctz(free);uint32_t options=adj[v]&free;
  uint32_t sum=0;
  while(options){int u=__builtin_ctz(options);options &= options-1;
    sum+=completions(free^(1u<<v)^(1u<<u));
  }
  return cache[free]=sum;
}
int main(){
  vector<uint8_t> triple;
  for(int a=1;a<8;a++)for(int b=a+1;b<8;b++)for(int c=b+1;c<8;c++)
    if((a^b^c)!=0) triple.push_back(uint8_t((1<<a)|(1<<b)|(1<<c)));
  assert(triple.size()==28);
  vector<Edge> E;
  for(int i=0;i<28;i++)for(int j=i+1;j<28;j++) if(!(triple[i]&triple[j])){
    adj[i] |= 1u<<j;adj[j]|=1u<<i;E.emplace_back(i,j);
  }
  assert(E.size()==42);
  for(int i=0;i<28;i++) assert(__builtin_popcount(adj[i])==3);
  Matching m;dfs((1u<<28)-1,m);
  for(auto &z:all)sort(z.begin(),z.end());
  sort(all.begin(),all.end());
  all.erase(unique(all.begin(),all.end()),all.end());
  assert(all.size()==84);
  const Matching &ref=all.front();
  assert(ref.size()==14);
  uint32_t coef[15]={};uint32_t max_extension=0;
  for(int s=0;s<(1<<14);s++){
    uint32_t used=0;
    for(int k=0;k<14;k++)if(s&(1<<k)){
      used|=1u<<ref[k].first;used|=1u<<ref[k].second;
    }
    uint32_t count=completions(((1u<<28)-1)^used);
    assert(count>=1);
    if(count==1)coef[__builtin_popcount((unsigned)s)]++;
    max_extension=max(max_extension,count);
  }
  int expected[15]={0,0,0,0,198,1018,2300,3124,2918,1988,1000,364,91,14,1};
  for(int k=0;k<15;k++) assert(coef[k]==(uint32_t)expected[k]);
  assert(completions((1u<<28)-1)==84);
  map<vector<Edge>, uint32_t> alt;
  for(auto &matching: all){
    vector<Edge> diff;
    set_symmetric_difference(ref.begin(),ref.end(),matching.begin(),matching.end(),back_inserter(diff));
    if(diff.empty())continue;
    array<uint32_t,28> g{};
    for(auto [a,b]:diff){g[a]|=1u<<b;g[b]|=1u<<a;}
    uint32_t seen=0;
    for(int s=0;s<28;s++) if(g[s]&&!(seen&(1u<<s))){
      uint32_t component=0;
      vector<int> q={s};component|=1u<<s;
      while(!q.empty()){
        int u=q.back();q.pop_back();uint32_t nb=g[u]&~component;
        while(nb){int v=__builtin_ctz(nb);nb&=nb-1;component|=1u<<v;q.push_back(v);}
      }
      seen|=component;
      vector<Edge> cyc;
      for(auto e:diff)if(component&(1u<<e.first))cyc.push_back(e);
      assert(int(cyc.size())==__builtin_popcount(component));
      alt[cyc]=component;
    }
  }
  map<int,int> cnt;
  vector<uint32_t> cm;
  for(auto [edges,vertices]:alt){cnt[edges.size()]++;cm.push_back(vertices);}
  assert(alt.size()==74);
  assert((cnt==map<int,int>({{8,1},{10,4},{12,4},{14,12},{16,9},{18,4},{20,16},{22,16},{24,8}})));
  bool two=false;bool three=false;
  for(size_t i=0;i<cm.size();i++)for(size_t j=i+1;j<cm.size();j++)if(!(cm[i]&cm[j])){
    two=true;
    for(size_t k=j+1;k<cm.size();k++)if(!(cm[i]&cm[k])&&!(cm[j]&cm[k]))three=true;
  }
  assert(two && !three);
  cout << "VERIFY_INDEPENDENT_OK vertices=28 edges=42 matchings=84\n";
  cout << "VERIFY_INDEPENDENT_OK extension_DP_residual_states="<<cache.size()<<" full_matchings=84\n";
  cout << "VERIFY_INDEPENDENT_OK forcing_counts=";
  for(int k=4;k<=14;k++)cout<<k<<":"<<coef[k]<<(k==14?'\n':',');
  cout << "VERIFY_INDEPENDENT_OK alternating_cycles=74 pair_disjoint=true triple_disjoint=false\n";
  cout << "VERIFY_INDEPENDENT_OK local_forcing_number=4 cycle_packing=2 gap=2\n";
}
