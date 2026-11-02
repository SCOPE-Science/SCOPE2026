// Independent exhaustive check using five-bit parity labels for folded Q_5.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
int main() {
  vector<int> words;
  for (int a = 0; a < 32; ++a) if (__builtin_popcount((unsigned)a)%2 == 0) words.push_back(a);
  assert(words.size()==16);
  array<unsigned,16> nbr{};
  for (int i=0;i<16;i++) for(int j=0;j<16;j++) {
    if(i!=j && __builtin_popcount((unsigned)(words[i]^words[j])) == 4) nbr[i] |= 1u<<j;
  }
  for(int i=0;i<16;i++) assert(__builtin_popcount(nbr[i])==5);
  vector<unsigned> four,five;
  // Uniform full-universe mask sweep, unlike the combinations approach.
  for (unsigned mask=0;mask<65536u;mask++) {
    int k=__builtin_popcount(mask);
    if (k>5) continue;
    bool valid=true;
    for (int v=0;v<16;v++) if(!(mask&(nbr[v]|(1u<<v)))) {valid=false;break;}
    if (!valid)continue;
    assert(k>=4);
    if(k==4)four.push_back(mask);
    if(k==5)five.push_back(mask);
  }
  assert(four.size()==80 && five.size()==1056);
  int ind4=0,cyc4=0;
  for(unsigned mask:four){
    int e=0;
    for(int v=0;v<16;v++) if(mask&(1u<<v))e+=__builtin_popcount(nbr[v]&mask);
    e/=2;
    assert(e==0 || e==4);
    if(e==0)ind4++; else cyc4++;
    for(int i=0;i<16;i++)if(mask&(1u<<i))
      for(int j=0;j<16;j++)if(!(mask&(1u<<j))){
        unsigned nxt=mask^(1u<<i)^(1u<<j);
        assert(!binary_search(four.begin(),four.end(),nxt));
      }
  }
  assert(ind4==40 && cyc4==40);
  map<unsigned,int> index;
  for(int i=0;i<(int)five.size();i++)index[five[i]]=i;
  vector<vector<int>> adj(five.size());
  long edgecount=0;
  map<int,int> degrees;
  for(int idx=0;idx<(int)five.size();idx++){
    unsigned s=five[idx];
    for(int i=0;i<16;i++)if(s&(1u<<i))
      for(int j=0;j<16;j++)if(!(s&(1u<<j))){
        auto f=index.find(s^(1u<<i)^(1u<<j));
        if(f!=index.end())adj[idx].push_back(f->second);
      }
    sort(adj[idx].begin(),adj[idx].end());
    assert(unique(adj[idx].begin(),adj[idx].end())==adj[idx].end());
    degrees[adj[idx].size()]++;
    edgecount+=adj[idx].size();
  }
  assert(edgecount==20640 && degrees.size()==2 && degrees[19]==960 && degrees[25]==96);
  map<vector<int>,int> profiles;
  for(int root=0;root<(int)five.size();root++){
    vector<int> dist(five.size(),-1), counts(6,0);
    queue<int> q;dist[root]=0;q.push(root);
    while(!q.empty()){
      int x=q.front();q.pop();
      for(int y:adj[x])if(dist[y]<0){dist[y]=dist[x]+1;q.push(y);}
    }
    for(int d:dist){assert(d>=0 && d<=5);counts[d]++;}
    assert(counts[0]==1);
    profiles[counts]++;
  }
  assert(profiles.size()==2);
  assert(profiles[vector<int>({1,19,94,316,507,119})]==960);
  assert(profiles[vector<int>({1,25,130,250,570,80})]==96);
  cout << "INDEPENDENT_GRAPH_OK sixteen_even_five_bit_words=16 degree=5\n";
  cout << "INDEPENDENT_MINIMUM_OK gamma=4 minimizers=80 independent=40 cycles=40 isolated=80\n";
  cout << "INDEPENDENT_FIVE_OK vertices=1056 edges=10320 connected=1 radius=5 diameter=5\n";
  cout << "INDEPENDENT_VERIFY_OK\n";
}
