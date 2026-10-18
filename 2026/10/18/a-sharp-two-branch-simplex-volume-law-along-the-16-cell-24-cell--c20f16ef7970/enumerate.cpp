#include <bits/stdc++.h>
using namespace std;
using P=array<int,5>;
struct V {int a[4],b[4];};
int permS[24][4],permsign[24];
int main(){
 vector<V> v;
 for(int i=0;i<4;i++) for(int si:{-1,1}) for(int j=0;j<4;j++) if(i!=j)for(int sj:{-1,1}){
 V p={}; p.a[i]=si;p.b[i]=-si;p.b[j]=sj;v.push_back(p);
 }

 array<int,4> perm{0,1,2,3};int z=0;do{for(int k=0;k<4;k++)permS[z][k]=perm[k];int sign=1;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(perm[i]>perm[j])sign=-sign;permsign[z]=sign;z++;}while(next_permutation(perm.begin(),perm.end()));
 map<P,pair<int,array<int,4>>> counts;
 int inds[4];
 for(int a=1;a<45;a++)for(int b=a+1;b<46;b++)for(int c=b+1;c<47;c++)for(int d=c+1;d<48;d++){
   inds[0]=a;inds[1]=b;inds[2]=c;inds[3]=d;
   int mat[4][4][2];
   for(int i=0;i<4;i++)for(int j=0;j<4;j++){
    mat[i][j][0]=v[inds[i]].a[j]-v[0].a[j];
    mat[i][j][1]=v[inds[i]].b[j]-v[0].b[j];
   }
   P poly{};
   for(int p=0;p<24;p++){
     int coeff[5]={permsign[p],0,0,0,0};
     for(int i=0;i<4;i++){
       int lin0=mat[i][permS[p][i]][0],lin1=mat[i][permS[p][i]][1];
       for(int k=i+1;k>=0;k--){
         int x=(k<=i?coeff[k]:0),y=(k>=1?coeff[k-1]:0);
         coeff[k]= x*lin0 + y*lin1;
       }
     }
     for(int k=0;k<=4;k++)poly[k]+=coeff[k];
   }
     P negative;for(int k=0;k<=4;k++)negative[k]=-poly[k];
   if(negative<poly)poly=negative;
   if(!counts.count(poly))counts[poly]={0,{a,b,c,d}};
   counts[poly].first++;
 }
 ostream &f=cout;
 f<<"c0\tc1\tc2\tc3\tc4\tcount\ta\tb\tc\td\n";
 for(auto &e:counts){for(int k=0;k<5;k++)f<<e.first[k]<<"\t";f<<e.second.first;for(int ix:e.second.second)f<<"\t"<<ix;f<<"\n";}
}
