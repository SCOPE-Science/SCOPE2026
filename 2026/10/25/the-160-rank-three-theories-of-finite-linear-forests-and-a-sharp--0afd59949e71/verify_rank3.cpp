#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
using V=vector<U>;
struct VHash {size_t operator()(V const&v) const noexcept { U h=0x9e3779b97f4a7c15ULL; for(U x:v){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}return h;}};
struct G {int n; vector<array<U,2>> adj;};
G build(int code){int c[7],n=0; for(int i=0;i<7;i++){c[i]=code%4; code/=4;n+=(i+1)*c[i];} G g{n,vector<array<U,2>>(n,{0,0})};int off=0; for(int i=0;i<7;i++) for(int j=0;j<c[i];j++){for(int k=0;k<i;k++){int a=off+k,b=a+1;g.adj[a][b/64]|=1ULL<<(b%64);g.adj[b][a/64]|=1ULL<<(a%64);}off+=i+1;}return g;}
V sig(const G&g){const int n=g.n;U full[2]={n>=64?~0ULL: (n==0?0:((1ULL<<n)-1)),n<=64?0:( (1ULL<<(n-64))-1 )}; V root;root.reserve(n);
for(int x=0;x<n;x++){
 U rootsig=0;
 for(int y=0;y<n;y++){
  unsigned ty=0;
  if(x==y){ bool yes=false,no=false;for(int k=0;k<2;k++){U mask=full[k] & ~( ((x/64)==k) ? 1ULL<<(x%64):0ULL );if(g.adj[x][k]&mask)yes=true; if((~g.adj[x][k])&mask)no=true;} ty=32+(yes?1:0)+(no?2:0);}
  else {
   int e=(g.adj[x][y/64]>>(y%64))&1;int pat=0;
   for(int k=0;k<2;k++) {
     U mask=full[k]; if(x/64==k)mask &=~(1ULL<<(x%64));if(y/64==k)mask &=~(1ULL<<(y%64));
     U a=g.adj[x][k],b=g.adj[y][k];
     if(mask& ~a & ~b)pat |=1;
     if(mask& a & ~b)pat |=2;
     if(mask& ~a & b)pat |=4;
     if(mask& a & b)pat |=8;
   }
   ty=e*16+pat;
  }
  rootsig |= 1ULL<<ty;
 }
 root.push_back(rootsig);
}
sort(root.begin(),root.end());root.erase(unique(root.begin(),root.end()),root.end());return root;}
int main(){
 unordered_map<V,pair<int,int>,VHash> lookup;lookup.reserve(17000);
 vector<int> ss(85),classes_by_min(85);
 for(int code=1;code<16384;code++) {auto g=build(code);auto sg=sig(g);ss[g.n]++; auto itr=lookup.find(sg);if(itr==lookup.end())lookup.emplace(move(sg),make_pair(g.n,code));else if(g.n<itr->second.first)itr->second={g.n,code};}
 map<int,int> countByOrder, cntByN;int maxn=0,maxcode=-1;for(auto &it:lookup){int n=it.second.first;countByOrder[n]++;if(n>maxn){maxn=n;maxcode=it.second.second;}}
 cout<<"canonical="<<16383<<" q3_types="<<lookup.size()<<" sharp_smallest_worst="<<maxn<<" code="<<maxcode<<"\n";
 cout<<"min_orders:";for(auto [n,k]:countByOrder)cout<<" "<<n<<":"<<k;cout<<"\n";
 for(auto &it:lookup){if(it.second.first==maxn) {int code=it.second.second;cout<<"worst canonical code="<<code<<" multiplicities=";for(int i=1;i<=7;i++){cout<<code%4<<",";code/=4;}cout<<"\n";break;}}
}
