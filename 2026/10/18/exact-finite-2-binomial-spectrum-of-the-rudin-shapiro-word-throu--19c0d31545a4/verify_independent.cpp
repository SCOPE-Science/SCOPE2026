// Independent exact census using the direct binary expansion definition,
// with no morphism and no adjacent-state pair decomposition.
// g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent
// ./verify_independent spectrum.csv dyadic_weights.csv
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: verify_independent spectrum.csv dyadic_weights.csv\n";return 2;}
 const int LIMIT=4096, FULL=(1<<16);
 vector<int> y(FULL);
 for(int i=0;i<FULL;++i)y[i]=__builtin_parity((unsigned)i&((unsigned)i>>1));
 vector<array<int,4>> expect(LIMIT+1);
 ifstream t(argv[1]);string line;getline(t,line);
 for(int n=1;n<=LIMIT;++n){
  if(!getline(t,line)){cerr<<"missing spectrum row "<<n<<"\n";return 3;}
  stringstream ss(line);string a;array<int,4> row;
  getline(ss,a,',');if(stoi(a)!=n){cerr<<"nonconsecutive spectrum\n";return 4;}
  for(int j=0;j<4;++j){getline(ss,a,',');row[j]=stoi(a);} expect[n]=row;
 }
 if(getline(t,line)){cerr<<"extra spectrum row\n";return 5;}
 vector<vector<int>> weights(LIMIT+1);
 ifstream g(argv[2]);getline(g,line);
 while(getline(g,line)){
   stringstream ss(line);string a,b,c;
   getline(ss,a,',');getline(ss,b,',');getline(ss,c,',');
   int n=stoi(a),w=stoi(b),v=stoi(c);
   if(n<=0 || n>LIMIT || (n&(n-1))!=0){cerr<<"bad dyadic n\n";return 6;}
   if(weights[n].empty())weights[n].assign(n+1,-1);
   weights[n][w]=v;
 }
 for(int n=1;n<=LIMIT;++n){
   unordered_set<uint64_t> vals;vals.reserve((size_t)8*n+40);
   int w=0;int64_t z=0;
   for(int j=0;j<n;++j){w+=y[j];z+=(int64_t)j*y[j];}
   for(int s=0;s+n<=FULL;++s){
     vals.insert(((uint64_t)w<<32)|(uint64_t)z);
     if(s+n==FULL)break;
     int old=y[s],newb=y[s+n];
     z=z-w+old+(int64_t)(n-1)*newb;
     w=w-old+newb;
   }
   int lo=n+1,hi=-1;vector<int> cnt(n+1);
   for(uint64_t v:vals){int a=(int)(v>>32);lo=min(lo,a);hi=max(hi,a);cnt[a]++;}
   auto e=expect[n];
   if((int)vals.size()!=e[0] || hi-lo+1!=e[1] || lo!=e[2] || hi!=e[3]){
      cerr<<"COUNT_MISMATCH at n="<<n<<" got "<<vals.size()<<" expected "<<e[0]<<"\n";return 7;
   }
   if(!weights[n].empty()){
     for(int a=0;a<=n;++a){int q=weights[n][a];if((cnt[a]?cnt[a]:-1)!=q){
       cerr<<"WEIGHT_MISMATCH n="<<n<<" ones="<<a<<"\n";return 8;}
     }
   }
   if((n&(n-1))==0)cerr<<"confirmed n="<<n<<" profiles="<<vals.size()<<"\n";
 }
 cerr<<"VERIFY_OK: all 4096 complexity rows and every dyadic weight profile\n";
 return 0;
}
