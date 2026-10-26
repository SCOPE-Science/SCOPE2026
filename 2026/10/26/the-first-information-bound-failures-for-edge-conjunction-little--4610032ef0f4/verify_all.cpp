#include <bits/stdc++.h>
using namespace std;
int main(){
 const int n=7, m=n*(n-1)/2, states=1<<m;
 uint32_t qmask[1<<n]={};
 int id=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,id++)for(int s=0;s<(1<<n);s++)if((s>>i&1)&&(s>>j&1))qmask[s]|=1u<<id;
 vector<uint8_t> d(states,0);
 array<long long,8> checkedByOrder{};array<long long,22> failuresByEdge{};vector<uint32_t> failures;
 for(int g=1;g<states;g++){
  int k=31-__builtin_clz(__builtin_popcount((unsigned)g));
  int best=0;
  for(int s=0;s<(1<<n);s++){
   uint32_t a=g&qmask[s];if(!a||a==g)continue;
   uint32_t b=g^a;
   int c=1+min(d[a],d[b]);
   if(c>best){best=c;if(best==k)break;}
  }
  d[g]=best;
  if(best<k){failuresByEdge[__builtin_popcount((unsigned)g)]++; failures.push_back(g);}
 }
 cout<<"states="<<states<<" labeled_nonempty="<<states-1<<" failures="<<failures.size()<<"\n";
 for(int e=1;e<=21;e++)if(failuresByEdge[e])cout<<"edge_count="<<e<<" failed="<<failuresByEdge[e]<<"\n";
 for(auto g:failures){cout<<"FAIL "<<hex<<g<<dec<<" depth="<<int(d[g])<<" edges="<<__builtin_popcount(g)<<"\n";}
}
