// Independent C++17 exhaustive verifier of Clebsch edge metric basis exchanges.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
    constexpr int n=16;
    const array<int,5> directions={1,2,4,8,15};
    vector<vector<int>> adj(n);
    vector<pair<int,int>> edges;
    for(int a=0;a<n;++a) for(int d:directions){
        int b=a^d;
        if(a<b) {edges.emplace_back(a,b);adj[a].push_back(b);adj[b].push_back(a);}
    }
    assert(edges.size()==40);
    int dist[n][n];
    for(int a=0;a<n;++a){
        fill(dist[a], dist[a]+n,1000000);
        queue<int> q;q.push(a);dist[a][a]=0;
        while(!q.empty()) {int v=q.front();q.pop();
            for(int w:adj[v]) if(dist[a][w]>dist[a][v]+1){dist[a][w]=dist[a][v]+1;q.push(w);}
        }
    }
    int edge_distance[n][40];
    for(int v=0;v<n;++v) for(int j=0;j<40;++j)
        edge_distance[v][j]=min(dist[v][edges[j].first],dist[v][edges[j].second]);
    vector<int> bases;
    int checked=0;
    for(int s=0;s<(1<<n);++s){
        int k=__builtin_popcount((unsigned)s);
        if(k>9)continue;
        ++checked;
        int witnesses[9],pow3[9];
        int p=0;
        for(int v=0;v<n;++v)if(s>>v&1) witnesses[p++]=v;
        int weight=1;
        for(int i=0;i<k;++i){pow3[i]=weight;weight*=3;}
        vector<unsigned char> seen(weight,0);
        bool ok=true;
        for(int e=0;e<40;++e){
            int code=0;
            for(int i=0;i<k;++i)
                code+=edge_distance[witnesses[i]][e]*pow3[i];
            if(seen[code]){ok=false;break;}
            seen[code]=1;
        }
        if(ok){assert(k==9);bases.push_back(s);}
    }
    assert(bases.size()==1600);
    unordered_map<int,int> id;
    for(int i=0;i<(int)bases.size();++i)id[bases[i]]=i;
    vector<vector<int>> nbr(bases.size());
    long edge_count=0;
    int degree15=0,degree27=0;
    for(int i=0;i<(int)bases.size();++i){
        int s=bases[i];
        for(int x=0;x<n;++x)if(s>>x&1)
            for(int y=0;y<n;++y)if(!(s>>y&1)){
                int t=s^(1<<x)^(1<<y);
                auto it=id.find(t);
                if(it!=id.end()) nbr[i].push_back(it->second);
            }
        sort(nbr[i].begin(),nbr[i].end());
        nbr[i].erase(unique(nbr[i].begin(),nbr[i].end()),nbr[i].end());
        int d=(int)nbr[i].size();
        assert(d==15||d==27);
        if(d==15)++degree15;else ++degree27;
        edge_count+=d;
    }
    assert(degree15==1440 && degree27==160);
    assert(edge_count==2*12960);
    int radius=1000, diameter=0, ecc6=0,ecc7=0;
    for(int i=0;i<(int)bases.size();++i){
        vector<int> distance(bases.size(),-1);
        queue<int> q;q.push(i);distance[i]=0;
        int maxd=0,visited=0;
        while(!q.empty()){
            int v=q.front();q.pop();++visited;
            for(int w:nbr[v])if(distance[w]<0){distance[w]=distance[v]+1;
                maxd=max(maxd,distance[w]);q.push(w);}
        }
        assert(visited==1600);
        if(maxd==6)++ecc6;
        else if(maxd==7)++ecc7;
        else assert(false);
        radius=min(radius,maxd);diameter=max(diameter,maxd);
    }
    assert(ecc6==160 && ecc7==1440 && radius==6 && diameter==7);
    cout<<"INDEPENDENT_GRAPH_OK vertices=16 edges=40 BFS_distances=complete\n";
    cout<<"INDEPENDENT_BASIS_OK subsets_tested="<<checked<<" minimum=9 bases="<<bases.size()<<"\n";
    cout<<"INDEPENDENT_EXCHANGE_OK edges="<<edge_count/2<<" connected=1 radius="<<radius<<" diameter="<<diameter<<" ecc6="<<ecc6<<" ecc7="<<ecc7<<"\n";
    cout<<"INDEPENDENT_VERIFY_OK\n";
}
