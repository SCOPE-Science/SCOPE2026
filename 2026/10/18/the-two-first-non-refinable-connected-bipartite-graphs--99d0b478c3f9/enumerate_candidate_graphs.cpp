// Exhaustive connected simple bipartite incidence matrices through ten vertices.
// Canonicalization uses every row permutation and sorted column signatures.
// Only colour classes that are not manifest twin-orbits require exact orbit tests.
#include <bits/stdc++.h>
using namespace std;
int a,b,n; int rows[10]; long long tot=0, conn=0, cand=0, uniq=0; unordered_set<unsigned int> seen, allseen; ofstream fout, foutall;
int popcnt(int x){return __builtin_popcount((unsigned)x);}
bool connected(){int mask=1,old=0;while(mask!=old){old=mask; for(int i=0;i<a;i++)if(mask&(1<<i))for(int j=0;j<b;j++)if(rows[i]&(1<<j))mask|=1<<(a+j);for(int j=0;j<b;j++)if(mask&(1<<(a+j)))for(int i=0;i<a;i++)if(rows[i]&(1<<j))mask|=1<<i;}return mask==(1<<n)-1;}
bool non_twin_color(){int color[10]={};int csize=1;for(int rr=0;rr<n;rr++){vector<array<int,11>> ss(n); for(int i=0;i<n;i++){auto &s=ss[i];s.fill(0);s[0]=color[i]+1;if(i<a){for(int j=0;j<b;j++)if(rows[i]&(1<<j))s[color[a+j]+1]++;}else{for(int j=0;j<a;j++)if(rows[j]&(1<<(i-a)))s[color[j]+1]++;}}
 auto uniqs=ss;sort(uniqs.begin(),uniqs.end());uniqs.erase(unique(uniqs.begin(),uniqs.end()),uniqs.end());int cc[10];for(int i=0;i<n;i++)cc[i]=lower_bound(uniqs.begin(),uniqs.end(),ss[i])-uniqs.begin();if(int(uniqs.size())==csize){memcpy(color,cc,sizeof(cc));break;}csize=uniqs.size();memcpy(color,cc,sizeof(cc));}
 // exact check: equal colors within one bipartition but differing neighbour masks
 for(int i=0;i<a;i++)for(int j=0;j<i;j++)if(color[i]==color[j] && rows[i]!=rows[j])return true;
 // columns masks compare
 for(int i=0;i<b;i++)for(int j=0;j<i;j++)if(color[a+i]==color[a+j]){
  for(int k=0;k<a;k++)if(bool(rows[k]&(1<<i))!=bool(rows[k]&(1<<j)))return true;
 }
 // color shared across bipartitions: open neighborhoods differ, but can still be automorphic; emit
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(color[i]==color[a+j])return true;
 return false;
}
unsigned int canonical(){int perm[5]={0,1,2,3,4}; unsigned int best=UINT_MAX; do{int cols[9]={};for(int j=0;j<b;j++)for(int r=0;r<a;r++)if(rows[perm[r]]&(1<<j))cols[j]|=1<<r;sort(cols,cols+b);unsigned int s=0;for(int j=0;j<b;j++)s|=((unsigned)cols[j])<<(j*a);best=min(best,s);}while(next_permutation(perm,perm+a));return best;}
void dfs(int depth,int low,int cover){if(depth==a){tot++;if(cover!=(1<<b)-1)return;if(!connected())return;conn++;unsigned int cc=canonical();if(allseen.insert(cc).second)foutall<<a<<" "<<b<<" "<<cc<<"\n";if(!non_twin_color())return;cand++;if(seen.insert(cc).second){uniq++;fout<<a<<" "<<b<<" "<<cc<<"\n";}return;}for(int x=low;x<(1<<b);x++){rows[depth]=x;dfs(depth+1,x,cover|x);}}
int main(int argc,char** argv){n=atoi(argv[1]);fout.open(argv[2]);if(argc>3)foutall.open(argv[3]);auto tt=chrono::steady_clock::now();for(a=1;a<=n/2;a++){b=n-a;seen.clear();allseen.clear();tot=conn=cand=uniq=0;dfs(0,1,0);cerr<<"a "<<a<<" b "<<b<<" reps "<<tot<<" connected "<<conn<<" candidates "<<cand<<" unique "<<uniq<<" all-unique "<<allseen.size()<<" sec "<<chrono::duration<double>(chrono::steady_clock::now()-tt).count()<<"\n";} }
