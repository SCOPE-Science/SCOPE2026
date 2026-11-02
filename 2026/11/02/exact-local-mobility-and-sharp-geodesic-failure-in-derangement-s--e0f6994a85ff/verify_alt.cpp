// Independent combinatorial census for the derangement switch graph.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
using Perm=vector<int>;
long long choose(int n,int k){long long a=1;for(int i=1;i<=k;i++)a=a*(n-i+1)/i;return a;}
int cyclecount(const Perm& p){int n=p.size(),cnt=0; vector<int> used(n);for(int i=0;i<n;i++)if(!used[i]){cnt++;int j=i;while(!used[j]){used[j]=1;j=p[j];}}return cnt;}
int transpositions(const Perm& p){int n=p.size();vector<int> seen(n);int c=0;for(int i=0;i<n;i++)if(!seen[i]){int j=i,l=0;while(!seen[j]){seen[j]=1;j=p[j];l++;}if(l==2)c++;}return c;}
int baseline(const Perm& a,const Perm& b){int n=a.size();Perm inv(n),r(n);for(int i=0;i<n;i++)inv[b[i]]=i;for(int i=0;i<n;i++)r[i]=inv[a[i]];return n-cyclecount(r);}
vector<int> bfs(const vector<vector<int>>& g,int s){vector<int> d(g.size(),-1);d[s]=0;queue<int> q;q.push(s);while(!q.empty()){int x=q.front();q.pop();for(int y:g[x])if(d[y]<0){d[y]=d[x]+1;q.push(y);}}return d;}
int main(){
 for(int n=3;n<=8;n++){
  Perm p(n);iota(p.begin(),p.end(),0);vector<Perm> ss;
  do{bool valid=true;for(int i=0;i<n;i++)if(p[i]==i){valid=false;break;}if(valid)ss.push_back(p);}while(next_permutation(p.begin(),p.end()));
  map<Perm,int> idx;for(int i=0;i<(int)ss.size();i++)idx[ss[i]]=i;
  vector<vector<int>> g(ss.size());map<int,int> degrees;long long ends=0;
  for(int s=0;s<(int)ss.size();s++){
   auto a=ss[s];
   // A 4-cycle switch is legal exactly when both cross edges avoid the forbidden diagonal.
   for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(a[j]!=i && a[i]!=j){
     Perm b=a;swap(b[i],b[j]);auto it=idx.find(b);assert(it!=idx.end());g[s].push_back(it->second);
   }
   int illegal=n-transpositions(a);
   assert((int)g[s].size()==n*(n-1)/2-illegal);
   degrees[g[s].size()]++;ends+=g[s].size();
  }
  for(int s=0;s<(int)ss.size();s++)for(int t:g[s]){auto &v=g[t];assert(find(v.begin(),v.end(),s)!=v.end());}
  long long edges=ends/2;
  vector<int> d=bfs(g,0);
  if(n==3){assert(ss.size()==2 && edges==0);}else assert(find(d.begin(),d.end(),-1)==d.end());
  if(n==4){for(int s=0;s<(int)ss.size();s++){d=bfs(g,s);for(int t=0;t<(int)ss.size();t++)assert(d[t]==baseline(ss[s],ss[t]));}}
  if(n==5 || n==6){Perm a,b;if(n==5){a={1,0,3,4,2};b={1,0,4,2,3};}
    else{a={1,2,0,4,5,3};b={2,0,1,4,5,3};}
    d=bfs(g,idx.at(a));assert(baseline(a,b)==2 && d[idx.at(b)]==4);
  }
  cout << "ALTERNATIVE_OK n="<<n<<" states="<<ss.size()<<" edges="<<edges<<" degree_classes="<<degrees.size()<<"\n";
 }
 cout<<"ALTERNATIVE_COMPLETE_OK\n";
}
