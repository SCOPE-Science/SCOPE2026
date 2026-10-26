// Exhaustive exact arithmetic for rational-minimal nontrivial blocking quartics over F_3.
#include <bits/stdc++.h>
using namespace std;
using E=array<int,3>;
int mod3(int x){x%=3;return x<0?x+3:x;}
vector<E> mons(int d){vector<E> v;for(int a=d;a>=0;--a)for(int b=d-a;b>=0;--b)v.push_back({a,b,d-a-b});return v;}
int pow3(int x,int n){int y=1;for(int i=0;i<n;i++)y=y*x%3;return y;}
int rank3(vector<array<uint8_t,36>>& v){int rank=0;for(int col=0;col<36;col++){
 int j=rank; while(j<(int)v.size() && v[j][col]==0)j++;
 if(j==(int)v.size())continue;
 if(j!=rank)swap(v[j],v[rank]);
 if(v[rank][col]==2)for(int c=col;c<36;c++)v[rank][c]=mod3(2*v[rank][c]);
 for(int row=rank+1;row<(int)v.size();row++){
  int z=v[row][col];if(!z)continue;
  for(int c=col;c<36;c++)v[row][c]=mod3((int)v[row][c]-z*v[rank][c]);
 }
 rank++;if(rank==36)break;
 }return rank;}
int main(int argc,char**argv){
 vector<E> p;for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
 if(!(x||y||z))continue;E v={x,y,z};int t=x?x:(y?y:z), s=(t==1?1:2);for(int&i:v)i=i*s%3;
 if(find(p.begin(),p.end(),v)==p.end())p.push_back(v); }
 sort(p.begin(),p.end());assert(p.size()==13);
 int target=311;
 auto M4=mons(4), M7=mons(7);assert(M4.size()==15&&M7.size()==36);
 int ev[13][15]={};for(int i=0;i<13;i++)for(int j=0;j<15;j++)ev[i][j]=pow3(p[i][0],M4[j][0])*pow3(p[i][1],M4[j][1])%3*pow3(p[i][2],M4[j][2])%3;
 int B[9][15]={
{0,2,0,1,0,0,0,0,0,0,0,0,0,0,0},
{0,2,0,0,1,0,0,0,0,0,0,0,0,0,0},
{0,0,2,0,0,1,0,0,0,0,0,0,0,0,0},
{0,2,0,0,0,0,1,0,0,0,0,0,0,0,0},
{0,2,0,0,0,0,0,1,0,0,0,0,0,0,0},
{0,2,0,0,0,0,0,0,1,0,0,0,0,0,0},
{0,0,2,0,0,0,0,0,0,1,0,0,0,0,0},
{0,0,0,0,0,0,0,0,0,0,0,2,1,0,0},
{0,0,0,0,0,0,0,0,0,0,0,2,0,1,0}};
 map<E,int> row7;for(int i=0;i<36;i++)row7[M7[i]]=i;
 int total=0,smooth=0,nonsmooth=0,ranks[37]={};
 ofstream all("verification/candidate_coefficients.txt");ofstream yes("verification/smooth_coefficients.txt");
 for(int k=1;k<19683;k++){
  int d[9];int n=k;for(int i=0;i<9;i++){d[i]=n%3;n/=3;}
  int c[15]={};for(int i=0;i<9;i++)for(int j=0;j<15;j++)c[j]=mod3(c[j]+d[i]*B[i][j]);
  int mask=0;for(int i=0;i<13;i++){int s=0;for(int j=0;j<15;j++)s+=ev[i][j]*c[j];if(s%3==0)mask|=1<<i;}
  if(mask!=target)continue;
  total++;
  vector<array<uint8_t,36>> rows;rows.reserve(45);
  for(int der=0;der<3;der++)for(const E&mul:M4){
   array<uint8_t,36> a={};
   for(int j=0;j<15;j++)if(c[j] && M4[j][der]){
    E e=mul;e[0]+=M4[j][0];e[1]+=M4[j][1];e[2]+=M4[j][2];e[der]--;
    int pos=row7.at(e);
    a[pos]=mod3(a[pos]+c[j]*M4[j][der]);
   }
   rows.push_back(a);
  }
  int rank=rank3(rows);ranks[rank]++;
  for(int j=0;j<15;j++)all<<c[j];all<<" "<<rank<<"\n";
  if(rank==36){smooth++;for(int j=0;j<15;j++)yes<<c[j];yes<<"\n";}
  else nonsmooth++;
 }
 cout<<"target_mask="<<target<<" candidate_vectors="<<total<<" smooth_vectors="<<smooth<<" singular_vectors="<<nonsmooth<<"\n";
 cout<<"ranks:";for(int i=0;i<=36;i++)if(ranks[i])cout<<" "<<i<<":"<<ranks[i];cout<<"\n";
}
