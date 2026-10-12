// Exact transfer-count and exhaustive rank-order verification for binary three-mer minimizers.
// Build: c++ -O3 -std=c++17 verify_transfer.cpp -o verify_transfer
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <map>
#include <vector>
using namespace std;
using Order=array<int,8>;
int successor(int u,int bit){return ((u<<1)&7)|bit;}
int count_changes(const Order& order,int w){
 int rank[8];for(int j=0;j<8;++j)rank[order[j]]=j;
 int count=0;
 for(int r=0;r<8;++r){
  int u=order[r];
  int dp[8]={};dp[u]=1;
  for(int step=0;step<w;++step){
   int ndp[8]={};
   for(int v=0;v<8;++v)if(rank[v]>=r)for(int bit=0;bit<2;++bit){
    int t=successor(v,bit);if(rank[t]>=r)ndp[t]+=dp[v];
   }
   copy(ndp,ndp+8,dp);
  }
  for(int v=0;v<8;++v)count+=dp[v];
  int before[8]={};for(int v=0;v<8;++v)if(rank[v]>r)before[v]=1;
  for(int step=1;step<w;++step){
   int next[8]={};
   for(int v=0;v<8;++v)if(rank[v]>r)for(int bit=0;bit<2;++bit){
    int t=successor(v,bit);if(rank[t]>r)next[t]+=before[v];
   }
   copy(next,next+8,before);
  }
  for(int v=0;v<8;++v)if(rank[v]>r)for(int bit=0;bit<2;++bit)
   if(successor(v,bit)==u) count+=before[v];
 }
 return count;
}
int main(){
 Order p{0,1,2,3,4,5,6,7};
 array<int,10> minima;minima.fill(numeric_limits<int>::max());
 array<int,10> multiplicity{};
 map<pair<int,int>,int> pairs;
 vector<pair<Order,array<int,10>>> all;
 do{
  array<int,10> score{};
  for(int w=2;w<=9;++w){
   score[w]=count_changes(p,w);
   if(score[w]<minima[w]){minima[w]=score[w];multiplicity[w]=0;}
   if(score[w]==minima[w])multiplicity[w]++;
  }
  pairs[{score[4],score[9]}]++;
  all.push_back({p,score});
 }while(next_permutation(p.begin(),p.end()));
 if(all.size()!=40320)return 1;
 cout << "orders=" << all.size() << "\n";
 for(int w=2;w<=9;++w)cout<<"w="<<w<<" minimum="<<minima[w]<<" count="<<multiplicity[w]<<"\n";
 int all28=0, ordertypes=0, overlap=0;
 map<string,int> firstfour;
 for(auto& e:all){
  bool a=true;for(int w=2;w<=8;++w)if(e.second[w]!=minima[w])a=false;
  if(a){all28++;string s;for(int j=0;j<4;++j)s+=char('0'+e.first[j]);firstfour[s]++;}
  if(a && e.second[9]==minima[9])overlap++;
 }
 cout<<"joint_w2_to_w8="<<all28<<" also_w9="<<overlap<<"\n";
 for(auto [prefix,n]:firstfour)cout<<"optimal_prefix="<<prefix<<" count="<<n<<"\n";
 vector<pair<int,int>> frontier;int limit=numeric_limits<int>::max();
 for(auto [pair,n]:pairs)if(pair.second<limit){frontier.push_back(pair);limit=pair.second;}
 for(auto p:frontier)cout<<"PARETO="<<p.first<<","<<p.second<<" count="<<pairs[p]<<"\n";
 if(minima[2]!=20||minima[3]!=29||minima[4]!=46||minima[5]!=76||minima[6]!=130||minima[7]!=229||minima[8]!=413||minima[9]!=750||all28!=48||overlap!=0||firstfour!=map<string,int>{{"3206",24},{"4571",24}}||frontier!=vector<pair<int,int>>{{46,759},{50,750}}||pairs[{46,759}]!=48||pairs[{50,750}]!=32)return 1;
 cout<<"VERIFY_OK\n";
}
