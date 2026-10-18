// Exact finite certificate for variance-order reversals under one degree-preserving ecological rewiring.
// C++17, standard library only. Compile: g++ -O3 -std=c++17 rewiring_verifier.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
int bits(int n){return __builtin_popcount((unsigned)n);}
i64 choose(int n,int k){if(k<0||k>n)return 0;i64 p=1;for(int i=1;i<=k;i++)p=p*(n-i+1)/i;return p;}
bool connected(const vector<int>&r,int b){
 int a=r.size(),seen=1,full=(1<<(a+b))-1;
 for(int step=0;step<a+b;step++){
  int old=seen;
  for(int i=0;i<a;i++)if(seen&(1<<i))for(int j=0;j<b;j++)if(r[i]&(1<<j))seen|=1<<(a+j);
  for(int j=0;j<b;j++)if(seen&(1<<(a+j)))for(int i=0;i<a;i++)if(r[i]&(1<<j))seen|=1<<i;
  if(old==seen)break;
 }
 return seen==full;
}
vector<int> pair_union_hist(const vector<int>&r,int b){
 vector<int>h(b+1,0);
 for(int i=0;i<(int)r.size();i++)for(int j=i+1;j<(int)r.size();j++)h[bits(r[i]|r[j])]++;
 return h;
}
// If the transformed coefficients have one sign, the polynomial has one sign on (0,1).
bool fixed_sign_on_unit_interval(const vector<int>&p,int b){
 bool pos=false,neg=false;
 for(int j=0;j<=b;j++){
  i64 h=0;
  for(int k=0;k<=j;k++)h+=p[k]*choose(b-k,j-k);
  pos|=(h>0);neg|=(h<0);
 }
 return !(pos&&neg);
}
i64 connected_count_recurrence(int a,int b,vector<vector<i64>>&C){
 if(b==0)return a==1?1:0;
 i64 val=1LL<<(a*b);
 for(int i=1;i<=a;i++)for(int j=0;j<=b;j++){
  if(i==a&&j==b)continue;
  val-=choose(a-1,i-1)*choose(b,j)*C[i][j]*(1LL<<((a-i)*(b-j)));
 }
 return val;
}
void lower_bound(){
 vector<vector<i64>>C(10,vector<i64>(10,0));
 for(int a=1;a<=8;a++)C[a][0]=(a==1);
 for(int n=2;n<=9;n++)for(int a=1;a<n;a++){
  int b=n-a;C[a][b]=connected_count_recurrence(a,b,C);
  i64 scanned=0,swaps=0;set<vector<int>>polynomials;
  i64 total=1LL<<(a*b);vector<int>r(a);
  for(i64 mask=0;mask<total;mask++){
   i64 x=mask;for(int i=0;i<a;i++){r[i]=int(x&((1<<b)-1));x>>=b;}
   if(!connected(r,b))continue;
   scanned++;auto original=pair_union_hist(r,b);
   for(int i=0;i<a;i++)for(int j=i+1;j<a;j++){
    int left=r[i]&~r[j],right=r[j]&~r[i];
    while(left){int p=__builtin_ctz((unsigned)left);left&=left-1;int rm=right;
     while(rm){int t=__builtin_ctz((unsigned)rm);rm&=rm-1;
      vector<int>post=r;post[i]^=(1<<p)|(1<<t);post[j]^=(1<<p)|(1<<t);
      if(!connected(post,b))continue;
      swaps++;auto changed=pair_union_hist(post,b);
      vector<int>d(b+1);for(int k=0;k<=b;k++)d[k]=changed[k]-original[k];
      polynomials.insert(d);
      if(!fixed_sign_on_unit_interval(d,b)){
       cerr<<"FAIL: mixed sign transformed coefficients for a="<<a<<" b="<<b<<"\n";exit(1);
      }
     }
    }
   }
  }
  if(scanned!=C[a][b]){
   cerr<<"FAIL connected count a="<<a<<" b="<<b<<" counted="<<scanned<<" recurrence="<<C[a][b]<<"\n";exit(1);
  }
  cout<<"a="<<a<<" b="<<b<<" connected="<<scanned<<" swaps="<<swaps<<" distinct_differences="<<polynomials.size()<<" OK\n";
 }
}
void witness(){
 vector<int>A={22,3,12,25,3},B={22,6,9,25,3};int b=5;
 if(!connected(A,b)||!connected(B,b)){cerr<<"FAIL witness connectivity\n";exit(1);}
 for(int i=0;i<5;i++)if(bits(A[i])!=bits(B[i])||bits(A[i])<2||bits(B[i])<2){cerr<<"FAIL plant degree\n";exit(1);}
 vector<int>da(5,0),db(5,0);
 for(int i=0;i<5;i++)for(int j=0;j<b;j++){da[j]+=(A[i]>>j)&1;db[j]+=(B[i]>>j)&1;}
 if(da!=db){cerr<<"FAIL pollinator degrees\n";exit(1);}
 for(auto d:da)if(d<2){cerr<<"FAIL pollinator degree at least two\n";exit(1);}
 int changedRows=0,changedCols=0;
 for(int i=0;i<5;i++)if(A[i]!=B[i])changedRows++;
 int colmask=0;for(int i=0;i<5;i++)colmask|=(A[i]^B[i]);changedCols=bits(colmask);
 if(changedRows!=2||changedCols!=2){cerr<<"FAIL checkerboard\n";exit(1);}
 for(int j=0;j<b;j++)if(colmask&(1<<j)){
  int colA=0,colB=0;for(int i=0;i<5;i++){colA|=((A[i]>>j)&1)<<i;colB|=((B[i]>>j)&1)<<i;}
  if(bits(colA^colB)!=2){cerr<<"FAIL checkerboard column\n";exit(1);}
 }
 auto a=pair_union_hist(A,b),h=pair_union_hist(B,b);
 vector<int>expected={0,0,-1,4,-5,2};
 for(int k=0;k<=b;k++)if(h[k]-a[k]!=expected[k]){
  cerr<<"FAIL difference coefficient at "<<k<<"\n";exit(1);
 }
 // Directly enumerate all 2^5 failure configurations to check the same exact moment difference.
 // For fixed q=u/v, each failure mask has integer numerator u^f(v-u)^(b-f), denominator v^b.
 for(int u:{1,3}){
  int v=4; i64 means[2]={},squares[2]={};vector<vector<int>>R={A,B};
  for(int w=0;w<2;w++)for(int failed=0;failed<(1<<b);failed++){
   int f=bits(failed),extinct=0;
   for(int row:R[w])if((row&failed)==row)extinct++;
   i64 prob=1;for(int k=0;k<f;k++)prob*=u;for(int k=f;k<b;k++)prob*=v-u;
   means[w]+=prob*extinct;squares[w]+=prob*extinct*extinct;
  }
  if(means[0]!=means[1]){cerr<<"FAIL means\n";exit(1);}
  i64 den=1;for(int k=0;k<b;k++)den*=v;
  i64 squaredDifference=squares[1]-squares[0];
  // The two moments: expected variance difference is 2 P(u/v); compare scaled integers.
  i64 polyScaled=0,powu[6]={1},powv[6]={1};for(int k=1;k<=b;k++){powu[k]=powu[k-1]*u;powv[k]=powv[k-1]*v;}
  for(int k=0;k<=b;k++)polyScaled+=2LL*expected[k]*powu[k]*powv[b-k];
  if(squaredDifference!=polyScaled){cerr<<"FAIL direct moment identity\n";exit(1);}
  if((u==1&&squaredDifference>=0)||(u==3&&squaredDifference<=0)){
   cerr<<"FAIL variance crossover\n";exit(1);
  }
  cout<<"q="<<u<<"/4 E[Z] numerator="<<means[0]<<" denominator="<<den
      <<" variance difference numerator="<<squaredDifference<<" denominator="<<den<<" OK\n";
 }
 cout<<"WITNESS_OK min-degree-two 5+5, variance(B)-variance(A)=-2 q^2(1-q)^2(1-2q)\n";
}
int main(){lower_bound();witness();cout<<"ALL_EXACT_CHECKS_PASSED\n";}
