#include <array>
#include <iostream>
#include <vector>
#include <functional>
#include <cstdint>
using namespace std;
using V=array<int,8>;
int mod3(int n){n%=3;return n<0?n+3:n;}
vector<array<int,3>> pts;
void init_pts(){
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
  int v[3]={x,y,z};int f=-1;
  for(int k=0;k<3;k++)if(v[k]){f=k;break;}
  if(f<0 || v[f]!=1)continue;
  pts.push_back({x,y,z});
 }
}
bool smooth(V a){
 // a00=0, a01 a02 a10 a11 a12 a20 a21 a22
 for(const auto& p:pts){
  int x=p[0],y=p[1],z=p[2];
  int X=mod3(a[0]*y+a[1]*z);
  int Y=mod3(a[2]*x+a[3]*y+a[4]*z);
  int Z=mod3(a[5]*x+a[6]*y+a[7]*z);
  if(mod3(y*Z-z*Y)==0 && mod3(z*X-x*Z)==0 && mod3(x*Y-y*X)==0)return false;
 }
 return true;
}
int main(){
 init_pts(); if(pts.size()!=13)return 3;
 long long total=0, good=0;
 for(int i=0;i<8;i++)for(int j=i+1;j<8;j++){
  V a{},b{};a[i]=1;b[j]=1;
  vector<pair<int,int>> free;
  for(int k=i+1;k<8;k++)if(k!=j)free.push_back({0,k});
  for(int k=j+1;k<8;k++)free.push_back({1,k});
  function<void(int)> rec=[&](int s){
   if(s==(int)free.size()){
    total++;
    V c{},d{};
    for(int k=0;k<8;k++){c[k]=mod3(a[k]+b[k]);d[k]=mod3(a[k]+2*b[k]);}
    if(smooth(a)&&smooth(b)&&smooth(c)&&smooth(d))good++;
    return;
   }
   auto [row,k]=free[s];
   for(int r=0;r<3;r++){
    if(row==0)a[k]=r;else b[k]=r;
    rec(s+1);
   }
  };
  rec(0);
 }
 cout<<"RREF two-spaces="<<total<<" all-smooth="<<good<<"\n";
 return !(total==896260 && good==2016);
}
