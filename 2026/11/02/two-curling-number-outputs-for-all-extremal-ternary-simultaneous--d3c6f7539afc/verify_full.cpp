#include <algorithm>
#include <cassert>
#include <cstddef>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;
bool has_suffix_overlap(const string& s) {
 int n=(int)s.size();
 for(int p=1;2*p+1<=n;p++) {
  bool match=true;
  for(int j=0;j<=p;j++) {
   if(s[n-2*p-1+j] != s[n-p-1+j]) {match=false;break;}
  }
  if(match)return true;
 }
 return false;
}
int curling(const string& w){
 const int n=w.size();int best=1;
 for(int width=1;width<=n/2;width++) {
  for(int times=2;times*width<=n;times++) {
   bool repeats=true;
   for(int i=0;i<width*times;i++) {
    if(w[n-i-1]!=w[n-(i%width)-1]) {repeats=false;break;}
   }
   if(repeats)best=max(best,times);
  }
 }
 return best;
}
int main(){
 vector<pair<string,string>> cur={{"",""}};
 for(int n=1;n<=85;n++) {
  vector<pair<string,string>> nxt;
  for(const auto& x:cur){
   for(char a='0';a<='2';a++){
    string v=x.first+a;
    if(has_suffix_overlap(v))continue;
    int cn=curling(v);
    if(cn>2){cerr<<"bad curling bound";return 2;}
    string output=x.second+char('0'+cn);
    if(has_suffix_overlap(output))continue;
    nxt.emplace_back(move(v),move(output));
   }
  }
  cur.swap(nxt);
  if(n%10==0||n>=83)cerr<<"length="<<n<<" count="<<cur.size()<<'\n';
  if(n==84){
   map<string,int> out;
   for(auto& a:cur)out[a.second]++;
   cout<<"source_words="<<cur.size()<<" distinct_outputs="<<out.size()<<'\n';
   for(auto& a:out)cout<<"output="<<a.first<<" count="<<a.second<<'\n';
   auto it=out.begin();string u=(it++)->first,v=it->first;
   size_t agreement=0;
   while(agreement<u.size()&&u[agreement]==v[agreement])agreement++;
   cout<<"shared_prefix_length="<<agreement<<'\n';
  }
  if(cur.empty())break;
 }
}
