// Independent bit-vector check of XOR dynamics under one toggled incidence.
// Example inputs are the symmetric 2-(4,3,2) design and the Paley 2-(11,5,2) biplane.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using U = std::uint64_t;
using M = std::vector<U>;
static int pop(U x) { return __builtin_popcountll(x); }
static U act(const M& m, U x) { U y=0; for(int i=0;i<(int)m.size();++i) y |= U(pop(m[i]&x)&1)<<i; return y; }
static int binary_rank(M a) {
  const int n=a.size();int r=0;
  for(int bit=0;bit<n;++bit){int k=r;
    while(k<n && !((a[k]>>bit)&1))++k;
    if(k==n)continue;
    std::swap(a[k],a[r]);
    for(int j=0;j<n;++j) if(j!=r && ((a[j]>>bit)&1))a[j]^=a[r];
    ++r;
  }
  return r;
}
static M map_rows(int n, const std::vector<M::value_type>& raw, int point,int block) {
  M m(2*n,0);
  for(int i=0;i<n;++i)for(int j=0;j<n;++j) {
    int v=(int((raw[i]>>j)&1)^int(i==point&&j==block));
    if(v) {m[i]|=U(1)<<(n+j);m[n+j]|=U(1)<<i;}
  }
  return m;
}
static int iter_rank(const M& m,int p){
  int n=m.size();M cols(n,0);for(int j=0;j<n;++j){U x=U(1)<<j;for(int t=0;t<p;++t)x=act(m,x);cols[j]=x;}
  return binary_rank(cols);
}
static int fixed_dim(const M& m,int p){
  int n=m.size();M cols(n,0);for(int j=0;j<n;++j){U x=U(1)<<j;for(int t=0;t<p;++t)x=act(m,x);cols[j]=x^(U(1)<<j);}
  return n-binary_rank(cols);
}
int main(){
  std::vector<std::pair<std::string,M>> designs;
  M d4(4,0);for(int i=0;i<4;++i)for(int j=0;j<4;++j)if(i!=j)d4[i]|=U(1)<<j;
  designs.push_back({"complement_singletons_4",d4});
  M d11(11,0);const int residues[]={1,3,4,5,9};
  for(int i=0;i<11;++i)for(int d:residues)d11[i]|=U(1)<<((i+d)%11);
  designs.push_back({"paley_biplane_11",d11});
  for(auto [name,d]:designs){
    const int n=d.size();int ct0=0,ct1=0;
    for(int i=0;i<n;++i)for(int j=0;j<n;++j){
      bool original=(d[i]>>j)&1;
      M f=map_rows(n,d,i,j);
      if(original){
        ++ct1;
        assert(iter_rank(f,1)==2*n-2 && iter_rank(f,2)==2*n-2);
        assert(fixed_dim(f,1)==n-2 && fixed_dim(f,2)==2*n-4);
        assert(fixed_dim(f,4)==2*n-2);
        assert(fixed_dim(f,3)==n-2);
        // The 1-step image is periodic with orders dividing four.
        for(int b=0;b<2*n;++b){U x=U(1)<<b;
          assert(act(f,act(f,act(f,act(f,act(f,x)))))==act(f,x));}
      }else{
        ++ct0;
        assert(iter_rank(f,1)==2*n && iter_rank(f,6)==2*n);
        assert(fixed_dim(f,1)==n-2 && fixed_dim(f,2)==2*n-4);
        assert(fixed_dim(f,3)==n && fixed_dim(f,6)==2*n);
        for(int b=0;b<2*n;++b){U x=U(1)<<b,y=x;for(int t=0;t<6;++t)y=act(f,y);assert(x==y);}
      }
    }
    std::cout<<name<<" n="<<n<<" inserted="<<ct0<<" deleted="<<ct1<<" all_toggle_checks=PASS\n";
  }
  M d=d4;
  for(int j=0;j<4;++j)if(j==0||j==1){
    M f=map_rows(4,d,0,j);
    std::map<int,int> period,entrance;
    for(U initial=0;initial<(U(1)<<8);++initial){
      std::map<U,int> seen;U s=initial;int step=0;
      while(!seen.count(s)){seen[s]=step++;s=act(f,s);}
      int start=seen.at(s), cyc=step-start;
      ++entrance[start];if(start==0)++period[cyc];
    }
    if(j==0){assert(period[1]==4 && period[2]==12 && period[3]==12 && period[6]==228);assert(entrance[0]==256);}
    else {assert(period[1]==4 && period[2]==12 && period[4]==48);assert(entrance[0]==64 && entrance[1]==192);}
    std::cout<<"exhaustive_256 "<<(j==0?"insert":"delete")<<" periodic_point_counts=";
    for(auto [k,v]:period)std::cout<<k<<":"<<v<<" ";
    std::cout<<"entrance=";for(auto [k,v]:entrance)std::cout<<k<<":"<<v<<" ";std::cout<<"PASS\n";
  }
}
