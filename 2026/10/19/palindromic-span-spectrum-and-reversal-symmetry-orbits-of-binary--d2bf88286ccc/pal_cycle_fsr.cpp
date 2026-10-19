// Exhaustive local-pairing certificate for the palindromic-span spectrum
// of binary order-five de Bruijn cycles. Standalone C++17.
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <cassert>
using namespace std;
int main(){
 constexpr int n=5,N=1<<n,M=1<<(n-1);
 map<int,int> hist;
 unsigned accepted=0;
 for(unsigned f=0;f<(1u<<M);f++){
   array<int,N> seen{};
   string w; w.reserve(N);
   unsigned x=0;
   for(int step=0;step<N;step++){
      if(seen[x])break;
      seen[x]=1;
      w.push_back(char('0'+((x>>(n-1))&1)));
      unsigned tail=x&(M-1);
      unsigned bit=((x>>(n-1))&1)^((f>>tail)&1);
      x=((x<<1)&(N-1))|bit;
   }
   if(w.size()!=N||x!=0)continue;
   ++accepted;
   string repeated=w+w+w;
   int longest=0;
   for(int len=1;len<=N;len++){
      for(int i=0;i<N;i++){
         bool ok=true;
         for(int j=0;j<len/2;j++){
            if(repeated[i+j]!=repeated[i+len-1-j]){ok=false;break;}
         }
         if(ok){longest=len;break;}
      }
   }
   hist[longest]++;
 }
 cout << "FSR accepted=" <<accepted<<" ";
 for(auto [k,v]:hist)cout<<k<<":"<<v<<" ";
 cout<<"\n";
 assert(accepted==2048);
 map<int,int> expected={{7,200},{8,192},{9,856},{10,128},{11,392},{12,32},{13,200},{15,48}};
 assert(hist==expected);
 cout<<"FSR_VERIFY_OK\n";
}
