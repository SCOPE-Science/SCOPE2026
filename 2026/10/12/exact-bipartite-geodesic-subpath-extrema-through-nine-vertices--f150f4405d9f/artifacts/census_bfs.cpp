#include <bits/stdc++.h>
using namespace std;
struct Result {long long maxv=-1,count=0,connected=0,mask=0;};
long long gpn(int a,int b,uint64_t mask){
 int n=a+b;uint32_t adj[12]={0};
 int q=0;
 for(int i=0;i<a;i++)for(int j=0;j<b;j++,q++)if(mask>>q&1){adj[i]|=1u<<(a+j);adj[a+j]|=1u<<i;}
 for(int i=0;i<n;i++)if(!adj[i])return -1;
 long long answer=n;
 for(int s=0;s<n;s++){
  int dist[12],ways[12];fill(dist,dist+n,-1);fill(ways,ways+n,0);
  int queue[12],front=0,back=0;
  queue[back++]=s;dist[s]=0;ways[s]=1;
  while(front<back){int x=queue[front++];
   uint32_t todo=adj[x];
   while(todo){int y=__builtin_ctz(todo);todo&=todo-1;
    if(dist[y]<0){dist[y]=dist[x]+1;queue[back++]=y;}
    if(dist[y]==dist[x]+1)ways[y]+=ways[x];
   }
  }
  if(back!=n)return -1;
  for(int v=s+1;v<n;v++)answer+=ways[v];
 }
 return answer;
}
int main(int argc,char**argv){
 for(int n=5;n<=9;n++){
  long long best=-1;int ba=0,bb=0;uint64_t bm=0;
  map<pair<int,int>,Result> stats;
  for(int a=1;a<=n/2;a++){
   int b=n-a,ed=a*b;
   auto &r=stats[{a,b}];
   for(uint64_t mask=0;mask<(1ull<<ed);mask++){
    long long k=gpn(a,b,mask);
    if(k<0)continue;
    r.connected++;
    if(k>r.maxv){r.maxv=k;r.count=1;r.mask=mask;}
    else if(k==r.maxv)r.count++;
    if(k>best){best=k;ba=a;bb=b;bm=mask;}
   }
  }
  cout<<"n "<<n<<" overall_best "<<best<<" witness_shores "<<ba<<","<<bb<<" witness_mask "<<bm<<"\n";
  for(auto [ab,r]:stats){cout<<" shores "<<ab.first<<","<<ab.second<<" best "<<r.maxv<<" labelled_bipartition_maximizers "<<r.count<<" connected_labeled_bipartition_graphs "<<r.connected<<" representative_mask "<<r.mask<<"\n";}
 }
}
