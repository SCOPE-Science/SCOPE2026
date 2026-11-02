// Exact exhaustive verifier for edge-open-packings of rectangular rook graphs.
// This uses the original pair-of-edges condition rather than the star-decomposition proof.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
struct Edge {int a,b;};
long long fact(int k){ long long z=1; for(int i=2;i<=k;i++)z*=i;return z;}
long long predicted(int m,int n){
 if(m>n)swap(m,n);
 if(m==n){int k=m/2; if(m%2==0)return fact(m)*fact(n)/fact(k);
 return fact(m)*fact(n)/fact(k)+fact(m)*fact(n)/(4*fact(k-1));}
 long long ans=0;
 for(int a=0;2*a<=m;a++){
  int b=m-2*a;
  if(m+b>n)continue;
  ans+=fact(m)*fact(n)/((1LL<<b)*fact(a)*fact(b)*fact(n-m-b));
 }
 return ans;
}
long long predicted_coefficient(int m,int n,int k){
 long long ans=0;
 for(int a=0;a<=k/2;a++)for(int b=0;b<=k-2*a;b++){
  int c=k-2*a-b;
  int r=2*a+b+2*c, t=2*a+2*b+c;
  if(r>m||t>n)continue;
  long long denom=(1LL<<(b+c))*fact(a)*fact(b)*fact(c)*fact(m-r)*fact(n-t);
  ans+=fact(m)*fact(n)/denom;
 }
 return ans;
}
int opt(int m,int n){return min(m,n) - (m==n && m%2==1);}
long long enumerate(int m,int n,int k){
 const int v=m*n;
 auto adjacent=[&](int u,int w){return (u/n==w/n) != (u%n==w%n);};
 vector<Edge> es;
 for(int u=0;u<v;u++)for(int w=u+1;w<v;w++)if(adjacent(u,w))es.push_back({u,w});
 int E=es.size();
 vector<vector<unsigned char>> ok(E,vector<unsigned char>(E,1));
 for(int i=0;i<E;i++)for(int j=i+1;j<E;j++){
  bool fine=true;
  for(int u:{es[i].a,es[i].b})for(int w:{es[j].a,es[j].b}){
   if(u==w||!adjacent(u,w))continue;
   if((u==es[i].a&&w==es[i].b)||(w==es[i].a&&u==es[i].b)||
      (u==es[j].a&&w==es[j].b)||(w==es[j].a&&u==es[j].b))continue;
   fine=false;
  }
  ok[i][j]=ok[j][i]=fine;
 }
 long long count=0;
 vector<int> s;
 auto dfs=[&](auto&& self,int start)->void{
  if((int)s.size()==k){count++;return;}
  if(E-start < k-(int)s.size())return;
  for(int i=start;i<=E-(k-(int)s.size());i++){
   bool possible=true;
   for(int j:s)if(!ok[i][j]){possible=false;break;}
   if(!possible)continue;
   s.push_back(i);self(self,i+1);s.pop_back();
  }
 };
 dfs(dfs,0);
 return count;
}
int main(){
 vector<pair<int,int>> tests={{2,2},{2,3},{2,4},{2,5},{3,3},{3,4},{3,5},{3,6},{4,4},{4,5},{5,5}};
 for(auto [m,n]:tests){
  for(int k=0;k<=opt(m,n);k++){
   auto got=enumerate(m,n,k);
   auto want=predicted_coefficient(m,n,k);
   if(got!=want){cerr<<"Coefficient mismatch: "<<m<<"x"<<n<<" k="<<k<<" got="<<got<<" want="<<want<<"\n";return 1;}
   if(k==opt(m,n)){
    cout<<m<<"x"<<n<<" max="<<k<<" counted="<<got<<" predicted="<<predicted(m,n)<<"\n";
    if(got!=predicted(m,n))return 1;
   }
  }
  if(enumerate(m,n,opt(m,n)+1)!=0)return 1;
 }
 cout<<"VERIFY_OK\n";
}
