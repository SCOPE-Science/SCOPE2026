// Exact graph automorphism enumeration by backtracking partial adjacency isomorphisms.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
using namespace std;
static constexpr int a[20][3]={{1,10,19},{0,2,8},{1,3,6},{2,4,19},{3,5,17},{4,6,15},{2,5,7},{6,8,14},{1,7,9},{8,10,13},{0,9,11},{10,12,18},{11,13,16},{9,12,14},{7,13,15},{5,14,16},{12,15,17},{4,16,18},{11,17,19},{0,3,18}};
static bool e[20][20]{};
static array<int,20> p;
static bool taken[20]{};
static set<array<int,20>> auts;
static uint64_t nodes=0; static uint64_t root_counts[20]={};
void dfs(int depth){
 ++nodes;
 if(depth==20){auts.insert(p);root_counts[p[0]]++;return;}
 int bestv=-1,bestmapped=-1;
 for(int v=0;v<20;v++)if(p[v]<0){int c=0;for(int u=0;u<20;u++)if(p[u]>=0&&e[v][u])c++;
  if(c>bestmapped){bestv=v;bestmapped=c;}
 }
 for(int w=0;w<20;w++)if(!taken[w]){
  bool ok=true;for(int u=0;u<20;u++)if(p[u]>=0 && e[bestv][u]!=e[w][p[u]]){ok=false;break;}
  if(!ok)continue;
  p[bestv]=w;taken[w]=true;dfs(depth+1);taken[w]=false;p[bestv]=-1;
 }
}
int main(){for(int i=0;i<20;i++)for(int v:a[i])e[i][v]=true;for(int i=0;i<20;i++)p[i]=-1;
 dfs(0);
 if(auts.size()!=120){cerr<<"BAD_GROUP "<<auts.size()<<"\n";return 1;}
 set<array<int,20>> fileaut;ifstream f("automorphisms.csv");string line;
 while(getline(f,line)){stringstream ss(line);array<int,20> perm;char sep;for(int i=0;i<20;i++){ss>>perm[i];if(i<19)ss>>sep;}fileaut.insert(perm);}
 if(fileaut!=auts){cerr<<"GROUP_FILE_NOT_EXHAUSTIVE\n";return 1;}
 cout<<"AUTOMORPHISM_GROUP_EXHAUSTIVE=120\nGROUP_FILE_MATCHES_EXACTLY=YES\nBACKTRACK_NODES="<<nodes<<"\n";
}
