// Independent Burnside orbit-count check for binary cubic surfaces.
#include <bits/stdc++.h>
using namespace std;
struct E{int a[4];};
vector<E> mon;int idx[4][4][4][4];
int row_rank(array<int,4> a){int r=0;for(int b=3;b>=0;b--){int j=r;while(j<4&&!(a[j]&(1<<b)))j++;if(j==4)continue;swap(a[j],a[r]);for(int k=0;k<4;k++)if(k!=r &&(a[k]&(1<<b)))a[k]^=a[r];r++;}return r;}
uint64_t multiply(uint64_t A,uint64_t B){uint64_t R=0;while(A){int i=__builtin_ctzll(A);A&=A-1;uint64_t C=B;while(C){int j=__builtin_ctzll(C);C&=C-1;auto x=mon[i],y=mon[j];int a=x.a[0]+y.a[0],b=x.a[1]+y.a[1],c=x.a[2]+y.a[2],d=x.a[3]+y.a[3];if(a+b+c+d<=3)R^=1ull<<idx[a][b][c][d];}}return R;}
int main(){memset(idx,-1,sizeof idx);for(int degree=0;degree<=3;degree++)for(int a=0;a<=degree;a++)for(int b=0;b<=degree-a;b++)for(int c=0;c<=degree-a-b;c++){int d=degree-a-b-c;idx[a][b][c][d]=mon.size();mon.push_back({a,b,c,d});}
vector<int> deg3;for(int k=0;k<(int)mon.size();k++){int d=0;for(int q=0;q<4;q++)d+=mon[k].a[q];if(d==3)deg3.push_back(k);}int inv[35]={};for(int i=0;i<20;i++)inv[deg3[i]]=i;
long long totalFixed=0;int groupSize=0;map<int,int> rankHist;
for(int a=1;a<16;a++)for(int b=1;b<16;b++)for(int c=1;c<16;c++)for(int d=1;d<16;d++){
 array<int,4> matrix={a,b,c,d};if(row_rank(matrix)!=4)continue;groupSize++;
 uint64_t L[4]={};for(int i=0;i<4;i++)for(int k=0;k<4;k++)if(matrix[i]>>k&1){int ex[4]={};ex[k]=1;L[i]^=1ull<<idx[ex[0]][ex[1]][ex[2]][ex[3]];}
 uint32_t cols[20]={};for(int h=0;h<20;h++){
  auto e=mon[deg3[h]];uint64_t p=1ull<<idx[0][0][0][0];for(int i=0;i<4;i++)for(int j=0;j<e.a[i];j++)p=multiply(p,L[i]);
  while(p){int k=__builtin_ctzll(p);p&=p-1;cols[h]^=1u<<inv[k];}
  cols[h]^=1u<<h;
 }
 uint32_t piv[20]={};int rank=0;for(int k=0;k<20;k++){auto v=cols[k];while(v){int bit=31-__builtin_clz(v);if(!piv[bit]){piv[bit]=v;rank++;break;}v^=piv[bit];}}
 rankHist[rank]++;totalFixed+=(1ll<<(20-rank));
}
cout<<"GL4="<<groupSize<<" Burnside_fixed_sum="<<totalFixed<<" polynomial_orbits="<<totalFixed/groupSize<<" nonzero_orbits="<<totalFixed/groupSize-1<<" remainder="<<totalFixed%groupSize<<"\n";
for(auto [r,n]:rankHist)cout<<"rank "<<r<<" class_count "<<n<<"\n";
}
