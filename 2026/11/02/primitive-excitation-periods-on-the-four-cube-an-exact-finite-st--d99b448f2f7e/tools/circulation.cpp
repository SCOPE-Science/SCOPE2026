#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <array>
using namespace std;
// Independent topological extinction test using the square generators of the cube cycle space.
int main(int argc,char**argv){
 int d=argc>1?atoi(argv[1]):4;int n=1<<d;uint32_t N=1;
 for(int i=0;i<n;i++)N*=3;
 vector<array<int,4>> faces;
 for(int a=0;a<d;a++)for(int b=a+1;b<d;b++)
  for(int v=0;v<n;v++)if(!(v&(1<<a))&&!(v&(1<<b)))
   faces.push_back({v,v^(1<<a),v^(1<<a)^(1<<b),v^(1<<b)});
 uint64_t zero=0,nonzero=0;
 for(uint32_t s=0;s<N;s++){
  uint32_t x=s;uint8_t digits[16];
  for(int v=0;v<n;v++){digits[v]=x%3;x/=3;}
  bool irrotational=true;
  for(const auto& face:faces){
   int sum=0;
   for(int k=0;k<4;k++){
    int u=digits[face[k]],v=digits[face[(k+1)&3]];
    if(u==0&&v==1)sum++;
    if(u==1&&v==0)sum--;
   }
   if(sum!=0){irrotational=false;break;}
  }
  if(irrotational)zero++; else nonzero++;
 }
 printf("CIRCULATION d=%d squares=%zu extinction=%llu persistent=%llu total=%u\n",d,faces.size(),(unsigned long long)zero,(unsigned long long)nonzero,N);
}
