// Independent edge-signature census for the seven-petal flower snark.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_signatures.cpp -o verify_signatures
// Run: ./verify_signatures
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
    const int n=7, nv=4*n;
    auto vertex=[&](int type,int i){return type*n+i;};
    vector<pair<int,int>> edge;
    auto add=[&](int x,int y){edge.push_back({x,y});};
    for(int i=0;i<n;i++){
        for(int t=1;t<4;t++) add(vertex(0,i),vertex(t,i));
        add(vertex(1,i),vertex(1,(i+1)%n));
        if(i<n-1){add(vertex(2,i),vertex(2,i+1));add(vertex(3,i),vertex(3,i+1));}
        else {add(vertex(2,i),vertex(3,0));add(vertex(3,i),vertex(2,0));}
    }
    assert(edge.size()==42);
    vector<vector<int>> nb(nv);
    for(auto [u,v]:edge){nb[u].push_back(v);nb[v].push_back(u);}
    for(auto a:nb) assert(a.size()==3);
    // Floyd-Warshall, independent of shortest-path BFS used in the companion verifier.
    vector<vector<int>> dd(nv,vector<int>(nv,9999));
    for(int i=0;i<nv;i++)dd[i][i]=0;
    for(auto [u,v]:edge)dd[u][v]=dd[v][u]=1;
    for(int k=0;k<nv;k++)for(int i=0;i<nv;i++)for(int j=0;j<nv;j++)
        dd[i][j]=min(dd[i][j],dd[i][k]+dd[k][j]);
    vector<vector<int>> ed(nv,vector<int>(edge.size()));
    for(int v=0;v<nv;v++)for(int e=0;e<(int)edge.size();e++)
        ed[v][e]=min(dd[v][edge[e].first],dd[v][edge[e].second]);
    auto resolves=[&](const vector<int>& s){
        set<vector<int>> signatures;
        for(int e=0;e<(int)edge.size();e++){
            vector<int> sig;
            for(int v:s)sig.push_back(ed[v][e]);
            signatures.insert(sig);
        }
        return signatures.size()==edge.size();
    };
    int count3=0;
    for(int a=0;a<nv;a++)for(int b=a+1;b<nv;b++)for(int c=b+1;c<nv;c++)
        count3+=resolves({a,b,c});
    assert(count3==0);
    vector<array<int,4>> bases;
    map<array<int,4>,int> idx;
    for(int a=0;a<nv;a++)for(int b=a+1;b<nv;b++)for(int c=b+1;c<nv;c++)for(int d=c+1;d<nv;d++){
        if(resolves({a,b,c,d})){
            array<int,4> x={a,b,c,d}; idx[x]=(int)bases.size();bases.push_back(x);
        }
    }
    assert(bases.size()==1932);
    assert(resolves({vertex(0,0),vertex(1,0),vertex(2,1),vertex(2,4)}));
    vector<vector<int>> change(bases.size());
    long long edges=0;
    for(int i=0;i<(int)bases.size();i++)for(int j=i+1;j<(int)bases.size();j++){
        int overlap=0;
        for(int a:bases[i])for(int b:bases[j])overlap+=(a==b);
        if(overlap==3){change[i].push_back(j);change[j].push_back(i);edges++;}
    }
    assert(edges==17920);
    int min_ecc=999,max_ecc=0;
    for(int src=0;src<(int)bases.size();src++){
        vector<int> distances(bases.size(),-1);distances[src]=0;
        queue<int> Q;Q.push(src);
        while(!Q.empty()){
            int u=Q.front();Q.pop();
            for(int w:change[u])if(distances[w]<0){distances[w]=distances[u]+1;Q.push(w);}
        }
        int ecc=0;
        for(int d:distances){assert(d>=0);ecc=max(ecc,d);}
        min_ecc=min(min_ecc,ecc);max_ecc=max(max_ecc,ecc);
        assert(ecc==5);
    }
    assert(min_ecc==5 && max_ecc==5);
    cout<<"graph: vertices=28 edges=42 degree=3\n";
    cout<<"edge-pair separation constraints=861\n";
    cout<<"3-subsets checked=3276 resolving=0\n";
    cout<<"4-subsets checked=20475 resolving=1932\n";
    cout<<"witness={a0,b0,c1,c4}\n";
    cout<<"basis-exchange: vertices=1932 edges=17920 components=1\n";
    cout<<"eccentricities: {5: 1932}; radius=5 diameter=5\n";
    cout<<"VERIFIED\n";
}
