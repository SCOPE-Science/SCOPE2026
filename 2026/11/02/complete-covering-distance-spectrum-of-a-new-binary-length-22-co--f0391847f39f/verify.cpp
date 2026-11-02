#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int main(int argc,char**argv){
    if(argc!=2){cerr<<"usage: verify CODEWORDS\n";return 1;}
    ifstream in(argv[1]); if(!in){cerr<<"cannot open words\n";return 1;}
    vector<uint32_t> c; uint32_t a; while(in>>a)c.push_back(a);
    constexpr uint32_t U=uint32_t(1)<<22;
    if(c.size()!=84){cerr<<"wrong number of words\n";return 1;}
    for(auto w:c)if(w>=U){cerr<<"word outside length 22\n";return 1;}
    sort(c.begin(),c.end());if(adjacent_find(c.begin(),c.end())!=c.end()){
        cerr<<"duplicate codeword\n";return 1;}
    int mind=22;for(size_t i=0;i<c.size();i++)for(size_t j=i+1;j<c.size();j++)
        mind=min(mind,__builtin_popcount(c[i]^c[j]));
    if(mind!=9){cerr<<"incorrect minimum distance "<<mind<<"\n";return 1;}
    array<uint64_t,23> direct{}; uint32_t first=U;
    for(uint32_t x=0;x<U;x++){
        int d=22;
        for(uint32_t w:c){d=min(d,__builtin_popcount(x^w));if(!d)break;}
        ++direct[d]; if(d==8&&first==U)first=x;
    }
    vector<uint8_t> dist(U,255);vector<uint32_t> q(U);uint32_t front=0,tail=0;
    for(uint32_t w:c){dist[w]=0;q[tail++]=w;}
    while(front<tail){uint32_t x=q[front++];const uint8_t d=dist[x];
        for(unsigned j=0;j<22;j++){
            uint32_t y=x^(uint32_t(1)<<j);
            if(dist[y]==255){dist[y]=d+1;q[tail++]=y;}
        }
    }
    if(tail!=U){cerr<<"BFS omitted vertices\n";return 1;}
    array<uint64_t,23> bfs{};for(auto d:dist){if(d>22){cerr<<"invalid BFS distance\n";return 1;}++bfs[d];}
    const array<uint64_t,9> expected{84,1848,19404,129360,614460,1712308,1566756,149908,176};
    for(int d=0;d<=22;d++){
       uint64_t e=(d<9)?expected[d]:0;
       if(bfs[d]!=direct[d]||direct[d]!=e){cerr<<"histogram mismatch at "<<d<<"\n";return 1;}
    }
    if(first!=78501){cerr<<"unexpected first hole\n";return 1;}
    uint64_t total=accumulate(direct.begin(),direct.end(),uint64_t{0});
    if(total!=U){cerr<<"wrong total\n";return 1;}
    uint64_t moment=0;for(int d=0;d<=22;d++)moment+=uint64_t(d)*direct[d];
    if(moment!=uint64_t(2737427)*8){cerr<<"unexpected distance sum "<<moment<<"\n";return 1;}
    cout<<"VERIFY_OK"<<" SIZE "<<c.size()<<" DISTANCE "<<mind<<" RADIUS 8 DEEP "<<direct[8]<<"\n";
    for(int d=0;d<9;d++)cout<<d<<' '<<direct[d]<<'\n';
    cout<<"TOTAL "<<total<<" FIRST_DEEP "<<first<<" MEAN "<<moment<<"/"<<U<<"\n";
}
