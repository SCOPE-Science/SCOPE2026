// Exact finite census of the Pythagorean-leg graph on the fifth prime box.
// Compile: g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
using i64 = long long;
using i128 = __int128_t;
static bool square_sum(i64 x, i64 y) {
    const i128 s = (i128)x*x + (i128)y*y;
    i64 r = (i64)sqrtl((long double)s);
    while ((i128)r*r < s) ++r;
    while ((i128)r*r > s) --r;
    return (i128)r*r == s;
}
int main() {
    vector<i64> vals;
    for(i64 a=1, i=0; i<5; ++i,a*=2)
    for(i64 b=1, j=0; j<5; ++j,b*=3)
    for(i64 c=1, k=0; k<5; ++k,c*=5)
    for(i64 d=1, l=0; l<5; ++l,d*=7)
    for(i64 e=1, m=0; m<5; ++m,e*=11)
        vals.push_back(a*b*c*d*e);
    sort(vals.begin(), vals.end());
    if (vals.size() != 3125 || adjacent_find(vals.begin(),vals.end()) != vals.end())
        throw runtime_error("vertex generation failed");
    const int n=(int)vals.size();
    vector<vector<unsigned char>> adjacency(n,vector<unsigned char>(n,0));
    i64 edges=0;
    for(int i=0;i<n;++i) for(int j=i+1;j<n;++j) {
        if(square_sum(vals[i],vals[j])) {
            adjacency[i][j]=adjacency[j][i]=1;
            ++edges;
        }
    }
    map<array<i64,3>,i64> types;
    vector<array<i64,3>> triangle_list;
    i64 triangles=0;
    for(int i=0;i<n;++i) for(int j=i+1;j<n;++j) if(adjacency[i][j])
      for(int k=j+1;k<n;++k) if(adjacency[i][k] && adjacency[j][k]) {
        i64 g=gcd(gcd(vals[i],vals[j]),vals[k]);
        ++types[{vals[i]/g,vals[j]/g,vals[k]/g}];
        triangle_list.push_back({vals[i],vals[j],vals[k]});
        ++triangles;
    }
    const map<array<i64,3>,i64> expected={{{240,252,275},144},{{1008,1100,1155},144}};
    if(edges!=14856 || triangles!=288 || types!=expected)
        throw runtime_error("triangle census did not match the theorem");
    // Independently count intersections of every pair of canonical triangles.
    vector<int> degree(triangles,0);
    int shared_one=0, shared_two=0;
    for (int i=0;i<triangles;++i) for(int j=i+1;j<triangles;++j) {
        int common=0;
        for(i64 a:triangle_list[i]) for(i64 b:triangle_list[j])
            if(a==b)++common;
        if(common) {
            ++degree[i]; ++degree[j];
            if(common==1)++shared_one;
            else if(common==2)++shared_two;
            else throw runtime_error("duplicate triangle");
        }
    }
    int isolated=count(degree.begin(),degree.end(),0);
    int degree_one=count(degree.begin(),degree.end(),1);
    if(isolated!=174 || degree_one!=114 || isolated+degree_one!=triangles
       || shared_one!=9 || shared_two!=48)
        throw runtime_error("triangle intersection verification failed");
    cout<<"VERIFIED vertices="<<n<<" edges="<<edges
        <<" triangles="<<triangles<<" primitive_types="<<types.size()
        <<" isolated="<<isolated<<" overlap_pairs="<<(shared_one+shared_two)
        <<" packing="<<(isolated+shared_one+shared_two)<<"\n";
}
