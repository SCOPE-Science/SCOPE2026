// Exhaustive, deterministic certificate for binary substring-composition classes
// of length 23. Compile: g++ -O3 -std=c++17 verify.cpp -o verify
// Run in the directory containing quadruple_classes.csv: ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
static constexpr int N=23;
using Quad=array<uint32_t,4>;
struct Record{uint64_t key;uint32_t word;
 bool operator<(const Record& o)const{return key<o.key||(key==o.key&&word<o.word);}};
uint64_t scramble(uint64_t x){
 x+=0x9e3779b97f4a7c15ULL;
 x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;
 x=(x^(x>>27))*0x94d049bb133111ebULL;
 return x^(x>>31);
}
// Independent direct histogram, using prefix sums instead of popcount windows.
vector<unsigned char> exact_signature(uint32_t w){
 int prefix[N+1]={0};
 for(int i=0;i<N;++i)prefix[i+1]=prefix[i]+((w>>i)&1u);
 vector<unsigned char> out;
 out.reserve((N+1)*(N+2)/2-1);
 for(int k=1;k<=N;++k){
  int count[N+1]={0};
  for(int i=0;i+k<=N;++i)++count[prefix[i+k]-prefix[i]];
  for(int j=0;j<=k;++j)out.push_back(static_cast<unsigned char>(count[j]));
 }
 return out;
}
string bits(uint32_t x,int n=N){
 string s(n,'0');for(int i=0;i<n;++i)s[n-1-i]='0'+((x>>i)&1u);return s;
}
uint32_t reverse_bits(uint32_t v,int n){
 uint32_t r=0;for(int i=0;i<n;++i){r=(r<<1)|(v&1u);v>>=1;}return r;
}
uint32_t interleave(uint32_t u,int m,uint32_t v,int k){
 uint32_t out=0;
 for(int i=k-1;i>=0;--i){out=(out<<m)|u;out=(out<<1)|((v>>i)&1u);}
 return (out<<m)|u;
}
set<Quad> interleaved_quadruples(){
 set<Quad> ans;
 for(int m=2;m<N;++m){
  if((N+1)%(m+1)!=0)continue;
  const int k=(N+1)/(m+1)-1;
  if(k<2)continue;
  for(uint32_t u=0;u<(1u<<m);++u){
   uint32_t ru=reverse_bits(u,m);if(u==ru)continue;
   for(uint32_t v=0;v<(1u<<k);++v){
    uint32_t rv=reverse_bits(v,k);if(v==rv)continue;
    Quad q={interleave(u,m,v,k),interleave(u,m,rv,k),
            interleave(ru,m,v,k),interleave(ru,m,rv,k)};
    sort(q.begin(),q.end());
    if(unique(q.begin(),q.end())!=q.end())throw runtime_error("bad interleaving orbit");
    ans.insert(q);
   }
  }
 }
 return ans;
}
int main(){
 try{
  // Each word enters the list exactly once. Equal complete composition
  // histograms always have equal additive keys (mod 2^64).
  // Hash collisions cannot hide classes: every nonsingleton key bucket is
  // checked against the exact, independent prefix-sum signature.
  uint64_t salt[N+1][N+1]={};
  for(int k=1;k<=N;++k)
   for(int j=0;j<=k;++j)
    salt[k][j]=scramble((uint64_t(k)<<32)|uint64_t(j));
  vector<Record> records;
  records.reserve(1u<<N);
  for(uint32_t w=0;w<(1u<<N);++w){
   uint64_t key=0;
   for(int k=1;k<=N;++k){
    const uint32_t mask=(1u<<k)-1u;
    for(int i=0;i+k<=N;++i)
     key+=salt[k][__builtin_popcount((w>>i)&mask)];
   }
   records.push_back({key,w});
  }
  sort(records.begin(),records.end());
  map<size_t,size_t> counts;
  set<Quad> quad;
  for(size_t i=0,j;i<records.size();i=j){
   j=i+1;
   while(j<records.size()&&records[j].key==records[i].key)++j;
   auto count=j-i;
   counts[count]++;
   if(count>1){
    const auto first=exact_signature(records[i].word);
    for(size_t h=i+1;h<j;++h)
     if(exact_signature(records[h].word)!=first)
      throw runtime_error("collision between unequal composition spectra");
   }
   if(count==4){
    Quad group{};
    for(size_t h=0;h<4;++h)group[h]=records[i+h].word;
    sort(group.begin(),group.end());
    quad.insert(group);
   }
  }
  if(counts!=map<size_t,size_t>{{1,4096},{2,4191936},{4,160}})
   throw runtime_error("wrong exhaustive class histogram");
  if(quad.size()!=160)throw runtime_error("wrong quadruple count");
  // The 152 classes coming from two independently reversible nonpalindromic
  // factors are compared with all 160 true size-four classes.
  auto generated=interleaved_quadruples();
  if(generated.size()!=152)throw runtime_error("wrong classical interleaving count");
  for(auto const&g:generated)
   if(quad.count(g)==0)throw runtime_error("interleaved orbit not a class");
  size_t exceptions=0;
  ifstream in("quadruple_classes.csv");
  if(!in)throw runtime_error("missing quadruple_classes.csv");
  string line;
  if(!getline(in,line)||line!="kind,word_1,word_2,word_3,word_4")
   throw runtime_error("wrong table header");
  set<Quad> from_table;
  while(getline(in,line)){
   istringstream is(line);string piece;vector<string> field;
   while(getline(is,piece,','))field.push_back(piece);
   if(field.size()!=5)throw runtime_error("bad table row");
   Quad g{};
   for(int j=0;j<4;++j){
    string b=field[j+1];if(b.size()!=N||b.find_first_not_of("01")!=string::npos)
     throw runtime_error("bad binary word in table");
    g[j]=static_cast<uint32_t>(stoul(b,nullptr,2));
   }
   if(!is_sorted(g.begin(),g.end())||unique(g.begin(),g.end())!=g.end())
    throw runtime_error("unsorted or repeated table member");
   bool classical=generated.count(g)>0;
   if(field[0]!=(classical?"interleaved":"noninterleaved"))
    throw runtime_error("incorrect interleaving label");
   if(!classical)++exceptions;
   from_table.insert(g);
  }
  if(from_table!=quad||exceptions!=8)
   throw runtime_error("table not equal to exhaustive quadruple list");
  const Quad example={0b01000101010000100011001,
                      0b01010100010000110010001,
                      0b10001001100001000101010,
                      0b10011000100001010100010};
  Quad sorted_example=example;
  sort(sorted_example.begin(),sorted_example.end());
  if(!quad.count(sorted_example)||generated.count(sorted_example))
   throw runtime_error("missing first noninterleaved example");
  cout<<"CHECK_OK n=23 words=8388608 singleton_classes=4096 "
      <<"double_classes=4191936 quadruple_classes=160 "
      <<"interleaved_classes=152 exceptional_classes=8 "
      <<"distinct_profiles=4196192 max_ambiguity=4\n";
  return 0;
 }catch(const exception&e){cerr<<"CHECK_FAIL: "<<e.what()<<"\n";return 1;}
}
