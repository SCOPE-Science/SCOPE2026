// Exhaustive exact finite verification for limited domination on Q4 and Q5.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <queue>
#include <stdexcept>
#include <unordered_set>
#include <vector>
using namespace std;
using U = uint64_t;
static inline int pc(U x) { return __builtin_popcountll(x); }
static U transform(U x, int d, int axis, bool is_flip) {
    U out=0;
    for (int i=0;i<(1<<d);++i) if ((x>>i)&1ULL) {
        int j;
        if (is_flip) j=i^(1<<axis);
        else {
            int a=(i>>axis)&1, b=(i>>(axis+1))&1;
            j=(i&~((1<<axis)|(1<<(axis+1))))|(a<<(axis+1))|(b<<axis);
        }
        out|=U(1)<<j;
    }
    return out;
}
static vector<pair<U,int>> orbit_profile(const vector<U>& minima,int d) {
    unordered_set<U> unseen(minima.begin(),minima.end());
    if (unseen.size()!=minima.size()) throw runtime_error("duplicate minima");
    vector<pair<U,int>> orbits;
    while(!unseen.empty()) {
        U seed=*unseen.begin();
        queue<U> q;q.push(seed);unseen.erase(seed);
        int count=0;U least=seed;
        while(!q.empty()) {
            U a=q.front();q.pop();count++;least=min(least,a);
            for (int ax=0;ax<d;++ax) {
                U b=transform(a,d,ax,true);
                auto it=unseen.find(b);
                if(it!=unseen.end()) {unseen.erase(it);q.push(b);}
                else if(find(minima.begin(),minima.end(),b)==minima.end()) throw runtime_error("flip left minimizer family");
            }
            for (int ax=0;ax<d-1;++ax) {
                U b=transform(a,d,ax,false);
                auto it=unseen.find(b);
                if(it!=unseen.end()) {unseen.erase(it);q.push(b);}
                else if(find(minima.begin(),minima.end(),b)==minima.end()) throw runtime_error("swap left minimizer family");
            }
        }
        orbits.push_back({least,count});
    }
    sort(orbits.begin(),orbits.end(),[](auto a,auto b){return a.second<b.second ||(a.second==b.second&&a.first<b.first);});
    return orbits;
}
static bool direct_check(U selected,int d,int k) {
    for(int u=0;u<(1<<d);++u) {
        int inside=0;
        for(int b=0;b<d;++b) inside+=int((selected>>(u^(1<<b)))&1ULL);
        if((selected>>u)&1ULL) {if(d-inside>k) return false;}
        else if(inside==0) return false;
    }
    return true;
}
struct Layer {uint16_t selected, required;uint8_t size;};
int main() {
    vector<U> opt4,opt5;
    int best4=17;
    for (unsigned a=0;a<65536;++a) {
        if (!direct_check(a,4,2)) continue;
        int z=pc(a);
        if(z<best4){best4=z;opt4.clear();}
        if(z==best4)opt4.push_back(a);
    }
    if(best4!=8 || opt4.size()!=428) throw runtime_error("Q4 result mismatch");
    printf("Q4_EXHAUSTIVE %d %zu SUBSETS_CHECKED 65536\n",best4,opt4.size());
    uint16_t adj[16]={};
    for(int u=0;u<16;++u) for(int b=0;b<4;++b) adj[u]|=uint16_t(1)<<(u^(1<<b));
    vector<Layer> layers;
    for(unsigned a=0;a<65536;++a) {
        unsigned req=0;bool feasible=true;
        for(int u=0;u<16;++u) {
            int inside=pc(a&adj[u]);
            if((a>>u)&1U) {
                if(inside<2){feasible=false;break;}
                if(inside==2)req|=1U<<u;
            } else if(inside==0) req|=1U<<u;
        }
        if(feasible)layers.push_back({uint16_t(a),uint16_t(req),uint8_t(pc(a))});
    }
    if(layers.size()!=8122) throw runtime_error("layer count mismatch");
    int best5=33; U solutions=0;
    U tested=0;
    // No early stopping: each ordered pair of feasible layer masks is processed.
    for(const Layer& a:layers) for(const Layer& b:layers) {
        ++tested;
        if((b.selected&a.required)!=a.required ||
           (a.selected&b.required)!=b.required) continue;
        int z=a.size+b.size;
        if(z<best5){best5=z;opt5.clear();}
        if(z==best5)opt5.push_back(U(a.selected)|(U(b.selected)<<16));
        ++solutions;
    }
    if(tested!=U(8122)*8122 || best5!=16 || opt5.size()!=1830)
       throw runtime_error("Q5 exhaustive layer enumeration mismatch");
    for(U a:opt5) if(!direct_check(a,5,2)||pc(a)!=16)
       throw runtime_error("original Q5 graph check failed");
    printf("Q5_EXHAUSTIVE %d %zu ADMISSIBLE_LAYERS %zu ORDERED_PAIRS %llu\n",
        best5,opt5.size(),layers.size(),(unsigned long long)tested);
    for(int d=4;d<=5;++d) {
        auto orbits=orbit_profile(d==4?opt4:opt5,d);
        if(orbits.size()!=6) throw runtime_error("expected six orbits");
        int target=(d==4?428:1830),sum=0;
        printf("Q%d_SIX_AUTOMORPHISM_ORBITS",d);
        for(auto [rep,size]:orbits){sum+=size;printf(" %d:%llu",size,(unsigned long long)rep);}
        printf("\n");
        if(sum!=target)throw runtime_error("orbit size sum mismatch");
    }
    puts("VERIFY_OK");
}
