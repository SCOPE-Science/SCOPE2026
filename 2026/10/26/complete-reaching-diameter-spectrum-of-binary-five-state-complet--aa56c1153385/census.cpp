#include <bits/stdc++.h>
using namespace std;
int main(){
 const int N=3125,Q=31;
 uint8_t tr[N][32], tab[N][5];
 for(int x=0;x<N;x++){
  int z=x; for(int i=0;i<5;i++){tab[x][i]=z%5; z/=5;}
  for(int s=1;s<=31;s++){int m=0;for(int i=0;i<5;i++)if(s>>i&1)m|=1<<tab[x][i];tr[x][s]=m;}
 }
 long long full=0, total=1LL*N*N;
 long long hist[32]={}, reachcount[32]={},reset[32]={};
 long long bymax[32][32]={}, maxper[6][32]={};
 vector<pair<int,int>> ex;
 int maxdist=-1;
 int dist[32], queue[32];
 for(int a=0;a<N;a++)for(int b=0;b<N;b++){
  for(int s=0;s<=31;s++)dist[s]=-1;
  int head=0,tail=1;queue[0]=31;dist[31]=0;
  int mxsz[6]={};
  while(head<tail){int s=queue[head++];int t=tr[a][s];if(dist[t]<0){dist[t]=dist[s]+1;queue[tail++]=t;}t=tr[b][s];if(dist[t]<0){dist[t]=dist[s]+1;queue[tail++]=t;}}
  reachcount[tail]++;
  if(tail!=31)continue;
  full++;
  int m=0,r=999;
  for(int s=1;s<=31;s++){
   m=max(m,dist[s]);
   int k=__builtin_popcount((unsigned)s);
   mxsz[k]=max(mxsz[k],dist[s]);
   if(k==1)r=min(r,dist[s]);
  }
  hist[m]++;
  reset[r]++;
  bymax[m][r]++;
  for(int k=1;k<=4;k++)maxper[k][mxsz[k]]++;
  if(m>maxdist){maxdist=m;ex.clear();}
  if(m==maxdist)ex.push_back({a,b});
 }
 cerr<<"Total "<<total<<" completely reachable "<<full<<" max "<<maxdist<<" extremizers "<<ex.size()<<"\n";
 cout<<"reach_count\n";for(int k=1;k<=31;k++)if(reachcount[k])cout<<k<<":"<<reachcount[k]<<" ";cout<<"\n";
 cout<<"diameter\n";for(int k=0;k<=31;k++)if(hist[k])cout<<k<<":"<<hist[k]<<" ";cout<<"\n";
 cout<<"reset\n";for(int k=0;k<=31;k++)if(reset[k])cout<<k<<":"<<reset[k]<<" ";cout<<"\n";
 for(int s=1;s<=4;s++){cout<<"maximum minimum reaching length size "<<s<<"\n";for(int k=0;k<=31;k++)if(maxper[s][k])cout<<k<<":"<<maxper[s][k]<<" ";cout<<"\n";}
 cout<<"joint diameter/reset\n";for(int m=0;m<=31;m++)for(int r=0;r<=31;r++)if(bymax[m][r])cout<<m<<","<<r<<":"<<bymax[m][r]<<" ";cout<<"\n";
 cout<<"extremizers\n";for(auto [a,b]:ex)cout<<a<<","<<b<<" ";cout<<"\n";
}
