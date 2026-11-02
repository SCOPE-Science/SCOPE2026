// Exact full-state functional-graph test for synchronous majority on the Heawood graph.
// C++17: g++ -std=c++17 -O2 -Wall -Wextra check_heawood.cpp -o check_heawood
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
constexpr int V=14, N=1<<V;
int main(){
  const int line[7][3]={{0,1,2},{0,3,4},{0,5,6},{1,3,5},
                        {1,4,6},{2,3,6},{2,4,5}};
  array<array<int,3>,V> nb{}; array<int,V> deg{};
  for(int j=0;j<7;++j)for(int k=0;k<3;++k){
    int i=line[j][k];nb[i][deg[i]++]=j+7;nb[j+7][deg[j+7]++]=i;
  }
  for(int d:deg)assert(d==3);
  vector<int> next(N),indeg(N,0);
  for(int s=0;s<N;++s){
    int t=0;
    for(int i=0;i<V;++i){
      int c=((s>>nb[i][0])&1)+((s>>nb[i][1])&1)+((s>>nb[i][2])&1);
      if(c>=2)t|=1<<i;
    }
    next[s]=t;indeg[t]++;
  }
  set<int> image1,image2;
  for(int s=0;s<N;++s){
    int a=next[s],b=next[a];
    image1.insert(a);image2.insert(b);
    assert(next[next[b]]==b);
  }
  assert(image1.size()==5184 && image2.size()==3364);
  queue<int> q; for(int s=0;s<N;++s)if(!indeg[s])q.push(s);
  vector<int> peeled;
  while(!q.empty()){
    int s=q.front();q.pop();peeled.push_back(s);
    if(--indeg[next[s]]==0)q.push(next[s]);
  }
  vector<int> period(N,0),entry(N,-1),id(N,-1),cycleLen;
  for(int s=0;s<N;++s)if(indeg[s] && id[s]<0){
    int k=cycleLen.size(),t=s,count=0;
    do{assert(id[t]<0);id[t]=k;entry[t]=0;t=next[t];++count;}while(t!=s);
    cycleLen.push_back(count);
  }
  for(int s=0;s<N;++s)if(indeg[s])period[s]=cycleLen[id[s]];
  for(auto it=peeled.rbegin();it!=peeled.rend();++it){
    int s=*it,t=next[s];id[s]=id[t];period[s]=period[t];entry[s]=entry[t]+1;
  }
  map<pair<int,int>,int> shells,basinHist;
  vector<int> basin(cycleLen.size(),0);
  for(int s=0;s<N;++s){
    assert(entry[s]>=0 && entry[s]<=2);
    assert(period[s]==1 || period[s]==2);
    shells[{entry[s],period[s]}]++;
    basin[id[s]]++;
  }
  map<int,int> orbitCounts;
  for(size_t i=0;i<cycleLen.size();++i){
    orbitCounts[cycleLen[i]]++;
    basinHist[{cycleLen[i],basin[i]}]++;
  }
  assert(orbitCounts[1]==58 && orbitCounts[2]==1653);
  const map<pair<int,int>,int> wantedShells={{{0,1},58},{{0,2},3306},
                 {{1,1},126},{{1,2},1694},{{2,1},2464},{{2,2},8736}};
  const map<pair<int,int>,int> wantedBasins={{{1,1},56},{{1,1296},2},
                 {{2,2},1540},{{2,72},112},{{2,2592},1}};
  assert(shells==wantedShells && basinHist==wantedBasins);
  cout<<"Heawood majority, full state count: "<<N<<"\n";
  cout<<"|im F|="<<image1.size()<<" |im F^2|="<<image2.size()<<" F^4=F^2\n";
  cout<<"primitive orbit counts: fixed="<<orbitCounts[1]<<" two="<<orbitCounts[2]<<"\n";
  for(auto [key,v]:shells)cout<<"first entry "<<key.first<<", eventual period "<<key.second<<": "<<v<<"\n";
  for(auto [key,v]:basinHist)cout<<"period "<<key.first<<", basin size "<<key.second<<": "<<v<<" orbits\n";
  cout<<"sharp witness (points 0,1 occupied, lines empty): "<<3<<" -> "<<next[3]<<" -> "<<next[next[3]]<<"\n";
  assert(entry[3]==2);
  cout<<"ALL ASSERTIONS PASSED\n";
}
