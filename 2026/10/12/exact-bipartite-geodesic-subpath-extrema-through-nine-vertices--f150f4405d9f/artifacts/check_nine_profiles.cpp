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
int main(){int a=4,b=5;map<string,pair<int,uint64_t>> types;
for(uint64_t mask=0;mask<(1ull<<(a*b));mask++){
 if(gpn(a,b,mask)!=105)continue;
 vector<int> ar(a),br(b);int m=0;
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(!(mask>>(i*b+j)&1)){m++;ar[i]++;br[j]++;}
 sort(ar.begin(),ar.end());sort(br.begin(),br.end());
 string s=to_string(m)+" | ";for(int x:ar)s+=to_string(x);s+=" | ";for(int x:br)s+=to_string(x);
 types[s].first++;
 if(!types[s].second)types[s].second=mask;
}
for(auto [s,p]:types)cout<<s<<" | count="<<p.first<<" | mask="<<p.second<<"\n";
}