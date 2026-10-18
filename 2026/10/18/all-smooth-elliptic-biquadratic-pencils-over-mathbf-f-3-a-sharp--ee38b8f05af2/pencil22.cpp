#include <bits/stdc++.h>
using namespace std;
using I=int;
struct Form{array<int,9> c; uint16_t pointmask; int N; int code;};
array<int,9> decode(int m){array<int,9> c;for(int i=0;i<9;i++){c[i]=m%3;m/=3;}return c;}
int encode(array<int,9> const &c){int a=0,m=1;for(int i=0;i<9;i++){a+=m*c[i];m*=3;}return a;}
int normalize(int m){auto a=decode(m); for(int t:a)if(t){if(t==2){for(int &v:a)v=(2*v)%3;}break;}return encode(a);}
int add(int a,int b,int k){auto x=decode(a),y=decode(b);for(int i=0;i<9;i++)x[i]=(x[i]+k*y[i])%3;return normalize(encode(x));}
int pmod(int a){a%=3;if(a<0)a+=3;return a;}
array<int,5> delta(array<int,9> const &f){
 // forms coefficient A/B/C in u^2,uv,v^2. A_j=f[0*3+j], B_j=f[1*3+j], C_j=f[2*3+j]
 array<int,5> h={};
 for(int i=0;i<3;i++)for(int j=0;j<3;j++){h[i+j]=pmod(h[i+j]+f[i*3+1]*f[j*3+1]-f[i*3+0]*f[j*3+2]);}
 return h;
}
using Poly=vector<int>;
void trim(Poly&v){while(!v.empty()&&!v.back())v.pop_back();}
Poly rem(Poly a, Poly b){trim(a);trim(b);if(b.empty())throw 1;int d=b.size()-1, inv=b[d];while((int)a.size()-1>=d){int coeff=a.back()*inv%3, shift=(int)a.size()-1-d;for(int j=0;j<=d;j++)a[j+shift]=pmod(a[j+shift]-coeff*b[j]);trim(a);}return a;}
bool smooth(array<int,9> const &f){
 auto h=delta(f); // homogeneous binary quartic, ordered u^(4-i)*v^i
 int lo=0,hi=4;
 while(lo<=4 && h[lo]==0)lo++;
 while(hi>=0 && h[hi]==0)hi--;
 if(lo>1 || hi<3)return false; // exclude double roots at v=0 and u=0
 Poly p(5-lo,0);
 for(int i=lo;i<=hi;i++)p[4-i]=h[i];
 trim(p);
 Poly dp(p.size()-1,0);
 for(int i=1;i<(int)p.size();i++)dp[i-1]=i*p[i]%3;
 trim(dp);
 if(dp.empty())return false;
 while(!dp.empty()){Poly r=rem(p,dp);p=dp;dp=r;}
 return p.size()==1; // affine polynomial squarefree
}
int eval(array<int,9> const&c,int X,int Y){ // X,Y each index0..3 points [1:0],[0:1],[1:1],[1:2]
 const int U[4]={1,0,1,1},V[4]={0,1,1,2};
 int a[3]={U[X]*U[X]%3,U[X]*V[X]%3,V[X]*V[X]%3};
 int b[3]={U[Y]*U[Y]%3,U[Y]*V[Y]%3,V[Y]*V[Y]%3};
 int z=0;for(int i=0;i<3;i++)for(int j=0;j<3;j++)z+=c[i*3+j]*a[i]*b[j];return z%3;
}
int main(){const int MM=19683;vector<uint8_t> good(MM,0);vector<Form> smooths;for(int m=1;m<MM;m++){int nm=normalize(m);if(m!=nm)continue;auto c=decode(m);if(!smooth(c))continue;good[m]=1;Form f{c,0,0,m};for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(!eval(c,i,j)){f.pointmask|=1<<(i*4+j);f.N++;}smooths.push_back(f);}
 cerr<<"smooths "<<smooths.size()<<"\n";
 long long hist[17]={},joint[17][8]={},pencils=0,pairs=0;
 map<array<int,4>,long long> nmult;
 for(int i=0;i<(int)smooths.size();i++)for(int j=i+1;j<(int)smooths.size();j++){
  int a=smooths[i].code,b=smooths[j].code;
  if(!good[add(a,b,1)] || !good[add(a,b,2)])continue;
  int k=__builtin_popcount((unsigned)(smooths[i].pointmask & smooths[j].pointmask));
  int codes[4]={a,b,add(a,b,1),add(a,b,2)};
  array<int,4> ns;
  for(int t=0;t<4;t++){
   int cm=codes[t]; // calculate N via direct eval
   auto c=decode(cm);int n=0;for(int x=0;x<4;x++)for(int y=0;y<4;y++)n+=eval(c,x,y)==0;ns[t]=n;
  }
  sort(ns.begin(),ns.end());nmult[ns]++;
  hist[k]++;joint[k][ns[0]]++;pairs++;
 }
 cout<<"forms "<<smooths.size()<<" pairs "<<pairs<<" pencils "<<pairs/6<<" remainder "<<pairs%6<<"\n";
 for(int k=0;k<17;k++)if(hist[k])cout<<"base "<<k<<" pairs "<<hist[k]<<" pencils "<<hist[k]/6<<"\n";
 for(auto [v,c]:nmult)cout<<"Ntuple "<<v[0]<<","<<v[1]<<","<<v[2]<<","<<v[3]<<" "<<c/6<<"\n";
}
