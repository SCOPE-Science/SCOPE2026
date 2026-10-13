// Exhaustive independent verifier for proper conflict-free colorings of crown graphs.
// Run: c++ -O3 -std=c++17 verify_crown_bruteforce.cpp -o verify_crown_bruteforce && ./verify_crown_bruteforce
#include <iostream>
#include <map>
using namespace std;

long long count_colorings(int n,int q,map<int,long long>& by_shared) {
 long long profiles=1;
 for(int i=0;i<2*n;i++) profiles*=q;
 long long ans=0;
 for(long long mask=0;mask<profiles;mask++) {
  int c[20]={};long long v=mask;
  for(int i=0;i<2*n;i++){c[i]=v%q;v/=q;}
  bool ok=true;
  for(int i=0;i<n&&ok;i++) for(int j=0;j<n&&ok;j++)
   if(i!=j && c[i]==c[n+j]) ok=false;
  if(!ok) continue;
  for(int side=0;side<2 && ok;side++)for(int i=0;i<n && ok;i++) {
    int hist[10]={};
    for(int j=0;j<n;j++) if(i!=j) hist[c[(1-side)*n+j]]++;
    bool unique=false;for(int h=0;h<q;h++)if(hist[h]==1)unique=true;
    if(!unique) ok=false;
  }
  if(ok){
    ans++;int shared=0;
    for(int color=0;color<q;color++){
      bool a=false,b=false;
      for(int i=0;i<n;i++){
        if(c[i]==color)a=true;
        if(c[n+i]==color)b=true;
      }
      if(a&&b)shared++;
    }
    by_shared[shared]++;
  }
 }
 return ans;
}
int main(){
 // Expected numbers independently obtained by the partial-Bell-polynomial closed formula.
 const int parms[][3]={{3,2,0},{3,3,6},{3,4,96},{3,5,780},
     {4,2,0},{4,3,0},{4,4,384},{4,5,12480},
     {5,2,0},{5,3,0},{5,4,240},{5,5,19320},
     {6,3,0},{6,4,360}};
 long long profiles=0;
 for(const auto &x:parms){
   int n=x[0],q=x[1],wanted=x[2];
   map<int,long long> shared;
   long long got=count_colorings(n,q,shared);
   long long total=1;for(int i=0;i<2*n;i++)total*=q;
   profiles+=total;
   cout<<"n="<<n<<" q="<<q<<" count="<<got<<" shared_breakdown=";
   for(auto p:shared) cout<<p.first<<":"<<p.second<<",";
   cout<<"\n";
   if(got!=wanted){cerr<<"FAILED n="<<n<<" q="<<q<<"\n";return 1;}
 }
 cout<<"ALL_EXHAUSTIVE_CHECKS_PASSED profiles="<<profiles<<" cases="<<sizeof(parms)/sizeof(parms[0])<<"\n";
}
