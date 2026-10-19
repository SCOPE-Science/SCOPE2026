// Exhaustive, independent checker for complementary prisms of cycles.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify_bruteforce.cpp -o verify_bruteforce
// Run: ./verify_bruteforce > brute_certificate.tsv
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <unordered_map>
#include <queue>
#include <map>
#include <cassert>
using namespace std;
int main(){
 for(int n=5;n<=12;n++){
  int N=2*n, k=n/3+2;
  vector<uint32_t> open(N,0),closed(N,0);
  auto put=[&](int u,int v){open[u]|=1u<<v;open[v]|=1u<<u;};
  for(int i=0;i<n;i++){
   put(i,(i+1)%n);put(i,n+i);
   for(int j=i+1;j<n;j++)if((j-i)!=1 && (j-i)!=n-1)put(n+i,n+j);
  }
  for(int u=0;u<N;u++)closed[u]=open[u]|(1u<<u);
  vector<uint32_t> minsets;
  uint32_t limit=1u<<N,full=limit-1;
  for(uint32_t mask=0;mask<limit;mask++){
   int ct=__builtin_popcount(mask);
   if(ct>k)continue;
   bool independent=true;
   uint32_t vv=mask,union_closed=0;
   while(vv){int u=__builtin_ctz(vv); vv&=vv-1;
    if(open[u]&mask){independent=false;break;}
    union_closed|=closed[u];
   }
   if(!independent||union_closed!=full)continue;
   if(ct<k){fprintf(stderr,"smaller-than-predicted independent dominating set n=%d mask=%u\n",n,mask);return 2;}
   minsets.push_back(mask);
  }
  unordered_map<uint32_t,int> loc;
  for(int i=0;i<(int)minsets.size();i++)loc[minsets[i]]=i;
  int edges_jump=0,edges_slide=0;
  vector<vector<int>> slide(minsets.size()),jump(minsets.size());
  for(int i=0;i<(int)minsets.size();i++){
   uint32_t s=minsets[i], vv=s;
   while(vv){int u=__builtin_ctz(vv);vv&=vv-1;
    uint32_t outside=full&~s;
    while(outside){int w=__builtin_ctz(outside);outside&=outside-1;
     auto it=loc.find(s^(1u<<u)^(1u<<w));
     if(it!=loc.end()&&it->second>i){
      edges_jump++;jump[i].push_back(it->second);jump[it->second].push_back(i);
      if(open[u]&(1u<<w)){
       edges_slide++;slide[i].push_back(it->second);slide[it->second].push_back(i);
      }
     }
    }
   }
  }
  auto components=[&](const vector<vector<int>>& adj){
   vector<int> seen(minsets.size(),0);map<int,int> c;
   for(int i=0;i<(int)minsets.size();i++)if(!seen[i]){
    queue<int> q;seen[i]=1;q.push(i);int z=0;
    while(!q.empty()){int v=q.front();q.pop();z++;for(int w:adj[v])if(!seen[w]){seen[w]=1;q.push(w);}}
    c[z]++;
   }
   return c;
  };
  auto a=components(slide),b=components(jump);
  int expected=(n%3==2)?2*n:((n%3==0)?n*(n/3)*(n/3):n*(2*(n/3)+1));
  if((int)minsets.size()!=expected){fprintf(stderr,"bad count n=%d\n",n);return 3;}
  if((n%3==2 && (edges_jump||edges_slide)) || (n%3!=2 && (a.size()!=1||a.begin()->first!=expected))){
    fprintf(stderr,"bad mobility n=%d\n",n);return 4;
  }
  printf("SUMMARY\t%d\t%d\t%zu\t%d\t%d\t",n,k,minsets.size(),edges_jump,edges_slide);
  for(auto x:a)printf("S%d:%d,",x.first,x.second);
  printf("\t");for(auto x:b)printf("J%d:%d,",x.first,x.second);printf("\n");
  for(uint32_t s:minsets)printf("SET\t%d\t%u\n",n,s);
 }
}
