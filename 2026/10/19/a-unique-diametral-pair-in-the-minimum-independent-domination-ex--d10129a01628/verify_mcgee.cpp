// Independent exhaustive verifier for the McGee graph minimum independent-dominating exchange result.
// Build: g++ -std=c++17 -O2 -Wall -Wextra verify_mcgee.cpp -o verify_mcgee
// Run: ./verify_mcgee
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int N=24;
constexpr uint32_t ALL=(1u<<N)-1;
int main(){
  array<uint32_t,N> nb{};
  const int shift[3]={-12,7,-7};
  auto add_edge=[&](int u,int v){assert(u!=v);nb[u]|=1u<<v;nb[v]|=1u<<u;};
  for(int u=0;u<N;u++){
    add_edge(u,(u+1)%N);
    int v=(u+shift[u%3]+N)%N;
    add_edge(u,v);
  }
  int sumdeg=0;
  for(int u=0;u<N;u++){
    assert(__builtin_popcount(nb[u])==3);
    sumdeg+=__builtin_popcount(nb[u]);
  }
  assert(sumdeg==72);
  array<int,25> f{};
  array<int,25> mis{};
  vector<uint32_t> opt;
  // Full independent-face and maximal-independent-set census, not a sampled search.
  for(uint32_t s=0;s<=ALL;s++){
    bool independent=true;
    uint32_t x=s;
    while(x){int u=__builtin_ctz(x);x&=x-1;if(nb[u]&s){independent=false;break;}}
    if(!independent)continue;
    int k=__builtin_popcount(s);
    f[k]++;
    uint32_t covered=s;
    x=s;
    while(x){int u=__builtin_ctz(x);x&=x-1;covered|=nb[u];}
    if(covered==ALL){mis[k]++;if(k==8)opt.push_back(s);}
  }
  sort(opt.begin(),opt.end());
  assert(accumulate(f.begin(),f.end(),0)==34305);
  assert(mis[8]==146 && mis[9]==352 && mis[10]==8);
  for(int k=0;k<8;k++)assert(mis[k]==0);
  for(int k=11;k<=24;k++)assert(mis[k]==0);
  assert(opt.size()==146);
  unordered_map<uint32_t,int> idx;
  for(int i=0;i<(int)opt.size();i++)idx[opt[i]]=i;
  vector<vector<int>> adj(opt.size());
  int tsedges=0, tjedges=0;
  for(int i=0;i<(int)opt.size();i++)for(int j=i+1;j<(int)opt.size();j++){
    uint32_t diff=opt[i]^opt[j];
    if(__builtin_popcount(diff)!=2)continue;
    tjedges++;
    uint32_t a=opt[i]&diff,b=opt[j]&diff;
    assert(__builtin_popcount(a)==1 && __builtin_popcount(b)==1);
    // For two maximal independent sets, a one-token jump is forced to be a slide.
    int x=__builtin_ctz(a),y=__builtin_ctz(b);
    assert((nb[x]>>y)&1u);
    tsedges++;
    adj[i].push_back(j);
    adj[j].push_back(i);
  }
  assert(tsedges==216 && tjedges==216);
  map<int,int> degree_hist,ecc_hist;
  for(auto &row:adj)degree_hist[row.size()]++;
  int radius=10000,diameter=0,diam_pair_count=0;
  pair<uint32_t,uint32_t> diam_pair={0,0};
  for(int root=0;root<(int)opt.size();root++){
    vector<int> dist(opt.size(),-1);
    dist[root]=0;
    queue<int> q;q.push(root);
    while(!q.empty()){
      int v=q.front();q.pop();
      for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;q.push(w);}
    }
    int ecc=0;
    for(int j=0;j<(int)opt.size();j++){
      assert(dist[j]>=0);
      ecc=max(ecc,dist[j]);
      if(j>root){
        if(dist[j]>diameter){diameter=dist[j];diam_pair_count=1;diam_pair={opt[root],opt[j]};}
        else if(dist[j]==diameter){diam_pair_count++;}
      }
    }
    radius=min(radius,ecc);ecc_hist[ecc]++;
  }
  assert(radius==11 && diameter==12 && diam_pair_count==1);
  assert(diam_pair==make_pair((uint32_t)4793490,(uint32_t)9586980));
  assert((degree_hist==map<int,int>{{2,64},{3,48},{4,16},{5,16},{8,2}}));
  assert((ecc_hist==map<int,int>{{11,144},{12,2}}));
  int triangles=0;
  for(int i=0;i<(int)opt.size();i++)for(int j:adj[i])if(j>i){
    for(int k:adj[i])if(k>j && find(adj[j].begin(),adj[j].end(),k)!=adj[j].end())triangles++;
  }
  assert(triangles==0);
  cout<<"McGee independent-domination independent C++ verification\n";
  cout<<"independent_faces:";for(int k=0;k<=10;k++)cout<<" "<<f[k];cout<<"\n";
  cout<<"maximal_independent:";for(int k=8;k<=10;k++)cout<<" "<<k<<":"<<mis[k];cout<<"\n";
  cout<<"minimum_size:8 minimum_count:"<<opt.size()<<"\n";
  cout<<"TJ_edges:"<<tjedges<<" TS_edges:"<<tsedges<<"\n";
  cout<<"degree_spectrum:";for(auto &p:degree_hist)cout<<" "<<p.first<<":"<<p.second;cout<<"\n";
  cout<<"radius:"<<radius<<" diameter:"<<diameter<<"\n";
  cout<<"eccentricity_spectrum:";for(auto &p:ecc_hist)cout<<" "<<p.first<<":"<<p.second;cout<<"\n";
  cout<<"diametral_pair_count:"<<diam_pair_count<<" masks:"<<diam_pair.first<<","<<diam_pair.second<<"\n";
  cout<<"triangles:"<<triangles<<"\n";
}
