#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
int main(){
for(int n=1;n<=4;n++){
 int N=(1<<n)-1; vector<int> masks(N);for(int i=0;i<N;i++)masks[i]=i+1;
 vector<uint32_t> nei(N);for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(masks[i]&masks[j])nei[i]|=(1u<<j);
 long long total=1;for(int i=0;i<N;i++)total*=3;
 long long good=0, onto=0;
 for(long long k=0;k<total;k++){
  uint32_t colors[3]={0,0,0};long long q=k;for(int i=0;i<N;i++){int d=q%3;q/=3;colors[d]|=1u<<i;}
  // target 0=a,1=b,2=c; non-R iff (0,1) or (1,0)
  bool ok=true;
  for(int i=0;i<N;i++)if((colors[0]>>i)&1u){if(nei[i]&colors[1]){ok=false;break;}}
  if(!ok)continue;
  for(int i=0;i<N;i++){
   int c = ((colors[1]>>i)&1u)?1:(((colors[2]>>i)&1u)?2:0);
   if(c==2){if(!(nei[i]&colors[0])||!(nei[i]&colors[1])){ok=false;break;}}
   else if(!(nei[i]&colors[2])) {ok=false;break;}
  }
  if(ok){good++;if(colors[0]&&colors[1]&&colors[2])onto++;}
 }
 cout<<"n="<<n<<" vertices="<<N<<" possible_maps="<<total<<" p_morphisms="<<good<<" surjective="<<onto<<" expected="<<((1<<n)-2)<<"\n";
}
}
