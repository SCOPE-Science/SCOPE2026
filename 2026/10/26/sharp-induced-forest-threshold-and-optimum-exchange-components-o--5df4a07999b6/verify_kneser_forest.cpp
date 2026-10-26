// Standalone exact finite checks for the sharp Kneser induced-forest classification.
// Compile: c++ -O2 -std=c++17 verify_kneser_forest.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using U=uint64_t;
int main(){
 for(int n=5;n<=8;++n){
  vector<pair<int,int>> edges;
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)edges.push_back({a,b});
  int N=(int)edges.size(); assert(N<=28);
  vector<U> nbr(N,0);
  for(int i=0;i<N;++i)for(int j=i+1;j<N;++j){
   auto [a,b]=edges[i];auto [c,d]=edges[j];
   if(a!=c&&a!=d&&b!=c&&b!=d)nbr[i]|=U(1)<<j,nbr[j]|=U(1)<<i;
  }
  auto idx=[&](int a,int b){if(a>b)swap(a,b);for(int i=0;i<N;++i)if(edges[i]==make_pair(a,b))return i;assert(false);return -1;};
  auto checkDSU=[&](U mask){
   int par[28];iota(par,par+N,0);
   auto rt=[&](int x){while(par[x]!=x)x=par[x]=par[par[x]];return x;};
   for(int x=0;x<N;++x)if((mask>>x)&1){
    U y=mask&nbr[x]&~((U(1)<<(x+1))-1);
    while(y){int z=__builtin_ctzll(y);y&=y-1;int a=rt(x),b=rt(z);if(a==b)return false;par[a]=b;}
   }
   return true;
  };
  // Independent DFS cycle check of accepted states, distinct from union-find enumeration.
  auto checkDFS=[&](U mask){
   bool seen[28]={};
   function<bool(int,int)> dfs=[&](int x,int from){seen[x]=true;U y=mask&nbr[x];while(y){int z=__builtin_ctzll(y);y&=y-1;if(z==from)continue;if(seen[z]||!dfs(z,x))return false;}return true;};
   for(int x=0;x<N;++x)if((mask>>x&1)&&!seen[x])if(!dfs(x,-1))return false;
   return true;
  };
  auto bits=[&](const vector<pair<int,int>>& L){U x=0;for(auto [a,b]:L)x|=U(1)<<idx(a,b);return x;};
  set<U> predicted;
  // Type C: a K4 plus an external pendant edge.
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)for(int d=c+1;d<n;++d){
   vector<int> T={a,b,c,d};vector<pair<int,int>> full;
   for(int i=0;i<4;++i)for(int j=i+1;j<4;++j)full.push_back({T[i],T[j]});
   for(int center:T)for(int outside=0;outside<n;++outside)
    if(find(T.begin(),T.end(),outside)==T.end()){
     auto B=full;B.push_back({center,outside});
     if(n<=7)predicted.insert(bits(B));
    }
  }
  // Type S: full star plus one extra nonincident pair.
  if(n>=7)for(int a=0;a<n;++a)for(int b=0;b<n;++b)for(int c=b+1;c<n;++c)
   if(b!=a&&c!=a){vector<pair<int,int>> B;for(int j=0;j<n;++j)if(j!=a)B.push_back({a,j});B.push_back({b,c});predicted.insert(bits(B));}
  int best=max(n,7);
  set<U> actual;
  auto enumerate=[&](int k,bool save){
   U s=(U(1)<<k)-1;U stop=U(1)<<N;size_t count=0;
   while(s<stop){if(checkDSU(s)){++count;if(save){assert(checkDFS(s));actual.insert(s);}}
    U c=s&-s, r=s+c;
    s=(((r^s)>>2)/c)|r;
   }
   return count;
  };
  assert(enumerate(best+1,false)==0); // monotonicity excludes every larger forest
  assert(enumerate(best,true)==predicted.size());
  assert(actual==predicted);
  map<U,int> index;int ctr=0;for(U x:predicted)index[x]=ctr++;
  vector<vector<int>> adj(ctr);
  // Exchange graph: two optimum families are adjacent iff they share best-1 vertices.
  for(auto i=index.begin();i!=index.end();++i)for(auto j=next(i);j!=index.end();++j)
   if(__builtin_popcountll(i->first&j->first)==best-1){adj[i->second].push_back(j->second);adj[j->second].push_back(i->second);}
  vector<int> used(ctr), components;
  for(int s=0;s<ctr;++s)if(!used[s]){vector<int> q={s};used[s]=1;
   for(size_t at=0;at<q.size();++at)for(int t:adj[q[at]])if(!used[t])used[t]=1,q.push_back(t);
   components.push_back((int)q.size());
   for(int v:q)assert((int)adj[v].size()==(int)q.size()-1);
  }
  sort(components.begin(),components.end());
  vector<int> expect;
  if(n<=7)expect.insert(expect.end(),(n*(n-1)*(n-2)*(n-3)/24),4*(n-4));
  if(n>=7)expect.insert(expect.end(),n,(n-1)*(n-2)/2);
  sort(expect.begin(),expect.end());assert(components==expect);
  cout<<"n="<<n<<" optimum="<<best<<" sets="<<actual.size()<<" components="<<components.size()<<" edges=";
  size_t sides=0;for(auto &v:adj)sides+=v.size();cout<<sides/2<<" VERIFY_OK\n";
 }
}
