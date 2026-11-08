#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
struct State {bool center; int hole, a,b; uint32_t middles;};
int pop(uint32_t x){return __builtin_popcount(x);}
State decode(uint32_t z,int m){
 State s{};
 s.center=(z&1);s.middles=0;s.hole=-1;s.a=s.b=-1;
 for(int i=0;i<m;i++){
  bool mid=(z>>(i+1))&1,leaf=(z>>(i+1+m))&1;
  if(mid)s.middles|=1u<<i;
  if(!mid&&!leaf){if(s.a<0)s.a=i;else s.b=i;s.hole=i;}
 }
 if(!s.center){assert(s.b==-1);}
 else{assert(s.a>=0&&s.b>=0&&s.middles==0);}
 return s;
}
int du(State x,State y){assert(!x.center&&!y.center);
 if(x.hole==y.hole)return pop(x.middles^y.middles);
 return pop(x.middles)+pop(y.middles)+4-2*(((x.middles>>y.hole)&1)+((y.middles>>x.hole)&1));
}
State endpoint(int hole,int mid){State s{};s.center=false;s.hole=hole;s.middles=1u<<mid;return s;}
int expect(State x,State y){
 if(!x.center&&!y.center)return du(x,y);
 if(x.center&&!y.center)swap(x,y);
 if(!x.center&&y.center)return 1+min(du(x,endpoint(y.a,y.b)),du(x,endpoint(y.b,y.a)));
 if(x.a==y.a&&x.b==y.b)return 0;
 int best=1000000;
 for(auto [h,i]:{pair<int,int>{x.a,x.b},{x.b,x.a}})
  for(auto [g,j]:{pair<int,int>{y.a,y.b},{y.b,y.a}})
   best=min(best,2+du(endpoint(h,i),endpoint(g,j)));
 return best;
}
int main(){
 for(int m=3;m<=9;m++){
  int n=2*m+1,k=m-1;
  vector<uint32_t> adj(n,0);
  for(int i=0;i<m;i++){
   int x=i+1,y=i+1+m;
   adj[0]|=1u<<x;adj[x]|=1;adj[x]|=1u<<y;adj[y]|=1u<<x;
  }
  vector<uint32_t> nodes;
  unordered_map<uint32_t,int> id;
  for(uint32_t z=0;z<(1u<<n);z++){
   if(pop(z)!=k)continue;
   bool ok=true;
   for(int a=0;a<n;a++)if(z&(1u<<a))if(z&adj[a]){ok=false;break;}
   if(ok){id[z]=nodes.size();nodes.push_back(z);}
  }
  vector<vector<int>> edges(nodes.size());
  for(int t=0;t<(int)nodes.size();t++){
   uint32_t z=nodes[t];
   for(int a=0;a<n;a++)if(z&(1u<<a))
    for(int b=0;b<n;b++)if((adj[a]&(1u<<b))&&!(z&(1u<<b))){
     auto it=id.find(z^(1u<<a)^(1u<<b));
     if(it!=id.end())edges[t].push_back(it->second);
    }
  }
  vector<State> ps;
  for(auto z:nodes)ps.push_back(decode(z,m));
  long long ed=0;for(auto v:edges)ed+=v.size();ed/=2;
  assert((int)nodes.size()==m*(1<<(m-1))+m*(m-1)/2);
  assert(ed==m*(m-1)*(1<<(m-2))+m*(m-1));
  int diameter=0;
  for(int u=0;u<(int)nodes.size();u++){
   vector<int>d(nodes.size(),-1);queue<int>q;q.push(u);d[u]=0;
   while(!q.empty()){
    int v=q.front();q.pop();
    for(int w:edges[v])if(d[w]<0){d[w]=d[v]+1;q.push(w);}
   }
   for(int v=0;v<(int)nodes.size();v++){
    if(d[v]!=expect(ps[u],ps[v])){
     cerr<<"FAIL m="<<m<<" u="<<u<<" v="<<v<<" computed="<<d[v]<<" formula="<<expect(ps[u],ps[v])<<'\n';return 1;
    }
    diameter=max(diameter,d[v]);
   }
  }
  assert(diameter==2*m);
  cout<<"PASS m="<<m<<" vertices="<<nodes.size()<<" edges="<<ed<<" diameter="<<diameter<<'\n';
 }
 cout<<"ALL_PASS\n";
}
