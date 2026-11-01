#include <bits/stdc++.h>
using namespace std;
int main(){const int n=12;
int edges[][2]={{0,1},{0,5},{0,7},{0,8},{0,11},{1,2},{1,5},{1,6},{1,8},{2,3},{2,6},{2,8},{2,9},{3,4},{3,6},{3,9},{3,10},{4,5},{4,6},{4,10},{4,11},{5,6},{5,11},{7,8},{7,9},{7,10},{7,11},{8,9},{9,10},{10,11}};
int adj[12][12]{};for(auto &e:edges)adj[e[0]][e[1]]=adj[e[1]][e[0]]=1;
int pow3[13];pow3[0]=1;for(int j=1;j<=12;j++)pow3[j]=pow3[j-1]*3;
int M=pow3[12]; vector<int> nxt(M),indeg(M),entry(M,-1),kind(M,0),cycId(M,-1);int x[12];
for(int s=0;s<M;s++){
 int v=s;for(int j=0;j<12;j++){x[j]=v%3;v/=3;}
 int out=0;
 for(int j=0;j<12;j++){
  int y=x[j];if(y!=0)y=(y+1)%3;else {for(int k=0;k<12;k++)if(adj[j][k]&&x[k]==1){y=1;break;}}
  out+=y*pow3[j];
 }
 nxt[s]=out; indeg[out]++;
}
queue<int> q;for(int s=0;s<M;s++)if(!indeg[s])q.push(s);
vector<int> seq;seq.reserve(M);while(!q.empty()){int s=q.front();q.pop();seq.push_back(s);if(!--indeg[nxt[s]])q.push(nxt[s]);}
map<int,int> orbits;vector<int> cycLength,cycReps,cycleNstates;int cid=0;for(int s=0;s<M;s++) if(indeg[s]>0&&cycId[s]<0){int cur=s,len=0;do{cycId[cur]=cid;entry[cur]=0;cur=nxt[cur];len++;}while(cur!=s);cycLength.push_back(len);cycReps.push_back(s);orbits[len]++;cid++;}
for(int j=(int)seq.size()-1;j>=0;j--){int s=seq[j];entry[s]=entry[nxt[s]]+1;cycId[s]=cycId[nxt[s]];}
map<pair<int,int>,long long> hist;int maxe=0;vector<long long> basins(cid);for(int s=0;s<M;s++){hist[{cycLength[cycId[s]],entry[s]}]++;basins[cycId[s]]++;maxe=max(maxe,entry[s]);}
map<int,map<int,long long>> basinbylen;for(int i=0;i<cid;i++)basinbylen[cycLength[i]][basins[i]]++;
cout<<"M "<<M<<" cycles "<<cid<<" max_entry "<<maxe<<"\n";
cout<<"orbits";for(auto [l,c]:orbits)cout<<" "<<l<<":"<<c;cout<<"\n";
cout<<"hist period entry count\n";for(auto [pe,c]:hist)cout<<pe.first<<" "<<pe.second<<" "<<c<<"\n";
cout<<"basin_sizes length size count\n";for(auto [len,dist]:basinbylen)for(auto [bs,c]:dist)cout<<len<<" "<<bs<<" "<<c<<"\n";
cout<<"reps period state\n";for(int i=0;i<cid;i++)cout<<cycLength[i]<<" "<<cycReps[i]<<"\n";
}
