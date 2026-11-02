#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

static string decode_word(uint32_t w,int n){
 string s(n,'0');
 for(int k=0;k<n;++k) if((w>>k)&1u) s[k]='1';
 return s;
}
static uint32_t reversed(uint32_t w,int n){
 string s=decode_word(w,n);reverse(s.begin(),s.end());
 uint32_t z=0;for(int i=0;i<n;++i)if(s[i]=='1')z|=1u<<i;
 return z;
}
// Difference histogram of prefix-lattice walk: prefix points are (i-P_i,P_i).
// Every ordered pair of prefix positions a<b contributes the composition of [a,b).
static string prefix_difference_profile(uint32_t w,int n){
 vector<int> P(n+1);
 for(int i=0;i<n;++i)P[i+1]=P[i]+int((w>>i)&1u);
 string key(static_cast<size_t>(n*(n+3)/2),'\0');
 for(int b=1;b<=n;++b){
  for(int a=0;a<b;++a){
   int length=b-a,ones=P[b]-P[a];
   size_t index=static_cast<size_t>((length*(length+1))/2-1+ones);
   // Index for length=1 is 0+ones; length=2 is 2+ones.
   ++key.at(index);
  }
 }
 return key;
}
struct Entry{uint32_t reps[2]={0,0};int orbits=0,words=0;};
struct Row{uint64_t n,distinct,a1,a2,a4,maxf,c,w;};
static vector<Row> read_census(const string& path){
 ifstream f(path);if(!f)throw runtime_error("missing census");
 string line;getline(f,line);vector<Row> rows;
 while(getline(f,line)){
  if(line.empty())throw runtime_error("blank census line");
  replace(line.begin(),line.end(),',',' ');
  istringstream iss(line);Row r;
  if(!(iss>>r.n>>r.distinct>>r.a1>>r.a2>>r.a4>>r.maxf>>r.c>>r.w))throw runtime_error("malformed census row");
  rows.push_back(r);
 }
 return rows;
}
static vector<string> read_fourfold(const string& path){
 ifstream f(path);if(!f)throw runtime_error("missing fourfold table");
 string line;getline(f,line);vector<string> rows;
 while(getline(f,line)){if(line.empty())throw runtime_error("blank collision row"); rows.push_back(line);}
 sort(rows.begin(),rows.end());return rows;
}
int main(int argc,char** argv){
 if(argc!=3)throw runtime_error("Usage: verify_independent CENSUS.csv FOURFOLD.tsv");
 auto expected=read_census(argv[1]);
 if(expected.size()!=23)throw runtime_error("wrong row count");
 for(int n=1;n<=23;++n){
  unordered_map<string,Entry> classes;classes.reserve((1u<<n)/2u);
  for(uint32_t w=0;w<(1u<<n);++w){
   auto mirror=reversed(w,n);
   if(w>mirror)continue;
   Entry& e=classes[prefix_difference_profile(w,n)];
   if(e.orbits>=2)throw runtime_error("more than two reversal orbits in a fiber");
   e.reps[e.orbits++]=w;
   e.words+=(w==mirror)?1:2;
  }
  uint64_t a1=0,a2=0,a4=0,mx=0;
  vector<string> fourfold;
  for(const auto& item:classes){
   const Entry& e=item.second;mx=max(mx,static_cast<uint64_t>(e.words));
   if(e.words==1)++a1;
   else if(e.words==2)++a2;
   else if(e.words==4){
    ++a4;if(e.orbits!=2)throw runtime_error("unexpected orbit structure");
    if(n==23){
     vector<string> words;
     for(int k=0;k<2;++k){words.push_back(decode_word(e.reps[k],n));words.push_back(decode_word(reversed(e.reps[k],n),n));}
     sort(words.begin(),words.end());
     string csv=words[0]+"\t"+words[1]+"\t"+words[2]+"\t"+words[3];
     fourfold.push_back(csv);
    }
   } else throw runtime_error("unexpected fiber size");
  }
  const auto& r=expected[n-1];
  if(r.n!=static_cast<uint64_t>(n)||r.distinct!=classes.size()||r.a1!=a1||r.a2!=a2||r.a4!=a4||r.maxf!=mx||r.c!=a4||r.w!=4*a4)throw runtime_error("census discrepancy at n="+to_string(n));
  if(a1+2*a2+4*a4!=(1u<<n)) throw runtime_error("partition total mismatch");
  if(n==23){
   sort(fourfold.begin(),fourfold.end());
   auto table=read_fourfold(argv[2]);
   vector<string> stripped;
   for(auto& row:table){size_t tab=row.find('\t');if(tab==string::npos)throw runtime_error("missing table delimiter");stripped.push_back(row.substr(tab+1));}
   sort(stripped.begin(),stripped.end());
   if(fourfold!=stripped)throw runtime_error("collision table discrepancy");
  }
  cerr<<"verified n="<<n<<" spectra="<<classes.size()<<" quadruples="<<a4<<'\n';
 }
 cout<<"CROSSCHECK_OK all orders 1..23, including every length-23 collision class\n";
}
