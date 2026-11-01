// Exhaustive reduced simplicial Morse boundary certificate for pairwise-intersecting
// families of triples on a seven-element set. C++17 standard library only.
#include <bits/stdc++.h>
using namespace std;
using U = uint64_t;
using I = int32_t;
vector<U> faces, allowed;
vector<I> mate;
unordered_map<U,I> id;
vector<uint8_t> state;
vector<I> upper_order;
static inline int bits(U x){return __builtin_popcountll(x);}
static inline int sign_at(U f,int v){return (bits(f&((U(1)<<v)-1))&1)?-1:1;}
void enumerate(U avail,U f){
 faces.push_back(f);
 while(avail){U x=avail&-avail;int v=__builtin_ctzll(x);avail-=x;
  enumerate(avail&allowed[v],f|x);
 }
}
void dfs_upper(I s){
 if(state[s]==1)throw runtime_error("directed Morse cycle");
 if(state[s]==2)return;
 state[s]=1;
 U f=faces[s]; I lower=mate[s];
 for(U r=f;r;r&=r-1){int v=__builtin_ctzll(r);I k=id.at(f^(U(1)<<v));
  if(k==lower)continue;
  I j=mate[k];
  if(j>=0 && bits(faces[j])==bits(f))dfs_upper(j);
 }
 state[s]=2;upper_order.push_back(s);
}
vector<vector<long long>> boundary(int d){
 vector<I> lower,upper;
 int n=faces.size();
 for(I i=0;i<n;i++)if(mate[i]<0){
  if(bits(faces[i])==d)lower.push_back(i);
  if(bits(faces[i])==d+1)upper.push_back(i);
 }
 int t=lower.size();vector<I> lid(n,-1),lm(n,-1);
 for(int j=0;j<t;j++)lid[lower[j]]=j;
 int nl=0;
 for(I i=0;i<n;i++)if(mate[i]>=0&&bits(faces[i])==d&&bits(faces[mate[i]])==d+1)lm[i]=nl++;
 vector<long long> pool(size_t(nl)*t,0);
 auto ptr=[&](I i)->long long*{return pool.data()+size_t(lm[i])*t;};
 for(I s:upper_order){if(bits(faces[s])!=d+1)continue;
  I lo=mate[s];long long *dst=ptr(lo);U f=faces[s];
  int mv=__builtin_ctzll(f^faces[lo]);int a=sign_at(f,mv);
  for(U r=f;r;r&=r-1){int v=__builtin_ctzll(r);I i=id.at(f^(U(1)<<v));
   if(i==lo)continue;
   long long c=-(long long)a*sign_at(f,v);
   if(lid[i]>=0)dst[lid[i]]+=c;
   else if(lm[i]>=0){auto src=ptr(i);for(int j=0;j<t;j++){
     __int128 z=(__int128)dst[j]+(__int128)c*src[j];
     if(z<LLONG_MIN||z>LLONG_MAX)throw runtime_error("coefficient overflow");
     dst[j]=(long long)z;
   }}
  }
 }
 vector<vector<long long>> M(t,vector<long long>(upper.size()));
 for(int col=0;col<(int)upper.size();col++){
  U f=faces[upper[col]];
  for(U r=f;r;r&=r-1){int v=__builtin_ctzll(r);I i=id.at(f^(U(1)<<v));int c=sign_at(f,v);
   if(lid[i]>=0)M[lid[i]][col]+=c;
   else if(lm[i]>=0){auto src=ptr(i);for(int row=0;row<t;row++){
     __int128 z=(__int128)M[row][col]+(__int128)c*src[row];
     if(z<LLONG_MIN||z>LLONG_MAX)throw runtime_error("coefficient overflow");
     M[row][col]=(long long)z;
   }}
  }
 }
 return M;
}
int main(int argc,char**argv){
 try{
  bool rev=(argc>1 && string(argv[1])=="--reverse");
  vector<int> triples;
  for(int x=0;x<128;x++)if(__builtin_popcount((unsigned)x)==3)triples.push_back(x);
  if(triples.size()!=35)throw runtime_error("triple count");
  for(int a:triples){U c=0;for(int j=0;j<35;j++)if(a&triples[j])c|=U(1)<<j;allowed.push_back(c);}
  enumerate((U(1)<<35)-1,0);
  cout<<"faces_including_empty "<<faces.size()<<"\n";
  if(faces.size()!=1278686)throw runtime_error("face count");
  id.reserve(faces.size()*2);
  for(I i=0;i<(I)faces.size();i++){
   if(!id.emplace(faces[i],i).second)throw runtime_error("duplicate face");
  }
  vector<unsigned char> active(faces.size(),1);mate.assign(faces.size(),-1);
  long long np=0;
  for(int step=0;step<35;step++){
   int v=rev?34-step:step;U b=U(1)<<v;
   for(I i=0;i<(I)faces.size();i++)if(active[i]&&!(faces[i]&b)){
    auto it=id.find(faces[i]|b);
    if(it!=id.end()&&active[it->second]){
     I j=it->second;active[i]=active[j]=0;mate[i]=j;mate[j]=i;np++;
    }
   }
  }
  cout<<"matched_pairs "<<np<<"\n";
  map<int,int>critical;
  for(I i=0;i<(I)faces.size();i++)if(mate[i]<0)critical[bits(faces[i])-1]++;
  for(auto [d,k]:critical)cout<<"critical_degree_"<<d<<" "<<k<<"\n";
  state.resize(faces.size());
  for(I i=0;i<(I)faces.size();i++)
   if(mate[i]>=0&&bits(faces[i])>bits(faces[mate[i]])&&state[i]==0)dfs_upper(i);
  cout<<"acyclic_upper_faces "<<upper_order.size()<<"\n";
  if(upper_order.size()!=np)throw runtime_error("incomplete acyclicity check");
  const string prefix=rev?"reverse_boundary":"boundary";
  for(int d=1;d<=15;d++){
   if(critical.count(d)==0 && critical.count(d-1)==0)continue;
   auto M=boundary(d);int t=M.size(),w=t?M[0].size():critical[d];
   // The only nontrivial matrices for the chosen matching are degrees 7,8,9;
   // all other boundaries are necessarily the zero map to/from zero chain groups.
   if(t==0)continue;
   if(d!=7&&d!=8&&d!=9){if(w)throw runtime_error("unexpected Morse matrix");continue;}
   string name=prefix+to_string(d)+".txt";
   ofstream out(name);
   out<<t<<' '<<w<<'\n';
   long long nonzero=0,largest=0;
   for(auto&row:M){for(auto x:row){out<<x<<' ';nonzero+=(x!=0);largest=max(largest,llabs(x));}out<<'\n';}
   cout<<"boundary_degree_"<<d<<"_shape "<<t<<"x"<<w<<" nonzero "<<nonzero<<" max_abs "<<largest<<"\n";
  }
  cout<<"MORSE_CERTIFICATE_OK\n";
 }catch(const exception&e){cerr<<"FAILED: "<<e.what()<<'\n';return 1;}
}
