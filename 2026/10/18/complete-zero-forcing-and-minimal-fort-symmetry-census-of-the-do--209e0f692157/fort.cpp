#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <algorithm>
using namespace std;
constexpr int N=20, LIM=1<<N, ALL=LIM-1;
int main(){array<array<int,3>,N> g{};for(int i=0;i<10;i++){g[i]={(i+9)%10,(i+1)%10,10+i};g[i+10]={i,10+(i+8)%10,10+(i+2)%10};}
vector<uint32_t> zeta(LIM,0);vector<uint8_t> original(LIM,0);for(int m=1;m<LIM;m++){bool ok=true;for(int v=0;v<N && ok;v++)if(!(m&(1<<v))){int k=((m>>g[v][0])&1)+((m>>g[v][1])&1)+((m>>g[v][2])&1);if(k==1)ok=false;}if(ok){zeta[m]=1;original[m]=1;}}
for(int i=0;i<N;i++)for(int m=0;m<LIM;m++)if(m&(1<<i))zeta[m]+=zeta[m^(1<<i)];
array<int,N+1> forcing{},minimal{};uint64_t forts=0,minfort=0;vector<int> mf; for(int m=0;m<LIM;m++){int s=ALL^m;int k=__builtin_popcount((unsigned)s); if(!zeta[m])forcing[k]++;if(original[m])forts++;if(original[m]&&zeta[m]==1){int j=__builtin_popcount((unsigned)m);minimal[j]++;minfort++;mf.push_back(m);}}
cout<<"FORTS_OK all_nonempty="<<forts<<" minimal="<<minfort<<"\n";
cout<<"MIN_FORT_SPECTRUM=";for(int k=0;k<=N;k++)if(minimal[k])cout<<k<<":"<<minimal[k]<<",";cout<<"\nFORCING_POLYNOMIAL=";for(int k=0;k<=N;k++)if(forcing[k])cout<<k<<":"<<forcing[k]<<",";cout<<"\n";
ofstream out("fort_status.bin",ios::binary);for(int m=0;m<LIM;m++){unsigned char a=(zeta[ALL^m]==0);out.write((char*)&a,1);}out.close();ofstream fo("minfort_masks.txt");for(auto m:mf)fo<<m<<"\n";fo.close();
return 0;}
