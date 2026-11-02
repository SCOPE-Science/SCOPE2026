// Exhaustive direct-time simulation of inertial majority on two 16-vertex graphs.
// Each vertex is (row,col) in Z_4 x Z_4 with index 4*row+col.
// Only C++17 standard headers; no external dependencies.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using namespace std;

struct Graph {
  bool adj[16][16]{};
  explicit Graph(bool rook) {
    for (int u=0;u<16;u++) for (int v=0;v<16;v++) {
      if (u==v) continue;
      int i=u/4,j=u%4,a=v/4,b=v%4;
      if (rook) adj[u][v] = (i==a || j==b);
      else {
        int dx=(a-i+4)%4,dy=(b-j+4)%4;
        adj[u][v] = (dx==1&&dy==0)||(dx==3&&dy==0)||
                    (dx==0&&dy==1)||(dx==0&&dy==3)||
                    (dx==1&&dy==1)||(dx==3&&dy==3);
      }
    }
  }
  int four_cliques() const {
    int z=0;
    for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)
    for(int c=b+1;c<16;c++)for(int d=c+1;d<16;d++)
      if(adj[a][b]&&adj[a][c]&&adj[a][d]&&adj[b][c]&&adj[b][d]&&adj[c][d])z++;
    return z;
  }
  void check() const {
    for (int u=0;u<16;u++) {
      int deg=0;
      for (int v=0;v<16;v++) {
        if(adj[u][v] != adj[v][u]) throw runtime_error("nonsymmetric");
        deg+=adj[u][v];
      }
      if (deg!=6 || adj[u][u])throw runtime_error("wrong degree or loop");
      for (int v=0;v<16;v++) {
        int dot=0;
        for(int w=0;w<16;w++)dot+=adj[u][w] && adj[w][v];
        if (dot != (u==v ? 6 : 2)) throw runtime_error("wrong common-neighbor count");
      }
    }
  }
  int step(int x) const {
    int y=0;
    for (int v=0;v<16;v++) {
      int neighbor_spin_sum = 0;
      for (int w=0;w<16;w++) if (adj[v][w])
        neighbor_spin_sum += ((x>>w)&1) ? 1 : -1;
      bool on = neighbor_spin_sum>0 || (neighbor_spin_sum==0 && ((x>>v)&1));
      if (on) y|=(1<<v);
    }
    return y;
  }
};

static void showhist(const map<int,long long>& m) {
  cout<<"{";
  bool first=true;
  for(auto [k,v]:m){if(!first)cout<<",";first=false;cout<<k<<":"<<v;}
  cout<<"}";
}

int main() {
  for (int which=0;which<2;which++) {
    bool rook=(which==0);
    const char *name=rook?"rook":"shrikhande";
    Graph g(rook);g.check();
    map<int,int> cycle_period;
    map<int,long long> basins;
    map<int,long long> depth_hist;
    map<int,long long> by_period_time[3];
    int maxdepth=-1, witness=-1;
    array<int,9> witness_traj{};
    for(int x=0;x<65536;x++) {
      array<int,9> tr{};tr[0]=x;
      for(int t=1;t<9;t++)tr[t]=g.step(tr[t-1]);
      int entry=-1;
      for(int t=0;t<=6;t++)if(tr[t]==tr[t+2]){entry=t;break;}
      if(entry<0)throw runtime_error("period restriction failed");
      int per = (tr[entry]==tr[entry+1]) ? 1:2;
      int rep=min(tr[entry],tr[entry+1]);
      auto it=cycle_period.find(rep);
      if(it!=cycle_period.end() && it->second!=per)throw runtime_error("orbit inconsistency");
      cycle_period[rep]=per;
      basins[rep]++;
      depth_hist[entry]++;
      by_period_time[per][entry]++;
      if(entry>maxdepth){maxdepth=entry;witness=x;witness_traj=tr;}
    }
    map<int,long long> basin_hist[3];
    int fixed=0, twocycle=0;
    for(auto [rep,per]:cycle_period) {
      if(per==1)fixed++;else if(per==2)twocycle++;else throw runtime_error("bad period");
      basin_hist[per][static_cast<int>(basins[rep])]++;
    }
    if((rook && (fixed!=302||twocycle!=1197||maxdepth!=3||g.four_cliques()!=8)) ||
       (!rook && (fixed!=142||twocycle!=685||maxdepth!=5||g.four_cliques()!=0)))
       throw runtime_error("inconsistent expected census");
    if(basins[0]!=basins[65535])throw runtime_error("spin complement symmetry broken");
    cout<<"GRAPH "<<name<<"\n";
    cout<<"srg=16,6,2,2 k4="<<g.four_cliques()<<" fixed="<<fixed<<" two="<<twocycle
        <<" maxdepth="<<maxdepth<<" consensus="<<basins[0]<<"\n";
    cout<<"depth=";showhist(depth_hist);cout<<"\n";
    cout<<"fixed_by_depth=";showhist(by_period_time[1]);cout<<"\n";
    cout<<"two_by_depth=";showhist(by_period_time[2]);cout<<"\n";
    cout<<"fixed_basin_hist=";showhist(basin_hist[1]);cout<<"\n";
    cout<<"two_basin_hist=";showhist(basin_hist[2]);cout<<"\n";
    cout<<"maxdepth_witness="<<witness<<" path=";
    for (int t=0;t<maxdepth+3;t++)cout<<(t?",":"")<<witness_traj[t];
    cout<<"\n";
  }
}
