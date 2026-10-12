// Exact finite verification of limited domination in rectangular rook graphs.
// Compile: c++ -std=c++17 -O2 verify_rook.cpp -o verify_rook
// Run: ./verify_rook
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <numeric>
#include <iostream>
#include <vector>
using namespace std;

static int choose(int n, int k) {
  int v=1; for(int j=1;j<=k;++j) v=v*(n-j+1)/j; return v;
}

static int predicted(int m, int n, int k) {
  return min(m * max(1,n-k), n * max(1,m-k));
}

int main() {
  int graphs=0, comparisons=0;
  unsigned long long masks_tested=0;
  for (int m=2;m<=5;++m) for (int n=m;n<=9;++n) {
    int N=m*n;
    if (N>20) continue;
    int delta=m+n-2;
    vector<uint64_t> nb(N,0);
    for (int i=0;i<m;++i) for (int j=0;j<n;++j) {
      int a=i*n+j;
      for (int h=0;h<m;++h) for (int l=0;l<n;++l) {
        int b=h*n+l;
        if (a!=b && (i==h || j==l)) nb[a] |= (uint64_t(1)<<b);
      }
    }
    vector<int> best(delta+1,N+1);
    vector<unsigned long long> ways(delta+1,0);
    for (uint64_t D=1;D<(uint64_t(1)<<N);++D) {
      ++masks_tested;
      bool dominates=true;
      for (int v=0;v<N;++v) if (!(D>>v & 1)) {
        if ((nb[v]&D)==0) {dominates=false;break;}
      }
      if (!dominates)continue;
      int k0=0;
      uint64_t rem=((uint64_t(1)<<N)-1)^D;
      for (int v=0;v<N;++v) if (D>>v &1)
        k0=max(k0,__builtin_popcountll(nb[v]&rem));
      int size=__builtin_popcountll(D);
      for (int k=k0;k<=delta;++k) {
        if (size<best[k]) {best[k]=size; ways[k]=1;}
        else if(size==best[k]) ++ways[k];
      }
    }
    for (int k=0;k<=delta;++k) {
      int want=predicted(m,n,k);
      if (best[k]!=want) {
        cerr<<"FAIL m="<<m<<" n="<<n<<" k="<<k
            <<" observed="<<best[k]<<" formula="<<want<<"\n";
        return 1;
      }
      if (k<min(m,n)) {
        unsigned long long wantways = (k==0?1:(m==n?2ULL*choose(m,k):choose(m,k)));
        if(ways[k]!=wantways){
          cerr<<"OPTIMAL-COUNT FAIL m="<<m<<" n="<<n<<" k="<<k
              <<" found="<<ways[k]<<" expected="<<wantways<<"\n";return 2;
        }
      }
      ++comparisons;
    }
    ++graphs;
    cout<<"PASS m="<<m<<" n="<<n<<" k=0.."<<delta
        <<" values=";
    for(int k=0;k<=delta;++k)cout<<(k?",":"")<<best[k];
    cout<<"\n";
  }
  cout<<"SUMMARY graphs="<<graphs<<" cases="<<comparisons
      <<" nonempty_subsets="<<masks_tested<<" failures=0\n";
}
