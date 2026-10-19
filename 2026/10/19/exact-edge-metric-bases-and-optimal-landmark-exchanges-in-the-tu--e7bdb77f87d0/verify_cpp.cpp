#include <bits/stdc++.h>
using namespace std;
// Fully independent distance-vector enumeration and all-source BFS.
int main(){
 vector<pair<int,int>> duads;
 for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)duads.emplace_back(a,b);
 vector<array<int,3>> synthemes;
 function<void(vector<int>,vector<int>)> go=[&](vector<int> rem,vector<int> used){
   if(rem.empty()){array<int,3> x{used[0],used[1],used[2]};sort(x.begin(),x.end());synthemes.push_back(x);return;}
   int a=rem[0];for(int j=1;j<(int)rem.size();j++){
      int b=rem[j];vector<int> nr;for(int z:rem)if(z!=a && z!=b)nr.push_back(z);
      int idx=(int)(find(duads.begin(),duads.end(),make_pair(a,b))-duads.begin());
      auto uu=used;uu.push_back(idx);go(nr,uu);
   }
 };go({0,1,2,3,4,5},{});sort(synthemes.begin(),synthemes.end());
 vector<pair<int,int>> inc;
 vector<vector<int>> g(30);
 for(int s=0;s<15;s++)for(int d:synthemes[s]){
   inc.push_back({d,15+s});g[d].push_back(15+s);g[15+s].push_back(d);
 }
 sort(inc.begin(),inc.end());assert(inc.size()==45);
 int D[30][30];
 for(int v=0;v<30;v++){
   fill(D[v],D[v]+30,-1);queue<int> q;q.push(v);D[v][v]=0;
   while(!q.empty()){int u=q.front();q.pop();for(int w:g[u])if(D[v][w]<0){D[v][w]=1+D[v][u];q.push(w);}}
 }
 int ed[30][45];
 for(int v=0;v<30;v++)for(int e=0;e<45;e++)ed[v][e]=min(D[v][inc[e].first],D[v][inc[e].second]);
 auto isbasis=[&](const vector<int>&sel){
   int codes[45];
   for(int e=0;e<45;e++){
     int c=0;for(int v:sel)c=5*c+ed[v][e];codes[e]=c;
   }
   sort(codes,codes+45);
   return adjacent_find(codes,codes+45)==codes+45;
 };
 int low=0;for(int k=1;k<=4;k++){
   unsigned long long cnt=0;vector<int> s;
   function<void(int,int)> dfs=[&](int next,int need){
     if(need==0){cnt+=isbasis(s);return;}
     for(int v=next;v<=30-need;v++){s.push_back(v);dfs(v+1,need-1);s.pop_back();}
   };dfs(0,k);cout<<"size_"<<k<<"_bases "<<cnt<<"\n";if(cnt) return 3;
 }
 vector<uint32_t> bases;vector<int>sel;
 function<void(int,int)> dfs=[&](int next,int need){
  if(need==0){if(isbasis(sel)){uint32_t x=0;for(int v:sel)x|=1u<<v;bases.push_back(x);}return;}
  for(int v=next;v<=30-need;v++){sel.push_back(v);dfs(v+1,need-1);sel.pop_back();}
 };dfs(0,5);sort(bases.begin(),bases.end());
 cout<<"minimum_basis_size 5\n"<<"minimum_basis_count "<<bases.size()<<"\n";
 unordered_map<uint32_t,int> pos;pos.reserve(10000);for(int i=0;i<(int)bases.size();i++)pos[bases[i]]=i;
 vector<vector<int>> adj(bases.size());map<int,int> degree_counts, eccentricity_counts;int n=bases.size();
 for(int i=0;i<n;i++){
  uint32_t x=bases[i];
  for(int a=0;a<30;a++)if((x>>a)&1)
   for(int b=0;b<30;b++)if(!((x>>b)&1)){
     auto it=pos.find(x^(1u<<a)^(1u<<b));if(it!=pos.end())adj[i].push_back(it->second);
   }
  sort(adj[i].begin(),adj[i].end());degree_counts[adj[i].size()]++;
 }
 long long nedges=0;for(auto &a:adj)nedges+=a.size();nedges/=2;
 cout<<"token_jump_edges "<<nedges<<"\n";
 cout<<"degrees";for(auto [d,c]:degree_counts)cout<<" "<<d<<":"<<c;cout<<"\n";
 int diameter=0,radius=10000;long long diam_pairs=0;pair<uint32_t,uint32_t> witness{0,0};
 vector<int> dist(n,-1),queue_arr(n);
 for(int src=0;src<n;src++){
   fill(dist.begin(),dist.end(),-1);
   int head=0,tail=0;dist[src]=0;queue_arr[tail++]=src;
   while(head<tail){int u=queue_arr[head++];for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;queue_arr[tail++]=v;}}
   if(tail!=n){cerr<<"Disconnected at "<<src<<"\n";return 2;}
   int ec=*max_element(dist.begin(),dist.end());eccentricity_counts[ec]++;radius=min(radius,ec);diameter=max(diameter,ec);
   for(int j=src+1;j<n;j++)if(dist[j]==7){diam_pairs++;if(witness.first==0){witness={bases[src],bases[j]};}}
 }
 cout<<"components 1\n"<<"radius "<<radius<<"\n"<<"diameter "<<diameter<<"\n";
 cout<<"eccentricities";for(auto [d,c]:eccentricity_counts)cout<<" "<<d<<":"<<c;cout<<"\n";
 cout<<"distance_7_unordered_pairs "<<diam_pairs<<"\n";
 cout<<"diameter_witness_bitmasks "<<witness.first<<" "<<witness.second<<"\n";
}
