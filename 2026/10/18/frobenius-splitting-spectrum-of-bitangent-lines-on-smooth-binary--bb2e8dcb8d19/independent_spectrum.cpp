#include <bits/stdc++.h>
using namespace std;
using Vec=array<int,3>;
int Q=0,n=0,poly=0,mul_table[128][128];
int irr[8]={0,3,7,13,25,41,73,137};
void gf_init(int k){
 n=k;Q=1<<k;poly=irr[k];
 for(int a=0;a<Q;a++)for(int b=0;b<Q;b++){
  int aa=a,val=0;
  for(int j=0;j<n;j++){
   if((b>>j)&1)val^=aa;
   aa<<=1;
   if(aa&Q)aa^=poly;
  }
  mul_table[a][b]=val;
 }
}
using Pol=array<int,5>; // coeff of s^j t^(degree-j)
Pol power(Vec two,int exp){
 Pol f{};f[0]=1;int d=0;
 for(int t=0;t<exp;t++){
  Pol nxt{};
  for(int j=0;j<=d;j++){
   nxt[j]^=mul_table[f[j]][two[1]];
   nxt[j+1]^=mul_table[f[j]][two[0]];
  }
  f=nxt;d++;
 }
 return f;
}
Pol times(Pol a,Pol b,int da,int db){
 Pol z{};
 for(int i=0;i<=da;i++)for(int j=0;j<=db;j++)z[i+j]^=mul_table[a[i]][b[j]];
 return z;
}
vector<Vec> monomials(){
 vector<Vec> out;
 for(int i=4;i>=0;i--)for(int j=4-i;j>=0;j--)out.push_back({i,j,4-i-j});
 return out;
}
bool evencontact(int f,Vec P,Vec R,const vector<Vec>& exps){
 Pol px[3][5];
 for(int coord=0;coord<3;coord++)for(int d=0;d<=4;d++){
  px[coord][d]=power({P[coord],R[coord],0},d);
 }
 Pol c{};
 for(int j=0;j<15;j++) if((f>>j)&1){
  Vec v=exps[j];
  Pol tmp=times(px[0][v[0]],px[1][v[1]],v[0],v[1]);
  Pol tot=times(tmp,px[2][v[2]],v[0]+v[1],v[2]);
  for(int t=0;t<5;t++)c[t]^=tot[t];
 }
 return c[1]==0 && c[3]==0;
}
int main(){
 auto exps=monomials();
 ifstream fin("smooth_orbits.txt");
 vector<pair<int,int>> reps;int f,w;
 while(fin>>f>>w)reps.push_back({f,w});
 ofstream ofs("independent_fixed_counts.txt");
 for(auto [f,w]:reps){ofs<<f<<" "<<w;}
 // intentionally compute by extension to avoid relying on the first program's fixed-point values
 ofs.close();
 vector<array<int,8>> counts(reps.size());
 for(int k=1;k<=7;k++){
  gf_init(k);
  for(int j=0;j<(int)reps.size();j++){
   int mask=reps[j].first,ct=0;
   for(int b=0;b<Q;b++)for(int c=0;c<Q;c++)ct+=evencontact(mask,{b,1,0},{c,0,1},exps);
   for(int c=0;c<Q;c++)ct+=evencontact(mask,{1,0,0},{0,c,1},exps);
   ct+=evencontact(mask,{1,0,0},{0,1,0},exps);
   counts[j][k]=ct;
  }
  cerr<<"extension="<<k<<" checked\n";
 }
 ofstream out("independent_fixed_counts.txt");
 for(int j=0;j<(int)reps.size();j++){
  out<<reps[j].first<<" "<<reps[j].second;
  for(int k=1;k<=7;k++)out<<" "<<counts[j][k];
  out<<"\n";
 }
}
