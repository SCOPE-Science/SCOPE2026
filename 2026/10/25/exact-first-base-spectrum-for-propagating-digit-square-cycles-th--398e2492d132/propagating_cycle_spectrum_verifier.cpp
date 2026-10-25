// Exact census of the first propagating cycles of the base-b digit-square map.
// Build: c++ -O3 -std=c++17 propagating_cycle_spectrum_verifier.cpp -o verify
// Run: ./verify
#include <iostream>
#include <vector>
#include <array>
#include <cassert>
using namespace std;
constexpr int BOUND = 1230;
constexpr int LMAX = 20;
constexpr array<int, LMAX + 1> EXPECTED = {
   0,2,3,8,7,27,16,15,58,144,63,122,127,163,393,287,311,1120,96,269,1230
};

// Method A: a three-color exploration of every eligible integer state.
array<int, LMAX + 1> scan_dfs() {
 array<int, LMAX + 1> first{};
 for (int b=2; b<=BOUND; ++b) {
   const int N=b*b;
   vector<unsigned char> state(N,0);
   vector<int> enter(N,-1), path;
   for (int start=1; start<N; ++start) {
     if (start % b == 0 || state[start] != 0) continue;
     path.clear();
     int x=start;
     while (x>0 && x<N && x%b!=0 && state[x]==0) {
       state[x]=1; enter[x]=(int)path.size(); path.push_back(x);
       int r=x%b, q=x/b;
       x=r*r+q*q;
     }
     if(x>0 && x<N && x%b!=0 && state[x]==1) {
       int ell=(int)path.size()-enter[x];
       if(ell<=LMAX && first[ell]==0) first[ell]=b;
     }
     for(int p:path) state[p]=2;
   }
 }
 return first;
}

// Method B: independently construct the functional graph and peel indegree-zero vertices.
array<int, LMAX+1> scan_peeling() {
 array<int, LMAX+1> first{};
 for(int b=2; b<=BOUND; ++b) {
   int N=b*b;
   vector<int> next(N,-1), deg(N,0), queue;
   queue.reserve(N);
   for(int n=1; n<N; ++n) if(n%b!=0){
     int q=n/b, r=n%b, z=q*q+r*r;
     if(z>0 && z<N && z%b!=0){next[n]=z; ++deg[z];}
   }
   for(int n=1;n<N;++n) if(n%b!=0 && deg[n]==0) queue.push_back(n);
   for(size_t head=0;head<queue.size();++head){
     int z=next[queue[head]];
     if(z!=-1 && --deg[z]==0) queue.push_back(z);
   }
   for(int n=1;n<N;++n) if(n%b!=0 && deg[n]>0){
     int z=n, ell=0;
     do {assert(z>0 && z<N && z%b!=0 && deg[z]>0); deg[z]=0; z=next[z]; ++ell;} while(z!=n);
     if(ell<=LMAX && first[ell]==0) first[ell]=b;
   }
 }
 return first;
}

int main(){
 auto a=scan_dfs(), c=scan_peeling();
 assert(a==c);
 assert(a==EXPECTED);
 for(int ell=2;ell<=LMAX;++ell) {
   assert(a[ell]>=2 && a[ell]<=BOUND);
   cout<<ell<<" "<<a[ell]<<'\n';
 }
 cout<<"VERIFIED: complete scan of bases 2 through 1230, two independent graph algorithms.\n";
}
