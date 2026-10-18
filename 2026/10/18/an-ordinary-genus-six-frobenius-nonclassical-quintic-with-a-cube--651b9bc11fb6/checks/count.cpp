#include <bits/stdc++.h>
using namespace std;
static int m,Q,mask,mod,gen; static vector<int> expt,lg;
int mulslow(int a,int b){int r=0;while(b){if(b&1)r^=a;b>>=1;a<<=1;if(a&Q)a^=mod;}return r;}
int pwslow(int a,int e){int r=1;while(e){if(e&1)r=mulslow(r,a);a=mulslow(a,a);e>>=1;}return r;}
int gpow(int a,int e){if(!a)return e?0:1; int z=lg[a]*e%(Q-1);return expt[z];}
int mul(int a,int b){return a&&b?expt[(lg[a]+lg[b])%(Q-1)]:0;}
int power(int a,int n){if(n==0)return 1;if(a==0)return 0;return expt[(long long)lg[a]*n%(Q-1)];}
bool primitive(int g){if(g==0)return false;int t=1;for(int i=1;i<Q;i++){t=mulslow(t,g); if(t==1) return i==Q-1;}return false;}
int main(){map<int,int> pol={{2,0x7},{4,0x13},{6,0x43},{8,0x11b},{10,0x409},{12,0x1053},{14,0x4443}};
 for(auto kv:pol){m=kv.first;Q=1<<m;mask=Q-1;mod=kv.second; gen=0;for(int i=2;i<Q;i++)if(primitive(i)){gen=i;break;}if(!gen){cerr<<"NOT PRIMITIVE "<<m<<"\n";continue;}
 expt.assign(Q-1,0);lg.assign(Q,0);int t=1;for(int i=0;i<Q-1;i++){expt[i]=t;lg[t]=i;t=mulslow(t,gen);}int a=expt[(Q-1)/3],ap1=a^1;
 long long affine=0; int rankhist[20]={0};
 for(int x=0;x<Q;x++){
  int x2=mul(x,x),x3=mul(x2,x),x5=mul(x3,x2);
  int A=x^1, B=x3^x, C=x3^1, D=mul(ap1,x5)^x3^x;
  int basis[20]={0}, rank=0;
  for(int j=0;j<m;j++){
   int y=1<<j, y2=mul(y,y),y4=mul(y2,y2);
   int v=mul(A,y4)^mul(B,y2)^mul(C,y);
   for(int k=m-1;k>=0;k--)if((v>>k)&1){if(!basis[k]){basis[k]=v;rank++;break;}v^=basis[k];}
  }
  int rem=D;
  for(int k=m-1;k>=0;k--)if((rem>>k)&1){if(basis[k])rem^=basis[k];else break;}
  if(rem==0){affine+=(1LL<<(m-rank));rankhist[m-rank]++;}
 }
 // z=0, y=1 affine projective x=t: F=(a+1)t^5+t^3+t; y=0 case F=(a+1)x5 excludes (1,0,0)
 int inf=0;for(int x=0;x<Q;x++){int x2=mul(x,x),x3=mul(x2,x),x5=mul(x3,x2);if((mul(ap1,x5)^x3^x)==0)inf++;}
 long long total=affine+inf;
 cout<<"m="<<m<<" Q="<<Q<<" mod="<<hex<<mod<<dec<<" gen="<<gen<<" a="<<a<<" affine="<<affine<<" infinity="<<inf<<" N="<<total<<" kernel_hist=";
 for(int i=0;i<=m;i++)if(rankhist[i])cout<<i<<":"<<rankhist[i]<<",";cout<<"\n";
 }
}
