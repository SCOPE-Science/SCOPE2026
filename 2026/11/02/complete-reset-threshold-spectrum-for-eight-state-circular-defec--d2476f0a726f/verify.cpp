// Exhaustive count of normalized eight-state circular rank-seven automata.
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
static constexpr int N=8, STATES=1<<N;
using Mapping=array<int,N>;
int main(){
 array<int,STATES> shift{},image{};
 for(int s=0;s<STATES;s++)shift[s]=((s<<1)&255)|(s>>7);
 map<int,long long> frequency;
 map<int,Mapping> rare;
 long long congruence2=0,congruence4=0,both=0,invariant_not_sync=0,sync_no_invariant=0,not_sync_no_invariant=0,maximum=0;
 Mapping f{};
 for(int duplicate=1;duplicate<N;duplicate++)for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
  vector<int> others;for(int x=1;x<N;x++)if(x!=duplicate)others.push_back(x);
  do{
   f[i]=f[j]=duplicate;int k=0;for(int x=0;x<N;x++)if(x!=i&&x!=j)f[x]=others[k++];
   image[0]=0;for(int s=1;s<STATES;s++){
    int bit=__builtin_ctz((unsigned)s);
    image[s]=image[s&(s-1)]|(1<<f[bit]);
   }
   auto congruence=[&](int divisor)->bool {
    int residue[N];fill(residue,residue+N,-1);
    for(int x=0;x<N;x++){int r=x%divisor,v=f[x]%divisor;
     if(residue[r]!=-1&&residue[r]!=v)return false;
     residue[r]=v;
    }
    set<int> outputs;for(int r=0;r<divisor;r++)outputs.insert(residue[r]);
    return (int)outputs.size()==divisor;
   };
   bool c2=congruence(2),c4=congruence(4);
   congruence2+=c2;congruence4+=c4;both+=(c2&&c4);
   bool seen[STATES]={};int queue[STATES],first=0,last=1,level=0;
   queue[0]=255;seen[255]=true;int rt=0;
   while(first<last){int boundary=last,found=0;
    while(first<boundary){int s=queue[first++];if((s&(s-1))==0){found=1;break;}
     int t=shift[s];if(!seen[t]){seen[t]=true;queue[last++]=t;}
     t=image[s];if(!seen[t]){seen[t]=true;queue[last++]=t;}
    }
    if(found){rt=level;break;}level++;
   }
   frequency[rt]++;if(rt>maximum)maximum=rt;
   if(rt>=30){rare[rt]=f;}
   if(rt==0){invariant_not_sync+=(c2||c4);not_sync_no_invariant+=!(c2||c4);}
   else sync_no_invariant+=!(c2||c4);
  }while(next_permutation(others.begin(),others.end()));
 }
 long long total=0;for(auto [r,c]:frequency)total+=c;
 assert(total==141120);
 assert(congruence2==1728&&congruence4==192&&both==64);
 assert(frequency[0]==1856&&invariant_not_sync==1856&&not_sync_no_invariant==0&&sync_no_invariant==139264);
 assert(maximum==49&&frequency[49]==1);
 cout<<"threshold,classes\n";
 for(auto [r,c]:frequency)cout<<r<<","<<c<<"\n";
 cout<<"COUNTS total="<<total<<" nonsynchronizing="<<frequency[0]<<" synchronizing="<<total-frequency[0]<<" congruence2="<<congruence2<<" congruence4="<<congruence4<<" both="<<both<<"\n";
 cout<<"RARE threshold,mapping\n";for(auto [r,f]:rare){cout<<r<<",";for(int j=0;j<N;j++)cout<<f[j];cout<<"\n";}
 cout<<"VERIFY_OK\n";
}
