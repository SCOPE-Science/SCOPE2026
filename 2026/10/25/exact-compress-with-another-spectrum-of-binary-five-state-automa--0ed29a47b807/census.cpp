#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <array>
#include <cstdint>
using namespace std;
static int n, np, pairs[64][2], pairid[10][10];
static long long total=0,strong=0,sync=0,hist[80]={0},exthist[80]={0};
static vector<unsigned long long> extremals;
inline int maxcomp(const int *a, const int *b, int &strongConn, int &synchronizing){
  // Strong-connectivity via graph reachability from each state; for 2 outgoing letters.
  strongConn=1;
  for(int src=0;src<n;src++) {
    int seen=1<<src, old=0;
    while (old!=seen){old=seen;for(int x=0;x<n;x++) if(seen&(1<<x)) seen|=(1<<a[x])|(1<<b[x]);}
    if(seen != (1<<n)-1){strongConn=0;break;}
  }
  // shortest pair-merging distance using reverse BFS, ALL n singleton pairs as terminal (distance 0)
  // each unordered distinct pair precompute forward successors; terminal successor = -1
  int f[64][2],d[64],que[64],hd=0,tl=0;
  for(int i=0;i<np;i++){
    for(int c=0;c<2;c++){
      int x=c?b[pairs[i][0]]:a[pairs[i][0]], y=c?b[pairs[i][1]]:a[pairs[i][1]];
      f[i][c]=(x==y)?-1:pairid[x][y];
    }
    d[i]=-1;
  }
  // initial distances 1 if direct merges, BFS preimage edges to infer shortest distances
  for(int i=0;i<np;i++) if(f[i][0]<0 || f[i][1]<0){d[i]=1;que[tl++]=i;}
  while(hd<tl){int t=que[hd++];for(int j=0;j<np;j++)if(d[j]<0 && (f[j][0]==t||f[j][1]==t)){d[j]=d[t]+1;que[tl++]=j;}}
  if(tl<np){synchronizing=0;return -1;}
  synchronizing=1;
  int threshold=0;
  for(int i=0;i<n;i++){
    int mi=100000;
    for(int j=0;j<n;j++)if(i!=j)mi=min(mi,d[pairid[i][j]]);
    threshold=max(threshold,mi);
    exthist[mi]++;
  }
  return threshold;
}
int main(int argc,char**argv){
 if(argc<2){fprintf(stderr,"usage: census n\n");return 1;} n=atoi(argv[1]);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)pairid[i][j]=-1;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){pairid[i][j]=pairid[j][i]=np;pairs[np][0]=i;pairs[np][1]=j;np++;}
 unsigned long long limit=1;for(int i=0;i<2*n;i++)limit*=n;
 int a[10],b[10]; int maxval=0;
 for(unsigned long long code=0;code<limit;code++){
   unsigned long long m=code;
   for(int i=0;i<n;i++){a[i]=m%n;m/=n;}
   for(int i=0;i<n;i++){b[i]=m%n;m/=n;}
   int strongConn=0,synchronizing=0;
   int v=maxcomp(a,b,strongConn,synchronizing);total++;
   if(strongConn)strong++;
   if(synchronizing){sync++;hist[v]++;if (v>maxval){maxval=v; extremals.clear();} if(v==maxval)extremals.push_back(code); }
 }
 printf("n=%d total=%lld strong=%lld synchronizing=%lld max=%d extremal=%zu\n",n,total,strong,sync,maxval,extremals.size());
 for(int i=0;i<=maxval;i++)if(hist[i])printf("automaton_tau_%d=%lld\n",i,hist[i]);
 for(int i=0;i<=40;i++)if(exthist[i])printf("state_tau_%d=%lld\n",i,exthist[i]);
 // orbit classification through full state relabeling + letter swapping; only among maximizers.
 if(extremals.size()<1000000){
    vector<unsigned long long> canonical;
    int p[10]; for(int i=0;i<n;i++)p[i]=i;
    for(auto code:extremals){
      unsigned long long m=code;for(int i=0;i<n;i++){a[i]=m%n;m/=n;}for(int i=0;i<n;i++){b[i]=m%n;m/=n;}
      unsigned long long best=code;
      do {
        int inv[10]; for(int i=0;i<n;i++)inv[p[i]]=i;
        for(int s=0;s<=1;s++){
          unsigned long long cur=0,t=1;
          for(int letter=0;letter<2;letter++)for(int i=0;i<n;i++){
            int source=(letter^s)?b[inv[i]]:a[inv[i]];
            cur+=(unsigned long long)p[source]*t; t*=n;
          }
          best=min(best,cur);
        }
      } while(next_permutation(p,p+n));
      canonical.push_back(best);
    }
    sort(canonical.begin(),canonical.end());
    for(int i=0,j;i<(int)canonical.size();i=j){j=i+1;while(j<(int)canonical.size()&&canonical[j]==canonical[i])j++;printf("class code=%llu labeled_orbit=%d\n",canonical[i],j-i);}
  }
 return 0;
}
