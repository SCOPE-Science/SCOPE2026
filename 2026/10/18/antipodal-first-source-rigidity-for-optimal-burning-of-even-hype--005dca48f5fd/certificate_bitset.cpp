#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
using U=uint64_t;
static unsigned count(U x){return __builtin_popcountll(x);}
int main(int argc,char**argv){
  if(argc!=2){std::fprintf(stderr,"usage: %s even_dimension\n",argv[0]);return 2;}
  int n=std::atoi(argv[1]);if(n<6||n>14||n%2){return 2;}
  int N=1<<n,k=n/2+1,W=(N+63)/64;
  // The first four ignition balls have radii k-1,k-2,k-3,k-4.
  std::vector<std::vector<U>> B(4,std::vector<U>((size_t)N*W));
  std::vector<int> r={k-1,k-2,k-3,k-4};
  for(int j=0;j<4;j++){
    std::vector<int> offsets;
    for(int t=0;t<N;t++)if(__builtin_popcount((unsigned)t)<=r[j])offsets.push_back(t);
    for(int c=0;c<N;c++){
      U *p=B[j].data()+(size_t)c*W;
      for(int t:offsets){int v=c^t;p[v>>6] |= U(1)<<(v&63);}
    }
  }
  int later_capacity=0;
  for(int r0=0;r0<=k-5;r0++){
    int v=1,b=1;for(int j=0;j<=r0;j++){if(j){b=b*(n-j+1)/j;}if(j==0)v=1;else v+=b;}
    later_capacity+=v;
  }
  int dmin=0;
  for(int d=0;d<n;d++){
    int best=N+1;unsigned bestx3=0,bestx4=0;size_t orbit_count=0;
    unsigned x2=(1u<<d)-1u;
    const U*p1=B[0].data();const U*p2=B[1].data()+(size_t)x2*W;
    for(int a=0;a<=d;a++)for(int b=0;b<=n-d;b++){
      unsigned x3=((1u<<a)-1u)|(((1u<<b)-1u)<<d);
      const U*p3=B[2].data()+(size_t)x3*W;
      for(int i=0;i<=a;i++)for(int j=0;j<=d-a;j++)
       for(int z=0;z<=b;z++)for(int t=0;t<=n-d-b;t++){
        unsigned x4=((1u<<i)-1u)|(((1u<<j)-1u)<<a)
         |(((1u<<z)-1u)<<d)|(((1u<<t)-1u)<<(d+b));
        const U*p4=B[3].data()+(size_t)x4*W;
        int unc=0;
        for(int w=0;w<W;w++){
          U u=~(p1[w]|p2[w]|p3[w]|p4[w]);
          if(w==W-1&&N%64)u&=(U(1)<<(N%64))-1;
          unc+=count(u);
        }
        orbit_count++;
        if(unc<best){best=unc;bestx3=x3;bestx4=x4;}
      }
    }
    if(best<=later_capacity){std::printf("FAIL dimension=%d second_weight=%d min_uncovered=%d later_volume=%d\n",n,d,best,later_capacity);return 1;}
    if(best<dmin||d==0)dmin=best;
    std::printf("dimension=%d second_weight=%d four_source_orbits=%zu min_uncovered=%d remaining_total_ball_volume=%d\n",n,d,orbit_count,best,later_capacity);
    if(n==14&&d>=12)std::printf("WITNESS dimension=%d x1=0 x2=%u x3=%u x4=%u uncovered=%d\n",n,x2,bestx3,bestx4,best);
  }
  std::printf("FOUR_BALL_CERTIFICATE_OK dimension=%d lower_min_uncovered=%d threshold=%d\n",n,dmin,later_capacity);
}
