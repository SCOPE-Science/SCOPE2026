#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// A direct, exact census of anonymous approval profiles. Candidate masks and
// the voter-approval masks use ordinary zero-based bit positions.
struct CaseChecker {
  int m,n;
  vector<int> pairs, counts;
  uint64_t profiles=0, nongeodesic=0, disconnected=0, oversized=0;
  CaseChecker(int m_,int n_):m(m_),n(n_),counts(1<<m,0) {
    for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)pairs.push_back((1<<a)|(1<<b));
  }
  bool jr(int w) {
    for(int c=0;c<m;c++) {
      int u=0;
      for(int a=0;a<(1<<m);a++)
        if((a&(1<<c)) && !(a&w))u+=counts[a];
      if(2*u>=n)return false;
    }
    return true;
  }
  void evaluate() {
    ++profiles;
    int p=pairs.size();vector<int> good(p,0);
    for(int i=0;i<p;i++)good[i]=jr(pairs[i]);
    for(int i=0;i<p;i++) if(good[i]) {
      vector<int> d(p,100);d[i]=0;
      vector<int> q={i};
      for(int z=0;z<(int)q.size();z++) {
        int u=q[z];
        for(int v=0;v<p;v++)
          if(good[v] && d[v]==100 && __builtin_popcount((unsigned)(pairs[u]^pairs[v]))==2) {
            d[v]=d[u]+1;q.push_back(v);
          }
      }
      for(int j=i+1;j<p;j++) if(good[j]) {
        int johnson=2-__builtin_popcount((unsigned)(pairs[i]&pairs[j]));
        if(d[j]==100)++disconnected;
        if(d[j]!=100 && d[j]>johnson)++nongeodesic;
        if(d[j]>3 && d[j]!=100)++oversized;
      }
    }
  }
  void enumerate(int mask,int remaining) {
    if(mask==(1<<m)-1) {counts[mask]=remaining;evaluate();counts[mask]=0;return;}
    for(int c=0;c<=remaining;c++) {
      counts[mask]=c;enumerate(mask+1,remaining-c);
    }
    counts[mask]=0;
  }
};

int main() {
  for(int m=2;m<=5;m++) {
    int maxn=(m==5?5:(m==4?8:10));
    for(int n=1;n<=maxn;n++) {
      CaseChecker v(m,n);v.enumerate(0,n);
      cout<<"m="<<m<<" n="<<n<<" anonymous_profiles="<<v.profiles
          <<" disconnected_pairs="<<v.disconnected
          <<" distance_over_three="<<v.oversized
          <<" nongeodesic_pairs="<<v.nongeodesic<<'\n';
      if(v.disconnected || v.oversized) return 1;
      if(m<=4 && v.nongeodesic) return 2;
      if(m==5 && n<=5 && v.nongeodesic) return 3;
    }
  }
  // Six voters, five candidates a,b,c,d,e with e approved by all.
  // Two voters approve e only; four approve e and one member of each pair.
  CaseChecker ex(5,6);
  ex.counts[1<<4]=2;
  ex.counts[(1<<4)|(1<<0)|(1<<2)]=1;
  ex.counts[(1<<4)|(1<<0)|(1<<3)]=1;
  ex.counts[(1<<4)|(1<<1)|(1<<2)]=1;
  ex.counts[(1<<4)|(1<<1)|(1<<3)]=1;
  int ab=(1<<0)|(1<<1), cd=(1<<2)|(1<<3);
  assert(ex.jr(ab) && ex.jr(cd));
  for(int x=0;x<2;x++)for(int y=2;y<4;y++)
    assert(!ex.jr((1<<x)|(1<<y)));
  for(int x=0;x<4;x++)assert(ex.jr((1<<x)|(1<<4)));
  cout<<"six_voter_five_candidate_witness=PASS shortest_path_length=3\n";
  return 0;
}
