// Independent permutation-rank union-find checker for excedance-top components.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
struct UF{vector<int> p,r; UF(int n):p(n),r(n,0){iota(p.begin(),p.end(),0);}int root(int x){return p[x]==x?x:p[x]=root(p[x]);}void unite(int a,int b){a=root(a);b=root(b);if(a!=b){if(r[a]<r[b])swap(a,b);p[b]=a;if(r[a]==r[b])r[a]++;}}};
int rankp(const vector<int>&p,const vector<int>&f){int n=p.size(),z=0;for(int i=0;i<n;i++){int smaller=0;for(int j=i+1;j<n;j++) smaller+=p[j]<p[i];z+=smaller*f[n-1-i];}return z;}
int main(){vector<int> f(11,1);for(int i=1;i<11;i++) f[i]=f[i-1]*i;for(int n=2;n<=9;n++){
 UF u(f[n]);vector<int> deg(f[n],0),topmask(f[n],0),ex(f[n],0);vector<int> p(n);iota(p.begin(),p.end(),1);long long twice_edges=0;
 do{int a=rankp(p,f),mask=0,k=0;for(int i=0;i<n;i++)if(p[i]>i+1){mask|=1<<(p[i]-2);k++;}ex[a]=k;topmask[a]=mask;
 for(int i=0;i<n-1;i++){int x=p[i],y=p[i+1]; if(x!=i+2&&y!=i+2){swap(p[i],p[i+1]);int b=rankp(p,f);swap(p[i],p[i+1]);u.unite(a,b);deg[a]++;twice_edges++;}}
 }while(next_permutation(p.begin(),p.end()));
 map<int,int> signature_root;map<int,int> signature_population;vector<int> isolated(n,0);long long counted_edges=0;
 for(int i=0;i<f[n];i++){int mask=topmask[i],rt=u.root(i);if(signature_root.count(mask))assert(signature_root[mask]==rt);else signature_root[mask]=rt;signature_population[mask]++;if(deg[i]==0) isolated[ex[i]]++;counted_edges+=deg[i];}
 assert(twice_edges==counted_edges);assert((int)signature_root.size()==(1<<(n-1)));for(int k=0;k<n;k++) assert(isolated[k]==1);
 for(auto [mask,rt]:signature_root){int k=__builtin_popcount((unsigned)mask);assert(k>=0&&k<n);assert(signature_population[mask]>0);}
 cout<<"INDEPENDENT_PASS "<<n<<" "<<f[n]<<" "<<signature_root.size()<<" "<<twice_edges/2<<"\n";
 }}
