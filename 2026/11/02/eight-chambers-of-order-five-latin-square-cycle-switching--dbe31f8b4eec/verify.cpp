// Independent complete enumeration: test all possible two-line cell exchanges directly.
// Every subset of positions is tested, not a precomputed cycle decomposition.
#include <bits/stdc++.h>
using namespace std;
using S=array<unsigned char,25>;
struct DSU{vector<int>p,sz;DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);}int r(int x){return x==p[x]?x:p[x]=r(p[x]);}void add(int x,int y){x=r(x);y=r(y);if(x==y)return;if(sz[x]<sz[y])swap(x,y);p[y]=x;sz[x]+=sz[y];}};
void rec(S& s,int row,const vector<array<int,5>>& perms,vector<S>& base){if(row==5){base.push_back(s);return;}for(auto &p:perms){bool ok=true;for(int c=0;c<5&&ok;c++)for(int q=0;q<row;q++)if(s[5*q+c]==p[c]){ok=false;break;}if(ok){for(int c=0;c<5;c++)s[5*row+c]=p[c];rec(s,row+1,perms,base);}}}
string key(const S&s){return string((char*)s.data(),25);}
int main(){
 vector<array<int,5>> perms;array<int,5> p={0,1,2,3,4};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 vector<S> first,all;S s{};for(int c=0;c<5;c++)s[c]=c;rec(s,1,perms,first);
 assert(first.size()==1344);all.reserve(161280);
 for(auto &u:first)for(auto &perm:perms){S t{};for(int k=0;k<25;k++)t[k]=perm[u[k]];all.push_back(t);}
 assert(all.size()==161280);const int N=all.size();unordered_map<string,int> id;id.reserve(400000);
 for(int i=0;i<N;i++)id.emplace(key(all[i]),i);assert((int)id.size()==N);
 array<vector<uint64_t>,3> edge;
 long long no_valid_1=0,no_valid_4=0;
 for(int i=0;i<N;i++){
  const S&u=all[i];
  for(int axis=0;axis<2;axis++)for(int a=0;a<5;a++)for(int b=a+1;b<5;b++){
   for(int mask=1;mask<32;mask++){
     int len=__builtin_popcount((unsigned)mask);S t=u;
     for(int k=0;k<5;k++)if(mask>>k&1){int x=axis==0?5*a+k:5*k+a;int y=axis==0?5*b+k:5*k+b;swap(t[x],t[y]);}
     // A cell exchange between two rows preserves every column automatically;
     // it is Latin precisely when each of those two altered rows is a permutation.
     bool valid=true;
     for(int h:{a,b}){
       int used=0;for(int k=0;k<5;k++){int v=axis==0?t[5*h+k]:t[5*k+h];used|=1<<v;}
       if(used!=31){valid=false;break;}
     }
     if(!valid)continue;
     // A whole-line swap is a single cycle only if it has no smaller
     // nonempty Latin-preserving two-line subtrade.
     if(len==5){bool has_proper_subtrade=false;
       for(int sub=1;sub<31&&!has_proper_subtrade;sub++)if(__builtin_popcount((unsigned)sub)==2){
         S q=u;for(int z=0;z<5;z++)if(sub>>z&1){int x=axis==0?5*a+z:5*z+a;int y=axis==0?5*b+z:5*z+b;swap(q[x],q[y]);}
         bool okay=true;for(int h:{a,b}){int bits=0;for(int z=0;z<5;z++)bits|=1<<(axis==0?q[5*h+z]:q[5*z+h]);if(bits!=31){okay=false;break;}}
         if(okay)has_proper_subtrade=true;
       }
       if(has_proper_subtrade)continue;
     }
     if(len==1){no_valid_1++;continue;}
     if(len==4){no_valid_4++;continue;}
     assert(len==2||len==3||len==5);
     int j=id.at(key(t));assert(i!=j);
     if(i<j)edge[len==2?0:len==3?1:2].push_back((uint64_t)i*N+j);
   }
  }
 }
 assert(no_valid_1==0&&no_valid_4==0);
 for(auto &e:edge){sort(e.begin(),e.end());e.erase(unique(e.begin(),e.end()),e.end());}
 assert(edge[0].size()==288000&&edge[1].size()==576000&&edge[2].size()==1036800);
 cout<<"SUBSET_METHOD_SQUARES "<<N<<" REDUCED_FIRST_ROW "<<first.size()<<"\n";
 cout<<"SUBSET_METHOD_EDGES "<<edge[0].size()<<" "<<edge[1].size()<<" "<<edge[2].size()<<"\n";
 for(int m:{1,3,7}){
  DSU d(N);for(int k=0;k<3;k++)if(m>>k&1)for(auto z:edge[k])d.add(z/N,z%N);
  map<int,int> sizes;for(int i=0;i<N;i++)if(d.r(i)==i)sizes[d.sz[i]]++;
  cout<<"SUBSET_METHOD_COMPONENTS mask="<<m;for(auto [a,b]:sizes)cout<<" "<<a<<":"<<b;cout<<"\n";
  if(m==1)assert((sizes==map<int,int>{{1,17280},{18000,8}}));
  if(m==3)assert((sizes==map<int,int>{{1,17280},{72000,2}}));
  if(m==7)assert((sizes==map<int,int>{{2880,6},{72000,2}}));
 }
 cout<<"SUBSET_CERTIFICATE_OK\n";
}
