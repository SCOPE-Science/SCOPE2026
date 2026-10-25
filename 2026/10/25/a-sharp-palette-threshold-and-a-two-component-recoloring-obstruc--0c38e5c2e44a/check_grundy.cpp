/* Exhaustive upper bound on the Grundy number of Paley(13).
   A vertex of color 7 can be translated to zero. Its six neighbors
   must have all six colors 1,...,6, tested in all 720 orders.
   The remaining six vertices get every legal color from 1,...,7.
   Each resulting complete proper coloring is checked for Grundy validity. */
#include <bits/stdc++.h>
using namespace std;
int main(){int N=13;int a[13]={};for(int i=0;i<N;i++)for(int j=0;j<N;j++){int d=(j-i+N)%N;if(d==1||d==3||d==4||d==9||d==10||d==12)a[i]|=1<<j;}
vector<int> neigh,non;for(int i=1;i<N;i++)((a[0]&(1<<i))?neigh:non).push_back(i);int col[13];fill(col,col+13,-1);col[0]=7;int perm[6]={1,2,3,4,5,6};long long tries=0;bool found=false;
function<void(int)> dfs=[&](int p){if(found)return;if(p==6){tries++;for(int i=0;i<N;i++){int c=col[i];int mask=0;for(int j=0;j<N;j++)if(a[i]&(1<<j))mask|=1<<col[j];for(int d=1;d<c;d++)if(!(mask&(1<<d)))return;}found=true;cout<<"GRUNDY7 witness";for(int i=0;i<N;i++)cout<<" "<<col[i];cout<<"\n";return;}int v=non[p];int forbidden=0;for(int j=0;j<N;j++)if(col[j]>=1&&(a[v]&(1<<j)))forbidden|=1<<col[j];for(int c=1;c<=7;c++)if(!(forbidden&(1<<c))){col[v]=c;dfs(p+1);}col[v]=-1;};
do{for(int i=0;i<6;i++)col[neigh[i]]=perm[i];dfs(0);if(found)break;}while(next_permutation(perm,perm+6));
cout<<"found "<<found<<" leaf_assignments "<<tries<<"\n";
}
