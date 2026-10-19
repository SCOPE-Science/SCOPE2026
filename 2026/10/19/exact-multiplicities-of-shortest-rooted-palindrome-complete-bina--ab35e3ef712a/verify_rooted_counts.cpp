// Exact breadth-first enumeration of shortest rooted palindrome-complete binary cycles.
// c++ -O2 -std=c++17 verify_rooted_counts.cpp -o verify_rooted_counts
// ./verify_rooted_counts
#include<bits/stdc++.h>
using namespace std;
static string dec(__uint128_t x){if(x==0)return "0";string t;while(x){t.push_back(char('0'+x%10));x/=10;}reverse(t.begin(),t.end());return t;}
static bool pal(int x,int k){int y=x,r=0;for(int i=0;i<k;i++){r=(r<<1)|(y&1);y>>=1;}return x==r;}
int main(){for(int k=2;k<=8;k++){
 int V=1<<(k-1),M=1<<((k+1)/2),N=V*(1<<M),full=(1<<M)-1;
 vector<int> palI(1<<k,-1);int ix=0;for(int x=0;x<(1<<k);x++)if(pal(x,k))palI[x]=ix++;
 vector<int16_t> d(N,-1);vector<__uint128_t> cnt(N,0);vector<int> queue(N);
 int start=V;d[start]=1;cnt[start]=1;int front=0,back=0;queue[back++]=start;int goal=-1;
 while(front<back){int s=queue[front++];int mask=s/V,v=s%V;if(mask==full&&v==0){goal=s;break;}
 for(int b=0;b<2;b++){int edge=(v<<1)|b, nm=mask, nv=edge&(V-1);if(palI[edge]>=0)nm|=1<<palI[edge];int ns=nm*V+nv;
  if(d[ns]==-1){d[ns]=d[s]+1;cnt[ns]=cnt[s];queue[back++]=ns;}
  else if(d[ns]==d[s]+1){__uint128_t old=cnt[ns];cnt[ns]+=cnt[s];if(cnt[ns]<old)throw runtime_error("128-bit count overflow");}
 }
 }
 const int expectedL[]={0,0,4,8,12,22,32,60,74};
 const unsigned long long expectedC[]={0,0,1,2,2,8,40,6272,768};
 if(d[goal]!=expectedL[k] || cnt[goal]!=expectedC[k])throw runtime_error("certificate mismatch");
 cout<<"k="<<k<<" depth="<<d[goal]<<" marked_optimal_cycles="<<dec(cnt[goal])<<" visited="<<back<<"\n";
} cout<<"VERIFY_OK rooted_palindrome_complete_counts_k=2..8\n"; }
