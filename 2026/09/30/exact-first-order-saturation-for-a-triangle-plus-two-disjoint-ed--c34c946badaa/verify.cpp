#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

struct Instance {
  int n;
  vector<pair<int,int>> edges;
  int idx[8][8]{};
  vector<uint64_t> fcopies;
  vector<vector<uint64_t>> witnesses;
  Instance(int n_): n(n_) {
    for(int i=0;i<8;i++) for(int j=0;j<8;j++) idx[i][j]=-1;
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) {
      idx[i][j]=idx[j][i]=(int)edges.size();
      edges.push_back({i,j});
    }
    int m=edges.size();
    for(int omit=-1;omit<n;omit++) {
      if(n==7 && omit!=-1) continue;
      if(n==8 && omit==-1) continue;
      vector<int> vs;
      for(int v=0;v<n;v++) if(v!=omit) vs.push_back(v);
      if((int)vs.size()!=7) continue;
      for(int ia=0;ia<7;ia++) for(int ib=ia+1;ib<7;ib++) for(int ic=ib+1;ic<7;ic++) {
        int tri[3]={vs[ia],vs[ib],vs[ic]};
        vector<int> r;
        for(int v:vs) if(v!=tri[0]&&v!=tri[1]&&v!=tri[2]) r.push_back(v);
        int P[3][4]={{0,1,2,3},{0,2,1,3},{0,3,1,2}};
        for(auto &p:P) {
          uint64_t f=0;
          for(int a=0;a<3;a++) for(int b=a+1;b<3;b++) f |= 1ULL<<idx[tri[a]][tri[b]];
          f |= 1ULL<<idx[r[p[0]]][r[p[1]]];
          f |= 1ULL<<idx[r[p[2]]][r[p[3]]];
          fcopies.push_back(f);
        }
      }
    }
    sort(fcopies.begin(),fcopies.end());
    fcopies.erase(unique(fcopies.begin(),fcopies.end()),fcopies.end());
    witnesses.assign(m,{});
    for(uint64_t f:fcopies) for(int e=0;e<m;e++) if((f>>e)&1ULL) witnesses[e].push_back(f^(1ULL<<e));
    for(auto &w:witnesses) { sort(w.begin(),w.end()); w.erase(unique(w.begin(),w.end()),w.end()); }
  }
  bool ffree(uint64_t g) const {
    for(uint64_t f:fcopies) if((g&f)==f) return false;
    return true;
  }
  bool saturated(uint64_t g) const {
    if(!ffree(g)) return false;
    int m=edges.size();
    for(int e=0;e<m;e++) if(!((g>>e)&1ULL)) {
      bool ok=false;
      for(uint64_t w:witnesses[e]) if((g&w)==w) {ok=true;break;}
      if(!ok) return false;
    }
    return true;
  }
  uint64_t mask(initializer_list<pair<int,int>> es) const {
    uint64_t g=0;
    for(auto [a,b]:es) g |= 1ULL<<idx[a][b];
    return g;
  }
};

uint64_t next_comb(uint64_t x) {
  uint64_t u=x&-x, v=u+x;
  if(v==0) return 0;
  return v + (((v^x)/u)>>2);
}

uint64_t count_sat_exact(const Instance &I, int k) {
  int m=I.edges.size();
  if(k<0||k>m) return 0;
  uint64_t limit=1ULL<<m;
  if(k==0) return I.saturated(0)?1:0;
  uint64_t g=(1ULL<<k)-1, c=0;
  while(g<limit) {
    if(I.saturated(g)) ++c;
    uint64_t ng=next_comb(g);
    if(ng<=g || ng>=limit) break;
    g=ng;
  }
  return c;
}

uint64_t permute_mask(const Instance &I, uint64_t g, const vector<int>& p) {
  uint64_t h=0;
  for(int e=0;e<(int)I.edges.size();e++) if((g>>e)&1ULL) {
    auto [a,b]=I.edges[e]; int x=p[a], y=p[b]; if(x>y) swap(x,y);
    h |= 1ULL<<I.idx[x][y];
  }
  return h;
}

