// Finite exact certificate for length-13 gap-two three-decks.
// This file uses only the standard C++17 library.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

static constexpr int L = 13;
static const vector<pair<string,string>> binary_pairs = {
 {"0001010000100", "0010000101000"},
 {"0101111010110", "0110101111010"},
 {"1001010000101", "1010000101001"},
 {"1101111010111", "1110101111011"}
};

string word_of(uint32_t x, int n, int q) {
 string s(n, '0');
 for (int j=n-1;j>=0;--j) {s[j]=char('0'+(x%q));x/=q;}
 return s;
}
uint32_t power(int q,int n) {uint32_t x=1;for(int j=0;j<n;++j)x*=q;return x;}

// A signature has q+q*q+q*q*q exact integer multiplicities,
// one for every ordered pattern of length 1, 2, or 3.
// Each term is counted by a distinct index tuple with gaps >= 2.
string signature(const string& w,int q) {
 const int n=(int)w.size();
 vector<uint16_t> cnt(q+q*q+q*q*q,0);
 for(int i=0;i<n;++i){
  int a=w[i]-'0'; ++cnt[a];
  for(int j=i+2;j<n;++j){
   int b=w[j]-'0'; ++cnt[q+a*q+b];
   for(int k=j+2;k<n;++k){
    int c=w[k]-'0'; ++cnt[q+q*q+(a*q+b)*q+c];
   }
  }
 }
 // uint16_t is sufficient: every multiplicity is at most C(11,3)=165.
 return string(reinterpret_cast<const char*>(cnt.data()),cnt.size()*sizeof(uint16_t));
}

vector<pair<string,string>> census(int q,int n) {
 uint32_t total=power(q,n);
 unordered_map<string,uint32_t> seen;
 seen.reserve(total+total/4);
 vector<pair<string,string>> pairs;
 for(uint32_t code=0;code<total;++code) {
  string w=word_of(code,n,q);
  string sig=signature(w,q);
  auto [it,was_inserted]=seen.emplace(std::move(sig),code);
  if(!was_inserted) {
   string old=word_of(it->second,n,q);
   pairs.emplace_back(old,w);
  }
 }
 sort(pairs.begin(),pairs.end());
 cout << "CENSUS q=" << q << " n=" << n
      << " words=" << total << " signatures=" << seen.size()
      << " excess=" << pairs.size() << "\n";
 return pairs;
}

int main(){
 for(int n=3;n<=12;++n) {
  auto pairs=census(2,n);
  if(!pairs.empty()){cerr<<"UNEXPECTED BINARY COLLISION\n";return 1;}
 }
 auto bp=census(2,L);
 if(bp!=binary_pairs){cerr<<"BINARY CLASSIFICATION MISMATCH\n";return 2;}
 auto tp=census(3,L);
 vector<pair<string,string>> expected;
 for(int a=0;a<3;++a)for(int b=a+1;b<3;++b)
  for(const auto& [u,v]:binary_pairs){
   string x=u,y=v;
   for(char& c:x)c=(c=='0'?char('0'+a):char('0'+b));
   for(char& c:y)c=(c=='0'?char('0'+a):char('0'+b));
   if(y<x)swap(x,y);
   expected.emplace_back(x,y);
  }
 sort(expected.begin(),expected.end());
 if(tp!=expected){
  cerr << "TERNARY CLASSIFICATION MISMATCH: observed=" << tp.size()
       << " expected=" << expected.size() << "\n";
  return 3;
 }
 for(const auto& [x,y]:tp){
  string alphabet=x+y;sort(alphabet.begin(),alphabet.end());
  alphabet.erase(unique(alphabet.begin(),alphabet.end()),alphabet.end());
  if(alphabet.size()!=2 || x==y){cerr<<"TERNARY RIGIDITY FAILED\n";return 4;}
 }
 cout << "PASS_BINARY_3_TO_12_INJECTIVE_BINARY_13_FOUR_TERNARY_13_TWELVE_TWO_LETTER_PAIRS\n";
 return 0;
}
