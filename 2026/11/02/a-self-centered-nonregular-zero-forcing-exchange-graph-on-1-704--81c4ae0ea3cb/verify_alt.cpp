// Exhaustive finite checker for the minimum-zero-forcing-set exchange graph of GP(8,3).
// Build: c++ -O3 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <vector>
using namespace std;
int main(){
 constexpr int n=8, N=16, FULL=(1<<N)-1;
 array<unsigned, N> adj{};
 auto link=[&](int a,int b){adj[a]|=1u<<b;adj[b]|=1u<<a;};
 for(int i=0;i<n;++i){link(i,(i+1)%n);link(i,8+i);link(8+i,8+(i+3)%n);}
 auto forcing=[&](unsigned initial){
  unsigned blue=initial;
  while(true){
   bool progressed=false;
   for(int v=0;v<N;++v){
    if(!(blue&(1u<<v))) continue;
    unsigned white=adj[v]&~blue;
    if(white && !(white&(white-1))){blue |= white;progressed=true;break;}
   }
   if(!progressed)break;
  }
  return blue==FULL;
 };
 vector<unsigned> states;int five=0;
 for(unsigned mask=0;mask<=FULL;++mask){
  int c=__builtin_popcount(mask);
  if(c==5 && forcing(mask))++five;
  if(c==6 && forcing(mask))states.push_back(mask);
 }
 if(five || states.size()!=1704)throw runtime_error("forcing family discrepancy");
 vector<int> idx(1<<N,-1);
 for(int i=0;i<(int)states.size();++i)idx[states[i]]=i;
 vector<vector<int>> graph(states.size());map<int,int> degrees;
 for(int i=0;i<(int)states.size();++i){
  unsigned s=states[i];
  for(int x=0;x<N;++x){
   if(!(s&(1u<<x)))continue;
   for(int y=0;y<N;++y){
    if(s&(1u<<y))continue;
    unsigned t=s^(1u<<x)^(1u<<y);
    if(idx[t]>=0)graph[i].push_back(idx[t]);
   }
  }
  sort(graph[i].begin(),graph[i].end());
  if(unique(graph[i].begin(),graph[i].end())!=graph[i].end())throw runtime_error("duplicate transition");
  ++degrees[(int)graph[i].size()];
 }
 long long twoE=0;for(auto& g:graph)twoE+=g.size();
 if(twoE!=33120)throw runtime_error("edge count discrepancy");
 map<int,long long> pair_distribution, exc, gap; map<pair<int,int>,long long> gap_h; vector<pair<int,int>> gap2pairs;long long wiener=0, overlap_excess=0;
 for(int s=0;s<(int)states.size();++s){
  vector<int> dist(states.size(),-1);queue<int> q;dist[s]=0;q.push(s);
  while(!q.empty()){
   int v=q.front();q.pop();
   for(int t:graph[v])if(dist[t]<0){dist[t]=dist[v]+1;q.push(t);}
  }
  if(find(dist.begin(),dist.end(),-1)!=dist.end())throw runtime_error("disconnected");
  int ecc=*max_element(dist.begin(),dist.end());++exc[ecc];
  for(int t=s+1;t<(int)states.size();++t){
   int d=dist[t];++pair_distribution[d];wiener+=d;
   int h=__builtin_popcount(states[s]^states[t])/2;
   if(d<h)throw runtime_error("invalid move lower bound");
   ++gap[d-h]; ++gap_h[{d-h,h}]; if(d-h==2) gap2pairs.emplace_back(s,t); if(d>h)++overlap_excess;
  }
 }
 cout<<"ALT_FINITE_PASS forcing5="<<five<<" forcing6="<<states.size()<<" edges="<<twoE/2
  <<" wiener="<<wiener<<" excess_pairs="<<overlap_excess<<"\n";
 cout<<"degrees";for(auto [d,k]:degrees)cout<<" "<<d<<":"<<k;cout<<"\n";
 cout<<"eccentricity";for(auto [d,k]:exc)cout<<" "<<d<<":"<<k;cout<<"\n";
 cout<<"gap_ambient"; for(auto [p,k]:gap_h)cout<<" ("<<p.first<<","<<p.second<<"):"<<k; cout<<"\n";
 map<int,int> endpoint_incidence;map<pair<int,int>,int> endpoint_degrees; for(auto [a,b]:gap2pairs){++endpoint_incidence[a];++endpoint_incidence[b];auto x=min(graph[a].size(),graph[b].size()), y=max(graph[a].size(),graph[b].size()); ++endpoint_degrees[{(int)x,(int)y}];} map<int,int> incidence_hist; for(auto [v,c]:endpoint_incidence)++incidence_hist[c];cout<<"gap2_endpoints";for(auto [i,c]:incidence_hist)cout<<" "<<i<<":"<<c;cout<<"\n"; cout<<"gap2_endpoint_degrees";for(auto [p,c]:endpoint_degrees)cout<<" ("<<p.first<<","<<p.second<<"):"<<c;cout<<"\n"; cout<<"gap2_samples";for(int i=0;i<min(8,(int)gap2pairs.size());++i)cout<<" ("<<states[gap2pairs[i].first]<<","<<states[gap2pairs[i].second]<<")";cout<<"\n";
 cout<<"johnson_gap";for(auto [g,k]:gap)cout<<" "<<g<<":"<<k;cout<<"\n";
 cout<<"unordered_distances";for(auto [d,k]:pair_distribution)cout<<" "<<d<<":"<<k;cout<<"\n";
 if(exc.size()!=1 || exc.begin()->first!=6 || exc.begin()->second!=1704 || wiener!=5453976)
  throw runtime_error("radius/diameter/Wiener mismatch");
 return 0;
}
