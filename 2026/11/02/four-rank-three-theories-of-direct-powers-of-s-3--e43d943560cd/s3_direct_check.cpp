#include <bits/stdc++.h>
using namespace std;
using U=unsigned __int128;
int main(){
 vector<array<int,3>> p;
 array<int,3> z={0,1,2};do{p.push_back(z);}while(next_permutation(z.begin(),z.end()));
 int id[3][3][3]; memset(id,0,sizeof(id));
 for(int i=0;i<6;i++)id[p[i][0]][p[i][1]][p[i][2]]=i;
 int mul[6][6];for(int i=0;i<6;i++)for(int j=0;j<6;j++)mul[i][j]=id[p[i][p[j][0]]][p[i][p[j][1]]][p[i][p[j][2]]];
 int e=id[0][1][2]; U local[6][6][6];
 for(int a=0;a<6;a++)for(int b=0;b<6;b++)for(int c=0;c<6;c++){
  int v[4]={e,a,b,c},bit=0;U m=0;
  for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(v[i]==v[j])m|=U(1)<<bit++;else bit++;
  for(int i=0;i<4;i++)for(int j=0;j<4;j++)for(int k=0;k<4;k++){if(mul[v[i]][v[j]]==v[k])m|=U(1)<<bit;bit++;}
  assert(bit==70);local[a][b][c]=m;
 }
 map<vector<U>,int> profiles;
 for(int n=1;n<=3;n++){
  int N=1;for(int j=0;j<n;j++)N*=6;
  vector<array<int,3>> digs(N);for(int x=0;x<N;x++){int t=x;for(int j=0;j<n;j++){digs[x][j]=t%6;t/=6;}}
  map<vector<int>,int> pointed;
  for(int x=0;x<N;x++){
   vector<int> profile_ids;
   for(int y=0;y<N;y++){
    vector<U> ext;
    ext.reserve(N);
    for(int w=0;w<N;w++){
     U m=~U(0);
     for(int j=0;j<n;j++)m &= local[digs[x][j]][digs[y][j]][digs[w][j]];
     ext.push_back(m);
    }
    sort(ext.begin(),ext.end());ext.erase(unique(ext.begin(),ext.end()),ext.end());
    auto it=profiles.find(ext);
    if(it==profiles.end())it=profiles.emplace(move(ext),(int)profiles.size()).first;
    profile_ids.push_back(it->second);
   }
   sort(profile_ids.begin(),profile_ids.end());profile_ids.erase(unique(profile_ids.begin(),profile_ids.end()),profile_ids.end());
   pointed.emplace(move(profile_ids),0);
  }
  cout<<"n="<<n<<" group_size="<<N<<" pointed_rank2_types="<<pointed.size()<<" cumulative_pair_rank1_types="<<profiles.size()<<"\n";
 }
}
