// Independent enumeration of all 24^4 full-order Mallows profiles.
// Compile: c++ -O2 -std=c++17 verify_independent.cpp -o check && ./check
#include <array>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <cstdlib>
using namespace std;
struct Rank {array<int,4> rank; int inversions;};
int main(){
 array<array<Rank,24>,4> options;
 array<int,4> p={0,1,2,3}; int idx=0;
 do {
  int inv=0;
  for(int i=0;i<4;i++)for(int j=i+1;j<4;j++) inv+=(p[i]>p[j]);
  for(int agent=0;agent<4;agent++){
    Rank z; z.rank.fill(-1); int k=0;
    for(int v:p) if(v!=agent) z.rank[v]=k++;
    z.inversions=inv; options[agent][idx]=z;
  }
  idx++;
 }while(next_permutation(p.begin(),p.end()));
 if(idx!=24) return 1;
 const int mates[3][4]={{1,0,3,2},{2,3,0,1},{3,2,1,0}};
 long long counts[25]={};
 for(const auto &a:options[0]) for(const auto &b:options[1])
 for(const auto &c:options[2]) for(const auto &d:options[3]){
   const Rank* ranks[4]={&a,&b,&c,&d};
   bool any_stable=false;
   for(int m=0;m<3;m++){
     bool blocked=false;
     for(int i=0;i<4 && !blocked;i++) for(int j=i+1;j<4;j++){
       if(mates[m][i]==j)continue;
       if(ranks[i]->rank[j]<ranks[i]->rank[mates[m][i]] &&
          ranks[j]->rank[i]<ranks[j]->rank[mates[m][j]]){
         blocked=true; break;
       }
     }
     if(!blocked){any_stable=true;break;}
   }
   if(!any_stable)counts[a.inversions+b.inversions+c.inversions+d.inversions]++;
 }
 const long long expected[25]={0,0,3,22,82,208,404,642,870,1038,1129,1162,1168,1162,1129,1038,870,642,404,208,82,22,3,0,0};
 long long sum=0;
 for(int k=0;k<25;k++){
   if(counts[k]!=expected[k]){cerr<<"Mismatch at exponent "<<k<<endl; return 2;}
   sum+=counts[k];
 }
 if(sum!=12288) return 3;
 cout<<"VERIFY_INDEPENDENT_OK: 331776 full-draw profiles, 12288 unsolvable, 25 exact inversion coefficients"<<endl;
}
