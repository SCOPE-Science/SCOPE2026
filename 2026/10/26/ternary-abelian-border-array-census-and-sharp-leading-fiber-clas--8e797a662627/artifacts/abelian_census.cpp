// Exhaustive ternary abelian-border-array census by restricted-growth representatives.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
constexpr int MAXN=16;
array<vector<uint64_t>,MAXN+1> vals;
int word[MAXN+1];
int pref[MAXN+1][3];
uint64_t code[MAXN+1];
uint64_t ntot=0;
void dfs(int n,int mx){
 if(n>=1) vals[n].push_back(code[n]);
 if(n==MAXN)return;
 for(int c=0;c<=min(2,mx+1);c++){
   word[n]=c;
   for(int s=0;s<3;s++)pref[n+1][s]=pref[n][s]+(s==c);
   int longest=0;
   for(int j=n;j>=1;j--){ // Proper border lengths j < n+1
     bool eq=true;
     for(int s=0;s<3;s++) if(pref[j][s]!=pref[n+1][s]-pref[n+1-j][s]){eq=false;break;}
     if(eq){longest=j;break;}
   }
   code[n+1]=code[n] | (uint64_t(longest)<<(4*n));
   dfs(n+1,max(c,mx));
 }
}
int main(){
 pref[0][0]=pref[0][1]=pref[0][2]=0;
 word[0]=0;pref[1][0]=1;pref[1][1]=0;pref[1][2]=0;code[1]=0;
 dfs(1,0);
 for(int n=1;n<=MAXN;n++){
  vector<uint64_t>& v=vals[n];
  sort(v.begin(),v.end());
  uint64_t distinct=0,maxfib=0,maxcnt=0,singletons=0,sqsum=0;
  map<uint64_t,uint64_t> distribution;
  for(size_t i=0;i<v.size();){
   size_t j=i+1;while(j<v.size() && v[j]==v[i])j++;
   uint64_t f=j-i;
   distinct++; if(f>maxfib){maxfib=f;maxcnt=1;}else if(f==maxfib)maxcnt++;
   if(f==1)singletons++;
   distribution[f]++;
   sqsum+=f*f;
   i=j;
  }
  cout<<n<<" "<<v.size()<<" "<<distinct<<" "<<maxfib<<" "<<maxcnt<<" "<<singletons<<" "<<sqsum<<" histogram=";
  for(auto [f,k]:distribution)cout<<f<<":"<<k<<",";
  cout<<"\n";
 }
}
