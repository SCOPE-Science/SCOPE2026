// Exact finite checker for total bondage of the grids P_5 square P_4,
// P_7 square P_4, and P_8 square P_4. ISO C++17, standard library only.
// Compile: g++ -std=c++17 -O3 check_total_bondage.cpp -o check_total_bondage
// Run: ./check_total_bondage
#include <array>
#include <bitset>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

class Grid {
public:
  int n;
  vector<pair<int,int>> edges;
  vector<vector<int>> inc;
  explicit Grid(int rows) : n(rows), inc(4*rows) {
    for (int i=0;i<n;i++) for (int j=0;j<4;j++) {
      const int v=4*i+j;
      if (i+1<n) add(v,v+4);
      if (j+1<4) add(v,v+1);
    }
  }
  void add(int u,int v) {
    const int id=static_cast<int>(edges.size());
    edges.push_back({u,v}); inc[u].push_back(id); inc[v].push_back(id);
  }
  bool admissible(const bitset<64>& removed) const {
    // The total-bondage definition excludes removals creating isolated vertices.
    for(const auto &row:inc){
      bool live=false;
      for(int e:row) if(!removed[e]) live=true;
      if(!live) return false;
    }
    return true;
  }
  int total_domination(const bitset<64>& removed) const {
    // The table local[i][a] records vertices of row i dominated from
    // the selected vertices a in that same row; down[i][a] records
    // vertices of row i dominated from row i-1 with selected mask a.
    int local[8][16]={},down[8][16]={};
    for(int i=0;i<n;i++) for(int a=0;a<16;a++) {
      for(int j=0;j<4;j++) if(a&(1<<j)) {
        int v=4*i+j;
        for(int e:inc[v]) if(!removed[e]) {
          auto [u,w]=edges[e]; const int z=(u==v?w:u);
          if(z/4==i) local[i][a] |= 1<<(z%4);
        }
      }
      if(i) for(int j=0;j<4;j++) if(a&(1<<j)) {
        // Here a selects vertices of the preceding row, not the current row.
        int v=4*(i-1)+j;
        for(int e:inc[v]) if(!removed[e]) {
          auto [u,w]=edges[e];const int z=(u==v?w:u);
          if(z/4==i) down[i][a] |= 1<<(z%4);
        }
      }
    }
    constexpr int infinity=100;
    int d[16][16],nd[16][16];
    for(auto& r:d) for(int&x:r) x=infinity;
    for(int a=0;a<16;a++) d[0][a]=__builtin_popcount((unsigned)a);
    // d[previous][current] minimizes the number of selected vertices
    // through the current row before domination of the current row is checked.
    for(int i=0;i<n;i++) {
      for(auto&r:nd) for(int&x:r) x=infinity;
      for(int prev=0;prev<16;prev++) for(int cur=0;cur<16;cur++) {
        const int cost=d[prev][cur];if(cost==infinity) continue;
        int covered=local[i][cur]|down[i][prev];
        for(int nxt=0;nxt<(i+1==n?1:16);nxt++) {
          // Vertical edges connect identical column indices, so the set of
          // vertices in row i dominated from next row's mask 'nxt' is
          // exactly down[i+1][nxt] (same edge set read in reverse).
          const int from_next=(i+1==n?0:down[i+1][nxt]);
          if((covered|from_next)!=15) continue;
          const int nc=cost+__builtin_popcount((unsigned)nxt);
          int &slot=nd[cur][nxt];if(nc<slot) slot=nc;
        }
      }
      for(int a=0;a<16;a++) for(int b=0;b<16;b++) d[a][b]=nd[a][b];
    }
    int answer=infinity;
    for(int prev=0;prev<16;prev++) if(d[prev][0]<answer)answer=d[prev][0];
    return answer;
  }
  bitset<64> removal(const vector<pair<pair<int,int>,pair<int,int>>>& list)const{
    bitset<64> removed;
    for(const auto& item:list){
      auto [v,w]=item;
      int a=4*v.first+v.second,b=4*w.first+w.second;
      bool found=false;
      for(size_t e=0;e<edges.size();e++) if((edges[e].first==a&&edges[e].second==b)||(edges[e].first==b&&edges[e].second==a)){
        assert(!removed[e]); removed.set(e);found=true;break;
      }
      assert(found);
    }
    return removed;
  }
  void verify()const{
    assert(edges.size()<64 && n<=8);
    bitset<64> f;
    const int baseline=total_domination(f);
    unsigned long long viable[4]={1,0,0,0}, damaging[4]={0,0,0,0};
    const int M=edges.size();
    for(int a=0;a<M;a++) {
      f.set(a);
      if(admissible(f)){viable[1]++; if(total_domination(f)>baseline)damaging[1]++;}
      f.reset(a);
      for(int b=a+1;b<M;b++) {
        f.set(a);f.set(b);
        if(admissible(f)){viable[2]++;if(total_domination(f)>baseline)damaging[2]++;}
        f.reset(a);f.reset(b);
        for(int c=b+1;c<M;c++) {
          f.set(a);f.set(b);f.set(c);
          if(admissible(f)){viable[3]++;if(total_domination(f)>baseline)damaging[3]++;}
          f.reset(a);f.reset(b);f.reset(c);
        }
      }
    }
    cout<<"rows="<<n<<" vertices="<<4*n<<" edges="<<M
        <<" gamma_t="<<baseline<<"\n";
    for(int k=1;k<=3;k++) cout<<" k="<<k<<" admissible="<<viable[k]
                              <<" damaging="<<damaging[k]<<"\n";
    if(n==5){assert(baseline==8);assert(damaging[1]==0&&damaging[2]==0&&damaging[3]==40);}
    if(n==7){assert(baseline==10);assert(damaging[1]==0&&damaging[2]==0&&damaging[3]==727);}
    if(n==8){assert(baseline==12);assert(damaging[1]==0&&damaging[2]==0&&damaging[3]==0);}
    // Explicit upper-bound witnesses: 0-based grid coordinates.
    bitset<64> witness;
    if(n==5) witness=removal({{{0,0},{1,0}},{{0,1},{0,2}},{{2,0},{3,0}}});
    if(n==7) witness=removal({{{5,0},{6,0}},{{5,1},{6,1}},{{6,1},{6,2}}});
    if(n==8) witness=removal({{{4,0},{5,0}},{{6,0},{7,0}},{{6,1},{7,1}},{{7,1},{7,2}}});
    assert(admissible(witness));
    const int after=total_domination(witness);
    assert(after>baseline);
    cout<<" witness_edges="<<witness.count()<<" witness_gamma_t="<<after<<"\n";
    cout<<"total_bondage="<<witness.count()<<"\n";
  }
};
int main(){for(int n:{5,7,8})Grid(n).verify();cout<<"all checks passed\n";}
