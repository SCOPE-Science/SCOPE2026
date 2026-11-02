#include <iostream>
#include <array>
using namespace std;
int mod(int a,int q){a%=q;return a<0?a+q:a;}
int det(const int p[3][3],int q){return mod(p[0][0]*(p[1][1]*p[2][2]-p[1][2]*p[2][1])-p[0][1]*(p[1][0]*p[2][2]-p[1][2]*p[2][0])+p[0][2]*(p[1][0]*p[2][1]-p[1][1]*p[2][0]),q);}
int main(){for(int q:{2,3,5}){
  int m[3][3]={};if(q==2){for(int i=0;i<3;i++)m[i][(i+1)%3]=1;}else{for(int i=0;i<3;i++){m[i][i]=1;m[i][(i+1)%3]=1;}}
  int p[3][3];long long num=0, invertible=0;
  for(int a=0;a<q*q*q;a++)for(int b=0;b<q*q*q;b++)for(int c=0;c<q*q*q;c++){
    int v[3]={a,b,c};for(int col=0;col<3;col++){int w=v[col];for(int row=0;row<3;row++){p[row][col]=w%q;w/=q;}}
    if(det(p,q)==0)continue;invertible++;
    bool ok=true;
    for(int i=0;i<3&&ok;i++)for(int j=i;j<3&&ok;j++)for(int r=0;r<3;r++){
       int lhs=0,rhs=0;
       if(i==j){for(int k=0;k<3;k++)lhs+=m[i][k]*p[r][k];}
       for(int k=0;k<3;k++)rhs+=p[k][i]*p[k][j]*m[k][r];
       if(mod(lhs-rhs,q)!=0){ok=false;break;}
    }
    if(ok)num++;
  }
  cout<<"q="<<q<<" invertible="<<invertible<<" aut="<<num<<"\n";
  if(num!=3)return 1;
 }
 cout<<"VERIFY3_OK\n";
}
