// Exhaustive face-poset verifier for the radius-two Hamming-ball nerve on Q_5.
// Requires a C++17 compiler. Usage: g++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
    constexpr int n=5, V=1<<n, radius=2;
    vector<uint32_t> faces;
    for (int center=0; center<V; ++center) {
        uint32_t ball=0;
        for (int v=0; v<V; ++v)
            if (__builtin_popcount(static_cast<unsigned>(center^v))<=radius)
                ball |= uint32_t(1)<<v;
        assert(__builtin_popcount(ball)==16);
        for (uint32_t f=ball; f; f=(f-1)&ball) faces.push_back(f);
    }
    sort(faces.begin(),faces.end());
    faces.erase(unique(faces.begin(),faces.end()),faces.end());
    const size_t M=faces.size();
    unordered_map<uint32_t,int> index;
    index.reserve(M*2);
    for (int i=0;i<(int)M;++i) index.emplace(faces[i],i);
    assert(index.size()==M);
    vector<int> mate(M,-1);
    vector<unsigned char> remaining(M,1);
    size_t pairs=0;
    for (int v=0; v<V; ++v) {
        const uint32_t bit=uint32_t(1)<<v;
        for (int i=0;i<(int)M;++i) {
            if (!remaining[i] || (faces[i]&bit)) continue;
            auto it=index.find(faces[i]|bit);
            if (it==index.end()) continue;
            const int j=it->second;
            if (!remaining[j]) continue;
            assert(i!=j && mate[i]<0 && mate[j]<0);
            assert(faces[j] == (faces[i]|bit));
            assert(__builtin_popcount(faces[j])==__builtin_popcount(faces[i])+1);
            mate[i]=j; mate[j]=i;
            remaining[i]=remaining[j]=0;
            ++pairs;
        }
    }
    size_t critical=0;
    map<int,size_t> critical_counts, face_counts;
    for (int i=0;i<(int)M;++i) {
        face_counts[__builtin_popcount(faces[i])-1]++;
        if (remaining[i]) {
            assert(mate[i]==-1);
            critical_counts[__builtin_popcount(faces[i])-1]++;
            ++critical;
        } else {
            assert(mate[i]>=0 && mate[mate[i]]==i);
        }
    }
    assert(2*pairs+critical==M);
    vector<int> indegree(M,0);
    size_t covers=0;
    for (int i=0;i<(int)M;++i) {
        const uint32_t face=faces[i];
        for (uint32_t bits=face; bits; bits&=bits-1) {
            const uint32_t bit=bits&-bits, lower=face^bit;
            if (!lower) continue;
            const int j=index.at(lower);
            ++covers;
            // Reverse the cover edge only when this is its matched pair.
            if (mate[j]==i) ++indegree[i];
            else ++indegree[j];
        }
    }
    deque<int> todo;
    for (int i=0;i<(int)M;++i) if (!indegree[i]) todo.push_back(i);
    size_t visited=0;
    while (!todo.empty()) {
        const int i=todo.front(); todo.pop_front(); ++visited;
        const uint32_t face=faces[i];
        if (mate[i]>=0 && __builtin_popcount(faces[mate[i]])==__builtin_popcount(face)+1) {
            if (--indegree[mate[i]]==0) todo.push_back(mate[i]);
        }
        for (uint32_t bits=face; bits; bits&=bits-1) {
            const uint32_t lower=face^(bits&-bits);
            if (!lower) continue;
            const int j=index.at(lower);
            if (mate[j]!=i && --indegree[j]==0) todo.push_back(j);
        }
    }
    long long reduced_euler=-1;
    for (auto [dimension,number]:face_counts)
        reduced_euler+=(dimension%2?-1:1)*static_cast<long long>(number);
    cout << "faces=" << M << " pairs=" << pairs << " critical=" << critical
         << " covers=" << covers << " visited=" << visited
         << " acyclic=" << (visited==M) << '\n';
    cout << "critical_dimensions";
    for (auto [dimension,number]:critical_counts) cout << ' ' << dimension << ':' << number;
    cout << '\n';
    cout << "f_vector";
    for (auto [dimension,number]:face_counts) cout << ' ' << dimension << ':' << number;
    cout << '\n';
    cout << "reduced_euler=" << reduced_euler << '\n';
    assert(M==1910200 && pairs==955064 && critical==72);
    assert(covers==15768064 && visited==M && reduced_euler==71);
    assert(critical_counts.size()==3 && critical_counts[0]==1 && critical_counts[4]==11 && critical_counts[6]==60);
    cout << "VERIFIED\n";
}
