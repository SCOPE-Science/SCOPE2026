#include <bits/stdc++.h>
using namespace std;
struct H{size_t operator()(const vector<int>&a)const noexcept {size_t h=0xcbf29ce484222325ULL; for(auto v:a)h=(h^uint32_t(v+0x9e3779b9))*0x100000001b3ULL;return h;}};
int main(int argc,char**argv){unordered_map<vector<int>,int,H> intern;int next=1;int maxn=argc>1?atoi(argv[1]):25;
for(int n=5;n<=maxn;n++){
 vector<int> lev;int p=1;for(int i=0;i<4;i++)p*=n;lev.resize(p);
 for(int t=0;t<p;t++) {int a[4],x=t;for(int i=3;i>=0;i--){a[i]=x%n;x/=n;}int s=0,z=1;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){int d=(a[j]-a[i]+n)%n;int state=d==0?0:((d<=2||d>=n-2)?1:2);s+=state*z;z*=3;}vector<int> sig={0,4,s};auto it=intern.find(sig);if(it==intern.end()){lev[t]=next; intern.emplace(move(sig),next++);}else lev[t]=it->second;}
 for(int k=3;k>=0;k--){p/=n;vector<int> nextlev(p);for(int t=0;t<p;t++){vector<int> sig={4-k,k};int a[4],x=t;for(int i=k-1;i>=0;i--){a[i]=x%n;x/=n;}int s=0,z=1;for(int i=0;i<k;i++)for(int j=i+1;j<k;j++){int d=(a[j]-a[i]+n)%n;int state=d==0?0:((d<=2||d>=n-2)?1:2);s+=state*z;z*=3;}sig.push_back(s);for(int v=0;v<n;v++)sig.push_back(lev[t*n+v]);sort(sig.begin()+3,sig.end());sig.erase(unique(sig.begin()+3,sig.end()),sig.end());auto it=intern.find(sig);if(it==intern.end()){nextlev[t]=next;intern.emplace(move(sig),next++);}else nextlev[t]=it->second;}lev.swap(nextlev);}cout<<n<<","<<lev[0]<<"\n";cerr<<"direct n="<<n<<" unique="<<intern.size()<<"\n";}
}