pair<uint64_t,uint64_t> aut_and_orbit(const Instance &I, uint64_t g) {
  vector<int> p(I.n); iota(p.begin(),p.end(),0);
  uint64_t aut=0;
  do { if(permute_mask(I,g,p)==g) ++aut; } while(next_permutation(p.begin(),p.end()));
  uint64_t fact=1; for(int i=2;i<=I.n;i++) fact*=i;
  return {aut,fact/aut};
}

vector<int> degree_sequence(const Instance &I, uint64_t g) {
  vector<int>d(I.n,0);
  for(int e=0;e<(int)I.edges.size();e++) if((g>>e)&1ULL){auto[a,b]=I.edges[e];d[a]++;d[b]++;}
  sort(d.begin(),d.end()); return d;
}

string joinv(const vector<int>&v){string s;for(size_t i=0;i<v.size();i++){if(i)s+=",";s+=to_string(v[i]);}return s;}

int main(){
  Instance I7(7), I8(8);
  if(I7.fcopies.size()!=105 || I8.fcopies.size()!=840) { cerr<<"bad F-copy counts\n"; return 2; }

  uint64_t r7=I7.mask({{1,2},{1,3},{2,3},{0,4},{4,1},{0,5},{5,2},{0,6},{6,3}});
  uint64_t a8=I8.mask({{0,1},{0,2},{0,3},{1,2},{1,3},{2,3},{0,4},{1,5},{2,6},{3,7}});
  uint64_t b8=I8.mask({{0,1},{0,2},{0,3},{1,2},{1,3},{0,4},{1,5},{2,6},{6,7},{7,3}});
  if(!I7.saturated(r7)||!I8.saturated(a8)||!I8.saturated(b8)){cerr<<"representative not saturated\n";return 3;}

  for(int k=0;k<9;k++) if(count_sat_exact(I7,k)!=0){cerr<<"n=7 lower bound failed at "<<k<<"\n";return 4;}
  uint64_t c79=count_sat_exact(I7,9);
  if(c79!=840){cerr<<"n=7 count mismatch "<<c79<<"\n";return 5;}
  auto [aut7,orb7]=aut_and_orbit(I7,r7);
  if(orb7!=c79){cerr<<"n=7 orbit mismatch\n";return 6;}

  for(int k=0;k<10;k++) if(count_sat_exact(I8,k)!=0){cerr<<"n=8 lower bound failed at "<<k<<"\n";return 7;}
  uint64_t c810=count_sat_exact(I8,10);
  if(c810!=11760){cerr<<"n=8 count mismatch "<<c810<<"\n";return 8;}
  auto [autA,orbA]=aut_and_orbit(I8,a8);
  auto [autB,orbB]=aut_and_orbit(I8,b8);
  auto dA=degree_sequence(I8,a8), dB=degree_sequence(I8,b8);
  if(dA==dB){cerr<<"n=8 reps not separated\n";return 9;}
  if(orbA+orbB!=c810){cerr<<"n=8 orbit cover mismatch\n";return 10;}

  cout<<"F7_COPIES="<<I7.fcopies.size()<<"\n";
  cout<<"N7_MIN_EDGES=9\nN7_LABELED_EXTREMALS="<<c79<<"\nN7_AUT="<<aut7<<"\nN7_ORBIT="<<orb7<<"\nN7_DEGREES="<<joinv(degree_sequence(I7,r7))<<"\n";
  cout<<"F8_COPIES="<<I8.fcopies.size()<<"\n";
  cout<<"N8_MIN_EDGES=10\nN8_LABELED_EXTREMALS="<<c810<<"\n";
  cout<<"TYPE_A_AUT="<<autA<<"\nTYPE_A_ORBIT="<<orbA<<"\nTYPE_A_DEGREES="<<joinv(dA)<<"\n";
  cout<<"TYPE_B_AUT="<<autB<<"\nTYPE_B_ORBIT="<<orbB<<"\nTYPE_B_DEGREES="<<joinv(dB)<<"\n";
  cout<<"VERIFY_OK\n";
  return 0;
}
