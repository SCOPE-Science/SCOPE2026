// Independent direct bitwise finite-ring count for the Rule 22 modal-fiber theorem.
// Compile: c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck && ./crosscheck
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  uint64_t g[25]={3,1,1};
  for(int n=3;n<=24;n++)g[n]=g[n-1]+g[n-3];
  for(int n=3;n<=22;n++) {
    uint32_t N=uint32_t(1)<<n, mask=N-1;
    vector<uint32_t> hist(N,0);
    for(uint32_t x=0;x<N;x++) {
      uint32_t left=((x<<1)&mask)|(x>>(n-1));
      uint32_t right=(x>>1)|((x&1)<<(n-1));
      uint32_t out=((~x&~left&right)|(~x&left&~right)|(x&~left&~right))&mask;
      ++hist[out];
    }
    uint32_t competitor=*max_element(hist.begin()+1,hist.end());
    if(hist[0]!=1+g[n] || competitor>=hist[0])return 1;
  }
  cout<<"CROSSCHECK_OK"<<endl;
}
