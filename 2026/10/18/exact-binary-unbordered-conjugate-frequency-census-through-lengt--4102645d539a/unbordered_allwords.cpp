#include <bits/stdc++.h>
using namespace std;
int main(int argc, char** argv) {
 int N=atoi(argv[1]);
 for(int n=1;n<=N;n++){
   uint64_t lim=uint64_t(1)<<n, mask=lim-1;
   vector<uint64_t> h(n+1,0);
   for(uint64_t w=0; w<lim; ++w){
     int k=0;
     for(int s=0;s<n;s++){
       uint64_t r=(w>>s) | ((w&((uint64_t(1)<<s)-1))<<(n-s));
       bool unbordered=true;
       for(int b=1;b<=n/2;b++){
         uint64_t m=(uint64_t(1)<<b)-1;
         if(((r ^ (r>>(n-b))) & m)==0){unbordered=false;break;}
       }
       k+=unbordered;
     }
     h[k]++;
   }
   cout<<n;for(uint64_t z:h)cout<<" "<<z;cout<<"\n"<<flush;
 }
}
