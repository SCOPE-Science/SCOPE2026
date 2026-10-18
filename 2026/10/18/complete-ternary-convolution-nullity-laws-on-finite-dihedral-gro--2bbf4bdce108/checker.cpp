// Exact integer finite-group convolution and modular rank sanity checks.
// Reproduce: c++ -std=c++17 -O2 checker.cpp -o checker && ./checker
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int prod(int x,int y,int n){int a=x%n,b=y%n,e=x/n,f=y/n; return ((a+(e?-b:b)+n)%n)+(e^f)*n;}
int modrank(vector<int> mat,int M,int P){
 int h=0;
 for(int c=0;c<M&&h<M;c++){
  int i=h;while(i<M&&mat[i*M+c]%P==0)i++;
  if(i==M)continue;
  for(int j=c;j<M;j++)swap(mat[i*M+j],mat[h*M+j]);
  int64_t z=mat[h*M+c],v=1,e=P-2;
  while(e){if(e&1)v=v*z%P; z=z*z%P;e>>=1;}
  for(int j=c;j<M;j++)mat[h*M+j]=(int)((int64_t)mat[h*M+j]*v%P);
  for(int r=h+1;r<M;r++){
    int factor=mat[r*M+c];if(!factor)continue;
    for(int j=c;j<M;j++){int64_t v=mat[r*M+j]-(int64_t)factor*mat[h*M+j];v%=P;if(v<0)v+=P;mat[r*M+j]=(int)v;}
  }
  h++;
 }return h;
}
int predicted(int n,int a,int b,int c){
  int R=(a<n)+(b<n)+(c<n);
  if(R==0||R==3){
    int u=a%n,v=b%n,w=c%n;
    int d=std::gcd(n,std::gcd(abs(u-v),abs(u-w)));
    if((n/d)%3!=0)return 0;
    // The reductions modulo 3d must be in the three different cosets modulo d.
    if ((u-v)%d || (u-w)%d) return 0;
    int v1=((v-u)/d%3+3)%3, v2=((w-u)/d%3+3)%3;
    if(v1==v2 || v1==0 || v2==0)return 0;
    return 4*d;
  }
  int v[2],q=0;
  for(int t:{a,b,c})if((t<n)==(R==2))v[q++]=t%n;
  assert(q==2);
  int g=std::gcd(n,abs(v[0]-v[1]));
  return (n/g)%3==0?2*g:0;
}
int main(){
  const int P1=1000003, P2=1000033;
  for(int n=3;n<=14;n++){
    int M=2*n;int64_t singular=0, maxNull=0,total=0;
    vector<int64_t> histogram(M+1,0), predicted_hist(M+1,0);
    int vv=n,pp=1;while(vv%3==0){vv/=3;pp*=3;}
    int64_t expected=(int64_t)n*n*(n-vv)+(int64_t)n*n*n*(pp*pp-1)/(12*pp*pp);
    // Note second term may require rational arithmetic; integer after combining.
    expected=(int64_t)n*n*(n-vv) + ((int64_t)n*n*n-(int64_t)n*n*n/(pp*pp))/12;
    for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++){
      int pred=predicted(n,a,b,c);
      singular+=(pred>0); histogram[pred]++;
      maxNull=std::max(maxNull,(int64_t)pred);
      vector<int> mat(M*M,0);
      for(int s:{a,b,c})for(int x=0;x<M;x++)mat[prod(s,x,n)*M+x]++;
      int rk1=modrank(mat,M,P1),rk2=modrank(mat,M,P2);
      int nullity=M-max(rk1,rk2);
      if(nullity!=pred || M-rk1!=pred || M-rk2!=pred){cerr<<"FAIL n="<<n<<" ("<<a<<","<<b<<","<<c<<") predicted="<<pred<<" observed="<<nullity<<"\n";return 1;}
      total++;
    }
    for(int g=1;g<=n;g++)if(n%g==0 && (n/g)%3==0){
      int q=n/g,m=q;while(m%3==0)m/=3;
      int phi=q;for(int p=2;p<=q;p++)if(q%p==0){bool prime=true;for(int d=2;d*d<=p;d++)if(p%d==0)prime=false;if(prime)phi=phi/p*(p-1);}
      predicted_hist[2*g] += (int64_t)n*n*phi;
      int64_t T=(int64_t)2*(q/3)*(q/3);
      for(int p=2;p<=m;p++)if(m%p==0){bool prime=true;for(int d=2;d*d<=p;d++)if(p%d==0)prime=false;if(prime)T=T/(p*p)*(p*p-1);}
      if(n*T%3){cerr<<"DIVISIBILITY_FAIL n="<<n<<" g="<<g<<"\n";return 3;}
      predicted_hist[4*g] += n*T/3;
    }
    for(int u=1;u<=M;u++)if(histogram[u]!=predicted_hist[u]){cerr<<"STRATUM_FAIL n="<<n<<" nullity="<<u<<" got="<<histogram[u]<<" expected="<<predicted_hist[u]<<"\n";return 4;}
    if(singular!=expected){cerr<<"COUNT_FAIL n="<<n<<" actual="<<singular<<" expected="<<expected<<"\n";return 2;}
    cout<<"n="<<n<<" triple_sets="<<total<<" singular="<<singular<<" maximum_nullity="<<maxNull<<" OK\n";
  }
  cout<<"CHECK_PASS\n";
}
