// Direct two-round chip-firing enumeration independently of the cut formula.
#include <iostream>
#include <vector>
#include <set>
#include <utility>
using namespace std;
using ll = long long;

vector<vector<int>> neighbors(int n, const set<pair<int,int>>& deleted) {
  vector<vector<int>> adj(2*n);
  for (int i=0;i<n;i++) for(int j=0;j<n;j++) {
    if(deleted.count({i,j})) continue;
    adj[i].push_back(n+j);adj[n+j].push_back(i);
  }
  return adj;
}
vector<int> step(const vector<int>& chips,const vector<vector<int>>& adj) {
  int sz=chips.size();vector<int> next=chips,fire(sz);
  for(int i=0;i<sz;i++)fire[i]=(chips[i]>=int(adj[i].size()));
  for(int i=0;i<sz;i++)if(fire[i]){
    next[i]-=int(adj[i].size());
    for(int j:adj[i])next[j]++;
  }
  return next;
}
ll direct_cycles(const vector<vector<int>>& adj) {
  const int m=adj.size();vector<int> chips(m),mx(m);
  for(int i=0;i<m;i++)mx[i]=2*int(adj[i].size());
  ll count=0;
  while(true){
    auto y=step(chips,adj);
    if(y!=chips && step(y,adj)==chips)count++;
    int k=0;
    for(;k<m;k++){
      chips[k]++;
      if(chips[k]<mx[k])break;
      chips[k]=0;
    }
    if(k==m)break;
  }
  if(count%2)throw 1;
  return count/2;
}
ll cut_cycles(const vector<vector<int>>& adj){
  const int m=adj.size();ll total=0;
  for(int f=0;f<(1<<m);f++){
    ll weight=1;
    for(int u=0;u<m;u++){
      int cross=0;
      for(int v:adj[u])if(((f>>u)^(f>>v))&1)cross++;
      weight*=cross;
    }
    total+=weight;
  }
  return total/2;
}
int main(){
  vector<pair<int,set<pair<int,int>>>> cases={
    {2,{}}, {3,{}}, {3,{{0,0},{1,1},{2,2}}},
    {4,{{0,0},{1,1},{2,2},{3,3}}},
    {4,{{0,0},{0,1},{1,1},{1,2},{2,2},{2,3},{3,3},{3,0}}},
    {4,{{0,0},{0,1}}}, {4,{{0,0},{0,1},{1,1}}}
  };
  // Skip cases where the remaining graph is disconnected: theorem concerns connected graphs.
  for(auto& caseinfo:cases){
    const int n=caseinfo.first;auto adj=neighbors(n,caseinfo.second);
    ll c1=direct_cycles(adj),c2=cut_cycles(adj);
    cout<<"n="<<n<<" deleted_edges="<<caseinfo.second.size()<<" direct="<<c1<<" cut="<<c2<<"\n";
    if(c1!=c2)return 1;
  }
  cout<<"PASS direct chip dynamics against cut census\n";
}
