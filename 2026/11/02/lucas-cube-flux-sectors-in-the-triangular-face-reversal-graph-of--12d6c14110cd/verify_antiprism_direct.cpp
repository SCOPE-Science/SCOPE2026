// Independent exact enumeration of balanced edge orientations of antiprism graphs.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
struct Enumeration {
  int n, nv, ne;
  vector<pair<int,int>> edges;
  vector<array<int,3>> faces;
  vector<int> remaining, outgoing;
  vector<uint64_t> orient;
  uint64_t nodes=0;
  Enumeration(int m):n(m),nv(2*m),ne(4*m),remaining(2*m,4),outgoing(2*m,0){
    for(int i=0;i<n;i++){
      int j=(i+1)%n;
      edges.push_back({i,j});
      edges.push_back({n+i,n+j});
      edges.push_back({n+i,j});
      edges.push_back({i,n+i});
    }
    for(int i=0;i<n;i++){
      int j=(i+1)%n;
      faces.push_back({4*i,4*i+2,4*i+3});
      faces.push_back({4*i+1,4*i+2,4*j+3});
    }
  }
  void recurse(int idx,uint64_t mask){
    nodes++;
    if(idx==ne){
      for(int d:outgoing)assert(d==2);
      orient.push_back(mask);return;
    }
    auto [a,b]=edges[idx];
    remaining[a]--;remaining[b]--;
    for(int val=0;val<=1;val++){
      outgoing[val?a:b]++;
      bool ok=true;
      for(int v:{a,b})if(outgoing[v]>2||outgoing[v]+remaining[v]<2)ok=false;
      if(ok)recurse(idx+1,mask | (uint64_t(val)<<idx));
      outgoing[val?a:b]--;
    }
    remaining[a]++;remaining[b]++;
  }
};
int fib(int k){int a=0,b=1;while(k--){int t=a+b;a=b;b=t;}return a;}
int lucas(int k){int a=2,b=1;while(k--){int t=a+b;a=b;b=t;}return a;}
int main(){
 for(int n=3;n<=8;n++){
  Enumeration E(n); E.recurse(0,0);
  unordered_map<uint64_t,int> which;
  for(int i=0;i<(int)E.orient.size();i++)which[E.orient[i]]=i;
  assert(which.size()==E.orient.size());
  assert((int)E.orient.size()==2+2*lucas(2*n));
  vector<int> sectors(4,0),deg(E.orient.size(),0);
  vector<vector<int>> adj(E.orient.size());
  array<unordered_map<uint64_t,int>,4> coded;
  vector<int> desired_deg;
  for(uint64_t mask=0;mask<(1ULL<<(2*n));mask++){
    if((mask & (mask<<1)) || ((mask&1) && (mask&(1ULL<<(2*n-1)))))continue;
    int d=0;
    for(int i=0;i<2*n;i++){
      uint64_t flip=mask^(1ULL<<i);
      if(!(flip&(flip<<1)) && !((flip&1)&&(flip&(1ULL<<(2*n-1)))))d++;
    }
    desired_deg.push_back(d);
  }
  assert((int)desired_deg.size()==lucas(2*n));
  for(int idx=0;idx<(int)E.orient.size();idx++){
    uint64_t mask=E.orient[idx];
    int flux=-1;
    uint64_t code=0;
    for(int i=0;i<n;i++){
      int t=(mask>>(4*i))&1, b=(mask>>(4*i+1))&1, d=(mask>>(4*i+2))&1;
      if(flux<0)flux=t+b+d;
      assert(flux==t+b+d);
      if(flux==1 || flux==2){
        if(flux==2){t=1-t;b=1-b;d=1-d;}
        if(t)code|=1ULL<<(2*i);
        if(b)code|=1ULL<<(2*i+1);
      }
    }
    assert(0<=flux&&flux<=3);
    sectors[flux]++;
    if(flux==1||flux==2){
      assert(!(code&(code<<1)));
      assert(!((code&1)&&(code&(1ULL<<(2*n-1)))));
      assert(coded[flux].emplace(code,idx).second);
    }
    for(auto [a,b,c]:E.faces){
      uint64_t next=mask^(1ULL<<a)^(1ULL<<b)^(1ULL<<c);
      auto it=which.find(next);
      if(it!=which.end()){
        adj[idx].push_back(it->second);
      }
    }
    deg[idx]=adj[idx].size();
    if(flux==0||flux==3)assert(deg[idx]==0);
  }
  assert(sectors[0]==1&&sectors[3]==1);
  assert(sectors[1]==lucas(2*n)&&sectors[2]==lucas(2*n));
  for(int sector:{1,2}){
    vector<int> observed;
    for(auto [code,idx]:coded[sector]){
      observed.push_back(deg[idx]);
      for(int next:adj[idx]){
        uint64_t w=E.orient[next];
        (void)w;
        bool found=false;
        for(int pos=0;pos<2*n;pos++){
          auto it=coded[sector].find(code^(1ULL<<pos));
          if(it!=coded[sector].end()&&it->second==next){found=true;break;}
        }
        assert(found);
      }
    }
    sort(observed.begin(),observed.end());
    auto desired=desired_deg;
    sort(desired.begin(),desired.end());
    assert(observed==desired);
  }
  long long edgecnt=0;
  for(auto &v:adj)edgecnt+=v.size();
  assert(edgecnt%2==0);
  edgecnt/=2;
  assert(edgecnt==4LL*n*fib(2*n-1));
  vector<int> component(E.orient.size(),-1);
  vector<int> sizes;
  for(int i=0;i<(int)component.size();i++)if(component[i]<0){
    int cid=sizes.size(),count=0;
    queue<int> q;q.push(i);component[i]=cid;
    while(!q.empty()){
      int a=q.front();q.pop();count++;
      for(int b:adj[a])if(component[b]<0){component[b]=cid;q.push(b);}
    }
    sizes.push_back(count);
  }
  sort(sizes.begin(),sizes.end());
  assert(sizes==vector<int>({1,1,lucas(2*n),lucas(2*n)}));
  cout<<"DIRECT_PASS n="<<n<<" orientations="<<E.orient.size()<<" edges="<<edgecnt<<" components=4 nodes_explored="<<E.nodes<<"\n";
 }
 cout<<"DIRECT_VERIFIER_PASS\n";
}
