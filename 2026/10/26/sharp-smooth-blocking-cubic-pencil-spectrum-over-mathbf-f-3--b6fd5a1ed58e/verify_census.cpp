#include <bits/stdc++.h>
using namespace std;
struct FF {
 int d,q;vector<int> mul,add;FF(int D):d(D),q(1){for(int i=0;i<d;i++)q*=3;mul.resize(q*q);add.resize(q*q);
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int x=a,y=b,z=0,p=1;for(int i=0;i<d;i++){z+=((x%3+y%3)%3)*p;x/=3;y/=3;p*=3;}add[a*q+b]=z;
   int A[3]={},B[3]={},C[5]={};x=a;y=b;for(int i=0;i<d;i++){A[i]=x%3;B[i]=y%3;x/=3;y/=3;}
   for(int i=0;i<d;i++)for(int j=0;j<d;j++)C[i+j]=(C[i+j]+A[i]*B[j])%3;
   for(int k=2*d-2;k>=d;k--) if(C[k]) {
     int v=C[k];
     if(d==2){ // u^2 + 1 =0, u^2=2
       C[k-2]=(C[k-2]+2*v)%3;
     }else { // u^3+2u+1=0 so u^3=u+2
       C[k-3]=(C[k-3]+2*v)%3;
       C[k-2]=(C[k-2]+v)%3;
     }
   }
   z=0;p=1;for(int i=0;i<d;i++){z+=C[i]*p;p*=3;}mul[a*q+b]=z;
  }
 }
 int plus(int a,int b)const{return add[a*q+b];}
 int times(int a,int b)const{return mul[a*q+b];}
 int power(int a,int n)const{int res=1;while(n){if(n&1)res=times(res,a);a=times(a,a);n>>=1;}return res;}
};
int ex[10][3]={{3,0,0},{2,1,0},{2,0,1},{1,2,0},{1,1,1},{1,0,2},{0,3,0},{0,2,1},{0,1,2},{0,0,3}};
struct Info {FF ff;int q;vector<array<int,40>> E; Info(int d):ff(d),q(ff.q){
  vector<array<int,3>> points;
  for(int y=0;y<q;y++)for(int z=0;z<q;z++)points.push_back({1,y,z});
  for(int z=0;z<q;z++)points.push_back({0,1,z});points.push_back({0,0,1});
  for(auto v:points){array<int,40> e={};
   for(int i=0;i<10;i++){
    int mon=1;for(int j=0;j<3;j++)mon=ff.times(mon,ff.power(v[j],ex[i][j]));e[i]=mon;
    for(int j=0;j<3;j++)if(ex[i][j]%3){int der=ex[i][j]%3;
      for(int k=0;k<3;k++)der=ff.times(der,ff.power(v[k],ex[i][k]-(j==k)));
      e[10+j*10+i]=der;
    }
   }
   E.push_back(e);
  }
 }
 bool nonsing(const array<int,10>& c)const {
  for(const auto&e:E){bool bad=true;
   for(int j=0;j<4;j++){
    int s=0;for(int i=0;i<10;i++)if(c[i])s=ff.plus(s,ff.times(c[i],e[j*10+i]));
    if(s){bad=false;break;}
   }
   if(bad)return false;
  }
  return true;
 }
};
int main(){
 array<int,10> F={2,0,2,0,0,1,0,1,0,0};
 vector<Info> inf; for(int d=1;d<=3;d++){inf.emplace_back(d);cout<<"GF"<<inf.back().q<<" points="<<inf.back().E.size()<<" F-smooth="<<inf.back().nonsing(F)<<"\n";}
 vector<int> Bi;
 for(size_t j=0;j<inf[0].E.size();j++){
  auto&e=inf[0].E[j];int v=0;for(int i=0;i<10;i++)v=(v+F[i]*e[i])%3;
  if(v==0)Bi.push_back((int)j);
 }
 cout<<"F rational points="<<Bi.size()<<"\n";
 int basefree=0,smoothG=0,smoothAll=0,blockG=0,blockAll=0; map<tuple<int,int,int>,int> dist;
 vector<array<int,10>> goodies;
 for(int x=0;x<6561;x++){
  array<int,10> G={};G[9]=1;int t=x;for(int i=1;i<9;i++){G[i]=t%3;t/=3;}
  bool ok=true;for(int j:Bi){auto&e=inf[0].E[j];int v=0;for(int i=0;i<10;i++)v=(v+G[i]*e[i])%3;if(!v){ok=false;break;}}
  if(!ok)continue;
  basefree++;
  array<int,10> H=G,J=G;
  for(int i=0;i<10;i++){H[i]=(G[i]+F[i])%3;J[i]=(G[i]+2*F[i])%3;}
  auto smooth=[&](const array<int,10>&c){for(const auto& f:inf)if(!f.nonsing(c))return false;return true;};
  if(!smooth(G))continue; smoothG++;
  if(!smooth(H)||!smooth(J))continue;smoothAll++;goodies.push_back(G);
  auto points=[&](const array<int,10>&c){int k=0;for(const auto&e:inf[0].E){int v=0;for(int i=0;i<10;i++)v=(v+c[i]*e[i])%3;if(v==0)k++;}return k;};
  array<int,3> counts={points(G),points(H),points(J)}; sort(counts.begin(),counts.end());dist[tuple<int,int,int>(counts[0],counts[1],counts[2])]++;

 }
 cout<<"basefree="<<basefree<<" Gsmooth="<<smoothG<<" all_smooth="<<smoothAll<<"\n";
 for(auto [tr,n]:dist)cout<<"profile "<<get<0>(tr)<<","<<get<1>(tr)<<","<<get<2>(tr)<<": "<<n<<"\n";
 ofstream out("pencils_recomputed.txt");for(auto g:goodies){for(int a:g)out<<a;out<<"\n";}
 cout<<"first example: ";for(int a:goodies[0])cout<<a;cout<<"\n";

 // Independent global census of cubic equation classes and orbit of the fixed blocking cubic.
 vector<array<int,3>> pp;
 for(int y=0;y<3;y++)for(int z=0;z<3;z++)pp.push_back({1,y,z});
 for(int z=0;z<3;z++)pp.push_back({0,1,z});pp.push_back({0,0,1});
 map<array<int,3>,int> pidx;for(int i=0;i<13;i++)pidx[pp[i]]=i;
 auto sigc=[&](const array<int,10>& c){string ss;
  for(const auto&e:inf[0].E){int v=0;for(int i=0;i<10;i++)v=(v+c[i]*e[i])%3;ss.push_back(char('0'+v));}
  size_t ix=ss.find_first_not_of('0');if(ix!=string::npos && ss[ix]=='2')for(auto&c:ss)if(c!='0')c=(c=='1'?'2':'1');
  return ss;};
 array<int,13> FM={};for(int i=0;i<13;i++){auto&e=inf[0].E[i];for(int j=0;j<10;j++)FM[i]=(FM[i]+F[j]*e[j])%3;}
 set<string> projectiveOrbit;
 for(int n=0;n<19683;n++){
  int t=n;int m[9];for(int i=0;i<9;i++){m[i]=t%3;t/=3;}
  int values[13];bool used[13]={},invertible=true;
  for(int j=0;j<13;j++){
   array<int,3> u{};for(int a=0;a<3;a++)for(int b=0;b<3;b++)u[a]=(u[a]+m[3*a+b]*pp[j][b])%3;
   if(u==array<int,3>{0,0,0}){invertible=false;break;}
   int alpha=find_if(u.begin(),u.end(),[](int v){return v!=0;})-u.begin();
   int inv=u[alpha];for(int a=0;a<3;a++)u[a]=u[a]*inv%3;
   int k=pidx.at(u);if(used[k]){invertible=false;break;}used[k]=true;
   values[j]=(FM[k]*inv)%3;
  }
  if(!invertible)continue;
  string vv;for(int i:values)vv.push_back(char('0'+i));
  size_t ix=vv.find_first_not_of('0');if(ix!=string::npos && vv[ix]=='2')for(auto&c:vv)if(c!='0')c=(c=='1'?'2':'1');
  projectiveOrbit.insert(vv);
 }
 cout<<"projective_orbit="<<projectiveOrbit.size()<<"\n";
 vector<int> lineMasks;for(const auto&a:pp){int mask=0;for(int i=0;i<13;i++)if((a[0]*pp[i][0]+a[1]*pp[i][1]+a[2]*pp[i][2])%3==0)mask|=(1<<i);lineMasks.push_back(mask);}
 int blocking=0,smoothblocking=0,outsiders=0;
 map<int,int> blockedPointCount;
 for(int n=1;n<59049;n++){
  int t=n;array<int,10> c={};for(int i=0;i<10;i++){c[i]=t%3;t/=3;}
  auto it=find_if(c.begin(),c.end(),[](int v){return v!=0;});if(*it!=1)continue;
  int mask=0;for(int i=0;i<13;i++){
   int v=0;auto&e=inf[0].E[i];for(int j=0;j<10;j++)v=(v+c[j]*e[j])%3;
   if(!v)mask|=(1<<i);
  }
  bool block=true;for(int l:lineMasks)if(!(l&mask)){block=false;break;}
  if(!block)continue;blocking++;
  if(!inf[0].nonsing(c)||!inf[1].nonsing(c)||!inf[2].nonsing(c))continue;
  smoothblocking++;blockedPointCount[__builtin_popcount((unsigned)mask)]++;
  if(!projectiveOrbit.count(sigc(c))) outsiders++;
 }
 cout<<"blocking_projective_cubics="<<blocking<<" smooth_blocking="<<smoothblocking<<" outsiders="<<outsiders<<"\n";
 for(auto [k,v]:blockedPointCount)cout<<"smooth_blocking_with_"<<k<<"_points="<<v<<"\n";
 if(basefree!=864 || smoothG!=576 || smoothAll!=312 || (int)projectiveOrbit.size()!=936 || blocking!=4940 || smoothblocking!=936 || outsiders!=0) return 1;
 if(dist[make_tuple(1,1,5)]!=24 || dist[make_tuple(1,2,4)]!=132 || dist[make_tuple(1,3,3)]!=42 || dist[make_tuple(2,2,3)]!=114) return 2;
 cout<<"VERIFY_CENSUS_OK\n";

}
