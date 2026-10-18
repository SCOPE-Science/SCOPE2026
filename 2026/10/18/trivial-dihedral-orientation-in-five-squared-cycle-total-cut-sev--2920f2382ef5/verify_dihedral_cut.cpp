// Exhaustive integral Morse and equivariant Lefschetz checks for five squared-cycle total cut complexes.
// Compile: g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify_dihedral_cut.cpp -o verify_dihedral_cut
// Run: ./verify_dihedral_cut
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using U=uint32_t;
static int pop(U x){return __builtin_popcount(x);}
static bool independent(U m,int n){
  U rem=m;
  while(rem){int i=__builtin_ctz(rem);rem&=rem-1;
    for(int s=1;s<=2;s++) if(m&(U(1)<<((i+s)%n)))return false;
  }
  return true;
}
// Generate k-subsets by monotone recursion, checking independence at the leaf.
static void enumerate_ind(int n,int k,int next,int left,U m,vector<U>& out){
  if(!left){if(independent(m,n))out.push_back(m);return;}
  for(int i=next;i<=n-left;i++){
    if(i>0 && ((m&(U(1)<<(i-1))) || (i>1 && (m&(U(1)<<(i-2))))))continue;
    enumerate_ind(n,k,i+1,left-1,m|(U(1)<<i),out);
  }
}
static vector<U> orbits(int n,int a,int b){
  vector<uint8_t> visited(n,0);vector<U> parts;
  for(int v=0;v<n;v++)if(!visited[v]){
    int u=v;U mask=0;
    do{if(visited[u])throw runtime_error("permutation collision");
      visited[u]=1; mask|=(U(1)<<u);u=(a*u+b+4*n)%n;
    }while(u!=v);
    parts.push_back(mask);
  }
  return parts;
}
// Every g-fixed face is the union of a unique subset of its vertex orbits.
// The alternating orbit sum equals the induced homology trace if the
// reduced homology is one-dimensional in odd degree and zero otherwise.
static int orbit_sum(int n,int a,int b,const vector<uint8_t>& face){
  vector<U> o=orbits(n,a,b);if(o.size()>=31)throw runtime_error("orbit overflow");
  const U count=U(1)<<o.size();vector<U> unions(count,0);int result=0;
  for(U i=0;i<count;i++){
    if(i){int j=__builtin_ctz(i);unions[i]=unions[i^(U(1)<<j)]|o[j];}
    if(face[unions[i]])result+=(pop(i)&1)?-1:1;
  }
  return result;
}
static void check(int k){
  int n=3*k+3;
  const U size=U(1)<<n,all=size-1;
  vector<U> inds;enumerate_ind(n,k,0,k,0,inds);
  const uint64_t expected_facets=(uint64_t)n*(k+1)*(k+2)/6;
  if(inds.size()!=expected_facets)throw runtime_error("facet count disagreement");
  vector<uint8_t> live(size,0);
  for(U ind:inds){
    U facet=all^ind;
    for(U x=facet;;x=(x-1)&facet){live[x]=1;if(!x)break;}
  }
  uint64_t faces=0;int64_t augmented_euler=0;
  for(U x=0;x<size;x++)if(live[x]){faces++;augmented_euler+=(pop(x)&1)?-1:1;}
  if(augmented_euler!=1)throw runtime_error("Euler characteristic mismatch");
  // Check every rotation and every reflection, not merely generators.
  unsigned checked=0;
  for(int sign: {1,-1})for(int b=0;b<n;b++){
    int chi=orbit_sum(n,sign,b,live);
    if(chi!=1){cerr<<"k="<<k<<" sign="<<sign<<" b="<<b<<" chi="<<chi<<"\n";
      throw runtime_error("dihedral character not trivial");}
    ++checked;
  }
  // The first element matching pairs faces differing in vertex 0.
  const U first_bit=1;
  uint64_t pairs=0;
  for(U x=0;x<size;x+=2){
    if(live[x]&&live[x|first_bit]){live[x]=live[x|first_bit]=0;++pairs;}
  }
  vector<U> survivors;
  for(U x=0;x<size;x++)if(live[x])survivors.push_back(x);
  // Later element matchings process only the remaining, explicitly listed faces.
  for(int v=1;v<n;v++){
    U bit=U(1)<<v;
    for(U x:survivors)if(!(x&bit)&&live[x]&&live[x|bit]){
      live[x]=live[x|bit]=0;++pairs;
    }
    size_t j=0;
    for(U x:survivors)if(live[x])survivors[j++]=x;
    survivors.resize(j);
  }
  const U critical_mask=21846;
  if(survivors.size()!=1||survivors[0]!=critical_mask||pop(critical_mask)!=8 ||
     2*pairs+1!=faces)throw runtime_error("Morse matching mismatch");
  cout<<"k="<<k<<" n="<<n<<" independent_sets="<<inds.size()
      <<" faces_including_empty="<<faces<<" matched_pairs="<<pairs
      <<" critical_face_mask="<<critical_mask<<" dimension=7"
      <<" dihedral_elements_checked="<<checked
      <<" all_traces=1\n"<<flush;
}
int main(){try{for(int k=4;k<=8;k++)check(k);cout<<"ALL_CHECKS_PASSED\n";}
 catch(const exception& e){cerr<<"CHECK_FAILED: "<<e.what()<<"\n";return 1;}}
