#include <bits/stdc++.h>
using namespace std;static inline int md(int x){x%=5;return x<0?x+5:x;}
int main(){
 vector<array<int,3>> mon;for(int a=0;a<=4;a++)for(int b=0;b<=4-a;b++)mon.push_back({a,b,4-a-b});
 int powers[5][5];for(int x=0;x<5;x++){powers[x][0]=1;for(int e=1;e<=4;e++)powers[x][e]=powers[x][e-1]*x%5;}
 int A[6][6][2][15]={};int xs[6]={1,1,1,1,1,0},ys[6]={0,1,2,3,4,1};
 for(int d=0;d<6;d++)for(int z=0;z<6;z++)for(int j=0;j<15;j++){
 auto[a,b,c]=mon[j];if(z<5){A[d][z][0][j]=powers[xs[d]][a]*powers[ys[d]][b]%5*powers[z][c]%5;A[d][z][1][j]=c?powers[xs[d]][a]*powers[ys[d]][b]%5*c%5*powers[z][c-1]%5:0;}
 else{A[d][z][0][j]=(a==0&&b==0&&c==4);A[d][z][1][j]=(a==1&&b==0&&c==3)? xs[d]:((a==0&&b==1&&c==3)?ys[d]:0);}}
 vector<array<int,3>> pts;for(int y=0;y<5;y++)for(int z=0;z<5;z++)pts.push_back({1,y,z});for(int z=0;z<5;z++)pts.push_back({0,1,z});pts.push_back({0,0,1});
 int V[31][15],X[31][15],Y[31][15],Z[31][15];for(int i=0;i<31;i++)for(int j=0;j<15;j++){
 auto[a,b,c]=mon[j];auto[x,y,z]=pts[i];V[i][j]=powers[x][a]*powers[y][b]%5*powers[z][c]%5;
 X[i][j]=a? a*powers[x][a-1]%5*powers[y][b]%5*powers[z][c]%5:0;
 Y[i][j]=b? b*powers[x][a]%5*powers[y][b-1]%5*powers[z][c]%5:0;
 Z[i][j]=c? c*powers[x][a]%5*powers[y][b]%5*powers[z][c-1]%5:0;}
 int minpts=100,minpts_p=100,total=0,onesmooth=0,roots[6];int ranks[16]={};
 for(int special=-1;special<6;special++){
  for(int tup=0;tup<15625;tup++){
   int t=tup;for(int i=0;i<6;i++){roots[i]=t%5;t/=5;}if(special>=0)roots[special]=5;
   if(special>=0&&tup>0){ // avoid duplicate ignored digit for special
      int base=1;for(int i=0;i<special;i++)base*=5;
      if((tup/base)%5!=0)continue;
   }
   int M[12][15]={};for(int d=0;d<6;d++)for(int r=0;r<2;r++)for(int j=0;j<15;j++)M[2*d+r][j]=A[d][roots[d]][r][j];
   int pivot[12],rank=0;for(int c=0;c<15;c++){
     int r=rank;while(r<12&&!M[r][c])r++;if(r==12)continue;
     for(int j=c;j<15;j++)swap(M[rank][j],M[r][j]);int inv=1;while(inv*M[rank][c]%5!=1)inv++;for(int j=c;j<15;j++)M[rank][j]=M[rank][j]*inv%5;
     for(int i=0;i<12;i++)if(i!=rank&&M[i][c]){int mul=M[i][c];for(int j=c;j<15;j++)M[i][j]=md(M[i][j]-mul*M[rank][j]);}
     pivot[rank]=c;rank++;if(rank==12)break;
   }
   ranks[rank]++;int ispv[15]={};for(int i=0;i<rank;i++)ispv[pivot[i]]=1;vector<int> fv;for(int i=0;i<15;i++)if(!ispv[i])fv.push_back(i);
   int numcases=1;for(auto f:fv)numcases*=5;
   for(int v=1;v<numcases;v++){
     int C[15]={};int rr=v;for(auto j:fv){C[j]=rr%5;rr/=5;}for(int i=rank-1;i>=0;i--){int q=0;for(auto j:fv)q=md(q-M[i][j]*C[j]);C[pivot[i]]=q;}
     int ptscount=0;bool nonsing=true;for(int p=0;p<31;p++){int f=0,fx=0,fy=0,fz=0;for(int j=0;j<15;j++){int cc=C[j];f+=cc*V[p][j];fx+=cc*X[p][j];fy+=cc*Y[p][j];fz+=cc*Z[p][j];}
       if(f%5==0){ptscount++;if(fx%5==0&&fy%5==0&&fz%5==0){nonsing=false;break;}}}
     if(!nonsing)continue;onesmooth++;
     if(ptscount<minpts){minpts=ptscount;cerr<<"NEW MIN "<<minpts<<" special "<<special<<" tup "<<tup<<" rank "<<rank<<"\n";cout<<"MIN "<<minpts<<" special "<<special<<" coeff";for(int j=0;j<15;j++)cout<<" "<<C[j];cout<<" roots";for(auto j:roots)cout<<" "<<j;cout<<"\n";cout.flush();}
     if(special>=0&&ptscount<minpts_p)minpts_p=ptscount;
   }
   total++;
  }
 }
 cerr<<"FINISHED total tuples "<<total<<" nonsing solutions "<<onesmooth<<" global minimum "<<minpts<<" special min "<<minpts_p<<" ranks ";for(int i=0;i<=15;i++)if(ranks[i])cerr<<i<<":"<<ranks[i]<<" ";cerr<<"\n";
}
