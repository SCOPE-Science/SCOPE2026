// Complete GL_3(F4)-orbit of the Hermitian cubic; compare normalized forms.
#include <bits/stdc++.h>
using namespace std;
int mul(int a,int b){int v=0;for(int i=0;i<2;i++)if((b>>i)&1)v^=a<<i;if(v&8)v^=12;if(v&4)v^=7;return v;}
int inv(int a){return a==1?1:a==2?3:a==3?2:0;}
bool independent(int A[3][3]){int B[3][3];memcpy(B,A,sizeof(B));int k=0;for(int j=0;j<3;j++){int p=-1;for(int i=k;i<3;i++)if(B[i][j]){p=i;break;}if(p<0)continue;for(int v=0;v<3;v++)swap(B[k][v],B[p][v]);int t=inv(B[k][j]);for(int v=j;v<3;v++)B[k][v]=mul(B[k][v],t);for(int i=k+1;i<3;i++)if(B[i][j]){int t=B[i][j];for(int v=j;v<3;v++)B[i][v]^=mul(t,B[k][v]);}k++;}return k==3;}
int main(){set<uint32_t> orbit;int gl=0, stabil=0;for(int code=0;code<(1<<18);code++) {int t=code,A[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++){A[i][j]=t&3;t>>=2;}if(!independent(A))continue;gl++;int c[10]={};for(int i=0;i<3;i++){int a=A[i][0],b=A[i][1],z=A[i][2];int v[10]={mul(mul(a,a),a),mul(mul(a,a),b),mul(mul(a,a),z),mul(a,mul(b,b)),0,mul(a,mul(z,z)),mul(mul(b,b),b),mul(mul(b,b),z),mul(b,mul(z,z)),mul(mul(z,z),z)};for(int k=0;k<10;k++)c[k]^=v[k];}int highest=-1;for(int i=0;i<10;i++)if(c[i])highest=i;if(highest<0)abort();int z=inv(c[highest]);uint32_t id=0;for(int j=0;j<10;j++)id|=(uint32_t)mul(c[j],z)<<(2*j);orbit.insert(id);if(id==((1u<<0)|(1u<<12)|(1u<<18)))stabil++;}
cout<<"GL3(F4)="<<gl<<" hermitian stabilizer in GL="<<stabil<<" projective stabilizer="<<stabil/3<<" distinct cubic orbit="<<orbit.size()<<"\n";
ifstream input("smooth_codes.txt");set<uint32_t> all;uint32_t c;while(input>>c)all.insert(c);cout<<"orbit equality with smooth tangent filling="<<(all==orbit?"YES":"NO")<<" hermitian in orbit="<<bool(orbit.count((1u<<0)|(1u<<12)|(1u<<18)))<<"\n";ifstream input2("tangent_noline_codes.txt");set<uint32_t> b;while(input2>>c)b.insert(c);cout<<"orbit equality with no-rational-line tangent cubics="<<(b==orbit?"YES":"NO")<<"\n";
}
