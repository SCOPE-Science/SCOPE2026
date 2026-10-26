#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
using V=array<int,3>;
int mod3(int x){x%=3;if(x<0)x+=3;return x;}
V norm(V v){for(int z:v){if(z){if(z==2)for(int &x:v)x=mod3(2*x);break;}}return v;}
int dot(V a,V b){return mod3(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]);}
int main(){
 vector<V> vs;map<V,int> ids;
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++){
  V v=norm({a,b,c});if(v==V{0,0,0})continue;if(!ids.count(v)){ids[v]=vs.size();vs.push_back(v);}}
 assert(vs.size()==13);
 int dd[26][26]={};
 for(int i=0;i<26;i++)for(int j=0;j<26;j++){
  if(i==j)dd[i][j]=0;else if((i<13)==(j<13))dd[i][j]=2;else dd[i][j]=(dot(vs[i%13],vs[j%13])==0?1:3);
 }
 U edges[26]={}; for(int i=0;i<13;i++)for(int j=0;j<13;j++)if(dd[i][j+13]==1){edges[i]|=1u<<(j+13);edges[j+13]|=1u<<i;}
 for(int i=0;i<26;i++)assert(__builtin_popcount(edges[i])==4);
 vector<U> distinguish;
 for(int i=0;i<26;i++)for(int j=i+1;j<26;j++){
  U w=0;for(int k=0;k<26;k++)if(dd[i][k]!=dd[j][k])w|=1u<<k;
  distinguish.push_back(w);
 }
 vector<array<int,26>> gens;
 vector<array<array<int,3>,3>> mats={{{{0,1,0},{1,0,0},{0,0,1}}}, {{{1,1,0},{0,1,0},{0,0,1}}},{{{2,0,0},{0,1,0},{0,0,1}}},{{{0,1,0},{0,0,1},{1,0,0}}}};

 for(auto M:mats){
  array<int,26> per{};
  for(int i=0;i<13;i++){
   V v=vs[i],o{};for(int a=0;a<3;a++)for(int b=0;b<3;b++)o[a]=mod3(o[a]+M[a][b]*v[b]);
   o=norm(o);per[i]=ids.at(o);
  }
  for(int j=0;j<13;j++){
   U transp=0;for(int i=0;i<13;i++)if(dot(vs[i],vs[j])==0)transp|=1u<<per[i];
   int jj=-1;
   for(int k=0;k<13;k++){
    U in=0;for(int i=0;i<13;i++)if(dot(vs[i],vs[k])==0)in|=1u<<i;
    if(in==transp){jj=k;break;}
   }
   assert(jj>=0);per[j+13]=jj+13;
  }
  gens.push_back(per);
 }
 array<int,26> dual;for(int i=0;i<13;i++){dual[i]=i+13;dual[i+13]=i;}gens.push_back(dual);
 for(auto per:gens)for(int i=0;i<26;i++)for(int j=0;j<26;j++)assert(dd[i][j]==dd[per[i]][per[j]]);

 string identity(26,'\0');for(int k=0;k<26;k++)identity[k]=char(k);
 unordered_set<string> group;group.reserve(16000);group.insert(identity);
 vector<string> elements{identity};
 for(size_t h=0;h<elements.size();h++)for(const auto &g:gens){
  string z(26,'\0');for(int j=0;j<26;j++)z[j]=elements[h][g[j]];
  if(group.insert(z).second)elements.push_back(z);
 }
 assert(elements.size()==11232);
 cout<<"automorphism subgroup size "<<elements.size()<<"\n";
 auto transform=[](U x,const array<int,26>& per){U y=0;while(x){int a=__builtin_ctz(x);x&=x-1;y|=1u<<per[a];}return y;};

 U seven_count=0;
 for(U x=(1u<<7)-1;x<(1u<<26);){
  bool ok=true;for(U w:distinguish)if(!(x&w)){ok=false;break;}
  if(ok)seven_count++;
  U low=x&-x,t=x+low;if(t>=1u<<26)break;x=t|(((t^x)/low)>>2);
 }
 assert(seven_count==0);
 cout<<"seven-landmark resolving sets "<<seven_count<<"\n";
 vector<U> bases;unordered_set<U> baseSet;
 int hist[14]={};
 auto st=chrono::steady_clock::now();
 for(U x=(1u<<8)-1; x < (1u<<26);){
  bool ok=true;
  for(U w:distinguish)if(!(x&w)){ok=false;break;}
  if(ok){bases.push_back(x);baseSet.insert(x);hist[__builtin_popcount(x&((1u<<13)-1))]++;}
  U low=x&-x,t=x+low; if(t>=1u<<26)break;x=t|(((t^x)/low)>>2);
 }
 cout << "bases " << bases.size()<<" elapsed " << chrono::duration<double>(chrono::steady_clock::now()-st).count()<<"s\n";
 for(int i=0;i<14;i++)if(hist[i])cout<<"points "<<i<<" count "<<hist[i]<<"\n";
 map<tuple<int,int,int>,int> counts;
 vector<vector<U>> orbits;
 unordered_set<U> seen;seen.reserve(bases.size()*2);
 for(U m:bases){
  if(seen.count(m))continue;
  vector<U> orb{m};seen.insert(m);
  for(size_t h=0;h<orb.size();h++)for(auto &p:gens){U z=transform(orb[h],p);assert(baseSet.count(z));if(seen.insert(z).second)orb.push_back(z);}
  int minp=26, maxp=0;for(U y:orb){int np=__builtin_popcount(y&((1u<<13)-1));minp=min(minp,np);maxp=max(maxp,np);}
  counts[{(int)orb.size(),minp,maxp}]++;
  orbits.push_back(move(orb));
 }
 cout<<"orbits "<<orbits.size()<<" size_minP_maxP:\n";
 for(auto [key,c]:counts){auto [size,mi,ma]=key;cout<<size<<" "<<mi<<" "<<ma<<" "<<c<<"\n";}

 cout<<"orbit classes (size, incidence edges, sorted point degrees, sorted line degrees, 3collinear, 3concurrent, representatives):\n";
 for(const auto &orb:orbits){
  U m=*min_element(orb.begin(),orb.end());vector<int> ps,ls,pdeg,ldeg;
  for(int i=0;i<13;i++){if((m>>i)&1)ps.push_back(i);if((m>>(i+13))&1)ls.push_back(i);}
  for(int i:ps){int d=0;for(int j:ls)if(dot(vs[i],vs[j])==0)d++;pdeg.push_back(d);}
  for(int j:ls){int d=0;for(int i:ps)if(dot(vs[i],vs[j])==0)d++;ldeg.push_back(d);}
  sort(pdeg.begin(),pdeg.end());sort(ldeg.begin(),ldeg.end());
  int tp=0,tl=0;
  for(int a=0;a<4;a++)for(int b=a+1;b<4;b++)for(int c=b+1;c<4;c++){
   for(int j=0;j<13;j++)if(dot(vs[ps[a]],vs[j])==0&&dot(vs[ps[b]],vs[j])==0&&dot(vs[ps[c]],vs[j])==0){tp++;break;}
   for(int i=0;i<13;i++)if(dot(vs[i],vs[ls[a]])==0&&dot(vs[i],vs[ls[b]])==0&&dot(vs[i],vs[ls[c]])==0){tl++;break;}
  }
  cout<<orb.size()<<" "<<accumulate(pdeg.begin(),pdeg.end(),0)<<" Pdeg";for(int x:pdeg)cout<<x;cout<<" Ldeg";for(int x:ldeg)cout<<x;
  cout<<" triples:"<<tp<<","<<tl<<" p:";for(int x:ps)cout<<" ("<<vs[x][0]<<vs[x][1]<<vs[x][2]<<")";
  cout<<" l:";for(int x:ls)cout<<" ("<<vs[x][0]<<vs[x][1]<<vs[x][2]<<")";cout<<"\n";
 }

 assert(bases.size()==9828);
 assert(orbits.size()==4);
 assert(counts[make_tuple(936,4,4)]==1 && counts[make_tuple(1404,4,4)]==1 && counts[make_tuple(1872,4,4)]==1 && counts[make_tuple(5616,4,4)]==1);
 cout<<"VERIFY_OK\n";
 cout<<"orbit listing (size, minimum point count, canonical hex set):\n";
 for(const auto &orb:orbits){U smallest=*min_element(orb.begin(),orb.end());int minp=26,maxp=0;for(auto x:orb){int k=__builtin_popcount(x&((1u<<13)-1));minp=min(minp,k);maxp=max(maxp,k);}cout<<orb.size()<<" "<<minp<<":"<<maxp<<" "<<hex<<smallest<<dec<<"\n";}
}
