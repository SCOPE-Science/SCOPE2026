#include <bits/stdc++.h>
using namespace std;
static const int polynomials[]={0,3,7,11,19,37,67,131};
int main(){
 for(int n=1;n<=7;n++){
  int q=1<<n,mod=polynomials[n];
  vector<unsigned char> mul(q*q);
  for(int a=0;a<q;a++) for(int b=0;b<q;b++){
   int x=a,y=b,z=0;
   while(y){if(y&1)z^=x; y>>=1; x<<=1;if(x&q)x^=mod;}
   mul[a*q+b]=z;
  }
  vector<unsigned char> sq(q);for(int i=0;i<q;i++)sq[i]=mul[i*q+i];
  long long total=0,pts=0;
  auto eval=[&](int a,int b,int c,int d,int e){return (mul[sq[a]*q+b]^mul[sq[b]*q+c]^mul[sq[c]*q+d]^mul[sq[d]*q+e]^mul[sq[e]*q+a])==0;};
  for(int i=0;i<5;i++){
   long long bound=1; for(int j=i+1;j<5;j++)bound*=q;
   for(long long idx=0;idx<bound;idx++){
    int coord[5]={},k=idx;coord[i]=1;
    for(int j=i+1;j<5;j++){coord[j]=k%q;k/=q;}
    total++;if(eval(coord[0],coord[1],coord[2],coord[3],coord[4]))pts++;
   }
  }
  long long predicted=1LL+q+1LL*q*q+1LL*q*q*q;
  if(total != (1LL*q*q*q*q*q-1)/(q-1) || pts!=predicted){fprintf(stderr,"FAIL n=%d: pts=%lld predicted=%lld\n",n,pts,predicted);return 1;}
  printf("n=%d q=%d total=%lld pts=%lld traceH3=%lld\n",n,q,total,pts,predicted-pts);
 }
  puts("VERIFY_OK");
}
