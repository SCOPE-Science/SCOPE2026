// Exact finite discrete Morse certificate for the 3-by-9 rectangular grid matching complex.
// Standard C++17 only; exhaustive over all simplicial faces; no external data.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;using M=unordered_map<U,U>;
static vector<pair<int,int>> edges;
static vector<U> faces;
static M up,down;
static vector<U> c8,c9;
static unordered_map<U,int> c8index;
using Sparse=vector<pair<int,long long>>;
static unordered_map<U,Sparse> memo;
static long long memo_hits=0;
void add(Sparse &a,const Sparse&b,long long scale){
 // add after convert to map; used rarely after paths
 unordered_map<int,long long> m; m.reserve(a.size()+b.size());
 for(auto [i,v]:a)m[i]+=v;
 for(auto [i,v]:b)m[i]+=v*scale;
 a.clear();for(auto [i,v]:m)if(v)a.push_back({i,v});
 sort(a.begin(),a.end());
}
Sparse projection(U x){
 auto it=memo.find(x);if(it!=memo.end()){++memo_hits;return it->second;}
 auto cr=c8index.find(x); if(cr!=c8index.end())return Sparse{{cr->second,1}};
 if(down.count(x))return {};
 auto p=up.find(x);if(p==up.end()){cerr<<"ERR missing lower cell "<<x<<"\n";exit(2);}
 U y=p->second; int i=__builtin_ctzll(y^x);
 int sign=(__builtin_popcountll(y&((1ULL<<i)-1))%2)?-1:1;
 Sparse ans;
 for(U b=y;b;b&=b-1){int j=__builtin_ctzll(b);if(j==i)continue;
  U z=y^(1ULL<<j);int s=(__builtin_popcountll(y&((1ULL<<j)-1))%2)?-1:1;
  add(ans,projection(z),-sign*s);
 }
 memo.emplace(x,ans); return ans;
}
void dfs(int next,U mask,uint32_t used){
 faces.push_back(mask);
 for(int i=next;i<(int)edges.size();++i){auto[a,b]=edges[i];uint32_t v=(1u<<a)|(1u<<b);if(!(v&used))dfs(i+1,mask|(1ULL<<i),v|used);}
}
int main(){
 auto start=chrono::steady_clock::now();
 const int n=9;
 for(int r=0;r<3;++r)for(int c=0;c<n-1;++c)edges.push_back({r*n+c,r*n+c+1});
 for(int r=0;r<2;++r)for(int c=0;c<n;++c)edges.push_back({r*n+c,(r+1)*n+c});
 dfs(0,0,0);
 assert(edges.size()==42 && faces.size()==7594361);
 vector<long long> f(15,0);for(U x:faces)if(x)f[__builtin_popcountll(x)-1]++;
 cout<<"FACES_OK "<<faces.size()<<" face_vector";for(int k=0;k<15;++k)if(f[k])cout<<" "<<k<<":"<<f[k];cout<<"\n"<<flush;
 unordered_set<U> live;live.reserve(faces.size());for(U x:faces)if(x!=0 && x!=1)live.insert(x);
 up.reserve(faces.size()/2);down.reserve(faces.size()/2);
 for(int i=0;i<(int)edges.size();++i){U b=1ULL<<i;for(U x:faces){if(x&b)continue;
  if(live.count(x)&&live.count(x|b)){live.erase(x);live.erase(x|b);up.emplace(x,x|b);down.emplace(x|b,x);}
 }}
 for(U x:live){if(__builtin_popcountll(x)==9)c8.push_back(x);else if(__builtin_popcountll(x)==10)c9.push_back(x);else{cerr<<"ERR unexpected critical dim "<<__builtin_popcountll(x)-1<<"\n";return 3;}}
 sort(c8.begin(),c8.end());sort(c9.begin(),c9.end());
 assert(c8.size()==173 && c9.size()==10 && up.size()==3797088);
 cout<<"MATCHING_OK pairs "<<up.size()<<" critical (1,173,10)\n"<<flush;
 for(size_t i=0;i<c8.size();++i)c8index[c8[i]]=i;
 // Exhaustive DAG: reverse matched Hasse covers and topologically sort.
 // Each face has distinct 64-bit encoding; no face is sampled or omitted.
 unordered_map<U,int> indeg;indeg.reserve(faces.size());for(U x:faces)if(x)indeg[x]=0;
 long long covers=0;
 for(U x:faces){if(!x)continue;
  for(U b=x;b;b&=b-1){int j=__builtin_ctzll(b);U z=x^(1ULL<<j);if(!z)continue;
   ++covers;
   auto p=up.find(z);if(p!=up.end()&&p->second==x)indeg[x]++;else indeg[z]++;
  }
 }
 queue<U> q;for(auto [x,d]:indeg)if(!d)q.push(x);
 size_t visited=0;
 while(!q.empty()){
  U x=q.front();q.pop();++visited;
  auto pp=up.find(x);if(pp!=up.end())if(--indeg[pp->second]==0)q.push(pp->second);
  auto p=down.find(x);U paired=(p==down.end()?0:p->second);
  for(U b=x;b;b&=b-1){int j=__builtin_ctzll(b);U z=x^(1ULL<<j);if(!z || z==paired)continue;
   if(--indeg[z]==0)q.push(z);
  }
 }
 if(visited!=faces.size()-1){cerr<<"ACYCLIC_FAILED visited "<<visited<<"\n";return 3;}
 cout<<"ACYCLIC_OK visited "<<visited<<" directed_covers "<<covers<<"\n"<<flush;
 indeg.clear();indeg.rehash(0);live.clear();live.rehash(0);
 vector<Sparse> rows;
 for(U x:c9){
  Sparse row;
  for(U b=x;b;b&=b-1){int j=__builtin_ctzll(b);U z=x^(1ULL<<j);int s=__builtin_popcountll(x&((1ULL<<j)-1))%2?-1:1;
   add(row,projection(z),s);
  }
  rows.push_back(row);cout<<"ROW "<<rows.size()-1<<" supports "<<row.size()<<" :";for(auto[i,v]:row)cout<<" "<<i<<":"<<v;cout<<"\n"<<flush;
  cerr<<"MEMO "<<rows.size()<<" "<<memo.size()<<" time "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 }
 // Display an explicit unimodular 10-by-10 column minor of the Morse boundary.
 const vector<int> pivot={2,53,49,72,20,87,148,166,17,16};
 for(int r=0;r<10;++r){
  unordered_map<int,long long> row;
  for(auto [col,val]:rows[r])row[col]=val;
  for(int c=0;c<10;++c){
   long long expected=(r==c?(r==7?-1:1):0);
   if(r==8 && c==7)expected=-1;
   if(row[pivot[c]]!=expected){cerr<<"UNIT_MINOR_FAILED "<<r<<" "<<c<<"\n";return 5;}
  }
 }
 cout<<"UNIT_MINOR_OK columns";
 for(auto c:pivot)cout<<" "<<c;
 cout<<" determinant -1\n"<<flush;
 cout<<"MATRIX_OK rows "<<rows.size()<<" cols "<<c8.size()<<"\n"<<flush;
 long long chi=0;for(int k=0;k<(int)f.size();++k)chi+=(k%2?-f[k]:f[k]);
 assert(chi==164);
 cout<<"EULER "<<chi<<" elapsed "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n"<<flush;
 cout<<"ALL_VERIFY_OK\n"<<flush;
}
