// Standalone exact arithmetic verification of a three-term convolution rank census
// on SL(2, F_5). Compile: g++ -O2 -std=c++17 check.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
using u64 = uint64_t;
using Mat = array<int,4>;
static constexpr int N = 120;
static constexpr u64 PRIMES[4] = {1000000007ULL,1000000009ULL,
                                   998244353ULL,1004535809ULL};
void verify(bool p, const string &what) { if (!p) throw runtime_error(what); }
int residue(int x) {x%=5; return x<0 ? x+5 : x;}
Mat product(const Mat &x,const Mat &y) {
 return {residue(x[0]*y[0]+x[1]*y[2]),
         residue(x[0]*y[1]+x[1]*y[3]),
         residue(x[2]*y[0]+x[3]*y[2]),
         residue(x[2]*y[1]+x[3]*y[3])};
}
struct Group {
 vector<Mat> el; map<Mat,int> label;
 int id; int mul[N][N], inv[N], ord[N], conj[N][N];
 Group() {
  for(int a=0;a<5;a++)for(int b=0;b<5;b++)for(int c=0;c<5;c++)for(int d=0;d<5;d++)
   if(residue(a*d-b*c)==1)el.push_back({a,b,c,d});
  verify(el.size()==N,"incorrect SL(2,5) cardinality");
  sort(el.begin(),el.end());
  for(int i=0;i<N;i++)label[el[i]]=i;
  id=label.at(Mat{1,0,0,1});
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)
   mul[i][j]=label.at(product(el[i],el[j]));
  for(int i=0;i<N;i++){
   int j=0;while(j<N && (mul[i][j]!=id || mul[j][i]!=id))j++;
   verify(j<N,"inverse missing");inv[i]=j;
   int z=i,k=1;
   while(z!=id && k<=N) { z=mul[z][i];k++; }
   verify(k<=N,"finite order invalid");ord[i]=k;
  }
  for(int g=0;g<N;g++)for(int x=0;x<N;x++)
   conj[g][x]=mul[mul[g][x]][inv[g]];
 }
};
bool prime(u64 p){
 if(p<2)return false;
 for(u64 d=2;d*d<=p;d++)if(p%d==0)return false;
 return true;
}
u64 power(u64 a,u64 n,u64 p){
 u64 out=1;
 while(n){if(n&1)out=(out*a)%p;a=(a*a)%p;n>>=1;}
 return out;
}
int mod_rank(const Group &G,int x,int y,u64 p){
 u64 a[N][N] = {};
 for(int h=0;h<N;h++){
  a[h][h]=1;
  a[h][G.mul[G.inv[x]][h]]=1;
  a[h][G.mul[G.inv[y]][h]]=1;
 }
 int rank=0;
 for(int col=0;col<N && rank<N;col++){
  int pivot=rank;
  while(pivot<N && a[pivot][col]==0)pivot++;
  if(pivot==N)continue;
  if(pivot!=rank)for(int j=col;j<N;j++)swap(a[rank][j],a[pivot][j]);
  u64 pinv=power(a[rank][col],p-2,p);
  for(int i=rank+1;i<N;i++)if(a[i][col]){
   u64 factor=(a[i][col]*pinv)%p;
   for(int j=col+1;j<N;j++){
    u64 subtract=(factor*a[rank][j])%p;
    a[i][j]=(a[i][j]+p-subtract)%p;
   }
   a[i][col]=0;
  }
  rank++;
 }
 return rank;
}
int main(){
 try {
  Group G;
  cpp_int modulus=1,bound=1;
  for(u64 p: PRIMES){verify(prime(p),"listed modulus is not prime");modulus*=p;}
  for(int i=0;i<60;i++)bound*=3;
  verify(modulus>bound,"modulus product does not exceed Hadamard bound");
  verify(G.ord[G.id]==1,"identity order incorrect");
  const auto label=[&](int a,int b){if(a>b)swap(a,b);return a*N+b;};
  vector<bool> visited(N*N,false);
  map<array<int,3>,pair<int,long long>> signature;
  map<int,long long> histogram;
  int orbit_count=0, pair_total=0;
  for(int x=0;x<N;x++)if(x!=G.id)
   for(int y=x+1;y<N;y++)if(y!=G.id && !visited[label(x,y)]){
    array<int,3> support={G.id,x,y};
    set<int> orbit;
    for(int base=0;base<3;base++){
     int other[2],k=0;
     for(int t=0;t<3;t++)if(t!=base)
      other[k++]=G.mul[G.inv[support[base]]][support[t]];
     for(int g=0;g<N;g++){
      int a=G.conj[g][other[0]],b=G.conj[g][other[1]];
      verify(a!=b && a!=G.id && b!=G.id,"invalid normalization");
      orbit.insert(label(a,b));
     }
    }
    verify(!orbit.empty(),"empty orbit");
    for(int v:orbit){verify(!visited[v],"orbits overlap");visited[v]=true;}
    pair_total+=(int)orbit.size();orbit_count++;
    array<int,3> sig={G.ord[x],G.ord[y],G.ord[G.mul[G.inv[x]][y]]};
    sort(sig.begin(),sig.end());
    int nullity=-1;
    for(u64 p:PRIMES){
     int q=N-mod_rank(G,x,y,p);
     if(nullity<0)nullity=q;
     verify(q==nullity,"modular ranks unexpectedly differ");
    }
    // Every r-by-r integer minor has modulus <= (sqrt(3))^r <= 3^60.
    // A common modular rank r, across primes of product >3^60, is
    // therefore exactly the rank over Q and C.
    auto &entry=signature[sig];
    if(entry.second==0)entry.first=nullity;
    verify(entry.first==nullity,"one order signature has two nullities");
    long long support_count=(long long)orbit.size()*N/3;
    entry.second+=support_count;
    histogram[nullity]+=support_count;
   }
  verify(pair_total==7021,"incomplete normalized-pair coverage");
  for(int x=0;x<N;x++)if(x!=G.id)
   for(int y=x+1;y<N;y++)if(y!=G.id)
    verify(visited[label(x,y)],"unvisited pair");
  verify(orbit_count==62,"orbit count changed");
  verify(signature.size()==35,"signature count changed");
  map<int,long long> expected_hist={{0,159240},{4,38400},{5,28800},{10,28800},
   {20,14400},{22,7200},{30,2400},{40,1200},{80,400}};
  verify(histogram==expected_hist,"full nullity census differs");
  long long total=0;for(auto [r,c]:histogram)total+=c;
  verify(total==280840,"support count does not equal C(120,3)");
  // Independent checks on the subtler 22-dimensional regime and maximum.
  verify(signature.at({6,10,10})==make_pair(22,7200LL),"exceptional signature");
  verify(signature.at({3,3,3})==make_pair(80,400LL),"maximal signature");
  cout << "PASS group=SL(2,5), normalized_pairs="<<pair_total
       <<", conjugation/rebasing_orbits="<<orbit_count
       <<", distinct_order_signatures="<<signature.size()<<"\n";
  cout << "Four-prime product="<<modulus<<", Hadamard_bound="<<bound<<"\n";
  cout << "Signature  |  complex nullity  |  supports\n";
  for(auto [t,info]:signature)
   cout << "("<<t[0]<<","<<t[1]<<","<<t[2]<<") "<<info.first<<" "<<info.second<<"\n";
  cout << "Complete nullity census:\n";
  for(auto [r,count]:histogram)cout<<r<<" "<<count<<"\n";
 }catch(const exception &e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
