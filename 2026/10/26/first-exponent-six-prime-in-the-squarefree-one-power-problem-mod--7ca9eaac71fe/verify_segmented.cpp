// Exact segmented prime and squarefree sieve for a finite first-occurrence theorem.
// Compile: c++ -std=c++17 -O2 verify_segmented.cpp -o verify_segmented
// Execute: ./verify_segmented
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
constexpr int LIMIT = 189954151;
constexpr int BLOCK = 1000000;
const vector<int> EXPECTED = {
  4851151,14627383,17026927,19883527,50671051,63716551,
  64734883,72319651,95075683,96041527,98555227,139820227,
  140570179,141618283,159658027,165167251,165964327,
  166059979,171086983,177257851,189954151
};
int main() {
  int root = static_cast<int>(sqrt(static_cast<double>(LIMIT)))+1;
  vector<uint8_t> small(root+1,0);
  vector<int> primes;
  for (int q=2; q<=root; ++q) {
    if(small[q]) continue;
    primes.push_back(q);
    if(1LL*q*q<=root)
      for(long long x=1LL*q*q;x<=root;x+=q)small[x]=1;
  }
  long long count=0;
  vector<int> four_fail, five_fail;
  for(long long L=7;L<=LIMIT;L+=BLOCK){
    long long R=min(1LL*LIMIT+1,L+BLOCK);
    long long lo=max(1LL,L-64);
    vector<uint8_t> composite(R-lo,0),squareful(R-lo,0);
    for(int q:primes){
      if(1LL*q*q>=R) break;
      long long st=max(1LL*q*q,((lo+q-1)/q)*q);
      for(long long x=st;x<R;x+=q) composite[x-lo]=1;
      long long qq=1LL*q*q;
      st=((lo+qq-1)/qq)*qq;
      for(long long x=st;x<R;x+=qq) squareful[x-lo]=1;
    }
    long long first=L+((7-L%36+36)%36);
    for(long long p=first;p<R;p+=36){
      if(composite[p-lo])continue;
      ++count;
      bool failed_four=true;
      for(int shift:{1,2,4,8})
        if(p>shift && !squareful[p-shift-lo])failed_four=false;
      if(!failed_four)continue;
      four_fail.push_back(static_cast<int>(p));
      if(p<=32 || !squareful[p-32-lo])continue;
      five_fail.push_back(static_cast<int>(p));
      if(p<=64 || squareful[p-64-lo])throw runtime_error("No exponent-six witness");
    }
  }
  if(count!=879429 || four_fail!=EXPECTED || five_fail!=vector<int>{LIMIT})
    throw runtime_error("Unexpected complete sieve results");
  cout << "CERTIFICATE_OK prime_candidates=" << count
       << " four_failure_count=" << four_fail.size()
       << " five_failure_count=" << five_fail.size()
       << " first_exponent_six=" << five_fail.front() << '\n';
}
