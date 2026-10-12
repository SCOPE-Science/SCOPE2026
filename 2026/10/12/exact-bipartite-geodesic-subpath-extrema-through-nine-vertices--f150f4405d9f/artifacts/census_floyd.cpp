#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int geodesics(int a,int b,uint32_t mask){
 const int n=a+b,inf=99;
 int dist[9][9];
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)dist[i][j]=(i==j?0:inf);
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(mask&(1u<<(i*b+j)))dist[i][a+j]=dist[a+j][i]=1;
 for(int k=0;k<n;k++)for(int i=0;i<n;i++)for(int j=0;j<n;j++)dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(dist[i][j]==inf)return -1;
 int total=n;
 for(int s=0;s<n;s++){
  int counts[9]={};counts[s]=1;
  for(int depth=0;depth<n;depth++)for(int u=0;u<n;u++)if(dist[s][u]==depth){
   for(int v=0;v<n;v++)if(dist[u][v]==1 && dist[s][v]==depth+1)counts[v]+=counts[u];
  }
  for(int v=s+1;v<n;v++)total+=counts[v];
 }
 return total;
}
string missing_profile(int a,int b,uint32_t mask){
 vector<int> dx(a),dy(b);int e=0;
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(!(mask&(1u<<(i*b+j)))){e++;dx[i]++;dy[j]++;}
 sort(dx.begin(),dx.end());sort(dy.begin(),dy.end());
 string s=to_string(e)+":";for(int v:dx)s+=char('0'+v);
 s+=':';for(int v:dy)s+=char('0'+v);
 return s;
}
int main(){
 for(int n=5;n<=9;n++){
  int global=-1,global_count=0;
  map<string,int> best_profiles;
  for(int a=1;a<=n/2;a++){
   int b=n-a,best=-1,cnt=0;
   for(uint32_t mask=0;mask<(1u<<(a*b));mask++){
    int val=geodesics(a,b,mask);
    if(val>best){best=val;cnt=1;}
    else if(val==best)cnt++;
   }
   if(best>global){global=best;global_count=0;best_profiles.clear();}
   if(best==global){
    for(uint32_t mask=0;mask<(1u<<(a*b));mask++){
     if(geodesics(a,b,mask)==global){best_profiles[to_string(a)+","+to_string(b)+"/"+missing_profile(a,b,mask)]++;global_count++;}
    }
   }
   cout<<"n="<<n<<" shores="<<a<<","<<b<<" max="<<best<<" count="<<cnt<<"\n";
  }
  cout<<"n="<<n<<" GLOBAL="<<global<<" count="<<global_count<<"\n";
  for(auto &entry:best_profiles)cout<<" TYPE "<<entry.first<<" count="<<entry.second<<"\n";
 }
}
