// Exhaustive extremal distinct reverse-shuffle-root counts for binary words.
// Compile: g++ -O3 -std=c++17 enumerate.cpp -o enumerate
// Run: ./enumerate 10
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

static uint64_t choose(int n,int k){
  uint64_t r=1;
  for(int i=1;i<=k;++i)r=r*(uint64_t)(n-i+1)/(uint64_t)i;
  return r;
}
static std::string word_string(uint32_t w,int len){
  std::string s;
  for(int k=0;k<len;++k)s+=((w>>k)&1u)?'1':'0';
  return s;
}
int main(int argc,char**argv){
  if(argc!=2){std::cerr<<"Usage: enumerate n (1 <= n <= 10)\n";return 2;}
  int n=std::atoi(argv[1]);
  if(n<1||n>10){std::cerr<<"n out of range\n";return 2;}
  const int m=2*n;
  const uint32_t word_count=1u<<m, root_count=1u<<n;
  const int root_chunks=(root_count+63)/64;
  // Root bit r at an output-word index is set iff some interleaving
  // of r with its reverse equals that output word.
  std::vector<uint64_t> seen((size_t)word_count*root_chunks,0u);
  uint64_t assignments=0, masks=0;
  for(uint32_t mask=0;mask<word_count;++mask){
    if(__builtin_popcount(mask)!=n)continue;
    ++masks;
    for(uint32_t root=0;root<root_count;++root){
      uint32_t w=0;
      int left=0,right=n-1;
      for(int pos=0;pos<m;++pos){
        int b;
        if(mask & (1u<<pos)) b=(root>>left++)&1u;
        else b=(root>>right--)&1u;
        w|=(uint32_t)b<<pos;
      }
      if(left!=n || right!=-1) throw std::runtime_error("invalid partition");
      seen[(size_t)w*root_chunks+(root>>6)]|=uint64_t(1)<<(root&63);
      ++assignments;
    }
  }
  if(masks!=choose(m,n)||assignments!=masks*root_count)
    throw std::runtime_error("incomplete exhaustive interleavings");
  int maximum=0;
  std::vector<uint32_t> maximizers;
  std::map<int,int> histogram;
  for(uint32_t w=0;w<word_count;++w){
    int num_roots=0;
    for(int k=0;k<root_chunks;++k){
      num_roots+=__builtin_popcountll(seen[(size_t)w*root_chunks+k]);
    }
    if(num_roots==0)continue;
    ++histogram[num_roots];
    if(num_roots>maximum){maximum=num_roots;maximizers.clear();maximizers.push_back(w);}
    else if(num_roots==maximum)maximizers.push_back(w);
  }
  uint64_t total_attainable=0;
  for(const auto& x:histogram)total_attainable+=x.second;
  // Independent necessary/sufficient identity: binary reverse-shuffle
  // squares are binary abelian squares, whose count is C(2n,n).
  if(total_attainable!=choose(m,n))throw std::runtime_error("wrong attainable-word count");
  std::cout<<"n="<<n<<" max="<<maximum<<" number_of_maximizers="<<maximizers.size()
           <<" attainable="<<total_attainable<<" masks="<<masks
           <<" assignments="<<assignments<<"\n";
  std::cout<<"maximizers:";
  for(uint32_t w:maximizers)std::cout<<" "<<word_string(w,m);
  std::cout<<"\n";
  std::cout<<"histogram:";
  for(const auto& x:histogram)std::cout<<" "<<x.first<<":"<<x.second;
  std::cout<<"\n";
}
