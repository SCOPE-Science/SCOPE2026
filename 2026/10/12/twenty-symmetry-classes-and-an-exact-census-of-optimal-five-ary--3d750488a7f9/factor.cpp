#include <bits/stdc++.h>
using namespace std;
int ds[4]={0,1,3,9};
int points[13][4],perms[24][4],num=0;
unsigned char masks[13]{}; long long nodes[14]{},solutions=0;
void dfs(int remain,int depth){
 nodes[depth]++;
 if(!remain){solutions++;return;}
 int best=-1,bestn=25,best_valid[24],nvalid=0;
 for(int l=1;l<13;l++)if(remain>>l&1){
  int nn=0;
  for(int k=0;k<24;k++){
   bool ok=true;for(int j=0;j<4;j++)if(masks[points[l][j]]>>(perms[k][j])&1){ok=false;break;}
   if(ok)nn++;
  }
  if(nn<bestn){bestn=nn;best=l;if(!nn)return; if(nn==1)break;}
 }
 int l=best;
 for(int k=0;k<24;k++){
  bool ok=true;for(int j=0;j<4;j++)if(masks[points[l][j]]>>(perms[k][j])&1){ok=false;break;}
  if(!ok)continue;
  for(int j=0;j<4;j++)masks[points[l][j]]|=1<<perms[k][j];
  dfs(remain ^ (1<<l),depth+1);
  for(int j=0;j<4;j++)masks[points[l][j]]^=1<<perms[k][j];
 }
}
int main(){for(int i=0;i<13;i++)for(int j=0;j<4;j++)points[i][j]=(i+ds[j])%13;
 int p[]={0,1,2,3};do{for(int j=0;j<4;j++)perms[num][j]=p[j];num++;}while(next_permutation(p,p+4));
 for(int j=0;j<4;j++)masks[points[0][j]]|=1<<j;
 dfs(((1<<13)-1)^1,1);
 cerr<<"solutions_reduced="<<solutions<<" all="<<solutions*24<<"\n";
 for(int i=1;i<=13;i++)cerr<<"depth "<<i<<" nodes "<<nodes[i]<<"\n";
}
