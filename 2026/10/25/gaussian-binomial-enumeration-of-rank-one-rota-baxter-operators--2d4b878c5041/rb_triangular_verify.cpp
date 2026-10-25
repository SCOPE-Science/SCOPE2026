#include <bits/stdc++.h>
using namespace std;
// Upper triangular matrix units in order 11,22,33,12,23,13.
const int NN=6;
const int r[6]={0,1,2,0,1,0}, c[6]={0,1,2,1,2,2};
using V=array<int,NN>;
V mul(const V &a,const V &b,int q){V z{};for(int i=0;i<6;i++)if(a[i])for(int j=0;j<6;j++)if(b[j]&&c[i]==r[j]){for(int h=0;h<6;h++)if(r[h]==r[i]&&c[h]==c[j]){z[h]=(z[h]+a[i]*b[j])%q;break;}}return z;}
int dot(const V&a,const V&b,int q){int z=0;for(int i=0;i<6;i++)z=(z+a[i]*b[i])%q;return z;}
V decode(int x,int q){V v{};for(int i=0;i<6;i++){v[i]=x%q;x/=q;}return v;}
int main(){for(int q:{2,3}){
 int sz=1;for(int i=0;i<6;i++)sz*=q;long long nil=0,other=0,rb=0,lines=0; 
 for(int u0=1;u0<sz;u0++) {V u=decode(u0,q);int h=0;while(h<6&&u[h]==0)h++;if(u[h]!=1)continue;lines++;V u2=mul(u,u,q);
 V left[6],right[6];for(int j=0;j<6;j++){V e{};e[j]=1;left[j]=mul(u,e,q);right[j]=mul(e,u,q);}
 for(int f0=1;f0<sz;f0++){V f=decode(f0,q);int L[6],R[6];for(int j=0;j<6;j++){L[j]=dot(f,left[j],q);R[j]=dot(f,right[j],q);}bool ok=true;
 for(int i=0;i<6&&ok;i++)for(int j=0;j<6&&ok;j++){int coeff=(f[i]*L[j]+f[j]*R[i])%q;int lhs=f[i]*f[j]%q;for(int t=0;t<6;t++)if((lhs*u2[t]-coeff*u[t])%q!=0){ok=false;break;}}
 if(ok){rb++;bool iszero=true;for(int t:u2)if(t!=0)iszero=false;if(iszero)nil++;else other++;}
 }
 }
 long long prednil=2LL*q*(1LL*q*q*q*q-1)+1LL*q*q*q*q*q-1;
 long long predother=4LL*q*q*(q*q+q-2);
 cout<<"q="<<q<<" projective_lines="<<lines<<" actual="<<rb<<" nilpotent_image="<<nil<<" idempotent_line="<<other<<" predicted="<<prednil+predother<<" parts="<<prednil<<","<<predother<<"\n";
 if(nil!=prednil||other!=predother)return 2;
 }
 cout<<"UT3_RANK_ONE_RB_DIRECT_OK\n";
}
