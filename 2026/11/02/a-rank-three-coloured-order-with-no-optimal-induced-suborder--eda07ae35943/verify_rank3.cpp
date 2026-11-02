#include <bits/stdc++.h>
using namespace std;
using Key=tuple<uint32_t,int,uint32_t>;
uint32_t rank2(string_view w){
 uint32_t ans=0; int left=0,right=0;vector<int> rm(w.size());
 for(int i=(int)w.size()-1;i>=0;i--){rm[i]=right;right|=1<<(w[i]=='b');}
 for(int i=0;i<(int)w.size();i++){int c=(w[i]=='b');ans |= uint32_t(1)<<((left*4+rm[i])*2+c);left|=1<<c;}
 return ans;
}
set<Key> rank3(const string& w){
 set<Key> a;
 for(int i=0;i<(int)w.size();i++)a.insert({rank2(string_view(w).substr(0,i)),w[i]=='b',rank2(string_view(w).substr(i+1))});
 return a;
}
int main(){
 string L="rrrrrrbbbbbbrbbbbbr",R="rbbbbbrbbbbbbrrrrrr";
 string M0="rbrbrrbbbrbrbbrbbbbbrrrrrbrrrbbr";
 string M="rbrrrbbrbbbbbrbrrbrbrbbrrrrrbrrbbbr";
 string A0=L+M0+R,W=L+M+R;
 auto t=rank3(A0);auto u=rank3(W);
 cout<<"REFERENCE_LEN="<<A0.size()<<" CANDIDATE_LEN="<<W.size()<<" REFERENCE_TYPES="<<t.size()<<" CANDIDATE_TYPES="<<u.size()<<" EQUIVALENT="<<(t==u)<<'\n';
 if(A0.size()!=70 || W.size()!=73 || t.size()!=70 || t!=u)return 2;
 for(char c: A0+W)if(c!='r' && c!='b')return 6;
 int count=0,equal=0;int maxfound=0;array<int,3> best{};
 for(int a=0;a<73;a++)for(int b=a+1;b<73;b++)for(int c=b+1;c<73;c++){
  string v;v.reserve(70);
  for(int i=0;i<73;i++)if(i!=a && i!=b && i!=c)v.push_back(W[i]);
  // Full exact comparison, not hash approximation.
  auto s=rank3(v);count++;
  int matched=0;
  for(auto& x:s)if(t.count(x))matched++;
  if(matched>maxfound){maxfound=matched;best={a,b,c};}
  if(s==t){equal++;cout<<"COUNTEREXAMPLE_FAIL_SEEN_EQUIVALENT_SUBSEQ:"<<a<<','<<b<<','<<c<<'\n';return 3;}
 }
 cout<<"CHECKED="<<count<<" EQUIVALENT_70_SUBSEQUENCES="<<equal<<" MAX_REFERENCE_TYPES_PRESENT="<<maxfound<<" AT="<<best[0]<<','<<best[1]<<','<<best[2]<<'\n';
 if(count!=62196)return 4;
 if(maxfound!=68)return 5;
 cout<<"RANK3_NO_OPTIMAL_SUBSEQUENCE_PASS\n";
}
