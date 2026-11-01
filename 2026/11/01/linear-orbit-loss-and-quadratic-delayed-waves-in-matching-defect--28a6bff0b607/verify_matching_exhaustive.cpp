// Independent full-state enumerator for synchronous three-color cyclic automata.
// Standard C++17; no third-party dependencies.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

using State = vector<unsigned char>;
State evolve(const State& x, int k) {
    const int n=(int)x.size(); State y=x;
    for (int v=0;v<n;++v){
        const int successor=(x[v]+1)%3;
        bool contact=false;
        for(int w=0;w<n;++w){
            if(w==v || (v<2*k && w==(v^1))) continue;
            if(x[w]==successor){contact=true;break;}
        }
        if(contact) y[v]=(unsigned char)successor;
    }
    return y;
}

array<uint64_t,6> expected(int n,int k){
    uint64_t pow2=1ULL<<n, pow3=1;
    for(int t=0;t<n;++t)pow3*=3;
    return {3, pow3-3*pow2+3-6ULL*k*((pow2>>2)-1),
            3*pow2-6-6ULL*k,6ULL*k*((pow2>>2)-2*k),
            12ULL*k,12ULL*k*(k-1)};
}
int main(){
    const array<pair<int,int>,6> labels={{{0,1},{0,3},{1,1},{1,3},{2,1},{2,3}}};
    uint64_t verified=0;int cases=0;
    for(int n=3;n<=11;++n){
        uint64_t total=1;for(int j=0;j<n;++j)total*=3;
        for(int k=0;k<=n/2;++k){
            if(n-k<3)continue;
            array<uint64_t,6> got{};
            for(uint64_t z=0;z<total;++z){
                uint64_t t=z;State state(n);
                for(int j=0;j<n;++j){state[j]=t%3;t/=3;}
                array<State,6> seq;
                seq[0]=state;
                for(int h=1;h<=5;++h)seq[h]=evolve(seq[h-1],k);
                if(seq[5]!=seq[2]){cerr<<"iterate identity failed "<<n<<" "<<k<<" "<<z<<"\n";return 1;}
                int d=-1;
                for(int h=0;h<=2;++h)if(seq[h]==seq[h+3]){d=h;break;}
                if(d<0){cerr<<"entry failure\n";return 2;}
                int period=seq[d]==seq[d+1]?1:3;
                int bin=-1;
                for(int j=0;j<6;++j)if(labels[j]==make_pair(d,period)){bin=j;break;}
                if(bin<0){cerr<<"unknown period\n";return 3;}
                ++got[bin];++verified;
            }
            if(got!=expected(n,k)){
                cerr<<"census mismatch n="<<n<<" k="<<k<<"\n";
                for(int j=0;j<6;++j)cerr<<got[j]<<" vs "<<expected(n,k)[j]<<"\n";
                return 4;
            }
            ++cases;
            cout<<"n="<<n<<" k="<<k<<" ";
            for(auto v:got)cout<<v<<" ";cout<<"\n";
        }
    }
    cout<<"EXHAUSTIVE_CENSUS_OK cases="<<cases<<" states="<<verified<<"\n";
}
