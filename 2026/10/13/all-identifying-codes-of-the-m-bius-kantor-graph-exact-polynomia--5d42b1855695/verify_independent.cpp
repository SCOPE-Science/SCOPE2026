// Independent exhaustive signature calculation for vertex identifying codes.
// C++17, no external libraries or data files.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
using namespace std;
int main(){
 array<uint16_t,16> N{};
 auto add=[&](int a,int b){N[a]|=uint16_t(1)<<b;N[b]|=uint16_t(1)<<a;};
 for(int i=0;i<8;i++){add(i,(i+1)%8);add(i,8+i);add(8+i,8+(i+3)%8);}
 for(int i=0;i<16;i++) {if(__builtin_popcount(N[i])!=3)throw runtime_error("bad graph");N[i]|=uint16_t(1)<<i;}
 array<int,17> cnt{};unsigned int opt=0;
 for(unsigned int mask=0; mask<(1u<<16);mask++){
  bool ok=true;
  uint16_t signatures[16];
  for(int v=0;v<16;v++){
   signatures[v]=N[v]&mask;
   if(!signatures[v]){ok=false;break;}
   for(int u=0;u<v;u++)if(signatures[u]==signatures[v]){ok=false;break;}
   if(!ok)break;
  }
  if(ok){int k=__builtin_popcount(mask);cnt[k]++;if(k==8)opt++;}
 }
 int expected[]={0,0,0,0,0,0,0,0,584,3840,5440,3888,1780,560,120,16,1};
 for(int k=0;k<=16;k++) if(cnt[k]!=expected[k])throw runtime_error("polynomial disagreement");
 if(opt!=584)throw runtime_error("basis disagreement");
 cout<<"VERIFY_CPP_OK vertices=16 all_masks=65536 minimum=8 minimum_identifying_codes=584 polynomial=";
 for(int k=8;k<=16;k++)cout<<k<<":"<<cnt[k]<<(k==16?'\n':',');
}
