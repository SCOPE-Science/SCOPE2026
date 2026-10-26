#include <bits/stdc++.h>
using namespace std;
const int pol[10]={0,3,7,11,19,37,67,131,283,529};
const int P[37][2]={{152,293},{152,310},{152,323},{152,329},{152,337},{152,355},{152,361},{152,567},{152,599},{154,295},{154,339},{154,355},{154,361},{154,535},{154,551},{154,564},{154,599},{154,611},{155,293},{155,355},{155,549},{155,551},{155,564},{155,583},{155,609},{155,610},{169,276},{169,279},{169,348},{169,551},{169,583},{169,599},{173,537},{173,599},{173,622},{194,345},{194,347}};
static inline int Fval(int F,int y,int z, const vector<vector<uint16_t>>& m,const vector<int>& sq,const vector<int>& cub) {
 int res=0;
 if(F&1)res ^=cub[z];
 if(F&2)res ^=m[y][sq[z]];
 if(F&4)res ^=m[sq[y]][z];
 if(F&8)res ^=cub[y];
 if(F&16)res ^=sq[z];
 if(F&32)res ^=m[y][z];
 if(F&64)res ^=sq[y];
 if(F&128)res ^=z;
 if(F&256)res ^=y;
 if(F&512)res ^=1;
 return res;
}
int main(){
 long C[37][10]={};
 for(int d=1;d<=9;d++){
  int q=1<<d,irr=pol[d];
  vector<vector<uint16_t>> m(q,vector<uint16_t>(q,0));
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
    int x=a,y=b,r=0;
    while(y){if(y&1)r^=x; y>>=1;x<<=1;if(x&q)x^=irr;}
    m[a][b]=r;
  }
  vector<int> sq(q),cub(q);for(int a=0;a<q;a++){sq[a]=m[a][a];cub[a]=m[sq[a]][a];}
  for(int rep=0;rep<37;rep++){
    int F=P[rep][0],G=P[rep][1];int count=0;
    for(int y=0;y<q;y++)for(int z=0;z<q;z++)if(Fval(F,y,z,m,sq,cub)==0 && Fval(G,y,z,m,sq,cub)==0)count++;
    for(int z=0;z<q;z++) {
      int f= ((F&1)?cub[z]:0)^((F&2)?sq[z]:0)^((F&4)?z:0)^((F&8)?1:0);
      int g= ((G&1)?cub[z]:0)^((G&2)?sq[z]:0)^((G&4)?z:0)^((G&8)?1:0);
      if(f==0 && g==0)count++;
    }
    if(!(F&1) && !(G&1))count++;
    C[rep][d]=count;
  }
 }
 for(int rep=0;rep<37;rep++){
  cout<<"rep "<<P[rep][0]<<","<<P[rep][1]<<" B(d)=";
  for(int d=1;d<=9;d++)cout<<C[rep][d]<<(d==9?" ":",");
  int nn[10]={};int total=0;
  for(int d=1;d<=9;d++){
    long rest=C[rep][d];for(int k=1;k<d;k++)if(d%k==0)rest-=k*nn[k];
    if(rest%d!=0){cerr<<"bad divisor"<<endl;return 1;}
    nn[d]=rest/d;
    total+=d*nn[d];
  }
  cout<<"closed=";
  for(int d=1;d<=9;d++)if(nn[d])cout<<d<<"^"<<nn[d]<<" ";
  cout<<" degree_sum="<<total<<"\n";
 }
}
