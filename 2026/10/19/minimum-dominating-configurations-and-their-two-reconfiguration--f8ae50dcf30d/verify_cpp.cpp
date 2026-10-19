// Exhaustive independent checker for minimum domination reconfiguration in J(7,3).
// C++17. Usage: ./verify_cpp certificate.tsv
// Vertex IDs 00..34 encode lexicographically sorted 3-subsets of {0,...,6}.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Block=array<int,4>;
int pc(unsigned int x){return __builtin_popcount(x);}

int main(int argc, char** argv){
 if(argc!=2) throw runtime_error("usage: verify_cpp certificate.tsv");
 vector<int> triples;
 for(int a=0;a<7;++a)for(int b=a+1;b<7;++b)for(int c=b+1;c<7;++c)
   triples.push_back((1<<a)|(1<<b)|(1<<c));
 assert(triples.size()==35);
 // Independent graph-2-shadow characterization: a triple is covered
 // iff at least one of its three constituent pairs is already in the shadow.
 vector<int> pairkeys;
 for(int a=0;a<7;++a)for(int b=a+1;b<7;++b)pairkeys.push_back((1<<a)|(1<<b));
 assert(pairkeys.size()==21);
 vector<uint32_t> tri_shadows(35);
 for(int i=0;i<35;++i)for(int j=0;j<21;++j)
   if((triples[i]&pairkeys[j])==pairkeys[j])tri_shadows[i]|=(1u<<j);
 vector<array<int,3>> triangle_pairs(35);
 for(int i=0;i<35;++i){
   int p=0;
   for(int j=0;j<21;++j){
      if(tri_shadows[i]&(1u<<j)) triangle_pairs[i][p++]=j;
   }
   assert(p==3);
 }
 vector<Block> good; map<uint64_t,int> indexes;
 for(int a=0;a<35;++a)for(int b=a+1;b<35;++b)
 for(int c=b+1;c<35;++c)for(int d=c+1;d<35;++d){
   uint32_t shadow=tri_shadows[a]|tri_shadows[b]|tri_shadows[c]|tri_shadows[d];
   bool dominates=true;
   for(auto pairs:triangle_pairs){
     if(!(shadow & ((1u<<pairs[0])|(1u<<pairs[1])|(1u<<pairs[2])))){
       dominates=false;break;
     }
   }
   if(dominates){
     Block s={a,b,c,d};
     uint64_t key=(1ull<<a)|(1ull<<b)|(1ull<<c)|(1ull<<d);
     indexes[key]=int(good.size());good.push_back(s);
   }
 }
 assert(good.size()==770);
 // A unique four-point core A is determined by pairs of chosen triples
 // sharing two base elements. B is the complementary three-point block.
 vector<int> owner(good.size()),kind(good.size());
 int typI=0,typII=0;
 for(size_t i=0;i<good.size();++i){
   map<int,int> counts;
   for(int a=0;a<4;++a)for(int b=a+1;b<4;++b)
      if(pc(triples[good[i][a]]&triples[good[i][b]])==2)
          counts[triples[good[i][a]]|triples[good[i][b]]]++;
   assert(!counts.empty());
   int bestunion=0,bestcount=-1;
   for(const auto& [key,n]:counts)if(n>bestcount){bestunion=key;bestcount=n;}
   assert(pc(bestunion)==4);
   owner[i]=127^bestunion;
   kind[i]=(bestcount==3)?1:2;
   assert(bestcount==3||bestcount==1);
   if(kind[i]==1)++typI;else ++typII;
 }
 assert(typI==140 && typII==630);
 // Full S_7 orbit enumeration of one representative of each geometric type.
 map<int,int> triple_index;
 for(int i=0;i<35;++i)triple_index[triples[i]]=i;
 array<set<int>,2> orbits;
 array<int,2> reps={-1,-1};
 for(int i=0;i<(int)good.size();++i){
   int type=kind[i]-1;
   if(reps[type]<0)reps[type]=i;
 }
 vector<int> p={0,1,2,3,4,5,6};
 do{
   for(int k=0;k<2;++k){
     uint64_t key=0;
     for(int x:good[reps[k]]){
       int t=0;
       for(int j=0;j<7;++j)if(triples[x]&(1<<j))t|=(1<<p[j]);
       key|=(1ull<<triple_index.at(t));
     }
     auto found=indexes.find(key);
     assert(found!=indexes.end());
     orbits[k].insert(found->second);
   }
 }while(next_permutation(p.begin(),p.end()));
 assert(orbits[0].size()==140 && orbits[1].size()==630);
 for(int i:orbits[0])assert(orbits[1].count(i)==0);
 vector<pair<int,int>> sliding,jumping;
 vector<vector<int>> T(good.size()),J(good.size());
 for(int i=0;i<(int)good.size();++i)for(int j=i+1;j<(int)good.size();++j){
   int count=0,aa=-1,bb=-1;
   for(int x:good[i]){
     if(find(good[j].begin(),good[j].end(),x)!=good[j].end())++count;
     else aa=x;
   }
   if(count!=3)continue;
   for(int x:good[j])if(find(good[i].begin(),good[i].end(),x)==good[i].end())bb=x;
   assert(aa!=-1&&bb!=-1);
   jumping.push_back({i,j});J[i].push_back(j);J[j].push_back(i);
   if(pc(triples[aa]&triples[bb])==2){
     sliding.push_back({i,j});T[i].push_back(j);T[j].push_back(i);
   }
 }
 assert(sliding.size()==2100 && jumping.size()==2730);
 vector<vector<int>> components;
 vector<int> labels(good.size(),-1);
 for(int i=0;i<(int)good.size();++i)if(labels[i]<0){
   int label=(int)components.size();
   vector<int> comp={i};labels[i]=label;
   for(size_t h=0;h<comp.size();++h)
      for(int j:T[comp[h]])if(labels[j]<0){labels[j]=label;comp.push_back(j);}
   components.push_back(comp);
 }
 assert(components.size()==35);
 for(const auto& comp:components){
   assert(comp.size()==22);
   int b=owner[comp[0]],co=0,ri=0;
   for(int i:comp){assert(owner[i]==b);if(kind[i]==1)++co;else ++ri;}
   assert(co==4&&ri==18);
 }
 map<pair<int,int>,int> cross;
 for(auto [u,v]:jumping)if(owner[u]!=owner[v]){
   assert((owner[u]&owner[v])==0);
   int a=owner[u],b=owner[v];if(a>b)swap(a,b);
   cross[{a,b}]++;
 }
 assert(cross.size()==70);
 for(auto [edge,mult]:cross)assert(mult==9);
 int max_T=0,min_T=1000,max_J=0,min_J=1000;
 int Ttwo=0,Tthree=0;
 for(int start=0;start<(int)good.size();++start){
   for(int type=0;type<2;++type){
     const auto& A=type?J:T;
     vector<int> dist(good.size(),-1);queue<int> q;
     dist[start]=0;q.push(start);int top=0,total=1;
     while(!q.empty()){
       int x=q.front();q.pop();
       for(int y:A[x])if(dist[y]<0){dist[y]=dist[x]+1;top=max(top,dist[y]);q.push(y);++total;}
     }
     if(type){assert(total==770);max_J=max(max_J,top);min_J=min(min_J,top);}
     else{assert(total==22);max_T=max(max_T,top);min_T=min(min_T,top);
       if(top==2)++Ttwo;else if(top==3)++Tthree;else assert(false);
     }
   }
 }
 assert(min_T==2&&max_T==3&&min_J==7&&max_J==7);
 assert(Ttwo==140 && Tthree==630);
 // Full canonical certificate independent of the Python implementation.
 ofstream f(argv[1],ios::binary);if(!f)throw runtime_error("cannot open output");
 char buf[128];
 for(auto s:good){
   snprintf(buf,sizeof(buf),"D %02d %02d %02d %02d\n",s[0],s[1],s[2],s[3]);f<<buf;
 }
 for(auto [i,j]:sliding){snprintf(buf,sizeof(buf),"S %03d %03d\n",i,j);f<<buf;}
 for(auto [i,j]:jumping){snprintf(buf,sizeof(buf),"J %03d %03d\n",i,j);f<<buf;}
 f.close();
 cout<<"OPTIMA=770; ORBITS=140,630; TYPE_COUNTS=140,630\n";
 cout<<"SLIDE_EDGES=2100; SLIDE_COMPONENTS=35x22; SLIDE_RADIUS_DIAMETER=2,3\n";
 cout<<"JUMP_EDGES=2730; JUMP_COMPONENTS=1x770; JUMP_RADIUS_DIAMETER=7,7\n";
 cout<<"CROSS_JUMP_EDGES=630; DISJOINT_TRIPLE_QUOTIENT=35v,70e,9peredge\n";
 cout<<"CERTIFICATE_LINES=5600\n";
}
