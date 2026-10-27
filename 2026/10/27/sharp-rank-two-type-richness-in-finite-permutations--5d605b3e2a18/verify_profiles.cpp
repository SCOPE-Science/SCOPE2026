// Reproducible finite census for the rank-one point-type spectrum of permutations.
// Public research code; standard C++17, no external packages.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

uint32_t signature_direct(const vector<int>&p){
  int n=(int)p.size();uint32_t seen=0;
  for(int i=0;i<n;i++){
    int type=0;
    for(int j=0;j<n;j++){
      if(i==j)continue;
      int b=(j<i?0:2)+(p[j]<p[i]?0:1);
      type|=(1<<b);
    }
    seen|=(uint32_t(1)<<type);
  }
  return seen;
}

uint32_t signature_records(const vector<int>&p){
  int n=(int)p.size();vector<int>lmin(n),lmax(n),rmin(n),rmax(n);
  int low=n,high=-1;
  for(int i=0;i<n;i++){
    lmin[i]=low;lmax[i]=high;
    low=min(low,p[i]);high=max(high,p[i]);
  }
  low=n;high=-1;
  for(int i=n-1;i>=0;i--){
    rmin[i]=low;rmax[i]=high;
    low=min(low,p[i]);high=max(high,p[i]);
  }
  uint32_t seen=0;
  for(int i=0;i<n;i++){
    int t=(p[i]>lmin[i])+(2*(p[i]<lmax[i]))
         +(4*(p[i]>rmin[i]))+(8*(p[i]<rmax[i]));
    seen|=(uint32_t(1)<<t);
  }
  return seen;
}

vector<int> inverse(const vector<int>&p){
  vector<int>out(p.size());for(int i=0;i<(int)p.size();i++)out[p[i]]=i;return out;
}
vector<int> reverse_position(vector<int>p){reverse(p.begin(),p.end());return p;}
vector<int> reverse_value(vector<int>p){int n=(int)p.size();for(int&v:p)v=n-1-v;return p;}
vector<vector<int>> symmetry_orbit(const vector<int>&p){
  vector<vector<int>>o;
  for(auto q:{p,inverse(p)})for(auto r:{q,reverse_position(q)})
    for(auto s:{r,reverse_value(r)})o.push_back(s);
  sort(o.begin(),o.end());o.erase(unique(o.begin(),o.end()),o.end());return o;
}

int main(){
  const int wanted[11]={0,1,2,3,4,5,6,7,8,9,10};
  unsigned long long all=0,extreme=0;
  map<uint32_t,int>extreme_sigs;
  map<vector<int>,int>orbits;
  for(int n=1;n<=10;n++){
    vector<int>p(n);iota(p.begin(),p.end(),0);
    int max_type_count=0;unsigned long long n_total=0,n_extreme=0;
    do{
      uint32_t a=signature_direct(p);
      uint32_t b=signature_records(p);
      assert(a==b);
      int k=__builtin_popcount(a);
      max_type_count=max(max_type_count,k);
      if(k==n)n_extreme++;
      if(n==10 && k==10){
        ++extreme;extreme_sigs[a]++;
        auto orbit=symmetry_orbit(p);
        assert(orbit.size()==4 || orbit.size()==8);
        orbits[orbit.front()]=(int)orbit.size();
        for(const auto&q:orbit)assert(__builtin_popcount(signature_records(q))==10);
      }
      n_total++;
    }while(next_permutation(p.begin(),p.end()));
    cout<<"n="<<n<<" checked="<<n_total<<" max_types="<<max_type_count<<" exactly_n_types="<<n_extreme<<"\n";
    assert(max_type_count==wanted[n]);all+=n_total;
  }
  map<int,int>orbit_sizes;
  for(const auto&e:orbits)orbit_sizes[e.second]++;
  cout<<"total_permutations_checked="<<all<<"\n";
  cout<<"length10_extremizers="<<extreme<<"\n";
  for(auto[k,v]:extreme_sigs)cout<<"signature="<<k<<" count="<<v<<"\n";
  for(auto[k,v]:orbit_sizes)cout<<"orbits_of_size_"<<k<<"="<<v<<"\n";
  assert(extreme==328);
  assert(extreme_sigs.size()==2);
  assert(extreme_sigs.at(64744)==164 && extreme_sigs.at(65192)==164);
  assert(orbit_sizes[4]==10 && orbit_sizes[8]==36);
  assert(10*4+36*8==328);
  cout<<"ALL_CHECKS_PASS\n";
}
