// Exact rational-point counts on extension fields; compare full genus-six Weil polynomials.
#include <bits/stdc++.h>
using namespace std;
struct E{int a,b,c;};
struct Rec{int mask,weight,p,a,n1;array<int,6> N{};};
int fieldmul(int x,int y,int mod,int n){int ans=0;int top=1<<n,lim=top-1;while(y){if(y&1)ans^=x;y>>=1;x<<=1;if(x&top)x^=mod;}return ans&lim;}
int main(){vector<E>M;for(int x=0;x<=5;x++)for(int y=0;y<=5-x;y++)M.push_back({x,y,5-x-y});if(M.size()!=21)return 1;
 ifstream in("representatives.csv");vector<Rec>R;Rec x;while(in>>x.mask>>x.weight>>x.p>>x.a>>x.n1)R.push_back(x);
 int irr[7]={0,0b11,0b111,0b1011,0b10011,0b100101,0b1000011};
 for(int n=1;n<=6;n++){
  int q=1<<n;vector<array<unsigned char,21>> rows;rows.reserve(q*q+q+1);
  vector<array<int,6>> Pow(q);for(int a=0;a<q;a++){Pow[a][0]=1;for(int k=1;k<=5;k++)Pow[a][k]=fieldmul(Pow[a][k-1],a,irr[n],n);}
  auto add=[&](int X,int Y,int Z){array<unsigned char,21>e{};for(int j=0;j<21;j++){auto t=M[j];e[j]=fieldmul(fieldmul(Pow[X][t.a],Pow[Y][t.b],irr[n],n),Pow[Z][t.c],irr[n],n);}rows.push_back(e);};
  for(int y=0;y<q;y++)for(int z=0;z<q;z++)add(1,y,z);
  for(int z=0;z<q;z++)add(0,1,z);add(0,0,1);
  for(auto &r:R){int zeros=0;for(auto &v:rows){int bit=0;unsigned f=r.mask;while(f){int k=__builtin_ctz(f);f&=f-1;bit^=v[k];}zeros+=(bit==0);}r.N[n-1]=zeros;}
  fprintf(stderr,"extension %d completed\n",n);
 }
 map<array<int,6>,vector<int>>groups;for(int i=0;i<(int)R.size();i++)groups[R[i].N].push_back(i);
 long long pairs=0;int collide=0;
 for(auto [key,ind]:groups){int a0=R[ind[0]].a;bool diff=0;for(int k:ind)if(R[k].a!=a0)diff=1;
  if(!diff)continue;collide++;
  printf("SAME_ZETA_DIFFERENT_A N=%d,%d,%d,%d,%d,%d\n",key[0],key[1],key[2],key[3],key[4],key[5]);
  for(int k:ind)printf("example mask=%d p=%d a=%d orbit_size=%d\n",R[k].mask,R[k].p,R[k].a,R[k].weight);
  if(collide==2)break;
 }
 if(!collide)puts("no_collision_with_distinct_a");
 fprintf(stderr,"total curves=%zu signatures=%zu first n1=%d\n",R.size(),groups.size(),R.empty()?0:R[0].N[0]);
}
