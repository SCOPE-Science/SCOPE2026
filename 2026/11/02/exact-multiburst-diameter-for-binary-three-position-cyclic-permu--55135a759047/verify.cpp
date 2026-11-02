// Independent all-pairs breadth-first enumeration of the binary length-three cyclic-shift graph.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main() {
  long long pairs_tested = 0;
  for (int n = 3; n <= 15; ++n) {
    for (int k = 1; k <= n/2; ++k) {
      vector<int> words;
      for (int x=0; x<(1<<n); ++x)
        if (__builtin_popcount((unsigned)x)==k) words.push_back(x);
      int N=(int)words.size();
      vector<int> index(1<<n,-1);
      for (int i=0;i<N;++i) index[words[i]]=i;
      vector<vector<int>> adj(N);
      for (int i=0;i<N;++i) {
        int x=words[i];
        for (int start=0;start<n-2;++start) {
          int bits=(x>>start)&7;
          int left=(bits>>1)|((bits&1)<<2);
          int right=((bits<<1)&7)|(bits>>2);
          for (int b : {left,right}) {
            int y=(x&~(7<<start))|(b<<start);
            if (y!=x) {
              assert(index[y]>=0);
              adj[i].push_back(index[y]);
            }
          }
        }
        sort(adj[i].begin(),adj[i].end());
        adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
        // Check equivalence with token swaps over edges of the squared path.
        vector<int> other;
        for (int j=0;j<n;++j)for(int h=1;h<=2&&j+h<n;++h) {
          if (((x>>j)^(x>>(j+h)))&1)
             other.push_back(index[x^(1<<j)^(1<<(j+h))]);
        }
        sort(other.begin(),other.end());
        if (adj[i]!=other) {cerr<<"NEIGHBOR_FAIL "<<n<<" "<<k<<"\n";return 1;}
      }
      int diameter=0;
      vector<int> distance(N,-1);
      for (int root=0;root<N;++root) {
        fill(distance.begin(),distance.end(),-1);
        queue<int> q; q.push(root); distance[root]=0;
        while(!q.empty()) {
          int v=q.front();q.pop();
          for(int w:adj[v]) if(distance[w]<0){distance[w]=distance[v]+1;q.push(w);}
        }
        if(find(distance.begin(),distance.end(),-1)!=distance.end()) {
          cerr<<"DISCONNECTED "<<n<<" "<<k<<"\n";return 1;
        }
        for(int d:distance)diameter=max(diameter,d);
      }
      pairs_tested+=(long long)N*N;
      int expected=(k*(n-k)+1)/2;
      if(diameter!=expected){
        cerr<<"DIAMETER_FAIL n="<<n<<" k="<<k<<" got="<<diameter<<" expected="<<expected<<"\n";
        return 1;
      }
      cout<<"n="<<n<<",k="<<k<<",diam="<<diameter<<"\n";
    }
  }
  cout<<"VERIFY_OK pairs="<<pairs_tested<<"; n=3..15; k=1..floor(n/2)"<<endl;
}
