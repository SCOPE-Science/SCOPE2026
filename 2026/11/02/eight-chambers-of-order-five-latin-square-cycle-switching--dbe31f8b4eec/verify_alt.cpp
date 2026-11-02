// Enumerate the labelled order-five Latin squares and their row/column cycle-switch graphs.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using Square=array<unsigned char,25>;
struct DSU {
 vector<int> p,sz;
 explicit DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);}
 int root(int i){if(p[i]!=i)p[i]=root(p[i]);return p[i];}
 void join(int a,int b){a=root(a);b=root(b);if(a!=b){if(sz[a]<sz[b])swap(a,b);p[b]=a;sz[a]+=sz[b];}}
};
string key(const Square &s){return string(reinterpret_cast<const char*>(s.data()),25);}
void make_square(Square& s,int r, vector<Square>& squares) {
 if(r==5){squares.push_back(s);return;}
 array<int,5> p={0,1,2,3,4};
 do {
  bool valid=true;
  for(int c=0;c<5;c++)for(int h=0;h<r;h++)if(s[5*h+c]==p[c])valid=false;
  if(valid){for(int c=0;c<5;c++)s[5*r+c]=p[c];make_square(s,r+1,squares);}
 }while(next_permutation(p.begin(),p.end()));
}
int parity(vector<int> p){int v=0;for(int a=0;a<(int)p.size();a++)for(int b=a+1;b<(int)p.size();b++)v^=p[a]>p[b];return v;}
int main(){
 vector<Square> normal, squares; Square base{}; for(int c=0;c<5;c++)base[c]=c;
 make_square(base,1,normal);assert(normal.size()==1344);
 for(const auto& s:normal){array<int,5> perm={0,1,2,3,4};do{Square t{};for(int j=0;j<25;j++)t[j]=perm[s[j]];squares.push_back(t);}while(next_permutation(perm.begin(),perm.end()));}
 const int n=squares.size();assert(n==161280);
 unordered_map<string,int> index;index.reserve(n*2);
 for(int i=0;i<n;i++)index.emplace(key(squares[i]),i);
 assert((int)index.size()==n);
 vector<vector<pair<int,int>>> edges(3);
 vector<int> num_inter(n,0), parity_code(n);
 for(int i=0;i<n;i++) {
  const auto &s=squares[i];int rp=0,cp=0,sp=0;
  for(int r=0;r<5;r++){vector<int> v(5);for(int c=0;c<5;c++)v[c]=s[5*r+c];rp^=parity(v);}
  for(int c=0;c<5;c++){vector<int> v(5);for(int r=0;r<5;r++)v[r]=s[5*r+c];cp^=parity(v);}
  for(int k=0;k<5;k++){vector<int> v(5);for(int r=0;r<5;r++)for(int c=0;c<5;c++)if(s[5*r+c]==k)v[r]=c;sp^=parity(v);}
  assert((rp^cp^sp)==0);
  parity_code[i]=(rp<<2)|(cp<<1)|sp;
  for(int axis=0;axis<2;axis++)for(int a=0;a<5;a++)for(int b=a+1;b<5;b++){
    int locations[5];for(int c=0;c<5;c++) locations[axis==0?s[5*a+c]:s[5*c+a]]=c;
    int sigma[5];for(int c=0;c<5;c++)sigma[c]=locations[axis==0?s[5*b+c]:s[5*c+b]];
    int used=0;
    for(int c=0;c<5;c++)if(!(used&(1<<c))){
      vector<int> cycle;int p=c;
      do {cycle.push_back(p);used|=1<<p;p=sigma[p];} while(p!=c);
      int k=cycle.size();assert(k==2||k==3||k==5);
      if(k==2&&axis==0)num_inter[i]++;
      Square t=s;for(int z:cycle) {
        if(axis==0)swap(t[5*a+z],t[5*b+z]);
        else swap(t[5*z+a],t[5*z+b]);
      }
      auto j=index.find(key(t));assert(j!=index.end());
      if(j->second>i)edges[k==2?0:k==3?1:2].push_back({i,j->second});
    }
  }
 }
 for(auto& e:edges){sort(e.begin(),e.end());e.erase(unique(e.begin(),e.end()),e.end());}
 cout<<"LATIN_COUNT "<<n<<" NORMAL_COUNT "<<normal.size()<<"\n";
 cout<<"UNIQUE_EDGES_2_3_5 "<<edges[0].size()<<" "<<edges[1].size()<<" "<<edges[2].size()<<"\n";
 map<int,int> ic;for(int i:num_inter)ic[i]++;cout<<"INTERCALATE_COUNTS";for(auto [k,v]:ic)cout<<" "<<k<<":"<<v;cout<<"\n";
 for(int mask:{1,2,3,4,5,6,7}) {
  DSU d(n);for(int k=0;k<3;k++)if(mask&(1<<k))for(auto [u,v]:edges[k])d.join(u,v);
  map<int,int> cc;map<int,map<int,int>> parity_by_size, inter_by_size;
  for(int i=0;i<n;i++) {int root=d.root(i);parity_by_size[d.sz[root]][parity_code[i]]++;inter_by_size[d.sz[root]][num_inter[i]]++;if(root==i)cc[d.sz[i]]++;}
  cout<<"SWITCH_TYPES";for(int k=0;k<3;k++)if(mask&(1<<k))cout<<" "<<(k==2?5:k+2);
  cout<<" COMPONENTS";for(auto [z,m]:cc)cout<<" "<<z<<":"<<m;
  cout<<" PARITIES";for(auto &e:parity_by_size){cout<<" {"<<e.first<<":";for(auto [pc,count]:e.second)cout<<pc<<"="<<count<<",";cout<<"}";}
  cout<<"\n";
  if(mask==3)assert((cc==map<int,int>({{1,17280},{72000,2}})));
  if(mask==7){
    assert((cc==map<int,int>({{2880,6},{72000,2}})));
    assert(inter_by_size[2880][0]==17280);
    assert(inter_by_size[72000][4]==144000);
    cout<<"CLASS_SEPARATION_OK small=17280_zero_intercalate large=144000_four_intercalate\n";
  }
 }
 assert((ic==map<int,int>({{0,17280},{4,144000}})));
 cout<<"EXHAUSTIVE_CERTIFICATE_OK\n";
}
