// Direct labelled-vertex verification of 4-color successor-contact automata on K_m join edgeless n.
// The graph has every edge inside the clique and every clique-to-independent edge;
// no edges join two independent vertices. No quotient transitions used here.
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <cassert>
#include <cstdint>
using namespace std;
using State=vector<unsigned char>;
State update(const State& a,int m,int n){
 State b=a;int N=m+n;
 for(int v=0;v<N;++v){
  int wanted=(int(a[v])+1)%4;bool found=false;
  for(int u=0;u<N;++u){
   if(u==v)continue;
   if(u>=m && v>=m)continue;
   if(int(a[u])==wanted){found=true;break;}
  }
  if(found)b[v]=static_cast<unsigned char>(wanted);
 }
 return b;
}
pair<int,int> classify(const State& a,int m,int n){
 vector<State> hist;State x=a;
 for(int t=0;t<16;++t){
  for(int s=0;s<t;++s)if(hist[s]==x)return {s,t-s};
  hist.push_back(x);x=update(x,m,n);
 }
 assert(false);return {-1,-1};
}
long long S(int k,int m){
 long long z=0;
 int binom[5][5]={{1},{1,1},{1,2,1},{1,3,3,1},{1,4,6,4,1}};
 for(int j=0;j<=k;++j){long long p=1;for(int v=0;v<m;++v)p*=j;
 z+= ((k-j)%2?-1:1)*binom[k][j]*p;
 }return z;
}
long long pow4(int r){long long t=1;for(int i=0;i<r;++i)t*=4;return t;}
long long pow3(int r){long long t=1;for(int i=0;i<r;++i)t*=3;return t;}
long long pow2(int r){long long t=1;for(int i=0;i<r;++i)t*=2;return t;}
int main(){
 long long total=0;
 for(int m=1;m<=5;++m)for(int n=1;n<=4;++n){
  if(m+n>9)continue;
  long long count=pow4(m+n), b4=0, fixed=0, t3=0;
  for(long long id=0;id<count;++id){
   State a(m+n);long long x=id;
   for(auto &s:a){s=x%4;x/=4;}
   int cmask=0,imask=0;
   for(int k=0;k<m;++k)cmask|=1<<a[k];
   for(int k=m;k<m+n;++k)imask|=1<<a[k];
   int support_size=__builtin_popcount((unsigned)cmask);
   bool p4 = support_size==4 || (support_size==3 && (imask&(~cmask&15))) ||
             (support_size==2 && (cmask==5||cmask==10) && (imask&(~cmask&15))==(~cmask&15));
   auto [t,p]=classify(a,m,n);
   assert(t<=3 && (p==1||p==4));
   assert((p==4)==p4);
   if(p==4)++b4;
   if(t==0 && p==1)++fixed;
   if(t==3)++t3;
  }
  long long E4=S(4,m)*pow4(n)+4*S(3,m)*(pow4(n)-pow3(n))+
                2*S(2,m)*(pow4(n)-2*pow3(n)+pow2(n));
  long long E3=4*(pow4(n)-2*pow3(n)+pow2(n))+
               4*S(2,m)*(pow4(n)-pow3(n)-pow2(n)+1);
  assert(b4==E4 && t3==E3 && fixed==pow2(m+n+1));
  total+=count;
  cout << "m=" << m << " n=" << n << " states=" << count << " period4_basin=" << b4 <<
          " stationary=" << fixed << " third_entry=" << t3 << " OK\n";
 }
 cout << "PASS: " << total << " labelled configurations checked directly.\n";
}
