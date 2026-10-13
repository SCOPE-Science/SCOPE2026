#include <cstdio>
#include <cassert>
#include <array>
#include <initializer_list>
using namespace std;
int mod3(int x){x%=3;return x<0?x+3:x;}
int mul(int a,int b){int c[9]={};for(int i=0;i<5;i++)for(int j=0;j<5;j++)c[i+j]+=((a/[] (int i){int n=1;while(i--)n*=3;return n;}(i))%3)*((b/[] (int j){int n=1;while(j--)n*=3;return n;}(j))%3);for(int i=8;i>=5;i--){int t=mod3(c[i]);c[i-5]-=t;c[i-1]-=2*t;}int ans=0,base=1;for(int i=0;i<5;i++){ans+=base*mod3(c[i]);base*=3;}return ans;}
int main(){static int add[243][243];int neg[243]={};for(int a=0;a<243;a++)for(int b=0;b<243;b++){int x=a,y=b,base=1,v=0;for(int j=0;j<5;j++){v+=base*((x%3+y%3)%3);base*=3;x/=3;y/=3;}add[a][b]=v;}for(int i=0;i<243;i++)for(int j=0;j<243;j++)if(!add[i][j])neg[i]=j;
int pw[242],z=1;bool seen[243]={};for(int i=0;i<242;i++){assert(z>0&&!seen[z]);seen[z]=true;pw[i]=z;z=mul(z,3);}assert(z==1);
for(int e : {2,16,20}){int y[242];for(int i=0;i<242;i++)y[i]=pw[i*e%242];long long a3=0,a4=0;
for(int i=0;i<240;i++)for(int j=i+1;j<241;j++)for(int k=j+1;k<242;k++)for(int bit=0;bit<4;bit++){
 int x=add[pw[i]][add[bit&1?neg[pw[j]]:pw[j]][bit&2?neg[pw[k]]:pw[k]]];
 if(x)continue;
 int yy=add[y[i]][add[bit&1?neg[y[j]]:y[j]][bit&2?neg[y[k]]:y[k]]];
 if(!yy)a3+=2;
}
for(int i=0;i<239;i++)for(int j=i+1;j<240;j++)for(int k=j+1;k<241;k++)for(int l=k+1;l<242;l++){
 for(int bits=0;bits<8;bits++){
  int x=pw[i];for(int idx=1;idx<4;idx++){int p=(idx==1?j:idx==2?k:l);x=add[x][(bits>>(idx-1))&1?neg[pw[p]]:pw[p]];}
  if(x)continue;
  int yy=y[i];for(int idx=1;idx<4;idx++){int p=(idx==1?j:idx==2?k:l);yy=add[yy][(bits>>(idx-1))&1?neg[y[p]]:y[p]];}
  if(!yy)a4+=2;
 }
}
printf("e=%d A3=%lld A4=%lld\n",e,a3,a4);assert(a3==0);assert(a4==(e==2?24200:e==16?33880:43560));
}
puts("VERIFY_OK");
}
