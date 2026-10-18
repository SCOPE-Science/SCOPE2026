#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;using u128=__uint128_t;
struct Exp{int x,y,z;};
vector<Exp> mono[11];int indexx[11][6][6];
void init(){memset(indexx,-1,sizeof(indexx));for(int d=0;d<=10;d++)for(int x=0;x<=d;x++)for(int y=0;y<=d-x;y++){int z=d-x-y;int i=mono[d].size();mono[d].push_back({x,y,z});if(d<=5)indexx[d][x][y]=i;}}
int actionbit[3][21];
// shear X->X+Y; swap X,Y; cycle X,Y,Z -> Y,Z,X
uint32_t montransform(Exp e,int g){
 if(g==1){int ind=indexx[5][e.y][e.x];return 1u<<ind;}
 if(g==2){int ind=indexx[5][e.z][e.x];return 1u<<ind;}
 uint32_t ans=0;for(int j=0;j<=e.x;j++)if((j&e.x)==j){int ind=indexx[5][j][e.y+e.x-j];ans^=(1u<<ind);}return ans;
}
inline uint32_t action(uint32_t f,int g){uint32_t out=0;while(f){int i=__builtin_ctz(f);f&=f-1;out^=actionbit[g][i];}return out;}
int pivrank(vector<u128> &arr){u128 b[66]{};int r=0;for(u128 v:arr){while(v){int j=((ull)(v>>64))?(64+63-__builtin_clzll((ull)(v>>64))):(63-__builtin_clzll((ull)v)); if(b[j])v^=b[j];else{b[j]=v;r++;break;}}if(r==66)return r;}return r;}
int rank6(array<unsigned,6> A){unsigned b[6]{};int r=0;for(auto v:A){while(v){int j=31-__builtin_clz(v);if(b[j])v^=b[j];else{b[j]=v;r++;break;}}}return r;}
array<unsigned,6> matmul(const array<unsigned,6>& A,const array<unsigned,6>& B){array<unsigned,6>C{};for(int i=0;i<6;i++)for(int j=0;j<6;j++)if((A[i]>>j)&1)C[i]^=B[j];return C;}
int derivative_index[21][3];int multidx[3][28][15];
vector<Exp> interior;
int Hidx[6][6];
int evalp[7][21];
int main(){auto t=chrono::steady_clock::now();init();
 for(int i=0;i<21;i++)for(int g=0;g<3;g++)actionbit[g][i]=montransform(mono[5][i],g);
 for(int i=0;i<21;i++){auto e=mono[5][i];derivative_index[i][0]=(e.x%2?indexx[4][e.x-1][e.y]:-1);derivative_index[i][1]=(e.y%2?indexx[4][e.x][e.y-1]:-1);derivative_index[i][2]=(e.z%2?indexx[4][e.x][e.y]:-1);}
 for(int g=0;g<3;g++)for(int a=0;a<28;a++)for(int j=0;j<15;j++){auto e=mono[6][a],h=mono[4][j];int X=e.x+h.x,Y=e.y+h.y;auto& v=mono[10];int id=-1;for(int ii=0;ii<(int)v.size();ii++)if(v[ii].x==X&&v[ii].y==Y){id=ii;break;}multidx[g][a][j]=id;}
 for(int x=1;x<=3;x++)for(int y=1;y<=4-x;y++){int z=5-x-y;if(z>=1)interior.push_back({x,y,z});}
 assert(interior.size()==6);
 for(int i=0;i<6;i++)for(int j=0;j<6;j++){auto a=interior[i],b=interior[j];int x=2*a.x-b.x,y=2*a.y-b.y,z=2*a.z-b.z;Hidx[i][j]=(x>=0&&y>=0&&z>=0&&x+y+z==5)?indexx[5][x][y]:-1;}
 for(int P=1;P<8;P++){int xyz[3];for(int j=0;j<3;j++)xyz[j]=(P>>j)&1;for(int i=0;i<21;i++){auto e=mono[5][i];evalp[P-1][i]=(!e.x||xyz[0])&&(!e.y||xyz[1])&&(!e.z||xyz[2]);}}
 ofstream repsout("representatives.csv");vector<uint8_t> vis(1<<21);map<pair<int,int>,long long> count;map<tuple<int,int,int>,long long> triples;map<pair<int,int>,long long> orbits;map<pair<int,int>,uint32_t> reps;long long smooth=0, all=0, orball=0;long long nonsmooth=0;
 for(uint32_t f=1;f<(1u<<21);f++){
  if(vis[f])continue;vector<uint32_t> Q(1,f);vis[f]=1;
  for(size_t k=0;k<Q.size();k++){uint32_t u=Q[k];for(int g=0;g<3;g++){uint32_t v=action(u,g);if(!vis[v]){vis[v]=1;Q.push_back(v);}}}
  orball++;
  unsigned dp[3][15]{};
  uint32_t z=f;while(z){int i=__builtin_ctz(z);z&=z-1;for(int g=0;g<3;g++){int j=derivative_index[i][g];if(j>=0)dp[g][j]^=1;}}
  vector<u128> rows;rows.reserve(84);for(int g=0;g<3;g++)for(int a=0;a<28;a++){u128 v=0;for(int j=0;j<15;j++)if(dp[g][j])v^=((u128)1<<multidx[g][a][j]);rows.push_back(v);}
  if(pivrank(rows)<66){nonsmooth+=Q.size();continue;}
  array<unsigned,6>H{};for(int i=0;i<6;i++)for(int j=0;j<6;j++)if(Hidx[i][j]>=0&&((f>>Hidx[i][j])&1))H[i]|=1u<<j;
  int r=rank6(H);auto powers=H;for(int k=1;k<6;k++)powers=matmul(powers,H);int p=rank6(powers);assert(p<=r);
  int N=0;for(int pp=0;pp<7;pp++){int bit=0;for(int i=0;i<21;i++)if((f>>i)&1)bit^=evalp[pp][i];if(!bit)N++;}
  smooth+=Q.size();all++;repsout<<f<<" "<<Q.size()<<" "<<p<<" "<<6-r<<" "<<N<<"\n";
  count[{p,6-r}]+=Q.size();triples[{p,6-r,N}]+=Q.size();orbits[{p,6-r}]++;if(!reps.count({p,6-r}))reps[{p,6-r}]=f;
 }
 cout<<"all_orbits "<<orball<<" smooth_orbits "<<all<<" smooth_equations "<<smooth<<" singular_equations "<<nonsmooth<<"\n";
 for(auto [pa,c]:count){auto [p,a]=pa;cout<<"p "<<p<<" a "<<a<<" eq "<<c<<" orbits "<<orbits[pa]<<" example "<<reps[pa]<<"\n";}
 for(auto [pa,c]:triples){auto [p,a,n]=pa;cout<<"stratum "<<p<<" "<<a<<" "<<n<<" "<<c<<"\n";}
 auto sec=chrono::duration<double>(chrono::steady_clock::now()-t).count();cerr<<"elapsed "<<sec<<" s\n";
}
