#include <bits/stdc++.h>
using namespace std;
struct DSU{vector<int>p,s;DSU(int n):p(n),s(n,1){iota(p.begin(),p.end(),0);}int find(int v){return p[v]==v?v:p[v]=find(p[v]);}bool join(int a,int b){a=find(a);b=find(b);if(a==b)return false;if(s[a]<s[b])swap(a,b);p[b]=a;s[a]+=s[b];return true;}};
int main(){
 vector<int>tri;for(int v=0;v<(1<<7);v++)if(__builtin_popcount((unsigned)v)==3)tri.push_back(v);
 int N=tri.size(), distances[35][35];vector<vector<int>>adj(N);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j&&!(tri[i]&tri[j]))adj[i].push_back(j);
 for(int i=0;i<N;i++){
  for(int j=0;j<N;j++)distances[i][j]=-1;
  queue<int>q;q.push(i);distances[i][i]=0;
  while(!q.empty()){int j=q.front();q.pop();for(int k:adj[j])if(distances[i][k]<0){distances[i][k]=distances[i][j]+1;q.push(k);}}
 }
 vector<uint64_t> bases;
 for(int a=0;a<N-4;a++)for(int b=a+1;b<N-3;b++)for(int c=b+1;c<N-2;c++)for(int d=c+1;d<N-1;d++)for(int e=d+1;e<N;e++){
  int v[5]={a,b,c,d,e};
  uint64_t codes[35];bool ok=true;
  for(int i=0;i<N;i++){
   uint64_t z=0;
   for(int k=0;k<5;k++)z=(z<<2)|distances[i][v[k]];
   codes[i]=z;
   for(int j=0;j<i;j++)if(codes[j]==z){ok=false;break;}
   if(!ok)break;
  }
  if(ok){uint64_t mask=0;for(int k:v)mask|=1ull<<k;bases.push_back(mask);}
 }
 cout<<"minbases="<<bases.size()<<"\n";
 unordered_map<uint64_t,int>idx;idx.reserve(bases.size()*2);for(int i=0;i<(int)bases.size();i++)idx[bases[i]]=i;
 DSU conn(bases.size());vector<vector<int>> neighbors(bases.size());long long edges=0;map<int,int> deg_hist;vector<int>deg(bases.size());
 for(int i=0;i<(int)bases.size();i++){
  auto m=bases[i];int dg=0;
  for(int a=0;a<N;a++)if(m>>a&1)for(int b=0;b<N;b++)if(!(m>>b&1)){
   auto it=idx.find(m ^ (1ull<<a) ^ (1ull<<b));
   if(it!=idx.end()){dg++;if(it->second>i){edges++;conn.join(i,it->second);neighbors[i].push_back(it->second);neighbors[it->second].push_back(i);}}
  }
  deg[i]=dg;deg_hist[dg]++;
 }
 map<int,int> csize;for(int i=0;i<(int)bases.size();i++)csize[conn.find(i)]++;
 map<int,int>ch;for(auto [root,c]:csize)ch[c]++;
 cout<<"exchange_edges="<<edges<<" components="<<csize.size()<<" component_sizes:";for(auto [s,c]:ch)cout<<" "<<s<<"x"<<c;cout<<"\n";
 cout<<"degree_dist:";for(auto [d,c]:deg_hist)cout<<" "<<d<<":"<<c;cout<<"\n";
 DSU orb(bases.size());
 for(int p=0;p<6;p++){
  int perm[35];for(int i=0;i<N;i++){int x=tri[i];int bitp=(x>>p)&1,bitq=(x>>(p+1))&1;int y=x;if(bitp!=bitq)y^=(1<<p)|(1<<(p+1));perm[i]=lower_bound(tri.begin(),tri.end(),y)-tri.begin();}
  for(int i=0;i<(int)bases.size();i++){
   uint64_t nm=0,m=bases[i];while(m){int j=__builtin_ctzll(m);m&=m-1;nm|=1ull<<perm[j];}
   orb.join(i,idx.at(nm));
  }
 }
 map<int,int>orbs;for(int i=0;i<(int)bases.size();i++)orbs[orb.find(i)]++;
 map<int,int> oh;for(auto [r,s]:orbs)oh[s]++;
 cout<<"orbits="<<orbs.size()<<" orbital_sizes:";for(auto [s,c]:oh)cout<<" "<<s<<"x"<<c;cout<<"\n";
 // Orbit-representative all-pairs distances, exact by 7-letter automorphisms.
 map<int,int> eccentricity_hist;map<int,map<int,int>> orbit_ecc_hist;
 int mins=10000,maxs=0;
 for(auto [r,size]:orbs){
   vector<int> dist(bases.size(),-1);vector<int> queue_v(bases.size());
   int first=0,last=0;queue_v[last++]=r;dist[r]=0;int ecc=0;
   while(first<last){int x=queue_v[first++];ecc=max(ecc,dist[x]);for(int y:neighbors[x])if(dist[y]<0){dist[y]=dist[x]+1;queue_v[last++]=y;}}
   if(last != (int)bases.size()){cerr<<"Orbit bfs failed\n";return 2;}
   eccentricity_hist[ecc]+=size;orbit_ecc_hist[ecc][size]++;
   if(ecc==6){
     int dst=-1;for(int x=0;x<(int)bases.size();x++)if(dist[x]==6){dst=x;break;}
     cout<<"ecc6_orbit size="<<size<<" representative=";
     uint64_t z=bases[r];while(z){int j=__builtin_ctzll(z);z&=z-1;cout<<tri[j]<<",";}cout<<" farthest=";
     z=bases[dst];while(z){int j=__builtin_ctzll(z);z&=z-1;cout<<tri[j]<<",";}cout<<" degree="<<deg[r]<<"\n";
   }
   mins=min(mins,ecc);maxs=max(maxs,ecc);
 }
 cout<<"radius="<<mins<<" diameter="<<maxs<<" ecc_dist:";for(auto [ecc,c]:eccentricity_hist)cout<<" "<<ecc<<":"<<c;cout<<"\n";
 cout<<"orbits_by_ecc:";for(auto [ecc,h]:orbit_ecc_hist){cout<<" ecc"<<ecc;for(auto [sz,c]:h)cout<<" size"<<sz<<"x"<<c;}cout<<"\n";
 // Single-source exact BFS profile for a representative (not global diameter).
 vector<int> dis(bases.size(),-1);queue<int>q;q.push(0);dis[0]=0;map<int,int> profile;
 while(!q.empty()){
  int i=q.front();q.pop();auto m=bases[i];profile[dis[i]]++;
  for(int a=0;a<N;a++)if(m>>a&1)for(int b=0;b<N;b++)if(!(m>>b&1)){
   auto it=idx.find(m^(1ull<<a)^(1ull<<b));if(it!=idx.end() && dis[it->second]==-1){dis[it->second]=dis[i]+1;q.push(it->second);}
  }
 }
 cout<<"oneBFS:";for(auto [d,c]:profile)cout<<" "<<d<<":"<<c;cout<<"\n";
 cout<<"first_example_triples:";int counter=0;for(int i=0;i<35;i++)if(bases[0]>>i&1){cout<<" {";for(int j=0;j<7;j++)if(tri[i]>>j&1)cout<<j+1<<",";cout<<"}";}cout<<"\n";
}
