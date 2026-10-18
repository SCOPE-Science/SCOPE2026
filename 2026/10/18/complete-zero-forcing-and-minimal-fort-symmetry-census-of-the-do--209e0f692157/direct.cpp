#include <bits/stdc++.h>
using namespace std;
static const int N=20, LIM=1<<N;
int nb[N];
int degree(int m){return __builtin_popcount((unsigned)m);}
int force(int black){int rounds=0; while(true){ if(black==LIM-1)return rounds; int additions=0;for(int v=0;v<N;v++)if(black>>v&1){int w=nb[v]&~black; if(w&&(w&(w-1))==0)additions|=w;} if(!additions)return -1; black|=additions;rounds++;}}
int main(){for(int i=0;i<10;i++){int u=i,v=i+10;int k=(i+1)%10; nb[u]|=1<<k;nb[k]|=1<<u;nb[u]|=1<<v;nb[v]|=1<<u;int j=(i+2)%10+10;nb[v]|=1<<j;nb[j]|=1<<v;} int cnt[N+1]={},mini[N+1]={},rt[N+1]={};vector<int> good(LIM);vector<int> minima; int first[N+1];fill(begin(first),end(first),-1);for(int m=0;m<LIM;m++){int t=force(m);if(t<0)continue;good[m]=1;int k=degree(m);cnt[k]++; if(first[k]<0)first[k]=m;if(k==6||k==7||k==8)rt[t]++;}
int totalminimal=0;for(int m=0;m<LIM;m++)if(good[m]){bool minimal=true;for(int v=0;v<N;v++)if(m>>v&1)if(good[m^(1<<v)]){minimal=false;break;}if(minimal){mini[degree(m)]++;totalminimal++;minima.push_back(m);}}
cout<<"DIRECT_N=20 edges=30 verified_degrees=";for(int v=0;v<N;v++)if(degree(nb[v])!=3){cout<<"FAIL";return 2;}cout<<"3x20\n";
cout<<"FORCING_POLYNOMIAL=";for(int k=0;k<=20;k++)if(cnt[k])cout<<k<<":"<<cnt[k]<<",";cout<<"\nMINIMAL_COUNTS=";for(int k=0;k<=20;k++)if(mini[k])cout<<k<<":"<<mini[k]<<",";cout<<"\n";cout<<"minimum_witness="<<first[find_if(begin(cnt),end(cnt),[](int n){return n>0;})-begin(cnt)]<<"\n";
int k0=find_if(begin(cnt),end(cnt),[](int n){return n>0;})-begin(cnt);cout<<"minimum="<<k0<<" rt=";int rdist[20]={};for(int m=0;m<LIM;m++)if(good[m]&&degree(m)==k0){int t=force(m);rdist[t]++;}for(int j=0;j<20;j++)if(rdist[j])cout<<j<<":"<<rdist[j]<<",";cout<<"\n";
FILE *f=fopen("direct_status.bin","wb");fwrite(good.data(),sizeof(int),LIM,f);fclose(f);
f=fopen("minimal_masks.txt","w");for(int m:minima)fprintf(f,"%d\n",m);fclose(f);
return 0;}
