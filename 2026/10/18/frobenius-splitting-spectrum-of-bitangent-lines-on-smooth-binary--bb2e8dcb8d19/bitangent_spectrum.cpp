#include <bits/stdc++.h>
using namespace std;
struct M{int x,y,z;};
vector<M> mons;
int p[8]={0,3,7,11,19,37,67,131};
int n,q,prod[128][128],powers[128][5];
void init(int k){
 n=k;q=1<<k;int poly=p[k];
 for(int a=0;a<q;a++)for(int b=0;b<q;b++){
  int x=a,z=0;
  for(int i=0;i<k;i++){
   if(b>>i&1)z^=x;
   x<<=1;if(x&q)x^=poly;
  }
  prod[a][b]=z;
 }
 for(int a=0;a<q;a++){
  powers[a][0]=1;
  for(int i=1;i<5;i++)powers[a][i]=prod[powers[a][i-1]][a];
 }
}
int oddbinom(int i,int h){return h>=0&&h<=i&&((h&i)==h);}
int evencontact(int F,int a,int b,int c){
 int odd1=0,odd3=0;
 // line a*x+b*y+c*z=0, with first nonzero normalized
 for(int t=0;t<15;t++) if(F>>t&1){
  auto m=mons[t];int i=m.x,j=m.y,k=m.z;
  if(a){ // x=b*s+c*t, y=s,z=t
   int h=1-j;
   if(oddbinom(i,h))odd1 ^=prod[powers[b][h]][powers[c][i-h]];
   h=3-j;
   if(oddbinom(i,h))odd3 ^=prod[powers[b][h]][powers[c][i-h]];
  } else if(b){ // x=s,y=c*t,z=t
   if(i==1)odd1 ^=powers[c][j];
   if(i==3)odd3 ^=powers[c][j];
  } else { // x=s,y=t,z=0
   if(k==0 && i==1)odd1 ^=1;
   if(k==0 && i==3)odd3 ^=1;
  }
 }
 return odd1==0&&odd3==0;
}
int main(){
 for(int i=4;i>=0;i--)for(int j=4-i;j>=0;j--)mons.push_back({i,j,4-i-j});
 ifstream fin("smooth_orbits.txt");
 vector<pair<int,int>> repr;int F,w;
 while(fin>>F>>w)repr.push_back({F,w});
 vector<array<int,8>> counts(repr.size());
 for(int k=1;k<=7;k++){
  init(k);auto start=chrono::steady_clock::now();
  for(int j=0;j<(int)repr.size();j++){
   F=repr[j].first;
   int count=0;
   for(int b=0;b<q;b++)for(int c=0;c<q;c++)count+=evencontact(F,1,b,c);
   for(int c=0;c<q;c++)count+=evencontact(F,0,1,c);
   count+=evencontact(F,0,0,1);
   counts[j][k]=count;
  }
  auto t=chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count();
  cerr<<"k="<<k<<" q="<<q<<" time_ms="<<t<<"\n";
 }
 ofstream out("splittings.tsv");
 for(int j=0;j<(int)repr.size();j++){
  array<int,8> m={};
  for(int k=1;k<=7;k++){
   int un=counts[j][k];
   for(int d=1;d<k;d++)if(k%d==0)un-=d*m[d];
   if(un<0||un%k)cerr<<"BAD ",exit(1);
   m[k]=un/k;
  }
  int total=0;for(int k=1;k<=7;k++)total+=k*m[k];
  out<<repr[j].first<<" "<<repr[j].second;
  for(int k=1;k<=7;k++)out<<" "<<counts[j][k];
  for(int k=1;k<=7;k++)out<<" "<<m[k];
  out<<" "<<total<<"\n";
 }
}
