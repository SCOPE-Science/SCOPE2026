// C++17: independent dodecahedral graph representation and leaf-pruning test.
// g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <map>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
int main(){
    const int N=20;
    // Standard dodecahedron planar labeling: pairs are undirected edges.
    const pair<int,int> edges[]={{0,1},{0,10},{0,19},{1,2},{1,8},{2,3},{2,6},{3,4},{3,19},
     {4,5},{4,17},{5,6},{5,15},{6,7},{7,8},{7,14},{8,9},{9,10},{9,13},{10,11},
     {11,12},{11,18},{12,13},{12,16},{13,14},{14,15},{15,16},{16,17},{17,18},{18,19}};
    const array<int,20> to_gp={0,1,2,12,14,4,3,13,11,19,9,8,7,17,15,5,6,16,18,10};
    set<pair<int,int>> GP,converted;
    auto mkedge=[](int a,int b){if(a>b)swap(a,b);return make_pair(a,b);};
    for(int i=0;i<10;i++){
       GP.insert(mkedge(i,(i+1)%10));GP.insert(mkedge(i,10+i));GP.insert(mkedge(10+i,10+(i+2)%10));
    }
    vector<int> ngh[N];
    for(auto [a,b]:edges){ngh[a].push_back(b);ngh[b].push_back(a);converted.insert(mkedge(to_gp[a],to_gp[b]));}
    assert(converted==GP && GP.size()==30);
    for(int i=0;i<20;i++)assert(ngh[i].size()==3);
    // Completely distinct acyclicity check: prune induced degree<=1 vertices.
    auto forest=[&](uint32_t deleted)->bool{
       int deg[N]={},alive[N]={};queue<int>q;
       for(int i=0;i<N;i++)if(!(deleted>>i&1)){
          alive[i]=1;
          for(int j:ngh[i])if(!(deleted>>j&1))deg[i]++;
          if(deg[i]<=1)q.push(i);
       }
       int pruned=0;
       while(!q.empty()){
          int i=q.front();q.pop();if(!alive[i])continue;
          alive[i]=0;pruned++;
          for(int j:ngh[i])if(alive[j])if(--deg[j]<=1)q.push(j);
       }
       return pruned==N-__builtin_popcount(deleted);
    };
    vector<uint32_t> states;
    for(uint32_t mask=0;mask<(1u<<N);mask++)
       if(__builtin_popcount(mask)==6 && forest(mask))states.push_back(mask);
    assert(states.size()==2520);
    unordered_map<uint32_t,int> id;
    for(int i=0;i<(int)states.size();i++)id[states[i]]=i;
    vector<int> typ(states.size());
    map<int,int> cnt;
    for(int i=0;i<(int)states.size();i++){
       int e=0;for(auto [a,b]:edges)if((states[i]>>a&1)&&(states[i]>>b&1))e++;
       assert(e<2);cnt[e]++;typ[i]=e;
    }
    assert(cnt[0]==660 && cnt[1]==1860);
    auto calculate=[&](bool sliding){
        vector<vector<int>> A(states.size());
        // Pairwise recognition, not token-enumeration, of a single replacement.
        map<pair<int,int>,int> bytype;
        int edges_count=0;
        for(int i=0;i<(int)states.size();i++)for(int j=i+1;j<(int)states.size();j++){
            uint32_t X=states[i]&~states[j],Y=states[j]&~states[i];
            if(__builtin_popcount(X)!=1 || __builtin_popcount(Y)!=1)continue;
            int x=__builtin_ctz(X),y=__builtin_ctz(Y);
            if(sliding && find(ngh[x].begin(),ngh[x].end(),y)==ngh[x].end())continue;
            A[i].push_back(j);A[j].push_back(i);edges_count++;
            bytype[mkedge(typ[i],typ[j])]++;
        }
        map<int,int> eccentricity;
        for(int src=0;src<(int)states.size();src++){
            vector<int> distance(states.size(),-1);queue<int>q;
            q.push(src);distance[src]=0;int reached=1,maxdist=0;
            while(!q.empty()){
                int x=q.front();q.pop();
                for(int y:A[x])if(distance[y]<0){
                    distance[y]=distance[x]+1;maxdist=max(maxdist,distance[y]);
                    q.push(y);reached++;
                }
            }
            assert(reached==(int)states.size());
            eccentricity[maxdist]++;
        }
        if(sliding){
            assert(edges_count==8880 && eccentricity.size()==3);
            assert(eccentricity[8]==120 && eccentricity[9]==2340 && eccentricity[10]==60);
            assert(bytype[mkedge(0,0)]==1620 && bytype[mkedge(0,1)]==3120 && bytype[mkedge(1,1)]==4140);
        } else {
            assert(edges_count==23940 && eccentricity.size()==1 && eccentricity[6]==2520);
            assert(bytype[mkedge(0,0)]==3180 && bytype[mkedge(0,1)]==9600 && bytype[mkedge(1,1)]==11160);
        }
        printf("%s_OK vertices=%zu edges=%d radius=%d diameter=%d eccentricity",sliding?"SLIDE_PAIR":"JUMP_PAIR",states.size(),edges_count,eccentricity.begin()->first,eccentricity.rbegin()->first);
        for(auto [d,c]:eccentricity)printf(" %d:%d",d,c);
        printf("\n");
    };
    calculate(true);calculate(false);
    puts("ALTERNATE_CERTIFICATE_OK");
}
