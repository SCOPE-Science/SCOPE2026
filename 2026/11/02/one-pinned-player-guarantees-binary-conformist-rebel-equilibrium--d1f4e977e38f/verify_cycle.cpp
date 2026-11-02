// Reproducible direct best-response enumeration for binary
// conformist / rebel / fixed-action network games on simple cycles.
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
static bool eq(int n, uint64_t typ, uint64_t act) {
  for (int i=0;i<n;i++) {
    int t=(typ>>(2*i))&3, x=(act>>i)&1;
    if (t>=2) { if(x!=t-2)return false; continue; }
    int a=(act>>((i+n-1)%n))&1, b=(act>>((i+1)%n))&1;
    if (a==b && x!=(a^t))return false;
  }
  return true;
}
static uint64_t count(int n,uint64_t typ){
  uint64_t ct=0;
  for(uint64_t x=0;x<(1ULL<<n);x++) if(eq(n,typ,x))ct++;
  return ct;
}
static bool alternating(int n,uint64_t typ){
 for(int i=0;i<n;i++){
  int a=(typ>>(2*i))&3,b=(typ>>(2*((i+1)%n)))&3;
  if(a>=2||b>=2||a==b)return false;
 }
 return true;
}
static uint64_t encode_alt_pin(int n,int position,int pinned_action,int initialtype){
 uint64_t typ=0;
 for(int i=0;i<n;i++){
  int t=(initialtype^(i&1));
  if(i==position)t=2+pinned_action;
  typ|=(uint64_t)t<<(2*i);
 }
 return typ;
}
static uint64_t seed=0x929ab3c19def45ULL;
static uint64_t rand64(){seed^=seed<<7;seed^=seed>>9;seed^=seed<<8;return seed;}
static int ntests=0;
static void demand(bool v,const char *msg){ntests++;if(!v){cerr<<"FAIL: "<<msg<<"\n";exit(2);}}
int main(){
 uint64_t checked=0, types=0, noeq=0;
 for(int n=3;n<=8;n++){
  uint64_t lim=1ULL<<(2*n);
  for(uint64_t typ=0;typ<lim;typ++){
   bool stubborn=false;
   for(int i=0;i<n;i++)if(((typ>>(2*i))&3)>=2)stubborn=true;
   bool absent=count(n,typ)==0;
   bool expected=!stubborn&&(n%4==2)&&alternating(n,typ);
   demand(absent==expected,"complete 4-type cycle classification");
   checked++;types+=stubborn;noeq+=absent;
  }
 }
 cout<<"exhaustive 4-type instances n=3..8: "<<checked<<", with stubborn="<<types<<", no PNE="<<noeq<<"\n";
 uint64_t pin_checks=0;
 for(int n=4;n<=16;n+=2){
   uint64_t predicted=(n%4==2)?(n/2):(n/2+1);
   for(int i=0;i<n;i++)for(int b=0;b<2;b++)for(int first=0;first<2;first++){
    uint64_t typ=encode_alt_pin(n,i,b,first);
    demand(count(n,typ)==predicted,"exact number after one pin on an alternating ring");
    pin_checks++;
   }
 }
 cout<<"exact alternating single-pin counts n=4..16: "<<pin_checks<<"\n";
 uint64_t trials=0;
 for(int n=9;n<=15;n++)for(int r=0;r<1000;r++){
  uint64_t typ=0;bool stubborn=false;
  for(int i=0;i<n;i++){
   int t=rand64()&3;if(t>=2)stubborn=true;
   typ|=(uint64_t)t<<(2*i);
  }
  if(!stubborn){ typ=(typ & ~3ULL) | 2ULL; stubborn=true; }
  demand(count(n,typ)>0,"sampled fixed-action cycles have equilibrium");
  trials++;
 }
 cout<<"randomized stubborn-cycle checks n=9..15: "<<trials<<"\n";
 // Three actions; four-ring with types R,C,R,S0, and all actions enumerated.
 int t3[4]={1,0,1,2};int ternary_ct=0;
 for(int p=0;p<81;p++){
  int x[4],q=p;for(int i=0;i<4;i++){x[i]=q%3;q/=3;}
  bool good=true;
  for(int i=0;i<4;i++){
   if(t3[i]==2){if(x[i]!=0)good=false;continue;}
   int score=(t3[i]==0)?(int)(x[i]==x[(i+3)%4])+(int)(x[i]==x[(i+1)%4]):(int)(x[i]!=x[(i+3)%4])+(int)(x[i]!=x[(i+1)%4]);
   for(int a=0;a<3;a++){
    int other=(t3[i]==0)?(int)(a==x[(i+3)%4])+(int)(a==x[(i+1)%4]):(int)(a!=x[(i+3)%4])+(int)(a!=x[(i+1)%4]);
    if(other>score)good=false;
   }
  }
  if(good)ternary_ct++;
 }
 demand(ternary_ct==0,"ternary four-cycle contrast");
 cout<<"ternary R-C-R-S0 cycle equilibria="<<ternary_ct<<"\n";
 cout<<"VERIFY_OK checks="<<ntests<<"\n";
}
