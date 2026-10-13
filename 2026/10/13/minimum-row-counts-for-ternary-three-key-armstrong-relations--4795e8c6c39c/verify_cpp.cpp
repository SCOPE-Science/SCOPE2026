// Independent verifier: canonical set-partition generation and explicit
// increasing-index search for incompatible diagonal instances. The direct
// row checker independently confirms all three exhibited constructions.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using Matrix=vector<vector<int>>;
Matrix transpose(const Matrix& x){
 Matrix out(x[0].size(),vector<int>(x.size()));
 for(size_t j=0;j<x.size();j++)for(size_t i=0;i<x[j].size();i++)out[i][j]=x[j][i];
 return out;
}
static const Matrix four=transpose({{0,0,0,1},{0,0,1,0},{0,1,0,0},{0,1,1,1}});
static const Matrix five=transpose({{0,0,0,0,1,2},{0,0,1,2,0,0},{0,1,0,2,0,2},
                          {0,1,1,2,2,2},{0,1,2,2,2,0}});
static const Matrix seven={{3,2,2,1,2,1,1},{1,3,2,2,1,2,1},
                            {1,1,3,2,2,1,2},{2,1,1,3,2,2,1},
                            {1,2,1,1,3,2,2},{2,1,2,1,1,3,2},
                            {2,2,1,2,1,1,3}};
static vector<uint32_t> masks;
static int m;
static array<int,7> lab;
static vector<long long> levels;
static long long maximal;
void makeColumns(int pos,int maxLabel){
  if(pos==m){
    uint32_t mask=0; int edge=0;
    for(int i=0;i<m;i++)for(int j=i+1;j<m;j++,edge++)
      if(lab[i]==lab[j])mask|=uint32_t(1)<<edge;
    if(mask!=((uint32_t(1)<<(m*(m-1)/2))-1)) masks.push_back(mask);
    return;
  }
  for(int c=0;c<=min(2,maxLabel+1);c++){
    lab[pos]=c;makeColumns(pos+1,max(c,maxLabel));
  }
}
void search(const vector<int>& remaining,int depth,uint32_t once,uint32_t twice){
 levels[depth]++;
 if(depth==m){maximal++;return;}
 if(depth+(int)remaining.size()<m)return;
 for(size_t k=0;k<remaining.size();k++){
    int i=remaining[k];
    if(masks[i]&twice)continue;
    vector<int> next;
    for(size_t t=k+1;t<remaining.size();t++){
      int j=remaining[t];
      if(__builtin_popcount(masks[i]&masks[j])==1)next.push_back(j);
    }
    search(next,depth+1,(once^masks[i])&~twice,twice|(once&masks[i]));
 }
}
void verify(const Matrix& rows){
 int r=rows.size(),n=rows[0].size();
 set<vector<int>> unique(rows.begin(),rows.end());assert((int)unique.size()==r);
 set<pair<int,int>> witness;
 for(int i=0;i<r;i++)for(int j=i+1;j<r;j++){
   vector<int> equal;
   for(int k=0;k<n;k++)if(rows[i][k]==rows[j][k])equal.push_back(k);
   assert(equal.size()<=2);
   if(equal.size()==2)witness.insert({equal[0],equal[1]});
 }
 assert((int)witness.size()==n*(n-1)/2);
 for(int k=0;k<n;k++){
   set<int> alphabet;for(auto& row:rows)alphabet.insert(row[k]);
   assert(alphabet.size()<=3);
 }
}
int main(){
 for(int sz: {3,5,6}){
   m=sz;masks.clear();lab[0]=0;makeColumns(1,0);
   sort(masks.begin(),masks.end());masks.erase(unique(masks.begin(),masks.end()),masks.end());
   assert((int)masks.size()==(sz==3?4:sz==5?40:121));
   levels.assign(m+1,0);maximal=0;
   vector<int> all;for(size_t i=0;i<masks.size();i++)all.push_back((int)i);
   search(all,0,0,0);
   assert(maximal==0);
   cout<<"DIAGONAL_NONEXISTENCE m="<<m<<" candidates="<<masks.size();
   for(int j=0;j<=m;j++)cout<<' '<<j<<':'<<levels[j];
   cout<<'\n';
 }
 verify(four);verify(five);verify(seven);
 Matrix fourProjected=four,sevenProjected=seven;
 for(auto& r:fourProjected)r.pop_back();
 for(auto& r:sevenProjected)r.pop_back();
 verify(fourProjected);verify(sevenProjected);
 cout<<"PASS minimum-row profile n=3..7: 4 4 6 7 7\n";
 cout<<"PASS explicit 4x4 6x5 7x7 and projections\n";
}
