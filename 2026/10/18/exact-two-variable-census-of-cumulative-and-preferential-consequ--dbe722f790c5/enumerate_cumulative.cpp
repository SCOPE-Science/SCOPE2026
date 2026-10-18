#include <bits/stdc++.h>
using namespace std;
int n=4,NN=16; int f[16],subs[16][16],ns[16],ord[16],perm[24][4],ntype[24],M[24][16],np=0;
unsigned long long total=0,yes=0,fx[5]={},px[5]={};
int typ(const int p[4]){int seen[4]={0}, len[5]={0};for(int i=0;i<4;i++)if(!seen[i]){int x=i,c=0;do{seen[x]=1;x=p[x];c++;}while(x!=i);len[c]++;}if(len[1]==4)return 0;if(len[2]==1)return 1;if(len[2]==2)return 2;if(len[3]==1)return 3;return 4;}
void dfs(int dep){
 if(dep==NN){
  total++;bool P=true;
  for(int A=0;A<NN;A++)for(int B=0;B<NN;B++)if(f[A|B] & ~(f[A]|f[B])){P=false;goto fin;}fin:
  if(P)yes++;
  for(int p=0;p<np;p++){
   bool fix=true;for(int A=0;A<NN;A++)if(f[M[p][A]]!=M[p][f[A]]){fix=false;break;}
   if(fix){fx[ntype[p]]++;if(P)px[ntype[p]]++;}
  }
  return;
 }
 int A=ord[dep];
 for(int k=0;k<ns[A];k++){
  int B=subs[A][k];bool ok=true;
  for(int h=0;h<ns[A];h++){
   int C=subs[A][h];if(C==A)continue;
   if((C&B)==B && f[C]!=B){ok=false;break;}
  }
  if(ok){f[A]=B;dfs(dep+1);}
 }
}
int main(){for(int i=0;i<16;i++)for(int j=0;j<16;j++)if((i&j)==j)subs[i][ns[i]++]=j;int o=0;
for(int k=0;k<=n;k++)for(int i=0;i<16;i++)if(__builtin_popcount((unsigned)i)==k)ord[o++]=i;
int p[4]={0,1,2,3};do{for(int i=0;i<4;i++)perm[np][i]=p[i];ntype[np]=typ(p);for(int A=0;A<16;A++){int B=0;for(int i=0;i<4;i++)if(A&(1<<i))B|=1<<p[i];M[np][A]=B;}np++;}while(next_permutation(p,p+4));
dfs(0);cout<<"total "<<total<<" P "<<yes<<"\n";
int sizes[5]={1,6,3,8,6};unsigned long long tf=0,tp=0;
for(int i=0;i<5;i++){cout<<"class "<<i<<" size "<<sizes[i]<<" fixed_C_per_el "<<fx[i]/sizes[i]<<" fixed_P_per_el "<<px[i]/sizes[i]<<"\n";tf+=fx[i];tp+=px[i];}
cout<<"C orbits "<<tf/24<<" P orbits "<<tp/24<<"\n";
}
