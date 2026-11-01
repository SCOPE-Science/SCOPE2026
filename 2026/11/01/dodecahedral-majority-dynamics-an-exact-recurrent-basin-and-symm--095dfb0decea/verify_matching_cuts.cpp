// A binary stable majority coloring on a cubic graph has at most one crossing neighbor at each vertex.
#include <cstdint>
#include <iostream>
#include <array>
using namespace std;
static constexpr int adj[20][3]={{1,10,19},{0,2,8},{1,3,6},{2,4,19},{3,5,17},{4,6,15},{2,5,7},{6,8,14},{1,7,9},{8,10,13},{0,9,11},{10,12,18},{11,13,16},{9,12,14},{7,13,15},{5,14,16},{12,15,17},{4,16,18},{11,17,19},{0,3,18}};
int main(){uint32_t nmatching=0,nfixed=0;for(uint32_t x=0;x<(1u<<20);x++){
 bool fixed=true,matching=true;
 for(int v=0;v<20;v++){
  int s=((x>>adj[v][0])&1u)+((x>>adj[v][1])&1u)+((x>>adj[v][2])&1u);
  int xi=(x>>v)&1u;
  if(xi!=(s>=2))fixed=false;
  int crossing=(xi?3-s:s);
  if(crossing>1)matching=false;
 }
 if(fixed!=matching){cerr<<"MATCHING_CUT_MISMATCH "<<x<<"\n";return 1;}
 nmatching+=matching;nfixed+=fixed;
}
if(nmatching!=118||nfixed!=118){cerr<<"COUNT_MISMATCH\n";return 1;}
cout<<"CUBIC_MAJORITY_FIXED_IFF_BICHROMATIC_EDGES_MATCHING=YES\nDODECAHEDRAL_LABELED_MATCHING_CUTS=118\nUNORDERED_COMPLEMENT_PAIRS=59\n";
}
