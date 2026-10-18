// Reproducible finite checks for resolving subsets of KG(n,2).
// The mathematical theorem for all n >= 5 is proved independently of this test.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <random>
#include <vector>
using namespace std;
struct DSU {
 int p[12];
 explicit DSU(int n) {for(int i=0;i<n;i++)p[i]=i;}
 int find(int a){while(a!=p[a])a=p[a]=p[p[a]];return a;}
 void join(int a,int b){a=find(a);b=find(b);if(a!=b)p[a]=b;}
};
struct Instance {
 int n, m;
 vector<array<int,2>> edges;
 vector<uint64_t> distinguishing_masks;
 explicit Instance(int n_):n(n_){
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edges.push_back({a,b});
  m=int(edges.size());
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
   uint64_t mask=0;
   for(int w=0;w<m;w++){
    auto distance=[&](int k)->int{
     if(w==k)return 0;
     bool disjoint=edges[w][0]!=edges[k][0]&&edges[w][0]!=edges[k][1]
       &&edges[w][1]!=edges[k][0]&&edges[w][1]!=edges[k][1];
     return disjoint?1:2;
    };
    if(distance(i)!=distance(j))mask|=uint64_t(1)<<w;
   }
   distinguishing_masks.push_back(mask);
  }
 }
 bool direct(uint64_t s)const {
  for(uint64_t mask:distinguishing_masks)if((s&mask)==0)return false;
  return true;
 }
 bool component_criterion(uint64_t s)const {
  DSU d(n);
  for(int j=0;j<m;j++)if((s>>j)&1)d.join(edges[j][0],edges[j][1]);
  int vertices[12]={},degrees[12]={},edge_counts[12]={};
  for(int i=0;i<n;i++)vertices[d.find(i)]++;
  for(int j=0;j<m;j++)if((s>>j)&1){
   degrees[edges[j][0]]++;degrees[edges[j][1]]++;
   edge_counts[d.find(edges[j][0])]++;
  }
  int isolated=0,three_paths=0;
  for(int root=0;root<n;root++)if(d.find(root)==root){
   int v=vertices[root],e=edge_counts[root];
   if(v==1)isolated++;
   if(v==2)return false;
   if(v==3&&e==2)three_paths++;
   if(v==4){
    int maxdegree=0;
    for(int j=0;j<n;j++)if(d.find(j)==root)maxdegree=max(maxdegree,degrees[j]);
    if(maxdegree<=2&&(e==3||e==4))return false;
   }
  }
  return isolated<=1&&!(isolated>0&&three_paths>0);
 }
};
int main(){
 long long count=0,yes=0;
 for(int n=5;n<=7;n++){
  Instance I(n);
  long long local=1LL<<I.m,passed=0;
  for(uint64_t s=0;s<(uint64_t)local;s++){
   bool a=I.direct(s),b=I.component_criterion(s);
   if(a!=b){printf("FAIL n=%d mask=%llu actual=%d predicted=%d\n",n,(unsigned long long)s,a,b);return 1;}
   passed+=a;
  }
  printf("EXHAUSTIVE_OK n=%d edge_subsets=%lld resolving=%lld\n",n,local,passed);
  count+=local;yes+=passed;
 }
 mt19937_64 rng(40320193);
 int random_count=0;
 for(int n=8;n<=10;n++){
  Instance I(n);
  for(int per100: {5,15,25,50,75}){
   int passed=0;
   for(int rep=0;rep<10000;rep++){
    uint64_t s=0;
    for(int j=0;j<I.m;j++)if(int(rng()%100)<per100)s|=uint64_t(1)<<j;
    bool a=I.direct(s),b=I.component_criterion(s);
    if(a!=b){printf("FAIL n=%d p=%d sample=%d\n",n,per100,rep);return 1;}
    passed+=a;random_count++;
   }
   printf("RANDOM_OK n=%d p_percent=%d samples=10000 resolving=%d\n",n,per100,passed);
  }
 }
 printf("VERIFICATION_OK exact_subsets=%lld exact_resolving=%lld random_samples=%d\n",count,yes,random_count);
 return 0;
}
