// Independent reverse-graph BFS for all ordered binary transition tables on five states.
#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <set>
#include <numeric>
#include <cassert>
using namespace std;
int main(){
 int ix[5][5]={}; int k=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)ix[i][j]=ix[j][i]=k++;
 unsigned long long hist[11]{}; unsigned long long failing=0; vector<pair<int,int>> extreme;
 for(int u=0;u<3125;u++)for(int v=0;v<3125;v++){
   int a[5],b[5];for(int j=0,z=u;j<5;j++,z/=5)a[j]=z%5;
   for(int j=0,z=v;j<5;j++,z/=5)b[j]=z%5;
   int back[10][20]{}; unsigned char indeg[10]{};
   int q[10],head=0,tail=0; signed char dist[10];fill(dist,dist+10,-1);
   int p=0;
   for(int i=0;i<5;i++)for(int j=i+1;j<5;j++,p++){
     int y0=a[i]==a[j]?-1:ix[a[i]][a[j]];
     int y1=b[i]==b[j]?-1:ix[b[i]][b[j]];
     if(y0<0||y1<0){dist[p]=1;q[tail++]=p;}
     if(y0>=0)back[y0][indeg[y0]++]=p;
     if(y1>=0)back[y1][indeg[y1]++]=p;
   }
   while(head<tail){int y=q[head++];for(int z=0;z<indeg[y];z++){
     int x=back[y][z];if(dist[x]<0){dist[x]=dist[y]+1;q[tail++]=x;}
   }}
   if(tail!=10){failing++;continue;}
   int radius=*max_element(dist,dist+10);
   if(radius>10){cerr<<"ERR";return 3;}
   hist[radius]++;
   if(radius==10)extreme.push_back({u,v});
 }
 cout<<"total "<<9765625<<" non "<<failing<<"\n";
 for(int d=1;d<=10;d++)cout<<d<<" "<<hist[d]<<"\n";
 cout<<"extreme_count "<<extreme.size()<<"\n";
 if(extreme.empty())return 3;
 // Verify the entire extremal list equals the full relabeling-and-letter-swap orbit.
 int a[5],b[5];for(int j=0,z=extreme[0].first;j<5;j++,z/=5)a[j]=z%5;
 for(int j=0,z=extreme[0].second;j<5;j++,z/=5)b[j]=z%5;
 int perm[5]={0,1,2,3,4};set<pair<int,int>> orbit;
 do {
   int aa[5],bb[5];for(int i=0;i<5;i++){aa[perm[i]]=perm[a[i]];bb[perm[i]]=perm[b[i]];}
   int ua=0,ub=0,mul=1;for(int j=0;j<5;j++,mul*=5){ua+=aa[j]*mul;ub+=bb[j]*mul;}
   orbit.insert({ua,ub});orbit.insert({ub,ua});
 }while(next_permutation(perm,perm+5));
 cout<<"orbit_size "<<orbit.size()<<" equal "<<(vector<pair<int,int>>(orbit.begin(),orbit.end())==extreme)<<"\n";
 if(orbit.size()!=240||vector<pair<int,int>>(orbit.begin(),orbit.end())!=extreme)return 4;
 cout<<"VERIFY_OK\n";
}
