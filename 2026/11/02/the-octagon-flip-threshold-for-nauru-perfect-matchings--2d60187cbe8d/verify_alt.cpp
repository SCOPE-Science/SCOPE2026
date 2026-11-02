// Exact independent pair-difference verification for perfect matchings of GP(12,5).
// Uses integer masks and compares every unordered pair; does not enumerate graph cycles.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
constexpr int N=24;
using U64=uint64_t;
vector<pair<int,int>> es;
array<vector<int>,N> incidence;
vector<U64> mats;
void enumerate(U64 covered,U64 chosen){
    if(covered==((1ULL<<N)-1)) {mats.push_back(chosen);return;}
    int v=0;
    while(covered&(1ULL<<v))++v;
    for(int eid:incidence[v]){
        auto [a,b]=es[eid];int w=a==v?b:a;
        if(!(covered&(1ULL<<w)))
            enumerate(covered | (1ULL<<v) | (1ULL<<w),chosen|(1ULL<<eid));
    }
}
bool one_alternating_cycle(U64 difference,int expected){
    if(__builtin_popcountll(difference)!=expected)return false;
    array<vector<int>,N> nbr;
    vector<int> occupied;
    for(int ei=0;ei<(int)es.size();ei++) if((difference>>ei)&1){
        auto [a,b]=es[ei]; nbr[a].push_back(b);nbr[b].push_back(a);
    }
    for(int v=0;v<N;v++){
        if(nbr[v].size()!=0 && nbr[v].size()!=2)return false;
        if(nbr[v].size()==2)occupied.push_back(v);
    }
    if((int)occupied.size()!=expected)return false;
    int count=0;array<bool,N> seen{}; queue<int> q;
    q.push(occupied[0]);seen[occupied[0]]=true;
    while(!q.empty()){
        int v=q.front();q.pop();++count;
        for(int w:nbr[v])if(!seen[w]){seen[w]=true;q.push(w);}
    }
    return count==expected;
}
vector<vector<int>> build(int length){
    vector<vector<int>> adj(mats.size());
    for(int i=0;i<(int)mats.size();i++)for(int j=i+1;j<(int)mats.size();j++){
        if(one_alternating_cycle(mats[i]^mats[j],length)){
            adj[i].push_back(j);adj[j].push_back(i);
        }
    }
    return adj;
}
map<int,int> components(const vector<vector<int>>& adj){
    vector<char> seen(adj.size());map<int,int> cc;
    for(int root=0;root<(int)adj.size();root++)if(!seen[root]){
        queue<int> q;q.push(root);seen[root]=true;int size=0;
        while(!q.empty()){
            int u=q.front();q.pop();size++;
            for(int v:adj[u])if(!seen[v]){seen[v]=true;q.push(v);}
        }
        cc[size]++;
    }return cc;
}
map<int,int> eccentricities(const vector<vector<int>>& adj){
    map<int,int> ecc;
    for(int root=0;root<(int)adj.size();root++){
        vector<int> dist(adj.size(),-1);queue<int> q;
        q.push(root);dist[root]=0;
        while(!q.empty()){
            int u=q.front();q.pop();
            for(int v:adj[u])if(dist[v]==-1){dist[v]=dist[u]+1;q.push(v);}
        }
        assert(find(dist.begin(),dist.end(),-1)==dist.end());
        ecc[*max_element(dist.begin(),dist.end())]++;
    }return ecc;
}
int main(){
    set<pair<int,int>> e;
    for(int i=0;i<12;i++){
        for(auto [a,b]:vector<pair<int,int>>{{i,(i+1)%12},{i,12+i},{12+i,12+(i+5)%12}})
            e.insert(minmax(a,b));
    }
    assert(e.size()==36);
    es.assign(e.begin(),e.end());
    for(int id=0;id<(int)es.size();id++){
        auto [a,b]=es[id];incidence[a].push_back(id);incidence[b].push_back(id);
    }
    for(int v=0;v<N;v++)assert(incidence[v].size()==3);
    enumerate(0,0);sort(mats.begin(),mats.end());
    assert(unique(mats.begin(),mats.end())==mats.end() && mats.size()==120);
    cout<<"INDEPENDENT_MATCHINGS_OK count="<<mats.size()<<"\n";
    for(int length:{4,6,8}){
        auto adj=build(length);
        auto cc=components(adj);
        long edges=accumulate(adj.begin(),adj.end(),0L,[](long a,const vector<int>& b){return a+b.size();})/2;
        cout<<"INDEPENDENT_FLIP_OK cycle="<<length<<" edges="<<edges<<" components=";
        for(auto [size,multiple]:cc)cout<<" "<<size<<":"<<multiple;
        cout<<"\n";
        if(length==4){assert(edges==0 && cc.size()==1 && cc.at(1)==120);}
        else if(length==6){assert((edges==192 && cc==map<int,int>({{1,9},{18,3},{57,1}})));}
        else{
            assert((edges==414 && cc==map<int,int>({{120,1}})));
            auto ec=eccentricities(adj);
            assert((ec==map<int,int>({{4,72},{5,42},{6,6}})));
            cout<<"INDEPENDENT_DISTANCE_OK radius="<<ec.begin()->first<<" diameter="<<ec.rbegin()->first<<" ecc4="<<ec[4]<<" ecc5="<<ec[5]<<" ecc6="<<ec[6]<<"\n";
        }
    }
    cout<<"INDEPENDENT_VERIFY_OK\n";
}
