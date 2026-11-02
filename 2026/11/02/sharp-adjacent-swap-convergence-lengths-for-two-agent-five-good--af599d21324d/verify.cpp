#include <bits/stdc++.h>
using namespace std;
struct E {int to; int player; int gain,loss;};
int main(){
 const int m=5, S=120,N=S*S;
 vector<array<int,m>> perm;array<int,m> p; iota(p.begin(),p.end(),0);do perm.push_back(p);while(next_permutation(p.begin(),p.end()));
 map<array<int,m>,int> ind;for(int i=0;i<S;i++)ind[perm[i]]=i;
 vector<array<int,m-1>>adj(S);for(int i=0;i<S;i++)for(int k=0;k<m-1;k++){auto z=perm[i];swap(z[k],z[k+1]);adj[i][k]=ind[z];}
 vector<int>mask(N);for(int i=0;i<S;i++)for(int j=0;j<S;j++){
  int available=(1<<m)-1,got=0;
  for(int t=0;t<m;t++){
   auto &arr=(t%2==0?perm[i]:perm[j]);int x=-1;
   for(int g:arr)if(available>>g&1){x=g;break;}
   if(t%2==0)got|=1<<x;
   available&=~(1<<x);
  }
  mask[i*S+j]=got;
 }
 vector<vector<E>>edge(N);long long changeCount=0,zeroCount=0,multichange=0;
 for(int i=0;i<S;i++)for(int j=0;j<S;j++){
  int st=i*S+j,a=mask[st];
  for(int k=0;k<m-1;k++)for(int player=0;player<2;player++){
   int to=player==0?adj[i][k]*S+j:i*S+adj[j][k];int b=mask[to];
   int gain=player==0?(b&~a):(a&~b);
   int loss=player==0?(a&~b):(b&~a);
   if(!gain){zeroCount++;continue;}
   if(__builtin_popcount((unsigned)gain)!=1 || __builtin_popcount((unsigned)loss)!=1)multichange++;
   int g=__builtin_ctz((unsigned)gain),l=__builtin_ctz((unsigned)loss);
   edge[st].push_back({to,player,g,l});changeCount++;
  }
 }
 cout<<"N="<<N<<" transitions_zero="<<zeroCount<<" transitions_one_swap="<<changeCount<<" transitions_multiple="<<multichange<<"\n";
 if(multichange)return 2;
 long long activeEdges=0;int bestAll=0,bestTruth=0,bestQAll=-1,bestQTruth=-1,bestSrc=-1;long long cycleCount=0;
 vector<int> bestTruthPath,bestGlobalPath;long long sumLongestTruth=0;
 for(int q=0;q<S;q++){
  int rank2[m];for(int k=0;k<m;k++)rank2[perm[q][k]]=k;
  vector<char>color(N,0);vector<int>dp(N,-1), nxt(N,-1);bool cycle=false;
  function<int(int)>dfs=[&](int st)->int{
   if(color[st]==1){cycle=true;return 0;}
   if(color[st]==2)return dp[st];
   color[st]=1;int longest=0,toBest=-1;
   for(const E&e:edge[st]){
    bool gain=e.player==0?(e.gain<e.loss):(rank2[e.gain]<rank2[e.loss]);
    if(!gain)continue;
    activeEdges++;
    int length=1+dfs(e.to);
    if(length>longest){longest=length;toBest=e.to;}
   }
   color[st]=2;nxt[st]=toBest;return dp[st]=longest;
  };
  int qmax=0,src=-1;
  for(int st=0;st<N;st++){
   int len=dfs(st);
   if(len>qmax){qmax=len;src=st;}
  }
  if(cycle){cycleCount++;cerr<<"cycle for true ranking 2="<<q<<"\n";}
  int truthSt=q;int truthLen=dp[truthSt];sumLongestTruth+=truthLen;
  if(qmax>bestAll){bestAll=qmax;bestQAll=q;bestSrc=src;bestGlobalPath.clear();for(int st=src;st>=0;st=nxt[st])bestGlobalPath.push_back(st);}
  if(truthLen>bestTruth){bestTruth=truthLen;bestQTruth=q;bestTruthPath.clear();for(int st=truthSt;st>=0;st=nxt[st])bestTruthPath.push_back(st);}
  if(q%20==0)cerr<<"q="<<q<<" max_global="<<qmax<<" max_truth="<<truthLen<<"\n";
 }
 cout<<"true_ranking_profiles="<<S<<" cycles="<<cycleCount<<" best_all="<<bestAll<<" best_from_truth="<<bestTruth<<" sum_longest_truth="<<sumLongestTruth<<" active_edges_total="<<activeEdges<<"\n";
 cout<<"best_truth2_global_index="<<bestQAll<<" ranking=";for(int g:perm[bestQAll])cout<<g;cout<<" start="<<bestSrc<<"\n";
 cout<<"best_truth2_truth_index="<<bestQTruth<<" ranking=";for(int g:perm[bestQTruth])cout<<g;cout<<"\n";
 for(auto [name,seq]:vector<pair<string,vector<int>>>{{"global",bestGlobalPath},{"truth",bestTruthPath}}){
  cout<<"witness="<<name<<" len="<<seq.size()-1<<"\n";
  for(int st:seq){cout<<st<<" ";for(int g:perm[st/S])cout<<g;cout<<"/";for(int g:perm[st%S])cout<<g;cout<<" m1="<<mask[st]<<"\n";}
 }
}
