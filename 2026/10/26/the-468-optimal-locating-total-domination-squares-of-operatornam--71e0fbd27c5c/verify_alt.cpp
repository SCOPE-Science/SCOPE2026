#include <bits/stdc++.h>
using namespace std;
int main(){
 const int q=3;vector<array<int,3>> v;
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
  if(!x&&!y&&!z)continue;
  array<int,3>a={x,y,z};int c=x?x:y?y:z;int inv=c==1?1:2;for(int&i:a)i=i*inv%3;if(find(v.begin(),v.end(),a)==v.end())v.push_back(a);
 }
 assert(v.size()==13); sort(v.begin(),v.end());
 int P[13]={},L[13]={};
 for(int i=0;i<13;i++)for(int j=0;j<13;j++){
  int dot=0;for(int k=0;k<3;k++)dot+=v[i][k]*v[j][k];
  if(dot%3==0){P[i]|=1<<j;L[j]|=1<<i;}
 }
 vector<int> coverPts,coverLines;
 bool pcov[8192]={},lcov[8192]={};
 int reqLine[8192][13]; int reqPt[8192][13];
 for(int s=0;s<8192;s++){
   pcov[s]=true;lcov[s]=true;
   for(int i=0;i<13;i++)if(!(s&P[i])) pcov[s]=false;
   for(int i=0;i<13;i++)if(!(s&L[i])) lcov[s]=false;
   if(pcov[s])coverPts.push_back(s);
   if(lcov[s])coverLines.push_back(s);
   for(int i=0;i<13;i++){
    reqLine[s][i]=s&L[i];reqPt[s][i]=s&P[i];
   }
 }
 cerr << "point blocking sets "<<coverPts.size()<<" line covers "<<coverLines.size()<<"\n";
 vector<pair<int,int>> res; map<pair<int,int>,int> counts;
 int minval=100;
 for(int a:coverPts){
  int ap=__builtin_popcount((unsigned)a);
  if(ap>minval-4) continue;
  for(int b:coverLines){
   int bp=__builtin_popcount((unsigned)b); if(ap+bp>minval)continue;
   bool ok=true;
   for(int i=0;i<13&&ok;i++)if(!(a>>i&1))for(int j=i+1;j<13;j++)if(!(a>>j&1)&&reqPt[b][i]==reqPt[b][j]){ok=false;break;}
   if(!ok)continue;
   for(int i=0;i<13&&ok;i++)if(!(b>>i&1))for(int j=i+1;j<13;j++)if(!(b>>j&1)&&reqLine[a][i]==reqLine[a][j]){ok=false;break;}
   if(!ok)continue;
   if(ap+bp<minval){minval=ap+bp;res.clear();counts.clear();cerr<<"NEW MIN "<<minval<<"\n";}
   res.emplace_back(a,b);counts[{ap,bp}]++;
  }
 }
 cout<<"min "<<minval<<" states "<<res.size()<<"\n";
 for(auto &[p,c]:counts)cout<<p.first<<"+"<<p.second<<"="<<c<<"\n";
 unordered_map<uint32_t,int> id;
 auto code=[](int a,int b){return (uint32_t)(a | (b<<13));};
 for(int i=0;i<(int)res.size();i++) id[code(res[i].first,res[i].second)]=i;
 vector<vector<int>> adj(res.size());
 for(int i=0;i<(int)res.size();i++){
  auto[a,b]=res[i];
  for(int u=0;u<13;u++)if(a>>u&1)for(int w=0;w<13;w++)if(!(a>>w&1)){
   auto it=id.find(code(a^(1<<u)^(1<<w),b));if(it!=id.end())adj[i].push_back(it->second);
  }
  for(int u=0;u<13;u++)if(b>>u&1)for(int w=0;w<13;w++)if(!(b>>w&1)){
   auto it=id.find(code(a,b^(1<<u)^(1<<w)));if(it!=id.end())adj[i].push_back(it->second);
  }
 }
 map<int,int>deg;int edges=0;for(auto &ns:adj){deg[ns.size()]++;edges+=ns.size();}cout<<"edges "<<edges/2<<" deg ";for(auto [k,c]:deg)cout<<k<<":"<<c<<" ";cout<<"\n";
 vector<int>vis(res.size());map<int,int>sizes;for(int i=0;i<(int)res.size();i++)if(!vis[i]){vector<int>q={i};vis[i]=1;for(int x=0;x<(int)q.size();x++)for(int j:adj[q[x]])if(!vis[j]){vis[j]=1;q.push_back(j);}sizes[q.size()]++;}
 cout<<"components ";for(auto[k,c]:sizes)cout<<k<<":"<<c<<" ";cout<<"\n";
 if(res.size()<25000){map<int,int>ecc;int dia=0;for(int i=0;i<(int)res.size();i++){
 vector<int>d(res.size(),-1),que={i};d[i]=0;
 for(int x=0;x<(int)que.size();x++)for(int j:adj[que[x]])if(d[j]<0){d[j]=d[que[x]]+1;que.push_back(j);}
 int e=*max_element(d.begin(),d.end()); ecc[e]++;dia=max(dia,e);
 }cout<<"ecc ";for(auto[k,c]:ecc)cout<<k<<":"<<c<<" ";cout<<"\n";}
}
