// Exhaustive 30-vertex enumeration and matching-pair comparison.
// g++ -std=c++17 -O2 independent.cpp -o independent && ./independent
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using E = pair<int,int>;
using M = vector<int>;
int main(){
    vector<E> d;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++) d.push_back({a,b});
    vector<array<E,3>> synthemes;
    auto canonical=[](array<E,3> a){for(auto &p:a) if(p.first>p.second)swap(p.first,p.second);sort(a.begin(),a.end());return a;};
    set<array<E,3>> distinct;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++) {
        vector<int> rest;for(int z=0;z<6;z++)if(z!=a&&z!=b)rest.push_back(z);
        for(int j=1;j<4;j++){
            vector<int> left;for(int k=1;k<4;k++)if(k!=j)left.push_back(rest[k]);
            distinct.insert(canonical({E{a,b},E{rest[0],rest[j]},E{left[0],left[1]}}));
        }
    }
    assert(distinct.size()==15);
    synthemes.assign(distinct.begin(),distinct.end());
    vector<E> edges;
    for(int i=0;i<15;i++)for(int j=0;j<15;j++)
        if(find(synthemes[j].begin(),synthemes[j].end(),d[i])!=synthemes[j].end())edges.push_back({i,15+j});
    assert(edges.size()==45);
    vector<vector<int>> incident(30);
    for(int e=0;e<45;e++){incident[edges[e].first].push_back(e);incident[edges[e].second].push_back(e);}
    for(auto &z:incident)assert(z.size()==3);
    vector<M> states;
    auto recurse=[&](auto&&self,unsigned used,M&chosen)->void{
        int first=-1;
        for(int z=0;z<30;z++)if(!(used&(1U<<z))){first=z;break;}
        if(first<0){states.push_back(chosen);return;}
        for(int e:incident[first]){
            auto [a,b]=edges[e];
            int other=(a==first?b:a);
            if(used&(1U<<other))continue;
            chosen.push_back(e);
            self(self,used|(1U<<first)|(1U<<other),chosen);
            chosen.pop_back();
        }
    };
    M chosen;
    recurse(recurse,0,chosen);
    for(auto &m:states)sort(m.begin(),m.end());
    sort(states.begin(),states.end());
    states.erase(unique(states.begin(),states.end()),states.end());
    assert(states.size()==288);
    vector<array<int,30>> chars;
    vector<vector<int>> graph(30);
    for(auto [a,b]:edges){graph[a].push_back(b);graph[b].push_back(a);}
    // Complementary cubic edge sets are spanning 2-regular graphs.
    vector<int> profile;map<vector<int>,int> classcount;
    for(const auto &m:states){
        vector<vector<int>> h(30);
        for(int ei=0;ei<45;ei++)if(!binary_search(m.begin(),m.end(),ei)){
            auto [a,b]=edges[ei];h[a].push_back(b);h[b].push_back(a);
        }
        for(auto &v:h)assert(v.size()==2);
        vector<char> seen(30);vector<int> ls;
        for(int root=0;root<30;root++)if(!seen[root]){
            queue<int>q;q.push(root);seen[root]=1;int k=0;
            while(!q.empty()){
                int x=q.front();q.pop();k++;
                for(int y:h[x])if(!seen[y]){seen[y]=1;q.push(y);}
            }
            ls.push_back(k);
        }
        sort(ls.begin(),ls.end());
        classcount[ls]++;
        profile.push_back(ls.size()==1?0:1);
    }
    assert(classcount[vector<int>({30})]==144);
    assert(classcount[vector<int>({10,20})]==144);
    assert(classcount.size()==2);
    // Compare every unordered pair, checking its symmetric difference is one eight-cycle.
    vector<vector<int>> jump(288);
    int flips=0,typed=0;
    for(int i=0;i<288;i++)for(int j=i+1;j<288;j++){
        vector<int> diff;
        set_symmetric_difference(states[i].begin(),states[i].end(),
                                 states[j].begin(),states[j].end(),back_inserter(diff));
        if(diff.size()!=8)continue;
        vector<vector<int>> h(30);
        for(int ei:diff){auto [a,b]=edges[ei];h[a].push_back(b);h[b].push_back(a);}
        int first=-1,ct=0;
        for(int v=0;v<30;v++){
            if(!h[v].empty()){
                assert(h[v].size()==2);
                if(first<0)first=v;
                ct++;
            }
        }
        assert(ct==8);
        vector<char>seen(30);queue<int>q;q.push(first);seen[first]=1;int n=0;
        while(!q.empty()){
            int x=q.front();q.pop();n++;
            for(int y:h[x])if(!seen[y]){seen[y]=1;q.push(y);}
        }
        assert(n==8); // not two 4-cycles; actual 8-cycle flip
        jump[i].push_back(j);jump[j].push_back(i);flips++;
        if(profile[i]!=profile[j])typed++;
    }
    assert(flips==1440&&typed==flips);
    for(auto &row:jump)assert(row.size()==10);
    map<int,int> ecc;
    map<vector<int>,int> distance_histograms[2];
    for(int root=0;root<288;root++){
        vector<int>dist(288,-1);queue<int>q;dist[root]=0;q.push(root);
        while(!q.empty()){
            int x=q.front();q.pop();
            for(int y:jump[x])if(dist[y]<0){dist[y]=dist[x]+1;q.push(y);}
        }
        assert(*min_element(dist.begin(),dist.end())>=0);
        int radius=*max_element(dist.begin(),dist.end());ecc[radius]++;
        vector<int>hist(7,0);
        for(int k:dist){assert(k<7);hist[k]++;}
        distance_histograms[profile[root]][hist]++;
    }
    assert(ecc[5]==144 && ecc[6]==144 && ecc.size()==2);
    assert(distance_histograms[0][vector<int>({1,10,42,97,101,37,0})]==144);
    assert(distance_histograms[1][vector<int>({1,10,45,97,96,37,2})]==144);
    assert(distance_histograms[0].size()==1 && distance_histograms[1].size()==1);
    // Enumerate all eight-cycles on the original graph independently.
    set<vector<E>> c8;
    auto dfs=[&](auto&&self,vector<int>&path)->void{
        int z=path.back();
        if(path.size()==8){
            if(find(graph[z].begin(),graph[z].end(),path[0])!=graph[z].end()){
                vector<E> ce;for(int i=0;i<8;i++)ce.push_back(minmax(path[i],path[(i+1)%8]));
                sort(ce.begin(),ce.end());c8.insert(ce);
            }
            return;
        }
        for(int v:graph[z]){
            if(v<=path[0]||find(path.begin(),path.end(),v)!=path.end())continue;
            path.push_back(v);self(self,path);path.pop_back();
        }
    };
    for(int root=0;root<30;root++){
        vector<int>path={root};dfs(dfs,path);
    }
    assert(c8.size()==90);
    cout<<"graph_vertices=30 graph_edges=45 8_cycles=90\n";
    cout<<"perfect_matchings=288 complement_30=144 complement_10_20=144\n";
    cout<<"eight_cycle_flip_edges=1440 degree=10 connected=yes bipartite_by_complement=yes\n";
    cout<<"hamiltonian_complement_distances=(1, 10, 42, 97, 101, 37, 0)\n";
    cout<<"split_complement_distances=(1, 10, 45, 97, 96, 37, 2)\n";
    cout<<"radius=5 diameter=6 eccentricities_5=144 eccentricities_6=144\n";
    cout<<"VERIFY_OK\n";
}
