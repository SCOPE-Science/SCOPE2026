// Exhaustive classification of linear (9_3) incidence configurations.
// Compile: c++ -O2 -std=c++17 verify_census93.cpp -o census93 && ./census93
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
struct Triple { int a,b,c; uint64_t pm; };
vector<Triple> choices;
int pair_id[9][9], count_at[9] = {};
uint64_t taken_pairs = 0;
long long leaves=0, nodes=0;
map<int,long long> by_triangles;

int triangle_count() {
 bool e[9][9] = {};
 for (int a=0;a<9;a++) for(int b=a+1;b<9;b++)
  e[a][b]=e[b][a]=(taken_pairs & (uint64_t(1)<<pair_id[a][b]))!=0;
 int t=0;
 for(int a=0;a<9;a++) for(int b=a+1;b<9;b++) if(e[a][b])
  for(int c=b+1;c<9;c++) if(e[a][c]&&e[b][c]) ++t;
 return t;
}
void census(int point, int start) {
 ++nodes;
 if(point==9) {
  for(int i=0;i<9;i++) assert(count_at[i]==3);
  ++leaves; ++by_triangles[triangle_count()]; return;
 }
 if(count_at[point]==3) { census(point+1,0); return; }
 for(int j=start;j<(int)choices.size();j++) {
  const Triple &q=choices[j];
  if(q.a!=point || count_at[q.b]==3 || count_at[q.c]==3 || (taken_pairs & q.pm))continue;
  ++count_at[point]; ++count_at[q.b]; ++count_at[q.c]; taken_pairs |= q.pm;
  census(point,j+1);
  taken_pairs ^=q.pm; --count_at[point]; --count_at[q.b]; --count_at[q.c];
 }
}
using Design=array<array<int,3>,9>;
const Design pappus={{{0,3,6},{1,4,7},{2,5,8},{0,4,8},{1,5,6},{2,3,7},{0,5,7},{1,3,8},{2,4,6}}};
const Design nonp29={{{2,4,7},{1,4,8},{3,6,7},{3,5,8},{0,2,5},{1,5,7},{0,6,8},{1,2,6},{0,3,4}}};
const Design nonp30={{{0,1,8},{1,3,6},{5,6,8},{2,3,8},{2,5,7},{3,4,5},{1,4,7},{0,6,7},{0,2,4}}};
int encode(array<int,3> a){sort(a.begin(),a.end());return a[0]*81+a[1]*9+a[2];}
array<int,9> codes(const Design &d){array<int,9> x;for(int j=0;j<9;j++) x[j]=encode(d[j]);sort(x.begin(),x.end());return x;}
int automorphisms(const Design &d){
 array<int,9> p; for(int i=0;i<9;i++)p[i]=i;
 auto goal=codes(d);int aut=0;
 do{
  array<int,9> transform;
  for(int j=0;j<9;j++)transform[j]=encode({p[d[j][0]],p[d[j][1]],p[d[j][2]]});
  sort(transform.begin(),transform.end());
  if(transform==goal)++aut;
 }while(next_permutation(p.begin(),p.end()));
 return aut;
}
void validate(const Design &d,int expected_tri){
 int deg[9]={}; bool pairseen[9][9]={};
 for(auto line:d) {
  for(int a:line)++deg[a];
  for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){
   auto a=line[i], b=line[j];if(a>b)swap(a,b);
   assert(!pairseen[a][b]);pairseen[a][b]=true;
  }
 }
 for(int x:deg)assert(x==3);
 int t=0;for(int a=0;a<9;a++)for(int b=a+1;b<9;b++) if(pairseen[a][b])
 for(int c=b+1;c<9;c++)if(pairseen[a][c]&&pairseen[b][c])++t;
 assert(t==expected_tri);
}
int main(){
 int id=0;for(int a=0;a<9;a++)for(int b=a+1;b<9;b++)pair_id[a][b]=pair_id[b][a]=id++;
 for(int a=0;a<9;a++)for(int b=a+1;b<9;b++)for(int c=b+1;c<9;c++)
  choices.push_back({a,b,c,(uint64_t(1)<<pair_id[a][b]) |(uint64_t(1)<<pair_id[a][c])|(uint64_t(1)<<pair_id[b][c])});
 census(0,0);
 assert(leaves==73920 && by_triangles.size()==3 && by_triangles[27]==3360 && by_triangles[29]==30240 && by_triangles[30]==40320);
 for(auto [t,n]:by_triangles)cout<<"point_triangles="<<t<<" labelled_designs="<<n<<"\n";
 vector<pair<int,Design>> ds={{27,pappus},{29,nonp29},{30,nonp30}};
 for(auto [t,d]:ds){
  validate(d,t);int aut=automorphisms(d);long long orbit=362880/aut;
  assert(orbit==by_triangles[t]);
  cout<<"point_triangles="<<t<<" point_automorphisms="<<aut<<" orbit_size="<<orbit<<"\n";
 }
 cout<<"NINE_THREE_CLASSIFICATION_PASS labels="<<leaves<<" nodes="<<nodes<<" isomorphism_classes=3\n";
}
