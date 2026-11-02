#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

static uint32_t reverse_bits(uint32_t x, int n) {
    uint32_t y = 0;
    for (int i=0; i<n; ++i) { y = (y << 1) | (x & 1u); x >>= 1; }
    return y;
}
static string bits(uint32_t x, int n) {
    string s;
    for (int i=0;i<n;++i) s.push_back((x & (1u<<i)) ? '1' : '0');
    return s;
}
static string signature(uint32_t w, int n) {
    string out(static_cast<size_t>(n*(n+3)/2), '\0');
    for (int start=0; start<n; ++start) {
        int ones=0;
        for (int end=start; end<n; ++end) {
            ones += ((w >> end)&1u);
            int length=end-start+1;
            int offset=(length-1)*(length+2)/2+ones;
            ++out[static_cast<size_t>(offset)];
        }
    }
    return out;
}
struct Class {vector<uint32_t> representatives; uint32_t members=0;};
int main(int argc, char** argv) {
    if (argc!=3) { cerr << "Usage: build_census CENSUS.csv FOURFOLD.tsv\n"; return 2; }
    ofstream census(argv[1]), fourfold(argv[2]);
    if (!census || !fourfold) throw runtime_error("cannot create output file");
    census << "n,spectra,size1,size2,size4,max_fiber,ambiguous_classes,ambiguous_words\n";
    fourfold << "class_id\tword_1\tword_2\tword_3\tword_4\n";
    for (int n=1;n<=23;++n) {
        unordered_map<string,Class> classes;
        classes.reserve((1u<<n)/2);
        const uint32_t limit=1u<<n;
        for (uint32_t w=0;w<limit;++w) {
            uint32_t r=reverse_bits(w,n);
            if(w>r) continue;
            auto &g=classes[signature(w,n)];
            g.representatives.push_back(w);
            g.members += (w==r ? 1u : 2u);
        }
        uint32_t a1=0,a2=0,a4=0, maximum=0;
        vector<array<string,4>> exceptional;
        for (const auto& kv:classes) {
            const Class &g=kv.second;
            if (g.members==1) ++a1;
            else if (g.members==2) ++a2;
            else if (g.members==4) {
                ++a4;
                if (g.representatives.size()!=2) throw runtime_error("size-four class not two reversal pairs");
                vector<string> all;
                for (uint32_t w:g.representatives) {
                    all.push_back(bits(w,n));
                    uint32_t r=reverse_bits(w,n);
                    if(w!=r)all.push_back(bits(r,n));
                }
                if(all.size()!=4) throw runtime_error("invalid fourfold orbit");
                sort(all.begin(),all.end());
                exceptional.push_back({all[0],all[1],all[2],all[3]});
            } else throw runtime_error("unexpected fiber size");
            maximum=max(maximum,g.members);
        }
        if (a1+2*a2+4*a4!=limit) throw runtime_error("fiber partition identity failed");
        census<<n<<','<<classes.size()<<','<<a1<<','<<a2<<','<<a4<<','<<maximum<<','<<a4<<','<<(4*a4)<<'\n';
        if(n==23) {
            sort(exceptional.begin(),exceptional.end());
            for (size_t i=0;i<exceptional.size();++i) {
                fourfold << (i+1);
                for(const auto& s:exceptional[i]) fourfold << '\t' << s;
                fourfold << '\n';
            }
        }
        cerr<<"n="<<n<<" fibers="<<classes.size()<<" fourfold="<<a4<<"\n";
    }
}
