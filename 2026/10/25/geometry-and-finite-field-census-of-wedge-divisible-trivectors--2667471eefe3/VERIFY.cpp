// Independent finite-field tests of wedge-rank and cubic-multiplication formulas.
// Compile: c++ -O2 -std=c++17 VERIFY.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
vector<int> masks(int n,int k){vector<int> v;for(int x=0;x<(1<<n);++x)if(__builtin_popcount((unsigned)x)==k)v.push_back(x);return v;}
int bitrank(vector<unsigned> rows,int columns){int r=0;for(int col=columns-1;col>=0;--col){int j=r;while(j<(int)rows.size()&&!((rows[j]>>col)&1U))++j;if(j==(int)rows.size())continue;swap(rows[r],rows[j]);for(int i=0;i<(int)rows.size();++i)if(i!=r&&((rows[i]>>col)&1U))rows[i]^=rows[r];++r;if(r==(int)rows.size())break;}return r;}
long long gaussian(int n,int k,int q){long long num=1,den=1;for(int i=0;i<k;i++){long long a=1,b=1;for(int j=0;j<n-i;j++)a*=q;for(int j=0;j<k-i;j++)b*=q;num*=a-1;den*=b-1;}assert(num%den==0);return num/den;}
int irank(vector<vector<int>> a,int p){int rows=a.size(),cols=rows?(int)a[0].size():0,r=0;for(int c=0;c<cols;c++){int j=r;while(j<rows&&a[j][c]%p==0)j++;if(j==rows)continue;swap(a[r],a[j]);int inverse=1;while((a[r][c]*inverse)%p!=1)inverse++;for(int k=c;k<cols;k++)a[r][k]=(a[r][k]*inverse)%p;for(int i=0;i<rows;i++)if(i!=r){int factor=a[i][c];for(int k=c;k<cols;k++)a[i][k]=(a[i][k]-factor*a[r][k]%p+p)%p;}if(++r==rows)break;}return r;}
int sign(int a,int b){int parity=0;for(int i=0;i<6;i++)if((a>>i)&1)for(int j=0;j<i;j++)if((b>>j)&1)parity^=1;return parity?-1:1;}
int grade_rank(const vector<int>& cubic,int d,int p){auto triples=masks(6,3),cols=masks(6,d),rows=masks(6,d+3);vector<vector<int>> a(rows.size(),vector<int>(cols.size()));for(size_t j=0;j<cols.size();j++)for(size_t i=0;i<triples.size();i++)if(!(triples[i]&cols[j])){int unionmask=triples[i]|cols[j];auto it=find(rows.begin(),rows.end(),unionmask);int z=it-rows.begin();a[z][j]=(a[z][j]+p+cubic[i]*sign(triples[i],cols[j]))%p;}return irank(a,p);}
int main(){auto triples=masks(6,3),quads=masks(6,4);array<long long,7> count{};for(int x=0;x<(1<<20);x++){vector<unsigned> rows(15);for(int i=0;i<20;i++)if((x>>i)&1)for(int v=0;v<6;v++)if(!(triples[i]&(1<<v))){int mask=triples[i]|(1<<v);int k=find(quads.begin(),quads.end(),mask)-quads.begin();rows[k]^=1U<<v;}int r=bitrank(rows,6);count[r]++;}
long long n3=gaussian(6,3,2),n1=gaussian(6,1,2)*( (1LL<<10)-1-gaussian(5,2,2));long long n0=(1LL<<20)-1-n3-n1;assert(count[0]==1&&count[3]==n3&&count[5]==n1&&count[6]==n0);for(int i=0;i<=6;i++)if(i!=0&&i!=3&&i!=5&&i!=6)assert(count[i]==0);
for(int p: {2,3,5}){vector<int> dec(20),one(20),generic(20);auto put=[&](vector<int>& a,int x,int y,int z){int m=(1<<x)|(1<<y)|(1<<z);a[find(triples.begin(),triples.end(),m)-triples.begin()]=1;};put(dec,0,1,2);put(one,0,1,2);put(one,0,3,4);put(generic,0,1,2);put(generic,3,4,5);for(auto pair:vector<pair<vector<int>,int>>{{dec,3},{one,5},{generic,6}}){vector<int> got;for(int d=0;d<=3;d++)got.push_back(grade_rank(pair.first,d,p));assert(got[0]==1&&got[1]==pair.second&&got[2]==pair.second&&got[3]==1);int total=got[0]+got[1]+got[2]+got[3];assert(64-2*total==60-4*pair.second);}}
cout<<"WEDGE_TRIVECTOR_OK: F2 n=6 all 2^20 cubic forms; counts (kernel3,kernel1,kernel0)="<<n3<<","<<n1<<","<<n0<<"; graded maps verified in characteristics 2,3,5.\n";}
