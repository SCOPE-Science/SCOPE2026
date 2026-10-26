#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
using State = array<unsigned char,11>;
static vector<int> adj(11,0);
void add(int a,int b){adj[a]|=1<<b;adj[b]|=1<<a;}
void init(){
 for(int i=0;i<5;i++){
  int j=(i+1)%5;
  add(i,j);add(i,5+j);add(j,5+i);add(5+i,10);
 }
 int m=0;for(int a:adj)m+=__builtin_popcount((unsigned)a);
 assert(m==40);
}
bool proper(const State&s){
 for(int i=0;i<11;i++)for(int j=i+1;j<11;j++)
  if((adj[i]>>j&1) && s[i]==s[j])return false;
 return true;
}
int encode(const State&s){int v=0;for(int i=0;i<11;i++)v=4*v+s[i];return v;}
State decode(int v){State s{};for(int i=10;i>=0;i--){s[i]=v%4;v/=4;}return s;}
vector<State> states;
void dfs(State &s,int i){
 if(i==11){states.push_back(s);return;}
 for(int c=0;c<4;c++){
  bool ok=true;
  for(int j=0;j<i;j++)if((adj[i]>>j&1)&&s[j]==c){ok=false;break;}
  if(ok){s[i]=c;dfs(s,i+1);}
 }
}
int main(){
 init();State current{};dfs(current,0);
 assert(states.size()==12480);
 // Completely separate exhaustive 4^11 finite universe scan.
 int total=0;for(int i=0;i<(1<<22);i++)if(proper(decode(i)))total++;
 assert(total==12480);
 cout<<"EXHAUSTIVE_UNIVERSE_OK 4194304 assignments, proper="<<total<<"\n";
 vector<int> codes;codes.reserve(states.size());
 map<int,int> idx;
 for(int i=0;i<(int)states.size();i++){
  int code=encode(states[i]);assert(idx.emplace(code,i).second);codes.push_back(code);
 }
 vector<vector<int>> graph(states.size());
 map<int,int> degrees;
 int edge2=0;
 for(int i=0;i<(int)states.size();i++){
  State s=states[i];
  for(int v=0;v<11;v++){
   auto old=s[v];
   for(int c=0;c<4;c++)if(c!=old){
    s[v]=c;
    if(proper(s)){
     auto it=idx.find(encode(s));assert(it!=idx.end());
     graph[i].push_back(it->second);
    }
   }
   s[v]=old;
  }
  sort(graph[i].begin(),graph[i].end());
  auto z=unique(graph[i].begin(),graph[i].end());assert(z==graph[i].end());
  degrees[(int)graph[i].size()]++;
  edge2+=graph[i].size();
 }
 assert(edge2%2==0);
 for(int i=0;i<(int)states.size();i++)for(int j:graph[i])
  assert(binary_search(graph[j].begin(),graph[j].end(),i));
 assert(edge2/2==45240);
 assert((degrees==map<int,int>{{5,480},{6,2640},{7,3840},{8,4320},{9,1200}}));
 cout<<"RECOLOR_GRAPH_OK vertices="<<states.size()<<" edges="<<edge2/2<<" degrees";
 for(auto [d,c]:degrees)cout<<" "<<d<<":"<<c;cout<<"\n";
 vector<int> which(states.size(),-1);vector<vector<int>> comps;
 for(int i=0;i<(int)states.size();i++)if(which[i]<0){
  int id=comps.size();vector<int> q{i};which[i]=id;
  for(size_t k=0;k<q.size();k++)for(int j:graph[q[k]])if(which[j]<0){which[j]=id;q.push_back(j);}
  comps.push_back(move(q));
 }
 assert(comps.size()==2&&comps[0].size()==6240&&comps[1].size()==6240);
 cout<<"COMPONENTS_OK sizes=6240,6240\n";
 for(int j=0;j<2;j++){
  map<int,int> hist;for(int t:comps[j])hist[graph[t].size()]++;
  assert((hist==map<int,int>{{5,240},{6,1320},{7,1920},{8,2160},{9,600}}));
  int diameter=0;
  vector<int> dist(states.size(),-1),touched;
  for(int x:comps[j]){
   queue<int> qu;qu.push(x);dist[x]=0;touched.push_back(x);
   while(!qu.empty()){
    int u=qu.front();qu.pop();
    for(int v:graph[u])if(dist[v]<0){dist[v]=dist[u]+1;diameter=max(diameter,dist[v]);qu.push(v);touched.push_back(v);}
   }
   assert(touched.size()==6240);
   for(int v:touched)dist[v]=-1;
   touched.clear();
  }
  cout<<"COMPONENT_DETAIL_OK component="<<j<<" diameter="<<diameter<<"\n";
 }
 int first=comps[0][0];State s=states[first];
 // Every permutation of the four named colours preserves components iff even.
 array<int,4> perm{0,1,2,3};int count=0;
 do{
  State t=s;for(int v=0;v<11;v++)t[v]=perm[s[v]];
  int j=idx.at(encode(t));
  int inv=0;for(int x=0;x<4;x++)for(int y=x+1;y<4;y++)inv+=(perm[x]>perm[y]);
  assert(which[j]==(inv%2));count++;
 }while(next_permutation(perm.begin(),perm.end()));assert(count==24);
 // For rotations the two classes are preserved; reflections interchange them.
 for(int shift=0;shift<5;shift++)for(int reflect=0;reflect<2;reflect++){
  State t=s;
  for(int i=0;i<5;i++){
   int k=((reflect?-i:i)+shift+10)%5;
   t[k]=s[i];t[5+k]=s[5+i];
  }
  t[10]=s[10];
  int j=idx.at(encode(t));assert(which[j]==reflect);
 }
 State a{{0,1,0,1,2,0,1,0,1,2,3}};
 State b{{0,1,0,1,2,0,1,0,1,3,2}};
 assert(proper(a)&&proper(b));
 assert(which[idx.at(encode(a))]!=which[idx.at(encode(b))]);
 cout<<"SYMMETRY_OK odd_color_permutations_and_reflections_swap_components\n";
 cout<<"VERIFY_OK\n";
}
// A concrete pair of legal four-colourings in different recolouring components.
