#include <bits/stdc++.h>
using namespace std;
using U=uint32_t; using U64=uint64_t;
vector<array<int,3>> M5,M4,M6,M10;
int idx4[6][6][6],idx10[11][11][11];
vector<array<int,3>> mons(int d){vector<array<int,3>> a;for(int i=d;i>=0;i--)for(int j=d-i;j>=0;j--)a.push_back({i,j,d-i-j});return a;}
int gl3(){return 0;}
int main(){
 auto start=chrono::steady_clock::now();
 M5=mons(5);M4=mons(4);M6=mons(6);M10=mons(10);
 memset(idx4,-1,sizeof(idx4));memset(idx10,-1,sizeof(idx10));
 for(int j=0;j<(int)M4.size();j++){auto x=M4[j];idx4[x[0]][x[1]][x[2]]=j;}
 for(int j=0;j<(int)M10.size();j++){auto x=M10[j];idx10[x[0]][x[1]][x[2]]=j;}
 int idxd[6][6][6];memset(idxd,-1,sizeof(idxd));vector<array<int,3>> allmons;
 for(int d=0;d<=5;d++){auto a=mons(d);for(auto x:a)idxd[x[0]][x[1]][x[2]]=allmons.size(),allmons.push_back(x);}
 auto poly_mul = [&](U64 u,U64 v)->U64{ U64 r=0;for(int i=0;i<(int)allmons.size();i++)if(u>>i&1)for(int j=0;j<(int)allmons.size();j++)if(v>>j&1){auto a=allmons[i],b=allmons[j]; if(a[0]+b[0]+a[1]+b[1]+a[2]+b[2]<=5)r^=1ull<<idxd[a[0]+b[0]][a[1]+b[1]][a[2]+b[2]];}return r;};
 int index5[6][6][6];memset(index5,-1,sizeof(index5));for(int i=0;i<(int)M5.size();i++){auto x=M5[i];index5[x[0]][x[1]][x[2]]=i;}
 vector<array<U,21>> trans;
 for(int m=0;m<512;m++){
 int v[3]={m&7,(m>>3)&7,(m>>6)&7};
 if(!v[0]||!v[1]||!v[2]||v[0]==v[1]||v[0]==v[2]||v[1]==v[2]||(v[0]^v[1])==v[2]) continue;
 U64 lp[3]={0,0,0};for(int i=0;i<3;i++)for(int k=0;k<3;k++)if((v[i]>>k)&1)lp[i]^=1ull<<idxd[k==0][k==1][k==2];
 U64 powers[3][6];for(int i=0;i<3;i++){powers[i][0]=1ull<<0;for(int k=1;k<=5;k++)powers[i][k]=poly_mul(powers[i][k-1],lp[i]);}
 array<U,21> cols={};for(int i=0;i<21;i++){auto x=M5[i];U64 w=poly_mul(poly_mul(powers[0][x[0]],powers[1][x[1]]),powers[2][x[2]]),o=0;for(int j=0;j<(int)allmons.size();j++)if(w>>j&1ull){auto ex=allmons[j];if(ex[0]+ex[1]+ex[2]==5)o^=1u<<index5[ex[0]][ex[1]][ex[2]];}cols[i]=o;}
 trans.push_back(cols);
 }
 cerr<<"group transforms "<<trans.size()<<"\n";
 if(trans.size()!=168)exit(3);
 auto transform=[&](U f,const array<U,21>&cols)->U{U ans=0;while(f){int i=__builtin_ctz(f);ans^=cols[i];f&=f-1;}return ans;};
 U ev[7]={};int pts[7]={1,2,3,4,5,6,7};for(int p=1;p<8;p++)for(int i=0;i<21;i++){auto a=M5[i];if((a[0]&&!(p&1))||(a[1]&&!(p&2))||(a[2]&&!(p&4)))continue;ev[p-1]|=1u<<i;}
 int lines[7]={};for(int l=1;l<8;l++)for(int p=1;p<8;p++)if(!(__builtin_parity(l&p)))lines[l-1]|=1u<<(p-1);
 auto isblocking=[&](U f)->bool{int ps=0;for(int i=0;i<7;i++)if(!__builtin_parity(f&ev[i]))ps|=1<<i;for(int i=0;i<7;i++)if(!(ps&lines[i]))return false;return true;};
 auto numpts=[&](U f)->int{int ans=0;for(int i=0;i<7;i++)ans+=!__builtin_parity(f&ev[i]);return ans;};
 using Int=unsigned __int128;
 auto smooth=[&](U f)->bool{
  int der[3]={};for(int i=0;i<21;i++)if(f>>i&1){auto a=M5[i];for(int k=0;k<3;k++)if(a[k]&1){auto b=a;b[k]--;der[k]^=1<<idx4[b[0]][b[1]][b[2]];}}
  struct Col{U64 lo=0,hi=0;};Col piv[66];bool active[66]={};int rank=0;
  for(int k=0;k<3;k++)for(auto u:M6){Col c={};int d=der[k];while(d){int i=__builtin_ctz((U)d);d&=d-1;auto v=M4[i];int n=idx10[u[0]+v[0]][u[1]+v[1]][u[2]+v[2]];if(n<64)c.lo^=1ull<<n;else c.hi^=1ull<<(n-64);}
  while(c.lo||c.hi){int p=c.hi?64+63-__builtin_clzll(c.hi):63-__builtin_clzll(c.lo);if(!active[p]){active[p]=true;piv[p]=c;rank++;break;}c.lo^=piv[p].lo;c.hi^=piv[p].hi;}
  if(rank==66)return true;
  }
  return false;
 };
 vector<unsigned char> seen(1<<21,0);
 long long joint[2][2][8]={},orbits[2][2][8]={};
 long long orb_hist[169]={};
 int reps=0;
 for(U f=1;f<(1u<<21);f++) if(!seen[f]){
  vector<U> orbit;orbit.reserve(168);
  for(auto &tr:trans){U g=transform(f,tr);if(!seen[g]){seen[g]=1;orbit.push_back(g);}}
  int n=orbit.size();if(n==0){cerr<<"bad orbit";exit(4);}orb_hist[n]++;reps++;
  bool s=smooth(f),b=isblocking(f);int p=numpts(f);joint[s][b][p]+=n;orbits[s][b][p]++;
 }
 cout<<"transforms "<<trans.size()<<" representatives "<<reps<<"\n";
 for(int s=0;s<2;s++)for(int b=0;b<2;b++){long long sum=0,sumor=0;cout<<"smooth="<<s<<" blocking="<<b<<" :";for(int p=0;p<=7;p++){cout<<" "<<joint[s][b][p];sum+=joint[s][b][p];sumor+=orbits[s][b][p];}cout<<" SUM="<<sum<<" ORBITS="<<sumor<<"\n";}
 cerr<<"elapsed "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<" seconds\n";
 for(int n=1;n<=168;n++)if(orb_hist[n])cerr<<"orbsize="<<n<<" count="<<orb_hist[n]<<"\n";
}
