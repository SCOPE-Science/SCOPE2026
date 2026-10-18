// Exact enumeration of connected bipartite graphs and their color-refinement classes through order nine.
// Standard C++17; compile with: g++ -O2 -std=c++17 exhaustive.cpp -o exhaustive
// Run: ./exhaustive representatives.tsv > summary.txt
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
struct Graph {int n,a,b;uint32_t mask; vector<vector<int>> adj;};
vector<vector<int>> permutations(int n){vector<int>p(n);iota(p.begin(),p.end(),0);vector<vector<int>>v;do{v.push_back(p);}while(next_permutation(p.begin(),p.end()));return v;}
bool is_connected(int a,int b,uint32_t m){int n=a+b;int found=1;for(int k=0;k<n;k++){int update=found;for(int i=0;i<a;i++)for(int j=0;j<b;j++)if((m>>(i*b+j))&1){if(found&(1<<i)) update|=1<<(a+j);if(found&(1<<(a+j)))update|=1<<i;}if(update==found)break;found=update;}return found==(1<<n)-1;}
uint32_t transpose(int a,int b,uint32_t m){uint32_t q=0;for(int i=0;i<a;i++)for(int j=0;j<b;j++)if((m>>(i*b+j))&1)q|=uint32_t(1)<<(j*a+i);return q;}
uint32_t side_canonical(int a,int b,uint32_t m,const vector<vector<int>>&rowperms){uint32_t best=UINT32_MAX;for(const auto&perm:rowperms){unsigned cols[9]={};for(int i=0;i<a;i++)for(int j=0;j<b;j++)if((m>>(perm[i]*b+j))&1)cols[j]|=1u<<i;sort(cols,cols+b);uint32_t code=0;for(int j=0;j<b;j++)code=(code<<a)|cols[j];best=min(best,code);}return best;}
vector<int> signature(const Graph&g,const vector<int>&cols){vector<int>v=cols;sort(v.begin(),v.end());return v;}
int main(int argc,char**argv){try{
 if(argc!=2)throw runtime_error("usage: exhaustive representatives.tsv");
 ofstream tsv(argv[1]);if(!tsv)throw runtime_error("cannot create output");
 vector<int> expectedTypes={0,1,1,1,3,5,17,44,182,730};
 vector<int> expectedClasses={0,1,1,1,3,5,17,44,182,728};
 tsv<<"n\ta\tb\tmask\n";
 for(int n=1;n<=9;n++){
  vector<Graph> graphs;
  if(n==1){graphs.push_back({1,1,0,0,{{}}});}
  for(int a=1;a<=n/2;a++){int b=n-a;auto ra=permutations(a),rb=permutations(b);set<uint32_t>canonical;
   for(uint32_t mask=0;mask<(1u<<(a*b));mask++){
    if(!is_connected(a,b,mask))continue;
    uint32_t id=side_canonical(a,b,mask,ra);
    if(a==b)id=min(id,side_canonical(b,a,transpose(a,b,mask),rb));
    if(!canonical.insert(id).second)continue;
    Graph g{n,a,b,mask,vector<vector<int>>(n)};
    for(int i=0;i<a;i++)for(int j=0;j<b;j++)if((mask>>(i*b+j))&1){g.adj[i].push_back(a+j);g.adj[a+j].push_back(i);}
    graphs.push_back(move(g));
   }
  }
  if((int)graphs.size()!=expectedTypes[n])throw runtime_error("unexpected graph isomorphism count at n="+to_string(n));
  // Crucially, labels are synchronized over every graph of this order, not named separately inside each graph.
  vector<vector<int>> colors;for(const Graph&g:graphs)colors.push_back(vector<int>(n,0));
  for(int iteration=0;iteration<=2*n;iteration++){
   map<vector<int>,int> lookup;
   vector<vector<vector<int>>> keys(graphs.size());
   for(size_t i=0;i<graphs.size();i++)for(int v=0;v<n;v++){
    vector<int>key={colors[i][v],-1};
    for(int w:graphs[i].adj[v])key.push_back(colors[i][w]);
    sort(key.begin()+2,key.end());keys[i].push_back(key);lookup.insert({key,0});
   }
   int j=0;for(auto&kv:lookup)kv.second=j++;
   vector<vector<int>> next=colors;
   for(size_t i=0;i<graphs.size();i++)for(int v=0;v<n;v++)next[i][v]=lookup.at(keys[i][v]);
   if(next==colors)break;
   colors=move(next);
  }
  map<vector<int>,vector<size_t>> classes;
  for(size_t i=0;i<graphs.size();i++)classes[signature(graphs[i],colors[i])].push_back(i);
  if((int)classes.size()!=expectedClasses[n])throw runtime_error("unexpected WL class count at n="+to_string(n));
  cout<<"order="<<n<<" types="<<graphs.size()<<" C2_classes="<<classes.size()<<"\n";
  if(n==9){int pairs=0;for(auto&it:classes){if(it.second.size()==1)continue;if(it.second.size()!=2)throw runtime_error("unexpected collision size");pairs++;
   cout<<"collision="<<pairs;for(size_t i:it.second)cout<<" (a="<<graphs[i].a<<",b="<<graphs[i].b<<",mask="<<graphs[i].mask<<")";cout<<"\n";
   }if(pairs!=2)throw runtime_error("not exactly two collision pairs");}
  for(auto&g:graphs)tsv<<g.n<<'\t'<<g.a<<'\t'<<g.b<<'\t'<<g.mask<<'\n';
 }
 cout<<"ALL_CHECKS_PASS\n";
 }catch(const exception&e){cerr<<"ERROR "<<e.what()<<'\n';return 1;}
}
