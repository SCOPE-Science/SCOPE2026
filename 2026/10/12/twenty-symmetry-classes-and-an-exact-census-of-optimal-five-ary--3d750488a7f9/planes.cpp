#include <bits/stdc++.h>
using namespace std;
int adj[13][4], P[24][4];unsigned char pointmask[13]{}, cur[13][4]{};
long long count_=0;ofstream out("colorings.bin",ios::binary);
void dfs(int rem){if(!rem){unsigned char a[13];for(int l=0;l<13;l++){a[l]=0;for(int i=0;i<4;i++)a[l]|=cur[l][i]<<(2*i);}out.write((char*)a,13); count_++;return;}
 int best=-1,bestn=25;
 for(int l=1;l<13;l++)if(rem>>l&1){int kcnt=0;for(int k=0;k<24;k++){bool ok=1;for(int j=0;j<4;j++)if(pointmask[adj[l][j]]&(1<<P[k][j])){ok=0;break;}if(ok)kcnt++;}if(kcnt<bestn){bestn=kcnt;best=l;if(kcnt==0)return;if(kcnt==1)break;}}
 int l=best;
 for(int k=0;k<24;k++){bool ok=1;for(int j=0;j<4;j++)if(pointmask[adj[l][j]]&(1<<P[k][j])){ok=0;break;}if(!ok)continue;
 for(int j=0;j<4;j++){pointmask[adj[l][j]]|=1<<P[k][j];cur[l][j]=P[k][j];}
 dfs(rem^(1<<l));for(int j=0;j<4;j++)pointmask[adj[l][j]]^=1<<P[k][j];
 }
}
int main(){int v[13][3],n=0;for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++){
 int x[]={a,b,c};if(!a&&!b&&!c)continue;int lead=-1;for(int k=0;k<3;k++)if(x[k]){lead=k;break;}if(x[lead]!=1)continue;
 for(int k=0;k<3;k++)v[n][k]=x[k];n++;}assert(n==13);
 for(int l=0;l<13;l++){int j=0;for(int p=0;p<13;p++){int dot=0;for(int k=0;k<3;k++)dot+=v[l][k]*v[p][k];if(dot%3==0){assert(j<4);adj[l][j++]=p;}}assert(j==4);}
 cout<<"vectors:";for(int l=0;l<13;l++)cout<<" "<<v[l][0]<<v[l][1]<<v[l][2];cout<<"\n";
 for(int l=0;l<13;l++){cout<<"line "<<l<<":";for(int j=0;j<4;j++)cout<<" "<<adj[l][j];cout<<"\n";}
 int p[]={0,1,2,3},pc=0;do{for(int j=0;j<4;j++)P[pc][j]=p[j];pc++;}while(next_permutation(p,p+4));
 for(int j=0;j<4;j++){cur[0][j]=j;pointmask[adj[0][j]]|=1<<j;}
 dfs(((1<<13)-1)^1);cout<<"normalized_coloring_count="<<count_<<"\n";
}
