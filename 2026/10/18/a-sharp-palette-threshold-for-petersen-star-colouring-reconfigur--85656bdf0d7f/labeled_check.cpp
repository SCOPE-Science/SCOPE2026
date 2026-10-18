// Exhaustive six-color single-vertex star-recoloring verification on KG(5,2).
// C++17: g++ -O3 -std=c++17 labeled_check.cpp -o labeled_check && ./labeled_check
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using Vertex = pair<int,int>;
using Colors = array<int,10>;
static constexpr int SIZE = 60466176; // 6^10, indexing vertex labels 0,...,9.
int pw[10];
vector<Vertex> vertices;
vector<vector<int>> nbr(10), paths_at(10);
vector<array<int,4>> paths;

int code(const Colors &a){int x=0;for(int i=0;i<10;i++)x+=a[i]*pw[i];return x;}
Colors decode(int x){Colors a{};for(int i=0;i<10;i++){a[i]=x%6;x/=6;}return a;}
int canonical_code(const Colors &a){int next=0;int mapc[6];fill(mapc,mapc+6,-1);Colors b{};
 for(int i=0;i<10;i++){int c=a[i];if(mapc[c]==-1)mapc[c]=next++;b[i]=mapc[c];}return code(b);}
bool local_valid(const Colors &a,int pos){
 for(int v:nbr[pos])if(a[v]==a[pos])return false;
 for(int k:paths_at[pos]){auto p=paths[k];if(a[p[0]]==a[p[2]] && a[p[1]]==a[p[3]])return false;}
 return true;
}
void setup(){
 pw[0]=1;for(int i=1;i<10;i++)pw[i]=pw[i-1]*6;
 for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)vertices.push_back({i,j});
 for(int i=0;i<10;i++)for(int j=0;j<10;j++)if(i!=j){auto [a,b]=vertices[i];auto [c,d]=vertices[j];if(a!=c&&a!=d&&b!=c&&b!=d)nbr[i].push_back(j);}
 set<array<int,4>> s;
 for(int b=0;b<10;b++)for(int c:nbr[b])for(int a:nbr[b])if(a!=c)
  for(int d:nbr[c])if(d!=b&&d!=a){array<int,4> p={a,b,c,d},q={d,c,b,a};s.insert(min(p,q));}
 for(auto p:s){int id=paths.size();paths.push_back(p);for(int v:p)paths_at[v].push_back(id);}
 assert(paths.size()==60);
}
vector<int> enumerate(){
 vector<int> states;states.reserve(341280);Colors col{};col.fill(-1);
 auto rec=[&](auto&&self,int at)->void{
  if(at==10){states.push_back(code(col));return;}
  for(int c=0;c<6;c++){
   bool conflict=false;
   for(int j:nbr[at])if(j<at&&col[j]==c){conflict=true;break;}
   if(conflict)continue;
   col[at]=c;
   for(int k:paths_at[at]){auto p=paths[k];bool ready=true;
    for(int x:p)if(col[x]<0){ready=false;break;}
    if(ready&&col[p[0]]==col[p[2]]&&col[p[1]]==col[p[3]]){conflict=true;break;}}
   if(!conflict)self(self,at+1);
  }
  col[at]=-1;
 };
 rec(rec,0);
 assert(states.size()==341280);
 return states;
}
struct Orbit{int representative, partitions, exact_colors;};
vector<Orbit> orbits(const vector<int> &states){
 unordered_map<int,int> counts;counts.reserve(600);
 for(int st:states)++counts[canonical_code(decode(st))];
 assert(counts.size()==474);
 for(auto kv:counts)assert(kv.second==720);
 unordered_set<int> unseen;unseen.reserve(600);
 for(auto kv:counts)unseen.insert(kv.first);
 vector<array<int,10>> autos;
 array<int,5> p={0,1,2,3,4};
 do{array<int,10> move{};
   for(int i=0;i<10;i++){
    auto[a,b]=vertices[i];Vertex w=minmax(p[a],p[b]);
    int j=find(vertices.begin(),vertices.end(),w)-vertices.begin();assert(j<10);move[i]=j;
   }
   autos.push_back(move);
 }while(next_permutation(p.begin(),p.end()));
 assert(autos.size()==120);
 vector<Orbit> result;
 while(!unseen.empty()){
  int rep=*unseen.begin();Colors a=decode(rep);
  set<int> image;
  for(auto move:autos){Colors b{};
   for(int i=0;i<10;i++)b[move[i]]=a[i];
   int q=canonical_code(b);assert(counts.count(q));image.insert(q);
  }
  for(int q:image)assert(unseen.erase(q)==1);
  bool used[6]={};for(int c:a)used[c]=true;
  result.push_back({rep,(int)image.size(),accumulate(used,used+6,0)});
 }
 assert(result.size()==11);
 return result;
}
int bfs_ecc(int seed,vector<unsigned char> &seen){
 vector<int> q;q.reserve(341280);q.push_back(seed);seen[seed]=1;
 size_t head=0,until=1;int ecc=0;
 while(head<q.size()){
  int st=q[head++];Colors a=decode(st);
  for(int i=0;i<10;i++){
   int old=a[i];
   for(int c=0;c<6;c++)if(c!=old){
    int next=st+(c-old)*pw[i];
    if(seen[next])continue;
    a[i]=c;
    if(local_valid(a,i)){seen[next]=1;q.push_back(next);}
   }
   a[i]=old;
  }
  if(head==until){
   if(q.size()>until)++ecc;
   until=q.size();
  }
 }
 assert(q.size()==341280);
 for(int st:q)seen[st]=0;
 return ecc;
}
int main(){
 setup();vector<int> states=enumerate();
 vector<int> named_hist(11,0);long long deg_sum=0;int frozen5=0;
 for(int st:states){Colors a=decode(st);bool used[6]={};for(int c:a)used[c]=true;
  int k=accumulate(used,used+6,0);assert(k==5||k==6);
  int deg=0;
  for(int i=0;i<10;i++){
   int old=a[i];
   for(int c=0;c<6;c++)if(c!=old){
    a[i]=c;
    if(local_valid(a,i)){
     ++deg;
     if(k==5 && !used[5] && c<5)assert(false && "non-frozen 5-palette state");
    }
   }
   a[i]=old;
  }
  ++named_hist[deg];deg_sum+=deg;
  if(k==5&&!used[5])++frozen5;
 }
 assert(frozen5==7680);
 assert(deg_sum/2==1094400 && deg_sum%2==0);
 vector<pair<int,int>> hist_expected={{3,14400},{4,64800},{6,108000},{7,86400},{8,21600},{10,46080}};
 for(auto [d,n]:hist_expected)assert(named_hist[d]==n);
 int sumhist=accumulate(named_hist.begin(),named_hist.end(),0);assert(sumhist==341280);
 vector<Orbit> oo=orbits(states);
 int total_partition=0;vector<int> weighted_ecc(30,0);
 vector<unsigned char> visited(SIZE,0);
 for(const auto &o:oo){
  int ecc=bfs_ecc(o.representative,visited);
  weighted_ecc[ecc]+=720*o.partitions;total_partition+=o.partitions;
  cout<<"orbit colors="<<o.exact_colors<<" partitions="<<o.partitions<<" eccentricity="<<ecc<<'\n';
 }
 assert(total_partition==474);
 assert(weighted_ecc[14]==21600 && weighted_ecc[15]==319680);
 for(int i=0;i<30;i++)if(i!=14&&i!=15)assert(weighted_ecc[i]==0);
 cout<<"Petersen n=10 m=15 simple_4_paths="<<paths.size()<<'\n';
 cout<<"5-palette_star_colorings="<<frozen5<<" all_isolated=true\n";
 cout<<"6-palette_star_colorings="<<states.size()<<" edges="<<deg_sum/2<<" components=1\n";
 cout<<"degree_distribution:";for(auto [d,n]:hist_expected)cout<<' '<<d<<':'<<n;cout<<'\n';
 cout<<"radius=14 diameter=15 eccentricity_14="<<weighted_ecc[14]<<" eccentricity_15="<<weighted_ecc[15]<<'\n';
 cout<<"ALL_ASSERTIONS_PASSED\n";
}
