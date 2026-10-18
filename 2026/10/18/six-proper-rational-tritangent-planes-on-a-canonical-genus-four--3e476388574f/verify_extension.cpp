// Independent finite-extension replay for the quadric-cone section census.
// All arithmetic and coordinates are over F_2 or explicitly constructed F_{2^m}.
#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <cassert>
#include <algorithm>
using namespace std;
struct E {int x,y,z,w;};
vector<E> mons;
int polys[7]={0,3,7,11,19,37,67};
int mul(int a,int b,int m){int mod=polys[m],q=(1<<m),v=0;while(b){if(b&1)v^=a;b>>=1;a<<=1;if(a&q)a^=mod;}return v;}
int eval(const array<int,7>&c,int v,int m){int r=0;for(int i=6;i>=0;--i)r=mul(r,v,m)^c[i];return r;}
int pw(int x,int n,int m){int v=1;while(n){if(n&1)v=mul(v,x,m);x=mul(x,x,m);n>>=1;}return v;}
void chart(int mask,int which,array<int,7> coeff[3]){
 for(int t=0;t<3;t++)coeff[t].fill(0);
 for(int i=0;i<16;i++)if(mask>>i&1){auto z=mons[i];int deg=which==0?z.y+2*z.z:2*z.x+z.y;int w=z.w;if(w<3)coeff[w][deg]^=1;}
}
bool smoothext(int mask){
 if((mask&(1<<15))==0)return false;
 for(int which=0;which<2;which++){
  array<int,7> co[3];chart(mask,which,co);
  array<int,7> der[3];for(int k=0;k<3;k++){
   der[k].fill(0);for(int i=1;i<7;i+=2)der[k][i-1]=co[k][i];
  }
  for(int m=1;m<=6;m++)for(int t=0;t<(1<<m);t++){
   int a=eval(co[2],t,m),b=eval(co[1],t,m),c=eval(co[0],t,m);
   int w=b;for(int i=0;i<m-1;i++)w=mul(w,w,m);
   int f=mul(mul(w,w,m),w,m)^mul(a,mul(w,w,m),m)^mul(b,w,m)^c;
   int fy=mul(eval(der[2],t,m),mul(w,w,m),m)^mul(eval(der[1],t,m),w,m)^eval(der[0],t,m);
   int fw=mul(w,w,m)^b;
   if(!f&&!fy&&!fw)return false;
  }
 }
 return true;
}
// elementary geometric squarefreeness: no repeated zero in P^1(F_2).
bool sep(int c){
 for(auto pt:vector<pair<int,int>>{{1,0},{0,1},{1,1}}){
  int x=pt.first,y=pt.second;
  int f=(((c>>0)&1)&x)|0;
  // evaluate gradients of aX^3+bX^2Y+cXY^2+dY^3 by projective coordinates
  int dx=(((c>>0)&1)*x)^(((c>>2)&1)*y);
  int dy=(((c>>1)&1)*x)^(((c>>3)&1)*y);
  // actually derivatives are aX^2+cY^2 and bX^2+dY^2 (F2 coords)
  if(!dx&&!dy)return false;
 }
 return true;
}
int pntcount(int mask){int n=0;for(auto pr:vector<pair<int,int>>{{1,0},{0,1},{1,1}}){int x=pr.first,y=x*pr.second,z=pr.second;for(int w=0;w<2;w++){
 int f=0;for(int i=0;i<16;i++)if(mask>>i&1){auto e=mons[i];f^=(!e.x||x)&&(!e.y||y)&&(!e.z||z)&&(!e.w||w);}
 n+=1-f;
 }}return n;}
// General homogeneous binary forms represented by coefficient arrays in t-exponent.
vector<int> mulbin(const vector<int>&a,const vector<int>&b){vector<int>c(a.size()+b.size()-1,0);for(size_t i=0;i<a.size();i++)for(size_t j=0;j<b.size();j++)c[i+j]^=a[i]&b[j];return c;}
vector<int> powbin(vector<int>v,int n){vector<int>z{1};for(int i=0;i<n;i++)z=mulbin(z,v);return z;}
vector<int> section(int mask,int u,int v,int z){vector<int>total(7,0);
 for(int i=0;i<16;i++)if(mask>>i&1){auto ex=mons[i];auto p=mulbin(powbin({1,0,0},ex.x),powbin({0,1,0},ex.y));
 // use linear cone coordinates X=s²,Y=s*t,Z=t² on binary parameter, and W=u*s²+v*s*t+z*t²
 p=mulbin(powbin({1,0,0},ex.x),powbin({0,1,0},ex.y));p=mulbin(p,powbin({0,0,1},ex.z));p=mulbin(p,powbin({u,v,z},ex.w));
 for(size_t k=0;k<p.size();k++)total[k]^=p[k];
 }return total;}
int main(){
 for(int x=3;x>=0;x--)for(int y=3-x;y>=0;y--)for(int z=3-x-y;z>=0;z--){int w=3-x-y-z;if(!(x&&z))mons.push_back({x,y,z,w});}
 assert(mons.size()==16&&mons[15].w==3);
 array<long long,7> totals{};map<array<int,3>,int> joint;
 int smoothCount=0,large=0,maximum=0;
 for(int mask=(1<<15);mask<(1<<16);mask++)if(smoothext(mask)){
  int tcnt=0,scnt=0;
  for(auto pt:vector<pair<int,int>>{{1,0},{0,1},{1,1}}){int s=pt.first,t=pt.second;int bin=0;
   for(int i=0;i<16;i++)if(mask>>i&1){auto e=mons[i];int x=s,y=s*t,z=t;
    if((!e.x||x)&&(!e.y||y)&&(!e.z||z))bin^=1<<e.w;
   }
   tcnt+=sep(bin);
  }
  for(int u=0;u<2;u++)for(int v=0;v<2;v++)for(int z=0;z<2;z++){
   auto sextic=section(mask,u,v,z);int h=0;
   for(int j=0;j<=6;j++){if(j&1){if(sextic[j]){h=-1;break;}}else if(sextic[j])h|=1<<(j/2);}
   if(h>=0&&sep(h))scnt++;
  }
  int n=pntcount(mask);
  joint[{n,tcnt,scnt}]++;totals[tcnt+scnt]++;smoothCount++;maximum=max(maximum,tcnt+scnt);
 }
 cout<<"smooth="<<smoothCount<<" maximum="<<maximum<<" distribution=";for(int i=0;i<7;i++)cout<<i<<":"<<totals[i]<<",";cout<<"\n";
 for(auto [key,val]:joint)cout<<key[0]<<" "<<key[1]<<" "<<key[2]<<" "<<val<<"\n";
}
