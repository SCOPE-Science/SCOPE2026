#include <algorithm>
#include <cstdint>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
using namespace std;
constexpr int MAXN=87;
constexpr int vals[4]={0,1,2,5};
long long ps[MAXN+1]={0};
char w[MAXN+1]={0};
uint64_t nodes=0, counts[MAXN+1]={0};
vector<string> winners;
inline unsigned forb(int len){ // existing prefix length len; forbidden next letters
  unsigned b=0;
  int t=len+1; long long tot=ps[len];
  for(int k=1;k*2<=t;k++){
    long long v=2*ps[t-k]-ps[t-2*k]-tot;
    if(v==0) b|=1;
    else if(v==1) b|=2;
    else if(v==2) b|=4;
    else if(v==5) b|=8;
    if(b==15)break;
  }
  return b;
}
void dfs(int len){
 counts[len]++; nodes++;
 if(len==86){w[len]=0;winners.emplace_back(w,len);}
 if(len==87)return;
 unsigned banned=forb(len);
 for(int a=0;a<4;a++)if(!(banned&(1u<<a))){ps[len+1]=ps[len]+vals[a];w[len]='0'+vals[a];dfs(len+1);}
}
int main(){dfs(0);cerr<<"nodes="<<nodes<<" max length "<<max_element(begin(counts),end(counts))-begin(counts)<<"\n";
for(int i=0;i<=87;i++) if(i>=65||i%10==0)cerr<<i<<" "<<counts[i]<<"\n";
cout<<"winners="<<winners.size()<<"\n";
for(auto &v:winners)cout<<v<<"\n";
}
