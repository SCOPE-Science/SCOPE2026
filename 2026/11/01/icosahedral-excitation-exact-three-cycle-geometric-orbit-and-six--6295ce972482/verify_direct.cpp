// Independent direct-iterate verification for three-state GH dynamics on the icosahedral graph.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int V=12, M=531441;
// Each mask uses one bit per neighbor; this representation is independent of the edge-list traversal.
constexpr array<unsigned,12> masks={
 (1u<<1)|(1u<<5)|(1u<<7)|(1u<<8)|(1u<<11),
 (1u<<0)|(1u<<2)|(1u<<5)|(1u<<6)|(1u<<8),
 (1u<<1)|(1u<<3)|(1u<<6)|(1u<<8)|(1u<<9),
 (1u<<2)|(1u<<4)|(1u<<6)|(1u<<9)|(1u<<10),
 (1u<<3)|(1u<<5)|(1u<<6)|(1u<<10)|(1u<<11),
 (1u<<0)|(1u<<1)|(1u<<4)|(1u<<6)|(1u<<11),
 (1u<<1)|(1u<<2)|(1u<<3)|(1u<<4)|(1u<<5),
 (1u<<0)|(1u<<8)|(1u<<9)|(1u<<10)|(1u<<11),
 (1u<<0)|(1u<<1)|(1u<<2)|(1u<<7)|(1u<<9),
 (1u<<2)|(1u<<3)|(1u<<7)|(1u<<8)|(1u<<10),
 (1u<<3)|(1u<<4)|(1u<<7)|(1u<<9)|(1u<<11),
 (1u<<0)|(1u<<4)|(1u<<5)|(1u<<7)|(1u<<10)
};
int pw[12];
int step(int s){
 int y[12],q=s;unsigned active=0;
 for(int j=0;j<12;j++){y[j]=q%3;q/=3;if(y[j]==1) active|=1u<<j;}
 int z=0;
 for(int j=0;j<12;j++){
  int next=y[j]==1?2:(y[j]==2?0:((masks[j]&active)?1:0));
  z+=next*pw[j];
 }
 return z;
}
int main(){pw[0]=1;for(int j=1;j<12;j++)pw[j]=3*pw[j-1];
 map<pair<int,int>,long long> hist;map<int,long long> basins;
 int p1=0,p3=0,late_witness=-1; vector<int> late;
 for(int s=0;s<M;s++){
  int x[10];x[0]=s;for(int t=1;t<=9;t++)x[t]=step(x[t-1]);
  if(x[9]!=x[6]){cerr<<"FAILED global identity at "<<s<<"\n";return 1;}
  int entry=-1;
  for(int t=0;t<=6;t++)if(x[t]==x[t+3]){entry=t;break;}
  if(entry<0){cerr<<"FAILED entrance at "<<s<<"\n";return 1;}
  int per=(x[entry]==x[entry+1])?1:3;
  if(entry==6){if(late_witness<0)late_witness=s;late.push_back(s);}
  hist[{per,entry}]++;
  int rep=(per==1)?x[6]:min(x[6],min(x[7],x[8]));
  basins[rep]++;
  if(entry==0){if(per==1)p1++;else p3++;}
 }
 map<int,int> basin_freq1,basin_freq3;
 for(auto [rep,bs]:basins){if(rep==0)basin_freq1[bs]++;else basin_freq3[bs]++;}
 cout<<"M="<<M<<" recurrent_fixed_states="<<p1<<" recurrent_three_cycle_states="<<p3
 <<" three_cycle_orbits="<<p3/3<<" late_witness="<<late_witness<<"\n";
 cout<<"period,entry,count\n";for(auto [pr,v]:hist)cout<<pr.first<<","<<pr.second<<","<<v<<"\n";
 cout<<"period,basin_size,orbits\n";for(auto [bs,c]:basin_freq1)cout<<"1,"<<bs<<","<<c<<"\n";
 for(auto [bs,c]:basin_freq3)cout<<"3,"<<bs<<","<<c<<"\n";
 cout<<"late_states "; for(int s:late)cout<<s<<","; cout<<"\nCHECK_OK\n";
}
