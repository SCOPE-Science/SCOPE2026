// Self-contained exhaustive perfect-matching four-switch checker.
// Compile: g++ -O2 -std=c++17 independent.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <deque>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using State=array<int,16>;
struct Census{
    bool A[16][16]{};
    vector<State> states;
    map<State,int> index;
    void build(bool rook){
        for(int u=0;u<16;++u) for(int v=u+1;v<16;++v){
            int a=u/4,b=u%4,c=v/4,d=v%4;
            int x=((a-c+4)%4),y=((b-d+4)%4);
            bool edge=rook?(a==c || b==d):(
                (x==1&&y==0)||(x==3&&y==0)||(x==0&&y==1)||
                (x==0&&y==3)||(x==1&&y==1)||(x==3&&y==3));
            A[u][v]=A[v][u]=edge;
        }
        int ne=0;
        for(int u=0;u<16;++u){
            int deg=0;for(int v=0;v<16;++v)deg+=A[u][v];
            assert(deg==6);ne+=deg;
        }
        assert(ne==96);
        for(int u=0;u<16;++u)for(int v=u+1;v<16;++v){
            int common=0;for(int w=0;w<16;++w)common+=A[u][w]&&A[v][w];
            assert(common==2);
        }
        State s;s.fill(-1);recurse(s);
        sort(states.begin(),states.end());
        assert(unique(states.begin(),states.end())==states.end());
        for(int i=0;i<(int)states.size();++i)index[states[i]]=i;
    }
    void recurse(State &s){
        int u=0;while(u<16 && s[u]!=-1)++u;
        if(u==16){states.push_back(s);return;}
        for(int v=u+1;v<16;++v){
            if(s[v]==-1 && A[u][v]){
                s[u]=v;s[v]=u;recurse(s);s[u]=s[v]=-1;
            }
        }
    }
    void check(const string &name){
        vector<vector<int>> adj(states.size());
        for(int i=0;i<(int)states.size();++i){
            const State &s=states[i];set<int> neighbors;
            for(int u=0;u<16;++u)if(u<s[u]){
                int v=s[u];
                for(int x=u+1;x<16;++x)if(x<s[x] && x!=v){
                    int y=s[x];
                    for(int mode=0;mode<2;++mode){
                        int p=mode?y:x,q=mode?x:y;
                        if(!A[u][p] || !A[v][q])continue;
                        State t=s;t[u]=p;t[p]=u;t[v]=q;t[q]=v;
                        auto j=index.find(t);assert(j!=index.end());assert(j->second!=i);
                        neighbors.insert(j->second);
                    }
                }
            }
            adj[i]={neighbors.begin(),neighbors.end()};
        }
        long long sum=0;
        for(int u=0;u<(int)adj.size();++u){
            sum+=adj[u].size();
            for(int v:adj[u])assert(binary_search(adj[v].begin(),adj[v].end(),u));
        }
        assert((sum&1)==0);
        vector<char> seen(states.size(),false);
        vector<pair<int,pair<int,int>>> cc_info;
        map<int,int> sizes;
        int isolated=0;
        for(int start=0;start<(int)states.size();++start){
            if(seen[start])continue;
            vector<int> cc{start};seen[start]=true;
            for(size_t z=0;z<cc.size();++z){
                for(int v:adj[cc[z]]) if(!seen[v]){seen[v]=true;cc.push_back(v);}
            }
            ++sizes[cc.size()];
            if(cc.size()==1){isolated++;continue;}
            int radius=1e9,diameter=0;
            map<int,int> ecc_hist;
            for(int src:cc){
                vector<int> dist(states.size(),-1);
                deque<int> Q{src};dist[src]=0;int ecc=0,count=0;
                while(!Q.empty()){
                    int u=Q.front();Q.pop_front();count++;
                    ecc=max(ecc,dist[u]);
                    for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;Q.push_back(v);}
                }
                assert(count==(int)cc.size());
                radius=min(radius,ecc);diameter=max(diameter,ecc);ecc_hist[ecc]++;
            }
            cc_info.push_back({(int)cc.size(),{radius,diameter}});
            cout<<name<<" component_size="<<cc.size()<<" radius="<<radius<<" diameter="<<diameter<<" ecc=";
            for(auto [e,n]:ecc_hist)cout<<e<<":"<<n<<",";
            cout<<"\n";
        }
        sort(cc_info.begin(),cc_info.end());
        cout<<name<<" matchings="<<states.size()<<" switch_edges="<<(sum/2)<<" components=";
        for(auto [size,n]:sizes)cout<<size<<":"<<n<<",";
        cout<<" isolated="<<isolated<<"\n";
    }
};
int main(){
    Census r;r.build(true);r.check("rook");
    Census s;s.build(false);s.check("shrikhande");
}
