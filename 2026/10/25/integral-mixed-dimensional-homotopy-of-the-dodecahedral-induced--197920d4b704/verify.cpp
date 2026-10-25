#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

// Exact finite certificate for the vertex-induced acyclic-subgraph complex
// of the generalized Petersen graph GP(10,2).
constexpr int N_VERT=20;
constexpr int N=1<<N_VERT;
using Vec = vector<long long>;
using Mat = vector<Vec>;
int pc(int m){return __builtin_popcount(static_cast<unsigned>(m));}
vector<pair<int,int>> graph_edges(){
 vector<pair<int,int>> e;
 for(int i=0;i<10;i++){
  e.push_back({i,(i+1)%10});
  e.push_back({10+i,10+(i+2)%10});
  e.push_back({i,10+i});
 }
 return e;
}
array<uint32_t,N_VERT> adjacency(){
 array<uint32_t,N_VERT> a{};
 for(auto [u,v]:graph_edges()){a[u]|=1u<<v;a[v]|=1u<<u;}
 return a;
}

bool forest_dsu(unsigned mask,const array<uint32_t,N_VERT>& adj){
 int parent[N_VERT];
 for(int i=0;i<N_VERT;i++)parent[i]=i;
 auto root=[&](int v){while(parent[v]!=v){parent[v]=parent[parent[v]];v=parent[v];}return v;};
 for(int i=0;i<N_VERT;i++)if(mask&(1u<<i)){
  unsigned nb=mask & adj[i] & (~((1u<<(i+1))-1u));
  while(nb){int j=__builtin_ctz(nb);nb&=nb-1;
   int x=root(i),y=root(j);
   if(x==y)return false;
   parent[x]=y;
  }
 }
 return true;
}

