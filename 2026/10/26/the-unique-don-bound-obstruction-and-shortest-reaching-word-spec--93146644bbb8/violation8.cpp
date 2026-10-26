#include <bits/stdc++.h>
using namespace std;
int main(){const int n=8,U=256,F=255;int rot[U],sz[U];for(int s=0;s<U;s++){rot[s]=((s<<1)&255)|(s>>7);sz[s]=__builtin_popcount((unsigned)s);} unsigned char bmap[U],dist[U],q[U];int f[8];long long hist_count[29]={},hist_m[29]={},viol=0;map<int,int> pairs,viol_subset, max6freq, fixed,indeg, orbit_counter;
 vector<pair<unsigned long long,int>> records;
 for(int id=0;id<16777216;id++){
  int code=id, im=0;
  for(int i=0;i<8;i++){f[i]=code&7;code>>=3;im|=1<<f[i];}
  if(__builtin_popcount((unsigned)im)!=7)continue;
  bmap[0]=0;for(int s=1;s<U;s++){int p=__builtin_ctz((unsigned)s);bmap[s]=bmap[s&(s-1)]|(1<<f[p]);}
  memset(dist,255,sizeof(dist));int h=0,t=1;q[0]=255;dist[255]=0;
  while(h<t){int s=q[h++];int a=rot[s],b=bmap[s];if(dist[a]==255){dist[a]=dist[s]+1;q[t++]=a;}if(dist[b]==255){dist[b]=dist[s]+1;q[t++]=b;}}
  if(t!=255)continue;
  int bad=0,max6=0,badm=0,exmask=0;
  for(int s=1;s<F;s++)if(sz[s]==6){max6=max(max6,int(dist[s]));if(dist[s]>16){bad++;exmask=s;}}
  max6freq[max6]++;
  if(bad){viol++;pairs[bad]++;viol_subset[exmask]++;int fix=0;for(int i=0;i<8;i++)fix+=(f[i]==i);fixed[fix]++;records.push_back({id,exmask});}
 }
 cout<<"violating "<<viol<<"\n";for(auto [a,b]:pairs)cout<<"number hard subsets "<<a<<" count "<<b<<"\n";for(auto [a,b]:viol_subset)cout<<"hard subset "<<a<<" count "<<b<<"\n";for(auto [a,b]:fixed)cout<<"fixed points "<<a<<" count "<<b<<"\n";
 cout<<"REPS:\n";
 set<int> codes;
 for(auto [code, mask]:records)codes.insert((int)code);
 auto shiftcode=[](int code){int f[8];for(int i=0;i<8;i++){f[i]=code&7;code>>=3;}int res=0;for(int i=0;i<8;i++){int j=(i+1)&7;res|=((f[i]+1)&7)<<(3*j);}return res;};
 for(auto [code,mask]:records){int v=(int)code,mn=v;for(int j=0;j<8;j++){mn=min(mn,v);v=shiftcode(v);}if(mn==(int)code){cout<<code<<" "<<mask<<" ";int x=code;for(int j=0;j<8;j++){if(j)cout<<",";cout<<(x&7);x>>=3;}cout<<"\n";}}
}
