#include <bits/stdc++.h>
using namespace std;
constexpr int MAXV=400, W=(MAXV+63)/64;
struct Bit {array<uint64_t,W> a{}; void set(int x){a[x>>6]|=1ull<<(x&63);}void clr(int x){a[x>>6]&=~(1ull<<(x&63));}bool test(int x)const{return a[x>>6]>>(x&63)&1;} bool any()const{for(auto x:a)if(x)return true;return false;} int first()const{for(int j=0;j<W;j++)if(a[j])return (j<<6)+__builtin_ctzll(a[j]);return -1;} int cnt()const{int c=0;for(auto x:a)c+=__builtin_popcountll(x);return c;} Bit operator&(const Bit& b)const{Bit c;for(int j=0;j<W;j++)c.a[j]=a[j]&b.a[j];return c;} Bit minus(const Bit& b)const{Bit c;for(int j=0;j<W;j++)c.a[j]=a[j]&~b.a[j];return c;}};
int V,threshold=65,best=0;vector<Bit> adj;uint64_t nodes=0;vector<int> bestclq, cur;
chrono::steady_clock::time_point st;
void expand(Bit P){
 nodes++;if(!(nodes%1000000)){auto t=chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-st).count();cerr<<"nodes "<<nodes<<" ms "<<t<<" best "<<best<<" depth "<<cur.size()<<"\n";}
 if(!P.any()){if((int)cur.size()>best){best=cur.size();bestclq=cur;cerr<<"new best "<<best<<" nodes "<<nodes<<"\n";}return;}
 vector<int> order, colors;
 Bit Q=P;int col=0;
 while(Q.any()){
  col++;Bit R=Q;
  while(R.any()){
   int v=R.first();R.clr(v);Q.clr(v);order.push_back(v);colors.push_back(col);R=R.minus(adj[v]);
  }
 }
 for(int j=(int)order.size()-1;j>=0;j--){
  if((int)cur.size()+colors[j]<=best)return;
  int v=order[j];cur.push_back(v);Bit next=P&adj[v];
  if(next.any())expand(next);
  else if((int)cur.size()>best){best=cur.size();bestclq=cur;cerr<<"new best "<<best<<" nodes "<<nodes<<"\n";}
  cur.pop_back();P.clr(v);
 }
}
int main(int argc,char**argv){st=chrono::steady_clock::now();int N=7,K=3; if(argc>1)N=atoi(argv[1]);if(argc>2)K=atoi(argv[2]);V=0;vector<vector<int>> masks;
 vector<int> p(N,0);function<void(int,int)> rec=[&](int i,int mx){if(i==N){if(mx+1==N-K)masks.push_back(p);return;}for(int j=0;j<=min(mx+1,N-K-1);j++){p[i]=j;rec(i+1,max(mx,j));}};rec(1,0);V=masks.size();if(V>MAXV){cerr<<"too many";return 1;}
 vector<uint64_t> ms(V);int edgeid[12][12];int e=0;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)edgeid[i][j]=e++;
 for(int z=0;z<V;z++)for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(masks[z][i]==masks[z][j])ms[z]|=1ull<<edgeid[i][j];
 adj.resize(V);for(int i=0;i<V;i++)for(int j=0;j<V;j++)if(i!=j&&(ms[i]&ms[j]))adj[i].set(j);
 // relabel vertices sorted by degree descending (strong heuristic)
 vector<int> perm(V);iota(perm.begin(),perm.end(),0);sort(perm.begin(),perm.end(),[&](int i,int j){int a=adj[i].cnt(),b=adj[j].cnt();return a==b?i<j:a>b;});
 vector<Bit> a(V);for(int i=0;i<V;i++)for(int j=0;j<V;j++)if(adj[perm[i]].test(perm[j]))a[i].set(j);adj.swap(a);
 Bit P;for(int i=0;i<V;i++)P.set(i);
 // lower bound full edge star (rank k): choose all flats containing atom 01
 for(int i=0;i<V;i++)if(ms[perm[i]]&1ull)cur.push_back(i);
 best=cur.size();bestclq=cur;cur.clear();cerr<<"N "<<N<<" K "<<K<<" V "<<V<<" start bound "<<best<<"\n";
 expand(P);
 cout<<"MAX_CLIQUE "<<best<<" nodes "<<nodes<<"\n";for(int i:bestclq)cout<<perm[i]<<" ";cout<<"\n";
}
