// Exact finite verifier for constant-weight-three binary B2 codebooks on seven coordinates.
// Build: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
// Uses only the C++ standard library. No external solver or data files.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using Mask=uint64_t;
constexpr int N=7;
vector<array<int,3>> triples;
vector<Mask> bad;
array<Mask,N> incident{};
Mask allbits;
uint64_t nodes,solutions,balanced;
int goal;
Mask sample_code=0;
int bits(Mask x){return __builtin_popcountll(x);}

// Brute-force, all 2^15 simple graphs on six labeled vertices.
int extremal_C4_free_six(){
 vector<pair<int,int>> E;
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)E.push_back({i,j});
 int maximum=0;
 for(int mask=0;mask<(1<<15);mask++){
   int count=__builtin_popcount((unsigned)mask);
   if(count<=maximum)continue;
   bool a[6][6]{};
   for(int i=0;i<15;i++)if(mask>>i&1){auto [u,v]=E[i];a[u][v]=a[v][u]=true;}
   bool ok=true;
   for(int u=0;u<6;u++)for(int v=u+1;v<6;v++){
     int common=0;
     for(int x=0;x<6;x++)if(a[u][x]&&a[v][x])++common;
     if(common>=2)ok=false; // A C4 is two distinct common neighbors.
   }
   if(ok)maximum=count;
 }
 return maximum;
}

void build(){
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++){
   int i=(int)triples.size();triples.push_back({a,b,c});
   incident[a]|=Mask(1)<<i;incident[b]|=Mask(1)<<i;incident[c]|=Mask(1)<<i;
 }
 allbits=(Mask(1)<<triples.size())-1;
 // Bucket each unordered pair of DIFFERENT codewords by its integer coordinate sum.
 map<array<int,N>,vector<pair<int,int>>> buckets;
 for(int i=0;i<(int)triples.size();i++)for(int j=i+1;j<(int)triples.size();j++){
   array<int,N> key{};
   for(int p:triples[i])key[p]++;
   for(int p:triples[j])key[p]++;
   buckets[key].push_back({i,j});
 }
 set<Mask> s;
 for(auto &[key,pairs]:buckets)for(int i=0;i<(int)pairs.size();i++)
   for(int j=i+1;j<(int)pairs.size();j++){
     auto [a,b]=pairs[i];auto[c,d]=pairs[j];
     Mask q=(Mask(1)<<a)|(Mask(1)<<b)|(Mask(1)<<c)|(Mask(1)<<d);
     if(bits(q)!=4){cerr<<"Non-disjoint colliding source pairs\n";exit(1);}
     s.insert(q);
   }
 bad.assign(s.begin(),s.end());
}

bool is_balanced_design(Mask code){
 int lambda[7][7]{};
 for(int i=0;i<(int)triples.size();i++)if(code>>i&1){
   auto t=triples[i];
   for(int x=0;x<3;x++)for(int y=x+1;y<3;y++)lambda[t[x]][t[y]]++;
 }
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)if(lambda[a][b]!=2)return false;
 return true;
}

