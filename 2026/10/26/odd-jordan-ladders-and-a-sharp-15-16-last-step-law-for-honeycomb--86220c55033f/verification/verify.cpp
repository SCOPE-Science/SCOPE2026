#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
using Bits=vector<U>;
static inline void toggle(Bits &x,int j){x[j>>6]^=1ULL<<(j&63);}
static inline bool test(const Bits &x,int j){return (x[j>>6]>>(j&63))&1;}
int rank_gf2(const vector<Bits>&cols,int n){
 vector<Bits> basis(n);
 int r=0;
 for(auto v:cols){
  for(int j=n-1;j>=0;j--){
   if(!test(v,j))continue;
   if(basis[j].empty()){basis[j]=move(v);++r;break;}
   for(size_t i=0;i<v.size();i++)v[i]^=basis[j][i];
  }
 }
 return r;
}
struct Net{
 int side,n,w;vector<array<int,3>> adj;
 Net(int l):side(l),n(2*l*l),w((n+63)/64),adj(n){
  auto a=[&](int i,int j){return ((i+side)%side)*side+(j+side)%side;};
  auto b=[&](int i,int j){return side*side+a(i,j);};
  for(int i=0;i<side;i++)for(int j=0;j<side;j++){
    adj[a(i,j)]={b(i,j),b(i-1,j),b(i,j-1)};
    adj[b(i,j)]={a(i,j),a(i+1,j),a(i,j+1)};
  }
  for(int j=0;j<n;j++)for(int z:adj[j]){
    if(z==j || count(adj[z].begin(),adj[z].end(),j)!=1)throw runtime_error("not simple undirected");
  }
 }
 Bits apply(const Bits&v)const{
  Bits ans(w,0);
  for(int j=0;j<n;j++)if(test(v,j))for(int z:adj[j])toggle(ans,z);
  return ans;
 }
};
int main(){
 for(int k:{1,2,4,8}){
  Net net(3*k);int n=net.n,w=net.w;
  vector<Bits> cols(n,Bits(w,0));for(int j=0;j<n;j++)toggle(cols[j],j);
  cout<<"k="<<k<<" vertices="<<n<<"\n";
  for(int s=0;s<=2*k;s++){
   int d=0;
   if(s<2*k-1){
    int t=s/2;
    if(s%2==0)d=4*(k-t)*(k-t);
    else d=4*(k-t-1)*(k-t);
   }
   int expected=14*k*k+d;
   int got=rank_gf2(cols,n);
   if(got!=expected){cerr<<"FAIL k="<<k<<" step="<<s<<" observed="<<got<<" expected="<<expected<<"\n";return 1;}
   cout<<"  step="<<s<<" rank="<<got<<" predicted="<<expected<<"\n";
   if(s<2*k){for(auto &col:cols)col=net.apply(col);}
  }
 }
 {
  Net net(3);int n=net.n;
  vector<uint32_t> nbr(n);
  for(int j=0;j<n;j++)for(int z:net.adj[j])nbr[j]|=1U<<z;
  vector<uint8_t> has_preimage(1<<n,0);
  for(uint32_t x=0;x<(1U<<n);x++){
    uint32_t y=0;
    for(int j=0;j<n;j++)if(__builtin_parity(x&nbr[j]))y|=1U<<j;
    has_preimage[y]=1;
  }
  int recurring=accumulate(has_preimage.begin(),has_preimage.end(),0);
  if(recurring!=(1<<14)){cerr<<"FAIL exhaustive base recurring="<<recurring<<"\n";return 2;}
  cout<<"exhaustive_k1_states="<<(1<<n)<<" recurring="<<recurring<<" maximal_transient_count="<<((1<<n)-recurring)<<"\n";
 }
 cout<<"HONEYCOMB_VERIFY_OK\n";
}
