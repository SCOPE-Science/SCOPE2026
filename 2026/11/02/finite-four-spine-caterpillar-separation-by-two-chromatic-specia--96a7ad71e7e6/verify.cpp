// Deterministic finite separation for fourth chromatic principal specializations.
// Compile: g++ -std=c++17 -O3 verify.cpp -o verify
// Run: ./verify 200
// uint64_t arithmetic is exact arithmetic in Z/(2^64), not a random hash.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <tuple>
#include <unordered_map>
using U = std::uint64_t;
struct Signature {
    U q2, q3;
    bool operator==(const Signature &other) const {
        return q2==other.q2 && q3==other.q3;
    }
};
struct SignatureHash {
    std::size_t operator()(const Signature &x) const {
        U v = x.q2 ^ (x.q3 + 0x9e3779b97f4a7c15ULL + (x.q2<<6) + (x.q2>>2));
        v ^= v >> 33; v *= 0xff51afd7ed558ccdULL; v ^= v >> 33;
        return static_cast<std::size_t>(v);
    }
};
static U weight[2][4][201];
void initialize(int N) {
    for (int h=0;h<2;h++) {
        U z = h==0 ? U(2) : U(3);
        U zpower[4]={1,z,z*z,z*z*z};
        for (int color=0;color<4;color++) {
            U leafsum=0;
            for (int other=0;other<4;other++) if (other!=color) leafsum += zpower[other];
            U p=1;
            for (int s=1;s<=N;s++) { weight[h][color][s]=zpower[color]*p; p*=leafsum; }
        }
    }
}
U evaluate(int h, int a, int b, int c, int d) {
    U state[4];
    for (int j=0;j<4;j++) state[j]=weight[h][j][a];
    int sizes[3]={b,c,d};
    for (int s:sizes) {
        U total=state[0]+state[1]+state[2]+state[3];
        // In-place update is safe: the new state[j] uses only old total and old state[j].
        for (int j=0;j<4;j++) state[j]=weight[h][j][s]*(total-state[j]);
    }
    return state[0]+state[1]+state[2]+state[3];
}
int main(int argc,char **argv) {
    int limit=argc>1?std::atoi(argv[1]):200;
    if (limit<6 || limit>200) return 2;
    initialize(limit);
    U count=0;
    for (int n=6;n<=limit;n++) {
        std::unordered_map<Signature,std::array<int,4>,SignatureHash> seen;
        for (int a=2;a<=n-4;a++)
          for (int b=1;b<=n-a-3;b++)
            for (int c=1;c<=n-a-b-2;c++) {
                int d=n-a-b-c;
                if (d<2) continue;
                if (std::make_tuple(a,b,c,d)>std::make_tuple(d,c,b,a)) continue;
                Signature key{evaluate(0,a,b,c,d),evaluate(1,a,b,c,d)};
                auto ret=seen.emplace(key,std::array<int,4>{a,b,c,d});
                if (!ret.second) {
                    auto prior=ret.first->second;
                    std::cerr << "COLLISION order="<<n<<" types=("<<a<<","<<b<<","<<c<<","<<d
                              <<") and ("<<prior[0]<<","<<prior[1]<<","<<prior[2]<<","<<prior[3]<<")\n";
                    return 1;
                }
                ++count;
            }
        if (n%10==0) std::cerr << "CHECKED order="<<n<<" accumulated_classes="<<count<<"\n";
    }
    std::cout << "RESULT N<="<<limit<<" CLASSES="<<count<<" COLLISIONS=0\n";
    if (limit==200 && count!=31060953ULL) return 3;
    return 0;
}
