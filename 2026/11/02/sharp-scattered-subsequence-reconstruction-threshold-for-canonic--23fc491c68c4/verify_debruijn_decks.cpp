// Exact finite verification for scattered-subsequence reconstruction of binary
// order-five de Bruijn cycles. C++17 standard library only.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;

static void require(bool p,const char* s){if(!p)throw runtime_error(s);}
static U spread32(U x){
 x=(x|(x<<16))&0x0000ffff0000ffffULL;
 x=(x|(x<<8))&0x00ff00ff00ff00ffULL;
 x=(x|(x<<4))&0x0f0f0f0f0f0f0f0fULL;
 x=(x|(x<<2))&0x3333333333333333ULL;
 return (x|(x<<1))&0x5555555555555555ULL;
}

static vector<U> deck_dynamic(U w,int K){
 vector<vector<U>> dp(K+1);
 for(int j=0;j<=K;j++)dp[j].assign(max(1,(1<<j)/64),0);
 dp[0][0]=1;
 for(int i=0;i<32;i++){
  int b=int((w>>(31-i))&1);
  for(int j=min(K,i+1);j>=1;j--){
   int chunks=max(1,((1<<(j-1))+63)/64);
   for(int c=0;c<chunks;c++){
    U x=dp[j-1][c];
    U a=spread32(x&0xffffffffULL);
    U z=spread32(x>>32);
    if(b){a<<=1;z<<=1;}
    dp[j][2*c]|=a;
    if(2*c+1<(int)dp[j].size())dp[j][2*c+1]|=z;
   }
  }
 }
 return dp[K];
}
static vector<U> deck_greedy(U w,int K){
 int next[33][2];next[32][0]=next[32][1]=32;
 for(int p=31;p>=0;p--){
  next[p][0]=next[p+1][0];next[p][1]=next[p+1][1];
  next[p][(w>>(31-p))&1]=p;
 }
 vector<U> deck((1<<K)/64,0);
 for(int patt=0;patt<(1<<K);patt++){
  int pos=0;bool found=true;
  for(int j=K-1;j>=0;j--){
   int match=next[pos][(patt>>j)&1];
   if(match==32){found=false;break;}
   pos=match+1;
  }
  if(found)deck[patt>>6]|=U(1)<<(patt&63);
 }
 return deck;
}
static set<U> feedback_cycles(){
 set<U> words;
 for(unsigned mask=0;mask<65536;mask++){
  int x=0;U word=0;bool valid=true;
  for(int i=0;i<32;i++){
   word=(word<<1)|(x>>4);
   int bit=((mask>>(x&15))&1)^(x>>4);
   x=((x<<1)&31)|bit;
   if(i<31 && x==0){valid=false;break;}
  }
  if(valid && x==0)require(words.insert(word).second,"duplicate feedback word");
 }
 require(words.size()==2048,"wrong count of feedback cycles");
 return words;
}
static set<U> euler_cycles(){
 set<U> words;
 for(unsigned ord=0;ord<65536;ord++){
  array<int,16> ptr{};
  vector<pair<int,int>> st={{0,-1}};
  vector<int> edges;edges.reserve(32);
  while(!st.empty()){
   int v=st.back().first;
   if(ptr[v]<2){
    int b=((ord>>v)&1)^ptr[v]++;
    int e=(v<<1)|b;
    st.push_back({((v<<1)|b)&15,e});
   }else{
    int e=st.back().second;st.pop_back();
    if(e>=0)edges.push_back(e);
   }
  }
  require(edges.size()==32,"Euler output length");
  reverse(edges.begin(),edges.end());
  int pivot=int(find(edges.begin(),edges.end(),0)-edges.begin());
  require(pivot<32,"Euler tour missing 00000");
  U word=0;
  for(int i=0;i<32;i++)word=(word<<1)|(edges[(i+pivot)%32]>>4);
  words.insert(word);
 }
 require(words.size()==2048,"wrong Euler cycle count");
 return words;
}
int main(){
 try{
  const auto A=feedback_cycles(),B=euler_cycles();
  require(A==B,"independent constructions disagree");
  map<vector<U>,vector<U>> grp[7];
  for(U w:A){
   require((w>>27)==0,"canonical word fails to start with five zeros");
   for(int k=8;k<=14;k++){
    auto deck=deck_dynamic(w,k);
    require(deck==deck_greedy(w,k),"dynamic/greedy mismatch");
    grp[k-8][deck].push_back(w);
   }
  }
  const int distinct[7]={1,1,21,629,1520,2016,2048};
  for(int k=8;k<=14;k++){
   auto& g=grp[k-8];
   require((int)g.size()==distinct[k-8],"wrong exact deck partition count");
   int sum=0;for(auto& entry:g)sum+=entry.second.size();
   require(sum==2048,"partition lost cycles");
   cout<<"k="<<k<<" classes="<<g.size()<<"\n";
  }
  int pairs=0, singles=0;
  vector<pair<U,U>> witnesses;
  for(auto& [signature,words]:grp[5]){
   if(words.size()==2){
    pairs++;
    U a=min(words[0],words[1]),b=max(words[0],words[1]);
    U diff=a^b;
    bool local=false;
    for(int j=0;j<=29;j++)if(diff==(U(5)<<j))local=true;
    require(local,"an ambiguous pair is not a distance-two bit swap");
    witnesses.push_back({a,b});
   }
   else if(words.size()==1)singles++;
   else throw runtime_error("nontrivial 13-class beyond a pair");
  }
  require(pairs==32 && singles==1984,"incorrect 13-deck ambiguity profile");
  sort(witnesses.begin(),witnesses.end());
  cout<<"pair_hex_a,pair_hex_b\n";
  for(auto [a,b]:witnesses){
   cout<<hex<<setfill('0')<<setw(8)<<a<<","<<setw(8)<<b<<dec<<"\n";
  }
  cout<<"size-2 classes at k=13: "<<pairs<<"\n";
  cout<<"size-1 classes at k=13: "<<singles<<"\n";
  cout<<"all singleton at k=14: "<<grp[6].size()<<"\n";
  cout<<"VERIFY_OK\n";
 }catch(const exception&e){cerr<<"VERIFY_FAIL: "<<e.what()<<"\n";return 1;}
}
