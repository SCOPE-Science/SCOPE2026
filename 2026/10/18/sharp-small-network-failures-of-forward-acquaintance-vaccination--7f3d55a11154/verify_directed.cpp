// Exact enumeration of directed contact-network vaccination outcomes.
// Compile: g++ -O3 -std=c++17 verify_directed.cpp -o verify_directed
// Run: ./verify_directed
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <utility>
#include <vector>
using namespace std;
using Arc = pair<int,int>;
static const vector<Arc> small_witness={{0,1},{0,2},{1,0},{1,2},{1,3},{2,3},{3,0}};
static const vector<Arc> saturated_witness={{0,1},{0,3},{1,2},{1,3},{2,3},{2,4},{3,1},{4,0}};

vector<Arc> all_arcs(int n) {
 vector<Arc> e;for(int u=0;u<n;u++)for(int v=0;v<n;v++)if(v!=u)e.emplace_back(u,v);return e;
}
uint32_t arcs_mask(int n, const vector<Arc>& chosen) {
 auto all=all_arcs(n);uint32_t m=0;
 for(const auto& [u,v]:chosen){auto it=find(all.begin(),all.end(),Arc(u,v));assert(it!=all.end());m |= uint32_t(1) << (it-all.begin());}
 return m;
}
set<uint32_t> relabel_orbit(int n,const vector<Arc>& arcs){
 vector<int> p(n);iota(p.begin(),p.end(),0);set<uint32_t> masks;
 do{vector<Arc> changed;for(auto [u,v]:arcs)changed.emplace_back(p[u],p[v]);masks.insert(arcs_mask(n,changed));}while(next_permutation(p.begin(),p.end()));
 return masks;
}
struct Graph {
 int n,m;uint32_t encoding; vector<Arc> edges;array<int,5> out={},deg={},bias={};
};
Graph construct(int n,uint32_t encoding,int L){
 Graph g;g.n=n;g.encoding=encoding;auto all=all_arcs(n);
 for(size_t i=0;i<all.size();i++)if((encoding>>i)&1){auto [u,v]=all[i];g.edges.emplace_back(u,v);g.out[u] |= 1<<v;g.deg[u]++;}
 g.m=g.edges.size();
 for(int u=0;u<n;u++)if(g.deg[u])for(int v=0;v<n;v++)if((g.out[u]>>v)&1)g.bias[v]+=L/g.deg[u];
 for(int v=0;v<n;v++)g.bias[v]-=L;
 return g;
}
bool strongly_connected(const Graph& g){
 int n=g.n,all=(1<<n)-1;
 for(int u=0;u<n;u++)if(g.deg[u]==0)return false;
 for(int s=0;s<n;s++){
  int seen=1<<s,old=-1;
  while(old!=seen){old=seen;for(int u=0;u<n;u++)if((seen>>u)&1)seen|=g.out[u];}
  if(seen!=all)return false;
 }
 return true;
}
// R_v(F): sum of all directed reachable-set cardinalities after deleting v.
int reachable_sum(const array<int,5>& live,int n,int excluded){
 int active=((1<<n)-1)^(1<<excluded),sum=0;
 for(int s=0;s<n;s++)if(s!=excluded){
  int seen=1<<s,old=-1;
  while(old!=seen){old=seen;for(int u=0;u<n;u++)if((seen>>u)&1)seen|=live[u]&active;}
  sum+=__builtin_popcount((unsigned)seen);
 }
 return sum;
}
long long complete_transmission_numerator(const Graph& g){
 long long value=0;for(int v=0;v<g.n;v++)value+=(long long)g.bias[v]*reachable_sum(g.out,g.n,v);return value;
}
vector<long long> signed_bernstein_coefficients(const Graph& g){
 int m=g.m;vector<long long>b(m+1,0);assert(m<=12);
 for(int subset=0;subset<(1<<m);subset++){
  array<int,5> live={};for(int k=0;k<m;k++)if((subset>>k)&1){auto [u,v]=g.edges[k];live[u]|=1<<v;}
  long long score=0;for(int v=0;v<g.n;v++)score+=(long long)g.bias[v]*reachable_sum(live,g.n,v);
  b[__builtin_popcount((unsigned)subset)]+=score;
 }
 return b;
}
long long choose(int n,int k){if(k<0||k>n)return 0;long long v=1;for(int i=1;i<=k;i++)v=v*(n-i+1)/i;return v;}
vector<long long> power_coefficients(const vector<long long>& b){
 int m=(int)b.size()-1;vector<long long> c(m+1,0);
 for(int j=0;j<=m;j++)for(int k=0;k<=j;k++){
  long long add=b[k]*choose(m-k,j-k);
  if((j-k)&1)add=-add;
  c[j]+=add;
 }
 return c;
}
void test(){
 auto four_orbit=relabel_orbit(4,small_witness);
 auto five_orbit=relabel_orbit(5,saturated_witness);
 assert(four_orbit.size()==24 && five_orbit.size()==120);
 const vector<long long> four_bern={0,1,0,-20,-60,-75,-44,-10};
 const vector<long long> four_power={0,1,-6,-5,0,0,0,0};
 const vector<long long> five_bern={0,-18,-150,-486,-786,-660,-252,-12,12};
 const vector<long long> five_power={0,-18,-24,36,24,-6,0,0,0};
 auto four=construct(4,arcs_mask(4,small_witness),6);
 auto five=construct(5,arcs_mask(5,saturated_witness),12);
 assert(strongly_connected(four) && strongly_connected(five));
 assert(signed_bernstein_coefficients(four)==four_bern);
 assert(power_coefficients(four_bern)==four_power);
 assert(signed_bernstein_coefficients(five)==five_bern);
 assert(power_coefficients(five_bern)==five_power);
 assert(complete_transmission_numerator(four)==-10); // -10/(4*6*3)=-5/36.
 assert(complete_transmission_numerator(five)==12); // 12/(5*12*4)=1/20.
 long long total_states=0;
 for(int n=2;n<=4;n++){
  int L=n==4?6:2;int pairs=n*(n-1),checked=0,exceptional=0;
  for(uint32_t bits=0;bits<(uint32_t(1)<<pairs);bits++){
   Graph g=construct(n,bits,L);if(!strongly_connected(g))continue;checked++;
   auto coeff=signed_bernstein_coefficients(g);total_states+=uint64_t(1)<<g.m;
   bool has_positive=any_of(coeff.begin(),coeff.end(),[](long long z){return z>0;});
   if(has_positive){exceptional++;assert(n==4);assert(four_orbit.count(bits));assert(coeff==four_bern);}
   else{for(long long z:coeff)assert(z<=0);}
  }
  if(n==2)assert(checked==1 && exceptional==0);
  if(n==3)assert(checked==18 && exceptional==0);
  if(n==4)assert(checked==1606 && exceptional==24);
  cout<<"small_order n="<<n<<" strongly_connected="<<checked<<" exceptional="<<exceptional<<"\n";
 }
 cout<<"small_order_edge_configurations="<<total_states<<"\n";
 int checked=0,positive=0,minedge=100,min_count=0;
 for(uint32_t bits=0;bits<(1u<<20);bits++){
  Graph g=construct(5,bits,12);if(!strongly_connected(g))continue;checked++;
  long long diff=complete_transmission_numerator(g);
  if(diff>0){positive++;if(g.m<minedge){minedge=g.m;min_count=0;}if(g.m==minedge){min_count++;assert(five_orbit.count(bits));assert(diff==12);}}
 }
 assert(checked==565080 && positive==15180 && minedge==8 && min_count==120);
 cout<<"saturated n=5 strongly_connected="<<checked<<" harmful="<<positive<<" minimum_arcs="<<minedge<<" minimizing_labeled_graphs="<<min_count<<"\n";
 cout<<"four_graph_gap=p*(1-6*p-5*p^2)/72\n";
 cout<<"five_graph_gap=(-18*p-24*p^2+36*p^3+24*p^4-6*p^5)/240\n";
 cout<<"PASS\n";
}
int main(){test();}
