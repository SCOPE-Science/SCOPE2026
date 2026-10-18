#include <bits/stdc++.h>
using namespace std;
const int POW3[10]={1,3,9,27,81,243,729,2187,6561,19683};
int main(int argc,char**argv){
 if(argc<2){cerr<<"need independent smooth code file\n";return 1;}
 bool good[19683]={};ifstream in(argv[1]);int x;int n=0;while(in>>x){good[x]=true;n++;}cerr<<"smooth from algebraic Jacobian checks "<<n<<"\n";
 // eval at P1(F3)^2; basis order first factor [u^2,uv,v^2], second likewise
 int A[4][3]={{1,0,0},{0,0,1},{1,1,1},{1,2,1}};
 unsigned short zeros[19683]={};
 for(int code=1;code<19683;code++)if(good[code]){
  int c[9];int tmp=code;for(int k=0;k<9;k++){c[k]=tmp%3;tmp/=3;}
  for(int i=0;i<4;i++)for(int j=0;j<4;j++){
   int val=0;for(int h=0;h<3;h++)for(int v=0;v<3;v++)val+=c[3*h+v]*A[i][h]*A[j][v];
   if(val%3==0)zeros[code]|=uint16_t(1)<<(i*4+j);
  }
 }
 long long hist[17]={};long long total=0;int bestF=-1,bestG=-1;int bestWeight=100;
 for(int i=0;i<8;i++)for(int j=i+1;j<9;j++){
  int colsF[8],colsG[8],nf=0,ng=0;
  for(int z=i+1;z<9;z++)if(z!=j)colsF[nf++]=z;
  for(int z=j+1;z<9;z++)colsG[ng++]=z;
  int df=POW3[nf],dg=POW3[ng];
  for(int aa=0;aa<df;aa++){
   int f=POW3[i];int yy=aa;for(int z=0;z<nf;z++){f+=(yy%3)*POW3[colsF[z]];yy/=3;}
   if(!good[f])continue;
   for(int bb=0;bb<dg;bb++){
    int g=POW3[j], zz=bb;
    for(int z=0;z<ng;z++){g+=(zz%3)*POW3[colsG[z]];zz/=3;}
    if(!good[g])continue;
    int zf=f,zg=g,fpg=0,fmg=0;
    for(int z=0;z<9;z++){
     int a=zf%3,b=zg%3;zf/=3;zg/=3;
     fpg+=((a+b)%3)*POW3[z];fmg+=((a+2*b)%3)*POW3[z];
    }
    if(!good[fpg]||!good[fmg])continue;
    int base=__builtin_popcount((unsigned)(zeros[f]&zeros[g]));hist[base]++;total++;
    if(base==3){int wt=0;int u=f,v=g;for(int z=0;z<9;z++){wt+=(u%3!=0)+(v%3!=0);u/=3;v/=3;}if(wt<bestWeight){bestWeight=wt;bestF=f;bestG=g;}}
   }
  }
 }
 cout<<"RREF all smooth pencils "<<total<<"\n";
 for(int k=0;k<17;k++)if(hist[k])cout<<"k "<<k<<" count "<<hist[k]<<"\n";
 cout<<"best extremal "<<bestF<<" "<<bestG<<" coefficient nonzeros "<<bestWeight<<"\n";
}
