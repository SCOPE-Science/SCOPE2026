#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
struct Geometry {
 int q,d,n; vector<vector<int>> vec; vector<uint8_t> inc; vector<uint8_t> sortbit;
 int mul(int a,int b) const { if(q!=4) return (a*b)%q; int res=0;for(int i=0;i<2;i++)for(int j=0;j<2;j++)if(((a>>i)&1)&&((b>>j)&1))res^=(1<<(i+j));if(res&4)res^=7;return res;}
 int add(int a,int b) const {return q==4?(a^b):((a+b)%q);}
 int inv(int a) const {for(int b=1;b<q;b++)if(mul(a,b)==1)return b;abort();}
 Geometry(int q_,int d_):q(q_),d(d_){
   int N=1;for(int i=0;i<d+1;i++)N*=q;
   for(int i=1;i<N;i++){
     int tmp=i;vector<int> x(d+1);for(int j=0;j<d+1;j++){x[j]=tmp%q;tmp/=q;}
     int lead=0;while(x[lead]==0)lead++;int u=inv(x[lead]);for(auto &a:x)a=mul(a,u);
     if(find(vec.begin(),vec.end(),x)==vec.end())vec.push_back(x);
   }
   int M=vec.size();n=2*M;inc.assign(n*n,0);sortbit.resize(n);
   for(int a=0;a<n;a++)sortbit[a]=a>=M;
   for(int a=0;a<M;a++)for(int b=0;b<M;b++){
     int z=0;for(int j=0;j<d+1;j++)z=add(z,mul(vec[a][j],vec[b][j]));
     inc[a*n+(M+b)]=inc[(M+b)*n+a]=(z==0);
   }
   cout<<"GEOMETRY q="<<q<<" d="<<d<<" points="<<M<<" hyperplanes="<<M<<" total="<<n<<"\n";
 }
 int atom4(int a,int b,int c,int e)const{
   int v[4]={a,b,c,e},t=0;
   for(int i=0;i<4;i++)t|=int(sortbit[v[i]])<<i;
   int idx=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++,idx++){
      if(v[i]==v[j])t|=1<<(4+idx);
      if(inc[v[i]*n+v[j]])t|=1<<(10+idx);
   }
   return t;
 }
};
struct GlobalMaps {
 map<vector<int>,int> maps[4];
 int id(int layer,vector<int>&v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());auto &mp=maps[layer];auto it=mp.find(v);if(it!=mp.end())return it->second;int idx=mp.size();mp.emplace(v,idx);return idx;}
};
int signature(Geometry &g,GlobalMaps &M){
 int n=g.n;vector<int> triple(n*n*n);vector<int> v;v.reserve(n);
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++){
    v.clear();for(int x=0;x<n;x++)v.push_back(g.atom4(a,b,c,x));
    triple[(a*n+b)*n+c]=M.id(0,v);
 }
 cout<<"TRIPLE_RANK1_PROFILES q="<<g.q<<" d="<<g.d<<" unique="<<M.maps[0].size()<<"\n";
 vector<int> pair(n*n);for(int a=0;a<n;a++)for(int b=0;b<n;b++){
   v.clear();for(int c=0;c<n;c++)v.push_back(triple[(a*n+b)*n+c]);pair[a*n+b]=M.id(1,v);
 }
 vector<int> single(n);for(int a=0;a<n;a++){
   v.clear();for(int b=0;b<n;b++)v.push_back(pair[a*n+b]);single[a]=M.id(2,v);
 }
 v=single;int root=M.id(3,v);cout<<"ROOT_RANK4 q="<<g.q<<" d="<<g.d<<" canonical="<<root<<" types="<<M.maps[0].size()<<","<<M.maps[1].size()<<","<<M.maps[2].size()<<","<<M.maps[3].size()<<"\n";return root;
}
int main(){GlobalMaps M; Geometry g23(2,3);int a=signature(g23,M); Geometry g24(2,4);int b=signature(g24,M);Geometry g33(3,3);int c=signature(g33,M); assert(a==b);assert(a!=c);cout<<"BINARY_DIMENSION_STABILITY_AND_TERNARY_SEPARATOR_OK\n";cout<<"VERIFY_OK\n";}
