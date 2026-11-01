// Reproducible finite verification of synchronous binary majority on K_n corona K_1.
// Compile: c++ -O2 -std=c++17 verify_corona.cpp -o verify_corona
// Usage: ./verify_corona [max_n] ; default 10 (n=2,...,10)
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
using ll=long long;
static ll binom(int n,int k){ll z=1;for(int i=1;i<=k;i++)z=z*(n-k+i)/i;return z;}
int main(int argc,char**argv){int maxn=argc>1?stoi(argv[1]):10;if(maxn>10){cerr<<"max_n must be <=10\n";return 2;}
 for(int n=2;n<=maxn;n++){
  int bits=2*n,N=1<<bits,mask=(1<<n)-1;
  vector<vector<int>> adj(bits);
  for(int i=0;i<n;i++){
   for(int j=0;j<n;j++)if(i!=j)adj[i].push_back(j);
   adj[i].push_back(n+i);adj[n+i].push_back(i);
  }
  vector<int> to(N),indeg(N,0);
  for(int s=0;s<N;s++){
   int t=0;
   for(int i=0;i<bits;i++){
    int cnt=0;for(int j:adj[i])cnt+=(s>>j)&1;
    int d=adj[i].size();int b=(2*cnt>d) || ((2*cnt==d)&&((s>>i)&1));
    t|=b<<i;
   }
   to[s]=t;indeg[t]++;
  }
  vector<int> depth(N,-1),basin(N,-1);
  queue<int> Q;vector<int> peeled;peeled.reserve(N);
  for(int i=0;i<N;i++)if(indeg[i]==0)Q.push(i);
  while(!Q.empty()){int x=Q.front();Q.pop();peeled.push_back(x);if(--indeg[to[x]]==0)Q.push(to[x]);}
  vector<int> cyc_length;int cycles=0;
  for(int x=0;x<N;x++)if(indeg[x]>0&&basin[x]==-1){
   vector<int> cyc;int y=x;do{cyc.push_back(y);y=to[y];}while(y!=x);
   int id=cycles++;cyc_length.push_back(cyc.size());
   for(int z:cyc){depth[z]=0;basin[z]=id;}
  }
  for(int i=(int)peeled.size()-1;i>=0;i--){int x=peeled[i];depth[x]=depth[to[x]]+1;basin[x]=basin[to[x]];}
  vector<int> bs(cycles,0);map<int,int> duration;
  for(int x=0;x<N;x++){assert(depth[x]>=0);bs[basin[x]]++;duration[depth[x]]++;}
  map<int,ll> orbitcount;map<int,map<int,ll>> bdist;
  for(int i=0;i<cycles;i++){orbitcount[cyc_length[i]]++;bdist[cyc_length[i]][bs[i]]++;}
  ll B=binom(n,n/2),q1,q2,basin_uniform,basin_cycle;int m=n/2;
  if(n%2==0){q1=B+2;q2=B*(B-1)/2;basin_uniform=((ll)N-B*B)/2;basin_cycle=2;
   assert(orbitcount[1]==q1&&orbitcount[2]==q2&&orbitcount.size()==2);
   map<int,ll> qfix; qfix[1]=B; qfix[basin_uniform]+=2;
   assert((bdist[1]==qfix && bdist[2]==map<int,ll>{{2,q2}}));
   map<int,int> predict;
   predict[0]=B*B+2;predict[1]=2*((1<<n)-1);
   predict[2]=2*B+((1<<n)-B-2)*(1<<n);
   predict[3]=B*((1<<n)-B-2);
   for(auto it=predict.begin();it!=predict.end();)if(it->second==0)it=predict.erase(it);else ++it;
   assert(duration==predict);
  }else{q1=2;q2=B*(m+2);basin_cycle=(1<<(m+1));basin_uniform=((ll)N-q2*basin_cycle)/2;
   assert(orbitcount[1]==q1&&orbitcount[2]==q2&&orbitcount.size()==2);
   assert((bdist[1]==map<int,ll>{{(int)basin_uniform,2}}));
   assert((bdist[2]==map<int,ll>{{(int)basin_cycle,q2}}));
   map<int,int> predict;
   predict[0]=2+2*q2;predict[1]=2*((1<<n)-1)+2*q2*((1<<m)-1);
   predict[2]=((1<<n)-2-2*B)*(1<<n)+2*B*(1<<m);
   predict[3]=2*B*((1<<n)-(1<<m)*(m+3));
   for(auto it=predict.begin();it!=predict.end();)if(it->second==0)it=predict.erase(it);else ++it;
   assert(duration==predict);
  }
  int H=duration.rbegin()->first;assert(H==(n>=4?3:2));
  for(int s=0;s<N;s++){
   int y=s;for(int t=0;t<3;t++)y=to[y];assert(to[to[y]]==y);
  }
  cout<<"n="<<n<<" configurations="<<N<<" fixed="<<q1<<" two_orbits="<<q2
      <<" fixed_uniform_basin="<<basin_uniform<<" two_orbit_basin="<<basin_cycle
      <<" max_entrance="<<H<<" depth_histogram=";
  for(auto [d,v]:duration)cout<<d<<":"<<v<<",";
  cout<<" CHECK_OK\n";
 }
}
