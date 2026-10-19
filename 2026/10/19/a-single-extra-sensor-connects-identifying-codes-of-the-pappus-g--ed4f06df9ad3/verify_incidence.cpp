// Complete census of identifying codes on the 3-by-3 affine net's incidence graph.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify_incidence.cpp -o verify_incidence
// Run:   ./verify_incidence
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
using Mask = uint32_t;
static constexpr int nv=18;

static array<Mask,nv> closed_neighborhoods() {
    array<Mask,nv> nb{};
    for (int v=0;v<nv;v++) nb[v]=Mask(1)<<v;
    // Point (x,y) is vertex 3*x+y; line (m,b) is vertex 9+3*m+b.
    for (int x=0;x<3;x++) for (int y=0;y<3;y++)
      for (int m=0;m<3;m++) for (int b=0;b<3;b++)
        if (y==(m*x+b)%3) {
           int a=3*x+y,c=9+3*m+b;
           nb[a]|=Mask(1)<<c; nb[c]|=Mask(1)<<a;
        }
    return nb;
}
static bool identifying(Mask code,const array<Mask,nv>& nb) {
    array<Mask,nv> signatures{};
    for(int v=0;v<nv;v++) {
       Mask s=code&nb[v]; if (!s) return false;
       signatures[v]=s;
    }
    sort(signatures.begin(),signatures.end());
    return adjacent_find(signatures.begin(),signatures.end())==signatures.end();
}
struct Stat {long long vertices=0, edges=0; vector<int> components; map<int,int> degrees,eccentricities;};
static Stat graph_stats(const vector<Mask>& states, int k, bool get_ecc) {
    Stat out; out.vertices=states.size();
    vector<int> idx(1<<nv,-1);
    for(int i=0;i<(int)states.size();i++)idx[states[i]]=i;
    vector<vector<int>> adj(states.size());
    for(int i=0;i<(int)states.size();i++) {
        Mask s=states[i];
        for(int p=0;p<nv;p++) if(s&(Mask(1)<<p))
          for(int q=0;q<nv;q++) if(!(s&(Mask(1)<<q))) {
             Mask t=s^(Mask(1)<<p)^(Mask(1)<<q);
             int j=idx[t]; if(j>=0 && i<j) {adj[i].push_back(j);adj[j].push_back(i);out.edges++;}
          }
    }
    for(const auto& a:adj)out.degrees[(int)a.size()]++;
    vector<char> seen(states.size(),false);
    for(int seed=0;seed<(int)states.size();seed++)if(!seen[seed]) {
        queue<int> todo;todo.push(seed);seen[seed]=true;
        int count=0;
        while(!todo.empty()) {
           int u=todo.front();todo.pop();count++;
           for(int v:adj[u])if(!seen[v]){seen[v]=true;todo.push(v);}
        }
        out.components.push_back(count);
    }
    sort(out.components.begin(),out.components.end());
    if(get_ecc) {
      for(int seed=0;seed<(int)states.size();seed++) {
        vector<int> dist(states.size(),-1);queue<int> todo;
        dist[seed]=0;todo.push(seed);int far=0;
        while(!todo.empty()) {
          int u=todo.front();todo.pop();
          for(int v:adj[u])if(dist[v]<0) {
            dist[v]=dist[u]+1;far=max(far,dist[v]);todo.push(v);
          }
        }
        out.eccentricities[far]++;
      }
    }
    if(k==9) {
       assert(out.vertices==1028 && out.edges==3780);
       assert((out.components==vector<int>{514,514}));
       assert((out.degrees==map<int,int>({{2,108},{4,216},{5,216},{7,108},{11,270},{15,108},{27,2}})));
       assert((out.eccentricities==map<int,int>({{4,2},{5,54},{6,162},{7,486},{8,324}})));
    }
    return out;
}
int main() {
    const auto nb=closed_neighborhoods();
    for(Mask n:nb) assert(__builtin_popcount(n)==4);
    vector<vector<Mask>> codes(nv+1);
    for(Mask s=0;s<(Mask(1)<<nv);s++) if(identifying(s,nb)) {
       codes[__builtin_popcount(s)].push_back(s);
    }
    long long total=0;
    for(int k=0;k<=nv;k++)total+=codes[k].size();
    assert(total==52638); // independently recomputed from the inclusion--separation test.
    cout<<"graph_vertices="<<nv<<" graph_edges=27 exhaustive_masks="<<(1<<nv)<<"\n";
    cout<<"minimum_size=9\n";
    for(int k=9;k<=nv;k++) {
       auto st=graph_stats(codes[k],k,k==9);
       cout<<"k="<<k<<" codes="<<st.vertices<<" exchange_edges="<<st.edges<<" components=";
       for(size_t j=0;j<st.components.size();j++)cout<<(j?",":"")<<st.components[j];
       cout<<"\n";
       if(k==9) {
         cout<<"degrees=";for(auto [d,n]:st.degrees)cout<<d<<":"<<n<<" ";cout<<"\n";
         cout<<"eccentricities=";for(auto [d,n]:st.eccentricities)cout<<d<<":"<<n<<" ";cout<<"\n";
         map<int,int> bypoints;
         for(Mask s:codes[k])bypoints[__builtin_popcount(s & 511U)]++;
         cout<<"point_counts=";for(auto [d,n]:bypoints)cout<<d<<":"<<n<<" ";cout<<"\n";
       }
    }
    cout<<"identifying_codes_total="<<total<<"\n";
    cout<<"VERIFIED\n";
}
