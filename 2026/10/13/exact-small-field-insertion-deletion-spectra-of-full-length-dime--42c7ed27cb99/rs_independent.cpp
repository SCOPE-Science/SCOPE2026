// Independent finite-field and longest-increasing-subsequence census.
// C++17: g++ -O3 -std=c++17 rs_independent.cpp -o rs_independent
#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <map>
#include <vector>
using namespace std;
struct Arithmetic {
 int q;
 int mul(int a,int b) const {
  if(q==9){ int c[3]={};for(int i=0;i<2;i++)for(int j=0;j<2;j++){
   int t=((i?a/3:a%3)*(j?b/3:b%3))%3;
   if(i+j==2)c[0]=(c[0]+2*t)%3; else c[i+j]=(c[i+j]+t)%3;
  }return c[0]+3*c[1]; }
  if(q==4||q==8){int c=0;int k=q==4?2:3;int poly=q==4?3:3;
   for(int i=0;i<k;i++)for(int j=0;j<k;j++)if((a>>i&1)&&(b>>j&1))c^=1<<(i+j);
   for(int i=2*k-2;i>=k;i--)if(c>>i&1)c^=(1<<i)|(poly<<(i-k));
   return c;}
  return (a*b)%q;
 }
 int add(int x,int y) const {
  if(q==4||q==8)return x^y;
  if(q==9)return ((x%3+y%3)%3)+3*((x/3+y/3)%3);
  return (x+y)%q;
 }
};
int lis(const vector<int>& vals){int tails[20],len=0;
 for(int x:vals){int l=0,r=len;while(l<r){int m=(l+r)/2;if(tails[m]<x)l=m+1;else r=m;}tails[l]=x;if(l==len)len++;}return len;
}
int dp(const vector<int>&a,const vector<int>&b){int n=a.size(),dp[20]={};
 for(int i=0;i<n;i++){int left=0,diag=0;for(int j=0;j<n;j++){int old=dp[j+1];dp[j+1]=a[i]==b[j]?diag+1:max(dp[j+1],left);diag=old;left=dp[j+1];}}return dp[n];
}
int main(int argc,char**argv){int q=argc>1?atoi(argv[1]):11;
 if(q!=2&&q!=3&&q!=4&&q!=5&&q!=7&&q!=8&&q!=9&&q!=11&&q!=13)return 1;
 Arithmetic F{q}; for(int k=1;k<q;k++){bool seen[16]={};for(int x=0;x<q;x++){int y=F.mul(k,x);if(y>=q||seen[y])abort();seen[y]=true;}}
 if(q==13){vector<int>a={0,1,5,6,12,7,11,9,8,3,4,10,2};int pos[16];for(int i=0;i<q;i++)pos[a[i]]=i;map<int,int>hist;int maxl=0;
  for(int u=1;u<q;u++)for(int v=0;v<q;v++)if(u!=1||v!=0){vector<int>perm,b;for(int x:a){int y=F.add(F.mul(u,x),v);perm.push_back(pos[y]);b.push_back(y);}int len=lis(perm);if(len!=dp(a,b))abort();hist[len]++;maxl=max(maxl,len);}
  cout<<"q13 witness maxLCS="<<maxl<<", affine LCS histogram:";for(auto [l,n]:hist)cout<<" "<<l<<":"<<n;cout<<"\n";
  if(maxl!=6||hist!=map<int,int>{{3,6},{4,37},{5,73},{6,39}})return 2;
  cout<<"VERIFY_OK\n";return 0;
 }
 vector<int>rest(q-2),a(q),p(q),look(q);iota(rest.begin(),rest.end(),2);map<int,long long>freq;long long norders=0;
 do{a[0]=0;a[1]=1;for(int j=2;j<q;j++)a[j]=rest[j-2];
  for(int j=0;j<q;j++)p[a[j]]=j;
  int largest=0;
  for(int u=1;u<q;u++)for(int v=0;v<q;v++)if(u!=1||v!=0){
   for(int j=0;j<q;j++)look[j]=p[F.add(F.mul(u,a[j]),v)];
   largest=max(largest,lis(look));
  }
  freq[largest]++;norders++;
 }while(next_permutation(rest.begin(),rest.end()));
 cout<<"q="<<q<<" normalized="<<norders;for(auto [l,n]:freq)cout<<" LCS"<<l<<"="<<n;cout<<"\n";
 long long total=0;for(auto [l,n]:freq)total+=n;
 if(total!=norders)return 3;
 cout<<"VERIFY_OK\n";
}
