#include <iostream>
#include <map>
#include <cstdint>
#include <stdexcept>
using namespace std;
using H = map<int, long long>;
static H exhaustive(int p) {
  const int n=p*p*p;
  H hist;
  for (int a=0;a<n;++a) for (int b=0;b<n;++b) for (int c=0;c<n;++c) {
    int roots=0;
    for (int x=0;x<n;++x) {
      long long y=((static_cast<long long>(x)+a)*x+b)*x+c;
      if (y%n==0) ++roots;
    }
    ++hist[roots];
  }
  return hist;
}
int main() {
  const H h3={{0,7452},{1,9963},{3,1215},{4,486},{7,486},{9,81}};
  const H h5={{0,690000},{1,1056250},{3,156250},{5,12500},{6,12500},{11,25000},{25,625}};
  for (auto entry : {pair<int,H>{3,h3},pair<int,H>{5,h5}}) {
    int p=entry.first;
    H found=exhaustive(p);
    if(found!=entry.second) throw runtime_error("histogram disagrees with theorem");
    long long count=0, total_roots=0;
    cout << "VERIFY_OK p=" << p;
    for (auto [r,n]:found) { count+=n; total_roots+=static_cast<long long>(r)*n; cout << ' ' << r << ':' << n; }
    long long expected=1;
    for (int i=0;i<9;++i) expected*=p;
    if(count!=expected||total_roots!=expected) throw runtime_error("normalization mismatch");
    cout << " total=" << count << '\n';
  }
}
