// Independent exhaustive verifier: first-unmatched-face enumeration, reversed-Hasse-edge DAG test.
// Output lists each permutation fixing the critical vertex and its exact fixed count.
#include <bits/stdc++.h>
using namespace std;
int degs[32], adjj[32][16], id_of[32], mask_of[32];
pair<int,int> match_edges[16]; int mcount=0; long long perfect=0,acyclic=0;
vector<array<int,5>> perms; vector<array<int,31>> pmap; vector<long long> fixed_ct;

bool isdag(){ int dir[31][31]={}, ind[31]={}; for(int s=1;s<32;s++) for(int t=1;t<32;t++) if(__builtin_popcount((unsigned)t)==__builtin_popcount((unsigned)s)+1 && (s&t)==s){int a=id_of[s],b=id_of[t]; if(a<0||b<0)continue; dir[a][b]=1;}
 for(int i=0;i<mcount;i++){int a=match_edges[i].first,b=match_edges[i].second; if(dir[a][b]){dir[a][b]=0; dir[b][a]=1;}else{dir[b][a]=0;dir[a][b]=1;}}
 for(int a=0;a<31;a++)for(int b=0;b<31;b++)ind[b]+=dir[a][b]; int q[31],qhead=0,qtail=0;for(int a=0;a<31;a++)if(!ind[a])q[qtail++]=a;
 while(qhead<qtail){int a=q[qhead++];for(int b=0;b<31;b++)if(dir[a][b]&&--ind[b]==0)q[qtail++]=b;}return qtail==31; }
void dfs(uint32_t used){ if(mcount==15){perfect++; if(!isdag())return;acyclic++; int matrix[31]; fill(matrix,matrix+31,-1);for(int i=0;i<15;i++){auto[a,b]=match_edges[i];matrix[a]=b;matrix[b]=a;}
 for(int k=0;k<(int)perms.size();k++){bool ok=true;for(int a=0;a<31;a++)if(matrix[a]!=-1 && matrix[pmap[k][a]]!=pmap[k][matrix[a]]){ok=false;break;}if(ok)fixed_ct[k]++;}return;}
 int best=-1;for(int a=0;a<31;a++)if(!(used&(1u<<a))){best=a;break;}if(best<0)return;
 for(int j=0;j<degs[best];j++){int b=adjj[best][j];if(used&(1u<<b))continue;int a=best; if(__builtin_popcount((unsigned)mask_of[a])>__builtin_popcount((unsigned)mask_of[b]))swap(a,b);match_edges[mcount++]={a,b};dfs(used|(1u<<best)|(1u<<b));mcount--;}
}
int main(){ for(int s=1,idx=0;s<32;s++){id_of[s]=idx;mask_of[idx]=s;idx++;} id_of[0]=-1;
 for(int s=1;s<32;s++)for(int t=1;t<32;t++)if(__builtin_popcount((unsigned)t)==__builtin_popcount((unsigned)s)+1&&(s&t)==s){int a=id_of[s],b=id_of[t];adjj[a][degs[a]++]=b;adjj[b][degs[b]++]=a;}
 array<int,5> p={0,1,2,3,4};do{ if(p[0]!=0)continue; perms.push_back(p);array<int,31> mm;for(int i=0;i<31;i++){int s=mask_of[i],t=0;for(int k=0;k<5;k++)if(s&(1<<k))t|=1<<p[k];mm[i]=id_of[t];}pmap.push_back(mm);}while(next_permutation(p.begin(),p.end())); fixed_ct.resize(perms.size()); int crit=id_of[1];dfs(1u<<crit);cout<<"perfect="<<perfect<<" acyclic="<<acyclic<<"\n";
 for(int i=0;i<(int)perms.size();i++){for(int j=0;j<5;j++)cout<<perms[i][j];cout<<" "<<fixed_ct[i]<<"\n";} }
