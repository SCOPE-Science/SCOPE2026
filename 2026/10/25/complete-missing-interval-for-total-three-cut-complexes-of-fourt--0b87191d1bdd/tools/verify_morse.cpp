// Exhaustive simplicial discrete-Morse checker for fourth-power-cycle total three-cut complexes.
// Compile: c++ -O2 -std=c++17 -Wall -Wextra verify_morse.cpp -o verify_morse
// Run: ./verify_morse 16 20
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
static bool independent_pair(int a,int b,int n,int r){
 int d=abs(a-b);d=min(d,n-d);return d>r;
}
static void verify(int n) {
 const int r=4;
 if(n<16 || n>23){cerr<<"unsupported n\n"; exit(2);}
 const uint32_t N=uint32_t(1)<<n, all=N-1;
 vector<uint8_t> good(N,0),face(N,0),mate(N,0),indegree(N,0);
 uint64_t triples=0;
 for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)
   if(independent_pair(a,b,n,r)&&independent_pair(a,c,n,r)&&independent_pair(b,c,n,r)){
     good[(1u<<a)|(1u<<b)|(1u<<c)]=1; ++triples;
   }
 // Boolean upward closure of all independent three-subsets.
 for(int b=0;b<n;++b) {
   uint32_t p=1u<<b;
   for(uint32_t base=0;base<N;base+=2*p)
     for(uint32_t s=base;s<base+p;++s) good[s+p]|=good[s];
 }
 uint64_t nonempty=0;
 for(uint32_t s=0;s<N;++s){
   face[s]=good[all^s];
   if(s && face[s])++nonempty;
 }
 if(!face[0]){cerr<<"empty complex\n";exit(3);}
 // Deterministic staged face matching: at coordinate b pair an unmatched lower
 // face with its upper face when both are eligible and still unmatched.
 for(int b=0;b<n;++b){
   uint32_t p=1u<<b;
   for(uint32_t base=0;base<N;base+=2*p)for(uint32_t s=base;s<base+p;++s){
     uint32_t t=s+p;
     if(face[s]&&face[t]&&mate[s]==0&&mate[t]==0){mate[s]=mate[t]=uint8_t(b+1);}
   }
 }
 // Ordinary (unaugmented) discrete Morse convention: restore the vertex 0.
 if(mate[0]!=1 || mate[1]!=1){cerr<<"unexpected empty pair\n";exit(4);}
 mate[0]=mate[1]=0;
 map<int,uint32_t> critical;
 uint64_t pairs=0;
 for(uint32_t s=1;s<N;++s)if(face[s]){
   if(!mate[s]) ++critical[__builtin_popcount(s)-1];
   else if((s & (1u<<(mate[s]-1)))==0) ++pairs;
 }
 uint64_t covers=0;
 // Directed Hasse graph: unmatched cover edges go from coface to face,
 // matched cover edges go from face to coface.
 for(uint32_t s=0;s<N;++s)if(face[s]) {
   for(int b=0;b<n;++b){
     uint32_t p=1u<<b;
     if(!(s&p)) {
       uint32_t t=s|p;
       if(face[t]){
         ++covers;
         bool pair=(mate[s]==b+1 && mate[t]==b+1);
         if(!pair)++indegree[s];
       }
     } else {
       uint32_t t=s^p;
       if(face[t] && mate[t]==b+1 && mate[s]==b+1) ++indegree[s];
     }
   }
 }
 vector<uint32_t> q;
 q.reserve(size_t(nonempty)+1);
 for(uint32_t s=0;s<N;++s)if(face[s] && indegree[s]==0)q.push_back(s);
 for(size_t head=0;head<q.size();++head){
   uint32_t s=q[head];
   // Unmatched downward incidences.
   uint32_t m=s;
   while(m){
     uint32_t p=m&-m;int b=__builtin_ctz(p);m-=p;
     uint32_t t=s^p;
     if(face[t] && !(mate[t]==b+1 && mate[s]==b+1)){
       if(!indegree[t]){cerr<<"bad indegree downward\n";exit(5);}
       if(--indegree[t]==0)q.push_back(t);
     }
   }
   // Matched upward incidence, if current simplex is the lower partner.
   if(mate[s]) {
     uint32_t p=1u<<(mate[s]-1);
     if(!(s&p)) {
       uint32_t t=s|p;
       if(!face[t] || mate[t]!=mate[s]){cerr<<"bad mate\n";exit(6);}
       if(!indegree[t]){cerr<<"bad indegree upward\n";exit(7);}
       if(--indegree[t]==0)q.push_back(t);
     }
   }
 }
 if(q.size()!=nonempty+1){cerr<<"CYCLIC: "<<q.size()<<" of "<<nonempty+1<<"\n";exit(8);}
 uint32_t crit_total=0;
 for(auto [d,c]:critical)crit_total+=c;
 if(2*pairs+crit_total!=nonempty){cerr<<"count mismatch\n";exit(9);}
 cout<<"n="<<n<<" independent_triples="<<triples<<" nonempty_faces="<<nonempty
     <<" matched_pairs="<<pairs<<" hasse_covers="<<covers
     <<" topo_processed="<<q.size()<<" acyclic=YES critical={";
 bool first=true;
 for(auto[d,c]:critical){if(!first)cout<<",";first=false;cout<<d<<":"<<c;}
 cout<<"}\n";
}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: verify_morse START END\n";return 2;}
 int a=atoi(argv[1]), b=atoi(argv[2]);
 if(a>b) return 2;
 for(int n=a;n<=b;++n)verify(n);
}
