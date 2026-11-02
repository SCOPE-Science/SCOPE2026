#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int n,m; if(!(cin>>n>>m))return 1;vector<uint32_t>a(n);for(int j=0,u,v;j<m;j++){cin>>u>>v;a[u]|=1u<<v;a[v]|=1u<<u;}uint32_t all=(1u<<n)-1;auto pop=[](uint32_t b){return __builtin_popcount(b);};
auto good=[&](uint32_t s,uint32_t leaks){uint32_t blue=s;while(true){uint32_t extra=0;for(int v=0;v<n;v++)if((blue>>v&1)&&!(leaks>>v&1)){uint32_t avail=a[v]&~blue;if(pop(avail)==1)extra|=avail;} if(!extra)return blue==all; blue|=extra;}};
// Independently from the fort DP, compare all small-subset leak-test outcomes to computed fort DP results.
vector<uint8_t> hasbad(all+1);for(uint32_t W=1;W<=all;W++){int ex=0;for(int v=0;v<n;v++)if(!(W>>v&1)&&pop(a[v]&W)==1)ex++;bool b=ex<=2;bool sub=false;for(uint32_t t=W;t;t&=t-1)if(hasbad[W^(t&-t)]){sub=true;break;}hasbad[W]=b||sub;}
uint64_t checks=0, samples=0;uint64_t positive=0;mt19937_64 rng(987654321);for(uint32_t s=0;s<=all;s++) {bool predicted=!hasbad[all^s];int k=pop(s);bool must=(n<=12)||(n==20&&k==9&&predicted);bool sampled=(n==20&&k>=7&&k<=12&&(rng()%600==0));if(!must&&!sampled)continue;bool empiric=true;for(int v=-1;v<n&&empiric;v++){ if(v==-1){if(!good(s,0))empiric=false;checks++;continue;}if(!good(s,1u<<v))empiric=false;checks++;for(int w=v+1;w<n&&empiric;w++){if(!good(s,(1u<<v)|(1u<<w)))empiric=false;checks++;}}
if(empiric!=predicted){cerr<<"MISMATCH at S="<<s<<" graph n="<<n<<" predicted="<<predicted<<" direct="<<empiric<<"\n";return 2;}if(predicted)positive++;samples++;}
cout<<"DIRECT_CHECK_OK n="<<n<<" sets="<<samples<<" winning_sets="<<positive<<" individual_leak_tests="<<checks<<"\n";
}
