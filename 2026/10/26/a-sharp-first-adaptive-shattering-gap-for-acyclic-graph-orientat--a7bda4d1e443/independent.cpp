// Independent bitword/cycle and 5-round certificate verifier. C++17.
#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<int> H;
 for(int w=0;w<64;w++){
  bool a=false,b=false;
  for(int i=0;i<3;i++){
   int left=(w>>i)&1,right=(w>>(i+3))&1;
   if(left==0 && right==1)a=true;
   if(left==1 && right==0)b=true;
  }
  if(!(a&&b))H.push_back(w);
 }
 if(H.size()!=46)return 1;
 int node[]={0,1,1,2,2,2,2,3,3,3,4,4,3,3,3,4,4,4,4,4,5,5,3,3,5,5,4,4,4,4,4};
 int leaf[]={0,16,8,24,4,52,44,60,2,18,26,58,6,38,22,62,1,9,25,57,5,37,13,61,3,19,11,27,7,23,15,31};
 set<int> all(H.begin(),H.end()), seen;
 for(int p=0;p<32;p++){
  int w=leaf[p],prefix=0;
  if(!all.count(w))return 2;
  seen.insert(w);
  for(int depth=0;depth<5;depth++){
   int q=node[(1<<depth)-1+prefix];
   int branch=(p>>(4-depth))&1;
   if(((w>>q)&1)!=branch)return 3;
   prefix=(prefix<<1)|branch;
  }
 }
 if(seen.size()!=32)return 4;
 // A 6-round full tree requires 64 different hypotheses, but there are only 46.
 if(H.size()>=64)return 5;
 cout<<"CPP_INDEPENDENT_CERTIFICATE_PASS\n";
 cout<<"K23_hypotheses="<<H.size()<<";depth5_paths="<<seen.size()<<";depth6_ruled_out_by_count=1\n";
}
