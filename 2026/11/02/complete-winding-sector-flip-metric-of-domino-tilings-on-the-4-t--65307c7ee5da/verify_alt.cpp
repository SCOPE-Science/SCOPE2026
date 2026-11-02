// Independent exact enumeration of the 4-by-6 toroidal dimer face-flip graph.
// C++17: enumerates all bipartite matchings by assigning each black site a white neighbour.
// Local flips swap the two white partners of opposite black corners of a face.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
using U=uint64_t;
constexpr int R=4,C=6,VB=12;
int vertex(int r,int c){return ((r+R)%R)*C+((c+C)%C);}
struct Sector {int vertices=0,edges=0,radius=999,diameter=0;long long wiener=0;
 map<int,int>degrees,distances,eccentricities;};
int main(){
 vector<int> blacks,whites;
 array<int,R*C> bi,wi;bi.fill(-1);wi.fill(-1);
 for(int r=0;r<R;++r)for(int c=0;c<C;++c){
   int x=vertex(r,c);
   if((r+c)%2==0){bi[x]=blacks.size();blacks.push_back(x);}
   else{wi[x]=whites.size();whites.push_back(x);}
 }
 assert(blacks.size()==VB&&whites.size()==VB);
 vector<vector<int>> choices(VB);
 for(int b=0;b<VB;++b){
   int x=blacks[b],r=x/C,c=x%C;
   for(auto [dr,dc]:vector<pair<int,int>>{{-1,0},{0,-1},{0,1},{1,0}}){
     int w=wi[vertex(r+dr,c+dc)];assert(w>=0);
     choices[b].push_back(w);
   }
   sort(choices[b].begin(),choices[b].end());
   choices[b].erase(unique(choices[b].begin(),choices[b].end()),choices[b].end());
   assert(choices[b].size()==4);
 }
 vector<U> states;
 auto enumerate=[&](auto&&self,int k,int used,U encoded)->void{
   if(k==VB){states.push_back(encoded);return;}
   for(int w:choices[k])if(!(used&(1<<w)))
     self(self,k+1,used|(1<<w),encoded|(U(w)<<(4*k)));
 };
 enumerate(enumerate,0,0,0);
 sort(states.begin(),states.end());
 assert(states.size()==3108&&unique(states.begin(),states.end())==states.end());
 unordered_map<U,int> id;id.reserve(states.size()*2);
 for(int k=0;k<(int)states.size();++k)id[states[k]]=k;
 vector<array<int,2>> face_blacks,face_whites;
 for(int r=0;r<R;++r)for(int c=0;c<C;++c){
   array<int,4> corners{vertex(r,c),vertex(r+1,c),vertex(r,c+1),vertex(r+1,c+1)};
   array<int,2> fb,fw;int b=0,w=0;
   for(int v:corners){if(bi[v]>=0)fb[b++]=bi[v];else fw[w++]=wi[v];}
   assert(b==2&&w==2);
   face_blacks.push_back(fb);face_whites.push_back(fw);
 }
 assert(face_blacks.size()==24);
 vector<vector<int>> adj(states.size());
 for(int i=0;i<(int)states.size();++i){
   U mask=states[i];
   for(int f=0;f<24;++f){
     int b0=face_blacks[f][0],b1=face_blacks[f][1];
     int w0=(mask>>(4*b0))&15,w1=(mask>>(4*b1))&15;
     auto fw=face_whites[f];
     if(w0==w1||!((w0==fw[0]&&w1==fw[1])||(w0==fw[1]&&w1==fw[0])))continue;
     U replace=(mask&~(U(15)<<(4*b0))&~(U(15)<<(4*b1)))|
               (U(w1)<<(4*b0))|(U(w0)<<(4*b1));
     auto t=id.find(replace);assert(t!=id.end());
     adj[i].push_back(t->second);
   }
   sort(adj[i].begin(),adj[i].end());
   adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
 }
 for(int i=0;i<(int)states.size();++i)for(int j:adj[i])
    assert(binary_search(adj[j].begin(),adj[j].end(),i));
 long long globalEdges=0;
 for(const auto& v:adj)globalEdges+=v.size();
 assert(globalEdges==18096);
 auto flux=[&](U mask)->pair<int,int>{
   int h=0,v=0;
   for(int b=0;b<VB;++b){
     int x=blacks[b], y=whites[(mask>>(4*b))&15];
     int rx=x/C, cx=x%C, ry=y/C,cy=y%C;
     if(rx==ry&&((cx==0&&cy==5)||(cx==5&&cy==0)))
       h+=((rx+5)%2==0?1:-1);
     if(cx==cy&&((rx==0&&ry==3)||(rx==3&&ry==0)))
       v+=((3+cx)%2==0?1:-1);
   }
   return {h,v};
 };
 vector<int>component(states.size(),-1);
 map<pair<int,int>,Sector> result;
 int totalComponents=0;
 for(int root=0;root<(int)states.size();++root){
   if(component[root]!=-1)continue;
   int cid=totalComponents++;
   vector<int> part;
   queue<int> q;q.push(root);component[root]=cid;
   while(!q.empty()){
     int x=q.front();q.pop();part.push_back(x);
     for(int y:adj[x])if(component[y]==-1){component[y]=cid;q.push(y);}
   }
   auto phi=flux(states[root]);
   for(int x:part)assert(flux(states[x])==phi);
   assert(result.find(phi)==result.end());
   Sector& z=result[phi];z.vertices=part.size();
   for(int x:part){int d=adj[x].size();z.degrees[d]++;z.edges+=d;}
   assert(z.edges%2==0);z.edges/=2;
   long long weighted=0;
   for(int origin:part){
     vector<int>dist(states.size(),-1);
     queue<int> f;f.push(origin);dist[origin]=0;
     int visited=0, ecc=0;
     while(!f.empty()){
       int x=f.front();f.pop();++visited;
       ++z.distances[dist[x]];
       weighted+=dist[x];
       ecc=max(ecc,dist[x]);
       for(int y:adj[x])if(dist[y]==-1){dist[y]=dist[x]+1;f.push(y);}
     }
     assert(visited==(int)part.size());
     z.eccentricities[ecc]++;
     z.radius=min(z.radius,ecc);z.diameter=max(z.diameter,ecc);
   }
   assert(weighted%2==0);z.wiener=weighted/2;
 }
 assert(totalComponents==15&&result.size()==15);
 // Independent reference checks; ordered rows correspond to signed seam fluxes.
 const vector<tuple<int,int,int,int,int,int,long long>> expected={
  {-2,0,1,0,0,0,0},{-1,-1,24,24,12,12,1728},
  {-1,0,152,312,12,12,75600},{-1,1,24,24,12,12,1728},
  {0,-3,1,0,0,0,0},{0,-2,48,72,12,12,7032},
  {0,-1,576,1608,12,16,1238340},{0,0,1456,4968,12,20,8146752},
  {0,1,576,1608,12,16,1238340},{0,2,48,72,12,12,7032},
  {0,3,1,0,0,0,0},{1,-1,24,24,12,12,1728},
  {1,0,152,312,12,12,75600},{1,1,24,24,12,12,1728},
  {2,0,1,0,0,0,0}
 };
 long long totalWiener=0;
 int k=0;
 for(auto& [phi,z]:result){
   auto [h,v,n,e,r,d,w]=expected[k++];
   assert(phi.first==h&&phi.second==v&&z.vertices==n&&z.edges==e&&
          z.radius==r&&z.diameter==d&&z.wiener==w);
   assert(z.distances.at(0)==n);
   auto adjacentPairs=z.distances.find(1);
   assert((adjacentPairs==z.distances.end()?0:adjacentPairs->second)==2*e);
   int total=0;for(auto [dist,num]:z.distances)total+=num;
   assert(total==n*n);
   totalWiener+=z.wiener;
   cout<<"SECTOR "<<h<<" "<<v<<" "<<n<<" "<<e<<" "<<r<<" "<<d<<" "<<w<<" ";
   for(auto [dist,num]:z.distances)cout<<dist<<":"<<num<<",";
   cout<<"\n";
 }
 assert(totalWiener==10795608);
 cout<<"ALTERNATIVE_CERTIFICATE_OK count="<<states.size()<<" edges="<<globalEdges/2
     <<" components="<<totalComponents<<" wiener="<<totalWiener<<"\n";
}
