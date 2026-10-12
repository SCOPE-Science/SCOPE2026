// Exhaustive product-automaton shortest reset-word enumeration.
// Public reproducibility component: no external dependencies.
#include <bits/stdc++.h>
using namespace std;
int main(int argc,char** argv){
 int maximum=24;
 if(argc>1) maximum=stoi(argv[1]);
 if(maximum<3 || maximum>24){cerr<<"Use n from 3 through 24\n";return 1;}
 for(int n=3;n<=maximum;n++){
  uint32_t N=(1u<<n),total=3u*N,full=N-1;
  vector<uint32_t> prev(total, UINT32_MAX);
  vector<uint32_t> q(total);
  uint32_t start=3u*full,head=0,tail=0,found=UINT32_MAX;
  prev[start]=UINT32_MAX-1; q[tail++]=start;
  while(head<tail){
   uint32_t id=q[head++], m=id/3, r=id%3;
   if(__builtin_popcount(m)==1){found=id;break;}
   if(r<2){
    uint32_t t=3u*(((m<<1)&full)|(m>>(n-1)))+r+1;
    if(prev[t]==UINT32_MAX){prev[t]=id;q[tail++]=t;}
   }
   uint32_t m2=(m&~(1u<<(n-1))) | ((m>>(n-1))&1u);
   uint32_t t=3u*m2;
   if(prev[t]==UINT32_MAX){prev[t]=id|0x80000000u;q[tail++]=t;}
  }
  if(found==UINT32_MAX){cerr<<"No reset "<<n<<"\n";return 2;}
  string w;
  for(uint32_t i=found;i!=start;){uint32_t p=prev[i];w.push_back((p&0x80000000u)?'b':'a');i=p&0x7fffffffu;}
  reverse(w.begin(),w.end());
  cout<<n<<" "<<w.size()<<" "<<count(w.begin(),w.end(),'a')<<" "<<count(w.begin(),w.end(),'b')<<" "<<head<<" "<<tail<<" "<<w<<"\n";
 }
}
