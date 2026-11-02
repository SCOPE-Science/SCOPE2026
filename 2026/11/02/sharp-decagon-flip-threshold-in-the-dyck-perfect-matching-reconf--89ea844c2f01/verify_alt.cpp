// Independently construct the Dyck graph by its LCF representation
// [-13,5,-5,13]^8, and enumerate all alternating-cycle switches.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using Matching = vector<int>;
using Cycle = vector<int>;
vector<set<int>> graph(32);
vector<Matching> matchings;
set<Cycle> cycles[3];
map<Matching,int> index_of;

int id_edge(int a, int b) {if(a>b)swap(a,b);return a*32+b;}

void list_matchings(unsigned used, Matching &selected) {
  if(used==0xFFFFFFFFu) {
    Matching temp=selected;sort(temp.begin(),temp.end());
    matchings.push_back(temp);return;
  }
  int u=0;while(used&(1u<<u))++u;
  for(int v:graph[u]) if(!(used&(1u<<v))) {
    selected.push_back(id_edge(u,v));
    list_matchings(used|(1u<<u)|(1u<<v),selected);
    selected.pop_back();
  }
}

void list_cycles(int root, Cycle &path, int max_len) {
  int last=path.back();
  if(path.size()>=6 && path.size()<=10 && path.size()%2==0 && graph[last].count(root)) {
    if(root==*min_element(path.begin(),path.end())) {
      Cycle rev(path.rbegin(),path.rend());
      rotate(rev.begin(),prev(rev.end()),rev.end());
      // rev now starts at root
      cycles[(int(path.size())-6)/2].insert(min(path,rev));
    }
  }
  if((int)path.size()==max_len)return;
  for(int next:graph[last]) if(find(path.begin(),path.end(),next)==path.end()) {
    path.push_back(next);list_cycles(root,path,max_len);path.pop_back();
  }
}

vector<set<int>> build_flip(int ci) {
  vector<set<int>> adj(matchings.size());
  for(const Cycle &cyc:cycles[ci]) {
    const int k=cyc.size();
    set<int> parity[2];
    for(int p=0;p<k;++p)
      parity[p%2].insert(id_edge(cyc[p],cyc[(p+1)%k]));
    for(int i=0;i<(int)matchings.size();++i) {
      set<int> old(matchings[i].begin(),matchings[i].end());
      bool alternating=false;
      for(int h=0;h<2;++h) {
        if(includes(old.begin(),old.end(),parity[h].begin(),parity[h].end()))
          alternating=true;
      }
      if(!alternating)continue;
      set<int> next=old;
      for(int p=0;p<k;++p) {
        int e=id_edge(cyc[p],cyc[(p+1)%k]);
        if(!next.erase(e)) next.insert(e);
      }
      Matching result(next.begin(),next.end());
      auto it=index_of.find(result);
      assert(it!=index_of.end() && it->second!=i);
      adj[i].insert(it->second);
    }
  }
  return adj;
}

map<int,int> components(const vector<set<int>> &adj) {
  vector<char>seen(adj.size());map<int,int>c;
  for(int i=0;i<(int)adj.size();++i)if(!seen[i]) {
    vector<int> q{i};seen[i]=1;
    for(size_t p=0;p<q.size();++p)for(int j:adj[q[p]])if(!seen[j]) {
      seen[j]=1;q.push_back(j);
    }
    ++c[(int)q.size()];
  }
  return c;
}

long long count_edges(const vector<set<int>> &adj) {
  long long deg=0;for(const auto &row:adj)deg+=row.size();assert(deg%2==0);return deg/2;
}

vector<set<int>> unite(const vector<vector<set<int>>> &parts, vector<int> selected) {
  vector<set<int>> result(parts[0].size());
  for(int k:selected)for(size_t i=0;i<result.size();++i)
    result[i].insert(parts[k][i].begin(),parts[k][i].end());
  return result;
}

int main() {
  const int offsets[]={-13,5,-5,13};
  for(int i=0;i<32;++i) {
    int next=(i+1)%32,chord=(i+offsets[i%4]+32)%32;
    graph[i].insert(next);graph[next].insert(i);
    graph[i].insert(chord);graph[chord].insert(i);
  }
  for(const auto &row:graph)assert(row.size()==3);
  int undirected=0;for(const auto &row:graph)undirected+=row.size();assert(undirected==96);
  Matching cur;list_matchings(0u,cur);
  assert(matchings.size()==417);
  for(size_t i=0;i<matchings.size();++i)assert(index_of.emplace(matchings[i],int(i)).second);
  for(int i=0;i<32;++i){Cycle path{i};list_cycles(i,path,10);}
  assert(cycles[0].size()==16);
  vector<vector<set<int>>> parts;
  for(int ci=0;ci<3;++ci)parts.push_back(build_flip(ci));
  assert(count_edges(parts[0])==864);
  assert(count_edges(parts[1])==96);
  assert(count_edges(parts[2])==2736);
  assert(components(parts[0])==(map<int,int>{{1,45},{124,3}}));
  assert(components(parts[1])==(map<int,int>{{1,372},{45,1}}));
  assert(components(parts[2])==(map<int,int>{{1,21},{396,1}}));
  auto cutoff8=unite(parts,{0,1});
  assert(components(cutoff8)==(map<int,int>{{45,1},{124,3}}));
  assert(count_edges(cutoff8)==960);
  auto cutoff10=unite(parts,{0,1,2});
  assert(components(cutoff10)==(map<int,int>{{417,1}}));
  assert(count_edges(cutoff10)==3696);
  assert(components(unite(parts,{1,2}))==(map<int,int>{{417,1}}));
  map<int,int>ecc;
  for(int i=0;i<(int)matchings.size();++i) {
    vector<int>dist(matchings.size(),-1);dist[i]=0;queue<int>q;q.push(i);
    while(!q.empty()) {
      int u=q.front();q.pop();
      for(int j:cutoff10[u])if(dist[j]<0){dist[j]=dist[u]+1;q.push(j);}
    }
    assert(find(dist.begin(),dist.end(),-1)==dist.end());
    ++ecc[*max_element(dist.begin(),dist.end())];
  }
  assert((ecc==(map<int,int>{{4,360},{5,57}})));
  cout<<"INDEPENDENT_GRAPH_OK vertices=32 edges=48 girth6_cycles="<<cycles[0].size()<<"\n";
  cout<<"INDEPENDENT_MATCHINGS_OK count=417\n";
  cout<<"INDEPENDENT_CUTOFF_OK components_le8=4 components_le10=1 radius=4 diameter=5\n";
  cout<<"INDEPENDENT_VERIFY_OK\n";
}
