// Exact enumeration of the quarter-phase four-qubit balanced-purity optimum.
// Build: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>

using Phases=std::array<int,16>;
constexpr std::array<int,11> free_site={3,5,6,7,9,10,11,12,13,14,15};
std::array<std::array<std::array<int,4>,4>,3> cells{};
void initialize(){
  for(int p=0;p<3;++p){
    const int left0=0,left1=p+1;
    int right[2],t=0;
    for(int j=0;j<4;++j)if(j!=left0 && j!=left1)right[t++]=j;
    for(int a=0;a<4;++a)for(int b=0;b<4;++b)
      cells[p][a][b]=(((a&1)!=0)<<left0)|(((a&2)!=0)<<left1)|
                      (((b&1)!=0)<<right[0])|(((b&2)!=0)<<right[1]);
  }
}
Phases unpack(std::uint32_t m){
  Phases f{};
  for(int x:free_site){f[x]=int(m&3u);m>>=2;}
  return f;
}
std::uint32_t pack(Phases const&f){
  const int c0=f[0];int c[4];
  for(int j=0;j<4;++j)c[j]=(f[1<<j]-c0)&3;
  Phases h{};
  for(int x=0;x<16;++x){
    int v=f[x]-c0;
    for(int j=0;j<4;++j)if(x&(1<<j))v-=c[j];
    h[x]=v&3;
  }
  for(int x:{0,1,2,4,8})if(h[x]!=0)throw std::runtime_error("gauge failure");
  std::uint32_t m=0;
  for(int j=0;j<11;++j)m |= std::uint32_t(h[free_site[j]])<<(2*j);
  return m;
}
int purity_times_256(Phases const&f,int p){
  int total=64;
  for(int a=0;a<4;++a)for(int aa=a+1;aa<4;++aa){
    int re=0,im=0;
    for(int b=0;b<4;++b){
      int d=(f[cells[p][a][b]]-f[cells[p][aa][b]])&3;
      re+=(d==0)-(d==2);
      im+=(d==1)-(d==3);
    }
    total+=2*(re*re+im*im);
  }
  return total;
}
std::uint32_t transform(std::uint32_t m, std::array<int,4> const& perm,int flips,bool conj){
  Phases f=unpack(m),g{};
  for(int y=0;y<16;++y){
    int x=flips;
    for(int j=0;j<4;++j)if((y>>j)&1)x^=1<<perm[j];
    g[y]=(conj?-f[x]:f[x])&3;
  }
  return pack(g);
}
int main(){
  initialize();
  constexpr std::uint32_t N=(1u<<22);
  int best=257,best_real=257;
  std::set<std::uint32_t> optimizers;
  int count_real=0;
  for(std::uint32_t m=0;m<N;++m){
    Phases f=unpack(m);
    int vals[3];
    for(int p=0;p<3;++p){
      vals[p]=purity_times_256(f,p);
      if(vals[p]%4!=0 || vals[p]<64 || vals[p]>256)
        throw std::runtime_error("bad purity arithmetic");
    }
    int v=std::max({vals[0],vals[1],vals[2]});
    if(v<best){best=v;optimizers.clear();}
    if(v==best){
      optimizers.insert(m);
      if(vals[0]!=88 || vals[1]!=88 || vals[2]!=88){
        // For other interim minima, the final optimum need not be equidistributed.
        if(v==88)throw std::runtime_error("non-equidistributed minimizer");
      }
    }
    bool binary=true;
    for(int s:free_site)if((f[s]&1)!=0){binary=false;break;}
    if(binary){
      if(v<best_real){best_real=v;count_real=0;}
      if(v==best_real)++count_real;
    }
  }
  if(best!=88 || optimizers.size()!=96 || best_real!=96)
    throw std::runtime_error("exhaustive optimum/count discrepancy");
  for(auto m:optimizers){
    Phases f=unpack(m);
    if(pack(f)!=m)throw std::runtime_error("gauge ambiguity");
    for(int p=0;p<3;++p)if(purity_times_256(f,p)!=88)
      throw std::runtime_error("unbalanced optimum");
  }
  std::set<std::uint32_t> orbit;
  const auto rep=*optimizers.begin();
  std::array<int,4> perm={0,1,2,3};
  do{
    for(int mask=0;mask<16;++mask)for(int conj=0;conj<2;++conj)
      orbit.insert(transform(rep,perm,mask,conj!=0));
  }while(std::next_permutation(perm.begin(),perm.end()));
  if(orbit!=optimizers)throw std::runtime_error("optimizer orbit mismatch");
  std::cout<<"VERIFY_OK exhaustive="<<N<<" optimum="<<best<<"/256"
           <<" canonical_minimizers="<<optimizers.size()
           <<" one_symmetry_orbit="<<orbit.size()
           <<" real_optimum="<<best_real<<"/256"
           <<" real_minimizers="<<count_real<<" representative="<<rep<<"\n";
}
