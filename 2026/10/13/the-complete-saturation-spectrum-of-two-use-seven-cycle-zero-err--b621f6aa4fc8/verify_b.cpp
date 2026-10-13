// Independent exhaustive maximal-codebook enumeration; standard C++17.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <vector>
#include <unordered_set>
using U=uint64_t;
constexpr int Q=7,V=49;
std::array<U,V> compat{};
std::vector<U> results;
inline int pop(U z){return __builtin_popcountll(z);}
void search(U partial,U allowed,U excluded){
    if(!(allowed|excluded)){results.push_back(partial);return;}
    U pool=allowed|excluded; int best=-1,score=-1;
    while(pool){int u=__builtin_ctzll(pool);pool&=pool-1; int c=pop(allowed&compat[u]);if(c>score){score=c;best=u;}}
    U branch=allowed&~compat[best];
    while(branch){U bit=branch&-branch;int u=__builtin_ctzll(branch);
        search(partial|bit,allowed&compat[u],excluded&compat[u]);
        allowed&=~bit; excluded|=bit;branch&=~bit;
    }
}
int main(int argc,char**argv){
    for(int u=0;u<V;u++)for(int v=0;v<V;v++)if(u!=v){
        int x=u/Q,y=u%Q,a=v/Q,b=v%Q;
        int d=(x-a+Q)%Q,e=(y-b+Q)%Q;
        if((d>=2&&d<=Q-2)||(e>=2&&e<=Q-2)) compat[u]|=U(1)<<v;
    }
    search(0,(U(1)<<V)-1,0);
    std::sort(results.begin(),results.end());
    assert(std::adjacent_find(results.begin(),results.end())==results.end());
    std::map<int,int> spectrum;
    for(U m:results){
        spectrum[pop(m)]++;
        for(int v=0;v<V;v++){
            U bit=U(1)<<v;
            if(m&bit) assert((m&~compat[v])==bit);
            else assert(m&~compat[v]);
        }
    }
    const std::map<int,int> expected={{7,28},{8,9016},{9,73157},{10,980}}; assert(spectrum==expected);
    auto moved=[](U m,int g)->U {
        U out=0;
        while(m){int v=__builtin_ctzll(m);m&=m-1;
            int x=v/Q,y=v%Q;
            switch(g){case 0:x=(x+1)%Q;break;case 1:y=(y+1)%Q;break;
                case 2:x=(Q-x)%Q;break;case 3:y=(Q-y)%Q;break;
                default:std::swap(x,y);break;}
            out|=U(1)<<(x*Q+y);
        }
        return out;
    };
    std::unordered_set<U> remaining(results.begin(),results.end());
    std::map<std::pair<int,int>,int> orbitSizes;
    for(U root:results)if(remaining.count(root)){
        std::unordered_set<U> seen={root};std::vector<U> queue={root};
        for(size_t i=0;i<queue.size();i++)for(int g=0;g<5;g++){
            U z=moved(queue[i],g);
            if(seen.insert(z).second){assert(remaining.count(z));queue.push_back(z);}
        }
        for(U z:seen) remaining.erase(z);
        orbitSizes[{pop(root),(int)seen.size()}]++;
    }
    assert(remaining.empty());
    const std::map<std::pair<int,int>,int> expectedOrbit={
        {{7,28},1},{{8,196},8},{{8,392},19},{{9,49},1},
        {{9,98},2},{{9,196},18},{{9,392},177},{{10,196},1},{{10,392},2}
    };
    assert(orbitSizes==expectedOrbit);
    std::cerr<<"symmetry orbits ";
    for(auto [k,v]:orbitSizes) std::cerr<<"("<<k.first<<","<<k.second<<"):"<<v<<" ";
    std::cerr<<"\n";
    std::ostream* out=&std::cout;std::ofstream file;
    if(argc>1){file.open(argv[1],std::ios::binary);assert(file);out=&file;}
    for(U m:results)(*out)<<std::hex<<std::nouppercase<<std::setfill('0')<<std::setw(13)<<m<<'\n';
    std::cerr<<"complete count "<<results.size()<<" spectrum ";
    for(auto [k,c]:spectrum) std::cerr<<k<<":"<<c<<" ";
    std::cerr<<"\n";
}
