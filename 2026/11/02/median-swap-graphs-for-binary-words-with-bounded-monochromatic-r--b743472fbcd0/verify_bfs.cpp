// Exhaustive independently constructed exchange graphs for run-bounded binary words.
// Build: g++ -O2 -std=c++17 verify_bfs.cpp -o verify_bfs && ./verify_bfs
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <array>
using namespace std;
static bool allowed(int x,int n,int r,int s){
 int zr=0, orr=0;
 for(int i=0;i<n;++i){
  if((x>>i)&1){++orr;zr=0;} else {++zr;orr=0;}
  if(zr>=r || orr>=s)return false;
 }
 return true;
}
static int earth(int x,int y,int n){
 vector<int>a,b;
 for(int j=0;j<n;++j){if((x>>j)&1)a.push_back(j);if((y>>j)&1)b.push_back(j);}
 assert(a.size()==b.size());int d=0;
 for(size_t j=0;j<a.size();++j)d+=abs(a[j]-b[j]);
 return d;
}
int main(){
 long long tested=0;int sectors=0;
 for(int n=3;n<=11;++n){
 for(int r=2;r<=5;++r)for(int s=2;s<=5;++s){
  if(r==2 && s==2)continue;
  map<int,vector<int>> byweight;
  for(int x=0;x<(1<<n);++x)if(allowed(x,n,r,s))byweight[__builtin_popcount((unsigned)x)].push_back(x);
  for(auto &entry:byweight){
   auto &v=entry.second;int N=v.size();
   map<int,int> ix;for(int j=0;j<N;++j)ix[v[j]]=j;
   vector<vector<int>> adj(N);
   for(int j=0;j<N;++j){
    for(int pos=0;pos<n-1;++pos){
     int b1=(v[j]>>pos)&1,b2=(v[j]>>(pos+1))&1;
     if(b1!=b2){int to=v[j]^(3<<pos);auto t=ix.find(to);
      if(t!=ix.end())adj[j].push_back(t->second);
     }
    }
   }
   for(int a=0;a<N;++a){
    vector<int> dd(N,-1);dd[a]=0;queue<int> Q;Q.push(a);
    while(!Q.empty()){int z=Q.front();Q.pop();
     for(int w:adj[z])if(dd[w]==-1){dd[w]=dd[z]+1;Q.push(w);}
    }
    for(int b=0;b<N;++b){
     int want=earth(v[a],v[b],n);
     if(dd[b]!=want){
      cerr<<"MISMATCH n="<<n<<" r="<<r<<" s="<<s<<" k="<<entry.first
          <<" x="<<v[a]<<" y="<<v[b]<<" bfs="<<dd[b]<<" want="<<want<<"\n";
      return 1;
     }
     ++tested;
    }
   }
   ++sectors;
  }
 }
 }
 // The exceptional simultaneous no-00/no-11 restriction has disconnected words.
 assert(allowed(5,4,2,2) && allowed(10,4,2,2));
 cout<<"BFS_ALL_PASS sectors="<<sectors<<" ordered_pairs="<<tested<<"\n";
}
