#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
static inline bool rank2(const vector<unsigned short>& rows,int n,unsigned short subset){
 int m=__builtin_popcount((unsigned)subset);if(m<4)return false;
 for(int q=0;q<n;q++){
  unsigned short ones=0;
  for(int v=0;v<n;v++)if((subset>>v&1)&&(rows[v]>>q&1))ones|=1<<v;
  int p=__builtin_popcount((unsigned)ones);
  if(p>=2 && m-p>=2)return true;
 }
 return false;
}
static inline bool rank3(const vector<unsigned short>& r,int n){
 // full distinct concept masks
 unsigned short sub=0;for(int v=0;v<n;v++){bool dup=false;for(int w=0;w<v;w++)if(r[v]==r[w]){dup=true;break;}if(!dup)sub|=1<<v;}
 if(__builtin_popcount((unsigned)sub)<8)return false;
 for(int x=0;x<n;x++){
  unsigned short yes=0;
  for(int v=0;v<n;v++)if((sub>>v&1)&&(r[v]>>x&1))yes|=1<<v;
  int p=__builtin_popcount((unsigned)yes);
  if(p<4 || __builtin_popcount((unsigned)(sub^yes))<4)continue;
  if(rank2(r,n,yes)&&rank2(r,n,sub^yes))return true;
 }
 return false;
}
static bool minimal(const vector<unsigned short>& r,int n){
 for(int j=0;j<n;j++){
  vector<unsigned short> r2;
  for(int i=0;i<n;i++)if(i!=j){unsigned short mask=0;int kx=0;for(int k=0;k<n;k++)if(k!=j){if(r[i]>>k&1)mask|=(1<<kx);kx++;}r2.push_back(mask);}
  if(rank3(r2,n-1))return false;
 }
 return true;
}
static string degree_key(const vector<unsigned short>& r){
 vector<int>d;for(auto x:r)d.push_back(__builtin_popcount((unsigned)x));sort(d.begin(),d.end());string key;for(auto x:d)key+=to_string(x)+",";return key;
}
int main(){
 for(int n=1;n<=15;n++){
  int dim3=0,m=0;map<string,string> min_graphs;
  for(int s=0;s<(1<<max(0,n-1));s++){
   vector<unsigned short> rows(n,0);
   for(int j=1;j<n;j++)if(s>>(j-1)&1)for(int i=0;i<j;i++){
    rows[i]|=1<<j;rows[j]|=1<<i;
   }
   if(!rank3(rows,n))continue;
   dim3++;
   if(minimal(rows,n)){
    m++;string k=degree_key(rows);
    if(!min_graphs.count(k)){
      string code;for(int j=1;j<n;j++)code+=char('0'+(s>>(j-1)&1));
      min_graphs[k]=code;
    }
   }
  }
  cout << "n="<<n<<" rank3="<<dim3<<" minimal_codes="<<m<<" minimal_iso="<<min_graphs.size()<<"\n";
  for(auto [k,word]:min_graphs)cout<<"  "<<word<<" degrees "<<k<<"\n";
 }
}
