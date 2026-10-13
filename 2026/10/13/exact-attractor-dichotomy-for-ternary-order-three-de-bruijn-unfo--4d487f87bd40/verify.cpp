#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
static uint32_t used=1;
static int seq[27],w[27];
static vector<array<uint8_t,10>> cand10;
static ull cycles=0,hist[4]={},cut9=0,cut10=0,cutOver10=0,cycleNeeds10=0;
static int example[27]={}; static bool gotExample=false;
void recCand(array<uint8_t,10>&a,int d){
 if(d==10){if(a[9]>=26)cand10.push_back(a);return;}
 for(int k=1;k<=3;k++){int x=a[d-1]+k;if(x>28)break;a[d]=x;recCand(a,d+1);}
}
void inspect(){
 int hit=0;
 for(int m=0;m<3;m++){
  int letters=0,pairs=0;
  for(int i=0;i<27;i++){
   if(i%3==m)letters|=1<<w[i];
   if(i%3==m || (i+1)%3==m)pairs|=1<<(3*w[i]+w[(i+1)%27]);
  }
  if(letters==7 && pairs==511)hit|=1<<m;
 }
 ++cycles; ++hist[__builtin_popcount((unsigned)hit)];
 if(hit==0){++cycleNeeds10;if(!gotExample){gotExample=true;copy(w,w+27,example);}}
 for(int rot=0;rot<27;rot++){
  if((hit>>( ((rot+2)%3)))&1){++cut9;continue;}
  uint16_t letters[29], pairs[29];
  for(int p=0;p<29;p++){
   int c=w[(rot+p)%27];letters[p]=(1<<c);
   int val=0;
   if(p>0)val|=1<<(3*w[(rot+p-1)%27]+c);
   if(p<28)val|=1<<(3*c+w[(rot+p+1)%27]);
   pairs[p]=val;
  }
  bool ten=false;
  for(const auto& C:cand10){
   int let=0,bi=0;
   for(int j=0;j<10;j++){int p=C[j];let|=letters[p];bi|=pairs[p];}
   if(let==7 && bi==511){ten=true;break;}
  }
  if(ten)++cut10;else ++cutOver10;
 }
}
void dfs(int i,int v){
 if(i==27){if(v==0){for(int j=0;j<27;j++)w[j]=seq[j]/9;inspect();}return;}
 for(int c=0;c<3;c++){
  int e=3*v+c;
  if(used&(1u<<e))continue;
  used|=1u<<e;seq[i]=e;dfs(i+1,(v%3)*3+c);used^=1u<<e;
 }
}
int main(){
 array<uint8_t,10>a{};
 for(int i=0;i<3;i++){a[0]=i;recCand(a,1);}
 if(cand10.size()!=275){fprintf(stderr,"bad candidates %zu\n",cand10.size());return 2;}
 seq[0]=0;dfs(1,0);
 printf("cycles=%llu candidate10=%zu\n",cycles,cand10.size());
 for(int i=0;i<4;i++)printf("optimal9classes_%d=%llu\n",i,hist[i]);
 printf("cut9=%llu cut10=%llu cut_over10=%llu cycles_without_9=%llu\n",cut9,cut10,cutOver10,cycleNeeds10);
 printf("example_no_optimal_9_cut=");for(int i=0;i<27;i++)printf("%d",example[i]);puts("");
 if(cycles!=373248||hist[0]!=1632||hist[1]!=19968||hist[2]!=155568||hist[3]!=196080||cut9!=8274096||cut10!=1803600||cutOver10!=0)return 1;
 puts("VERIFY_OK");
}
