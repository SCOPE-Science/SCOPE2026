// Exact exhaustive enumeration of F_9 plane cubics with a marked rational smooth point.
// Represent a+b*i by a+3b, where i*i=2 in characteristic three.
// A projectivity sends the marked point and its tangent to [0:1:0] and Z=0.
// Every such cubic, scaled uniquely, has the seven coefficients tested below.
// Only smooth rational zeros contribute their projective tangent lines.
#include <bits/stdc++.h>
using namespace std;
struct B {uint64_t a=0,b=0;void add(B t){a|=t.a;b|=t.b;}int count()const{return __builtin_popcountll(a)+__builtin_popcountll(b);}bool full()const{return a==~0ULL&&(b&((1ULL<<27)-1))==((1ULL<<27)-1);} };
int ad[9][9],mu[9][9];
int main(){for(int x=0;x<9;x++)for(int y=0;y<9;y++){int a=x%3,b=x/3,c=y%3,e=y/3;ad[x][y]=(a+c)%3+3*((b+e)%3);mu[x][y]=((a*c+2*b*e)%3)+3*((a*e+b*c)%3);}auto A=[&](int x,int y){return ad[x][y];};auto M=[&](int x,int y){return mu[x][y];};
vector<array<int,3>> P;for(int x=0;x<9;x++)for(int y=0;y<9;y++)P.push_back({x,y,1});for(int x=0;x<9;x++)P.push_back({x,1,0});P.push_back({1,0,0});int n=P.size();
int ln[9][9][9];memset(ln,-1,sizeof ln);for(int i=0;i<n;i++){auto c=P[i];for(int k=1;k<9;k++)ln[M(c[0],k)][M(c[1],k)][M(c[2],k)]=i;}vector<B> inc(n);for(int i=0;i<n;i++)for(int j=0;j<n;j++){auto l=P[i],p=P[j];if(A(A(M(l[0],p[0]),M(l[1],p[1])),M(l[2],p[2]))==0){if(j<64)inc[i].a|=1ULL<<j;else inc[i].b|=1ULL<<(j-64);}}
// free coefficient order X^3, X^2Y, X^2Z, XYZ, XZ^2, YZ^2, Z^3, fixed Y^2 Z = 1; no XY^2/Y^3.
vector<array<int,3>> mon={{3,0,0},{2,1,0},{2,0,1},{1,1,1},{1,0,2},{0,1,2},{0,0,3},{0,2,1}};
int po[9][4];for(int x=0;x<9;x++){po[x][0]=1;for(int k=1;k<4;k++)po[x][k]=M(po[x][k-1],x);}unsigned char val[91][8],der[91][8][3];for(int pi=0;pi<n;pi++){auto p=P[pi];for(int k=0;k<8;k++){auto e=mon[k];val[pi][k]=M(M(po[p[0]][e[0]],po[p[1]][e[1]]),po[p[2]][e[2]]);for(int j=0;j<3;j++){if(!e[j]){der[pi][k][j]=0;continue;}auto ee=e;ee[j]--;der[pi][k][j]=M(e[j]%3,M(M(po[p[0]][ee[0]],po[p[1]][ee[1]]),po[p[2]][ee[2]]));}}}
unsigned long long tot=0,maxcov=0,full=0;array<int,7> bestcoef;int bestN=0;unsigned long long missing_by_one=0;int pvec[91];
for(int a=0;a<9;a++)for(int b=0;b<9;b++)for(int c=0;c<9;c++)for(int d=0;d<9;d++)for(int e=0;e<9;e++)for(int f=0;f<9;f++)for(int g=0;g<9;g++){
 int cf[]={a,b,c,d,e,f,g,1};++tot;int cnt=0;
 for(int i=0;i<91;i++){int v=val[i][7];for(int j=0;j<7;j++)v=A(v,M(cf[j],val[i][j]));if(v==0)pvec[cnt++]=i;}

 B co;
 for(int u=0;u<cnt;u++){int i=pvec[u];int derx=der[i][7][0],dery=der[i][7][1],derz=der[i][7][2];for(int j=0;j<7;j++){derx=A(derx,M(cf[j],der[i][j][0]));dery=A(dery,M(cf[j],der[i][j][1]));derz=A(derz,M(cf[j],der[i][j][2]));}int li=ln[derx][dery][derz];if(li<0)continue;co.add(inc[li]);}
 int nco=co.count();if(nco>maxcov){maxcov=nco;bestN=cnt;bestcoef={a,b,c,d,e,f,g};} if(nco>=90)missing_by_one++; if(co.full()){full++;cout<<"FOUND "<<tot<<" coeff="<<a<<","<<b<<","<<c<<","<<d<<","<<e<<","<<f<<","<<g<<" rational_points="<<cnt<<"\n";}
}
cout<<"TOTAL_NORMAL_FORMS "<<tot<<" FULL_COVERAGE "<<full<<" MAX_COVER "<<maxcov<<" EXAMPLE_RATIONAL_ZEROS "<<bestN<<" COVERAGE_GE90 "<<missing_by_one<<"\n";
cout<<"BEST_COEFF ";for(auto z:bestcoef)cout<<z<<",";cout<<"\n";
if(tot!=4782969||maxcov!=85||full!=0||bestcoef!=array<int,7>{0,1,0,0,0,0,1})return 1;
}
