// Independent exact integral census of eight-vertex tournament neighborhood complexes.
// Compile: c++ -std=c++17 -O2 verify_t8.cpp -o verify_t8 && ./verify_t8
// Uses only the C++ standard library.
#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using Rows = array<int,8>;
struct Key {array<int,8> entries{}; bool operator==(Key const& b) const {return entries==b.entries;}};
struct Hash {size_t operator()(Key const& x) const {
 size_t h=17;for(int y:x.entries)h=h*131+y;return h;
}};
Key invariant(Rows const& a,int n){
 Key k{};
 for(int i=0;i<n;i++){
  int cycles=0;
  for(int j=0;j<n;j++)if((a[i]>>j)&1)
   for(int t=0;t<n;t++)if(((a[j]>>t)&1)&&((a[t]>>i)&1))cycles++;
  k.entries[i]=100*__builtin_popcount((unsigned)a[i])+cycles;
 }
 sort(k.entries.begin(),k.entries.begin()+n);
 return k;
}
bool iso_step(Rows const&a,Rows const&b,vector<int>const&order,
              vector<vector<int>>const&possible,int d,int used,int mapto[8]){
 const int n=order.size();if(d==n)return true;
 int v=order[d];
 for(int w:possible[v])if(!(used>>w&1)){
  bool good=true;
  for(int j=0;j<d;j++){
   int u=order[j];if(((a[v]>>u)&1)!=((b[w]>>mapto[u])&1)){good=false;break;}
  }
  if(good){mapto[v]=w;if(iso_step(a,b,order,possible,d+1,used|(1<<w),mapto))return true;}
 }
 return false;
}
bool isomorphic(Rows const&a,Rows const&b,int n){
 if(!(invariant(a,n)==invariant(b,n)))return false;
 vector<int>sa(n),sb(n);
 auto label=[&](Rows const&x,int i){
  int cycles=0;for(int j=0;j<n;j++)if(x[i]>>j&1)
   for(int t=0;t<n;t++)if((x[j]>>t&1)&&(x[t]>>i&1))cycles++;
  return __builtin_popcount((unsigned)x[i])*100+cycles;
 };
 for(int i=0;i<n;i++){sa[i]=label(a,i);sb[i]=label(b,i);}
 vector<vector<int>>possible(n);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(sa[i]==sb[j])possible[i].push_back(j);
 vector<int>ord(n);iota(ord.begin(),ord.end(),0);
 sort(ord.begin(),ord.end(),[&](int i,int j){return possible[i].size()<possible[j].size();});
 int mapto[8]={};return iso_step(a,b,ord,possible,0,0,mapto);
}
Rows add_vertex(Rows const&a,int n,int pattern){
 Rows b{};
 for(int i=0;i<n;i++){
  b[i]=a[i]|(((pattern>>i)&1)<<n);
  if(!((pattern>>i)&1))b[n]|=1<<i;
 }
 return b;
}
vector<Rows> all_tournaments(int n){
 vector<Rows> reps(1); // one-vertex tournament
 const int census[]={0,1,1,2,4,12,56,456,6880};
 for(int m=1;m<n;m++){
  unordered_map<Key,vector<Rows>,Hash> buckets;
  for(Rows const& a:reps)for(int mask=0;mask<(1<<m);mask++){
   Rows b=add_vertex(a,m,mask);
   auto& choices=buckets[invariant(b,m+1)];
   bool dup=false;
   for(Rows const& other:choices)if(isomorphic(b,other,m+1)){dup=true;break;}
   if(!dup)choices.push_back(b);
  }
  reps.clear();for(auto const& p:buckets)for(Rows const& a:p.second)reps.push_back(a);
  if(int(reps.size())!=census[m+1]){
   cerr<<"Wrong tournament class count at order "<<m+1<<"\n";exit(1);
  }
 }
 return reps;
}
struct Reduction{int rank=0;bool residual=false;};
Reduction reduce_unimodular(vector<vector<long long>>mat,int nr,int nc){
 int rk=0;
 while(nr>0&&nc>0){
  int pi=-1,pj=-1;
  for(int i=0;i<nr&&pi<0;i++)for(int j=0;j<nc;j++)
   if(llabs(mat[i][j])==1){pi=i;pj=j;break;}
  if(pi<0)break;
  const long long unit=mat[pi][pj];
  for(int i=0;i<nr;i++)if(i!=pi)for(int j=0;j<nc;j++)if(j!=pj){
   mat[i][j]-=mat[i][pj]*mat[pi][j]*unit;
   if(llabs(mat[i][j])>100000000LL){cerr<<"Integer overflow guard\n";exit(1);}
  }
  swap(mat[pi],mat[nr-1]);
  for(int i=0;i<nr;i++)swap(mat[i][pj],mat[i][nc-1]);
  --nr;--nc;++rk;
 }
 for(int i=0;i<nr;i++)for(int j=0;j<nc;j++)if(mat[i][j])return {rk,true};
 return {rk,false};
}
array<int,8> betti_and_test(Rows const&a){
 vector<vector<int>> faces(9);
 for(int s=1;s<256;s++){
  for(int i=0;i<8;i++)if((s&a[i])==s){faces[__builtin_popcount((unsigned)s)].push_back(s);break;}
 }
 array<int,10> ranks{};
 ranks[1]=!faces[1].empty();
 for(int k=2;k<=8;k++){
  int nr=faces[k-1].size(),nc=faces[k].size();if(!nr||!nc)continue;
  vector<vector<long long>>b(nr,vector<long long>(nc));
  array<int,256> pos{};pos.fill(-1);
  for(int i=0;i<nr;i++)pos[faces[k-1][i]]=i;
  for(int j=0;j<nc;j++){
   int face=faces[k][j],sign=1;
   for(int v=0;v<8;v++)if(face>>v&1){
    int smaller=face^(1<<v);
    if(pos[smaller]<0){cerr<<"Broken simplicial closure\n";exit(1);}
    b[pos[smaller]][j]=sign;sign=-sign;
   }
  }
  Reduction reduced=reduce_unimodular(move(b),nr,nc);
  if(reduced.residual){cerr<<"Nonunit Smith remainder found\n";exit(1);}
  ranks[k]=reduced.rank;
 }
 array<int,8> beta{};
 for(int k=1;k<=8;k++){
  beta[k-1]=int(faces[k].size())-ranks[k]-ranks[k+1];
  if(beta[k-1]<0){cerr<<"Inconsistent boundary rank\n";exit(1);}
 }
 return beta;
}
int main(){
 const auto reps=all_tournaments(8);
 map<array<int,8>,int>hist;
 for(const auto&a:reps)hist[betti_and_test(a)]++;
 map<array<int,8>,int>expected;
 const vector<pair<array<int,3>,int>> target={
   {{{0,0,0}},3558},{{{0,0,1}},394},{{{0,0,2}},60},{{{0,0,3}},2},
   {{{0,1,0}},1602},{{{0,1,1}},218},{{{0,1,2}},17},
   {{{0,2,0}},623},{{{0,2,1}},78},{{{0,2,2}},36},{{{0,2,3}},1},
   {{{0,3,0}},181},{{{0,3,1}},18},{{{0,3,2}},2},
   {{{0,4,0}},26},{{{0,4,1}},2},{{{0,5,0}},3},{{{0,5,1}},2},{{{0,6,0}},1},
   {{{1,0,0}},34},{{{1,0,1}},11},{{{1,0,2}},4},{{{1,0,3}},2},
   {{{1,0,4}},1},{{{1,1,0}},3},{{{1,1,1}},1}};
 for(auto const&p:target){array<int,8>b{};copy(p.first.begin(),p.first.end(),b.begin());expected[b]=p.second;}
 if(hist!=expected||reps.size()!=6880){cerr<<"Incorrect complete spectrum\n";return 1;}
 for(const auto& entry:hist){
  for(int v:entry.first)cout<<v<<',';
  cout<<' '<<entry.second<<'\n';
 }
 cout<<"VERIFY_OK\n";
}
