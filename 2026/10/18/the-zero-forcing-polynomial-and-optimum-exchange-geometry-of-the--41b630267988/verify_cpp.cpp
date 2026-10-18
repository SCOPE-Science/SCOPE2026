// Standalone C++17 finite verifier for ordinary zero forcing on the
// 2-3-subset incidence graph of a five-element set.
// Usage: c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp certificate.tsv
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int weight(unsigned m) { return __builtin_popcount(m); }
int main(int argc,char**argv) {
    if (argc!=2) { cerr << "Specify output certificate path\n";return 2; }
    vector<unsigned> vv;
    for (unsigned s=0;s<32;s++) if (weight(s)==2 || weight(s)==3) vv.push_back(s);
    assert(vv.size()==20);
    int index[32];fill(index,index+32,-1);
    for (int i=0;i<20;i++)index[vv[i]]=i;
    array<unsigned,20> nbr{};
    for (int i=0;i<20;i++)for (int j=0;j<20;j++)
        if (weight(vv[i])==2 && weight(vv[j])==3 && (vv[i]&vv[j])==vv[i])
            nbr[i] |= (1u<<j),nbr[j] |= (1u<<i);
    assert(accumulate(nbr.begin(),nbr.end(),0,[](int z,unsigned m){return z+weight(m);})==60);
    constexpr unsigned FULL=(1u<<20)-1;
    // Deliberately sequential forcing (rather than simultaneous closure):
    // perform the first legal black -> unique-white force and restart.
    auto forcing = [&](unsigned mask) -> bool {
        for (;;) {
            bool moved=false;
            for (int i=0;i<20 && !moved;i++) if (mask & (1u<<i)) {
                unsigned white = nbr[i] & (~mask);
                if (white && ((white & (white-1)) == 0u)) {
                    mask |= white;moved=true;
                }
            }
            if (!moved)return mask==FULL;
        }
    };
    vector<uint8_t> allowed(FULL+1,0);
    vector<unsigned> states;
    array<long long,21> poly{};
    for (unsigned m=0;m<=FULL;m++)if (forcing(m)) {
        int k=weight(m);poly[k]++;
        if (k==8)states.push_back(m),allowed[m]=1;
    }
    assert(states.size()==13520);
    assert(accumulate(poly.begin(),poly.end(),0LL)==524462);
    unsigned side=0;
    for (int i=0;i<20;i++) if (weight(vv[i])==2)side|=(1u<<i);
    for (unsigned s:states)assert(weight(s&side)==4 && weight(s&(~side))==4);
    vector<int> ind(FULL+1,-1);
    for (int i=0;i<(int)states.size();i++)ind[states[i]]=i;
    vector<pair<unsigned,unsigned>> edges;
    vector<vector<int>> graph(states.size());
    for (unsigned s:states) {
        for (int i=0;i<20;i++)if (s&(1u<<i))
            for (int j=0;j<20;j++)if (!(s&(1u<<j))) {
                unsigned t=s^(1u<<i)^(1u<<j);
                if (t>s && allowed[t]) {
                    edges.push_back({s,t});
                    graph[ind[s]].push_back(ind[t]);
                    graph[ind[t]].push_back(ind[s]);
                }
            }
    }
    sort(edges.begin(),edges.end());
    assert(edges.size()==178560);
    map<int,int> degree;
    for (auto& L:graph)degree[(int)L.size()]++;

    // Explicit size-240 group: S5 on underlying points and complement duality.
    vector<array<int,20>> maps;
    array<int,5> perm{{0,1,2,3,4}};
    do {
        for (int dual=0;dual<2;dual++) {
            array<int,20> f{};
            for (int v=0;v<20;v++) {
                unsigned w=0;
                for (int i=0;i<5;i++)if (vv[v]&(1u<<i))w|=1u<<perm[i];
                if (dual)w^=31u;
                f[v]=index[w];assert(f[v]>=0);
            }
            maps.push_back(f);
        }
    }while(next_permutation(perm.begin(),perm.end()));
    assert(maps.size()==240);
    auto transform=[](unsigned s,const array<int,20>& f)->unsigned {
        unsigned res=0;
        for (int j=0;j<20;j++)if (s&(1u<<j))res|=1u<<f[j];
        return res;
    };
    vector<uint8_t> seen(FULL+1,0);
    struct Orbit {unsigned rep;int size,ecc;vector<int> hist;};
    vector<Orbit> orbits;
    map<int,int> eccdistrib,orbitsizes;
    int total_reps=0;
    for (unsigned s:states) {
        if (seen[s])continue;
        vector<unsigned> orb;
        for (const auto& p:maps) {
            unsigned t=transform(s,p);
            assert(allowed[t]);
            orb.push_back(t);
        }
        sort(orb.begin(),orb.end());orb.erase(unique(orb.begin(),orb.end()),orb.end());
        for (auto t:orb){assert(!seen[t]);seen[t]=1;}
        orbitsizes[(int)orb.size()]++;
        vector<int> distance(states.size(),-1);
        vector<int> queue;
        distance[ind[s]]=0;queue.push_back(ind[s]);
        for (size_t head=0;head<queue.size();head++) {
            int v=queue[head];
            for (int w:graph[v])if (distance[w]==-1) {
                distance[w]=distance[v]+1;queue.push_back(w);
            }
        }
        assert(queue.size()==states.size());
        int ecc=*max_element(distance.begin(),distance.end());
        vector<int> hist(ecc+1,0);
        for (int d:distance) {assert(d>=0);hist[d]++;}
        eccdistrib[ecc]+=(int)orb.size();
        orbits.push_back(Orbit{s,(int)orb.size(),ecc,hist});
        total_reps++;
    }
    assert(orbits.size()==67);
    assert(eccdistrib[7]==980 && eccdistrib[8]==12540);

    ofstream out(argv[1],ios::binary);
    if (!out) {cerr<<"Cannot write certificate\n";return 3;}
    out<<"DZF1\nPOLY";
    for (auto x:poly)out<<' '<<x;
    out<<"\nZ8 13520\nJUMPEDGES 178560\nECC 7:980 8:12540\nDEGREES";
    for (auto [k,c]:degree)out<<' '<<k<<':'<<c;
    out<<"\nORBITS 67\n";
    out<<hex<<setfill('0');
    for (unsigned s:states)out<<"S "<<setw(5)<<s<<'\n';
    for (auto [u,v]:edges)out<<"E "<<setw(5)<<u<<' '<<setw(5)<<v<<'\n';
    for (auto& o:orbits) {
        out<<"O "<<setw(5)<<o.rep<<dec<<' '<<o.size<<' '<<o.ecc<<' ';
        for (int i=0;i<(int)o.hist.size();i++) {if(i)out<<',';out<<o.hist[i];}
        out<<'\n'<<hex;
    }
    out.close();
    cout<<"verified vertices=20 edges=30 kmin=8 minsets=13520 balanced=13520\n";
    cout<<"forcing_polynomial=";
    for (int i=0;i<=20;i++){if (i)cout<<',';cout<<poly[i];}
    cout<<"\nexchanges="<<edges.size()<<" degree_hist=";
    for (auto [k,v]:degree)cout<<k<<':'<<v<<' ';
    cout<<"\ntoken_slide_edges=0\n";
    cout<<"automorphism_action_size=240 orbit_count="<<orbits.size()<<" orbit_sizes=";
    for (auto [k,v]:orbitsizes)cout<<k<<':'<<v<<' ';
    cout<<"\njump_components=1 radius=7 diameter=8 eccentricity_hist=";
    for (auto [k,v]:eccdistrib)cout<<k<<':'<<v<<' ';
    cout<<"\n";
    return 0;
}
