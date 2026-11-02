// Independent enumeration using integer ranks and disjoint-set unions.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
#include <map>
using namespace std;
struct DSU {
 vector<int> p;
 DSU(int n):p(n){iota(p.begin(),p.end(),0);}
 int root(int x){while(p[x]!=x){p[x]=p[p[x]]; x=p[x];}return x;}
 void join(int x,int y){x=root(x);y=root(y);if(x!=y)p[x]=y;}
};
int main(){
 for(int n=2;n<=8;n++){
   long long checked=0;
   for(int mask=0;mask<(1<<n);mask++){
     vector<vector<int>> words;
     vector<int> p(n);iota(p.begin(),p.end(),0);
     do {
       bool good=true;
       for(int i=0;i<n;i++)if((mask>>i&1)&&p[i]==i){good=false;break;}
       if(good)words.push_back(p);
     }while(next_permutation(p.begin(),p.end()));
     int sz=words.size();
     map<vector<int>,int> idx;
     for(int i=0;i<sz;i++)idx[words[i]]=i;
     DSU d(sz);
     for(int i=0;i<sz;i++){
       auto q=words[i];
       for(int j=0;j<n-1;j++){
         swap(q[j],q[j+1]);
         auto it=idx.find(q);
         if(it!=idx.end())d.join(i,it->second);
         swap(q[j],q[j+1]);
       }
     }
     map<int,int> comp_to_sign,sign_to_comp;
     for(int i=0;i<sz;i++){
       vector<int> inv(n);
       for(int j=0;j<n;j++)inv[words[i][j]]=j;
       int sign=0;
       for(int j=1;j<n-1;j++)if((mask>>j&1)&&inv[j]<j)sign|=1<<j;
       int root=d.root(i);
       if(comp_to_sign.count(root))assert(comp_to_sign[root]==sign);
       else comp_to_sign[root]=sign;
       if(sign_to_comp.count(sign))assert(sign_to_comp[sign]==root);
       else sign_to_comp[sign]=root;
     }
     int expected=1<<__builtin_popcount((unsigned)(mask & (((1<<n)-1)^1^(1<<(n-1)))));
     assert((int)comp_to_sign.size()==expected);
     assert((int)sign_to_comp.size()==expected);
     checked+=sz;
   }
   cout<<"ALTERNATIVE_OK n="<<n<<" masks="<<(1<<n)<<" examined_states="<<checked<<'\n';
 }
 cout<<"ALTERNATIVE_ALL_PASS\n";
}
