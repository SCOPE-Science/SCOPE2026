// Exact ternary (1,3)-overlap-free code enumeration. C++17, standard library only.
// Compile: c++ -O3 -std=c++17 verify_overlap.cpp -o verify_overlap
// Run: ./verify_overlap
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Mask = uint32_t;
constexpr int Q=3,K=3,N=27;
constexpr uint64_t ALL=uint64_t(1)<<N;
array<array<int,3>,N> words{};
array<Mask,N> conflicts{};
array<vector<int>,N> adjacency{};
vector<Mask> optimum;
int recBest=0;
uint64_t recCount=0,recLeaves=0;

void recur(int i,Mask forbidden,int pcount,Mask chosen){
    if(i==N){
        ++recLeaves;
        int product=pcount*(N-__builtin_popcount(forbidden));
        if(product>recBest){recBest=product;recCount=0;optimum.clear();}
        if(product==recBest){++recCount;optimum.push_back(chosen);}
        return;
    }
    recur(i+1,forbidden,pcount,chosen);
    recur(i+1,forbidden|conflicts[i],pcount+1,chosen|(Mask(1)<<i));
}

Mask compatible_suffixes(Mask p){
    Mask forbidden=0;
    for(int i=0;i<N;i++)if(p&(Mask(1)<<i)) forbidden|=conflicts[i];
    return ((Mask(1)<<N)-1)^forbidden;
}
Mask transform(Mask original, const array<int,N>& map){
    Mask result=0;
    for(int i=0;i<N;i++)if(original&(Mask(1)<<i))result|=Mask(1)<<map[i];
    return result;
}
int main(){
    for(int i=0;i<N;i++)words[i]={i/9,(i/3)%3,i%3};
    // Precompute directed forbidden-prefix / forbidden-suffix pairs by literal comparisons.
    for(int p=0;p<N;p++)for(int s=0;s<N;s++){
        bool bad=false;
        for(int t=1;t<=3;t++){
            bool equal=true;
            for(int j=0;j<t;j++)if(words[p][j]!=words[s][3-t+j])equal=false;
            if(equal)bad=true;
        }
        if(bad){conflicts[p]|=Mask(1)<<s;adjacency[p].push_back(s);}
    }
    recur(0,0,0,0);
    sort(optimum.begin(),optimum.end());
    if(recLeaves!=ALL || recBest!=72 || recCount!=42 || optimum.size()!=42){
        cerr << "Recursive enumeration disagreement.\n";return 1;
    }
    // Independent Gray-code exhaustive sweep with incrementally maintained suffix multiplicities.
    array<int,N> covered{};
    Mask old=0; int pcount=0,sfree=N;
    uint64_t grayCount=0; int grayBest=-1;
    vector<Mask> grayOptimum;
    for(uint64_t step=0;step<ALL;step++){
        if(step){
            Mask g=Mask(step^(step>>1));
            int bit=__builtin_ctz(g^old);
            bool adding=(g&(Mask(1)<<bit))!=0;
            old=g;
            pcount+=adding?1:-1;
            for(int s:adjacency[bit]){
                if(adding){if(covered[s]++==0)--sfree;}
                else{if(--covered[s]==0)++sfree;}
            }
        }
        const int product=pcount*sfree;
        if(product>grayBest){grayBest=product;grayCount=0;grayOptimum.clear();}
        if(product==grayBest){++grayCount;grayOptimum.push_back(old);}
    }
    sort(grayOptimum.begin(),grayOptimum.end());
    if(grayBest!=recBest || grayCount!=recCount || grayOptimum!=optimum){
        cerr << "Independent enumeration disagreement.\n";return 2;
    }
    // Check a concrete code by directly testing all 72 x 72 word pairs and overlap lengths.
    vector<array<int,6>> witness;
    for(int p=0;p<N;p++)if(words[p][0]==0)
      for(int s=0;s<N;s++)if(words[s][0]!=0 && words[s][1]!=0 && words[s][2]!=0)
        witness.push_back({words[p][0],words[p][1],words[p][2],words[s][0],words[s][1],words[s][2]});
    if(witness.size()!=72)return 3;
    for(const auto& a:witness)for(const auto& b:witness)for(int t=1;t<=3;t++){
        bool match=true;
        for(int j=0;j<t;j++)if(a[j]!=b[6-t+j])match=false;
        if(match){cerr<<"Invalid witness overlap.\n";return 4;}
    }
    // Maximum code sizes by the sizes of their prefix and suffix families.
    map<pair<int,int>,int> profiles;
    set<pair<Mask,Mask>> all;
    for(Mask p:optimum){Mask s=compatible_suffixes(p);
        profiles[{__builtin_popcount(p),__builtin_popcount(s)}]++;
        all.insert({p,s});
    }
    const map<pair<int,int>,int> expected={{{6,12},6},{{8,9},15},{{9,8},15},{{12,6},6}};
    if(profiles!=expected || all.size()!=42)return 5;
    // Symmetries: six alphabet relabelings, optionally followed by word reversal.
    array<int,N> reversal{};
    for(int i=0;i<N;i++)reversal[i]=words[i][2]*9+words[i][1]*3+words[i][0];
    vector<array<int,N>> permutations;
    array<int,3> abc={0,1,2};
    do{
        array<int,N> pi{};
        for(int i=0;i<N;i++)pi[i]=abc[words[i][0]]*9+abc[words[i][1]]*3+abc[words[i][2]];
        permutations.push_back(pi);
    }while(next_permutation(abc.begin(),abc.end()));
    set<pair<Mask,Mask>> remaining=all;
    map<int,int> orbits;
    while(!remaining.empty()){
        auto rep=*remaining.begin();
        set<pair<Mask,Mask>> orbit;
        for(const auto& pi:permutations){
            Mask pp=transform(rep.first,pi),ss=transform(rep.second,pi);
            orbit.insert({pp,ss});
            orbit.insert({transform(ss,reversal),transform(pp,reversal)});
        }
        for(auto x:orbit)if(!all.count(x)){cerr<<"Symmetry not closed.\n";return 6;}
        for(auto x:orbit)remaining.erase(x);
        orbits[(int)orbit.size()]++;
    }
    if(orbits!=map<int,int>{{6,1},{12,3}})return 7;
    cout<<"OVERLAP_Q3_K3_PASS maximum=72 maximum_codes=42 "
        <<"symmetry_orbits=6+12+12+12 exhaustive_prefix_families="<<ALL
        <<" profiles=(6,12):6,(8,9):15,(9,8):15,(12,6):6\n";
    return 0;
}
