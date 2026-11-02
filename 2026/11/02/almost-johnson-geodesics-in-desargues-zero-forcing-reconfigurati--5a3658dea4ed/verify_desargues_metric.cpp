// Exact finite proof checker: minimum zero-forcing-set exchange metric on GP(10,3).
// Compile: g++ -std=c++17 -O3 verify_desargues_metric.cpp -o verify_desargues_metric
// Run: ./verify_desargues_metric
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
static constexpr int N=20, K=8, MAXMASK=(1<<N);
static uint32_t nbr[N];
static void connect(int i,int j){nbr[i]|=(1u<<j);nbr[j]|=(1u<<i);}
static uint32_t closure(uint32_t mask){
    while(true){uint32_t addition=0, remaining=mask;
        while(remaining){int u=__builtin_ctz(remaining);remaining&=remaining-1;
            uint32_t white=nbr[u]&~mask;
            if(white!=0 && (white&(white-1))==0) addition|=white;
        }
        if((addition&~mask)==0)return mask;
        mask|=addition;
    }
}
// Gosper's exact fixed-cardinality enumeration; each mask appears once.
static vector<uint32_t> family(int k){
    vector<uint32_t> out;
    uint32_t x=(1u<<k)-1;
    while(x<MAXMASK){
        if(closure(x)==MAXMASK-1)out.push_back(x);
        uint32_t c=x&-x,r=x+c;
        if(!r || r>=MAXMASK)break;
        x=(((r^x)>>2)/c)|r;
    }
    return out;
}
static vector<int> shortest(int start,const vector<vector<int>>& graph){
    int n=graph.size();vector<int> distance(n,-1),queue(n);
    int head=0,tail=0;distance[start]=0;queue[tail++]=start;
    while(head<tail){int u=queue[head++];
        for(int v:graph[u])if(distance[v]<0){
            distance[v]=distance[u]+1;queue[tail++]=v;
        }
    }
    return distance;
}
int main(){
    for(int i=0;i<10;i++){
        connect(i,(i+1)%10);
        connect(i,10+i);
        connect(10+i,10+(i+3)%10);
    }
    for(int i=0;i<N;i++)assert(__builtin_popcount(nbr[i])==3);
    assert(family(7).empty());
    auto configurations=family(K);
    assert(configurations.size()==13520);
    int size=configurations.size();
    vector<int> index(MAXMASK,-1);
    for(int i=0;i<size;i++)index[configurations[i]]=i;
    vector<vector<int>> graph(size);
    map<int,long long> degrees,eccentricities;
    for(int i=0;i<size;i++){
        uint32_t mask=configurations[i],selected=mask,unselected=(MAXMASK-1)^mask;
        while(selected){int u=__builtin_ctz(selected);selected&=selected-1;
            uint32_t available=unselected;
            while(available){int v=__builtin_ctz(available);available&=available-1;
                int j=index[mask^(1u<<u)^(1u<<v)];
                if(j>=0)graph[i].push_back(j);
            }
        }
        degrees[graph[i].size()]++;
    }
    for(int i=0;i<size;i++){
        for(int j:graph[i]){
            assert(j>=0 && j<size);
            assert(binary_search(configurations.begin(),configurations.end(),configurations[j]));
            assert(find(graph[j].begin(),graph[j].end(),i)!=graph[j].end());
        }
    }
    long long directed_edges=0;
    for(auto &g:graph) directed_edges+=g.size();
    assert(directed_edges==357120);
    const map<int,long long> expected_degrees={{20,240},{21,120},{22,360},{23,480},{24,1340},{25,1800},{26,3000},{27,240},{28,4380},{29,480},{30,960},{32,120}};
    assert(degrees==expected_degrees);
    map<pair<int,int>,long long> joint;
    int radius=size,diameter=0;
    long long pairs=0;
    for(int s=0;s<size;s++){
        auto distance=shortest(s,graph);
        int eccentricity=0;
        for(int t=0;t<size;t++){
            assert(distance[t]>=0); // Every source reaches every configuration.
            eccentricity=max(eccentricity,distance[t]);
            if(t<=s)continue;
            int johnson=K-__builtin_popcount(configurations[s]&configurations[t]);
            int excess=distance[t]-johnson;
            assert(0<=excess && excess<=1);
            joint[{johnson,excess}]++;
            ++pairs;
        }
        eccentricities[eccentricity]++;
        radius=min(radius,eccentricity);
        diameter=max(diameter,eccentricity);
    }
    const map<pair<int,int>,long long> expected_joint={
      {{1,0},178560},{{2,0},1883280},{{2,1},16080},
      {{3,0},9472620},{{3,1},25080},{{4,0},23996580},{{4,1},5730},
      {{5,0},30815880},{{5,1},360},{{6,0},19315140},{{6,1},130},
      {{7,0},5187480},{{8,0},491520}};
    assert(joint==expected_joint);
    assert(pairs==91388440);
    assert(radius==7 && diameter==8);
    const map<int,long long> expected_ecc={{7,980},{8,12540}};
    assert(eccentricities==expected_ecc);
    // A concrete shortest detour: exchanged sites are 0,...,19 on GP(10,3).
    const array<uint32_t,4> path={255,639,879,999};
    for(auto mask:path)assert(index[mask]>=0);
    for(int i=0;i<3;i++){
        assert(__builtin_popcount(path[i]^path[i+1])==2);
        auto &out=graph[index[path[i]]];
        assert(find(out.begin(),out.end(),index[path[i+1]])!=out.end());
    }
    assert(K-__builtin_popcount(path.front()&path.back())==2);
    assert(shortest(index[path.front()],graph)[index[path.back()]]==3);
    cout<<"DESARGUES_METRIC_EXHAUSTIVE_PASS\n"
        <<"seven_subsets=77520 seven_forcing=0 eight_subsets=125970 eight_forcing=13520\n"
        <<"edges=178560 connected=1 radius=7 diameter=8\n"
        <<"eccentricities 7:980 8:12540\n"
        <<"paircount=91388440 excess_zero=91341060 excess_one=47380 excess_other=0\n"
        <<"exception_by_johnson 2:16080 3:25080 4:5730 5:360 6:130\n";
}
