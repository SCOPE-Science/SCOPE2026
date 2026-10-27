#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using U = uint64_t;
static int n,N,threshold,best,limit;
static unsigned long long ways,leaves;
static vector<U> closed_neighborhood;

// Any optimum places label 1 only outside the union of closed neighborhoods
// of the label-2 set. Otherwise a redundant label 1 could be changed to 0.
// Thus choosing the label-2 subset determines an optimum uniquely.
void enumerate(int pos,int twos,U monitored){
  if(pos==N){
    ++leaves;
    int weight=2*twos+N-__builtin_popcountll(monitored);
    if(weight<best){best=weight;ways=1;}
    else if(weight==best)++ways;
    return;
  }
  enumerate(pos+1,twos,monitored);
  if(twos<limit)enumerate(pos+1,twos+1,monitored|closed_neighborhood[pos]);
}
int main(){
  for(int m:{7,8,14}){
    n=m;N=2*n;limit=0; // all potentially optimum-sized sets are enumerated
    threshold=(8*n+6)/7;limit=threshold/2;
    closed_neighborhood.assign(N,0);
    for(int i=0;i<N;++i)closed_neighborhood[i]=U(1)<<i;
    auto edge=[](int a,int b){
      closed_neighborhood[a]|=U(1)<<b;
      closed_neighborhood[b]|=U(1)<<a;
    };
    for(int i=0;i<n;++i){edge(i,(i+1)%n);edge(i,n+i);edge(n+i,n+(i+2)%n);}
    best=threshold;ways=0;leaves=0;
    enumerate(0,0,U(0));
    assert(best==threshold && ways>0);
    cout<<"n="<<n<<" minimum="<<best<<" minima="<<ways<<" checked_two_sets="<<leaves<<'\n';
  }
}
