#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <unordered_set>
using namespace std;
// Direct independent implementation. For n<=50, enumerate all binary words
// of weight four and every even-length substring, retaining each distinct
// abelian-square substring by its exact length and bits.
int main(int argc,char**argv){
 int top=32;if(argc>1)top=atoi(argv[1]);
 if(top<4||top>50)return 2;
 puts("# n minimum labeled_minimizers all_four_one_words");
 for(int n=4;n<=top;n++){
  int best=n+1; unsigned long long count=0,total=0;
  for(int a=0;a<n-3;a++)for(int b=a+1;b<n-2;b++)
   for(int c=b+1;c<n-1;c++)for(int d=c+1;d<n;d++){
    uint64_t x=(1ULL<<a)|(1ULL<<b)|(1ULL<<c)|(1ULL<<d);
    unordered_set<uint64_t> found;
    for(int start=0;start<n;start++){
     for(int h=1;start+2*h<=n;h++){
      uint64_t mask=(1ULL<<h)-1ULL;
      int w1=__builtin_popcountll((x>>start)&mask);
      int w2=__builtin_popcountll((x>>(start+h))&mask);
      if(w1==w2){uint64_t bits=(x>>start)&((1ULL<<(2*h))-1ULL);
       found.insert(((uint64_t)(2*h)<<56)|bits);
      }
     }
    }
    ++total;int z=(int)found.size();
    if(z<best){best=z;count=1;}else if(z==best)count++;
  }
  printf("%d %d %llu %llu\n",n,best,count,total);
  fflush(stdout);
 }
}
