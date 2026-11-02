// Independent integer-indexed, bottom-up EF-signature computation.
// Graphs are the squares of undirected simple cycles C_n, n >= 3.
// Compile: c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using Vec = vector<int>;

vector<vector<int>> type_groups(int q, int limit) {
    vector<map<Vec,int>> dictionary(q+1);
    map<int,Vec> groups;
    for (int n=3; n<=limit; ++n) {
        int count=1;
        for(int k=0;k<q;++k)count*=n;
        Vec layer(count);
        for(int index=0;index<count;++index){
            Vec x(q); int z=index;
            for(int k=q-1;k>=0;--k){x[k]=z%n; z/=n;}
            Vec atom;
            for(int i=0;i<q;++i)for(int j=i+1;j<q;++j){
                int d=abs(x[i]-x[j]); d=min(d,n-d);
                atom.push_back(d==0?0:(d<=2?1:2));
            }
            auto &T=dictionary[0];
            auto p=T.find(atom);
            if(p==T.end())p=T.emplace(atom,(int)T.size()).first;
            layer[index]=p->second;
        }
        for(int r=1;r<=q;++r){
            Vec next(count/n);
            for(int i=0;i<(int)next.size();++i){
                Vec extension;
                for(int j=0;j<n;++j)extension.push_back(layer[i*n+j]);
                sort(extension.begin(),extension.end());
                extension.erase(unique(extension.begin(),extension.end()),extension.end());
                auto &T=dictionary[r];
                auto p=T.find(extension);
                if(p==T.end())p=T.emplace(extension,(int)T.size()).first;
                next[i]=p->second;
            }
            layer.swap(next);
            count/=n;
        }
        groups[layer.at(0)].push_back(n);
    }
    vector<Vec> result;
    for(auto &p:groups)result.push_back(p.second);
    sort(result.begin(),result.end());
    return result;
}
int main(){
    auto got=type_groups(4,24);
    vector<Vec> expected={{3},{4,5}};
    for(int n=6;n<=18;++n)expected.push_back({n});
    expected.push_back({19,20,21,22,23,24});
    assert(got==expected);
    cout<<"INDEPENDENT_INTEGER_INDEX_RANK4_PASS classes="<<got.size()<<" cutoff=19\n";
    got=type_groups(3,24);
    expected={{3,4,5}};
    for(int n=6;n<=10;++n)expected.push_back({n});
    expected.push_back({11,12,13,14,15,16,17,18,19,20,21,22,23,24});
    assert(got==expected);
    cout<<"INDEPENDENT_INTEGER_INDEX_RANK3_PASS classes="<<got.size()<<" cutoff=11\n";
}
