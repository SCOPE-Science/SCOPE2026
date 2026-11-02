#include <bits/stdc++.h>
using namespace std;
int n, counts[3], a[40];long long visited, sharp, unclustered_cycles; map<array<int,3>,long long> parikhs; string first;
void check(){
 ++visited;
 int k=(n+1)/2;
 if(n%2==0){int numOdd=(counts[0]%2)+(counts[1]%2)+(counts[2]%2);if(numOdd) return;}
 else {int numOdd=(counts[0]%2)+(counts[1]%2)+(counts[2]%2);if(numOdd!=1) return;}
 int mismatch=0; int pos[3]={0,counts[0],counts[0]+counts[1]};
 for(int i=0;i<n;i++){int f=(i<pos[1]?0:(i<pos[2]?1:2));if(a[i]!=f) ++mismatch;}
 if(mismatch!=k) return;
 int pi[40], cnt[3]={},st[3]={0,counts[0],counts[0]+counts[1]};
 for(int i=0;i<n;i++)pi[i]=st[a[i]]+cnt[a[i]]++;
 int r=0;int j=0;do{j=pi[j];++r;}while(j!=0 && r<n);
 if(r!=n)return;
 ++sharp;parikhs[{counts[0],counts[1],counts[2]}]++;
 if(first.empty())for(int i=0;i<n;i++)first.push_back('0'+a[i]);
}
void dfs(int at){if(at==n){check();return;}
 for(int v=0;v<3;v++)if(at==0||v!=a[at-1]){a[at]=v;counts[v]++;dfs(at+1);counts[v]--;}
}
int main(int argc,char **argv){for(n=atoi(argv[1]);n<=atoi(argv[2]);n++){
 visited=sharp=0;first.clear();parikhs.clear();dfs(0);cerr<<"n="<<n<<" candidates="<<visited<<" sharp="<<sharp<<" witness="<<first<<" pars=";
 for(auto&[a,k]:parikhs)cerr<<"("<<a[0]<<","<<a[1]<<","<<a[2]<<")="<<k<<" ";
 cerr<<"\n";
}}
