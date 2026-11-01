#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
using U=std::uint64_t;
U binom(unsigned n,unsigned k){if(k>n)return 0; if(k>n-k)k=n-k;U s=1;for(unsigned j=1;j<=k;j++)s=s*(n-j+1)/j;return s;}
U update(U x,unsigned n){
    U next=0;
    for(unsigned i=0;i<n;i++)if((x>>i)&1U){
       if(i==n-1)continue;
       if(((x>>(i+1))&1U)==0)next|=U(1)<<(i+1);
       else next|=U(1)<<i;
    }
    return next;
}
int predict(U x,unsigned n){
    if(!x)return 0;
    int height=0, largest=-1000000;
    for(unsigned i=0;i<n;i++){
        if((x>>i)&1U && height>largest)largest=height;
        height += ((x>>i)&1U)? 1:-1;
    }
    return int(n)+largest;
}
U shell(unsigned n,unsigned t){
    if(t==0)return 1;
    if(t<=n)return (t&1U)?binom(t,(t-1)/2):binom(t,t/2-1);
    if(t<2*n)return binom(n,(2*n-t-1)/2);
    return 0;
}
int main(){
    U cases=0;
    for(unsigned n=1;n<=20;n++){
       std::vector<U> counts(2*n);
       const U limit=U(1)<<n;
       for(U s=0;s<limit;s++){
          U cur=s;unsigned t=0;
          while(cur && t<=2*n){cur=update(cur,n);t++;}
          assert(t<=2*n-1 && t==unsigned(predict(s,n)));
          counts[t]++;
       }
       for(unsigned t=0;t<2*n;t++)assert(counts[t]==shell(n,t));
       cases+=limit;
    }
    std::cout<<"CPP_VERIFIED n=1..20, independent bitwise trajectories="<<cases<<", exact shells verified\n";
}
