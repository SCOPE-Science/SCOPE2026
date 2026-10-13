// Independent exact enumeration of one-factorizations and complementary 2-factors.
// Copyright-free mathematical verification; requires a standard C++17 compiler.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <tuple>
using namespace std;
using U=uint64_t;
vector<pair<int,int>> duads,edges;
vector<vector<int>> synthemes;
vector<vector<int>> adj(30);
vector<U> matchbits;
map<pair<int,int>,int> edgeidx;

void k6match(vector<int> left,vector<int> chosen){
 if(left.empty()){sort(chosen.begin(),chosen.end());synthemes.push_back(chosen);return;}
 int a=left[0];
 for(int i=1;i<(int)left.size();++i){
  int b=left[i];auto next=left;next.erase(next.begin()+i);next.erase(next.begin());
  auto x=make_pair(a,b);int eid=find(duads.begin(),duads.end(),x)-duads.begin();
  assert(eid<15); auto cur=chosen;cur.push_back(eid);
  k6match(next,cur);
 }
}
void matching_recur(int i,U used,U chosen){
 if(i==15){matchbits.push_back(chosen);return;}
 for(int v:adj[i]) if(!(used&(U(1)<<(v-15)))){
  matching_recur(i+1,used|(U(1)<<(v-15)),chosen|(U(1)<<edgeidx.at({i,v})));
 }
}
vector<int> cycle_type(U matching){
 auto rem=adj;
 for(int k=0;k<45;++k) if(matching&(U(1)<<k)){
  auto [a,b]=edges[k];rem[a].erase(find(rem[a].begin(),rem[a].end(),b));
  rem[b].erase(find(rem[b].begin(),rem[b].end(),a));
 }
 int seen[30]={};vector<int> sizes;
 for(int s=0;s<30;++s) if(!seen[s]){
  vector<int> stack={s};seen[s]=1;int count=0;
  while(!stack.empty()){
   int v=stack.back();stack.pop_back();++count;
   for(int w:rem[v]) if(!seen[w]) {seen[w]=1;stack.push_back(w);}
  }
  sizes.push_back(count);
 }
 sort(sizes.begin(),sizes.end());return sizes;
}
int main(){
 for(int i=0;i<6;++i) for(int j=i+1;j<6;++j) duads.emplace_back(i,j);
 k6match({0,1,2,3,4,5},{});
 sort(synthemes.begin(),synthemes.end());
 assert(synthemes.size()==15);
 for(int j=0;j<15;++j)for(int d:synthemes[j]){
  adj[d].push_back(15+j);adj[15+j].push_back(d);
 }
 for(int i=0;i<15;++i){sort(adj[i].begin(),adj[i].end());for(int j:adj[i])edges.emplace_back(i,j);}
 assert(edges.size()==45);
 for(int k=0;k<45;++k)edgeidx[edges[k]]=k;
 matching_recur(0,0,0);
 set<U> uniq(matchbits.begin(),matchbits.end());assert(uniq.size()==matchbits.size());
 map<vector<int>,int> cyct;map<U,vector<int>> part;
 for(U m:uniq){auto c=cycle_type(m);cyct[c]++;part[m]=c;}
 assert(uniq.size()==288);
 assert((cyct[vector<int>{10,20}]==144 && cyct[vector<int>{30}]==144));
 set<array<U,3>> facs;
 U all=(U(1)<<45)-1;
 for(U m:uniq) for(U q:uniq) if(!(m&q)) {
  U r=all^m^q;
  if(uniq.count(r) && !(m&r) && !(q&r)){
   array<U,3> f={m,q,r}; sort(f.begin(),f.end());facs.insert(f);
  }
 }
 assert(facs.size()==144);
 for(const auto& f:facs){
  map<vector<int>,int> types;
  for(U m:f)types[part.at(m)]++;
  assert((types[vector<int>{30}]==1 && types[vector<int>{10,20}]==2));
 }
 cout<<"VERIFY_CPP_OK graph=30_vertices_45_edges K6_duads_synthemes\n";
 cout<<"VERIFY_CPP_OK perfect_matchings=288 cycle_types_30=144 cycle_types_10+20=144\n";
 cout<<"VERIFY_CPP_OK factorization_triples=144 named_colorings=864 every_factorization_type=30+10+20+10+20\n";
}