// Invariant: 'in' and 'out' are disjoint; every surviving target code lies
// between 'in' and the complement of 'out'. Apply only logically forced exclusions.
void dfs(Mask in,Mask out){
 ++nodes;
 if(bits(in)>=goal){
   for(Mask q:bad)if((q&in)==q){cerr<<"Invalid terminal code\n";exit(1);}
   for(int x=0;x<N;x++)if(bits(in&incident[x])>7){cerr<<"Invalid link degree\n";exit(1);}
   ++solutions;
   if(is_balanced_design(in))++balanced;
   if(!sample_code)sample_code=in;
   return;
 }
 Mask avail=allbits&~(in|out);
 if(bits(in)+bits(avail)<goal)return;
 bool changed=true;
 while(changed){
   changed=false;
   // A four-cycle in any vertex-link gives two colliding pairs of triples.
   // The exact six-vertex extremum is independently enumerated above: 7 edges.
   for(int x=0;x<N;x++){
     int d=bits(in&incident[x]);
     if(d>7)return;
     if(d==7){
       Mask forced=avail&incident[x];
       if(forced){out|=forced;avail&=~forced;changed=true;}
     }
   }
   // If three codewords of a forbidden quadruple are in, its fourth is out.
   for(Mask q:bad){
     int s=bits(q&in);
     if(s==4)return;
     if(s==3){
       Mask forced=q&avail;
       if(forced){out|=forced;avail&=~forced;changed=true;}
     }
   }
   if(bits(in)+bits(avail)<goal)return;
 }
 int best=-1,bestscore=-1;
 for(int v=0;v<(int)triples.size();v++)if(avail>>v&1){
   int score=0;
   Mask t=Mask(1)<<v;
   for(Mask q:bad)if(q&t){int k=bits(q&in);score+=(k==2?10:(k==1?2:0));}
   for(int x:triples[v])score+=bits(in&incident[x]);
   if(score>bestscore){bestscore=score;best=v;}
 }
 assert(best>=0);
 Mask t=Mask(1)<<best;
 dfs(in|t,out);
 dfs(in,out|t);
}

Mask cyclic_double_fano(){
 Mask ans=0;
 for(int base: {1,2})for(int shift=0;shift<7;shift++){
   array<int,3> v={shift,(shift+base)%7,(shift+3)%7};
   sort(v.begin(),v.end());
   auto it=find(triples.begin(),triples.end(),v);
   assert(it!=triples.end());
   ans|=Mask(1)<<distance(triples.begin(),it);
 }
 return ans;
}

bool b2(Mask code){for(Mask q:bad)if((q&code)==q)return false;return true;}
int main(){
 build();
 if(triples.size()!=35||bad.size()!=630){cerr<<"Unexpected incidence size\n";return 1;}
 int ex=extremal_C4_free_six();
 if(ex!=7){cerr<<"Link bound failed\n";return 1;}
 Mask witness=cyclic_double_fano();
 if(bits(witness)!=14||!b2(witness)||!is_balanced_design(witness)){
   cerr<<"Cyclic design witness invalid\n";return 1;
 }
 goal=15;nodes=solutions=balanced=0;sample_code=0;
 // Every nonempty code can be relabeled so that triple {0,1,2} is present.
 dfs(Mask(1),0);
 uint64_t uppernodes=nodes;
 if(solutions){cerr<<"Found a 15-word B2 code\n";return 1;}
 goal=14;nodes=solutions=balanced=0;sample_code=0;
 dfs(Mask(1),0);
 uint64_t exactnodes=nodes;
 if(solutions!=48||balanced!=solutions){cerr<<"Classification failed\n";return 1;}
 // Count labeled cyclic-double-Fano translates under all 7! relabelings.
 vector<int> perm={0,1,2,3,4,5,6};
 set<Mask> orbit;
 do{
   Mask translated=0;
   for(int i=0;i<(int)triples.size();i++)if(witness>>i&1){
     array<int,3> w=triples[i];for(int &x:w)x=perm[x];sort(w.begin(),w.end());
     auto it=find(triples.begin(),triples.end(),w);
     assert(it!=triples.end());
     translated|=Mask(1)<<distance(triples.begin(),it);
   }
   orbit.insert(translated);
 }while(next_permutation(perm.begin(),perm.end()));
 if(orbit.size()!=120){cerr<<"Orbit size failed\n";return 1;}
 // Invariance and double counting: 48 optima through a specified triple
 // correspond to exactly 48*35/14 = 120 labeled optimum codebooks.
 cout<<"VERIFY_OK triples=35 forbidden_quadruples=630 C4free_six_max=7 "
     <<"size15_nodes="<<uppernodes<<" size15_solutions=0 "
     <<"size14_nodes="<<exactnodes<<" size14_containing_012="<<solutions
     <<" all_48_are_double_Fano=1 labeled_optima="<<48*35/14
     <<" witness_orbit="<<orbit.size()<<" max_size=14\n";
 return 0;
}
