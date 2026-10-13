#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;
struct Field {
 int q;
 int add(int a,int b)const{
   if(q==4||q==8)return a^b;
   if(q==9)return ((a%3+b%3)%3)+3*((a/3+b/3)%3);
   return (a+b)%q;
 }
 int mult(int a,int b)const{
   if(q==4||q==8){int mask=q-1,poly=q==4?7:11;int v=0;
    while(b){if(b&1)v^=a;b>>=1;a<<=1;if(a&q)a^=poly;}return v&mask;}
   if(q==9){int x=a%3,y=a/3,z=b%3,w=b/3;return ((x*z+2*y*w)%3)+3*((x*w+y*z)%3);}
   return a*b%q;
 }
};
int lcsBit(const vector<int>&alpha,const vector<int>&bb){
 uint64_t mask[16]={};for(int i=0;i<(int)alpha.size();++i)mask[alpha[i]]|=1ULL<<i;
 uint64_t d=0;
 for(int b:bb){uint64_t x=mask[b]|d,y=(d<<1)|1; d=x & ~(x-y);}
 return __builtin_popcountll(d);
}
int lcsDP(const vector<int>&x,const vector<int>&y){int q=x.size();vector<int>p(q+1),c(q+1);for(int a:x){c[0]=0;for(int j=1;j<=q;j++)c[j]=(a==y[j-1]?p[j-1]+1:max(c[j-1],p[j]));p.swap(c);}return p[q];}
int main(int argc,char**argv){
 int q=(argc>1?atoi(argv[1]):7); Field f{q};vector<int>v(q);for(int i=0;i<q;i++)v[i]=i;
 // sanity check fields: all nonzero multipliers yield permutations
 for(int a=1;a<q;a++){vector<bool>seen(q);for(int i=0;i<q;i++){int j=f.mult(a,i); if(j<0||j>=q||seen[j])abort();seen[j]=1;}}
 vector<int>rest;for(int i=2;i<q;i++)rest.push_back(i);
 map<int,long long>hist;map<int,vector<int>>rep;
 long long count=0;
 do{
  v[0]=0;v[1]=1;for(int j=2;j<q;j++)v[j]=rest[j-2];
  int worst=0;
  for(int a=1;a<q;a++)for(int b=0;b<q;b++){
   if(a==1&&b==0)continue;
   vector<int>t(q);
   for(int j=0;j<q;j++)t[j]=f.add(f.mult(a,v[j]),b);
   int cur=lcsBit(v,t);
   if(q<=7 && lcsDP(v,t)!=cur){fprintf(stderr,"LCS FAIL q=%d\n",q);exit(1);}
   worst=max(worst,cur);
  }
  hist[worst]++;if(!rep.count(worst))rep[worst]=v;
  count++;
 }while(next_permutation(rest.begin(),rest.end()));
 printf("q=%d normalized=%lld",q,count);
 for(auto [l,n]:hist)printf(" LCS%d=%lld",l,n);
 putchar('\n');
 for(auto [l,r]:rep){printf("q%d maxLCS%d example:",q,l);for(auto x:r)printf(" %d",x);printf("\n");}
 return 0;
}
