// Reproducible integer discrete-Morse computation for the two-independence
// complex of the dodecahedral graph GP(10,2). C++17, standard library only.
// Compile: g++ -O2 -std=c++17 dodecahedron_ind2_verify.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <unordered_map>
#include <vector>
using namespace std;
using ll=long long;
constexpr int n=20, N=1<<20;
void demand(bool p, const char *msg){if(!p)throw runtime_error(msg);}
int bits(unsigned s){return __builtin_popcount(s);}
int sign_of(unsigned s,unsigned bit){return (__builtin_popcount(s&(bit-1))&1)?-1:+1;}
vector<pair<int,int>> oriented_boundary(unsigned u){
 vector<pair<int,int>> r;
 for(unsigned b=u;b;b&=b-1){unsigned t=b&-b;r.emplace_back(u^t,sign_of(u,t));}
 return r;
}
ll det4(vector<vector<ll>> a){
 demand(a.size()==4 && a[0].size()==4,"det4 shape");
 ll result=0;
 for(int i=0;i<4;i++){
  vector<int> p;for(int j=0;j<4;j++)if(j!=i)p.push_back(j);
  ll minor=a[1][p[0]]*(a[2][p[1]]*a[3][p[2]]-a[2][p[2]]*a[3][p[1]])
          -a[1][p[1]]*(a[2][p[0]]*a[3][p[2]]-a[2][p[2]]*a[3][p[0]])
          +a[1][p[2]]*(a[2][p[0]]*a[3][p[1]]-a[2][p[1]]*a[3][p[0]]);
  result += (i%2?-1:1)*a[0][i]*minor;
 }
 return result;
}
int main(){
 try{
  array<unsigned,n> nbr{};
  auto edge=[&](int a,int b){nbr[a]|=1u<<b;nbr[b]|=1u<<a;};
  for(int i=0;i<10;i++){
   edge(i,(i+1)%10);
   edge(i,10+i);
   edge(10+i,10+(i+2)%10);
  }
  for(int v=0;v<n;v++)demand(bits(nbr[v])==3,"graph is not cubic");
  vector<uint8_t> face(N,0),unpaired(N,0);
  face[0]=1;
  vector<int> f(13,0);
  int count=0;
  for(unsigned s=1;s<N;s++){
   // In an undirected simple graph, induced components have <= 2 vertices
   // exactly when their maximum induced degree is <= 1.
   bool valid=true;
   for(unsigned t=s;t;t&=t-1){int v=__builtin_ctz(t);if(bits(nbr[v]&s)>1){valid=false;break;}}
   if(valid){face[s]=unpaired[s]=1;f[bits(s)-1]++;count++;}
  }
  demand(count==63142,"unexpected number of simplices");
  const vector<int> expected_f={20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5,0};
  demand(f==expected_f,"unexpected f vector");
  vector<int> mate(N,-1);
  // Staged element matching in increasing vertex order; the empty face is
  // excluded from the face poset. This is the matching of Prop. 2.10 in
  // Deshpande--Singh (arXiv:2001.05448), but acyclicity is also checked below.
  long long npairs=0;
  for(int v=0;v<n;v++){
   unsigned b=1u<<v;
   for(unsigned s=1;s<N;s++)if(face[s]&&unpaired[s]&&!(s&b)&&face[s|b]&&unpaired[s|b]){
    unpaired[s]=unpaired[s|b]=0;
    mate[s]=s|b;mate[s|b]=s;npairs++;
   }
  }
  map<int,vector<int>> critical;
  for(unsigned s=1;s<N;s++)if(face[s]&&mate[s]==-1)critical[bits(s)-1].push_back(s);
  demand(npairs==31565,"unexpected number of matched pairs");
  demand(critical.size()==4&&critical[0].size()==1&&critical[5].size()==1&&
         critical[6].size()==6&&critical[7].size()==4,"unexpected critical cells");
  // Full directed-Hasse graph: reverse each matched cover (lower -> upper),
  // orient every other cover down (upper -> lower), and topologically sort.
  vector<int> indeg(N,0);
  long long covers=0;
  for(unsigned s=1;s<N;s++)if(face[s]){
   for(unsigned t=s;t;t&=t-1){unsigned b=t&-t,u=s^b;if(!u)continue;
    demand(face[u],"not a simplicial complex");
    if(mate[u]==(int)s)indeg[s]++;else indeg[u]++;
    covers++;
   }
  }
  queue<int> q;
  for(unsigned s=1;s<N;s++)if(face[s]&&indeg[s]==0)q.push(s);
  int visited=0;
  while(!q.empty()){
   unsigned s=q.front();q.pop();visited++;
   // Only one upward outgoing cover is possible, namely its matched upper.
   if(mate[s]>(int)s){unsigned u=(unsigned)mate[s];if(!--indeg[u])q.push(u);}
   // Every unmatched downward cover is an outgoing edge.
   for(unsigned t=s;t;t&=t-1){unsigned b=t&-t,u=s^b;if(!u)continue;
    if(mate[u]!=(int)s){if(!--indeg[u])q.push(u);}
   }
  }
  demand(visited==count,"matching has a cycle");
  cout<<"f_vector";for(int x:f)cout<<" "<<x;cout<<"\n";
  cout<<"simplices="<<count<<" pairs="<<npairs<<" Hasse_covers="<<covers
      <<" topological_order="<<visited<<"\n";
  for(auto &p:critical){cout<<"critical_dim_"<<p.first<<":";for(int x:p.second)cout<<" "<<x;cout<<"\n";}
  // Signed integral gradient-path formula for the Morse boundary matrix.
  // For a k-face sigma matched UP to tau (a (k+1)-face),
  // [sigma] = -inc(sigma,tau) * sum_{u facet tau, u!=sigma} inc(u,tau)[u].
  // Facets paired down contribute zero; critical facets contribute basis units.
  auto morse_boundary=[&](int k){
   auto &targets=critical.at(k);auto &sources=critical.at(k+1);
   map<int,int> target_id;
   for(int j=0;j<(int)targets.size();j++)target_id[targets[j]]=j;
   const int cols=targets.size();
   unordered_map<int,vector<ll>> cache;
   function<vector<ll>(int)> expand=[&](int s)->vector<ll>{
    auto it=cache.find(s);if(it!=cache.end())return it->second;
    vector<ll> out(cols,0);
    int m=mate[s];
    if(m==-1){auto it2=target_id.find(s);if(it2!=target_id.end())out[it2->second]=1;}
    else if(m>s){
     int eps=sign_of((unsigned)m,(unsigned)(m^s));
     for(auto [u,c]:oriented_boundary((unsigned)m))if(u!=s){
      auto v=expand(u);
      for(int j=0;j<cols;j++)out[j]-=(ll)eps*c*v[j];
     }
    }
    cache.emplace(s,out);
    return out;
   };
   vector<vector<ll>> B(cols,vector<ll>(sources.size(),0));
   for(int i=0;i<(int)sources.size();i++){
    for(auto [s,c]:oriented_boundary((unsigned)sources[i])){
     auto v=expand(s);
     for(int j=0;j<cols;j++)B[j][i]+=(ll)c*v[j];
    }
   }
   return B;
  };
  auto B6=morse_boundary(5),B7=morse_boundary(6);
  const vector<vector<ll>> expected_B6={{0,0,-1,0,1,0}};
  const vector<vector<ll>> expected_B7={
   {1,1,0,0},{0,0,0,-1},{0,1,0,0},{0,-1,1,0},{0,1,0,0},{0,0,-1,0}};
  demand(B6==expected_B6&&B7==expected_B7,"Morse boundary mismatch");
  for(int c=0;c<4;c++){
   ll sum=0;for(int j=0;j<6;j++)sum+=B6[0][j]*B7[j][c];
   demand(sum==0,"Morse boundary does not square to zero");
  }
  // Since d6 is primitive, ker(d6) has rank five with basis
  // e0,e1,e3,e5,e2+e4. Restrict d7 to this basis; the first four rows
  // form a unimodular minor, leaving one free degree-six class.
  vector<vector<ll>> K;
  for(int j:vector<int>{0,1,3,5,4})K.push_back(B7[j]);
  vector<vector<ll>> M(K.begin(),K.begin()+4);
  demand(abs(det4(M))==1,"non-unimodular d7 image in ker d6");
  cout<<"morse_d6";for(ll x:B6[0])cout<<" "<<x;cout<<"\n";
  cout<<"morse_d7";for(auto &row:B7){cout<<"\n";for(ll x:row)cout<<" "<<x;}cout<<"\n";
  cout<<"primitive_d6=1 rank_d7=4 rank6=1, unimodular_minor="<<det4(M)<<"\n";
  // Signed simplicial Lefschetz number of cyclic rotations of the ten spokes.
  // Every permutation-fixed face is a union of vertex orbits. Its oriented
  // face contribution equals (-1)^dim times the sign of the permutation
  // induced on that face. In the reduced Euler-Lefschetz number, subtract 1.
  auto shifted=[&](int v,int t){return (v<10?0:10)+(v%10+t)%10;};
  for(int t=0;t<10;t++){
   ll raw=0;
   for(unsigned s=1;s<N;s++)if(face[s]){
    unsigned shifted_set=0;
    for(unsigned b=s;b;b&=b-1){int v=__builtin_ctz(b);shifted_set|=1u<<shifted(v,t);}
    if(shifted_set!=s)continue;
    // parity by inversions of images of the ordered vertices.
    vector<int> images;
    for(unsigned b=s;b;b&=b-1){int v=__builtin_ctz(b);images.push_back(shifted(v,t));}
    int parity=0;
    for(int i=0;i<(int)images.size();i++)for(int j=i+1;j<(int)images.size();j++)parity^=(images[i]>images[j]);
    int simplicial_sign=parity?-1:1;
    raw+=((bits(s)-1)&1)?-simplicial_sign:simplicial_sign;
   }
   ll reduced=raw-1;
   // The complex is S^6, so this reduced Lefschetz number is the
   // one-dimensional trace on H_6.
   demand(reduced==(t%2?-1:1),"rotation trace mismatch");
   cout<<"rotation_power="<<t<<" reduced_Lefschetz="<<reduced<<"\n";
  }
  cout<<"PASS: integral homotopy S^6 and C10 acts via sign on H6\n";
 }catch(const exception &e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
