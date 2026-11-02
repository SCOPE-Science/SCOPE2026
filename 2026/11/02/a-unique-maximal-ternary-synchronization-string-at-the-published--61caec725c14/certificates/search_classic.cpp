#include <bits/stdc++.h>
using namespace std;
vector<int> s; long long nodes=0; int maxdepth=0; vector<long long> perdepth(5001);int P,Q,Cap; string longest;
bool valid_tail(){int n=s.size();for(int j=n-1;j>=1;--j){
 // i = j-1 downto 0, subseq DP for two adjacent blocks
 vector<int> p(n-j+1), c(n-j+1);
 for(int i=j-1;i>=0;--i){ // dynamic computation for first block S[i:j] from right to left
  // Need compute reversed both strings DP: second word suffix reversed indexing
  c[0]=0;
  for(int k=1;k<=n-j;k++){
   int b=s[n-k];
   c[k]=s[i]==b?p[k-1]+1:max(p[k],c[k-1]);
  }
  p.swap(c);
  int lcs=p[n-j];
  if(2*Q*lcs >= P*(n-i)) return false;
 }
}return true;}
void dfs(int maxchar){int n=s.size();nodes++;if(n>maxdepth){maxdepth=n;longest.clear();for(int v:s)longest+=char('0'+v);}perdepth[n]++;if(n==Cap)return;
 for(int c=0;c<=min(2,maxchar+1);c++){s.push_back(c);if(valid_tail())dfs(max(maxchar,c));s.pop_back();}
}
int main(int argc,char**argv){P=stoi(argv[1]);Q=stoi(argv[2]);Cap=stoi(argv[3]);s={0};dfs(0);cout<<"epsilon="<<P<<"/"<<Q<<" maxdepth="<<maxdepth<<" nodes="<<nodes<<" witness="<<longest<<"\n";for(int i=1;i<=maxdepth;i++)cout<<i<<":"<<perdepth[i]<<" ";cout<<"\n";}
