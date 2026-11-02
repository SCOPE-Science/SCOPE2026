#include <bits/stdc++.h>
using namespace std;
struct VHash { size_t operator()(vector<int> const &v) const noexcept {uint64_t h=1469598103934665603ULL;for(int x:v){h^=x+0x9e3779b9;h*=1099511628211ULL;}return h;}};
struct Interner {unordered_map<vector<int>,int,VHash> dict; int intern(vector<int> &v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());auto it=dict.find(v);if(it!=dict.end())return it->second;int id=dict.size()+1;dict.emplace(v,id);return id;}};
struct Plane {int q,N,Np;vector<int> sortv;vector<vector<unsigned char>> I;Plane(int v):q(v),Np(v*v),N(v*v+v*(v+1)),sortv(N),I(N,vector<unsigned char>(N,0)){
  for(int l=0;l<q*(q+1);l++){int slope=l/q,b=l%q;int L=Np+l;sortv[L]=1;for(int x=0;x<q;x++)for(int y=0;y<q;y++){int p=x*q+y;bool on=(slope==q?x==b:y==add(mul(slope,x),b));if(on)I[p][L]=I[L][p]=1;}}
  for(int p=0;p<Np;p++){int c=0;for(int l=Np;l<N;l++)c+=I[p][l];if(c!=q+1)throw runtime_error("wrong degree");}
 }
int add(int a,int b){return q==4?(a^b):((a+b)%q);} int mul(int a,int b){if(q!=4)return a*b%q;int z=0;for(int k=0;k<2;k++)if((b>>k)&1){int y=a;for(int j=0;j<k;j++){y=y<<1;if(y&4)y^=7;}z^=y;}return z;}
int atomic(int a,int b,int c,int d){int v[4]={a,b,c,d};int id=0;for(int i=0;i<4;i++)id|=(sortv[v[i]]<<i);int bit=4;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){id|=((v[i]==v[j])<<bit++);}for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){id|=(int(I[v[i]][v[j]])<<bit++);}return id;}
};
int main(int argc,char **argv){ vector<int> qs={2,3,4,5}; if(argc>1){qs.clear();for(int i=1;i<argc;i++)qs.push_back(atoi(argv[i]));}Interner a,b,c,d;for(int q:qs){Plane P(q);int n=P.N;vector<int> ty1(n*n*n);vector<int> ty2(n*n),ty3(n);vector<int> v;v.reserve(n);for(int x=0;x<n;x++)for(int y=0;y<n;y++)for(int z=0;z<n;z++){v.clear();for(int w=0;w<n;w++)v.push_back(P.atomic(x,y,z,w));ty1[(x*n+y)*n+z]=a.intern(v);}for(int x=0;x<n;x++)for(int y=0;y<n;y++){v.clear();for(int z=0;z<n;z++)v.push_back(ty1[(x*n+y)*n+z]);ty2[x*n+y]=b.intern(v);}for(int x=0;x<n;x++){v.clear();for(int y=0;y<n;y++)v.push_back(ty2[x*n+y]);ty3[x]=c.intern(v);}v.clear();for(int x=0;x<n;x++)v.push_back(ty3[x]);int t=d.intern(v);set<int> ranksingle(ty3.begin(),ty3.end());cout<<"q="<<q<<" points="<<P.Np<<" lines="<<n-P.Np<<" type4="<<t<<" types1="<<ranksingle.size()<<" total_interned="<<a.dict.size()<<","<<b.dict.size()<<","<<c.dict.size()<<","<<d.dict.size()<<"\n"<<flush;}}
