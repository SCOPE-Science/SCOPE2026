#include <cstdio>
#include <vector>
#include <array>
#include <algorithm>
#include <cstdint>
#include <ctime>
using namespace std;
int main(){
 constexpr int k=3,n=5;
 vector<array<int,n>> E;
 for(int code=0;code<243;code++){
  int v=code;array<int,n> e{};
  for(int j=n-1;j>=0;--j){e[j]=v%3;v/=3;}
  bool okay=true;for(int j=1;j<n;j++)if(e[j]==e[j-1])okay=false;
  if(okay)E.push_back(e);
 }
 if(E.size()!=48)return 1;
 int indeg[81][2]{},outdeg[81][2]{},inN[81]{},outN[81]{};
 auto encode=[](const array<int,n>&w,int a,int b){int u=0;for(int j=a;j<b;j++)u=3*u+w[j];return u;};
 vector<int> tail(48),head(48);
 for(int e=0;e<48;e++){
  int a=encode(E[e],0,4),b=encode(E[e],1,5);
  tail[e]=a;head[e]=b;
  outdeg[a][outN[a]++]=e;
  indeg[b][inN[b]++]=e;
 }
 vector<int> vertices;
 for(int v=0;v<81;v++)if(inN[v]){
  if(inN[v]!=2||outN[v]!=2)return 2;
  vertices.push_back(v);
 }
 if(vertices.size()!=24)return 3;
 int pos[81];fill(pos,pos+81,-1);
 for(int a=0;a<24;a++)pos[vertices[a]]=a;
 int other[48][2];
 for(int e=0;e<48;e++){
  int v=head[e],r=(indeg[v][0]==e)?0:1;
  other[e][0]=outdeg[v][r];other[e][1]=outdeg[v][1-r];
 }
 long long hist[49]{};int trace[48];
 for(uint32_t mask=0;mask<(1u<<24);mask++){
  int e=0,len=0;
  do{
   trace[len++]=E[e][0];
   e=other[e][(mask>>pos[head[e]])&1];
  }while(e!=0&&len<48);
  if(e!=0||len!=48)continue;
  int c[3]{},mn[3]{},mx[3]{};
  for(int j=0;j<48;j++){
   int x=trace[j];
   c[0]+=(x==0)-(x==1);c[1]+=(x==0)-(x==2);c[2]+=(x==1)-(x==2);
   for(int i=0;i<3;i++){mn[i]=min(mn[i],c[i]);mx[i]=max(mx[i],c[i]);}
  }
  if(c[0]||c[1]||c[2])return 4;
  int d=0;for(int i=0;i<3;i++)d=max(d,mx[i]-mn[i]);
  if(d<0||d>48)return 7;
  hist[d]++;
 }
 if(hist[3]!=23700LL || hist[4]!=420924LL || hist[5]!=341808LL)return 5;
 for(int i=0;i<49;i++)if(i!=3 && i!=4 && i!=5 && hist[i])return 6;
 for(int i=0;i<49;i++)if(hist[i])printf("%d:%lld ",i,hist[i]);
 puts("\nVERIFY_PAIRINGS_OK");
}
