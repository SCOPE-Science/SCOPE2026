// Standalone enumeration and pairwise exchange-graph verification for Paley(41).
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
int main() {
    const int p=41;
    bool square[p]={};
    for(int x=1;x<p;x++) square[x*x%p]=true;
    auto adjacent = [&](int i,int j) {return i!=j && square[(j-i+p)%p];};
    vector<uint64_t> cliques;
    long long tested=0;
    for(int a=0;a<37;a++) for(int b=a+1;b<38;b++)
    for(int c=b+1;c<39;c++) for(int d=c+1;d<40;d++)
    for(int e=d+1;e<41;e++) {
       tested++;
       array<int,5> s={a,b,c,d,e};
       bool good=true;
       for(int i=0;i<5;i++) for(int j=i+1;j<5;j++)
           if(!adjacent(s[i],s[j])) good=false;
       if(good) {
          uint64_t mask=0;
          for(int i:s)mask |= (uint64_t(1)<<i);
          cliques.push_back(mask);
       }
    }
    assert(tested==749398 && cliques.size()==205);
    // If a six-clique existed, one of its five-subsets would occur here
    // and have a common outside neighbor.
    for(uint64_t mask:cliques) {
      for(int v=0;v<p;v++) if(!(mask & (uint64_t(1)<<v))) {
        bool yes=true;
        for(int w=0;w<p;w++) if(mask&(uint64_t(1)<<w))
          if(!adjacent(w,v)) yes=false;
        assert(!yes);
      }
    }
    vector<vector<int>> exchange(cliques.size());
    map<int,int> intersections;
    int one=0,two=0;
    for(int i=0;i<(int)cliques.size();i++)
      for(int j=0;j<i;j++) {
        int k=__builtin_popcountll(cliques[i]&cliques[j]);
        intersections[k]++;
        if(k==4)one++;
        if(k==3) {two++;exchange[i].push_back(j);exchange[j].push_back(i);}
      }
    assert(one==0 && two==820);
    for(auto &row:exchange)assert(row.size()==8);
    map<int,int> eccentricities;
    array<int,5> shell={1,8,36,98,62};
    for(int start=0;start<(int)exchange.size();start++) {
      vector<int> distance(exchange.size(),-1);
      distance[start]=0;
      queue<int> q; q.push(start);
      while(!q.empty()) {
        int u=q.front();q.pop();
        for(int v:exchange[u]) if(distance[v]==-1) {
          distance[v]=distance[u]+1;q.push(v);
        }
      }
      array<int,5> profile={};
      for(int z:distance) {
        assert(z>=0 && z<5);
        profile[z]++;
      }
      assert(profile==shell);
      eccentricities[4]++;
    }
    assert(eccentricities.size()==1 && eccentricities[4]==205);
    // For a fixed clique the intersection counts are (5:1,3:8,2:16,1:64,0:116).
    assert(intersections[3]==820 && intersections[4]==0);
    cout << "INDEPENDENT_ENUMERATION_OK tested=" << tested << " max_cliques=" << cliques.size() << " no_six_cliques=1\n";
    cout << "INDEPENDENT_EXCHANGE_OK edges_one=" << one << " edges_two=" << two << " degree=8\n";
    cout << "INDEPENDENT_METRIC_OK shells=1,8,36,98,62 diameter=4\n";
    cout << "INDEPENDENT_CERTIFICATE_OK\n";
}
