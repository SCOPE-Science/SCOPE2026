#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const ll P=1004221;
ll pw(ll a,ll k){ll y=1;for(;k;k>>=1,a=a*a%P)if(k&1)y=y*a%P;return y;}
int phi(int n){int ans=n;for(int p=2;p*p<=n;p++)if(n%p==0){while(n%p==0)n/=p;ans-=ans/p;}if(n>1)ans-=ans/n;return ans;}
ll predict(int n,int a,int b,int c){
 ll prim=6; // primitive modulo 1004221; direct integer checks for factors 2,3,5,7,797
 if((P-1)%n) throw runtime_error("modulus does not divide multiplicative-group order");
 for(int f:{2,3,5,7,797}) if(pw(prim,(P-1)/f)==1) throw runtime_error("primitive-root check failed");
 ll root=pw(prim,(P-1)/n);
 ll out=1;
 for(int m=1;m<=n;m++)if(n%m==0){int t=n/m;ll total=1;
  for(int i=0;i<t;i++)for(int j=0;j<t;j++){
   ll eta=pw(root,m*i),the=pw(root,m*j);
   ll term=(pw(a,m)+pw(b,m)*eta+pw(c,m)*the)%P;
   total=total*pw(term,(ll)m*phi(m))%P;
  }
  out=out*total%P;
 }
 return out;
}
int rank_det(int n,int a,int b,int c, ll &det){
 int N=n*n*n; vector<int> A((size_t)N*N,0);
 auto idx=[&](int x,int y,int z){return (x*n+y)*n+z;};
 for(int x=0;x<n;x++)for(int y=0;y<n;y++)for(int z=0;z<n;z++){
  int q=idx(x,y,z);
  A[(size_t)q*N+q]=(A[(size_t)q*N+q]+a)%P;
  A[(size_t)idx((x+1)%n,y,(z+y)%n)*N+q]=(A[(size_t)idx((x+1)%n,y,(z+y)%n)*N+q]+b)%P;
  A[(size_t)idx(x,(y+1)%n,z)*N+q]=(A[(size_t)idx(x,(y+1)%n,z)*N+q]+c)%P;
 }
 int rank=0;det=1;for(int col=0;col<N;col++){
  int pivot=rank;while(pivot<N && !A[(size_t)pivot*N+col])pivot++;
  if(pivot==N){det=0;continue;}
  if(rank!=pivot){for(int j=col;j<N;j++)swap(A[(size_t)rank*N+j],A[(size_t)pivot*N+j]);det=(P-det)%P;}
  ll v=A[(size_t)rank*N+col];det=det*v%P;ll inv=pw(v,P-2);
  for(int j=col;j<N;j++)A[(size_t)rank*N+j]=A[(size_t)rank*N+j]*inv%P;
  for(int i=rank+1;i<N;i++){
   ll mul=A[(size_t)i*N+col];if(!mul)continue;
   for(int j=col+1;j<N;j++)A[(size_t)i*N+j]=(A[(size_t)i*N+j]+P-mul*A[(size_t)rank*N+j]%P)%P;
   A[(size_t)i*N+col]=0;
  }
  rank++;
 }
 return rank;
}
int main(){
 for(ll d=2;d*d<=P;d++) if(P%d==0) {cerr<<"CHECK MODULUS NOT PRIME"<<endl;return 1;}
 for(int n:{3,5,7,9}){
  for(auto [a,b,c]:vector<tuple<int,int,int>>{{1,1,1},{2,3,5}}){
   ll d;int r=rank_det(n,a,b,c,d);ll pr=predict(n,a,b,c);
   if(d!=pr) {cerr<<"DETERMINANT MISMATCH"<<endl; return 1;}
   if(a==1 && b==1 && c==1) {
    int want = n==3?2 : n==9?14 : 0;
    if(n*n*n-r!=want) {cerr<<"UNWEIGHTED NULLITY MISMATCH"<<endl; return 1;}
   }
   cout<<"n="<<n<<" a,b,c="<<a<<","<<b<<","<<c<<" rank="<<r<<" nullity="<<n*n*n-r<<" det="<<d<<" pred="<<pr<<" match="<<(d==pr)<<"\n";
  }
 }
}
