// Independent construction: recursive inequality-pruned enumeration and certificate replay.
// Compile with: c++ -std=c++17 -O2 verify_alternative.cpp -o verify_alt
// Run: ./verify_alt [certificate path]
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
static int n;
static vector<vector<int>> states;
static vector<int> curr;
static void generate(int used) {
    int k=(int)curr.size();
    if(k==n){states.push_back(curr);return;}
    for(int v=0;v<n;++v) {
        if(used&(1<<v)) continue;
        if(k>0 && ((k-1)%2==0 ? !(curr.back()<v) : !(curr.back()>v)))continue;
        curr.push_back(v);
        generate(used|(1<<v));
        curr.pop_back();
    }
}
int main(int argc,char**argv){
    ifstream f(argc>1?argv[1]:"gray_paths_u16le.bin",ios::binary);
    assert(f.good());
    const array<pair<int,int>,4> specs{{{4,5},{6,61},{8,1385},{10,50521}}};
    for(auto [dim,count]:specs){
        n=dim;states.clear();curr.clear();generate(0);
        assert((int)states.size()==count);
        vector<int> path; path.reserve(count);vector<char> seen(count,0);
        for(int step=0;step<count;++step){
           unsigned char b[2]; f.read((char*)b,2);assert(f.gcount()==2);
           int idx=b[0]+256*b[1];assert(idx>=0&&idx<count&&!seen[idx]);
           seen[idx]=1;path.push_back(idx);
           if(step){
               const auto &a=states[path[step-1]],&c=states[idx];
               int i=-1,j=-1;
               for(int k=0;k<n;++k)if(a[k]!=c[k]){if(i<0)i=k;else if(j<0)j=k;else assert(false);}
               assert(i>=0&&j>=0&&j>i+1&&a[i]==c[j]&&a[j]==c[i]);
           }
        }
        for(char bit:seen) assert(bit);
        cout<<"ALTERNATIVE_PASS n="<<n<<" states="<<count<<"\n";
    }
    assert(f.peek()==char_traits<char>::eof());
    cout<<"ALTERNATIVE_ALL_PASS\n";
}
