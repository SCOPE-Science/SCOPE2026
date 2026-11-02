// Exact finite Ehrenfeucht--Fraisse quantifier-rank-four comparison of
// projective-plane Levi graphs, using the entire atomic extension spectrum.
// For prime orders 2,3,5 only. This computation is corroboration,
// not an infinite proof.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using Key=vector<int>;
struct KeyHash {size_t operator()(Key const& v) const noexcept {
 size_t h=1469598103934665603ULL;
 for(int x:v){h^=(uint64_t)x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}
 return h;
}};
struct Graph{int n; vector<vector<unsigned char>> adj;};
int inv(int a,int p){for(int b=1;b<p;++b)if(a*b%p==1)return b;assert(false);return 0;}
Graph pg(int p){
 vector<vector<int>> pts;
 for(int a=0;a<p;++a)for(int b=0;b<p;++b)for(int c=0;c<p;++c){
  if(a==0 && b==0 && c==0)continue;
  int t=a?a:(b?b:c);int u=inv(t,p);
  vector<int> x={(a*u)%p,(b*u)%p,(c*u)%p};pts.push_back(x);
 }
 sort(pts.begin(),pts.end());pts.erase(unique(pts.begin(),pts.end()),pts.end());
 int v=pts.size();Graph g{2*v,vector<vector<unsigned char>>(2*v,vector<unsigned char>(2*v,0))};
 for(int i=0;i<v;++i)for(int j=0;j<v;++j){int s=0;for(int k=0;k<3;++k)s+=pts[i][k]*pts[j][k];if(s%p==0)g.adj[i][v+j]=g.adj[v+j][i]=1;}
 return g;
}
int atom(Graph const&g,vector<int> const&t){int a=0,k=0;
 for(int i=0;i<(int)t.size();++i)for(int j=0;j<i;++j){a|=(int(t[i]==t[j])<<k++);a|=(int(g.adj[t[i]][t[j]])<<k++);}
 return a;
}
int lookup(Key const& k,unordered_map<Key,int,KeyHash>& reg){auto it=reg.find(k);if(it!=reg.end())return it->second;int x=reg.size();reg.emplace(k,x);return x;}
struct State{Graph g;vector<int> third,pair,single;int root=-1;};
void build_triples(State &s,unordered_map<Key,int,KeyHash>& global){int n=s.g.n;
 s.third.resize(n*n*n);vector<int> tuple;tuple.reserve(4);Key key;key.reserve(64);
 for(int i=0;i<n;++i)for(int j=0;j<n;++j)for(int k=0;k<n;++k){
  tuple={i,j,k};key.clear();key.push_back(atom(s.g,tuple));
  for(int v=0;v<n;++v){tuple.push_back(v);key.push_back(atom(s.g,tuple));tuple.pop_back();}
  sort(key.begin()+1,key.end());key.erase(unique(key.begin()+1,key.end()),key.end());
  s.third[(i*n+j)*n+k]=lookup(key,global);
 }
}
void build_pairs(State &s,unordered_map<Key,int,KeyHash>& global){int n=s.g.n;s.pair.resize(n*n);Key key;key.reserve(n+1);
 for(int i=0;i<n;++i)for(int j=0;j<n;++j){key.clear();key.push_back(atom(s.g,vector<int>{i,j}));for(int k=0;k<n;++k)key.push_back(s.third[(i*n+j)*n+k]);sort(key.begin()+1,key.end());key.erase(unique(key.begin()+1,key.end()),key.end());s.pair[i*n+j]=lookup(key,global);}
}
void build_single(State &s,unordered_map<Key,int,KeyHash>& global){int n=s.g.n;s.single.resize(n);Key key;key.reserve(n+1);
 for(int i=0;i<n;++i){key.clear();key.push_back(0);for(int j=0;j<n;++j)key.push_back(s.pair[i*n+j]);sort(key.begin()+1,key.end());key.erase(unique(key.begin()+1,key.end()),key.end());s.single[i]=lookup(key,global);}
}
void build_root(State &s,unordered_map<Key,int,KeyHash>& global){Key key{0};for(auto id:s.single)key.push_back(id);sort(key.begin()+1,key.end());key.erase(unique(key.begin()+1,key.end()),key.end());s.root=lookup(key,global);}
int main(){auto start=chrono::steady_clock::now();vector<int> primes={2,3,5};vector<State> S;
 for(int p:primes){S.push_back(State{pg(p),{},{},{},-1});cout<<"order="<<p<<" vertices="<<S.back().g.n<<"\n";}
 for(int level=3;level>=0;--level){unordered_map<Key,int,KeyHash> registry;
 for(size_t i=0;i<S.size();++i){State &s=S[i];if(level==3)build_triples(s,registry);if(level==2)build_pairs(s,registry);if(level==1)build_single(s,registry);if(level==0)build_root(s,registry);
  cout<<"order="<<primes[i]<<" level="<<level<<" distinct_types=";
  if(level==3){auto z=s.third;sort(z.begin(),z.end());cout<<(unique(z.begin(),z.end())-z.begin());}
  if(level==2){auto z=s.pair;sort(z.begin(),z.end());cout<<(unique(z.begin(),z.end())-z.begin());}
  if(level==1){auto z=s.single;sort(z.begin(),z.end());cout<<(unique(z.begin(),z.end())-z.begin());}
  if(level==0)cout<<"1 (root_id="<<s.root<<")";
  cout<<"\n";
 }
 cout<<"global_level="<<level<<" distinct_types="<<registry.size()<<"\n";
 }
 for(size_t i=1;i<S.size();++i)if(S[i].root!=S[0].root){cerr<<"FAIL unequal rank-four theories\n";return 1;}
 cout<<"PASS rank-four theories equal for PG(2,2), PG(2,3), PG(2,5)\n";
 for(size_t i=0;i<S.size();++i){
  bool degree_four=false;
  for(auto const& row:S[i].g.adj){int deg=0;for(unsigned char b:row)deg+=b; if(deg>=4)degree_four=true;}
  if(degree_four!=(primes[i]>=3)){cerr<<"FAIL rank-five degree witness\n";return 2;}
 }
 cout<<"PASS rank-five degree witness separates PG(2,2) from orders 3 and 5\n";
 (void)start;
}
