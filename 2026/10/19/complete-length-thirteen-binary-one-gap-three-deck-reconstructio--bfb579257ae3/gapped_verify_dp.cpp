#include <algorithm>
// Exact finite census of binary one-gap, up-to-three subsequence decks.
// Compile: c++ -std=c++17 -O2 gapped_verify_dp.cpp -o verify_dp
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using Sig = array<int,14>; // length-one (2), length-two (4), length-three (8)
static string bits(unsigned x,int n) {
    string z(n,'0'); for(int i=0;i<n;i++) z[i]=char('0'+((x>>(n-1-i))&1u)); return z;
}
static Sig profile(unsigned x,int n) {
    Sig f{},prev{},prior{};
    // At the start of iteration i, f = F_{i-1}, prior = F_{i-2}.
    // The zero-length count in any prefix is 1 and is handled explicitly.
    for(int i=0;i<n;i++) {
        int b=(x>>(n-1-i))&1u;
        Sig next=f;
        next[b]++;
        for(int q=0;q<2;q++) next[2+2*q+b]+=prior[q];
        for(int q=0;q<4;q++) next[6+2*q+b]+=prior[2+q];
        prior=f; f=next;
    }
    return f;
}
int main() {
    const vector<pair<string,string>> wanted={
      {"0001010000100","0010000101000"},
      {"0101111010110","0110101111010"},
      {"1001010000101","1010000101001"},
      {"1101111010111","1110101111011"}
    };
    for(int n=1;n<=13;n++) {
        map<Sig,vector<unsigned>> bins;
        for(unsigned x=0;x<(1u<<n);x++) bins[profile(x,n)].push_back(x);
        vector<pair<string,string>> doubled;
        size_t singleton=0, other=0;
        for(const auto& [key,group]:bins) {
            if(group.size()==1) {singleton++;continue;}
            if(group.size()!=2) {other++;continue;}
            string a=bits(group[0],n), b=bits(group[1],n);
            doubled.emplace_back(a,b);
        }
        sort(doubled.begin(),doubled.end());
        cout<<"n="<<n<<" classes="<<bins.size()<<" singleton="<<singleton
            <<" doubleton="<<doubled.size()<<" larger="<<other<<"\n";
        if(n==2) { assert(singleton==2 && doubled.size()==1 && other==0); }
        if(n>=3 && n<=12) { assert(bins.size()==(1u<<n) && doubled.empty() && other==0); }
        if(n==13) {
            assert(bins.size()==8188 && singleton==8184 && doubled.size()==4 && other==0);
            assert(doubled==wanted);
            for(auto [a,b]:doubled) {
                string r=a;reverse(r.begin(),r.end());assert(r==b);
                cout << "  " << a << " <=> " << b << "\n";
            }
        }
    }
    cout<<"VERIFY_DP_OK\n";
}
