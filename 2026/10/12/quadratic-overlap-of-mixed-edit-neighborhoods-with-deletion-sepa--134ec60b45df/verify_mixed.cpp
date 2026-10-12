// Exact finite-state certificate for the quadratic common-output family.
// Compile: c++ -O2 -std=c++17 verify_mixed.cpp -o verify_mixed && ./verify_mixed
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <vector>
using U=uint64_t;
using State=std::pair<int,int>;
int trans(int s,int x,int w){
 int t=0;
 if(s&1){if(x==w)t|=1; t|=2|(1<<(2+w))|(1<<(4+x));}
 if((s&2)&&x==w)t|=2;
 for(int p=0;p<2;p++){
  if((s&(1<<(2+p)))&&x==p)t|=2|(1<<(2+w));
  if((s&(1<<(4+p)))&&w==p)t|=2|(1<<(4+x));
 }
 return t;
}
using Mat=std::vector<std::vector<U>>;
Mat zero(int d){return Mat(d,std::vector<U>(d));}
Mat identity(int d){auto m=zero(d);for(int i=0;i<d;i++)m[i][i]=1;return m;}
Mat multiply(const Mat&A,const Mat&B){
 int d=A.size();Mat C=zero(d);
 for(int i=0;i<d;i++)for(int k=0;k<d;k++)if(A[i][k])
  for(int j=0;j<d;j++)if(B[k][j])C[i][j]+=A[i][k]*B[k][j];
 return C;
}
U rowsum(const Mat&A,int i){U r=0;for(U x:A[i])r+=x;return r;}
int main(){
 std::vector<State> states={{1,1}};
 std::map<State,int> ids;ids[{1,1}]=0;
 for(size_t i=0;i<states.size();i++){
  auto [s,t]=states[i];
  for(int a=0;a<2;a++)for(int b=0;b<2;b++)for(int w=0;w<2;w++){
   int u=trans(s,a,w),v=trans(t,b,w);
   if(!u||!v)continue;
   State next={u,v};
   if(!ids.count(next)){ids[next]=(int)states.size();states.push_back(next);}
  }
 }
 int d=states.size();
 if(d!=64){std::cerr<<"Unexpected reachable state count "<<d<<"\n";return 1;}
 Mat T[2][2];
 for(int a=0;a<2;a++)for(int b=0;b<2;b++){
  T[a][b]=zero(d);
  for(int i=0;i<d;i++)for(int w=0;w<2;w++){
   auto [s,t]=states[i];int u=trans(s,a,w),v=trans(t,b,w);
   if(u&&v)T[a][b][i][ids.at({u,v})]++;
  }
 }
 const Mat& Z=T[0][0]; const Mat& O=T[1][1];
 Mat core=identity(d);
 for(auto [a,b]:std::vector<State>{{0,1},{1,0},{1,0},{0,1}})
  core=multiply(core,T[a][b]);
 Mat P=multiply(Z,O),Q=multiply(O,Z);
 struct Case {int c;Mat k;Mat right;const char* label;};
 std::vector<Case> cases;
 cases.push_back({4,core,P,"4r+4"});
 cases.push_back({6,multiply(multiply(Z,core),O),P,"4r+6"});
 cases.push_back({5,multiply(Z,core),Q,"4r+5"});
 cases.push_back({7,multiply(multiply(P,core),Z),Q,"4r+7"});
 // For each class: a_r = initial_row(P^r K right^r) * all_ones.
 // X_(r+1)=P X_r right. Cayley-Hamilton gives recurrence order <=d*d.
 // The target quadratic has recurrence order 3, so d*d+3 checked
 // consecutive values certify equality for every r, not just small r.
 const int tests=d*d+3;
 for(auto &c:cases){
  Mat X=c.k;
  // Use sparse row lists to avoid dense matrix multiplications inside the loop.
  std::vector<std::vector<std::pair<int,U>>> left(d),right(d);
  for(int i=0;i<d;i++)for(int j=0;j<d;j++){
   if(P[i][j])left[i].push_back({j,P[i][j]});
   if(c.right[i][j])right[i].push_back({j,c.right[i][j]});
  }
  for(int r=0;r<tests;r++){
   U n=4ULL*r+c.c, expect=n*n/4+4;
   U observed=rowsum(X,0);
   if(observed!=expect){
    std::cerr<<"MISMATCH "<<c.label<<" r="<<r<<" count="<<observed<<" expected="<<expect<<"\n";
    return 2;
   }
   if(r+1==tests)break;
   Mat Y=zero(d),next=zero(d);
   for(int i=0;i<d;i++)for(auto [j,mult]:left[i])
    for(int k=0;k<d;k++)Y[i][k]+=mult*X[j][k];
   for(int i=0;i<d;i++)for(int j=0;j<d;j++)if(Y[i][j])
    for(auto [k,mult]:right[j])next[i][k]+=Y[i][j]*mult;
   X.swap(next);
  }
  std::cout<<"RESIDUE_OK "<<c.label<<" checked="<<tests<<"\n";
 }
 std::cout<<"VERIFY_OK states="<<d<<" matrix_dimension="<<d*d
          <<" initial_terms_per_residue="<<tests<<" all_n_at_least_4=proved\n";
}
