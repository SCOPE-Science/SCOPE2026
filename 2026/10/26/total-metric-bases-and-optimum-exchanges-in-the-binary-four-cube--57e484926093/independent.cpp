#include <cstdio>
#include <vector>
using namespace std;
int main(){vector<unsigned> masks;
 for(int a=0;a<16;a++)for(int b=a+1;b<16;b++){
 unsigned r=0;
 for(int x=0;x<16;x++)if(x!=a&&x!=b&&__builtin_popcount(unsigned(x^a))!=__builtin_popcount(unsigned(x^b)))r|=1u<<x;
 masks.push_back(r);
 }
 int hist[7]={};vector<int> ids;
 for(unsigned s=0;s<(1u<<16);s++){
  int k=__builtin_popcount(s);if(k>6)continue;
  bool ok=true;for(auto r:masks)if(!(s&r)){ok=false;break;}
  if(ok){hist[k]++;ids.push_back(s);}
 }
 for(int k=0;k<=6;k++)printf("%d:%d ",k,hist[k]);printf("\n");
 int degreehist[121]={}, edgeSum=0;for(int s:ids){
  int dg=0;for(int x=0;x<16;x++)if((s>>x)&1)for(int y=0;y<16;y++)if(!((s>>y)&1)){
   unsigned t=s ^ (1u<<x) ^ (1u<<y);
   bool ok=true;for(auto r:masks)if(!(t&r)){ok=false;break;}
   if(ok)dg++;
  }
  degreehist[dg]++;edgeSum+=dg;
 }
 printf("edges:%d\n",edgeSum/2);for(int j=0;j<=120;j++)if(degreehist[j])printf("degree %d:%d\n",j,degreehist[j]);
}
