// Geometric smoothness criterion: Jacobian quadrics generate every quartic.
#include <bits/stdc++.h>
using namespace std;
int mul(int a,int b){int v=0;for(int i=0;i<2;i++)if(b>>i&1)v ^= a<<i;if(v&8)v^=12;if(v&4)v^=7;return v;}
int monomial_index(int d,int x,int y,int z){int k=0;for(int i=d;i>=0;i--)for(int j=d-i;j>=0;j--)if(i==x&&j==y&&d-i-j==z)return k++;else k++;return -1;}
int main(){int ex[10][3],e2[6][3],e4[15][3],k=0;for(int i=3;i>=0;i--)for(int j=3-i;j>=0;j--){ex[k][0]=i;ex[k][1]=j;ex[k++][2]=3-i-j;}k=0;for(int i=2;i>=0;i--)for(int j=2-i;j>=0;j--){e2[k][0]=i;e2[k][1]=j;e2[k++][2]=2-i-j;}k=0;for(int i=4;i>=0;i--)for(int j=4-i;j>=0;j--){e4[k][0]=i;e4[k][1]=j;e4[k++][2]=4-i-j;}
 int ct=0,smooth=0;map<int,int> dist;vector<uint32_t> good;ifstream fin("tangent_codes.txt");uint32_t code;while(fin>>code){ct++;uint32_t t=code;int co[10];for(int i=0;i<10;i++){co[i]=t&3;t>>=2;}
  int der[3][6]={};for(int m=0;m<10;m++)for(int v=0;v<3;v++)if(ex[m][v]&1){int x=ex[m][0]-(v==0),y=ex[m][1]-(v==1),z=ex[m][2]-(v==2);int i=monomial_index(2,x,y,z);der[v][i]^=co[m];}
  int rows[18][15]={};for(int v=0;v<3;v++)for(int u=0;u<6;u++)for(int j=0;j<6;j++)if(der[v][j]){int x=e2[u][0]+e2[j][0],y=e2[u][1]+e2[j][1],z=e2[u][2]+e2[j][2];rows[6*v+u][monomial_index(4,x,y,z)]^=der[v][j];}
  int rank=0;for(int col=0;col<15;col++){int pivot=-1;for(int i=rank;i<18;i++)if(rows[i][col]){pivot=i;break;}if(pivot<0)continue;for(int j=0;j<15;j++)swap(rows[rank][j],rows[pivot][j]);int inv=(rows[rank][col]==1?1:(rows[rank][col]==2?3:2));for(int j=col;j<15;j++)rows[rank][j]=mul(rows[rank][j],inv);for(int i=0;i<18;i++)if(i!=rank&&rows[i][col]){int a=rows[i][col];for(int j=col;j<15;j++)rows[i][j]^=mul(a,rows[rank][j]);}rank++;}
  dist[rank]++;if(rank==15){smooth++;good.push_back(code);}
 }
 cout<<"tested "<<ct<<" smooth "<<smooth<<" rank distrib ";for(auto [a,b]:dist)cout<<a<<":"<<b<<" ";cout<<"\n";ofstream f("smooth_codes.txt");for(auto x:good)f<<x<<"\n";
}
