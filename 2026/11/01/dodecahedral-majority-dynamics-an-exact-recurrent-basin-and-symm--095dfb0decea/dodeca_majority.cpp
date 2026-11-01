#include <bits/stdc++.h>
using namespace std;
constexpr uint32_t N=(1u<<20);
const int adj[20][3]={{1,10,19},{0,2,8},{1,3,6},{2,4,19},{3,5,17},{4,6,15},{2,5,7},{6,8,14},{1,7,9},{8,10,13},{0,9,11},{10,12,18},{11,13,16},{9,12,14},{7,13,15},{5,14,16},{12,15,17},{4,16,18},{11,17,19},{0,3,18}};
static inline uint32_t go(uint32_t s){uint32_t t=0;for(int v=0;v<20;v++){int c=((s>>adj[v][0])&1)+((s>>adj[v][1])&1)+((s>>adj[v][2])&1);t|=(uint32_t)(c>=2)<<v;}return t;}
int main(int argc,char**argv){
 vector<uint32_t> nxt(N),indeg(N,0),order;order.reserve(N);
 for(uint32_t x=0;x<N;x++){nxt[x]=go(x);indeg[nxt[x]]++;}
 ofstream out("transition_u32le.bin",ios::binary);for(uint32_t x:nxt){for(int i=0;i<4;i++){uint8_t c=x>>(8*i);out.put(c);}}out.close();
 deque<uint32_t> q;for(uint32_t x=0;x<N;x++)if(!indeg[x])q.push_back(x);
 while(!q.empty()){uint32_t x=q.front();q.pop_front();order.push_back(x);if(!--indeg[nxt[x]])q.push_back(nxt[x]);}
 vector<int32_t> period(N,-1),entrance(N,-1),cycid(N,-1);vector<int> orbitcount(21), orbitstates(21);int norb=0;
 vector<uint32_t> representatives;vector<int> repsperiod;
 for(uint32_t x=0;x<N;x++)if(indeg[x]>0 && cycid[x]==-1){
  uint32_t y=x;vector<uint32_t> cyc;do{cyc.push_back(y);y=nxt[y];}while(y!=x);
  int d=cyc.size();if(d>20){cerr<<"period exceeded bound "<<d<<endl;return 1;}
  for(auto z:cyc){cycid[z]=norb;period[z]=d;entrance[z]=0;}
  representatives.push_back(*min_element(cyc.begin(),cyc.end()));repsperiod.push_back(d);
  orbitcount[d]++;orbitstates[d]+=d;norb++;
 }
 for(int i=(int)order.size()-1;i>=0;i--){uint32_t x=order[i];period[x]=period[nxt[x]];entrance[x]=entrance[nxt[x]]+1;cycid[x]=cycid[nxt[x]];}
 vector<uint64_t> countByPeriod(21,0);int maxentry=0;vector<uint64_t> byEntrance(40,0),byEntrFixed(40,0),byEntrTwo(40,0);vector<uint32_t> witness(40,0);
 for(uint32_t x=0;x<N;x++){int d=period[x],t=entrance[x];maxentry=max(maxentry,t);if(t>=40)abort();countByPeriod[d]++;byEntrance[t]++;if(d==1)byEntrFixed[t]++;if(d==2)byEntrTwo[t]++;if(!witness[t])witness[t]=x;}
 cout<<"GRAPH=dodecahedral N="<<N<<" ORBITS="<<norb<<" PERIODIC_STATES="<<N-order.size()<<" MAX_ENTRANCE="<<maxentry<<"\n";
 for(int d=1;d<=20;d++)if(orbitcount[d])cout<<"PERIOD="<<d<<" ORBITS="<<orbitcount[d]<<" STATES="<<orbitstates[d]<<" BASIN="<<countByPeriod[d]<<"\n";
 for(int i=0;i<=maxentry;i++)cout<<"ENTRANCE="<<i<<" total="<<byEntrance[i]<<" fixed="<<byEntrFixed[i]<<" two="<<byEntrTwo[i]<<" witness="<<witness[i]<<"\n";
 cout<<"WITNESS_TWO=";for(int i=0;i<norb;i++)if(repsperiod[i]==2){cout<<representatives[i]<<":"<<nxt[representatives[i]];break;}cout<<"\n";
 cout<<"checksum_transition_fnv64=";uint64_t h=14695981039346656037ull;for(uint32_t x:nxt)for(int i=0;i<4;i++){h^=(uint8_t)(x>>(8*i));h*=1099511628211ull;}cout<<hex<<h<<dec<<"\n";
 ofstream f("cycles.tsv");f<<"representative\tperiod\n";for(int i=0;i<norb;i++)f<<representatives[i]<<"\t"<<repsperiod[i]<<"\n";
}
