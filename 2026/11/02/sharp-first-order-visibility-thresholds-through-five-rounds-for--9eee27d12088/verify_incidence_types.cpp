#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct Obj { int a,b; }; // b<0: singleton; b>=0: two-element subset
bool operator<(const Obj& x,const Obj& y){return tie(x.a,x.b)<tie(y.a,y.b);}
bool operator==(const Obj& x,const Obj& y){return x.a==y.a&&x.b==y.b;}
bool adjacent(const Obj& x,const Obj& y){
 if(x.b<0&&y.b>=0)return x.a==y.a||x.a==y.b;
 if(y.b<0&&x.b>=0)return y.a==x.a||y.a==x.b;
 return false;
}
vector<Obj> representatives(int n,const vector<Obj>& seq){
 set<int> used;for(const auto& z:seq){used.insert(z.a);if(z.b>=0)used.insert(z.b);}
 vector<int> old(used.begin(),used.end()),fresh;
 for(int i=0;i<n&&fresh.size()<2;i++)if(!used.count(i))fresh.push_back(i);
 vector<Obj> out;
 for(int i:old)out.push_back({i,-1});
 if(!fresh.empty())out.push_back({fresh[0],-1});
 for(int k=0;k<(int)old.size();k++)for(int j=k+1;j<(int)old.size();j++)out.push_back({old[k],old[j]});
 if(!fresh.empty())for(int i:old)out.push_back({min(i,fresh[0]),max(i,fresh[0])});
 if(fresh.size()==2)out.push_back({fresh[0],fresh[1]});
 return out;
}
map<vector<int>,int> intern;
map<tuple<int,int,vector<Obj>>,int> memo;
int gettype(int n,int depth,const vector<Obj>& seq){
 auto key=make_tuple(n,depth,seq);auto z=memo.find(key);if(z!=memo.end())return z->second;
 vector<int> desc={-7,depth,(int)seq.size()};
 for(const auto& a:seq)for(const auto& b:seq){desc.push_back(a==b);desc.push_back(adjacent(a,b));}
 desc.push_back(-8);
 if(depth>0){
  vector<int> child;for(auto w:representatives(n,seq)){
   auto s=seq;s.push_back(w);child.push_back(gettype(n,depth-1,s));
  }
  sort(child.begin(),child.end());child.erase(unique(child.begin(),child.end()),child.end());
  desc.insert(desc.end(),child.begin(),child.end());
 }
 auto [it,added]=intern.emplace(desc,(int)intern.size()+1);
 memo.emplace(key,it->second);return it->second;
}
int main(){vector<Obj> empty;bool allgood=true;for(int r=1;r<=5;r++){
 map<int,int> seen;vector<int> cls;
 for(int n=1;n<=10;n++){
  int id=gettype(n,r,empty);if(!seen.count(id))seen[id]=(int)seen.size()+1;
  cls.push_back(seen[id]);
  cout << "r=" << r << " n=" << n << " vertices=" << n*(n+1)/2
       << " class=" << seen[id] << "\n";
 }
 int stop=(r==1?1:r==2?3:r==3?4:r==4?5:7);
 vector<int> expected;for(int n=1;n<=10;n++)expected.push_back(min(n,stop));
 bool ok=cls==expected;allgood=allgood&&ok;
 cout << "RANK_" << r << "_" << (ok?"PASS":"FAIL")
      << " cutoff=" << stop << " classes=" << seen.size() << "\n";
 }
 cout << "COMPLETE_PROFILE_" << (allgood?"PASS":"FAIL")
      << " states="<<memo.size()<<" signatures="<<intern.size()<<"\n";
 return allgood?0:1;
}
