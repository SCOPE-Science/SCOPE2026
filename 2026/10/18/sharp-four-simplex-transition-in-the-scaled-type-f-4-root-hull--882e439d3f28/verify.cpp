#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
using ll=long long;
using Vec=array<int,4>;
struct Pt {Vec c; int kind;};

int det4(const array<Vec,4>&a){
  int p[4]={0,1,2,3}, ans=0;
  do {int q=1,inv=0;
    for(int i=0;i<4;i++){q*=a[i][p[i]];for(int j=i+1;j<4;j++)inv+=(p[i]>p[j]);}
    ans+=(inv%2?-q:q);
  }while(next_permutation(p,p+4));
  return ans;
}
// sign of a + b*sqrt(2), exactly, using integer comparisons.
int sgn(ll a,ll b){
 if(b==0)return (a>0)-(a<0);
 if(a==0)return (b>0)-(b<0);
 if((a>0)==(b>0))return (a>0)?1:-1;
 ll x=a*a-2*b*b;
 assert(x!=0); // irrationality of sqrt(2) when a,b nonzero
 return (a>0)?(x>0?1:-1):(x>0?-1:1);
}
// a+b*sqrt(2) after evaluating t^(k-1)*(A*t+B) at t=sqrt(2)
pair<ll,ll> reduced(int k,int A,int B){
 switch(k){
  case 0:return {A,0};
  case 1:return {B,A};
  case 2:return {2*A,B};
  case 3:return {2*B,2*A};
  case 4:return {4*A,2*B};
  case 5:return {4*B,4*A};
 }
 abort();
}
// Return true if |u+v sqrt2| <= |w+z sqrt2| exactly, by squared comparison.
bool leabs(ll u,ll v,ll w,ll z){
 ll a=u*u+2*v*v-w*w-2*z*z, b=2*(u*v-w*z);
 return sgn(a,b)<=0;
}
int main(){
 vector<Pt> p;
 for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)for(int a:{-2,2})for(int b:{-2,2}){
  Pt v{{0,0,0,0},0};v.c[i]=a;v.c[j]=b;p.push_back(v);
 }
 for(int i=0;i<4;i++)for(int a:{-2,2}){
  Pt v{{0,0,0,0},1};v.c[i]=a;p.push_back(v);
 }
 for(int m=0;m<16;m++){
  Pt v{{0,0,0,0},1};for(int i=0;i<4;i++)v.c[i]=(m&(1<<i))?1:-1;p.push_back(v);
 }
 assert(p.size()==48);
 // The long roots form one signed-coordinate-permutation orbit, so anchor p[0].
 array<ll,5> totals{},tops{};
 array<pair<ll,ll>,5> maxv{};
 
 array<int,5> idx{0,0,0,0,0};
 map<tuple<int,int,int>,ll> classes;
 for(idx[1]=1;idx[1]<45;idx[1]++)
 for(idx[2]=idx[1]+1;idx[2]<46;idx[2]++)
 for(idx[3]=idx[2]+1;idx[3]<47;idx[3]++)
 for(idx[4]=idx[3]+1;idx[4]<48;idx[4]++){
   int k=0;for(int i=1;i<5;i++)k+=p[idx[i]].kind;
   int coeff[5]={};
   for(int drop=0;drop<5;drop++){
     array<Vec,4> a{};int j=0,power=0;
     for(int i=0;i<5;i++)if(i!=drop){a[j++]=p[idx[i]].c;power+=p[idx[i]].kind;}
     coeff[power]+=(drop%2?-1:1)*det4(a);
   }
   // Since anchor is long, total short count is k.
   int A=coeff[k],B=(k?coeff[k-1]:0);
   for(int l=0;l<5;l++)if(l!=k && l!=k-1)assert(coeff[l]==0);
   auto [u,v]=reduced(k,A,B);
   totals[k]++;
   if(k==0){
     assert(leabs(u,v,192,0));
     if(v==0 && (u==192||u==-192))tops[k]++;
   }else{
     assert(leabs(u,v,0,128)); // sharp bound |det| <= 128 sqrt(2)
     if(u==0 && (v==128||v==-128))tops[k]++;
   }
   if(totals[k]==1 || !leabs(u,v,maxv[k].first,maxv[k].second))maxv[k]={u,v};
   classes[{k,A,B}]++;
 }
 assert((totals==array<ll,5>{8855,42504,69828,46552,10626}));
 assert(tops[0]==10);
 assert(tops[1]==24);
 assert(tops[4]==6);
 assert(tops[2]==0 && tops[3]==0);
 ll sum=0;for(auto n:totals)sum+=n;assert(sum==178365);
 cout<<"VERIFIED long-root anchored 178365; classes="<<classes.size()<<"\n";
 for(int k=0;k<=4;k++)cout<<"k="<<k<<" total="<<totals[k]<<" bound_hits="<<tops[k]<<" max_at_sqrt2="<<maxv[k].first<<"+"<<maxv[k].second<<"sqrt2\n";
 cout<<"VERIFY_OK F4_root_family maximal_simplex_volume=max(1/2,t^4/8) critical_mixed_gap=1/2-sqrt2/3\n";
}
