// Independent exhaustive enumeration of labelled order-five Latin squares.
// Each output certificate record contains 25 row-major bytes (0..4), followed
// by one tag: 0 for an isolated state, otherwise component rank (1..8).
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
vector<array<int,5>> perms;
vector<string> all;
array<unsigned,5> used{};
string cur(25,'\0');

void fill_rows(int r){
 if(r==5){
   array<int,5> sy={0,1,2,3,4};
   do{
      string z=cur;
      for(char &ch:z)ch=(char)sy[(unsigned char)ch];
      all.push_back(z);
   }while(next_permutation(sy.begin(),sy.end()));
   return;
 }
 for(const auto &p:perms){
  bool ok=true;
  for(int c=0;c<5;c++)if(used[c]&(1u<<p[c])){ok=false;break;}
  if(!ok)continue;
  for(int c=0;c<5;c++){used[c]|=(1u<<p[c]);cur[5*r+c]=(char)p[c];}
  fill_rows(r+1);
  for(int c=0;c<5;c++)used[c]^=(1u<<p[c]);
 }
}
struct DSU{
 vector<int> p,sz;
 explicit DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);}
 int find(int i){if(p[i]==i)return i;return p[i]=find(p[i]);}
 void unite(int i,int j){i=find(i);j=find(j);if(i==j)return;if(sz[i]<sz[j])swap(i,j);p[j]=i;sz[i]+=sz[j];}
};
int odd(const array<int,5>&p){int k=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)k^=(p[i]>p[j]);return k;}
array<int,3> parity(const string &b){array<int,3> res{};array<int,5> p;
 for(int r=0;r<5;r++){for(int c=0;c<5;c++)p[c]=(unsigned char)b[5*r+c];res[0]^=odd(p);}
 for(int c=0;c<5;c++){for(int r=0;r<5;r++)p[r]=(unsigned char)b[5*r+c];res[1]^=odd(p);}
 for(int s=0;s<5;s++){
  for(int r=0;r<5;r++)for(int c=0;c<5;c++)if((unsigned char)b[5*r+c]==s)p[r]=c;
  res[2]^=odd(p);
 }
 return res;
}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"usage: verify_latin5 OUTPUT_CERTIFICATE\n";return 2;}
 array<int,5> z={0,1,2,3,4};do{perms.push_back(z);}while(next_permutation(z.begin(),z.end()));
 for(int c=0;c<5;c++){cur[c]=(char)c;used[c]=1u<<c;}
 fill_rows(1);
 if(all.size()!=161280)throw runtime_error("incorrect total");
 sort(all.begin(),all.end());
 if(adjacent_find(all.begin(),all.end())!=all.end())throw runtime_error("duplicate");
 unordered_map<string,int> id;id.reserve(all.size()*2);
 for(int i=0;i<(int)all.size();i++)id.emplace(all[i],i);
 DSU d(all.size());map<int,int> degrees;
 long long twice=0;
 for(int i=0;i<(int)all.size();i++){
  const string &b=all[i];int deg=0;
  for(int r=0;r<5;r++)for(int rr=r+1;rr<5;rr++)
   for(int c=0;c<5;c++)for(int cc=c+1;cc<5;cc++){
    int a=r*5+c,bb=r*5+cc,ccx=rr*5+c,dd=rr*5+cc;
    if(b[a]!=b[dd]||b[bb]!=b[ccx])continue;
    string q=b;swap(q[a],q[bb]);swap(q[ccx],q[dd]);
    auto j=id.find(q);if(j==id.end())throw runtime_error("bad switch");
    deg++;d.unite(i,j->second);
   }
  twice+=deg;degrees[deg]++;
 }
 map<int,vector<int>> comps;
 for(int i=0;i<(int)all.size();i++)comps[d.find(i)].push_back(i);
 map<int,int> sizes;
 vector<pair<string,int>> reps;
 map<array<int,3>,int> mobilep,isolatedp;
 for(auto &e:comps){
   auto &v=e.second;sizes[v.size()]++;
   if(v.size()==1)isolatedp[parity(all[v[0]])]++;
   else {
    auto sig=parity(all[v[0]]);
    for(int k:v)if(parity(all[k])!=sig)throw runtime_error("mixed parity");
    mobilep[sig]++;
    reps.push_back({all[v[0]],e.first});
   }
 }
 sort(reps.begin(),reps.end());
 vector<unsigned char> tags(all.size());
 for(int k=0;k<(int)reps.size();k++){
  for(int j:comps[reps[k].second])tags[j]=(unsigned char)(k+1);
 }
 ofstream out(argv[1],ios::binary);
 if(!out)throw runtime_error("cannot write");
 for(int i=0;i<(int)all.size();i++){
   out.write(all[i].data(),25);out.put((char)tags[i]);
 }
 out.close();
 if(degrees!=map<int,int>{{0,17280},{4,144000}} || sizes!=map<int,int>{{1,17280},{18000,8}}
 ||mobilep.size()!=4||isolatedp.size()!=4||twice!=576000)throw runtime_error("census mismatch");
 for(auto &e:mobilep)if(e.second!=2)throw runtime_error("parity components");
 for(auto &e:isolatedp)if(e.second!=4320)throw runtime_error("parity isolates");
 cout<<"{\"labelled_squares\":161280,\"degree_zero\":17280,\"degree_four\":144000,\"edges\":288000,";
 cout<<"\"isolated_components\":17280,\"mobile_components\":8,\"mobile_component_order\":18000,";
 cout<<"\"parity_classes\":4,\"mobile_components_per_parity\":2,\"isolates_per_parity\":4320,";
 cout<<"\"certificate_bytes\":4193280}\n";
}
