#include <bits/stdc++.h>
using namespace std;
static int S[2000];int n, P,Q,cap,MAXCH;
unsigned long long countN[2001]={},nodecount=0, maxlen=0;string witness;
static inline int pc(uint64_t x){return __builtin_popcountll(x);}
// Multiword bitset LCS for all adjacent intervals ending at n.
bool valid_end(){
  int len=n;
  for(int split=n-1;split>=1;--split){
    int m=n-split;
    int z=(m+63)>>6;
    uint64_t masks[3][32]={},D[32]={};
    for(int p=0;p<m;p++) masks[S[n-p-1]][p>>6] |= 1ULL<<(p&63);
    for(int left=split-1;left>=0;--left){
      int c=S[left]; uint64_t prev=0, borrow=0;int lcs=0;
      for(int v=0;v<z;v++){
        uint64_t x=masks[c][v]|D[v];
        uint64_t sh=(D[v]<<1)|prev;
        prev=D[v]>>63;
        if(v==0)sh|=1ULL;
        uint64_t y=sh+borrow;
        bool overflow=borrow && (y==0);
        uint64_t diff=x-y;
        borrow=(x<y)||overflow;
        D[v]=x & (x ^ diff);
        lcs+=pc(D[v]);
      }
      if(2LL*Q*lcs>=1LL*P*(n-left)) return false;
    }
  }
  return true;
}
void dfs(int currentMax){
  nodecount++;countN[n]++;
  if(n>maxlen){maxlen=n;witness.clear();for(int i=0;i<n;i++)witness+=char('0'+S[i]);}
  if(n>=cap)return;
  for(int ch=0;ch<=min(2,currentMax+1);ch++){
    S[n++]=ch;
    if(valid_end())dfs(max(ch,currentMax));
    n--;
  }
}
int main(int argc,char**argv){P=atoi(argv[1]);Q=atoi(argv[2]);cap=atoi(argv[3]);n=1;S[0]=0;dfs(0);cout<<"p="<<P<<" q="<<Q<<" cap="<<cap<<" nodes="<<nodecount<<" maxlen="<<maxlen<<" witness="<<witness<<"\n";for(int i=1;i<=maxlen;i++)cout<<i<<":"<<countN[i]<<" ";cout<<"\n";}
