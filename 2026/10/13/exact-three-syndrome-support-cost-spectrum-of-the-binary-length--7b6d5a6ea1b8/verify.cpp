#include <bits/stdc++.h>
using namespace std;
int mul(int x,int y){int z=0;while(y){if(y&1)z^=x;y>>=1;x<<=1;if(x&16)x^=0x13;}return z;}
using Mask=array<uint64_t,4>;
void setbit(Mask& M,int x){M[x>>6]|=1ULL<<(x&63);}
int main(){
 int p[15],x=1;for(int j=0;j<15;j++){p[j]=x;x=mul(x,2);}
 if(x!=1||set<int>(p,p+15).size()!=15){cerr<<"bad_field\n";return 1;}
 int col[15];for(int j=0;j<15;j++)col[j]=16*p[j]+p[(15-j)%15];
 vector<Mask> covers[8];
 for(int I=1;I<(1<<15);I++){
  int k=__builtin_popcount((unsigned)I);if(k<3||k>7)continue;
  vector<int> a={0};
  for(int j=0;j<15;j++)if(I>>j&1){int n=a.size();for(int t=0;t<n;t++)a.push_back(a[t]^col[j]);}
  Mask M{};for(int v:a)setbit(M,v);
  covers[k].push_back(M);
 }
 long total=0;map<int,long> hist;int hard[3]={};vector<array<int,3>> hardest;
 for(int b0=0;b0<8;b0++)for(int b1=b0+1;b1<8;b1++)for(int b2=b1+1;b2<8;b2++){
  vector<pair<int,int>> free;
  int piv[3]={b0,b1,b2};
  for(int h=0;h<3;h++)for(int j=piv[h]+1;j<8;j++)if(j!=b0&&j!=b1&&j!=b2)free.push_back({h,j});
  for(int z=0;z<(1<<free.size());z++){
   int b[3]={1<<b0,1<<b1,1<<b2};
   for(int h=0;h<(int)free.size();h++)if(z>>h&1)b[free[h].first]|=1<<free[h].second;
   Mask U{};for(int j=0;j<8;j++)setbit(U,((j&1)?b[0]:0)^((j&2)?b[1]:0)^((j&4)?b[2]:0));
   int radius=8;
   for(int k=3;k<=7;k++){
    bool found=false;
    for(const Mask& S:covers[k]){
     if(((U[0]&~S[0])|(U[1]&~S[1])|(U[2]&~S[2])|(U[3]&~S[3]))==0){found=true;break;}
    }
    if(found){radius=k;break;}
   }
   hist[radius]++;total++;
   if(radius==7){hardest.push_back({b[0],b[1],b[2]});if(hard[0]==0){hard[0]=b[0];hard[1]=b[1];hard[2]=b[2];}}
  }
 }
 cout<<"COUNT "<<total<<"\nHIST";for(auto [r,n]:hist)cout<<" "<<r<<":"<<n;
 cout<<"\nWITNESS "<<hard[0]<<","<<hard[1]<<","<<hard[2]<<"\n";
 if(total!=97155||hist[3]!=330||hist[4]!=6510||hist[5]!=39885||hist[6]!=49230||hist[7]!=1200||hist.size()!=5){cout<<"VERIFY_FAILED\n";return 2;}

 cout<<"VERIFY_OK\n";
}
