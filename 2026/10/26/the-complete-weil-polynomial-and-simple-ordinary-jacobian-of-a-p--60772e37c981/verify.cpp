#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <numeric>
#include <cassert>
using namespace std;
class GF{
public:int m,q,N;vector<int> P,pow3,E,L,Z,negv;
 GF(int m_, vector<int> cs):m(m_),P(cs){q=1;pow3={1};for(int i=1;i<m;i++)pow3.push_back(pow3.back()*3);for(int i=0;i<m;i++)q*=3; N=q-1;E.resize(N);L.assign(q,-1); Z.resize(N);negv.resize(q);
  int x=1;for(int i=0;i<N;i++){if(L[x]!=-1){fprintf(stderr,"nonprimitive m=%d\n",m);exit(1);}E[i]=x;L[x]=i;x=times_gen(x);}if(x!=1){fprintf(stderr,"wrong period\n");exit(1);}
  for(int i=0;i<N;i++){int a=plus_poly(1,E[i]);Z[i]=a?L[a]:-1;}
  for(int a=1;a<q;a++)negv[a]=E[(L[a]+N/2)%N];
 }
 int plus_poly(int a,int b)const{int r=0,t=1;for(int i=0;i<m;i++){int c=(a%3+b%3)%3;r+=c*t;a/=3;b/=3;t*=3;}return r;}
 int times_gen(int a)const{if(m==1)return (a*2)%3;int c=a/pow3[m-1],r=(a*3)%q; for(int i=0;i<m;i++){int digit=(r/pow3[i])%3,nd=(digit-c*P[i]%3+3)%3;r+=(nd-digit)*pow3[i];}return r;}
 inline int add(int a,int b)const{if(!a)return b;if(!b)return a;int i=L[a],j=L[b];if(i>j){int t=i;i=j;j=t;}int z=Z[j-i];if(z<0)return 0;int k=i+z;if(k>=N)k-=N;return E[k];}
 inline int neg(int a)const{return negv[a];}
 inline int sub(int a,int b)const{return add(a,negv[b]);}
 inline int mul(int a,int b)const{if(!a||!b)return 0;int k=L[a]+L[b];if(k>=N)k-=N;return E[k];}
 int power(int a,int n)const{int res=1;while(n){if(n&1)res=mul(res,a);a=mul(a,a);n>>=1;}return res;}
 int inv(int a)const{assert(a);return E[(N-L[a])%N];}
};
int degree(const vector<int>&v){for(int i=(int)v.size()-1;i>=0;i--)if(v[i])return i;return -1;}
vector<int> residue(vector<int> a,vector<int> b,const GF&g){int db=degree(b);assert(db>=0);int inv=g.inv(b[db]);for(int k=degree(a);k>=db;k--){int v=a[k];if(v){int t=g.mul(v,inv);for(int j=0;j<=db;j++)a[k-db+j]=g.sub(a[k-db+j],g.mul(t,b[j]));}}a.resize(db);return a;}
int gcddegree(vector<int>a,vector<int>b,const GF&g){while(degree(b)>=0){auto r=residue(a,b,g);a=std::move(b);b=std::move(r);}return degree(a);}
int root_count(int x,const GF &g){int x3=g.power(x,3),x5=g.power(x,5);int a=g.neg(g.add(x3,1)),b=x5,c=g.add(g.add(x5,x3),x);
 vector<int> f(6);f[0]=c;f[1]=b;f[3]=a;f[5]=1;
 vector<int> h(5);h[1]=1;
 for(int i=0;i<g.m;i++){
  vector<int> h3(13);
  for(int j=0;j<5;j++)h3[3*j]=g.power(h[j],3);
  for(int j=12;j>=5;j--){int v=h3[j]; if(!v){continue;}
   h3[j]=0;h3[j-5]=g.sub(h3[j-5],g.mul(v,c));h3[j-4]=g.sub(h3[j-4],g.mul(v,b));h3[j-2]=g.sub(h3[j-2],g.mul(v,a));
  }
  for(int j=0;j<5;j++)h[j]=h3[j];
 }
 h[1]=g.sub(h[1],1);return gcddegree(f,h,g);
}
int main(){vector<vector<int>> prim={{1},{2,1},{1,2,0},{2,1,0,0},{1,2,0,0,0},{2,1,0,0,0,0},{1,2,1,0,0,0,0},{2,0,0,1,0,0,0,0},{1,0,1,2,0,0,0,0,0},{2,1,0,1,0,0,0,0,0,0}};
 for(int m=1;m<=10;m++){
  GF g(m,prim[m-1]); long long count=4; for(int x=0;x<g.q;x++)count+=root_count(x,g);
  if(m<=5){long long brute=4;for(int x=0;x<g.q;x++){int x3=g.power(x,3),x5=g.power(x,5);for(int y=0;y<g.q;y++){int y3=g.power(y,3),y5=g.power(y,5);int val=g.add(g.add(g.add(g.add(x5,g.mul(x5,y)),g.neg(g.mul(x3,y3))),x3),x);val=g.add(g.add(val,y5),g.neg(y3));if(!val)brute++;}}if(brute!=count){fprintf(stderr,"BRUTE_MISMATCH %d %lld %lld\n",m,brute,count);return 2;}}
  printf("m=%d q=%d N=%lld\n",m,g.q,count);fflush(stdout);
 }
 puts("VERIFY_OK");return 0;
}
