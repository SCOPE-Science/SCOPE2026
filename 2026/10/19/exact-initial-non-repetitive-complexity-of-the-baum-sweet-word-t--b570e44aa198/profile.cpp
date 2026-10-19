#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 int M= argc>1 ? stoi(argv[1]):8192, L= 8*M; string s="A"; map<char,string> mu{{'A',"AB"},{'B',"CB"},{'C',"BD"},{'D',"DD"}};
 while((int)s.size()<L){string t; t.reserve(2*s.size());for(char x:s)t+=mu[x]; s=move(t);} s.resize(L);for(char &x:s)x=(x=='A'||x=='B')?'1':'0';
 vector<int> sa(L),rank(L),next_rank(L); iota(sa.begin(),sa.end(),0);for(int i=0;i<L;i++)rank[i]=s[i];
 for(int k=1;k<L;k*=2){sort(sa.begin(),sa.end(),[&](int i,int j){if(rank[i]!=rank[j])return rank[i]<rank[j];return (i+k<L?rank[i+k]:-1)<(j+k<L?rank[j+k]:-1);});next_rank[sa[0]]=0;for(int i=1;i<L;i++){int a=sa[i-1],b=sa[i];next_rank[b]=next_rank[a]+(rank[a]!=rank[b]||(a+k<L?rank[a+k]:-1)!=(b+k<L?rank[b+k]:-1));}rank.swap(next_rank);if(rank[sa.back()]==L-1)break;}
 vector<int> pos(L),height(L);for(int i=0;i<L;i++)pos[sa[i]]=i;
 for(int i=0,h=0;i<L;i++){int r=pos[i];if(!r){h=0;continue;}int j=sa[r-1];while(i+h<L&&j+h<L&&s[i+h]==s[j+h])h++;height[r]=h; if(h)h--;}
 int logn=1;while((1<<logn)<=L)logn++;vector<int> lg(L+1);for(int i=2;i<=L;i++)lg[i]=lg[i/2]+1;
 vector<vector<int>> st(logn,vector<int>(L)); st[0]=height;for(int k=1;k<logn;k++)for(int i=0;i+(1<<k)<=L;i++)st[k][i]=min(st[k-1][i],st[k-1][i+(1<<(k-1))]);
 auto lcp=[&](int i,int j){if(i==j)return L-i;int a=pos[i],b=pos[j];if(a>b)swap(a,b);a++;int k=lg[b-a+1];return min(st[k][a],st[k][b-(1<<k)+1]);};
 vector<int> R(M+1,-1),P(M+1,-1);int unresolved=M;set<int> seen;int maxSeen=0;
 // A suffix repeated at j with max previous LCP l implies all lengths <=l collide by j.
 // The earliest j is assigned when this length first becomes repeated.
 for(int j=0;j<7*M && unresolved>0;j++){
  int r=pos[j],best=0,src=-1;
  auto it=seen.lower_bound(r);
  if(it!=seen.end()){int x=sa[*it],v=lcp(j,x);if(v>best){best=v;src=x;}}
  if(it!=seen.begin()){--it;int x=sa[*it],v=lcp(j,x);if(v>best){best=v;src=x;}}
  best=min(best,M);
  if(best>maxSeen){for(int n=maxSeen+1;n<=best;n++){R[n]=j;P[n]=src;unresolved--;}maxSeen=best;}
  seen.insert(r);
 }
 if(unresolved){cerr<<"UNRESOLVED "<<unresolved<<"\n";return 1;}
 cerr<<"CALC_COMPLETE length="<<M<<" longest prefix="<<L<<"\n";
 cout<<"n_start,n_end,first_repetition,previous_match\n";
 for(int n=1;n<=M;){int e=n;while(e<M&&R[e+1]==R[n]&&P[e+1]==P[n])e++;cout<<n<<','<<e<<','<<R[n]<<','<<P[n]<<'\n';n=e+1;}
}
