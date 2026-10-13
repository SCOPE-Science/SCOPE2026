// Exact small-parameter independent-set verification via maximal-clique search.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <bitset>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Bits=bitset<128>;
int n,k,best,best_count;
vector<Bits> nbr;

set<string> deletion_outputs(int a,int b,int len){
 string w(len,'0'); w[a]='1';w[b]='1';
 set<string> ans;
 for(int t=0;t<len;++t) ans.insert(w.substr(0,t)+w.substr(t+1));
 return ans;
}
void enumerate(Bits P,Bits X,int depth){
 if(P.none() && X.none()){
   if(depth>best){best=depth;best_count=1;}
   else if(depth==best) ++best_count;
   return;
 }
 if(depth+(int)P.count()<best) return;
 Bits unionPX=P|X;
 int pivot=-1,pivot_degree=-1;
 for(int u=0;u<k;++u) if(unionPX.test(u)){
   int deg=(int)(P&nbr[u]).count();
   if(deg>pivot_degree){pivot=u;pivot_degree=deg;}
 }
 Bits candidates=(pivot==-1)?P:(P & ~nbr[pivot]);
 for(int v=0;v<k;++v) if(candidates.test(v)){
   enumerate(P&nbr[v],X&nbr[v],depth+1);
   P.reset(v); X.set(v);
 }
}
int main(){
 const int expected[]={0,0,0,1,2,3,4,4,5,6,7,7,8};
 for(n=3;n<=12;++n){
   vector<pair<int,int>> words;
   vector<set<string>> balls;
   for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){
     words.push_back({a,b});balls.push_back(deletion_outputs(a,b,n));
   }
   k=(int)words.size();assert(k<=128);
   nbr.assign(k,Bits{});
   for(int i=0;i<k;++i)for(int j=i+1;j<k;++j){
     bool compatible=true;
     for(const auto &s: balls[i]) if(balls[j].count(s)){compatible=false;break;}
     if(compatible){nbr[i].set(j);nbr[j].set(i);}
   }
   Bits P;for(int i=0;i<k;++i)P.set(i);
   best=best_count=0;
   enumerate(P,Bits{},0);
   assert(best==expected[n]);
   cout<<"n="<<n<<" maximum="<<best<<" optimizers="<<best_count<<"\n";
 }
 cout<<"PASS: exact small-parameter exhaustive graph search\n";
}
