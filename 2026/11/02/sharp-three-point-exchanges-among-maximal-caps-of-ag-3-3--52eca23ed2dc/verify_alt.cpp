// Independent verifier: exhaustive nine-subset scan and direct three-point exchanges.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr int V = 27;
static constexpr uint32_t LIMIT = 1u << V;
int third(int a, int b) {
    int ans = 0, base = 1;
    for (int i=0; i<3; ++i) {
        ans += ((6 - (a%3) - (b%3))%3) * base;
        a /= 3; b /= 3; base *= 3;
    }
    return ans;
}
int main() {
    vector<uint32_t> line;
    for (int a=0; a<V; ++a) for (int b=a+1; b<V; ++b) {
        int c=third(a,b);
        if (b<c) line.push_back((1u<<a)|(1u<<b)|(1u<<c));
    }
    assert(line.size()==117);
    vector<uint32_t> caps;
    uint64_t tested = 0;
    // Gosper's next-combination algorithm visits every one of C(27,9) subsets.
    for(uint32_t mask=(1u<<9)-1;mask<LIMIT;) {
        tested++;
        bool good=true;
        for(uint32_t triple:line) if((mask&triple)==triple) {good=false;break;}
        if(good) caps.push_back(mask);
        uint32_t low=mask & -mask;
        uint32_t next=mask+low;
        if(next==0) break;
        mask=(((next^mask)>>2)/low)|next;
    }
    assert(tested==4686825);
    assert(caps.size()==2106);
    unordered_map<uint32_t,int> idx;
    for(int i=0;i<(int)caps.size();++i)idx[caps[i]]=i;
    // If a ten-cap existed, some nine-subset would be in the list and extend.
    for(uint32_t c:caps) for(int x=0;x<V;x++) if(!(c>>x&1)) {
        uint32_t candidate=c|(1u<<x);
        bool good=true;
        for(uint32_t triple:line) if((candidate&triple)==triple){good=false;break;}
        assert(!good);
    }
    vector<vector<int>> adj(caps.size());
    for(int i=0;i<(int)caps.size();++i) {
        int inside[9],outside[18],a=0,b=0;
        for(int x=0;x<V;x++) if(caps[i]>>x&1)inside[a++]=x;else outside[b++]=x;
        assert(a==9&&b==18);
        // This implementation uses swaps, not all-pairs intersection testing.
        for(int p=0;p<9;p++)for(int q=p+1;q<9;q++)for(int r=q+1;r<9;r++){
            uint32_t remainder=caps[i]^(1u<<inside[p])^(1u<<inside[q])^(1u<<inside[r]);
            for(int u=0;u<18;u++)for(int v=u+1;v<18;v++)for(int w=v+1;w<18;w++){
                uint32_t replacement=remainder|(1u<<outside[u])|(1u<<outside[v])|(1u<<outside[w]);
                auto it=idx.find(replacement);
                if(it!=idx.end())adj[i].push_back(it->second);
            }
        }
        sort(adj[i].begin(),adj[i].end());
        assert(unique(adj[i].begin(),adj[i].end())==adj[i].end());
        assert(adj[i].size()==72);
    }
    long long twice=0;
    for(int i=0;i<(int)caps.size();++i){
        twice+=adj[i].size();
        for(int j:adj[i])assert(binary_search(adj[j].begin(),adj[j].end(),i));
    }
    assert(twice/2==75816);
    map<pair<int,int>,int> expected = {{{0,9},1},{{1,6},72},{{2,3},576},{{2,4},522},{{2,5},108},{{3,1},153},{{3,2},648},{{3,3},24},{{4,0},2}};
    vector<int> dist(caps.size());
    for(int root=0;root<(int)caps.size();root++){
        fill(dist.begin(),dist.end(),-1);
        queue<int> Q;Q.push(root);dist[root]=0;
        while(!Q.empty()){
            int v=Q.front();Q.pop();
            for(int j:adj[v])if(dist[j]<0){dist[j]=dist[v]+1;Q.push(j);}
        }
        map<pair<int,int>,int> hist;
        for(int j=0;j<(int)caps.size();j++)hist[{dist[j],__builtin_popcount(caps[root]&caps[j])}]++;
        assert(hist==expected);
    }
    cout<<"INDEPENDENT_VERIFY_OK nine_subsets_tested=4686825 nine_caps="<<caps.size()<<" edges="<<twice/2
        <<" regular_degree=72 diameter=4 disjoint_antipodes=2"<<endl;
}
