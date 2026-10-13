// Exact enumeration of ordinary identifying codes in the 24-vertex McGee graph.
// Compile with: c++ -std=c++17 -O3 verify.cpp -o verify_mcgee
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using U=uint32_t;
static constexpr int N=24;
int main(){
 array<U,N> neigh{};
 auto edge=[&](int a,int b){neigh[a]|=U(1)<<b;neigh[b]|=U(1)<<a;};
 for(int i=0;i<N;i++)edge(i,(i+1)%N);
 constexpr int jump[3]={12,7,-7};
 for(int i=0;i<N;i++)edge(i,(i+jump[i%3]+N)%N);
 array<U,N> closed{};
 for(int i=0;i<N;i++){
  if(__builtin_popcount(neigh[i])!=3) return 2;
  closed[i]=neigh[i]|(U(1)<<i);
 }
 vector<U> tests;
 for(int i=0;i<N;i++)tests.push_back(closed[i]);
 for(int i=0;i<N;i++)for(int j=0;j<i;j++)tests.push_back(closed[i]^closed[j]);
 if(tests.size()!=300) return 3;
 auto direct=[&](U c){
  U seen[N];
  for(int i=0;i<N;i++){
   U x=c&closed[i];
   if(!x)return false;
   for(int j=0;j<i;j++)if(seen[j]==x)return false;
   seen[i]=x;
  }
  return true;
 };
 auto dual=[&](U c){
  for(U t:tests)if((t&c)==0)return false;
  return true;
 };
 long counts[2][2]={{0,0},{0,0}};
 vector<U> codesA,codesB;
 // Analytic inequality 5*|C|>=48 excludes all sizes below ten.
 for(U c=0;c<(U(1)<<N);c++){
  int k=__builtin_popcount(c);if(k!=10 && k!=11)continue;
  bool a=direct(c),b=dual(c);
  if(a!=b){cerr<<"CHECKER_DISAGREEMENT:"<<c<<'\n';return 4;}
  if(a){counts[k-10][0]++;if(k==11)codesA.push_back(c);}
  if(b){counts[k-10][1]++;if(k==11)codesB.push_back(c);}
 }
 if(counts[0][0]!=0 || counts[0][1]!=0 || counts[1][0]!=384 || counts[1][1]!=384||codesA!=codesB) return 5;
 cout<<"CENSUS_OK N=24 tests=300 k10=0 k11=384 methods=signatures+separators\n";
 for(U c:codesA)cout<<"CODE "<<c<<'\n';
}
