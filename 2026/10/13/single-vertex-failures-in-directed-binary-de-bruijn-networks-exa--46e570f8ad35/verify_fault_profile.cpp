#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <utility>
using namespace std;

int main() {
  const vector<map<int,int>> expected = {
    {{-1,2},{2,2}},
    {{-1,4},{3,2},{4,2}},
    {{-1,4},{4,2},{5,2},{6,8}},
    {{-1,4},{5,2},{6,10},{7,12},{8,4}},
    {{-1,4},{6,2},{7,16},{8,42}},
    {{-1,4},{7,2},{8,50},{9,64},{10,8}},
    {{-1,4},{8,2},{9,104},{10,142},{11,4}},
    {{-1,4},{9,2},{10,234},{11,264},{12,8}},
    {{-1,4},{10,2},{11,496},{12,518},{13,4}}
  };
  for (int k=2; k<=10; ++k) {
    int N=1<<k, mask=N-1;
    map<int,int> histogram;
    for (int failed=0; failed<N; ++failed) {
      int diameter=0;
      bool disconnected=false;
      for (int source=0; source<N && !disconnected; ++source) {
        if (source==failed) continue;
        vector<int> distance(N,-1);
        queue<int> fifo;
        distance[source]=0; fifo.push(source);
        while(!fifo.empty()) {
          int u=fifo.front(); fifo.pop();
          for(int bit=0; bit!=2; ++bit) {
            int v=((u<<1)&mask)|bit;
            if(v!=failed && distance[v]<0) {
              distance[v]=distance[u]+1;
              diameter=max(diameter,distance[v]);
              fifo.push(v);
            }
          }
        }
        for(int v=0;v<N;++v) if(v!=failed && distance[v]<0) {
          disconnected=true; break;
        }
      }
      ++histogram[disconnected ? -1 : diameter];
    }
    assert(histogram == expected[k-2]);
    cout << "k=" << k << " OK:";
    for(auto [d,c]:histogram) cout << " " << d << ":" << c;
    cout << "\n";
  }
  cout << "PROFILE_VERIFIED\n";
}
