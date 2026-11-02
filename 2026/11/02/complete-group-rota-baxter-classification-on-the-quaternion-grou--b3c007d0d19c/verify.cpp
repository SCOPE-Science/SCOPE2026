// Exhaustive independent check of the group Rota--Baxter classification on Q8.
// Build: g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
// Run:   ./verify
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
using Map = array<int,8>;
int mul[8][8], inv[8];
void require(bool c, const char* msg) { if (!c) throw runtime_error(msg); }
void setup() {
    // Element 2*b+s represents (-1)^s times 1,i,j,k for b=0,1,2,3.
    const int basis[4][4] = {{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
    const int neg[4][4] = {{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
    for (int a=0;a<8;++a) for(int b=0;b<8;++b)
        mul[a][b] = 2*basis[a/2][b/2] + ((a&1)^(b&1)^neg[a/2][b/2]);
    for (int a=0;a<8;++a) {
        int n=0;
        for (int b=0;b<8;++b) if(mul[a][b]==0 && mul[b][a]==0) {inv[a]=b;++n;}
        require(n==1, "inverse not unique");
    }
    for(int a=0;a<8;++a) for(int b=0;b<8;++b) for(int c=0;c<8;++c)
        require(mul[mul[a][b]][c]==mul[a][mul[b][c]], "not associative");
}
int main() {
    try {
        setup();
        set<Map> predicted;
        for(int a=0;a<2;++a) for(int b=0;b<2;++b) {
            Map chi{}, twisted{};
            for(int x=0;x<8;++x) {
                int parity= (x/2==1 ? a : x/2==2 ? b : x/2==3 ? a^b : 0);
                chi[x]=parity; // 0=1, 1=-1
                twisted[x]=mul[inv[x]][chi[x]];
            }
            predicted.insert(chi); predicted.insert(twisted);
        }
        require(predicted.size()==8,"predicted family not eight distinct maps");
        set<Map> observed;
        constexpr int candidate_count=2097152; // 8^(|Q8|-1), B(1)=1.
        for(int code=0;code<candidate_count;++code) {
            int z=code;
            Map B{};
            B[0]=0;
            for(int x=1;x<8;++x){B[x]=z%8;z/=8;}
            bool ok=true;
            for(int g=0;g<8 && ok;++g) for(int h=0;h<8;++h) {
                const int left=mul[B[g]][B[h]];
                const int arg=mul[mul[mul[g][B[g]]][h]][inv[B[g]]];
                if(left!=B[arg]) {ok=false;break;}
            }
            if(ok)observed.insert(B);
        }
        require(observed==predicted,"exhaustive solution set differs from formula");
        map<int,int> ranks;
        for(const auto& B:observed) {
            set<int> image(B.begin(),B.end());
            ++ranks[image.size()];
        }
        require(ranks==map<int,int>({{1,1},{2,3},{8,4}}),"image-size distribution differs");
        // Every automorphism is specified by images of i,j of order four that do not commute.
        vector<Map> aut;
        for(int i=2;i<8;++i) for(int j=2;j<8;++j) {
            if(mul[i][j]==mul[j][i]) continue;
            Map A{};
            A[0]=0;A[1]=1;A[2]=i;A[3]=i^1;A[4]=j;A[5]=j^1;
            A[6]=mul[i][j];A[7]=A[6]^1;
            bool good=true;
            for(int x=0;x<8;++x) for(int y=0;y<8;++y)
                if(A[mul[x][y]]!=mul[A[x]][A[y]]) good=false;
            if(good)aut.push_back(A);
        }
        require(aut.size()==24,"automorphism group does not have order 24");
        set<Map> unclassified=observed;
        map<int,int> orbits;
        while(!unclassified.empty()) {
            const Map B=*unclassified.begin();
            set<Map> orbit;
            for(const auto& A:aut) {
                Map Ai{}, C{};
                for(int x=0;x<8;++x)Ai[A[x]]=x;
                for(int x=0;x<8;++x)C[x]=Ai[B[A[x]]];
                orbit.insert(C);
            }
            for(const auto& C:orbit) require(unclassified.erase(C)==1,"orbit escaped solutions");
            ++orbits[orbit.size()];
        }
        require(orbits==map<int,int>({{1,2},{3,2}}),"wrong automorphism orbit distribution");
        // Dual under the explicit convention B~(g)=g^{-1}B(g^{-1}).
        for(const auto& B:observed) {
            Map dual{};
            for(int g=0;g<8;++g)dual[g]=mul[inv[g]][B[inv[g]]];
            require(observed.count(dual)==1,"dual does not belong to classification");
            set<int> imB(B.begin(),B.end()), imD(dual.begin(),dual.end());
            require(! (imB.size()==8 && imD.size()==8),"mutual bijectivity counterexample");
        }
        cout << "VERIFY_OK candidates=2097152 operators=8 images=1:1,2:3,8:4 ";
        cout << "aut=24 orbit_sizes=1:2,3:2 dual=checked\n";
    } catch(const exception& e){cerr<<"VERIFY_FAILED: "<<e.what()<<"\n";return 1;}
}
