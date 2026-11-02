// Independent exhaustive enumeration of all ten-factorial exponent permutations.
#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
using namespace std;
int main() {
    const int n=10;
    array<int,n> permutation;
    iota(permutation.begin(),permutation.end(),1);
    int residues[n+1][n+1] = {};
    for(int i=1;i<=n;i++)for(int e=1;e<=n;e++) {
        int power=1;
        for(int j=0;j<e;j++)power=(power*i)%n;
        residues[i][e]=power;
    }
    array<long long,n+1> histogram = {};
    do {
        unsigned mask=0;
        for(int i=1;i<=n;i++) mask|=1u<<residues[i][permutation[i-1]];
        histogram[__builtin_popcount(mask)]++;
    } while(next_permutation(permutation.begin(),permutation.end()));
    const array<long long,n+1> expected={0,0,0,0,0,9792,537408,1822464,1175040,84096,0};
    if(histogram!=expected) return 1;
    for(int j=0;j<=n;j++)if(histogram[j])cout<<j<<":"<<histogram[j]<<" ";
    cout<<"VERIFY_OK\n";
}
