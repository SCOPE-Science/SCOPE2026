// Exhaustive verification of the sharp rank-one pointed-type spectrum
// in finite permutations with two named linear orders.
// Build: g++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using Perm = std::array<int,10>;
static std::uint16_t spectrum(const Perm& p) {
    std::uint16_t s=0;
    for(int i=0;i<10;++i){
        unsigned mask=0;
        for(int j=0;j<10;++j){
            if(j==i) continue;
            if(j<i) mask |= (p[j]<p[i] ? 1u : 2u);
            else    mask |= (p[j]<p[i] ? 4u : 8u);
        }
        s |= static_cast<std::uint16_t>(1u<<mask);
    }
    return s;
}
static Perm transform(const Perm& p,int reverse_x,int reverse_y,int transpose){
    Perm q{};
    for(int i=0;i<10;++i){
        int x=reverse_x ? 9-i : i;
        int y=reverse_y ? 9-p[i] : p[i];
        if(transpose) std::swap(x,y);
        q[x]=y;
    }
    return q;
}
int main(){
    Perm p{};
    for(int i=0;i<10;++i)p[i]=i;
    std::map<unsigned,long long> by_signature;
    std::set<Perm> extremizers;
    long long examined=0;
    do {
        ++examined;
        auto s=spectrum(p);
        if(__builtin_popcount(static_cast<unsigned>(s))==10){
            ++by_signature[s];
            extremizers.insert(p);
        }
    } while (std::next_permutation(p.begin(),p.end()));
    assert(examined==3628800);
    assert(extremizers.size()==328);
    assert(by_signature.size()==2);
    assert(by_signature.at(0xfce8)==164);
    assert(by_signature.at(0xfea8)==164);
    long long orbit_count=0, orbit4=0, orbit8=0;
    while(!extremizers.empty()){
        Perm rep=*extremizers.begin();
        std::set<Perm> orbit;
        for(int rx=0;rx<2;++rx) for(int ry=0;ry<2;++ry)
            for(int swap=0;swap<2;++swap)
                orbit.insert(transform(rep,rx,ry,swap));
        for(const auto& q:orbit) {
            assert(extremizers.erase(q)==1);
        }
        ++orbit_count;
        if(orbit.size()==4)++orbit4;
        else if(orbit.size()==8)++orbit8;
        else assert(false);
    }
    assert(orbit_count==46 && orbit4==10 && orbit8==36);
    Perm witness={2,1,0,3,5,4,9,7,8,6};
    assert(__builtin_popcount(static_cast<unsigned>(spectrum(witness)))==10);
    std::cout<<"permutations_checked="<<examined<<"\n";
    std::cout<<"extremizers=328; signatures: 0xfce8=164, 0xfea8=164\n";
    std::cout<<"dihedral_orbits=46; size4=10, size8=36\n";
    std::cout<<"witness (one-indexed): 3 2 1 4 6 5 10 8 9 7\n";
}
