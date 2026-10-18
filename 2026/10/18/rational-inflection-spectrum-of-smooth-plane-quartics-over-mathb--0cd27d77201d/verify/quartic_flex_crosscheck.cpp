// Independent direct coefficient census of rational flexes; no projective-orbit quotient.
#include <array>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <fstream>
using namespace std;
struct P{int v[3];};
static int E[15][3];
static int B[5][5];
static int F[13][15],D[13][3][15],H2[13][13][15],H3[13][13][15];
static P points[13];
static int ndots[15];
int val(int a){return (a%3+3)%3;}
int power(int v,int e){int r=1;while(e--)r=r*v%3;return r;}
int coeff(const P&p,const P&q,const int ex[3],int deg){
 int x=ex[0],y=ex[1],z=ex[2];int ans=0;
 for(int i=0;i<=x;i++)for(int j=0;j<=y;j++){
  int k=deg-i-j;if(k<0||k>z)continue;
  int t=B[x][i]*B[y][j]*B[z][k];
  t=t*power(p.v[0],x-i)*power(q.v[0],i);
  t=t*power(p.v[1],y-j)*power(q.v[1],j);
  t=t*power(p.v[2],z-k)*power(q.v[2],k);
  ans+=t;
 }
 return val(ans);
}
void init(){
 int i=0;for(int x=4;x>=0;x--)for(int y=4-x;y>=0;y--){E[i][0]=x;E[i][1]=y;E[i++][2]=4-x-y;}
 for(i=0;i<=4;i++){B[i][0]=B[i][i]=1;for(int j=1;j<i;j++)B[i][j]=val(B[i-1][j-1]+B[i-1][j]);}
 int j=0;for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
  if(x==0&&y==0&&z==0)continue;
  if((x?x:(y?y:z))!=1)continue;
  points[j++]={{x,y,z}};
 }
 if(j!=13)abort();
 for(int p=0;p<13;p++)for(int m=0;m<15;m++){
  F[p][m]=1;
  for(int k=0;k<3;k++)F[p][m]*=power(points[p].v[k],E[m][k]);
  F[p][m]%=3;
  for(int k=0;k<3;k++){
   int w=E[m][k];
   if(!w){D[p][k][m]=0;continue;}
   D[p][k][m]=w;
   for(int j=0;j<3;j++)D[p][k][m]*=power(points[p].v[j],E[m][j]-(k==j));
   D[p][k][m]%=3;
  }
  for(int q=0;q<13;q++){
   H2[p][q][m]=coeff(points[p],points[q],E[m],2);
   H3[p][q][m]=coeff(points[p],points[q],E[m],3);
  }
 }
 ndots[0]=1;for(i=1;i<15;i++)ndots[i]=ndots[i-1]*3;
}
int dot(const int u[15],const int a[15]){
 int v=0;for(int i=0;i<15;i++)v+=u[i]*a[i];return v%3;
}
int exact_geometric_smooth(const int a[15]){
 int degree7[8][8][8];int row=0;
 for(int x=7;x>=0;x--)for(int y=7-x;y>=0;y--)degree7[x][y][7-x-y]=row++;
 int M[36][45]={};
 for(int k=0;k<3;k++)for(int j=0;j<15;j++){
  int e[3]={E[j][0],E[j][1],E[j][2]};if(e[k]==0)continue;
  int scalar=a[j]*e[k]%3;e[k]--;
  for(int t=0;t<15;t++){
   int x=e[0]+E[t][0],y=e[1]+E[t][1],z=e[2]+E[t][2];
   int rr=degree7[x][y][z],cc=15*k+t;
   M[rr][cc]=(M[rr][cc]+scalar)%3;
  }
 }
 int pivot_row=0;
 for(int col=0;col<45;col++){
  int rr=pivot_row;while(rr<36&&M[rr][col]==0)rr++;
  if(rr==36)continue;
  for(int j=col;j<45;j++)swap(M[rr][j],M[pivot_row][j]);
  if(M[pivot_row][col]==2)for(int j=col;j<45;j++)M[pivot_row][j]=2*M[pivot_row][j]%3;
  for(int k=pivot_row+1;k<36;k++){
   int v=M[k][col];if(!v)continue;
   for(int j=col;j<45;j++)M[k][j]=val(M[k][j]-v*M[pivot_row][j]);
  }
  if(++pivot_row==36)return 1;
 }
 return 0;
}
#ifdef ORBIT_RECHECK
#include <iostream>
#include <map>
#include <sstream>
#include <string>
int main(){init();
 std::ifstream in("flex_orbits.tsv");
 std::string header;std::getline(in,header);
 long long forms=0, smooth_forms=0;int orb=0,good=0;
 std::map<std::pair<int,int>,std::pair<long long,int>> table;
 int code,sz,sm,np,r,h;
 while(in>>code>>sz>>sm>>np>>r>>h){
  ++orb;forms+=sz;int a[15]={};int v=code;
  for(int j=0;j<15;j++){a[j]=v%3;v/=3;}
  int is_smooth=exact_geometric_smooth(a);
  if(is_smooth!=sm){std::cerr<<"smoothness mismatch code="<<code<<"\n";return 2;}
  if(!sm)continue;
  ++good;smooth_forms+=sz;
  int pn=0,fn=0,hn=0;
  for(int p=0;p<13;p++){
   if(dot(F[p],a)!=0)continue;pn++;
   int g[3];for(int k=0;k<3;k++)g[k]=dot(D[p][k],a);
   if(!(g[0]||g[1]||g[2])){std::cerr<<"singular rational point";return 3;}
   int q=-1;for(int j=0;j<13;j++){
    if(j==p)continue;
    int s=0;for(int k=0;k<3;k++)s+=g[k]*points[j].v[k];
    if(s%3==0){q=j;break;}
   }
   if(q<0)abort();
   if(dot(H2[p][q],a)==0){if(dot(H3[p][q],a)==0)hn++;else fn++;}
  }
  if(pn!=np || fn!=r || hn!=h){
    std::cerr<<"contact mismatch code="<<code<<" computed "<<pn<<","<<fn<<","<<hn<<" table "<<np<<","<<r<<","<<h<<"\n";return 4;
  }
  table[{fn,hn}].first+=sz;table[{fn,hn}].second++;
 }
 std::cout<<"forms="<<forms<<" orbits="<<orb<<" smooth="<<smooth_forms<<" smooth_orbits="<<good<<"\n";
 for(auto &v:table)std::cout<<v.first.first<<" "<<v.first.second<<" "<<v.second.first<<" "<<v.second.second<<"\n";
}
#else
int main(){init();long long scanned=0,seven=0,sevenTypes[14]={},smoothTypes[14]={},eight=0;vector<pair<int,int>> candidates;
 for(int code=1;code<14348907;code++){
  int a[15],c=code,first=-1;
  for(int m=0;m<15;m++){a[m]=c%3;c/=3;if(first<0&&a[m])first=a[m];}
  if(first!=1)continue;
  scanned++;
  int r=0,h=0;
  for(int p=0;p<13;p++){
   if(r+h+13-p<7)break;
   if(dot(F[p],a))continue;
   int g[3];for(int k=0;k<3;k++)g[k]=dot(D[p][k],a);
   if(!(g[0]||g[1]||g[2]))continue;
   int q=-1;
   for(int l=0;l<13;l++){
    if(l==p)continue;
    int s=0;for(int k=0;k<3;k++)s+=g[k]*points[l].v[k];
    if(s%3==0){q=l;break;}
   }
   if(q<0)abort();
   if(dot(H2[p][q],a)==0){if(dot(H3[p][q],a)==0)h++;else r++;}
  }
  if(r+h>=7){seven++;if(r+h==8)eight++;if(h<14)sevenTypes[h]++; if(exact_geometric_smooth(a)) smoothTypes[h]++; candidates.push_back({code,r*100+h});}
 }
 printf("projective_forms %lld candidates_at_least_seven %lld candidate_eight %lld\n",scanned,seven,eight);
 for(int i=0;i<14;i++)if(sevenTypes[i])printf("hyperflex_%d candidates=%lld geometrically_smooth=%lld\n",i,sevenTypes[i],smoothTypes[i]);
 ofstream out("direct_candidates.tsv");for(auto [c,t]:candidates)out<<c<<'\t'<<t<<'\n';
}

#endif
