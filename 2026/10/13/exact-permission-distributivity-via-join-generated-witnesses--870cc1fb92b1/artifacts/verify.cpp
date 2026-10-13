// Standalone finite verification of exact-permission distributivity.
// g++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <cstdio>
#include <cassert>
#include <cstdint>
#include <vector>
#include <array>
using namespace std;
struct TestSpace {
  int n; int J[4][4]{}; int closed[16]{}; int disj[16][16]{};
  vector<int> admissible;
  TestSpace(int m,bool boolean_four=false):n(m){
    for(int i=0;i<n;i++)for(int j=0;j<n;j++) J[i][j]=boolean_four?(i|j):(i>j?i:j);
    for(int mask=0;mask<(1<<n);mask++){
      int c=mask; bool change=true;
      while(change){change=false;for(int i=0;i<n;i++)for(int j=0;j<n;j++)
        if((c&(1<<i))&&(c&(1<<j))&&!(c&(1<<J[i][j]))){c|=1<<J[i][j];change=true;}}
      closed[mask]=c;
      if(mask==c)admissible.push_back(mask);
    }
    for(int A=0;A<(1<<n);A++)for(int B=0;B<(1<<n);B++)disj[A][B]=closed[A|B];
  }
  bool permits(int rel,int s,int t)const{return !!(rel&(1<<(n*s+t)));}
  int permission_pre(int rel,int A)const{int b=0;for(int s=0;s<n;s++)for(int t=0;t<n;t++)if((A&(1<<t))&&permits(rel,s,t))b|=1<<s;return b;}
  bool check(int rel,bool& C1,bool& Cvee,bool& Valid){
    C1=Cvee=true;
    for(int s=0;s<n;s++)for(int t=0;t<n;t++)for(int u=0;u<n;u++)if(permits(rel,s,J[t][u])){
      int P=permission_pre(rel,(1<<t)|(1<<u));
      if(!permits(rel,s,t)&&!permits(rel,s,u))C1=false;
      if(!(closed[P]&(1<<s)))Cvee=false;
    }
    int diamond[16]{};
    for(int A=0;A<(1<<n);A++)diamond[A]=closed[permission_pre(rel,A)];
    Valid=true;
    for(int A:admissible)for(int B:admissible){
      int lhs=diamond[disj[A][B]];
      int rhs=disj[diamond[A]][diamond[B]];
      if(lhs!=rhs){Valid=false;return false;}
    }
    return true;
  }
};
int main(){
  for(int n=1;n<=4;n++){
    TestSpace test(n,n==4);int num=1<<(n*n);
    int count_C1=0,count_Cvee=0,count_valid=0,count_strict=0;
    for(int rel=0;rel<num;rel++){
      bool a,b,c;test.check(rel,a,b,c);
      if(a)count_C1++;
      if(b)count_Cvee++;
      if(c)count_valid++;
      if(b&&!a)count_strict++;
      assert(b==c);assert(!a||b);
      if(n==4&&rel==33824){assert(b&&!a&&c);}
    }
    printf("n=%d relations=%d admissible=%zu C1=%d exact_condition=%d schema_valid=%d strict=%d\n",n,num,test.admissible.size(),count_C1,count_Cvee,count_valid,count_strict);
    if(n<=3)assert(count_strict==0);
    if(n==4)assert(count_strict>0);
  }
  puts("VERIFY_OK");
}
