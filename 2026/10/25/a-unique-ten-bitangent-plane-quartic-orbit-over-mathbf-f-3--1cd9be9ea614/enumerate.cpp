#include <bits/stdc++.h>
using namespace std;
int R[13][5][15];bool squarebit[243];
int main(int argc,char**argv){
 ifstream fi("restrictions.dat");for(int l=0;l<13;l++)for(int k=0;k<5;k++)for(int j=0;j<15;j++)fi>>R[l][k][j];int m,c;fi>>m;for(int i=0;i<m;i++){fi>>c;squarebit[c]=1;}
 long counts[14]={};int top=0;long nTop=0;ofstream out("high_forms.tsv");
 // projective normalized coefficient vectors: leading nonzero value always 1
 for(int lead=0;lead<15;lead++){
  long N=1;for(int d=lead+1;d<15;d++)N*=3;
  int v[15]={};v[lead]=1;
  for(long index=0;index<N;index++){
   int z=index;for(int j=14;j>lead;j--){v[j]=z%3;z/=3;}
   int num=0;
   for(int l=0;l<13;l++){
    int code=0,base=1;
    for(int k=0;k<5;k++){
      int t=0;for(int j=lead;j<15;j++)t+=R[l][k][j]*v[j];
      code+=((t%3)*base);base*=3;
    }
    if(squarebit[code])num++;
   }
   counts[num]++;
   if(num>top){top=num;nTop=0;}
   if(num==top)nTop++; if(num>=8){for(int i=0;i<15;i++)out<<v[i];out<<" "<<num<<"\n";}
  }
 }
 for(int i=0;i<=13;i++)cout<<i<<" "<<counts[i]<<"\n";
 cout<<"TOP "<<top<<" "<<nTop<<"\n";
}
