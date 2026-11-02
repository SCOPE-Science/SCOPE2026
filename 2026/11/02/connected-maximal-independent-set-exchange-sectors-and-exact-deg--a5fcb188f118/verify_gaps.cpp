#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
long long C(int n,int k){if(k<0||k>n)return 0;k=min(k,n-k);long long r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
map<int,long long> expected(int n,int k){
 int a=3*k-n,b=n-2*k;map<int,long long> d;
 if(a<0||b<0)return d;
 if(!a||!b){d[0]=n/k;return d;}
 for(int r=1;r<=min(a,b);r++)d[2*r]=n*C(a-1,r-1)*C(b-1,r-1)/r;
 return d;
}
void check(int n,int k){
 // Enumerate circular 2/3 gap words, start at every possible cycle vertex.
 // A set is encoded by a 32-bit occupancy mask and counted only once.
 int a=3*k-n,b=n-2*k;
 set<uint32_t> states;
 vector<int> gaps(k);
 auto gen = [&](auto &&self,int i,int aa,int bb)->void {
  if(i==k){
   if(aa||bb)return;
   for(int anchor=0;anchor<n;anchor++){
    uint32_t mask=0;int pos=anchor;
    for(int t=0;t<k;t++){
     mask |= 1u<<pos;
     pos=(pos+gaps[t])%n;
    }
    assert(pos==anchor);
    assert(__builtin_popcount(mask)==k);
    states.insert(mask);
   }
   return;
  }
  if(aa){gaps[i]=2;self(self,i+1,aa-1,bb);}
  if(bb){gaps[i]=3;self(self,i+1,aa,bb-1);}
 };
 gen(gen,0,a,b);
 vector<uint32_t> v(states.begin(),states.end());
 unordered_map<uint32_t,int> ids;
 for(int i=0;i<(int)v.size();i++)ids[v[i]]=i;
 map<int,long long> hist;vector<vector<int>> graph(v.size());
 for(int t=0;t<(int)v.size();t++){
  uint32_t s=v[t];
  for(int i=0;i<n;i++)if(s&(1u<<i)){
   // The two possible one-step cycle slides.
   for(int dx: {-1,1}){
    int j=(i+dx+n)%n;
    if(s&(1u<<j))continue;
    uint32_t q=s^(1u<<i)^(1u<<j);
    auto it=ids.find(q);
    if(it!=ids.end())graph[t].push_back(it->second);
   }
  }
  sort(graph[t].begin(),graph[t].end());
  graph[t].erase(unique(graph[t].begin(),graph[t].end()),graph[t].end());
  hist[graph[t].size()]++;
 }
 assert(hist==expected(n,k));
 assert((long long)v.size()==n*C(k,a)/k);
 vector<char> seen(v.size(),0);vector<int> components;
 for(int u=0;u<(int)v.size();u++)if(!seen[u]){
  queue<int>q;q.push(u);seen[u]=1;int sz=0;
  while(!q.empty()){
   int x=q.front();q.pop();sz++;
   for(int y:graph[x])if(!seen[y]){seen[y]=1;q.push(y);}
  }
  components.push_back(sz);
 }
 if(a==0||b==0){assert((int)components.size()==n/k);
  for(int z:components) assert(z==1);
 } else {assert(components.size()==1);}
 long long edges=0;for(auto [d,m]:hist) edges+=d*m;
 assert(edges%2==0);edges/=2;
 assert(edges==(a&&b?n*C(k-2,a-1):0));
}
int main(){
 for(int n=4;n<=22;n++){
  for(int k=(n+2)/3;k<=n/2;k++)check(n,k);
  cout<<"n="<<n<<" GAP_GENERATION_PASS\n";
 }
 cout<<"INDEPENDENT_GAP_ENUMERATION_PASS\n";
}
