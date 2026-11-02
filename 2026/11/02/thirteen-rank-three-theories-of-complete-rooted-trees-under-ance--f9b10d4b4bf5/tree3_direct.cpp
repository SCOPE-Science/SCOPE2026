// Direct independent three-round atomic-pattern enumeration for finite rooted tree orders.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using PairType=pair<int,uint64_t>;
using PointType=vector<PairType>;
using RootType=vector<PointType>;
int rel(const string &x,const string &y){
 if(x==y)return 0;
 if(y.size()>x.size() && y.compare(0,x.size(),x)==0)return 1;
 if(x.size()>y.size() && x.compare(0,y.size(),y)==0)return 2;
 return 3;
}
RootType calc(int b,int h){
 vector<string> vertices={""};
 for(int i=0;i<(int)vertices.size();++i)
  if((int)vertices[i].size()<h)
   for(int c=0;c<b;++c)vertices.push_back(vertices[i]+char('0'+c));
 int n=vertices.size(); vector<vector<int>> r(n,vector<int>(n));
 for(int x=0;x<n;++x)for(int y=0;y<n;++y)r[x][y]=rel(vertices[x],vertices[y]);
 RootType R;
 for(int x=0;x<n;++x){
  PointType P;
  for(int y=0;y<n;++y){
   uint64_t bits=0;
   for(int z=0;z<n;++z){
    int id=16*r[x][y]+4*r[x][z]+r[y][z];
    bits|=(uint64_t(1)<<id);
   }
   P.emplace_back(r[x][y],bits);
  }
  sort(P.begin(),P.end());P.erase(unique(P.begin(),P.end()),P.end());
  R.push_back(P);
 }
 sort(R.begin(),R.end());R.erase(unique(R.begin(),R.end()),R.end());
 return R;
}
int main(){
 set<RootType> cls;
 for(int h=0;h<=6;++h){
  auto r=calc(2,h);assert(cls.insert(r).second);
  cout<<"binary height "<<h<<" pointed_types "<<r.size()<<"\n";
 }
 for(int h=1;h<=4;++h){
  auto r=calc(3,h);assert(cls.insert(r).second);
  if(h<=3)assert(r==calc(4,h));
  cout<<"ternary height "<<h<<" pointed_types "<<r.size()<<"\n";
 }
 cout<<"direct_checked_distinct_classes "<<cls.size()<<"\n";
}
