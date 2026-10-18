// Exact independent finite check using residual 4-core peeling.
// Build: g++ -std=c++17 -O2 -Wall -Wextra verify_peeling.cpp -o verify_peeling
// Run: ./verify_peeling
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
const int N=16,FULL=(1<<N)-1;
int bitcount(int v){return __builtin_popcount((unsigned)v);}

struct Graph {
    array<int,N> adjacency{};
    explicit Graph(bool rook){
        for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(i!=j){
            int x=i/4,y=i%4,u=j/4,v=j%4;
            int dx=(u-x+4)%4,dy=(v-y+4)%4;
            bool edge=rook ? (x==u || y==v) :
                ((dx==1&&dy==0)||(dx==3&&dy==0)||
                 (dx==0&&dy==1)||(dx==0&&dy==3)||
                 (dx==1&&dy==1)||(dx==3&&dy==3));
            if(edge) adjacency[i]|=1<<j;
        }
        for(int v=0;v<N;v++) assert(bitcount(adjacency[v])==6);
        for(int x=0;x<N;x++) for(int y=x+1;y<N;y++)
            assert(bitcount(adjacency[x]&adjacency[y])==2);
    }
    pair<int,int> run(int seeds) const {
        int remaining=FULL & (~seeds), steps=0;
        while(remaining){
            int peel=0;
            for(int v=0;v<N;v++) if(remaining&(1<<v))
                if(bitcount(adjacency[v]&remaining)<=3)peel|=1<<v;
            if(!peel)break;
            remaining &=~peel;steps++;
        }
        return {N-bitcount(remaining),steps};
    }
};

void verify(const char* name,bool rook){
    Graph G(rook);
    array<int,1<<N> index{};
    index.fill(-1);
    vector<int> seeds;
    int triple_closure=0;
    for(int m=0;m<=FULL;m++) if(bitcount(m)==3)
        triple_closure=max(triple_closure,G.run(m).first);
    for(int m=0;m<=FULL;m++) if(bitcount(m)==4)
        if(G.run(m).first==16){index[m]=(int)seeds.size();seeds.push_back(m);}
    int n=(int)seeds.size();
    assert(n==(rook?864:720));
    assert(triple_closure==(rook?5:7));
    cout<<name<<" largest closure from 3 seeds="<<triple_closure<<" minimum size=4 n="<<n<<'\n';
    map<int,int> hist;
    for(int b:seeds){assert(G.run(b).first==16);hist[G.run(b).second]++;}
    cout<<name<<" activation rounds ";for(auto [k,v]:hist)cout<<k<<":"<<v<<" ";cout<<'\n';
    for(int mode=0;mode<2;mode++){
        vector<vector<int>> ne(n);
        long long degree_sum=0;
        for(int a=0;a<n;a++){
            int mask=seeds[a];
            for(int x=0;x<N;x++) if(mask&(1<<x)) {
                int targets=(mode==1 ? G.adjacency[x]:FULL) & (~mask);
                for(int y=0;y<N;y++) if(targets&(1<<y)){
                    int next=(mask&~(1<<x))|(1<<y);
                    if(index[next]>=0)ne[a].push_back(index[next]);
                }
            }
            sort(ne[a].begin(),ne[a].end());
            assert(unique(ne[a].begin(),ne[a].end())==ne[a].end());
            degree_sum+=ne[a].size();
        }
        int rad=100,diam=0;
        map<int,int> ecc_hist,degree_hist;
        for(int s=0;s<n;s++){
            degree_hist[(int)ne[s].size()]++;
            vector<int> dist(n,-1);
            queue<int> q;q.push(s);dist[s]=0;int count=1,ecc=0;
            while(!q.empty()){
                int u=q.front();q.pop();
                for(int v:ne[u])if(dist[v]<0){
                    dist[v]=dist[u]+1;
                    ecc=max(ecc,dist[v]);
                    q.push(v);count++;
                }
            }
            assert(count==n);
            ecc_hist[ecc]++;rad=min(rad,ecc);diam=max(diam,ecc);
        }
        cout<<name<<(mode?" slide":" jump")<<" edges="<<degree_sum/2
            <<" components=1 radius="<<rad<<" diameter="<<diam<<" eccentricity=";
        for(auto [k,v]:ecc_hist)cout<<k<<":"<<v<<" ";cout<<"degrees=";
        for(auto [k,v]:degree_hist)cout<<k<<":"<<v<<" ";cout<<'\n';
    }
}
int main(){verify("rook",true);verify("shri",false);cout<<"OK independent residual-core verification\n";}
