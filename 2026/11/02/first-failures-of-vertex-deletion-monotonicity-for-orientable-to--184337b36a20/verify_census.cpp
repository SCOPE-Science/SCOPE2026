// Exhaustive finite census for the vertex-deletion gap in upper orientable
// total domination. Uses only the C++17 standard library.
// Compile: c++ -O3 -std=c++17 verify_census.cpp -o verify_census
// Run:     ./verify_census
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

int pair_index(int u,int v,int n){
  if(u>v) swap(u,v);
  return u*(2*n-u-1)/2+v-u-1;
}
int orientable_total_domination(int n,int edge_mask){
  vector<pair<int,int>> edges;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)
    if((edge_mask>>pair_index(u,v,n))&1)edges.emplace_back(u,v);
  const int e=(int)edges.size(),full=(1<<n)-1;
  int ans=-1, in[6], out[6], covered[64];
  // Each bit pattern orients each present edge one of its two ways.
  for(int o=0;o<(1<<e);o++){
    fill(in,in+n,0); fill(out,out+n,0);
    for(int j=0;j<e;j++){
      auto [a,b]=edges[j];
      if((o>>j)&1)swap(a,b);
      in[b]++;out[a]|=1<<b;
    }
    bool valid=true;
    for(int v=0;v<n;v++)if(!in[v])valid=false;
    if(!valid)continue;
    covered[0]=0;int min_size=n;
    // covered[S] is precisely the union of the out-neighborhoods of S.
    for(int s=1;s<=full;s++){
      int vertex=__builtin_ctz((unsigned)s);
      covered[s]=covered[s&(s-1)]|out[vertex];
      if(covered[s]==full)min_size=min(min_size,__builtin_popcount((unsigned)s));
    }
    ans=max(ans,min_size);
  }
  return ans; // -1 means no valid orientation.
}
int induced_mask_after_delete(int n,int edge_mask,int deleted){
  int result=0;
  vector<int> index(n,-1);
  for(int v=0,j=0;v<n;v++)if(v!=deleted)index[v]=j++;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)
    if(u!=deleted && v!=deleted && ((edge_mask>>pair_index(u,v,n))&1))
      result|=1<<pair_index(index[u],index[v],n-1);
  return result;
}
int main(){
  // Preliminary exhaustive check of all labeled graphs of order at most five.
  for(int n=3;n<=5;n++){
    const int edge_types=n*(n-1)/2;
    vector<int> values(1<<edge_types,-2);
    for(int g=0;g<(1<<edge_types);g++){
      for(int v=0;v<n;v++){
        int h=induced_mask_after_delete(n,g,v);
        int child=orientable_total_domination(n-1,h);
        if(child<0)continue;
        if(values[g]==-2)values[g]=orientable_total_domination(n,g);
        assert(values[g]<=child+1);
      }
    }
  }
  // Independently exhaustive enumeration of all 2^15 labeled graphs on [6].
  const int n=6;
  vector<int> child_cache(1<<10,-2),parent_cache(1<<15,-2);
  map<int,int> class_counts;
  array<int,6> vertex_permutation={0,1,2,3,4,5};
  vector<array<int,6>> perms;
  do{perms.push_back(vertex_permutation);}
  while(next_permutation(vertex_permutation.begin(),vertex_permutation.end()));
  long long good_pairs=0,good_graphs=0;
  for(int graph=0;graph<(1<<15);graph++){
    vector<int> violating_vertices;
    for(int v=0;v<n;v++){
      int h=induced_mask_after_delete(n,graph,v);
      if(child_cache[h]==-2)child_cache[h]=orientable_total_domination(5,h);
      if(child_cache[h]==3)violating_vertices.push_back(v);
    }
    if(violating_vertices.empty())continue;
    if(parent_cache[graph]==-2)
      parent_cache[graph]=orientable_total_domination(6,graph);
    if(parent_cache[graph]!=5)continue;
    good_graphs++;
    for(int v:violating_vertices){
      good_pairs++;
      // Canonical isomorphism class of a graph with one marked vertex.
      int representative=INT32_MAX;
      for(auto &p:perms){
        int relabeled=0;
        for(int u=0;u<n;u++)for(int w=u+1;w<n;w++)
          if((graph>>pair_index(u,w,n))&1)
            relabeled|=1<<pair_index(p[u],p[w],n);
        representative=min(representative,n*relabeled+p[v]);
      }
      class_counts[representative]++;
    }
  }
  assert(good_pairs==9000);
  assert(good_graphs==5850);
  assert(class_counts.size()==18);
  long long orbit_sum=0;
  for(auto [c,count]:class_counts)orbit_sum+=count;
  assert(orbit_sum==good_pairs);
  cout<<"minimum-order bound checked through order five\n";
  cout<<"labeled 6-vertex graph/marked-vertex pairs: "<<good_pairs<<"\n";
  cout<<"labeled underlying graphs with a violating vertex: "<<good_graphs<<"\n";
  cout<<"marked isomorphism classes: "<<class_counts.size()<<"\n";
  for(auto [c,count]:class_counts)
    cout<<"representative graph mask="<<c/n
        <<" marked vertex="<<c%n<<" labeled pairs="<<count<<"\n";
  cout<<"VERIFY_OK\n";
}
