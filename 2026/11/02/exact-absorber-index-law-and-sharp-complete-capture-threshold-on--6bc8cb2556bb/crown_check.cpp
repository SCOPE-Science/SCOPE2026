// Reproducibility checker for the crown-graph coherent absorption formula.
// Build: c++ -O2 -std=c++17 crown_check.cpp -o crown_check
// Run: ./crown_check
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <random>
#include <set>
#include <vector>
using namespace std;
static const int P=1009;
int power(int x,int y){int r=1;while(y){if(y&1)r=r*x%P;x=x*x%P;y>>=1;}return r;}
int rank_krylov(int n, uint32_t sinks){
 int m=2*n, rank=0;
 vector<vector<int>> piv(m);
 auto incorporate=[&](vector<int> v){
  for(int i=0;i<m;i++){
   if(!v[i])continue;
   if(piv[i].empty()){
    int inv=power(v[i],P-2);
    for(int &x:v)x=x*inv%P;
    piv[i]=std::move(v);rank++;return;
   }
   int factor=v[i];
   for(int j=i;j<m;j++)v[j]=(v[j]-factor*piv[i][j]%P+P)%P;
  }
 };
 for(int t=0;t<m;t++) if(sinks&(1u<<t)){
  vector<int> v(m);v[t]=1;
  for(int p=0;p<m;p++){
   incorporate(v);
   vector<int> w(m);
   for(int i=0;i<n;i++) for(int j=0;j<n;j++)if(i!=j){
    w[i]=(w[i]+v[n+j])%P;
    w[n+i]=(w[n+i]+v[j])%P;
   }
   v.swap(w);
  }
 }
 return rank;
}
int main(){
 long long checks=0;
 for(int n=3;n<=6;n++){
  uint32_t bound=1u<<(2*n);
  for(uint32_t mask=1;mask<bound;mask++){
   int t=0;
   for(int j=0;j<n;j++) if((mask&(1u<<j))||(mask&(1u<<(n+j)))) t++;
   int expected=2+2*min(t,n-1);
   int got=rank_krylov(n,mask);
   if(got!=expected){cerr<<"FAIL n="<<n<<" mask="<<mask<<" expected="<<expected<<" got="<<got<<"\n";return 1;}
   checks++;
  }
 }
 mt19937 rng(277191);
 for(int n=7;n<=12;n++)for(int j=0;j<80;j++){
  uint32_t mask=rng()&((1u<<(2*n))-1u);
  if(!mask)mask=1;
  int t=0;
  for(int k=0;k<n;k++)if((mask&(1u<<k))||(mask&(1u<<(n+k))))t++;
  int expected=2+2*min(t,n-1);
  int got=rank_krylov(n,mask);
  if(got!=expected){cerr<<"FAIL extended n="<<n<<" mask="<<mask<<"\n";return 1;}
  checks++;
 }
 cout<<"VERIFY_OK exact_krylov_cases="<<checks<<"\n";
 return 0;
}
