#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
struct Exp{array<int,4> a;};
vector<Exp> mons(int d){vector<Exp>v;for(int a=0;a<=d;a++)for(int b=0;b<=d-a;b++)for(int c=0;c<=d-a-b;c++){int e=d-a-b-c;v.push_back({{a,b,c,e}});}return v;}
int binom(int n,int k){ if(k<0||k>n)return 0;return ((k & ~n)==0);}
int main(){auto E=mons(3), Q=mons(2), H=mons(5); map<array<int,4>,int>I3,I5;
for(int i=0;i<20;i++)I3[E[i].a]=i;for(int i=0;i<56;i++)I5[H[i].a]=i;
vector<array<U,20>> masks(4);
for(int g=0;g<4;g++)for(int m=0;m<20;m++){
 auto v=E[m].a; U out=0;
 if(g<3){swap(v[g],v[g+1]);out=U(1)<<I3.at(v);}
 else { // substitution x0 -> x0+x1
  int p=v[0];for(int j=0;j<=p;j++)if(binom(p,j)){auto w=v; w[0]=j;w[1]+=p-j;out ^= U(1)<<I3.at(w);}
 }
 masks[g][m]=out;
 }
 vector<vector<U>> lo(4,vector<U>(65536)),hi(4,vector<U>(16));
 for(int g=0;g<4;g++){for(int s=1;s<65536;s++){int bit=__builtin_ctz((unsigned)s);lo[g][s]=lo[g][s&(s-1)]^masks[g][bit];}for(int s=1;s<16;s++){int bit=__builtin_ctz((unsigned)s);hi[g][s]=hi[g][s&(s-1)]^masks[g][16+bit];}}
 auto move=[&](U v,int g)->U{return lo[g][v&65535] ^hi[g][v>>16];};
 auto ev=[&](U mask,U pt)->int{int res=0;for(int k=0;k<20;k++)if((mask>>k)&1){bool val=true;for(int j=0;j<4;j++)if(E[k].a[j]&& !(pt>>j&1)){val=false;break;}res^=val;}return res;};
 auto pol=[&](U mask,U u,U v,int degree_u)->int{ // coefficient of s^degree_u * t^(3-degree_u) in F(su+tv)
 int out=0;for(int k=0;k<20;k++)if((mask>>k)&1){
  int poly[4]={1,0,0,0};int deg=0;
  for(int i=0;i<4;i++)for(int c=0;c<E[k].a[i];c++){
   int pnew[4]={};for(int a=0;a<=deg;a++)if(poly[a]){if((u>>i)&1)pnew[a+1]^=1;if((v>>i)&1)pnew[a]^=1;}
   ++deg;copy(pnew,pnew+4,poly);
  }
  out ^= poly[degree_u];
 }return out;};
 auto smooth=[&](U f)->bool{array<uint64_t,56> arr{}; array<uint64_t,56> arrhi{};
  for(int j=0;j<4;j++)for(int a=0;a<20;a++) {int col=j*20+a;auto base=E[a].a;
   for(int k=0;k<20;k++)if((f>>k&1) && (E[k].a[j]&1)){
    auto r=E[k].a;r[j]--;for(int n=0;n<4;n++)r[n]+=base[n];int row=I5.at(r);
    if(col<64)arr[row]^=uint64_t(1)<<col;else arrhi[row]^=uint64_t(1)<<(col-64);
   }
  }
  int rk=0;for(int col=79;col>=0;col--){int hit=-1;for(int r=rk;r<56;r++){bool x=col>=64 ? ((arrhi[r]>>(col-64))&1):((arr[r]>>col)&1);if(x){hit=r;break;}}
   if(hit<0)continue;swap(arr[hit],arr[rk]);swap(arrhi[hit],arrhi[rk]);
   for(int r=rk+1;r<56;r++)if(col>=64?((arrhi[r]>>(col-64))&1):((arr[r]>>col)&1)){arr[r]^=arr[rk];arrhi[r]^=arrhi[rk];}rk++;if(rk==56)break;
  }return rk==56;};
 vector<array<int,3>> lines;set<array<int,3>> used;
 for(int i=1;i<16;i++)for(int j=i+1;j<16;j++){array<int,3>line={i,j,i^j};sort(line.begin(),line.end());if(used.insert(line).second)lines.push_back(line);}
 assert(lines.size()==35);
 vector<unsigned char> done(1<<20);vector<U> queue;queue.reserve(30000);
 map<tuple<int,int,int,int>,pair<int,long long>> tally;
 ofstream table("cubic_surface_orbits.tsv");table<<"representative\torbit_size\tpoints\tlines\teckardt\tsmooth\n";
 vector<unsigned char> allsmooth(1<<20,0); int numOrbits=0,numSmoothOrbits=0;long long totalSmooth=0;
 for(U f=1;f<(1U<<20);f++)if(!done[f]){
  queue.clear();queue.push_back(f);done[f]=1;
  for(size_t k=0;k<queue.size();k++){U v=queue[k];for(int g=0;g<4;g++){U n=move(v,g);if(!done[n]){done[n]=1;queue.push_back(n);}}}
  numOrbits++;bool s=smooth(f);if(!s)continue;for(U v:queue)allsmooth[v]=1;numSmoothOrbits++;totalSmooth+=queue.size();
  int pts=0;for(int p=1;p<16;p++)pts+=!ev(f,p);
  int ls=0;vector<int> lin(16);
  for(auto L:lines){int u=L[0],v=L[1];if(!pol(f,u,v,3)&&!pol(f,u,v,2)&&!pol(f,u,v,1)&&!pol(f,u,v,0)){
   ls++;for(int p:L)lin[p]++;}}
  int eck=0;
  for(int p=1;p<16;p++)if(!ev(f,p)){
   // gradient in x_j = coefficient of s^2 t in F(s*p+t*e_j)
   int g[4];for(int j=0;j<4;j++)g[j]=pol(f,p,1<<j,2);
   vector<int>tang;for(int v=1;v<16;v++)if(v!=p){int dot=0;for(int j=0;j<4;j++)if(v>>j&1)dot^=g[j];if(!dot)tang.push_back(v);}
   if(tang.size()!=6){cerr<<"bad tangent plane";abort();}
   int u=tang[0],v=0;for(int x:tang)if(x!=u&&x!=(u^p)){v=x;break;}
   // quadratic terms in F(p+s*u+t*v): coefficient t^2, st, s^2 for p^1 variables.
   // cubic polarization: term F(s p + t u) coefficient s^1 t^2 etc.
   int aa=pol(f,p,u,1),bb=pol(f,p,v,1);
   // mixed st requires F(p+u+v) - F(p+u)-F(p+v)+F(p)+ cubic term F(u+v)-F(u)-F(v)
   // evaluate local polynomial at (1,1) then subtract linear (0) quadratic squares and cubic homogeneous terms
   int mixed=ev(f,p^u^v)^ev(f,p^u)^ev(f,p^v)^ev(f,p)^ev(f,u^v)^ev(f,u)^ev(f,v);
   if(!aa&&!bb&&!mixed)eck++;
  }
  tally[{pts,ls,eck,(int)queue.size()}].first++;
  tally[{pts,ls,eck,(int)queue.size()}].second+=queue.size();
  table<<f<<"\t"<<queue.size()<<"\t"<<pts<<"\t"<<ls<<"\t"<<eck<<"\t1\n";
 }
 ofstream b("cubic_surface_smooth.bin",ios::binary);b.write((char*)allsmooth.data(),allsmooth.size());b.close(); cout<<"orbits "<<numOrbits<<" smooth_orbits "<<numSmoothOrbits<<" smooth_equations "<<totalSmooth<<"\n";
 for(auto [key,v]:tally){auto[p,l,e,os]=key;cout<<p<<" "<<l<<" "<<e<<" "<<os<<" : "<<v.first<<" "<<v.second<<"\n";}
}
