#include <bits/stdc++.h>
using namespace std;
int mats[256], idx[512], br[256][256];
int mul(int x,int y){int z=0; for(int i=0;i<3;i++)for(int j=0;j<3;j++){int t=0;for(int k=0;k<3;k++)t^=((x>>(3*i+k))&1)&((y>>(3*k+j))&1);z|=(t<<(3*i+j));}return z;}
int inv(int a){for(int b=0;b<512;b++)if(mul(a,b)==273 && mul(b,a)==273) return b;return -1;}
int cl(int a,int b){int piv[9]={},v[9],n=0;auto add=[&](int x)->bool{for(int i=8;i>=0;i--)if((x>>i)&1){if(piv[i])x^=piv[i];else{piv[i]=x;v[n++]=idx[x];return true;}}return false;};add(mats[a]);add(mats[b]);for(int z=0;z<n;z++)for(int j=0;j<z;j++)add(mats[br[v[z]][v[j]]]);return n;}
int main(){fill(idx,idx+512,-1);int n=0; for(int x=0;x<512;x++)if(((__builtin_parity((x&1)|((x>>3)&2)|((x>>6)&4)))==0)){mats[n]=x;idx[x]=n++;}if(n!=256){cerr<<"wrong n "<<n;return 1;}for(int i=0;i<256;i++)for(int j=0;j<256;j++){int b=mul(mats[i],mats[j])^mul(mats[j],mats[i]);if(idx[b]<0){cerr<<"bracket not tracezero";return 1;}br[i][j]=idx[b];}
vector<int> gl;for(int x=0;x<512;x++)if(inv(x)>=0)gl.push_back(x);cerr<<"GL "<<gl.size()<<"\n";
int dist[9]={}, count[256]={},h[256][9]={};for(int i=0;i<256;i++)for(int j=0;j<256;j++){int d=cl(i,j);dist[d]++;h[i][d]++;if(d==8)count[i]++;}
cout<<"DIM_DIST";for(int d=0;d<=8;d++)cout<<" "<<d<<":"<<dist[d];cout<<"\n";
int seen[256]={};int classes=0;map<int,int> spectrum;
for(int i=0;i<256;i++)if(!seen[i]){vector<int> orbit;for(int g:gl){int v=mul(mul(g,mats[i]),inv(g));if(!seen[idx[v]])seen[idx[v]]=1,orbit.push_back(idx[v]);}sort(orbit.begin(),orbit.end());int mn=*min_element(orbit.begin(),orbit.end());cout<<"ORBIT "<<classes++<<" min="<<mn<<" mat="<<mats[mn]<<" size="<<orbit.size()<<" partners="<<count[i]<<" dims=";for(int d=0;d<=8;d++)cout<<h[i][d]<<",";cout<<"\n";for(int j:orbit)if(count[j]!=count[i]){cerr<<"bad conjugacy";return 1;}spectrum[count[i]]+=orbit.size();}
cout<<"PARTNER_SPECTRUM";for(auto [k,v]:spectrum)cout<<" "<<k<<":"<<v;cout<<"\n";
if(classes!=7 || dist[8]!=13440 || spectrum[0]!=50 || spectrum[56]!=24 || spectrum[64]!=126 || spectrum[72]!=56) return 2;
cout<<"VERIFY_OK\n";
return 0;}
