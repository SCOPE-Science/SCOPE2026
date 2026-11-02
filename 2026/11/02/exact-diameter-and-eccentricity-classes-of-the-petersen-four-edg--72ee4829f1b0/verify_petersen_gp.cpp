#include <array>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <cassert>
using namespace std;
using State = array<unsigned char,15>;
struct Edge {int u,v;};
int main(){
 vector<Edge> E;
 for(int i=0;i<5;i++)E.push_back({i,(i+1)%5});
 for(int i=0;i<5;i++)E.push_back({i,5+i});
 for(int i=0;i<5;i++)E.push_back({5+i,5+(i+2)%5});
 int adjv[10][10]={}; int edge_index[10][10];
 for(int i=0;i<10;i++)for(int j=0;j<10;j++)edge_index[i][j]=-1;
 for(int k=0;k<15;k++){int u=E[k].u,v=E[k].v;adjv[u][v]=adjv[v][u]=1;edge_index[u][v]=edge_index[v][u]=k;}
 // Independently generate an ordered matching decomposition of the edge set.
 vector<int> match;
 for(int mask=1;mask<(1<<15);mask++){
  int used=0;bool ok=1;
  for(int i=0;i<15;i++)if(mask&(1<<i)){
   int v=(1<<E[i].u)|(1<<E[i].v);
   if(used&v){ok=0;break;}used|=v;
  }
  if(ok)match.push_back(mask);
 }
 vector<State> states; states.reserve(49920);
 for(int a:match){
  for(int b:match){if(a&b)continue;
   int ab=a|b;
   for(int c:match){if(ab&c)continue;
    int d=((1<<15)-1)^(ab|c);if(!d)continue;
    int used=0;bool ok=true;
    for(int i=0;i<15;i++)if(d&(1<<i)){
     int v=(1<<E[i].u)|(1<<E[i].v);if(used&v){ok=false;break;}used|=v;
    }
    if(!ok)continue;
    State s{};
    for(int i=0;i<15;i++)s[i]=(a>>i&1)?0:((b>>i&1)?1:((c>>i&1)?2:3));
    states.push_back(s);
   }
  }
 }
 sort(states.begin(),states.end());states.erase(unique(states.begin(),states.end()),states.end());
 if(states.size()!=49920){cerr<<"state count: "<<states.size()<<"\n";return 1;}
 auto key=[](const State &s){return string((const char*)s.data(),15);};
 unordered_map<string,int> I;I.reserve(states.size()*2);
 for(int i=0;i<(int)states.size();i++)I.emplace(key(states[i]),i);
 vector<vector<int>> nbr(states.size());
 long long checks=0;
 for(int t=0;t<(int)states.size();t++){
  const State &s=states[t];set<int> neighbors;
  for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){
   // Union-find connected components of the two-colour subgraph on the ORIGINAL vertices.
   int parent[10];iota(parent,parent+10,0);
   auto root=[&](int x){while(parent[x]!=x)x=parent[x];return x;};
   for(int i=0;i<15;i++)if(s[i]==a||s[i]==b){int u=root(E[i].u),v=root(E[i].v);parent[v]=u;}
   map<int,vector<int>> comp;
   for(int i=0;i<15;i++)if(s[i]==a||s[i]==b)comp[root(E[i].u)].push_back(i);
   for(const auto &kv:comp){State x=s;for(int i:kv.second)x[i]=(unsigned char)(a+b-x[i]);
    auto j=I.find(key(x));if(j==I.end()){cerr<<"bad recolour\n";return 2;}
    if(j->second!=t)neighbors.insert(j->second);
    checks++;
   }
  }
  nbr[t].assign(neighbors.begin(),neighbors.end());
 }
 for(int i=0;i<(int)nbr.size();i++)for(int j:nbr[i])if(!binary_search(nbr[j].begin(),nbr[j].end(),i)){cerr<<"asymmetric\n";return 3;}
 // Generate every automorphism of GP(5,2) directly, using adjacency preservation.
 vector<array<int,10>> autos;array<int,10> p; p.fill(-1);bool occupied[10]={};
 auto rec=[&](auto &&self,int k)->void{
  if(k==10){autos.push_back(p);return;}
  for(int j=0;j<10;j++)if(!occupied[j]){
   bool ok=1;for(int a=0;a<k;a++)if(adjv[k][a]!=adjv[j][p[a]]){ok=0;break;}
   if(ok){p[k]=j;occupied[j]=true;self(self,k+1);occupied[j]=false;p[k]=-1;}
  }
 };rec(rec,0);
 if(autos.size()!=120){cerr<<"automorphisms "<<autos.size()<<"\n";return 4;}
 vector<array<int,15>> perma;
 for(auto &q:autos){array<int,15> f;for(int i=0;i<15;i++){f[i]=edge_index[q[E[i].u]][q[E[i].v]];if(f[i]<0)return 5;}perma.push_back(f);}
 vector<char> seen(states.size(),0);map<pair<int,int>,long long> orbitclasses;map<int,long long> ecc_count;map<int,long long> degree_count;int totalorbits=0;long long diametral_twice=0;
 for(int t=0;t<(int)states.size();t++){
  if(seen[t])continue;
  vector<int> orbit;orbit.push_back(t);seen[t]=1;
  for(size_t at=0;at<orbit.size();at++){
   int u=orbit[at];State s=states[u];
   for(const auto &pm:perma){State x{};for(int k=0;k<15;k++)x[pm[k]]=s[k];
    int j=I.at(key(x));if(!seen[j]){seen[j]=1;orbit.push_back(j);}
   }
   for(int a=0;a<3;a++){State x=s;for(auto &z:x){if(z==a)z=a+1;else if(z==a+1)z=a;}
    int j=I.at(key(x));if(!seen[j]){seen[j]=1;orbit.push_back(j);}
   }
  }
  vector<short> dist(states.size(),-1);queue<int> bfs;bfs.push(t);dist[t]=0;vector<int> spheres(1,0);
  while(!bfs.empty()){int i=bfs.front();bfs.pop();int d=dist[i];if(d==(int)spheres.size())spheres.push_back(0);spheres[d]++;
   for(int j:nbr[i])if(dist[j]==-1){dist[j]=d+1;bfs.push(j);}
  }
  int count=accumulate(spheres.begin(),spheres.end(),0);if(count!=(int)states.size()){cerr<<"disconnected\n";return 6;}
  int ecc=(int)spheres.size()-1;
  orbitclasses[{(int)orbit.size(),ecc}]++;
  ecc_count[ecc]+=orbit.size();
  if(ecc==8)diametral_twice+=(long long)orbit.size()*spheres.back();
  degree_count[nbr[t].size()]+=orbit.size();
  totalorbits++;
  cout<<"ORBIT size="<<orbit.size()<<" degree="<<nbr[t].size()<<" ecc="<<ecc<<" spheres=";
  for(size_t x=0;x<spheres.size();x++)cout<<(x?",":"")<<spheres[x];
  cout<<"\n";
 }
 long long edges=0;for(auto &x:nbr)edges+=x.size();
 edges/=2;
 cout<<"AUTOS="<<autos.size()<<" ORBITS="<<totalorbits<<" STATES="<<states.size()<<" EDGES="<<edges<<" DIAMETRAL_PAIRS="<<diametral_twice/2<<"\n";
 cout<<"ECCENTRICITY";for(auto [e,c]:ecc_count)cout<<" "<<e<<":"<<c;cout<<"\n";
 cout<<"DEGREES";for(auto [d,c]:degree_count)cout<<" "<<d<<":"<<c;cout<<"\n";
 if(totalorbits!=21||edges!=377280||ecc_count[7]!=45600||ecc_count[8]!=4320||degree_count[15]!=44160||degree_count[16]!=5760||diametral_twice!=5760)return 7;
 cout<<"INDEPENDENT_GP_MATCHING_VERIFICATION_PASS\n";
 return 0;
}
