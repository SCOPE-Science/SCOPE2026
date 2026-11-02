#include <algorithm>
#include <bitset>
#include <cassert>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
constexpr int MAXQ=192;
// Exhaustive quadratic-residue-tournament P4 test. Every 4-set can be translated
// so that it contains zero. Each of its 16 extension patterns is tested directly.
struct Field {
 int q;
 bool degree3;
 int add(int a,int b) const {
  if(!degree3) return (a+b)%q;
  int out=0,place=1;
  for(int i=0;i<3;i++) {out+= ((a%3+b%3)%3)*place; a/=3;b/=3;place*=3;}
  return out;
 }
 int neg(int a) const {
  if(!degree3) return (q-a)%q;
  int out=0,place=1;
  for(int i=0;i<3;i++){out+=((3-(a%3))%3)*place;a/=3;place*=3;}
  return out;
 }
 int sub(int a,int b) const {return add(a,neg(b));}
 int mul(int a,int b) const {
  if(!degree3) return int(1LL*a*b%q);
  int aa[3],bb[3]; for(int i=0;i<3;i++){aa[i]=a%3;bb[i]=b%3;a/=3;b/=3;}
  int c[5]={0,0,0,0,0};
  for(int i=0;i<3;i++) for(int j=0;j<3;j++) c[i+j]=(c[i+j]+aa[i]*bb[j])%3;
  // F_27 = F_3[X]/(X^3+2X+1), so X^3 = X-1.
  for(int k=4;k>=3;k--){int v=c[k]; c[k]=0;c[k-2]=(c[k-2]+v)%3;c[k-3]=(c[k-3]+3-v)%3;}
  return c[0]+3*c[1]+9*c[2];
 }
};
static bool prime(int n){if(n<2)return false;for(int j=2;j*j<=n;j++)if(n%j==0)return false;return true;}
struct Row {int q,min_count,min_s4;unsigned long long tuples; bool pass;int a,b,c,mask;};
Row check(Field f){
 const int q=f.q;
 vector<bool> square(q,false);
 for(int x=1;x<q;x++)square[f.mul(x,x)]=true;
 assert(count(square.begin(),square.end(),true)==(q-1)/2);
 bitset<MAXQ> domain; vector<bitset<MAXQ>> arc(q);
 for(int x=0;x<q;x++)domain.set(x);
 for(int x=0;x<q;x++)for(int y=0;y<q;y++)if(x!=y && square[f.sub(y,x)])arc[x].set(y);
 for(int x=0;x<q;x++)for(int y=0;y<q;y++)if(x!=y)assert(arc[x][y] != arc[y][x]);
 Row r{q,q,q,0,true,-1,-1,-1,-1};
 for(int a=1;a<q;a++)for(int b=a+1;b<q;b++)for(int c=b+1;c<q;c++){
  int points[4]={0,a,b,c};
  bitset<MAXQ> outside=domain;
  for(int x:points)outside.reset(x);
  for(int mask=0;mask<16;mask++){
   bitset<MAXQ> possibilities=outside;
   for(int j=0;j<4;j++) possibilities &= (mask&(1<<j)) ? arc[points[j]] : ~arc[points[j]];
   int count=possibilities.count();
   if(count<r.min_count)r.min_count=count;
   if(mask==15 && count<r.min_s4)r.min_s4=count;
   if(count==0 && r.pass){r.pass=false;r.a=a;r.b=b;r.c=c;r.mask=mask;}
  }
  r.tuples++;
 }
 return r;
}
int main(){
 cout << "VERIFIER_BEGIN\n";
 for(int q=7;q<191;q+=4){ // q == 3 (mod 4) includes 27=3^3
  if(!(prime(q)||q==27))continue;
  Row r=check(Field{q,q==27});
  cout<<"q="<<q<<" four_sets_with_zero="<<r.tuples<<" min_witnesses="<<r.min_count
      <<" min_S4_witnesses="<<r.min_s4<<" P4="<<(r.pass?"YES":"NO");
  if(!r.pass)cout<<" missing_pattern_on=(0,"<<r.a<<","<<r.b<<","<<r.c<<") mask="<<r.mask;
  cout<<"\n";
  if((q==67||q==71||q==79||q==83||q>=107)!=r.pass || (r.min_s4>0)!=r.pass){cerr<<"UNEXPECTED_CLASSIFICATION q="<<q<<"\n";return 2;}
 }
 cout << "EXHAUSTIVE_FINITE_CASES_OK\n";
}
