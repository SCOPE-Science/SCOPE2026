#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// A nonzero bit at position j of the mask denotes a distinct output word.
// The auxiliary implementation deliberately uses strings instead of bit slicing.
bitset<256> ball_by_strings(int x,int n) {
  string source;
  for(int j=n-1;j>=0;--j) source.push_back((x&(1<<j))?'1':'0');
  bitset<256> out;
  for(int d=0;d<n;d++){
    string w=source; w.erase(d,1);
    int y=0;for(char c:w)y=(y<<1)+(c-'0');
    out.set(y);
    for(int j=0;j<n-1;j++){
      w[j]=(w[j]=='0'?'1':'0');
      int z=0;for(char c:w)z=(z<<1)+(c-'0');
      out.set(z);
      w[j]=(w[j]=='0'?'1':'0');
    }
  }
  return out;
}

static const int MAXN=256;
using BS=bitset<MAXN>;
array<BS,MAXN> adj;
long long nodes=0;
int UB, target, nV;
int iter_first(BS const& a) {return a._Find_first();} // GNU libstdc++ bitset helper
// Exhaustively rule out cliques of size UB+1 by valid greedy-color bounds.
// For each vertex v, recurse on currently unprocessed neighbors of v.
// In a graph properly colored by colors <= c, no clique has > c vertices.
void no_larger(BS P,int depth) {
 nodes++;
 if(depth+(int)P.count()<=UB)return;
 vector<int> sorted, colors;
 BS temp=P;
 int color=0;
 while(temp.any()) {
  color++;
  BS avail=temp;
  while(avail.any()) {
   int v=iter_first(avail);
   sorted.push_back(v); colors.push_back(color);
   temp.reset(v);
   avail.reset(v); avail &= ~adj[v];
  }
 }
 for(int i=(int)sorted.size()-1;i>=0;i--) {
   // Remaining candidates are in color classes at most colors[i].
   if(depth+colors[i]<=UB) return;
   int v=sorted[i];
   if(depth+1>UB) {cerr<<"BAD: clique > upper bound\n";exit(2);}
   BS Q=P & adj[v];
   if(Q.any())no_larger(Q,depth+1);
   P.reset(v);
 }
}
// One deletion, followed by at most one substitution.
bitset<256> ball(int x,int n){
 bitset<256> B;
 for(int del=0;del<n;del++){
  int low=x & ((1<<(n-1-del))-1);
  int high=x>>(n-del);
  int y=(high<<(n-1-del))|low;
  B.set(y);
  for(int j=0;j<n-1;j++)B.set(y^(1<<j));
 }
 return B;
}
int main(){
 const vector<vector<int>> witnesses={
 {},{},{},{},{},
 {0,1,3,4,6,7,12,14,15,16,17,19,24,25,27,28,30,31},
 {0,1,3,6,7,8,12,14,15,24,28,30,31,32,33,35,39,48,49,51,56,57,59,60,62,63},
 {0,1,3,6,7,12,15,25,30,31,48,51,60,63,64,67,79,96,97,102,112,120,121,124,126,127},
 {0,1,7,12,31,37,48,60,72,102,113,125,130,142,153,183,195,207,218,224,243,248,254,255}
 };
 for(int n=5;n<=8;n++){
   nV=1<<n; auto start=chrono::steady_clock::now();
   vector<bitset<256>> B(nV);
   for(int x=0;x<nV;x++){
     B[x]=ball(x,n);
     if(B[x]!=ball_by_strings(x,n)){cerr<<"BAD: output-ball mismatch";return 4;}
   }
   for(int i=0;i<nV;i++)adj[i].reset();
   long long forbidden=0;
   for(int i=0;i<nV;i++)for(int j=0;j<i;j++){
     if((B[i]&B[j]).count()<9){adj[i].set(j);adj[j].set(i);}
     else forbidden++;
   }
   UB=(int)witnesses[n].size();
   for(int i=0;i<UB;i++)for(int j=0;j<i;j++){
    if(!adj[witnesses[n][i]].test(witnesses[n][j])){cerr<<"BAD witness";return 3;}
   }
   nodes=0; BS V;for(int i=0;i<nV;i++)V.set(i);
   no_larger(V,0);
   cout<<"n="<<n<<" optimum="<<UB<<" conflicts="<<forbidden<<" BBnodes="<<nodes<<" ball_crosschecks="<<nV<<"\n"<<flush;
 }
}
