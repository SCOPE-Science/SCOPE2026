#include <bits/stdc++.h>
using namespace std;
int md(int a){a%=5;return a<0?a+5:a;}
using V=array<int,6>;
int det(V a){int A=a[0],B=a[1],C=a[2],D=a[3],E=a[4],F=a[5];return md((2*A)*(2*B)*(2*C)+2*D*E*F-(2*A)*F*F-(2*B)*E*E-(2*C)*D*D);}
bool good(const array<V,2>&r){for(int t=0;t<5;t++){V a{};for(int j=0;j<6;j++)a[j]=md(r[0][j]+t*r[1][j]);if(det(a)==0)return false;}return det(r[1])!=0;}
int main(){long long count=0,goodcount=0;for(int p0=0;p0<6;p0++)for(int p1=p0+1;p1<6;p1++){array<V,2> r{};r[0][p0]=1;r[1][p1]=1;vector<pair<int,int>>slots;for(int i=0;i<2;i++)for(int j=0;j<6;j++)if(j>(i==0?p0:p1)&&j!=p0&&j!=p1)slots.push_back({i,j});int n=1;for(int i=0;i<slots.size();i++)n*=5;for(int k=0;k<n;k++){int z=k;for(auto [i,j]:slots){r[i][j]=z%5;z/=5;}count++;if(good(r))goodcount++;}}
cout<<"all_pencils "<<count<<" all_smooth_pencils "<<goodcount<<"\n";
}
