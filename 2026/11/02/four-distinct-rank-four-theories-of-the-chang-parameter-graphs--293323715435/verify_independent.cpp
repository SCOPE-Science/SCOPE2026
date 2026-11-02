// Independent bitset verifier for bounded-depth graph distinctions.
// g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Edge=pair<int,int>;
using Matrix=array<uint32_t,28>;

Edge norm(int a,int b){return {min(a,b),max(a,b)};}
vector<Edge> vertices(){vector<Edge> v;for(int a=0;a<8;++a)for(int b=a+1;b<8;++b)v.push_back({a,b});return v;}
Matrix build(const vector<Edge>& V,const vector<Edge>& switchSet){
  set<Edge> S(switchSet.begin(),switchSet.end());Matrix adj{};
  for(int i=0;i<28;++i)for(int j=i+1;j<28;++j){
    auto [a,b]=V[i];auto [c,d]=V[j];
    bool meet=(a==c||a==d||b==c||b==d);
    bool e= meet^(S.count(V[i])!=S.count(V[j]));
    if(e){adj[i]|=(1u<<j);adj[j]|=(1u<<i);}
  }
  return adj;
}
inline bool e(const Matrix& M,int x,int y){return (M[x]>>y)&1u;}
int code4(const Matrix& M,const array<int,4>& a){
 int best=1000;
 array<int,4> p={0,1,2,3};
 do{int c=0;
   for(int i=0;i<4;i++)for(int j=i+1;j<4;j++) c=(c<<1)|e(M,a[p[i]],a[p[j]]);
   best=min(best,c);
 }while(next_permutation(p.begin(),p.end()));
 return best;
}
string label(const vector<Edge>& V,int a){return to_string(V[a].first)+to_string(V[a].second);}
int main(){
 auto V=vertices();
 const vector<vector<Edge>> sets={
  {},{{0,1},{0,2},{1,2},{3,4},{4,5},{5,6},{6,7},{3,7}},
  {{0,4},{1,5},{2,6},{3,7}},
  {{0,1},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{0,7}}
 };
 const vector<string> names={"triangular","chang_3plus5","chang_matching","chang_8cycle"};
 vector<array<int,4>> summary;
 for(int g=0;g<4;g++){
  auto M=build(V,sets[g]);
  for(int x=0;x<28;x++)assert(__builtin_popcount(M[x])==12);
  for(int x=0;x<28;x++)for(int y=x+1;y<28;y++)
    assert(__builtin_popcount(M[x]&M[y])==(e(M,x,y)?6:4));
  long long claw=0, badTri=0, badEdge=0;
  array<int,4> cw={-1,-1,-1,-1};array<int,3> tw={-1,-1,-1},ew={-1,-1,-1};
  for(int x=0;x<28;x++)for(int y=0;y<28;y++)if(y!=x)
   for(int z=0;z<28;z++)if(z!=x&&z!=y){
    bool extTri=false,extEdge=false;
    for(int w=0;w<28;w++)if(w!=x&&w!=y&&w!=z){
      if(!e(M,w,x)&&e(M,w,y)&&e(M,w,z))extTri=true;
      if(e(M,w,x)&&e(M,w,y)&&!e(M,w,z))extEdge=true;
      if(e(M,x,y)&&e(M,x,z)&&e(M,x,w)&&!e(M,y,z)&&!e(M,y,w)&&!e(M,z,w)){
        claw++;if(cw[0]<0)cw={x,y,z,w};
      }
    }
    if(e(M,x,y)&&e(M,x,z)&&e(M,y,z)&&!extTri){badTri++;if(tw[0]<0)tw={x,y,z};}
    if(!e(M,x,y)&&!e(M,x,z)&&e(M,y,z)&&!extEdge){badEdge++;if(ew[0]<0)ew={x,y,z};}
  }
  set<int> motifs;
  for(int a=0;a<28;a++)for(int b=a+1;b<28;b++)for(int c=b+1;c<28;c++)for(int d=c+1;d<28;d++)
    motifs.insert(code4(M,{a,b,c,d}));
  auto desc=[&](const array<int,3>& t){if(t[0]<0)return string("none");return label(V,t[0])+","+label(V,t[1])+","+label(V,t[2]);};
  cout<<names[g]<<" claw-ordered="<<claw<<" triangle-bad-ordered="<<badTri<<" edge-bad-ordered="<<badEdge<<" motifs4="<<motifs.size()<<"\n";
  cout<<" witnesses triangle="<<desc(tw)<<" edge="<<desc(ew)<<"\n";
  summary.push_back({int(claw>0),int(badTri>0),int(badEdge>0),int(motifs.size())});
 }
 assert((summary==vector<array<int,4>>{{0,0,0,10},{1,1,0,11},{1,0,1,11},{1,0,0,11}}));
 cout<<"BITSET_VERIFIER_PASS\n";
}
