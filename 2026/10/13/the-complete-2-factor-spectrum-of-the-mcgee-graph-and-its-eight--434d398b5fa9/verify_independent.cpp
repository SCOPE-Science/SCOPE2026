// Independent exhaustive matching and complementary 2-factor census.
// Build: g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
constexpr int n = 24;
array<vector<int>,n> adj;
map<vector<int>,int> types;
long long total=0;
int main(){
  const int jump[3]={-12,7,-7};
  set<pair<int,int>> edge_set;
  auto add=[&](int x,int y){
    x=(x+n)%n;y=(y+n)%n;
    if(x>y)swap(x,y);
    edge_set.insert({x,y});
  };
  for(int v=0;v<n;++v){add(v,(v+1)%n);add(v,(v+jump[v%3]+n)%n);}
  assert(edge_set.size()==36);
  for(auto [a,b]:edge_set){adj[a].push_back(b);adj[b].push_back(a);}
  for(auto &v:adj){sort(v.begin(),v.end());assert(v.size()==3);}
  vector<pair<int,int>> matching;
  auto enumerate=[&](auto&& self,uint32_t occupied)->void{
    if(occupied==((1u<<n)-1)){
      ++total;
      bool chosen[n][n]={};
      for(auto [a,b]:matching){chosen[a][b]=chosen[b][a]=true;}
      vector<int> unseen(n,1), profile;
      for(int root=0;root<n;++root){
        if(!unseen[root])continue;
        int last=-1,v=root,size=0;
        do{
          assert(unseen[v]);unseen[v]=0;++size;
          int next=-1;
          for(int w:adj[v]) if(!chosen[v][w]&&w!=last) next=w;
          assert(next>=0);
          last=v;v=next;
        }while(v!=root);
        profile.push_back(size);
      }
      sort(profile.begin(),profile.end());
      ++types[profile];
      return;
    }
    // Different from the Python generator: choose an unpaired vertex with
    // fewest currently unpaired neighbours, so branches are reordered.
    int best=-1,count=4;
    for(int v=0;v<n;++v)if(!(occupied&(1u<<v))){
      int avail=0;
      for(int w:adj[v])if(!(occupied&(1u<<w)))++avail;
      if(avail<count){best=v;count=avail;}
    }
    if(count==0)return;
    for(int w:adj[best])if(!(occupied&(1u<<w))){
      matching.push_back({min(best,w),max(best,w)});
      self(self,occupied|(1u<<best)|(1u<<w));
      matching.pop_back();
    }
  };
  enumerate(enumerate,0);
  assert(total==60);
  assert(types.size()==3);
  assert(types[vector<int>{24}]==42);
  assert(types[(vector<int>{12,12})]==6);
  assert(types[(vector<int>{8,8,8})]==12);
  cout<<"VERIFY_INDEPENDENT_OK perfect_matchings=60 two_factor_types=24:42,12+12:6,8+8+8:12\n";
}