bool forest_search(unsigned mask,const array<uint32_t,N_VERT>& adj){
 unsigned seen=0;
 for(int v=0;v<N_VERT;v++)if((mask&(1u<<v))&&!(seen&(1u<<v))){
  int stack[N_VERT],parent[N_VERT],top=1;
  stack[0]=v; parent[v]=-1;seen|=1u<<v;
  while(top){int u=stack[--top];
   unsigned nb=mask&adj[u];
   while(nb){int w=__builtin_ctz(nb);nb&=nb-1;
    if(!(seen&(1u<<w))){seen|=1u<<w;parent[w]=u;stack[top++]=w;}
    else if(w!=parent[u])return false;
   }
  }
 }
 return true;
}
// Enumerates signed codimension-one faces, using increasing vertex order.
template<class F> void faces(int m,F action){
 int t=m,pos=0;
 while(t){int bit=t&-t;t-=bit;action(m^bit,(pos&1)?-1:1);pos++;}
}
int main(){
 auto adj=adjacency();
 vector<uint8_t> good(N,0);
 array<long long,21> f{};
 long long count=0;
 for(int mask=0;mask<N;mask++){
  bool b=forest_dsu(static_cast<unsigned>(mask),adj);
  if(b!=forest_search(static_cast<unsigned>(mask),adj))throw runtime_error("independent forest tests differ");
  good[mask]=b;
  if(b){f[pc(mask)]++;count++;}
 }
 if(count!=755608)throw runtime_error("face count mismatch");
 vector<int> mate(N,-1);
 for(int v=0;v<N_VERT;v++){
  int bit=1<<v;
  for(int m=0;m<N;m++)
   if(!(m&bit)&&good[m]&&good[m|bit]&&mate[m]<0&&mate[m|bit]<0){
    mate[m]=m|bit;mate[m|bit]=m;
   }
 }
 vector<int> lower,upper;
 for(int m=0;m<N;m++)if(good[m]&&mate[m]<0){
  if(pc(m)==12)lower.push_back(m);
  else if(pc(m)==13)upper.push_back(m);
  else throw runtime_error("critical cell outside sizes 12 and 13");
 }
 if(lower.size()!=34||upper.size()!=90)throw runtime_error("critical cell counts differ");
 // Orient unmatched Hasse edges downward and matched Hasse edges upward.
 vector<int> indeg(N,0);
 long long incidences=0;
 for(int m=1;m<N;m++)if(good[m])faces(m,[&](int lo,int){
  incidences++;
  if(mate[lo]==m)indeg[m]++;
  else indeg[lo]++;
 });
 vector<int> queue;queue.reserve(count);
 for(int m=0;m<N;m++)if(good[m]&&!indeg[m])queue.push_back(m);
 for(size_t p=0;p<queue.size();p++){
  int m=queue[p];
  if(mate[m]>m&&--indeg[mate[m]]==0)queue.push_back(mate[m]);
  faces(m,[&](int lo,int){if(mate[lo]!=m&&--indeg[lo]==0)queue.push_back(lo);});
 }
 if(queue.size()!=static_cast<size_t>(count))throw runtime_error("matching is not acyclic");
 if(incidences!=6967280)throw runtime_error("incidence count mismatch");
 // Integral algebraic Morse reduction of the single potentially nonzero differential.
 unordered_map<int,int> target;
 for(int j=0;j<(int)lower.size();j++)target[lower[j]]=j;
 unordered_map<int,Vec> cache;
 cache.reserve(55000);
 const int d=static_cast<int>(lower.size());
 function<const Vec&(int)> reduce=[&](int face)->const Vec&{
  auto it=cache.find(face);
  if(it!=cache.end())return it->second;
  Vec ans(d,0);
  auto ci=target.find(face);
  if(ci!=target.end())ans[ci->second]=1;
  else if(mate[face]<0)throw runtime_error("unknown unpaired face");
  else if(pc(mate[face])==pc(face)+1){
   int u=mate[face],pair_sign=0;
   faces(u,[&](int t,int s){if(t==face)pair_sign=s;});
   if(!pair_sign)throw runtime_error("missing paired incidence");
   faces(u,[&](int t,int s){
    if(t==face)return;
    Vec other=reduce(t);
    for(int j=0;j<d;j++)ans[j]-=pair_sign*s*other[j];
   });
  }
  auto ret=cache.emplace(face,std::move(ans));
  return ret.first->second;
 };
 Mat M(d,Vec(upper.size(),0));
 for(int c=0;c<(int)upper.size();c++)faces(upper[c],[&](int lo,int s){
  Vec b=reduce(lo);
  for(int j=0;j<d;j++)M[j][c]+=s*b[j];
 });
 long long nnz=0,maxcoef=0;
 for(auto& row:M)for(long long x:row){nnz+=(x!=0);maxcoef=max(maxcoef,llabs(x));}
 if(nnz!=125||maxcoef!=1)throw runtime_error("Morse matrix invariant mismatch");
 // Integer elementary row/column operations: each pivot is a unit.  The
 // final zero residual and 24 unit pivots certify the exact Smith form.
 Mat S=M;
 int rank=0,R=d,C=(int)upper.size();
 while(rank<min(R,C)){
  int pr=-1,pc=-1;
  for(int i=rank;i<R&&pr<0;i++)for(int j=rank;j<C;j++)if(llabs(S[i][j])==1){pr=i;pc=j;break;}
  if(pr<0)break;
  swap(S[pr],S[rank]);
  for(auto& row:S)swap(row[pc],row[rank]);
  if(S[rank][rank]==-1)for(auto& x:S[rank])x=-x;
  for(int i=rank+1;i<R;i++)if(S[i][rank]){
   long long multiplier=S[i][rank];
   for(int j=rank;j<C;j++)S[i][j]-=multiplier*S[rank][j];
  }
  for(int j=rank+1;j<C;j++)if(S[rank][j]){
   long long multiplier=S[rank][j];
   for(int i=rank;i<R;i++)S[i][j]-=multiplier*S[i][rank];
  }
  rank++;
 }
 for(int i=rank;i<R;i++)for(int j=rank;j<C;j++)if(S[i][j])throw runtime_error("remaining nonunit invariant");
 if(rank!=24)throw runtime_error("unexpected rank");
 cout<<"GRAPH_GP_10_2 vertices=20 edges=30\n";
 cout<<"FOREST_FACE_COUNT "<<count<<"\n";
 cout<<"FACE_COUNTS_BY_CARDINALITY";
 for(int k=0;k<=20;k++)if(f[k])cout<<" "<<k<<":"<<f[k];
 cout<<"\nMATCHING_PAIRS "<<(count-lower.size()-upper.size())/2<<"\n";
 cout<<"CRITICAL_NONEMPTY dimension11="<<lower.size()<<" dimension12="<<upper.size()<<"\n";
 cout<<"HASSE_DAG acyclic="<<queue.size()<<" incidences="<<incidences<<"\n";
 cout<<"MORSE_BOUNDARY shape=34x90 nonzero="<<nnz<<" max_abs="<<maxcoef<<"\n";
 cout<<"INTEGER_SMITH_DIAGONAL unit="<<rank<<" zero="<<d-rank<<"\n";
 cout<<"REDUCED_BETTI degree11="<<d-rank<<" degree12="<<upper.size()-rank<<"\n";
 cout<<"VERIFY_OK\n";
 return 0;
}
