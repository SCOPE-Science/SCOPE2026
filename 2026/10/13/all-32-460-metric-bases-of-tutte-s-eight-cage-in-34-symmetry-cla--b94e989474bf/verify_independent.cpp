// Independent direct-distance census for the Tutte--Coxeter incidence graph.
// Build: c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
using E=array<int,2>;
using F=array<int,3>;
vector<E> edges;
vector<F> factors;
void enumerate_factors(vector<int> rem,vector<int> chosen) {
    if(rem.empty()) {
        sort(chosen.begin(),chosen.end());
        factors.push_back({chosen[0],chosen[1],chosen[2]});
        return;
    }
    int a=rem[0];
    for(size_t j=1;j<rem.size();j++) {
        int b=rem[j],index=-1;
        for(int e=0;e<15;e++)if(edges[e]==E{a,b}){index=e;break;}
        assert(index>=0);
        vector<int> rest;
        for(int c:rem)if(c!=a && c!=b)rest.push_back(c);
        auto nxt=chosen; nxt.push_back(index);
        enumerate_factors(rest,nxt);
    }
}
int main(){
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)edges.push_back({a,b});
    enumerate_factors({0,1,2,3,4,5},{});
    sort(factors.begin(),factors.end());
    assert(factors.size()==15);
    vector<vector<int>> adj(30);
    for(int i=0;i<15;i++)for(int e:factors[i]){
        adj[i].push_back(15+e);adj[15+e].push_back(i);
    }
    for(const auto& a:adj)assert(a.size()==3);
    int d[30][30];
    for(int s=0;s<30;s++) {
        fill(d[s],d[s]+30,-1);
        queue<int> q;q.push(s);d[s][s]=0;
        while(!q.empty()){
            int u=q.front();q.pop();
            for(int v:adj[u])if(d[s][v]<0){d[s][v]=d[s][u]+1;q.push(v);}
        }
        for(int v=0;v<30;v++)assert(d[s][v]>=0 && d[s][v]<=4);
    }
    array<array<int,30>,30> dist;
    for(int u=0;u<30;u++)for(int v=0;v<30;v++)dist[u][v]=d[u][v];
    uint64_t examined[7]={}, resolving[7]={};
    map<pair<int,int>,long long> profile;
    // Independent predicate: construct direct ordered distance signature of every vertex.
    for(int k=5;k<=6;k++) {
        vector<int> C(k);
        for(int i=0;i<k;i++)C[i]=i;
        while(true) {
            examined[k]++;
            set<vector<int>> signatures;
            for(int vertex=0;vertex<30;vertex++) {
                vector<int> a;
                for(int c:C)a.push_back(dist[vertex][c]);
                signatures.insert(move(a));
            }
            if(signatures.size()==30){
                resolving[k]++;
                int nf=0,internal=0;
                for(int u:C){if(u<15)nf++;for(int v:C)if(u<v && find(adj[u].begin(),adj[u].end(),v)!=adj[u].end())internal++;}
                profile[{nf,internal}]++;
            }
            int j=k-1;
            while(j>=0 && C[j]==30-k+j)j--;
            if(j<0)break;
            C[j]++;
            for(int t=j+1;t<k;t++)C[t]=C[t-1]+1;
        }
    }
    assert(examined[5]==142506 && resolving[5]==0);
    assert(examined[6]==593775 && resolving[6]==32460);
    assert(profile[make_pair(2,0)]==4230 && profile[make_pair(2,1)]==2880 && profile[make_pair(2,2)]==360);
    assert(profile[make_pair(3,0)]==3840 && profile[make_pair(3,1)]==7920 && profile[make_pair(3,2)]==5760);
    assert(profile[make_pair(4,0)]==4230 && profile[make_pair(4,1)]==2880 && profile[make_pair(4,2)]==360);
    cout<<"VERIFY_INDEPENDENT_OK graph=K6_incidence n=30 m=45 BFS_distances\n";
    cout<<"VERIFY_INDEPENDENT_OK direct_distance_signatures_C30_5="<<examined[5]<<" none\n";
    cout<<"VERIFY_INDEPENDENT_OK direct_distance_signatures_C30_6="<<examined[6]<<" bases="<<resolving[6]<<"\n";
    cout<<"VERIFY_INDEPENDENT_OK same_side_and_induced_edge_profile=exact\n";
}
