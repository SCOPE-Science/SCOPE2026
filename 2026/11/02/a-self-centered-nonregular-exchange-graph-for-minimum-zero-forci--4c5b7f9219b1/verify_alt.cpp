#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
int main(){
 const int N=16, ALL=(1<<N)-1;
 array<int,16> nbr{};
 for(int a=0;a<16;++a)for(int b=0;b<4;++b) nbr[a] |= 1<<(a^(1<<b));
 auto forces=[&](int mask)->int {
  int d=0;
  for(;d<16;++d){
   if(mask==ALL) return d;
   bool progressed=false;
   for(int a=0;a<16 && !progressed;++a){
    if(!(mask&(1<<a)))continue;
    int whites=nbr[a]&(~mask)&ALL;
    if(whites && !(whites&(whites-1))){mask|=whites;progressed=true;}
   }
   if(!progressed)return -1;
  }
  return mask==ALL ? d:-1;
 };
 int smaller=0;
 for(int m=0;m<(1<<16);++m)if(__builtin_popcount((unsigned)m)==7 && forces(m)>=0)++smaller;
 vector<int> verts;
 for(int m=0;m<(1<<16);++m)if(__builtin_popcount((unsigned)m)==8 && forces(m)>=0)verts.push_back(m);
 cout<<"FORCING_COUNTS min7="<<smaller<<" min8="<<verts.size()<<"\n";
 if(smaller||verts.size()!=2360)return 1;
 map<int,int> propagation;
 for(int state:verts){
  int mask=state,rounds=0;
  for(;mask!=ALL;++rounds){
   int newbits=0;
   for(int u=0;u<16;++u){
    if(!(mask&(1<<u)))continue;
    int white=nbr[u]&(~mask)&ALL;
    if(__builtin_popcount((unsigned)white)==1)newbits|=white;
   }
   if(newbits==0)return 10;
   mask|=newbits;
  }
  ++propagation[rounds];
 }
 cout<<"PROPAGATION";for(auto [a,b]:propagation)cout<<" "<<a<<":"<<b;cout<<"\n";
 if(propagation!=map<int,int>{{1,8},{2,816},{3,1152},{4,384}})return 11;
 vector<int> ix(1<<16,-1);for(int i=0;i<(int)verts.size();++i)ix[verts[i]]=i;
 for(int x:verts)if(ix[ALL^x]<0)return 12;
 cout<<"COMPLEMENT_CLOSURE "<<verts.size()<<"\n";
 vector<vector<int>> g(verts.size()); map<int,int> degrees;
 for(int v=0;v<(int)verts.size();++v){
  int m=verts[v];
  for(int a=0;a<16;++a)if(m&(1<<a))
    for(int b=0;b<16;++b)if(!(m&(1<<b))){int t=m ^ (1<<a) ^ (1<<b);
     if(ix[t]>=0) g[v].push_back(ix[t]);
    }
  sort(g[v].begin(),g[v].end());
  if(unique(g[v].begin(),g[v].end())!=g[v].end())return 3;
  degrees[g[v].size()]++;
 }
 long long m2=0;for(auto &a:g)m2+=a.size();
 cout<<"EDGES "<<m2/2<<" DEGREES";for(auto [a,b]:degrees)cout<<" "<<a<<":"<<b;cout<<"\n";
 if(m2!=45696)return 2;
 // Full all-source BFS, no use of symmetries for distance counts.
 vector<long long> all(12,0), excess(9,0);int mn=10000,mx=0,components=0;long long wi=0;
 for(int src=0;src<(int)verts.size();++src){
  vector<int> d(verts.size(),-1);deque<int> q;q.push_back(src);d[src]=0;
  while(!q.empty()){
   int v=q.front();q.pop_front();
   for(int w:g[v])if(d[w]<0){d[w]=d[v]+1;q.push_back(w);}
  }
  int e=0;
  for(int target=0;target<(int)verts.size();++target){int k=d[target];
   if(k<0){components++;continue;}
   e=max(e,k);if(k>=int(all.size()))return 4;
   all[k]++;wi+=k;
   int ambient=8-__builtin_popcount((unsigned)(verts[src]&verts[target]));
   int gap=k-ambient;
   if(gap<0 || gap>=int(excess.size()))return 8;
   excess[gap]++;
  }
  mn=min(mn,e);mx=max(mx,e);
 }
 cout<<"METRICS radius="<<mn<<" diameter="<<mx<<" unreachable="<<components<<" ordered_dist";
 for(int j=0;j<(int)all.size();++j)if(all[j])cout<<" "<<j<<":"<<all[j];
 cout<<" WIENER="<<wi/2<<"\n";
 cout<<"JOHNSON_EXCESS";for(int j=0;j<(int)excess.size();++j)if(excess[j])cout<<" "<<j<<":"<<excess[j];cout<<"\n";
 if(excess[0]!=5458192 || excess[1]!=105600 || excess[2]!=5808)return 9;
 if(components||mn!=8||mx!=8)return 5;
 // automorphism orbit count under coordinate permutations + xor shifts
 vector<array<int,16>> aut;
 array<int,4> perm{0,1,2,3};do{
  for(int t=0;t<16;++t){array<int,16> p{};for(int i=0;i<16;++i){int x=t;for(int j=0;j<4;++j)if(i&(1<<j))x^=(1<<perm[j]);p[i]=x;}aut.push_back(p);}
 }while(next_permutation(perm.begin(),perm.end()));
 vector<char> visited(1<<16,0);map<int,int> orb;
 for(int s:verts){if(visited[s])continue;set<int> imgs;
  for(auto &p:aut){int im=0;for(int i=0;i<16;++i)if(s&(1<<i))im|=1<<p[i];imgs.insert(im);}
  for(int m:imgs){if(ix[m]<0)return 6;visited[m]=1;}
  orb[imgs.size()]++;
 }
 cout<<"ORBITS";for(auto [a,b]:orb)cout<<" "<<a<<":"<<b;cout<<"\n";
 if(orb.size()!=5||orb[8]!=1||orb[48]!=1||orb[96]!=2||orb[192]!=3||orb[384]!=4)return 7;
 cout<<"INDEPENDENT_CERTIFICATE_PASS\n";
}
