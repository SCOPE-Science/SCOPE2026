#include <bits/stdc++.h>
using namespace std;
int main(){
 constexpr int N=14,M=1<<14;
 int adj[N]={};
 for(int p=1;p<=7;p++)for(int a=1;a<=7;a++)if((__builtin_popcount(p&a)%2)==0){int x=p-1,y=7+a-1;adj[x]|=1<<y;adj[y]|=1<<x;}
 int cov[M];bool dom[M]={};cov[0]=0;
 int cover[N];for(int i=0;i<N;i++)cover[i]=adj[i]|(1<<i);
 for(int s=1;s<M;s++){int bit=s&-s,i=__builtin_ctz(bit);cov[s]=cov[s^bit]|cover[i];dom[s]=cov[s]==M-1;}
 for(int k=4;k<=8;k++){
  vector<int> vertex;int idx[M];fill(idx,idx+M,-1);
  for(int s=0;s<M;s++)if(dom[s]&&__builtin_popcount(s)<=k){idx[s]=vertex.size();vertex.push_back(s);}
  int n=vertex.size();vector<vector<int>> gr(n);
  for(int i=0;i<n;i++)for(int x=0;x<N;x++)if(idx[vertex[i]^(1<<x)]!=-1)gr[i].push_back(idx[vertex[i]^(1<<x)]);
  int comps=0,diam=0,rad=1e9;map<int,int> cmp_size,diam_comp,rad_comp,deg;
  for(auto &ar:gr)deg[ar.size()]++;
  vector<int> vis(n),cc(n,-1),d(n,0),seen(n,0),queue(n);
  int stamp=0;
  for(int v=0;v<n;v++)if(!vis[v]){
   vector<int> comp;int a=0,b=0;queue[b++]=v;vis[v]=1;
   while(a<b){int u=queue[a++];comp.push_back(u);for(int w:gr[u])if(!vis[w])vis[w]=1,queue[b++]=w;}
   int id=comps++;cmp_size[comp.size()]++;
   int dmax=0, rmin=1e9;
   for(int root:comp){
    int a=0,b=0;queue[b++]=root;seen[root]=++stamp;d[root]=0;
    int ecc=0;
    while(a<b){int u=queue[a++];ecc=max(ecc,d[u]);for(int w:gr[u])if(seen[w]!=stamp)seen[w]=stamp,d[w]=d[u]+1,queue[b++]=w;}
    if(b!=comp.size()){cerr<<"err";exit(1);}
    dmax=max(dmax,ecc);rmin=min(rmin,ecc);
   }
   diam=max(diam,dmax);rad=min(rad,rmin);diam_comp[dmax]++;rad_comp[rmin]++;
  }
  const int expected_n[]={21,245,1176,3138,5532};
  const int expected_m[]={0,210,2226,9674,23408};
  const int expected_comp[]={21,35,29,3,1};
  const int expected_diam[]={0,2,12,14,14};
  int m=accumulate(gr.begin(),gr.end(),0ll,[](long long s,const vector<int>&v){return s+v.size();})/2;
  if(n!=expected_n[k-4]||m!=expected_m[k-4]||comps!=expected_comp[k-4]||diam!=expected_diam[k-4]) {cerr<<"INCONSISTENT CLASSIFICATION";return 1;}
  if(k==4 && !(cmp_size.size()==1 && cmp_size[1]==21))return 2;
  if(k==5 && !(cmp_size[1]==14 && cmp_size[11]==21))return 3;
  if(k==6 && !(cmp_size[1]==28 && cmp_size[1148]==1 && rad_comp[10]==1))return 4;
  if(k==7 && !(cmp_size[1]==2 && cmp_size[3136]==1 && rad_comp[11]==1))return 5;
  if(k==8 && !(cmp_size[5532]==1 && rad_comp[12]==1))return 6;
  cerr<<"k="<<k<<" n="<<n<<" m="<<accumulate(gr.begin(),gr.end(),0ll,[](long long s,const vector<int>&v){return s+v.size();})/2<<" comp="<<comps<<" sizes ";
  for(auto [s,c]:cmp_size)cerr<<s<<":"<<c<<" ";cerr<<" dim_by_comp ";for(auto [s,c]:diam_comp)cerr<<s<<":"<<c<<" ";cerr<<" radius_by_comp ";for(auto [s,c]:rad_comp)cerr<<s<<":"<<c<<" ";cerr<<" minradius="<<rad<<" maxdiam="<<diam<<" degrees ";for(auto [s,c]:deg)cerr<<s<<":"<<c<<" ";cerr<<"\n";
 }
 cerr << "VERIFY_OK C++ independent graph and metrics" << "\n";
}
