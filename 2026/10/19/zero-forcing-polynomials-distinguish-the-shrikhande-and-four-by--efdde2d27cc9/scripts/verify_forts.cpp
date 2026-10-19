#include <array>
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
#include <string>
#include <cassert>
using namespace std;
constexpr int N=16, ALL=(1<<N)-1;
using A=array<uint16_t,N>;
A neighbors(bool shrikhande){
    A adj{};
    auto id=[](int a,int b){return 4*a+b;};
    for(int x=0;x<4;x++)for(int y=0;y<4;y++)
      for(int u=0;u<4;u++)for(int v=0;v<4;v++){
        int dx=(u-x+4)%4,dy=(v-y+4)%4;
        bool edge=shrikhande ?
          ((dy==0&&(dx==1||dx==3))||(dx==0&&(dy==1||dy==3))||
           (dx==1&&dy==1)||(dx==3&&dy==3)) :
          ((x==u)!=(y==v));
        if(edge)adj[id(x,y)]|=1<<id(u,v);
      }
    return adj;
}
struct Summary{array<int,17> coeff{},minimal{};uint64_t signature=0;int forts=0;vector<unsigned char> truth;array<int,17> minimal_forts{},six_white_classes{},five_white_classes{};};
Summary check(bool is_shrikhande){
 A adj=neighbors(is_shrikhande);
 for(int a=0;a<N;a++){
    assert(__builtin_popcount((unsigned)adj[a])==6);
    for(int b=0;b<N;b++)if(a!=b){
      assert(__builtin_popcount((unsigned)(adj[a]&adj[b]))==2);
      assert(((adj[a]>>b)&1)==((adj[b]>>a)&1));
    }
 }
 vector<unsigned char> contains_fort(1<<N,0),is_fort(1<<N,0);
 Summary s; s.signature=14695981039346656037ULL;s.truth.assign(1<<N,0);
 for(int W=1;W<=ALL;W++){
    bool fort=true;
    for(int x=0;x<N;x++)if(!(W&(1<<x))){
      if(__builtin_popcount((unsigned)(adj[x]&W))==1){fort=false;break;}
    }
    if(fort){contains_fort[W]=is_fort[W]=1;s.forts++;}
 }
 // Boolean subset zeta transform: W is obstructed precisely when it contains some nonempty fort.
 for(int bit=0;bit<N;bit++)for(int W=0;W<=ALL;W++)
    if(W&(1<<bit))contains_fort[W]|=contains_fort[W^(1<<bit)];
 vector<unsigned char> is_minimal_fort(1<<N,0);
 for(int W=1;W<=ALL;W++)if(is_fort[W]){
   bool has_smaller=false;
   for(int x=0;x<N;x++)if(W&(1<<x))
     if(contains_fort[W^(1<<x)]){has_smaller=true;break;}
   if(!has_smaller){is_minimal_fort[W]=1;s.minimal_forts[__builtin_popcount((unsigned)W)]++;}
 }
 for(int W=0;W<=ALL;W++)if(__builtin_popcount((unsigned)W)==5){
    int obstruction=0;
    for(int sub=W;sub;sub=(sub-1)&W)
      if(is_minimal_fort[sub] && __builtin_popcount((unsigned)sub)==4){obstruction=4;break;}
    if(!obstruction && is_minimal_fort[W])obstruction=5;
    if(!obstruction)assert(!contains_fort[W]);
    s.five_white_classes[obstruction]++;
 }
 for(int W=0;W<=ALL;W++)if(__builtin_popcount((unsigned)W)==6){
    int obstruction=0;
    for(int sub=W;sub;sub=(sub-1)&W)
      if(is_minimal_fort[sub] && __builtin_popcount((unsigned)sub)==4){obstruction=4;break;}
    if(!obstruction)for(int sub=W;sub;sub=(sub-1)&W)
      if(is_minimal_fort[sub] && __builtin_popcount((unsigned)sub)==5){obstruction=5;break;}
    if(!obstruction&&is_minimal_fort[W])obstruction=6;
    if(!obstruction)assert(!contains_fort[W]);
    s.six_white_classes[obstruction]++;
 }
 for(int blue=0;blue<=ALL;blue++){
    int white=ALL^blue;
    if(contains_fort[white])continue;
    s.truth[blue]=1;
    int k=__builtin_popcount((unsigned)blue);
    s.coeff[k]++;
    bool inclusion_minimal=true;
    for(int x=0;x<N;x++)if(blue&(1<<x)){
      if(!contains_fort[white|(1<<x)]){inclusion_minimal=false;break;}
    }
    if(inclusion_minimal)s.minimal[k]++;
    // Canonical checksum of all successful BLUE bit masks in increasing numeric order.
    for(int j=0;j<4;j++){
      s.signature^=(uint8_t)(blue>>(8*j));
      s.signature*=1099511628211ULL;
    }
 }
 return s;
}
int main(int argc,char** argv){
 auto s=check(true),r=check(false);
 if(argc>1){
    ifstream f(argv[1],ios::binary);
    assert(f.good());
    vector<unsigned char> data((istreambuf_iterator<char>(f)),istreambuf_iterator<char>());
    assert(data.size()==16384);
    for(int i=0;i<=ALL;i++){
      assert(((data[i>>3]>>(i&7))&1)==s.truth[i]);
      assert(((data[8192+(i>>3)]>>(i&7))&1)==r.truth[i]);
    }
    cout<<"VERIFY_BINARY_CERTIFICATE_OK exactly_131072_mask_decisions_equal=true\n";
 }
 auto print=[](const char* name,const Summary& t){
   cout << name << " forts=" <<t.forts<<" coefficients=";
   for(int i=0;i<=16;i++)if(t.coeff[i])cout<<i<<":"<<t.coeff[i]<<",";
   cout << " inclusion_minimal=";
   for(int i=0;i<=16;i++)if(t.minimal[i])cout<<i<<":"<<t.minimal[i]<<",";
   cout<<" minimal_forts=";
   for(int i=0;i<=16;i++)if(t.minimal_forts[i])cout<<i<<":"<<t.minimal_forts[i]<<",";
   cout<<" white_five_obstructions=";
   for(int i: {0,4,5})cout<<i<<":"<<t.five_white_classes[i]<<",";
   cout<<" white_six_obstructions=";
   for(int i: {0,4,5,6})cout<<i<<":"<<t.six_white_classes[i]<<",";
   cout << " signature=0x"<<hex<<t.signature<<dec<<"\n";
 };
 print("SHRIKHANDE",s);print("ROOK",r);
 assert(s.forts==43175 && r.forts==44167);
 assert(s.coeff[10]==3616 && s.coeff[11]==3600 && r.coeff[10]==3456 && r.coeff[11]==3504);
 assert(s.coeff[12]==1760 && s.coeff[13]==560 && s.coeff[14]==120 && s.coeff[15]==16 && s.coeff[16]==1);
 for(int i=0;i<=16;i++){
   if(i<10){assert(s.coeff[i]==0 && r.coeff[i]==0);}
   if(i>=12)assert(s.coeff[i]==r.coeff[i]);
   if(i!=10)assert(s.minimal[i]==0 && r.minimal[i]==0);
 }
 assert(s.minimal[10]==3616 && r.minimal[10]==3456);
 assert(s.minimal_forts[4]==60 && s.minimal_forts[5]==48 && s.minimal_forts[6]==336);
 for(int i=0;i<=16;i++)if(i!=4 && i!=5 && i!=6){
   assert(s.minimal_forts[i]==0 && r.minimal_forts[i]==0);
 }
 assert(r.minimal_forts[4]==60 && r.minimal_forts[5]==144 && r.minimal_forts[6]==112);
 assert(s.five_white_classes[0]==3600 && s.five_white_classes[4]==720 && s.five_white_classes[5]==48);
 assert(r.five_white_classes[0]==3504 && r.five_white_classes[4]==720 && r.five_white_classes[5]==144);
 assert(s.six_white_classes[0]==3616 && s.six_white_classes[4]==3720 && s.six_white_classes[5]==336 && s.six_white_classes[6]==336);
 assert(r.six_white_classes[0]==3456 && r.six_white_classes[4]==3720 && r.six_white_classes[5]==720 && r.six_white_classes[6]==112);
 cout<<"VERIFY_FORTS_OK two_strongly_regular_graphs all_65536_masks=true coefficients_and_minimality=true\n";
}
