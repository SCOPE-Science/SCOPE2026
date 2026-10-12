// Exhaustive cross-check for 3-uniform words representing K_3 square K_4.
// Enumerates all placements of the second row by bitmasks, then merges two
// admissible two-row restrictions with an online alternation automaton.
#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;
using Gaps=array<vector<unsigned char>,12>;
vector<Gaps> P;

bool alternates(const array<int,3>& a,const array<int,3>& b){
  array<pair<int,int>,6> s;
  for(int i=0;i<3;i++){s[i]={a[i],0};s[i+3]={b[i],1};}
  sort(s.begin(),s.end());
  for(int i=1;i<6;i++)if(s[i].second==s[i-1].second)return false;
  return true;
}
void generate(){
 int perm[4]={0,1,2,3};
 do{
  // The canonical first letter is row-A column 0.  Choose the locations
  // of the remaining 11 A symbols among the remaining 23 positions.
  // Hence all interleavings of two forced 3-fold clique orders occur.
  for(uint32_t s=0;s<(1u<<23);s++){
   if(__builtin_popcount(s)!=11)continue;
   array<array<int,3>,4>A{},B{};int ia=0,ib=0;
   Gaps gap;int currentgap=-1;
   for(int pos=0;pos<24;pos++){
    bool isA=(pos==0)||(pos>0&&((s>>(pos-1))&1));
    if(isA){int col=ia%4;A[col][ia/4]=pos;ia++;currentgap++;}
    else {int col=perm[ib%4];B[col][ib/4]=pos;ib++;gap[currentgap].push_back(col);}
   }
   bool good=true;
   for(int i=0;i<4&&good;i++)for(int j=0;j<4;j++)
     if(alternates(A[i],B[j])!=(i==j)){good=false;break;}
   if(good)P.push_back(move(gap));
  }
 }while(next_permutation(perm,perm+4));
}
struct State{
 unsigned char last[16]{};uint16_t broken=0;
};
uint64_t feasible=0,matchingLeaves=0,pairs=0;
const uint16_t nonedges=0xFFFFu ^ ((1u<<0)|(1u<<5)|(1u<<10)|(1u<<15));
const Gaps* G1;const Gaps* G2;

bool step(State& s,unsigned char x,bool first){
 // x: B column (first=true) or C column (first=false).
 for(int k=0;k<4;k++){
  int i=first?x:k,j=first?k:x;
  int t=4*i+j;unsigned char type=first?1:2;
  if(s.last[t]==type){
   if(i==j)return false;
   s.broken|=(uint16_t)(1u<<t);
  }
  s.last[t]=type;
 }
 return true;
}
void gap_rec(int gap,int b,int c,State state);
void scan(int gap,State state){
 if(gap==12){matchingLeaves++;
   if((state.broken&nonedges)==nonedges)feasible++;
   return;
 }
 gap_rec(gap,0,0,state);
}
void gap_rec(int g,int b,int c,State state){
 auto& x=(*G1)[g];auto& y=(*G2)[g];
 if(b==(int)x.size()&&c==(int)y.size()){scan(g+1,state);return;}
 if(b<(int)x.size()){
  State next=state;
  if(step(next,x[b],true))gap_rec(g,b+1,c,next);
 }
 if(c<(int)y.size()){
  State next=state;
  if(step(next,y[c],false))gap_rec(g,b,c+1,next);
 }
}
int main(){
 generate();printf("admissible_pair_projections=%zu\n",P.size());
 for(const auto& b:P){G1=&b;
  for(const auto& c:P){G2=&c;pairs++;State st;scan(0,st);}
 }
 printf("projection_pairs=%llu\n",(unsigned long long)pairs);
 printf("match_alternating_shuffles=%llu\n",(unsigned long long)matchingLeaves);
 printf("full_representation_words=%llu\n",(unsigned long long)feasible);
 if(P.size()!=354||pairs!=125316||feasible!=0)return 1;
}
