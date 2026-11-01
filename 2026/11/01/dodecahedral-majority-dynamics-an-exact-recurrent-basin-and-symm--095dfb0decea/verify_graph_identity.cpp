// Verify a vertex-by-vertex bijective isomorphism with GP(10,2).
#include <array>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
static constexpr int adj[20][3]={{1,10,19},{0,2,8},{1,3,6},{2,4,19},{3,5,17},{4,6,15},{2,5,7},{6,8,14},{1,7,9},{8,10,13},{0,9,11},{10,12,18},{11,13,16},{9,12,14},{7,13,15},{5,14,16},{12,15,17},{4,16,18},{11,17,19},{0,3,18}};
int main(){ifstream f("gp10_2_isomorphism.tsv");string header;getline(f,header);array<int,20> a;bool seen[20]={};
for(int i=0;i<20;i++){int v=-1,w=-1;f>>v>>w;if(v!=i||w<0||w>=20||seen[w]){cerr<<"INVALID_MAP\n";return 1;}a[v]=w;seen[w]=true;}
int more=-1;if(f>>more){cerr<<"EXTRA_MAP\n";return 1;}
bool e[20][20]={};for(int i=0;i<10;i++){int j=(i+1)%10, k=(i+2)%10;e[i][j]=e[j][i]=true;e[i][i+10]=e[i+10][i]=true;e[i+10][k+10]=e[k+10][i+10]=true;}
for(int v=0;v<20;v++)for(int w=0;w<20;w++){
 bool yes=false;for(int k:adj[v])if(k==w)yes=true;
 if(yes!=e[a[v]][a[w]]){cerr<<"EDGE_MISMATCH\n";return 1;}
}
cout<<"EXPLICIT_ISOMORPHISM_TO_GP_10_2_VERIFIED\n20_VERTICES_30_EDGES_3_REGULAR\n";
}
