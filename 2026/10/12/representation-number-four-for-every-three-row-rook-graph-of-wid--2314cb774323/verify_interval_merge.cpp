#include <bits/stdc++.h>
using namespace std;
using Gap=array<vector<unsigned char>,12>;
vector<Gap> patterns; int cur[24], piB[4],locA[4][3],locB[4][3];
bool alt(const int a[3],const int b[3]) {int t[6];for(int i=0;i<3;i++)t[i]=a[i],t[i+3]=b[i];sort(t,t+6);for(int i=1;i<6;i++){bool p=false,q=false;for(int j=0;j<3;j++){p|=t[i-1]==a[j];q|=t[i]==a[j];}if(p==q)return false;}return true;}
void build(int a,int b){if(a==12&&b==12){int x=0,y=0;for(int i=0;i<24;i++){int t=cur[i];if(t<4)locA[t][x++/4]=i;else locB[t-4][y++/4]=i;}for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(alt(locA[i],locB[j]) != (i==j))return;Gap gp;int g=-1;for(int i=0;i<24;i++){if(cur[i]<4)g++;else gp[g].push_back((unsigned char)(cur[i]-4));}patterns.push_back(move(gp));return;}if(a<12){cur[a+b]=a%4;build(a+1,b);}if(b<12){cur[a+b]=4+piB[b%4];build(a,b+1);}}
uint64_t leaves=0, pairs=0, totalPossible=0;
unsigned char cc[24]; bool found=false;Gap *BB,*CC; vector<unsigned char> output;
bool check(){int pB[4][3],pC[4][3];int nb[4]={},nc[4]={};for(int i=0;i<24;i++){int v=output[i];if(v<4)pB[v][nb[v]++]=i;else pC[v-4][nc[v-4]++]=i;}for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(alt(pB[i],pC[j])!=(i==j))return false;return true;}
void weave(int gap);
void mergegap(int gap,int ib,int ic){auto &b=(*BB)[gap],&c=(*CC)[gap];if(ib==(int)b.size()&&ic==(int)c.size()){weave(gap+1);return;}if(ib<(int)b.size()){output.push_back(b[ib]);mergegap(gap,ib+1,ic);output.pop_back();if(found)return;}if(ic<(int)c.size()){output.push_back(c[ic]+4);mergegap(gap,ib,ic+1);output.pop_back();}}
void weave(int gap){if(found)return;if(gap==12){leaves++;if(check()){found=true;cerr<<"FOUND: ";for(auto x:output)cerr<<(int)x<<" ";cerr<<"\n";}return;}mergegap(gap,0,0);}
int main(){int pp[4]={0,1,2,3};do{for(int i=0;i<4;i++)piB[i]=pp[i];cur[0]=0;build(1,0);}while(next_permutation(pp,pp+4));cerr<<"pair patterns "<<patterns.size()<<"\n";for(auto &b:patterns){BB=&b;for(auto &c:patterns){CC=&c;pairs++;output.clear();weave(0);if(found)break;}if(found)break;}cerr<<"pairs "<<pairs<<" leaves "<<leaves<<" found "<<found<<"\n";}
