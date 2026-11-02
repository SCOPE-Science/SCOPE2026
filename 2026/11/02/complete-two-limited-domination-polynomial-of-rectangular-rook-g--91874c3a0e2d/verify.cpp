#include <cstdint>
#include <vector>
#include <iostream>
#include <string>
#include <numeric>
#include <algorithm>
#include <stdexcept>
using namespace std;
using ull = unsigned long long;

ull choose(int n, int r){if(r<0||r>n) return 0;ull x=1;for(int i=1;i<=r;i++)x=x*(n-i+1)/i;return x;}
ull fact(int n){ull x=1;for(int i=2;i<=n;i++)x*=i;return x;}
vector<ull> formula(int m,int n){
 vector<ull> c(m*n+1,0);
 for(int t=0;t<=min(m,n);++t)c[t]+=choose(m,t)*choose(n,t)*fact(t);
 c[2]+=m*choose(n,2)+n*choose(m,2);
 c[3]+=4*choose(m,2)*choose(n,2);
 c[4]+=choose(m,2)*choose(n,2);
 c[n]+=m; c[m]+=n;
 c[n+1]+=ull(m)*(m-1)*n; c[m+1]+=ull(n)*(n-1)*m;
 c[2*n]+=choose(m,2); c[2*m]+=choose(n,2);
 return c;
}
// Direct graph checker, independent of the missing-edge support classification:
// H's set bits are omitted vertices.  Check each vertex's actual rook-neighbor count.
bool direct_check(int m,int n,ull missing){
 ull all=(1ULL<<(m*n))-1, selected=(~missing)&all;
 if(!selected)return false;
 for(int v=0;v<m*n;v++){
   int i=v/n,j=v%n;
   int neighbors_in=0,neighbors_out=0;
   for(int w=0;w<m*n;w++){
     if(v==w)continue;
     if(w/n!=i && w%n!=j)continue;
     if(selected&(1ULL<<w)) ++neighbors_in;
     else ++neighbors_out;
   }
   if(selected&(1ULL<<v)){
     if(neighbors_out>2)return false;
   } else if(neighbors_in==0)return false;
 }
 return true;
}
// The proposed exhaustive bipartite-support classification, checked separately.
bool classified(int m,int n,ull h){
 int rd[10]={},cd[10]={};
 for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(h & (1ULL<<(i*n+j))){++rd[i];++cd[j];}
 int fr=0,fc=0;
 for(int i=0;i<m;i++)fr+=(rd[i]==n);
 for(int j=0;j<n;j++)fc+=(cd[j]==m);
 if(fr&&fc)return false;
 if(fr){
  int extra=0;
  for(int i=0;i<m;i++)if(rd[i] && rd[i]!=n)extra+=rd[i];
  return (fr==1 && extra<=1) || (fr==2 && extra==0);
 }
 if(fc){
  int extra=0;
  for(int j=0;j<n;j++)if(cd[j] && cd[j]!=m)extra+=cd[j];
  return (fc==1 && extra<=1) || (fc==2 && extra==0);
 }
 int maxd=0;for(int i=0;i<m;i++)maxd=max(maxd,rd[i]);for(int j=0;j<n;j++)maxd=max(maxd,cd[j]);
 if(maxd<=1)return true;
 int nr=0,nc=0;
 for(int i=0;i<m;i++)nr+=(rd[i]>0);
 for(int j=0;j<n;j++)nc+=(cd[j]>0);
 return nr<=2 && nc<=2 && maxd<=2;
}
void run(int m,int n){
 if(m<4||n<4||m*n>25)throw runtime_error("invalid test dimensions");
 auto exp=formula(m,n);
 vector<ull> got(m*n+1,0);
 ull total=1ULL<<(m*n),classified_count=0;
 for(ull h=0;h<total;h++){
  bool b=direct_check(m,n,h),c=classified(m,n,h);
  if(b!=c)throw runtime_error("classification mismatch at "+to_string(m)+"x"+to_string(n)+" mask "+to_string(h));
  if(b){got[__builtin_popcountll(h)]++;classified_count++;}
 }
 if(got!=exp)throw runtime_error("polynomial mismatch at "+to_string(m)+"x"+to_string(n));
 ull cnt=accumulate(got.begin(),got.end(),0ULL);
 int k=2;int largest=0;for(int i=0;i<=m*n;i++)if(got[i])largest=i;
 if(largest!=k*max(m,n))throw runtime_error("minimum size mismatch");
 ull extremal=(m<n?choose(m,2):(n<m?choose(n,2):2*choose(m,2)));
 if(got[largest]!=extremal)throw runtime_error("minimum multiplicity mismatch");
 cout<<"DIRECT_ALL_SUBSETS_OK "<<m<<" "<<n<<" "<<total<<" "<<cnt<<" "<<"minimum "<<(m*n-largest)<<" minimizers "<<got[largest]<<"\n";
}
int main(){try{
 run(4,4); run(4,5); run(5,4); run(5,5);
 cout<<"VERIFY_OK\n";
}catch(const exception& e){cerr<<"FAIL "<<e.what()<<"\n";return 1;}}
