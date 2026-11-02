#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
struct Record{int distance; unsigned long long paths;};
static void pair_swap(vector<int>&t,int i,int j){t[i]=j;t[j]=i;}
static pair<vector<int>, vector<int>> make_letters(int p){
 int n=3*p;vector<int> L(n),R(n);
 iota(L.begin(),L.end(),0);iota(R.begin(),R.end(),0);
 // Main staircase of adjacent transpositions
 for(int i=1;i<2*p-1;i+=2)pair_swap(L,i,i+1);
 for(int i=0;i<2*p;i+=2)pair_swap(R,i,i+1);
 L[2*p-1]=2*p;L[2*p]=2*p+1;L[2*p+1]=3;R[2*p]=2;
 // Outer staircase, alternation staggered by one
 for(int i=2*p+2;i+1<n;i+=2)pair_swap(L,i,i+1);
 for(int i=2*p+1;i+1<n;i+=2)pair_swap(R,i,i+1);
 return {L,R};
}
static tuple<int,unsigned long long,size_t> enumerate(int p){
 auto [a,b]=make_letters(p);int n=3*p;U full=(U(1)<<n)-1;
 array<vector<U>,2> pred;pred[0].assign(n,0);pred[1].assign(n,0);
 for(int i=0;i<n;i++){pred[0][a[i]]|=U(1)<<i;pred[1][b[i]]|=U(1)<<i;}
 unordered_map<U,Record> info;info.max_load_factor(.72);info.reserve(min<size_t>(10000000, (size_t(1)<<min(n,20))));
 vector<U> frontier;frontier.reserve(2000000);
 for(int q=0;q<n;q++){U v=U(1)<<q;info.emplace(v,Record{0,1});frontier.push_back(v);}
 int depth=0;while(!frontier.empty()){
  vector<U> next;
  for(U x:frontier){
   U y[2]={0,0},v=x;
   while(v){int j=__builtin_ctzll(v);v&=v-1;y[0]|=pred[0][j];y[1]|=pred[1][j];}
   for(int t=0;t<2;t++){
    U z=y[t];auto [it,inserted]=info.emplace(z,Record{depth+1,info[x].paths});
    if(inserted)next.push_back(z);
    else if(it->second.distance==depth+1){auto c=info[x].paths; if(ULLONG_MAX-it->second.paths<c)throw runtime_error("path-count overflow");it->second.paths+=c;}
   }
  }
  depth++;
  auto it=info.find(full);
  if(it!=info.end() && it->second.distance==depth)return {depth,it->second.paths,info.size()};
  frontier.swap(next);
 }
 throw runtime_error("no reset word");
}
int main(int argc,char**argv){int lo=3,hi=15;if(argc>1)lo=stoi(argv[1]);if(argc>2)hi=stoi(argv[2]);
 for(int p=lo;p<=hi;p++){auto t0=chrono::steady_clock::now(); auto [l,c,visited]=enumerate(p); auto secs=chrono::duration<double>(chrono::steady_clock::now()-t0).count();cout<<p<<","<<l<<","<<c<<","<<visited<<","<<secs<<"\n"<<flush;}
}
