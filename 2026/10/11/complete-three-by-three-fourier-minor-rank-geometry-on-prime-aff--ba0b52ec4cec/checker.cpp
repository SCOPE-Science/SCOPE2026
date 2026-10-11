// Exact cyclotomic and incidence verification of three-by-three Fourier minors.
// Build: c++ -O3 -std=c++17 checker.cpp -o checker && ./checker
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
using P=array<int,2>; using Tri=array<int,3>;
int dot(P a,P b,int p){return (a[0]*b[0]+a[1]*b[1])%p;}
int main(){
for(int p:{3,5}){
 vector<P> pts;for(int x=0;x<p;x++)for(int y=0;y<p;y++)pts.push_back({x,y});
 int n=pts.size(); vector<Tri> triples;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)triples.push_back({i,j,k});
 const long long T=triples.size();
 auto collinear=[&](const Tri& z){P a=pts[z[0]], b=pts[z[1]], c=pts[z[2]]; int det=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]); return ((det%p)+p)%p==0;};
 long long L=0,R[4]={},geo[4]={}, bad=0;
 for(auto A:triples)if(collinear(A))L++;
 for(const auto &A:triples){
  for(const auto &B:triples){
   int exp[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)exp[i][j]=dot(pts[A[i]],pts[B[j]],p);
   int coeff[7]={};const int perm[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
   for(int t=0;t<6;t++){
    int q=(exp[0][perm[t][0]]+exp[1][perm[t][1]]+exp[2][perm[t][2]])%p;
    coeff[q]+=((t==0||t==3||t==4)?1:-1);
   }
   // For prime p, a polynomial of degree <=p-1 vanishes at a primitive
   // pth root iff all its coefficients are equal. Here their sum is zero.
   bool singular=true;for(int k=1;k<p;k++)if(coeff[k]!=coeff[0])singular=false;
   bool rank1=true;
   for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)for(int r=0;r<3;r++)for(int s=r+1;s<3;s++){
    P da={(pts[A[i]][0]-pts[A[j]][0]+p)%p,(pts[A[i]][1]-pts[A[j]][1]+p)%p};
    P db={(pts[B[r]][0]-pts[B[s]][0]+p)%p,(pts[B[r]][1]-pts[B[s]][1]+p)%p};
    if(dot(da,db,p)!=0)rank1=false;
   }
   int actual=rank1?1:(singular?2:3);R[actual]++;
   bool rowdup=false,coldup=false;
   for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){
    bool prop=true;for(int k=1;k<3;k++)if((exp[i][k]-exp[j][k]-exp[i][0]+exp[j][0]+4*p)%p)prop=false;
    if(prop)rowdup=true;
    prop=true;for(int k=1;k<3;k++)if((exp[k][i]-exp[k][j]-exp[0][i]+exp[0][j]+4*p)%p)prop=false;
    if(prop)coldup=true;
   }
   if(singular != (rowdup||coldup))bad++;
   bool ca=collinear(A),cb=collinear(B);
   int predicted=1;
   if(!ca && !cb)predicted=3;
   else if(!ca && cb){
    predicted=3;for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){
      P da={(pts[A[i]][0]-pts[A[j]][0]+p)%p,(pts[A[i]][1]-pts[A[j]][1]+p)%p};
      P db={(pts[B[0]][0]-pts[B[1]][0]+p)%p,(pts[B[0]][1]-pts[B[1]][1]+p)%p};
      if(dot(da,db,p)==0)predicted=2;
    }
   }else if(ca){
    P v={(pts[A[1]][0]-pts[A[0]][0]+p)%p,(pts[A[1]][1]-pts[A[0]][1]+p)%p};
    int d0=dot(v,pts[B[0]],p),d1=dot(v,pts[B[1]],p),d2=dot(v,pts[B[2]],p);
    predicted=(d0==d1 && d1==d2)?1:(d0!=d1&&d1!=d2&&d0!=d2?3:2);
   }
   if(actual!=predicted)bad++;
  }
 }
 const long long K=1LL*p*(p*(p-1)*(p-2)/6),U=T-L,C=p*(p-1)*(p-2)/6;
 const long long ex1=L*K, ex2=U*3*K + L*(T-1LL*p*p*p*C-K), ex3=U*(T-3*K)+L*1LL*p*p*p*C;
 if(R[1]!=ex1||R[2]!=ex2||R[3]!=ex3||bad){cerr<<"FAIL p="<<p<<" bad="<<bad<<"\n";return 1;}
 cout<<"CHECK_PASS p="<<p<<" triples="<<T<<" collinear="<<L<<" rank1="<<R[1]<<" rank2="<<R[2]<<" rank3="<<R[3]<<" exact_cyclotomic=true geometry=true\n";
}
}
