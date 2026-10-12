// Exact finite enumeration for the labeled truncated-octahedron graph.
// Compile: c++ -std=c++17 -O3 verify_bondage.cpp -o verify_bondage
// Run: ./verify_bondage
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using U = uint64_t;
constexpr int V=24,E=36;
const array<pair<int,int>,E> edge = {{{0,1},{0,2},{0,3},{1,4},{1,5},{2,6},{2,7},{3,4},{3,8},{4,9},{5,10},{5,11},{6,11},{6,12},{7,12},{7,13},{8,13},{8,14},{9,15},{9,16},{10,16},{10,17},{11,17},{12,18},{13,19},{14,15},{14,19},{15,20},{16,20},{17,21},{18,21},{18,22},{19,22},{20,23},{21,23},{22,23}}};
array<U,V> adj={}, closed={};
vector<U> dom8;
vector<array<int,5>> optimal;
array<array<bool,V>,V> mat{};
vector<int> bfsorder;
vector<array<int,V>> automorphisms;
int mapped[V],used[V];
void enumerate_autos(int at) {
 if(at==V) {array<int,V> a{};for(int j=0;j<V;j++)a[j]=mapped[j];automorphisms.push_back(a);return;}
 int u=bfsorder[at];
 for(int v=0;v<V;v++) {
  if(used[v])continue;
  bool ok=true;
  for(int j=0;j<at;j++) {
   int u0=bfsorder[j];if(mat[u][u0]!=mat[v][mapped[u0]]){ok=false;break;}
  }
  if(!ok)continue;
  mapped[u]=v;used[v]=1;
  enumerate_autos(at+1);
  used[v]=0;mapped[u]=-1;
 }
}
int survivor_count(U f,bool break_on_one=true) {
 array<U,V> n=closed;
 for(int e=0;e<E;e++)if((f>>e)&1ull){int u=edge[e].first,v=edge[e].second;n[u]&=~(1ull<<v);n[v]&=~(1ull<<u);}
 int survive=0;
 for(U d:dom8) {
  U cover=0,rest=d;
  while(rest) {int v=__builtin_ctzll(rest);rest&=rest-1;cover|=n[v];}
  if(cover==((1ull<<V)-1)){
   ++survive;
   if(break_on_one)return survive;
  }
 }
 return survive;
}
U edge_mask(const array<int,5>& a) {U f=0;for(int e:a)f|=1ull<<e;return f;}
int star_count(U f) {
 int n=0;
 for(int v=0;v<V;v++){
  U s=0;for(int e=0;e<E;e++)if(edge[e].first==v||edge[e].second==v)s|=1ull<<e;
  if((f&s)==s)n++;
 }
 return n;
}
int main(){
 for(int v=0;v<V;v++)closed[v]=1ull<<v;
 for(auto [u,v]:edge){adj[u]|=1ull<<v;adj[v]|=1ull<<u;mat[u][v]=mat[v][u]=true;closed[u]|=1ull<<v;closed[v]|=1ull<<u;}
 for(int v=0;v<V;v++)assert(__builtin_popcountll(adj[v])==3);
 // As the graph is cubic, a set of at most five vertices cannot dominate
 // all 24 vertices. Explicitly exclude six- and seven-vertex dominating sets.
 size_t small_checked=0;
 for(U d=0;d<(1ull<<V);d++) if(__builtin_popcountll(d)==6 || __builtin_popcountll(d)==7) {
  U cover=0,r=d;while(r){int v=__builtin_ctzll(r);r&=r-1;cover|=closed[v];}
  assert(cover!=((1ull<<V)-1));small_checked++;
 }
 assert(small_checked==480700);
 // Full direct closed-neighborhood test, independent of the bundle formulation.
 for(U d=0;d<(1ull<<V);d++) if(__builtin_popcountll(d)==8) {
  U c=0,r=d;while(r){int v=__builtin_ctzll(r);r&=r-1;c|=closed[v];}
  if(c==((1ull<<V)-1))dom8.push_back(d);
 }
 assert(dom8.size()==1767);
 size_t checked4=0;int smallest_survival=1767;
 for(int a=0;a<E;a++)for(int b=a+1;b<E;b++)for(int c=b+1;c<E;c++)for(int d=c+1;d<E;d++){
  U f=(1ull<<a)|(1ull<<b)|(1ull<<c)|(1ull<<d);
  int s=survivor_count(f,false);smallest_survival=min(smallest_survival,s);checked4++;
 }
 assert(checked4==58905 && smallest_survival==5);
 size_t checked5=0;int withoutstar=0,double_star=0;
 int localcounts[V]={};
 for(int a=0;a<E;a++)for(int b=a+1;b<E;b++)for(int c=b+1;c<E;c++)for(int d=c+1;d<E;d++)for(int e=d+1;e<E;e++){
  array<int,5> fidx={a,b,c,d,e};U f=edge_mask(fidx);
  if(survivor_count(f)==0) {
   optimal.push_back(fidx);
   int ns=star_count(f);assert(ns==1 || ns==2);if(ns==0)withoutstar++;if(ns==2)double_star++;
   for(int v=0;v<V;v++){
    U star=0;for(int k=0;k<E;k++)if(edge[k].first==v||edge[k].second==v)star|=1ull<<k;
    if((f&star)==star)localcounts[v]++;
   }
  }
  checked5++;
 }
 assert(checked5==376992 && optimal.size()==276 && withoutstar==0 && double_star==36);
 for(int v=0;v<V;v++)assert(localcounts[v]==13);
 // All automorphisms, verified by pairwise adjacency constraints against an entirely
 // deterministic vertex order; no graph-isomorphism library is used.
 queue<int> q;array<bool,V> vis{};q.push(0);vis[0]=true;
 while(!q.empty()){int u=q.front();q.pop();bfsorder.push_back(u);for(int v=0;v<V;v++)if(mat[u][v]&&!vis[v]){vis[v]=true;q.push(v);}}
 assert(bfsorder.size()==V);
 fill(mapped,mapped+V,-1);fill(used,used+V,0);enumerate_autos(0);
 assert(automorphisms.size()==48);
 map<pair<int,int>,int> eid;
 for(int e=0;e<E;e++)eid[edge[e]]=e;
 vector<array<int,E>> transforms;
 for(auto a:automorphisms){array<int,E> trans{};
  for(int e=0;e<E;e++){int u=a[edge[e].first],v=a[edge[e].second];if(u>v)swap(u,v);auto it=eid.find({u,v});assert(it!=eid.end());trans[e]=it->second;}
  transforms.push_back(trans);
 }
 set<array<int,5>> unseen(optimal.begin(),optimal.end());
 vector<pair<int,array<int,5>>> orbit_types;
 while(!unseen.empty()){
  auto s=*unseen.begin();set<array<int,5>> orb;
  for(auto trans:transforms){array<int,5> t{};for(int i=0;i<5;i++)t[i]=trans[s[i]];sort(t.begin(),t.end());orb.insert(t);}
  for(auto t:orb){assert(unseen.count(t));unseen.erase(t);}
  orbit_types.push_back({(int)orb.size(),*orb.begin()});
 }
 sort(orbit_types.begin(),orbit_types.end());
 assert(orbit_types.size()==8);
 vector<int> sizes;for(auto [sz,rep]:orbit_types)sizes.push_back(sz);
 assert((sizes==vector<int>{12,24,24,24,48,48,48,48}));
 // For each orbit one nine-vertex dominating set after deletion suffices to
 // establish that every optimal five-edge deletion raises gamma to exactly nine.
 for(auto [sz,rep]:orbit_types){
  U f=edge_mask(rep);array<U,V> n=closed;
  for(int e:rep){int u=edge[e].first,v=edge[e].second;n[u]&=~(1ull<<v);n[v]&=~(1ull<<u);}
  bool nine=false;U nineset=0;
  for(U s=0;s<(1ull<<V);s++)if(__builtin_popcountll(s)==9){U cover=0,r=s;while(r){int v=__builtin_ctzll(r);r&=r-1;cover|=n[v];}if(cover==((1ull<<V)-1)){nine=true;nineset=s;break;}}
  assert(nine);
  cout<<"nine_vertex_witness_for_orbit";for(int e:rep)cout<<"_"<<e;cout<<":";for(int v=0;v<V;v++)if(nineset&(1ull<<v))cout<<" "<<v;cout<<"\n";
 }
 cout<<"ALL CHECKS PASSED\n";
 cout<<"checked_six_seven="<<small_checked<<"; gamma8_sets="<<dom8.size()<<"; four_edge_sets="<<checked4<<"; min_four_edge_survivors="<<smallest_survival<<"\n";
 cout<<"five_edge_sets="<<checked5<<"; bondage_sets="<<optimal.size()<<"; no_star="<<withoutstar<<"; two_stars="<<double_star<<"\n";
 cout<<"star_extensions_per_vertex=13; automorphisms="<<automorphisms.size()<<"; orbit_sizes=12,24,24,24,48,48,48,48\n";
 cout<<"orbit_representatives_edge_indices_zero_based:\n";
 for(auto [sz,rep]:orbit_types){cout<<sz<<":";for(int e:rep)cout<<" "<<e;cout<<"\n";}
 cout<<"star_vertex_zero_extension_pairs:\n";
 for(auto a:optimal){U f=edge_mask(a);if((f&7)==7){cout<<a[3]<<" "<<a[4]<<"\n";}}
}
