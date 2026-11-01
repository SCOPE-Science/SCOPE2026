// Direct, labelled-vertex verification of majority dynamics on clique-plus-leaf graphs.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

static uint64_t binom(int n,int k){
    if(k<0 || k>n) return 0;
    uint64_t v=1;
    for(int i=1;i<=k;i++) v=v*(n-i+1)/i;
    return v;
}

static uint64_t update(int r,uint64_t x){
    const int n=r+2; // hub=vertex 0, nonhubs=1..r, leaf=r+1.
    uint64_t y=0;
    for(int u=0;u<n;u++){
        int ones=0,deg=0;
        for(int v=0;v<n;v++){
            bool adjacent=(u!=v && u<=r && v<=r) ||
                (u==0 && v==r+1) || (u==r+1 && v==0);
            if(adjacent){ones+=(x>>v)&1ULL;deg++;}
        }
        bool result = (2*ones>deg) || (2*ones==deg && ((x>>u)&1ULL));
        if(result) y|=(1ULL<<u);
    }
    return y;
}

static pair<int,int> first_entry(int r,uint64_t x){
    map<uint64_t,int> seen;
    for(int t=0;t<12;t++){
        if(seen.count(x)) return {seen[x],t-seen[x]};
        seen[x]=t;
        x=update(r,x);
    }
    assert(false);return {-1,-1};
}

int main(){
    uint64_t checked=0;
    for(int r=2;r<=16;r++){
        map<pair<int,int>,uint64_t> count;
        uint64_t states=uint64_t(1)<<(r+2);
        for(uint64_t x=0;x<states;x++){
            count[first_entry(r,x)]++;
            checked++;
        }
        uint64_t mid=binom(r,r/2);
        assert(count[make_pair(0,1)]==2);
        assert(count[make_pair(1,1)]==(uint64_t(1)<<(r+1))-2);
        assert(count[make_pair(2,1)]==(uint64_t(1)<<(r+1))-2*mid);
        if(r%2==0){
            assert(count[make_pair(3,1)]==2*mid);
            assert(count.size()==4);
        }else{
            assert(count[make_pair(0,2)]==2*mid);
            assert(count.size()==4);
        }
        cout<<"r="<<r<<" full_states="<<states<<" first_entry_classes="<<count.size()<<" OK\n";
    }
    cout<<"FULL_OK labelled_initial_states="<<checked<<" r_range=2..16\n";
}
