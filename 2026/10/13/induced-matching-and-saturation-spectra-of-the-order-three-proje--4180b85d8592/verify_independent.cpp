// Independent exhaustive implementation: independent sets of the flag-conflict graph.
#include <array>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using namespace std;
using U=uint64_t;
using V=array<int,3>;
int main(){
 vector<V> pts;
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
  if(x==0&&y==0&&z==0)continue;
  V v{x,y,z}; int t= x?x:(y?y:z);
  if(t==2)for(int &a:v)a=(a*2)%3;
  bool dup=false;for(V w:pts)if(v==w)dup=true;
  if(!dup)pts.push_back(v);
 }
 assert(pts.size()==13);
 auto on=[&](int p,int l){int a=0;for(int i=0;i<3;i++)a+=pts[p][i]*pts[l][i];return a%3==0;};
 vector<pair<int,int>> e;
 for(int p=0;p<13;p++)for(int l=0;l<13;l++)if(on(p,l))e.push_back({p,l});
 assert(e.size()==52);
 array<U,52> conflicts{};
 for(int i=0;i<52;i++)for(int j=0;j<52;j++){
  auto [p,l]=e[i]; auto [q,m]=e[j];
  if(p==q||l==m||on(p,m)||on(q,l))conflicts[i]|=(U(1)<<j);
 }
 array<long long,53> poly{},maximal{}; long long total=0,complete5=0;
 const U ALL=(U(1)<<52)-1;
 function<void(U,U,int)> dfs=[&](U avail,U chosen,int n){
  if(avail==0){
   ++poly[n];++total;
   int add=0;
   for(int i=0;i<52;i++)if((chosen&conflicts[i])==0)++add;
   if(add==0)++maximal[n];
   if(n==5){assert(add==1);++complete5;}
   return;
  }
  int v=__builtin_ctzll(avail);
  dfs(avail&~(U(1)<<v),chosen,n);
  dfs(avail&~conflicts[v],chosen|(U(1)<<v),n+1);
 };
 dfs(ALL,0,0);
 const long long expected[7]={1,52,702,3276,5031,1404,234};
 for(int k=0;k<7;k++)assert(poly[k]==expected[k]);
 for(int k=7;k<53;k++)assert(poly[k]==0);
 assert(total==10700 && complete5==1404);
 assert(maximal[4]==1989 && maximal[6]==234);
 for(int k=0;k<53;k++)if(k!=4&&k!=6)assert(maximal[k]==0);
 cout<<"VERIFY_INDEPENDENT_OK vertices=52 independent_sets=10700 polynomial=";
 for(int k=0;k<7;k++)cout<<(k?",":"")<<poly[k];
 cout<<"\nVERIFY_INDEPENDENT_OK maximal_4=1989 maximal_6=234 five_unique_extension=1404\n";
}
