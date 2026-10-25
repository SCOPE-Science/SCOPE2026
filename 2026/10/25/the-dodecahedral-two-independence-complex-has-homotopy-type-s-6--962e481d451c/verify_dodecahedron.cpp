// Independent exhaustive certificate for the ordinary two-independence complex of GP(10,2).
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_dodecahedron.cpp -o verifier
// Run: ./verifier
#include <bits/stdc++.h>
using namespace std;
static constexpr int N=20, LIM=1<<N;
int main(){
 array<uint32_t,N> adj{};
 auto edge=[&](int a,int b){if(a==b || a<0 || a>=N || b<0 || b>=N)abort();adj[a]|=1u<<b;adj[b]|=1u<<a;};
 for(int i=0;i<10;i++){edge(i,(i+1)%10);edge(i,10+i);edge(10+i,10+(i+2)%10);}
 int nedges=0;for(auto m:adj){if(__builtin_popcount(m)!=3)abort();nedges+=__builtin_popcount(m);}if(nedges!=60)abort();
 array<vector<uint32_t>,N> tri;
 set<uint32_t> triples;
 for(int v=0;v<N;v++)for(int a=0;a<N;a++)if(adj[v]>>a&1)
  for(int b=a+1;b<N;b++)if(adj[v]>>b&1)
   triples.insert((1u<<v)|(1u<<a)|(1u<<b));
 for(auto mask:triples)for(int v=0;v<N;v++)if(mask>>v&1)tri[v].push_back(mask^(1u<<v));
 if(triples.size()!=60)abort();
 vector<uint8_t> face(LIM);face[0]=1;
 vector<uint32_t> all;all.reserve(65000);all.push_back(0);
 array<uint64_t,N+1> f{};f[0]=1;
 // Inductive exhaustive recognition by all connected three-vertex subsets.
 for(uint32_t s=1;s<LIM;s++){
  int v=__builtin_ctz(s);uint32_t parent=s^(1u<<v);
  if(!face[parent])continue;
  bool ok=true;for(uint32_t t:tri[v])if((parent&t)==t){ok=false;break;}
  if(ok){face[s]=1;all.push_back(s);f[__builtin_popcount(s)]++;}
 }
 // A second recognition method based directly on the definition: every component of G[s] has size at most two.
 for(uint32_t s=0;s<LIM;s++){
  bool ok=true;
  uint32_t remaining=s;
  while(remaining){
   uint32_t start=remaining&-remaining;
   uint32_t seen=start, frontier=start;
   while(frontier){
    int v=__builtin_ctz(frontier);frontier&=frontier-1;
    uint32_t next=adj[v]&s&~seen;
    seen|=next;frontier|=next;
   }
   if(__builtin_popcount(seen)>2){ok=false;break;}
   remaining &= ~seen;
  }
  if(ok!=bool(face[s])){cerr<<"Face classifier mismatch "<<s<<"\n";return 2;}
 }
 array<uint64_t,N> facets{};
 for(uint32_t s:all)if(s){
  bool maximal=true;
  for(int v=0;v<N;v++)if(!(s>>v&1) && face[s|(1u<<v)]){maximal=false;break;}
  if(maximal)facets[__builtin_popcount(s)-1]++;
 }
 if(facets[7]!=25 || facets[8]!=60 || facets[9]!=420 || facets[11]!=5)abort();
 for(int d=0;d<N;d++)if(d!=7&&d!=8&&d!=9&&d!=11 && facets[d])abort();
 const array<uint64_t,13> expected={1,20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5};
 for(int i=0;i<13;i++)if(f[i]!=expected[i])abort();
 for(int i=13;i<=N;i++)if(f[i]!=0)abort();
 const array<int,N> order={10,17,4,16,14,0,8,6,1,9,5,3,13,7,11,2,12,19,18,15};
 vector<uint8_t> alive=face;
 vector<int32_t> mate(LIM,-1);
 uint64_t pairs=0;
 for(int v:order){uint32_t bit=1u<<v;
  for(auto low:all)if(!(low&bit)&&alive[low]&&alive[low|bit]){
   uint32_t high=low|bit;
   if(mate[low]!=-1 || mate[high]!=-1)abort();
   mate[low]=high;mate[high]=low;
   alive[low]=alive[high]=0;pairs++;
  }
 }
 // Passing from augmented to ordinary Morse theory: leave the empty simplex and a vertex unmatched.
 uint32_t base=mate[0];
 if(base>=LIM || !base || (base&(base-1))!=0){cerr<<"BADBASE "<<base<<"\n";abort();}
 if(base != (1u<<10))abort();
 mate[0]=mate[base]=-1;
 alive[0]=alive[base]=1;
 pairs--;
 map<int,int> critical;
 for(auto s:all){
  if(mate[s]!=-1){
   uint32_t t=mate[s];if(!face[t]||mate[t]!=(int32_t)s)abort();
   if(abs(__builtin_popcount(s)-__builtin_popcount(t))!=1)abort();
  } else critical[__builtin_popcount(s)-1]++;
 }
 if(critical.size()!=3 || critical[-1]!=1 || critical[0]!=1 || critical[6]!=1)abort();
 uint32_t critical_six=0;
 for(auto s:all)if(mate[s]==-1 && __builtin_popcount(s)==7)critical_six=s;
 if(!critical_six)abort();
 // Build complete oriented face-poset cover relations. Matched edges point upwards; all others downwards.
 vector<int> indeg(LIM,0);uint64_t hasse=0;
 for(uint32_t high:all)if(high){
  for(uint32_t bits=high;bits;bits&=bits-1){
   uint32_t low=high^(bits&-bits);if(!face[low])abort();
   if(mate[high]==(int32_t)low)indeg[high]++;
   else indeg[low]++;
   hasse++;
  }
 }
 deque<uint32_t> q;
 for(auto s:all)if(indeg[s]==0)q.push_back(s);
 uint64_t seen=0;
 while(!q.empty()){
  auto s=q.front();q.pop_front();seen++;
  // Matched upward arrows.
  if(mate[s]!=-1 && __builtin_popcount(s)<__builtin_popcount((uint32_t)mate[s])){
   uint32_t t=mate[s];if(--indeg[t]==0)q.push_back(t);
  }
  // All unmatched downward arrows.
  for(uint32_t bits=s;bits;bits&=bits-1){
   uint32_t low=s^(bits&-bits);
   if(mate[s]!=(int32_t)low){if(--indeg[low]==0)q.push_back(low);}
  }
 }
 if(seen != all.size()){
  cerr<<"Matching not acyclic, visited "<<seen<<" of "<<all.size()<<"\n";return 3;
 }
 long long reducedEuler=-1;
 for(int d=1;d<=N;d++)reducedEuler+=(d&1?+1:-1)*(long long)f[d];
 if(reducedEuler!=1)abort();
 cout<<"GRAPH GP(10,2) vertices="<<N<<" edges="<<nedges/2<<" forbidden_triples="<<triples.size()<<"\n";
 cout<<"F_VECTOR_WITH_EMPTY=";for(int i=0;i<13;i++)cout<<(i?",":"")<<f[i];cout<<"\n";
 cout<<"FACETS_DIM7_8_9_11="<<facets[7]<<","<<facets[8]<<","<<facets[9]<<","<<facets[11]<<"\n";
 cout<<"FACES_WITH_EMPTY="<<all.size()<<" MORSE_PAIRS="<<pairs<<" HASSE="<<hasse<<"\n";
 cout<<"CRITICAL_MINUS_ONE="<<critical[-1]<<" CRITICAL_ZERO="<<critical[0]<<" CRITICAL_SIX="<<critical[6]<<"\n";
 cout<<"CRITICAL_SIX_MASK="<<critical_six<<" CRITICAL_SIX_VERTICES=";
 for(int i=0;i<N;i++){if(critical_six>>i&1)cout<<i<<",";}cout<<"\n";
 cout<<"EULER_REDUCED="<<reducedEuler<<" TOPOLOGICAL_SORT="<<seen<<"\n";
 cout<<"VERIFY_OK\n";
}
