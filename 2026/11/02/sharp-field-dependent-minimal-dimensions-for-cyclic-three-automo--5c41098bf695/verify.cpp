#include <array>
#include <algorithm>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
struct Field {
 int q, p, degree, modpoly;
 vector<vector<int>> add, mul;
 Field(int q0):q(q0),p(q0),degree(1),modpoly(0) {
  if(q==4){p=2;degree=2;modpoly=7;} // x²+x+1
  if(q==8){p=2;degree=3;modpoly=11;} // x³+x+1
  if(q==9){p=3;degree=2;modpoly=10;} // x²+1 = (1,0,1) base3
  add.assign(q,vector<int>(q));mul=add;
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
    int u=a,v=b,s=0,pp=1;
    for(int i=0;i<degree;i++){s+=((u%p+v%p)%p)*pp;u/=p;v/=p;pp*=p;}
    add[a][b]=s;
    if(degree==1){mul[a][b]=(a*b)%p;continue;}
    vector<int> poly(2*degree,0);u=a;
    for(int i=0;i<degree;i++){int ai=u%p;u/=p;v=b;for(int j=0;j<degree;j++){poly[i+j]=(poly[i+j]+ai*(v%p))%p;v/=p;}}
    for(int k=2*degree-2;k>=degree;k--){int c=poly[k];
      for(int j=0;j<degree;j++){int coeff=(modpoly/(int)([] (int base,int power){int s=1;while(power--)s*=base;return s;}(p,j)))%p;poly[k-degree+j]=(poly[k-degree+j]+p-c*coeff%p)%p;}
      poly[k]=0;
    }
    int val=0,base=1;for(int i=0;i<degree;i++){val+=poly[i]*base;base*=p;}
    mul[a][b]=val;
  }
 }
 int ad(int a,int b)const{return add[a][b];}int mm(int a,int b)const{return mul[a][b];}
};
struct Mat { int a,b,c,d;}; // col 1=(a,b), col2=(c,d)
vector<Mat> gl2(const Field&f){vector<Mat> out;
 for(int a=0;a<f.q;a++)for(int b=0;b<f.q;b++)for(int c=0;c<f.q;c++)for(int d=0;d<f.q;d++)if(f.mm(a,d)!=f.mm(b,c))out.push_back({a,b,c,d}); return out;}
int count_auto2(const Field &f,const Mat &str,const vector<Mat>&group){
 int out=0;int a0=str.a,a1=str.b,b0=str.c,b1=str.d;
 for(auto g:group){
  if(f.ad(f.mm(a0,g.a),f.mm(a1,g.c))!=f.ad(f.mm(a0,f.mm(g.a,g.a)),f.mm(b0,f.mm(g.b,g.b))))continue;
  if(f.ad(f.mm(a0,g.b),f.mm(a1,g.d))!=f.ad(f.mm(a1,f.mm(g.a,g.a)),f.mm(b1,f.mm(g.b,g.b))))continue;
  if(f.ad(f.mm(b0,g.a),f.mm(b1,g.c))!=f.ad(f.mm(a0,f.mm(g.c,g.c)),f.mm(b0,f.mm(g.d,g.d))))continue;
  if(f.ad(f.mm(b0,g.b),f.mm(b1,g.d))!=f.ad(f.mm(a1,f.mm(g.c,g.c)),f.mm(b1,f.mm(g.d,g.d))))continue;
  if(f.ad(f.mm(a0,f.mm(g.a,g.c)),f.mm(b0,f.mm(g.b,g.d)))!=0)continue;
  if(f.ad(f.mm(a1,f.mm(g.a,g.c)),f.mm(b1,f.mm(g.b,g.d)))!=0)continue;
  out++;
 }
 return out;
}
int main(){
 for(int q:{2,3,4,5,7,8,9}){
  Field f(q);auto G=gl2(f);
  long long exact3=0, perfect3=0, nonperfect3=0, total=0;
  for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)for(int d=0;d<q;d++){
   Mat st{a,b,c,d};int n=count_auto2(f,st,G);total++;
   if(n==3){exact3++; if(f.mm(a,d)!=f.mm(b,c))perfect3++; else nonperfect3++;}
  }
  // all two-cycle forms with alpha not cube have 3 automorphisms iff field has nontrivial cube roots
  int cubeRoots=0,noncubes=0;
  for(int a=1;a<q;a++)if(f.mm(f.mm(a,a),a)==1)cubeRoots++;
  for(int a=1;a<q;a++){bool cube=false;for(int b=1;b<q;b++)if(f.mm(f.mm(b,b),b)==a)cube=true;if(!cube)noncubes++;}
  cout<<"q="<<q<<" structures="<<total<<" Aut_C3="<<exact3<<" perfect="<<perfect3<<" nonperfect="<<nonperfect3<<" cubeRoots="<<cubeRoots<<" noncubes="<<noncubes<<"\n";
  bool expected= (cubeRoots==3&&noncubes>0) || (q==4);
  if((exact3>0)!=expected || (q!=4&&nonperfect3))throw runtime_error("classification mismatch");
 }
 cout<<"VERIFY_OK\n";
}
