#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int CAP=256;
using Bits=bitset<CAP>;
using Matrix=vector<Bits>;

Matrix adjacency(int n){
 Matrix a(2*n);
 auto edge=[&](int i,int j){assert(i!=j);a[i].set(j);a[j].set(i);};
 for(int i=0;i<n;i++){
   edge(i,(i+1)%n);edge(i,i+n);edge(n+i,n+(i+3)%n);
 }
 for(auto &r:a) assert(r.count()==3);
 return a;
}
Matrix multiply(const Matrix&a,const Matrix&b){
 int N=(int)a.size();Matrix c(N);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(a[i][j])c[i]^=b[j];
 return c;
}
int matrix_rank(Matrix a){
 int N=(int)a.size(), r=0;
 for(int col=0;col<N;col++){
  int k=r;while(k<N&&!a[k][col])k++;
  if(k==N)continue;
  swap(a[k],a[r]);
  for(int j=r+1;j<N;j++)if(a[j][col])a[j]^=a[r];
  r++;
 }
 return r;
}
int step(int state,const Matrix&a){
 int y=0,N=(int)a.size();
 for(int i=0;i<N;i++){
  unsigned int parity=0;
  for(int j=0;j<N;j++)if(a[i][j])parity^=(state>>j)&1;
  if(parity)y|=1<<i;
 }
 return y;
}

int main(){
 for(int n=7;n<=120;n++){
  Matrix a=adjacency(n), p(2*n);
  for(int i=0;i<2*n;i++)p[i].set(i);
  int e=1,odd=n;while(!(odd&1)){e*=2;odd>>=1;}
  if(n%5)e=0;
  int T=(e+1)/2;
  for(int t=0;t<=max(2,T+1);t++){
   int observed=matrix_rank(p);
   int expected=2*n-(e?4*min(2*t,e):0);
   if(observed!=expected){cerr<<"rank mismatch n="<<n<<" t="<<t<<" "<<observed<<" vs "<<expected<<"\n";return 1;}
   p=multiply(a,p);
  }
  Matrix plusI=a;for(int j=0;j<2*n;j++)plusI[j].flip(j);
  int fixdim=2*n-matrix_rank(plusI);
  int pp=n&-n; int expected_fix=min(4,pp)+(n%5==0?4:0);
  assert(fixdim==expected_fix);
  if(n==10||n==15||n==20||n==40||n==80||n==120)cout<<"n="<<n<<" stable_rank="<<2*n-4*e<<" first_periodic_time="<<T<<"\n";
 }
 cout<<"INDEPENDENT_MATRIX_RANK_OK n=7..120\n";
 // For the Desargues graph n=10, exhaust every 20-bit state and
 // count the image of the one-step update independently of rank().
 Matrix a=adjacency(10);
 std::vector<unsigned char> observed(1u<<20,0);
 for(int x=0;x<(1<<20);x++)observed[step(x,a)]=1;
 int image=0,fix=0;
 for(unsigned char x:observed)image+=(x!=0);
 for(int x=0;x<(1<<20);x++)if(step(x,a)==x)fix++;
 assert(fix==64);
 assert(image==(1<<12));
 cout<<"DESARGUES_FULL_STATES_OK states=1048576 image=4096 fixed=64 nonperiodic=1044480\n";
}
