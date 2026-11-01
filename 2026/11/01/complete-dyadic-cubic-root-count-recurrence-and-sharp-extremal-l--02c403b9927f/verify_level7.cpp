// Exhaustive, independent binary-cubic root census modulo 128.
// Compile: c++ -O2 -std=c++17 verify_level7.cpp -o verify_level7
#include <array>
#include <cstdint>
#include <cstdio>
int main() {
    constexpr int modulus = 128;
    constexpr int mask = modulus - 1;
    std::array<std::uint64_t, modulus + 1> histogram{};
    std::array<int, modulus> cubes{}, squares{};
    for (int x=0; x<modulus; ++x) {
        cubes[x] = (x*x*x)&mask;
        squares[x] = (x*x)&mask;
    }
    for (int a=0; a<modulus; ++a)
      for (int b=0; b<modulus; ++b)
        for (int c=0; c<modulus; ++c) {
            int roots = 0;
            for (int x=0; x<modulus; ++x)
                roots += (((cubes[x] + a*squares[x] + b*x + c)&mask)==0);
            ++histogram[roots];
        }
    std::array<std::uint64_t, modulus + 1> expected{};
    expected[0]=879104; expected[1]=954368; expected[2]=131072;
    expected[4]=28672; expected[5]=65536; expected[8]=4096;
    expected[9]=24576; expected[16]=1024; expected[17]=4096;
    expected[20]=4096; expected[32]=512;
    if (histogram != expected) return 1;
    std::puts("VERIFY_OK modulus=128 cubics=2097152 max_roots=32 extremizers=512 exact_integer=yes");
    return 0;
}
