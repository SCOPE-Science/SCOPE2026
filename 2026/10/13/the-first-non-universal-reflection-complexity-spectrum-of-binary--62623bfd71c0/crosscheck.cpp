#include <iostream>
#include <array>
#include <map>
#include <string>
#include <set>
#include <cstdint>
using namespace std;
array<int,32> path{};
map<int,int> h;
long long nodes=0,solutions=0;
int direct_reflect(){
 string w;
 for(int i=0;i<32;i++) w+=char('0'+((path[i]>>4)&1));
 set<string> classes;
 for(int i=0;i<32;i++){
  string s;
  for(int j=0;j<6;j++) s+=w[(i+j)%32];
  string t(s.rbegin(),s.rend());
  classes.insert(min(s,t));
 }
 return (int)classes.size();
}
void dfs(int v,uint64_t used,int depth){
 ++nodes;
 if(depth==32){
  if(((v<<1)&31)!=0) return;
  ++solutions; ++h[direct_reflect()]; return;
 }
 for(int b=0;b<=1;b++){
   int z=((v<<1)&31)|b;
   if(!(used & (uint64_t(1)<<z))){
     path[depth]=z;dfs(z,used|(uint64_t(1)<<z),depth+1);
   }
 }
}
int main(){path[0]=0;dfs(0,1,1);
 cout << "GRAPH_DFS cycles="<<solutions<<" nodes="<<nodes;
 for(auto [r,c]:h) cout <<" r"<<r<<"="<<c;
 cout <<"\n";
 if(solutions!=2048 || h!=map<int,int>{{22,576},{25,960},{26,192},{28,256},{29,64}}) return 1;
 cout<<"GRAPH_DFS_VERIFY_OK\n";
}
