// Independent finite verification using vector-space Fano lines over GF(2).
// Compile with: c++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using Mask = uint32_t;
using Partition = array<Mask,7>;
int main() {
    vector<array<int,3>> lines;
    set<array<int,3>> distinct;
    for(int a=1;a<=7;a++) for(int b=a+1;b<=7;b++) {
        array<int,3> line{a,b,a^b}; sort(line.begin(),line.end());
        distinct.insert(line);
    }
    assert(distinct.size()==7);
    for(auto L:distinct) lines.push_back(L);
    auto incident=[&](int p,int j) {return find(lines[j].begin(),lines[j].end(),p)!=lines[j].end();};
    vector<pair<int,int>> E;
    for(int p=1;p<=7;p++) for(int j=0;j<7;j++) if(incident(p,j)) E.emplace_back(p,j);
    assert(E.size()==21);
    auto disjoint_strong=[&](int i,int j) {
        auto [p,l]=E[i]; auto [q,m]=E[j];
        return p!=q && l!=m && !incident(p,m) && !incident(q,l);
    };
    vector<Mask> triples;
    for(int i=0;i<21;i++) for(int j=i+1;j<21;j++) for(int k=j+1;k<21;k++) {
        if(disjoint_strong(i,j) && disjoint_strong(i,k) && disjoint_strong(j,k))
            triples.push_back((1u<<i)|(1u<<j)|(1u<<k));
    }
    assert(triples.size()==84);
    for(int a=0;a<21;a++) for(int b=a+1;b<21;b++)
       for(int c=b+1;c<21;c++) for(int d=c+1;d<21;d++) {
           bool valid=true;
           for(int x: {a,b,c,d}) for(int y: {a,b,c,d}) if(x<y && !disjoint_strong(x,y)) valid=false;
           assert(!valid);
       }
    vector<vector<Mask>> at(21);
    for(Mask m:triples) for(int i=0;i<21;i++) if(m&(1u<<i)) at[i].push_back(m);
    set<Partition> solutions;
    Partition stack{};
    auto dfs = [&](auto&& self,Mask used,int length)->void {
        if(used==(1u<<21)-1){assert(length==7);Partition p=stack;sort(p.begin(),p.end());solutions.insert(p);return;}
        int first=0;while(used&(1u<<first))first++;
        for(Mask m:at[first]) if(!(m&used)) {stack[length]=m;self(self,used|m,length+1);}
    };
    dfs(dfs,0,0);
    assert(solutions.size()==416);
    vector<Partition> S(solutions.begin(),solutions.end());
    vector<vector<int>> graph(S.size());
    long long edges2=0,edges3=0;
    for(int i=0;i<(int)S.size();i++)for(int j=0;j<i;j++) {
        int common=0;
        for(Mask x:S[i]) for(Mask y:S[j]) if(x==y) common++;
        if(common==5) edges2++;
        if(common==4) {
            graph[i].push_back(j);graph[j].push_back(i);edges3++;
        }
    }
    assert(edges2==0 && edges3==1568);
    map<int,int> degree_hist;
    for(const auto& g:graph)degree_hist[g.size()]++;
    const map<int,int> expected_degrees{{5,112},{8,280},{14,24}};
    assert(degree_hist==expected_degrees);
    int r=100000,d=0;
    for(int root=0;root<(int)S.size();root++){
        vector<int> dist(S.size(),-1);queue<int> q;
        dist[root]=0;q.push(root);
        int visited=0,ecc=0;
        while(!q.empty()) {
            int x=q.front();q.pop();visited++;
            ecc=max(ecc,dist[x]);
            for(int y:graph[x])if(dist[y]<0){dist[y]=dist[x]+1;q.push(y);}
        }
        assert(visited==416);
        r=min(r,ecc);d=max(d,ecc);
    }
    assert(r==6 && d==6);
    cout<<"INDEPENDENT_MATCHINGS_OK maximum=3 triples="<<triples.size()<<"\n";
    cout<<"INDEPENDENT_PARTITIONS_OK "<<solutions.size()<<"\n";
    cout<<"INDEPENDENT_TRADE_OK two_colour_edges="<<edges2<<" three_colour_edges="<<edges3<<"\n";
    cout<<"INDEPENDENT_METRIC_OK connected=1 radius="<<r<<" diameter="<<d<<"\n";
    cout<<"INDEPENDENT_VERIFY_OK\n";
}
