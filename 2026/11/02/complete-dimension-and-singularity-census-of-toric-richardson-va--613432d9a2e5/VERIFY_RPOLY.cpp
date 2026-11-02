#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct Perm {
 array<unsigned char,8> x{}; unsigned char len=0; array<unsigned char,64> prefix{};
 array<int,7> right{};
};
int n,N;
vector<Perm> P;
vector<unsigned char> cache;
vector<vector<pair<int,int>>> extrema;
long long compares=0;
inline bool leq(int a,int b){
 if(P[a].len>P[b].len) return false;
 for(int k=1;k<n;k++){
  for(int t=0;t<n;t++) if(P[a].prefix[k*8+t]<P[b].prefix[k*8+t])return false;
 }
 return true;
}
int rank_perm(const array<unsigned char,8>& a){
 int code=0;
 for(int i=0;i<n;i++){
  int k=0;for(int j=i+1;j<n;j++) k+=(a[j]<a[i]);
  code=code*(n-i)+k;
 }
 return code;
}
// R_{v,w}(2) capped at 2, 0 if incomparable.
unsigned char r2(int a,int b){
 size_t idx=(size_t)a*N+b;
 if(cache[idx])return cache[idx]-1;
 if(!leq(a,b)){cache[idx]=1;return 0;}
 if(a==b){cache[idx]=2;return 1;}
 int s=-1;for(int k=0;k<n-1;k++)if(P[b].x[k]>P[b].x[k+1]){s=k;break;}
 if(s<0){cerr<<"BAD\n";exit(2);}
 int as=P[a].right[s],bs=P[b].right[s];
 int r;
 if(P[as].len<P[a].len)r=r2(as,bs);
 else r=2*(int)r2(as,bs)+(int)r2(a,bs);
 r=min(r,2);cache[idx]=r+1;return (unsigned char)r;
}
int main(int argc,char**argv){
 n=argc>1?atoi(argv[1]):7;
 array<unsigned char,8> a{};for(int i=0;i<n;i++)a[i]=i;
 do {
  Perm p;p.x=a;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)p.len+=(a[i]>a[j]);
  for(int k=1;k<n;k++)for(int t=0;t<n;t++)p.prefix[k*8+t]=p.prefix[(k-1)*8+t]+(a[k-1]<=t);
  P.push_back(p);
 }while(next_permutation(a.begin(),a.begin()+n));
 N=P.size();
 if(n<2||n>7){cerr<<"ONLY_N_2_TO_7\n";return 2;}
 for(int i=0;i<N;i++)for(int s=0;s<n-1;s++){
  auto x=P[i].x; swap(x[s],x[s+1]);P[i].right[s]=rank_perm(x);
 }
 cache.assign((size_t)N*N,0);
 vector<long long> dist(n*(n-1)/2+1,0);
 int md=-1;vector<pair<int,int>> best;
 for(int a=0;a<N;a++)for(int b=0;b<N;b++){
  int d=(int)P[b].len-(int)P[a].len;
  if(d<0) continue;
  if(r2(a,b)!=1)continue;
  dist[d]++;
  if(d>md){md=d;best.clear();best.emplace_back(a,b);}
  else if(d==md){best.emplace_back(a,b);}
 }
 cout<<"N "<<n<<" #perms "<<N<<" total_toric ";long long total=0;for(auto x:dist)total+=x;cout<<total<<" max_d "<<md<<" extremals "<<best.size()<<"\n";
 cout<<"DIST ";for(int i=0;i<(int)dist.size();i++)if(dist[i])cout<<i<<":"<<dist[i]<<" ";cout<<"\n";
 cout<<"EXTREMAL_BEGIN\n";
 for(auto [i,j]:best){
  int size=0;vector<int> profile(md+1);
  for(int x=0;x<N;x++)if(leq(i,x)&&leq(x,j)) {size++;profile[P[x].len-P[i].len]++;}
  bool cube = size==(1<<md);
  cout<<i<<" "<<j<<" ";for(int k=0;k<n;k++)cout<<(int)P[i].x[k]+1;cout<<" ";for(int k=0;k<n;k++)cout<<(int)P[j].x[k]+1;
  cout<<" size "<<size<<" boolean "<<cube<<" ranks ";for(auto q:profile)cout<<q<<",";cout<<"\n";
 }
 cout<<"EXTREMAL_END\n";
 if(n==7){long long ref[]={5040,33984,111910,229848,312552,276604,146138,37852,3448,64}; if(md!=9||best.size()!=64){cerr<<"BAD_MAXIMUM\n";return 1;}for(int d=0;d<=9;d++)if(dist[d]!=ref[d]){cerr<<"BAD_COUNT\n";return 1;}for(int d=10;d<(int)dist.size();d++)if(dist[d]){cerr<<"BAD_BOUND\n";return 1;}}
 cout<<"VERIFY_OK\n";return 0;
}
