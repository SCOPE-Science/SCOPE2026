// Exhaustive coefficient certificate for a prescribed six-point cubic branch divisor over F_7.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
using namespace std;
int mod7(int x) { x %= 7; return x < 0 ? x + 7 : x; }
using Quad = array<int,3>;
using Cubic = array<int,4>;
using Solution = tuple<Quad,Cubic,int>;
int main() {
    set<Solution> solutions;
    for (int u = 0; u < 343; ++u) {
        Quad a = {u%7,(u/7)%7,(u/49)%7};
        int square[5]={}, cube[7]={};
        for(int i=0;i<3;i++)for(int j=0;j<3;j++) square[i+j]+=a[i]*a[j];
        for(int i=0;i<5;i++)for(int j=0;j<3;j++) cube[i+j]+=square[i]*a[j];
        for (int v = 0; v < 2401; ++v) {
            Cubic b={v%7,(v/7)%7,(v/49)%7,(v/343)%7};
            int d[7]; for(int i=0;i<7;i++)d[i]=mod7(3*cube[i]);
            for(int i=0;i<4;i++)for(int j=0;j<4;j++) d[i+j]=mod7(d[i+j]+b[i]*b[j]);
            if (d[0]==0 || d[6]!=mod7(-d[0])) continue;
            bool ok=true;
            for(int i=1;i<6;i++)if(d[i]!=0)ok=false;
            if(ok)solutions.insert({a,b,d[0]});
        }
    }
    assert(solutions.size()==12);
    int counts[7]={};
    for(const auto& s: solutions) {
        const auto& [a,b,k]=s;
        counts[k]++;
        if(k==3) {
            assert(a[1]==0 && a[2]==0 && b[0]==0 && b[1]==0 && b[2]==0);
            assert((a[0]==1 || a[0]==2 || a[0]==4) && (b[3]==2 || b[3]==5));
        } else if(k==4) {
            assert(a[0]==0 && a[1]==0 && b[1]==0 && b[2]==0 && b[3]==0);
            assert((a[2]==1 || a[2]==2 || a[2]==4) && (b[0]==2 || b[0]==5));
        } else assert(false);
    }
    assert(counts[3]==6 && counts[4]==6);
    // The six k=3 solutions form one orbit under z -> s*z, s in F_7^*.
    set<Solution> orbit;
    for(int s=1;s<7;s++) {
        int s2=mod7(s*s), s3=mod7(s2*s);
        int inv2=0,inv3=0;
        for(int x=1;x<7;x++) { if(mod7(x*s2)==1)inv2=x; if(mod7(x*s3)==1)inv3=x; }
        orbit.insert({Quad{inv2,0,0},Cubic{0,0,0,mod7(2*inv3)},3});
    }
    assert(orbit.size()==6);
    for(const auto& s: orbit)assert(solutions.count(s)==1);
    // Interchanging x,y identifies the other six solutions up to target automorphism.
    for(const auto& sol: orbit) {
        auto [a,b,k]=sol;
        assert(solutions.count({Quad{a[2],a[1],a[0]}, Cubic{b[3],b[2],b[1],b[0]},4})==1);
    }
    int rational_points=0;
    for(int x=0;x<7;x++)for(int z=0;z<7;z++)
        if(mod7(z*z*z + x*x*z +2)==0) rational_points++;
    for(int z=0;z<7;z++)
        if(mod7(z*z*z+z)==0)rational_points++;
    assert(rational_points==13);
    cout << "VERIFY_OK 823543 coefficients, 12 models, 2 fixed-base classes, 1 unmarked class; points=13\n";
}
