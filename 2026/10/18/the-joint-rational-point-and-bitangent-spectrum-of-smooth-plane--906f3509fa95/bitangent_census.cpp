#include <bits/stdc++.h>
using namespace std;
using U=__uint128_t;
struct E {int a,b,c;};
vector<E> mon(int d){vector<E> v;for(int a=d;a>=0;--a)for(int b=d-a;b>=0;--b)v.push_back({a,b,d-a-b});return v;}
int find(const vector<E>&v,E e){for(int i=0;i<(int)v.size();++i)if(v[i].a==e.a&&v[i].b==e.b&&v[i].c==e.c)return i;return -1;}
int pp(int n){return __builtin_parity((unsigned)n);}
int main(){auto m4=mon(4),m3=mon(3),m6=mon(6),m7=mon(7),m10=mon(10); if(m4.size()!=15||m10.size()!=66)abort();
 U FM[15][28]={},DM[3][15][36]={};
 for(int j=0;j<15;++j){auto e=m4[j];for(int k=0;k<28;++k){auto b=m6[k];int z=find(m10,{e.a+b.a,e.b+b.b,e.c+b.c});FM[j][k]=U(1)<<z;}
  for(int v=0;v<3;++v){int ex=v==0?e.a:v==1?e.b:e.c;if(!(ex&1))continue;E de=e;if(v==0)--de.a;if(v==1)--de.b;if(v==2)--de.c;for(int k=0;k<36;++k){auto b=m7[k];int z=find(m10,{de.a+b.a,de.b+b.b,de.c+b.c});DM[v][j][k]=U(1)<<z;}}
 }
 int pointmon[7]={};for(int p=1;p<8;++p){for(int j=0;j<15;++j){E e=m4[j];int v=((!(e.a)|| (p&4))&&(!(e.b)||(p&2))&&(!(e.c)||(p&1)));if(v)pointmon[p-1]|=1<<j;}}
 int bt[7][2]={};
 for(int l=1;l<8;++l){vector<int> vec; for(int p=1;p<8;++p)if(pp(l&p)==0)vec.push_back(p);if(vec.size()!=3)abort();int u=vec[0],v=vec[1];
 for(int j=0;j<15;++j){auto e=m4[j];int coeff[5]={1,0,0,0,0};E ex=e;int pows[3]={e.a,e.b,e.c};for(int q=0;q<3;++q){int newcoeff[5]={};int uval=(u>>(2-q))&1,vval=(v>>(2-q))&1;for(int h=0;h<=4;++h)if(coeff[h]){for(int t=0;t<=pows[q];++t){int h2=h+t;if(h2>4)abort();if((t&pows[q])==t &&(t==0||vval)&&(pows[q]-t==0||uval))newcoeff[h2]^=1;}}copy(newcoeff,newcoeff+5,coeff);}
 for(int k=0;k<2;++k){if(coeff[k?3:1])bt[l-1][k]|=1<<j;}
 }
 }
 long long cnt=0, counts[8]={}, points[8][8]={};map<pair<int,int>,long long> joint;map<int,long long> btsets;map<int,int> witnesses;
 auto rank=[&](int mask)->bool{U bas[66]={};int r=0;auto add=[&](U x){while(x){int p=0;U y=x;while(y>>1){y>>=1;++p;}if(!bas[p]){bas[p]=x;++r;break;}x^=bas[p];}};for(int k=0;k<28&&r<66;++k){U x=0;for(int j=0;j<15;++j)if(mask>>j&1)x^=FM[j][k];add(x);}for(int v=0;v<3&&r<66;++v)for(int k=0;k<36&&r<66;++k){U x=0;for(int j=0;j<15;++j)if(mask>>j&1)x^=DM[v][j][k];add(x);}return r==66;};
 for(int mask=1;mask<32768;++mask){if(!rank(mask))continue;int bset=0,rset=0;for(int l=0;l<7;++l)if(!pp(mask&bt[l][0])&&!pp(mask&bt[l][1]))bset|=1<<l;for(int p=0;p<7;++p)if(!pp(mask&pointmon[p]))rset|=1<<p;cnt++;int b=__builtin_popcount((unsigned)bset),r=__builtin_popcount((unsigned)rset);counts[b]++;points[r][b]++;btsets[bset]++;joint[{r,b}]++;if(b>=4&&witnesses.find(b)==witnesses.end())witnesses[b]=mask;
 }
 cout<<"smooth="<<cnt<<"\n";for(int i=0;i<=7;++i)cout<<"b="<<i<<" count="<<counts[i]<<"\n";cout<<"nonzero bitangent subsets="<<btsets.size()<<"\n";for(auto [s,c]:btsets)cout<<"bitset="<<s<<" count="<<c<<"\n";cout<<"JOINT\n";for(auto [z,c]:joint)cout<<z.first<<","<<z.second<<":"<<c<<"\n";for(auto [b,f]:witnesses)cout<<"witness="<<b<<":"<<f<<"\n";
}
