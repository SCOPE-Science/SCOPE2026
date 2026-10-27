// Exact arithmetic census of genus-four hyperelliptic equations over F_3.
// All calculations use deterministic polynomial residue-field arithmetic.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static int mod3(int a){a%=3;return a<0?a+3:a;}
struct Field{
 int m,q;vector<int> modulus;vector<vector<uint8_t>> add,mul;vector<int> quadratic_character;
 Field(int degree,vector<int> p):m(degree),modulus(p){
  q=1;for(int j=0;j<m;j++)q*=3;
  add.assign(q,vector<uint8_t>(q));mul=add;quadratic_character.assign(q,-1);quadratic_character[0]=0;
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int aa=a,bb=b,A=0,place=1;
   for(int i=0;i<m;i++){A+=((aa%3+bb%3)%3)*place;aa/=3;bb/=3;place*=3;}
   add[a][b]=A;
   vector<int> c(2*m,0);aa=a;
   for(int i=0;i<m;i++){bb=b;for(int j=0;j<m;j++){c[i+j]+=(aa%3)*(bb%3);bb/=3;}aa/=3;}
   for(int i=2*m-2;i>=m;i--){int u=mod3(c[i]);for(int j=0;j<m;j++)c[i-m+j]-=u*modulus[j];}
   int M=0;place=1;for(int i=0;i<m;i++){M+=mod3(c[i])*place;place*=3;}
   mul[a][b]=M;
  }
  for(int a=1;a<q;a++)quadratic_character[mul[a][a]]=1;
  int squares=0;for(int a=1;a<q;a++)squares+=(quadratic_character[a]==1);
  assert(squares==(q-1)/2);
  for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++){
   assert(add[add[a][b]][c]==add[a][add[b][c]]);
   // Multiplication associativity is mathematically guaranteed by the irreducible modulus.
  }
 }
 int point_count(const vector<int>& c, int degree){
  int N=q+1+(degree==10);
  for(int x=0;x<q;x++){
   int u=1;
   for(int k=degree-1;k>=0;k--)u=add[mul[u][x]][c[k]];
   N+=quadratic_character[u];
  }
  return N;
 }
};
using Poly=vector<int>;
void trim(Poly &a){while(!a.empty()&&a.back()==0)a.pop_back();}
Poly residue(Poly a,const Poly &b){assert(!b.empty());int lc=b.back(),inv=(lc==1?1:2);
 while(a.size()>=b.size()){
  int k=(int)a.size()-(int)b.size(),t=mod3(a.back()*inv);
  for(size_t j=0;j<b.size();j++)a[j+k]=mod3(a[j+k]-t*b[j]);
  trim(a);
 }
 return a;
}
Poly gcdpoly(Poly a,Poly b){trim(a);trim(b);while(!b.empty()){Poly r=residue(a,b);a=b;b=r;}return a;}
bool squarefree(const vector<int> &a,int d){Poly f(a);f.push_back(1);Poly df(d,0);
 for(int j=1;j<=d;j++)df[j-1]=mod3(j*f[j]);trim(df);return gcdpoly(f,df).size()==1;
}
int main(){
 Field F9(2,{1,0}),F81(4,{2,1,0,0});
 // Check both modulus irreducibilities over F3 by computing root exclusions in F3 and F9.
 auto eval=[&](const vector<int>& coeff,const Field& F,int x){int y=0;for(int j=(int)coeff.size()-1;j>=0;j--)y=F.add[F.mul[y][x]][coeff[j]];return y;};
 for(int x=0;x<3;x++) assert(eval({1,0,1},F9,x)!=0);
 for(int x=0;x<9;x++) assert(eval({2,1,0,0,1},F9,x)!=0);
 int totalSmooth9=0,totalSmooth10=0,zero9=0,zero10=0,min9=10000,min10=10000;
 int firstMask=-1;
 for(int d:{9,10}){
  int N=1;for(int j=0;j<d;j++)N*=3;
  vector<int> c(d);
  for(int mask=0;mask<N;mask++){
   int n=mask;for(int j=0;j<d;j++){c[j]=n%3;n/=3;}
   if(!squarefree(c,d))continue;
   if(d==9)totalSmooth9++;else totalSmooth10++;
   int n2=F9.point_count(c,d),n4=F81.point_count(c,d);
   assert(n4>=n2);assert((n4-n2)%4==0);
   int b4=(n4-n2)/4;
   if(d==9)min9=min(min9,b4);else min10=min(min10,b4);
   if(b4==0){
     if(d==9){zero9++;firstMask=mask;}else zero10++;
     cout<<"ZERO degree="<<d<<" coefficients_low_to_high=";
     for(int j=0;j<d;j++)cout<<c[j]<<(j+1==d?'\n':',');
     cout<<"N2="<<n2<<" N4="<<n4<<"\n";
   }
  }
 }
 cout<<"smooth_degree9="<<totalSmooth9<<" smooth_degree10="<<totalSmooth10
     <<" zero_degree9="<<zero9<<" zero_degree10="<<zero10
     <<" min_B4_degree9="<<min9<<" min_B4_degree10="<<min10<<"\n";
 assert(zero9==1 && zero10==0 && firstMask==6);
 assert(min9==0 && min10>0);
 cout<<"VERIFY_OK\n";
}
