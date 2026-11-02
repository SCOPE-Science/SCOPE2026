// Exact independent enumeration of toric type-A Bruhat intervals by forbidden rank-three subintervals.
// Compile: c++ -O3 -std=c++17 VERIFY_CROWN.cpp -o verify_crown; ./verify_crown 7
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct Pm {array<unsigned char,8> x{}; array<unsigned char,64> rankmat{}; int len=0; vector<int> cover_up,cover_down;};
int n,N; vector<Pm> p; vector<unsigned char> comp,bad; vector<vector<uint64_t>> upper,lower;
int ord(const array<unsigned char,8>& a){int r=0;for(int i=0;i<n;i++){int c=0;for(int j=i+1;j<n;j++)c+=(a[j]<a[i]);r=r*(n-i)+c;}return r;}
inline bool order(int a,int b){if(p[a].len>p[b].len)return false;for(int i=1;i<n;i++)for(int j=0;j<n;j++)if(p[a].rankmat[i*8+j]<p[b].rankmat[i*8+j])return false;return true;}
int main(int argc,char**argv){n=argc>1?atoi(argv[1]):7; array<unsigned char,8>a{};iota(a.begin(),a.begin()+n,0);
 do{Pm q;q.x=a;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)q.len+=(a[i]>a[j]);for(int i=1;i<n;i++)for(int j=0;j<n;j++)q.rankmat[i*8+j]=q.rankmat[(i-1)*8+j]+(a[i-1]<=j);p.push_back(q);}while(next_permutation(a.begin(),a.begin()+n));N=p.size();
 for(int i=0;i<N;i++)for(int x=0;x<n;x++)for(int y=x+1;y<n;y++)if(p[i].x[x]<p[i].x[y]){bool cover=true;for(int z=x+1;z<y;z++)if(p[i].x[x]<p[i].x[z]&&p[i].x[z]<p[i].x[y])cover=false;if(cover){auto v=p[i].x;swap(v[x],v[y]);int j=ord(v);if(p[i].len+1!=p[j].len){cerr<<"BAD_COVER\n";return 2;}p[i].cover_up.push_back(j);p[j].cover_down.push_back(i);}}
 vector<vector<int>> layer(n*(n-1)/2+1);for(int i=0;i<N;i++)layer[p[i].len].push_back(i);
 comp.resize((size_t)N*N);bad.resize((size_t)N*N);upper.assign(N,vector<uint64_t>((N+63)/64));lower.assign(N,vector<uint64_t>((N+63)/64));for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(order(i,j)){comp[(size_t)i*N+j]=1;upper[i][j/64]|=1ULL<<(j%64);lower[j][i/64]|=1ULL<<(i%64);}
 vector<long long> toric(layer.size()), boolean(layer.size());long long bad3=0;
 for(int d=0;d<(int)layer.size();d++)for(int i=0;i<N;i++)if(p[i].len+d<(int)layer.size())for(int j:layer[p[i].len+d]){
  size_t ij=(size_t)i*N+j;if(!comp[ij])continue;
  bool bb=false;if(d==3){int cnt=0;for(int k:p[i].cover_up)cnt+=comp[(size_t)k*N+j];int n_interval=0;for(int z=0;z<(N+63)/64;z++)n_interval+=__builtin_popcountll(upper[i][z]&lower[j][z]);if((cnt==2&&n_interval!=6)||(cnt!=2&&n_interval==6)){cerr<<"BAD_RANK3_SHAPE "<<i<<" "<<j<<" cnt="<<cnt<<" size="<<n_interval<<" len="<<p[i].len<<"->"<<p[j].len<<"\n";return 3;}bb=(cnt==2);bad3+=bb;}
  else if(d>3){for(int k:p[i].cover_up)if(comp[(size_t)k*N+j]&&bad[(size_t)k*N+j]){bb=true;break;}if(!bb)for(int k:p[j].cover_down)if(comp[(size_t)i*N+k]&&bad[(size_t)i*N+k]){bb=true;break;}}
  bad[ij]=bb;if(!bb){toric[d]++;int size=0;for(int k=0;k<(N+63)/64;k++)size+=__builtin_popcountll(upper[i][k]&lower[j][k]);if(size==(1<<d))boolean[d]++;}
 }
 long long total=accumulate(toric.begin(),toric.end(),0LL);cout<<"N "<<n<<" PERMS "<<N<<" TORIC "<<total<<" BAD3 "<<bad3<<"\n";for(int d=0;d<(int)toric.size();d++)if(toric[d])cout<<d<<" "<<toric[d]<<" "<<boolean[d]<<" "<<toric[d]-boolean[d]<<"\n";
 if(n==7){long long t[]={5040,33984,111910,229848,312552,276604,146138,37852,3448,64};long long b[]={5040,33984,111910,223704,286108,231484,111064,27484,2736,64};if(total!=1157440){cerr<<"TOTAL_MISMATCH\n";return 1;}for(int d=0;d<=9;d++)if(toric[d]!=t[d]||boolean[d]!=b[d]){cerr<<"MISMATCH_AT_"<<d<<"\n";return 1;}for(int d=10;d<(int)toric.size();d++)if(toric[d]){cerr<<"HIGH_DIMENSION_MISMATCH\n";return 1;}}
 cout<<"VERIFY_OK\n";
}
