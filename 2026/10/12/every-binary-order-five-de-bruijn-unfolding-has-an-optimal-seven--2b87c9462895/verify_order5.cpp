// Exhaustive finite certificate for binary order-five de Bruijn unfoldings.
// Compile: c++ -O2 -std=c++17 verify_order5.cpp -o verify_order5
// Execute: ./verify_order5
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;
static constexpr int ORDER=5, PERIOD=32, LENGTH=36;
static vector<uint64_t> candidates;
static uint32_t used_edges = 1u; // Edge 00000 is prescribed first.
static string traversal="0";
static long long cycles=0, unfoldings=0, witness_checks=0;
static int min_multiplicity=10000, max_multiplicity=-1;
static array<long long,121> histogram{};

static void require(bool x,const char* msg){if(!x)throw runtime_error(msg);}

static void make_candidates(int last,int remaining,uint64_t chosen){
    if(remaining==0){
        if(last>=31)candidates.push_back(chosen);
        return;
    }
    for(int next=last+1;next<=35 && next-last<=5;next++)
        make_candidates(next,remaining-1,chosen|(uint64_t(1)<<next));
}

// Independent direct check of every nonempty factor: used for one witness
// in every unfolding, not merely as a length-five reduction.
static bool direct_full_attractor(const string &w,uint64_t positions){
    for(int len=1;len<=LENGTH;len++){
        set<string> all, hit;
        for(int st=0;st+len<=LENGTH;st++){
            string f=w.substr(st,len);
            all.insert(f);
            uint64_t interval=((uint64_t(1)<<len)-1)<<st;
            if(interval&positions)hit.insert(f);
        }
        if(all!=hit)return false;
    }
    return true;
}

static void test_cut(const string &w){
    require(w.size()==LENGTH,"wrong unfolding length");
    set<string> length_five;
    for(int i=0;i<PERIOD;i++)length_five.insert(w.substr(i,ORDER));
    require(length_five.size()==PERIOD,"not a de Bruijn unfolding");

    // For each factor of length at most four, collect the union of its
    // occurrence intervals, represented by a 36-bit mask.
    map<string,uint64_t> factor_positions;
    for(int len=1;len<ORDER;len++){
        for(int i=0;i+len<=LENGTH;i++){
            auto f=w.substr(i,len);
            factor_positions[f]|=((uint64_t(1)<<len)-1)<<i;
        }
    }
    require(factor_positions.size()==30,"short-factor table not full");

    int admissible=0;
    uint64_t witness=0;
    for(uint64_t selected:candidates){
        // Every length-five window must be hit. The candidate generator
        // enforces this condition by spacing and endpoint constraints.
        for(int i=0;i<PERIOD;i++){
            uint64_t interval=((uint64_t(1)<<ORDER)-1)<<i;
            require(bool(interval&selected),"bad candidate generation");
        }
        bool pass=true;
        for(const auto &kv:factor_positions){
            if(!(kv.second&selected)){pass=false;break;}
        }
        if(pass){admissible++;witness=selected;}
    }
    require(admissible>0,"an unfolding has no size-seven attractor");
    require(direct_full_attractor(w,witness),"independent full-factor check failed");
    witness_checks++;
    histogram[admissible]++;
    min_multiplicity=min(min_multiplicity,admissible);
    max_multiplicity=max(max_multiplicity,admissible);
    unfoldings++;
}

static void enumerate_circuits(int vertex,int depth){
    if(depth==PERIOD){
        if(vertex!=0)return;
        cycles++;
        for(int rotation=0;rotation<PERIOD;rotation++){
            string w;
            for(int j=0;j<LENGTH;j++)w.push_back(traversal[(rotation+j)%PERIOD]);
            test_cut(w);
        }
        return;
    }
    for(int symbol=0;symbol<2;symbol++){
        int edge=2*vertex+symbol;
        if((used_edges>>edge)&1u)continue;
        used_edges|=uint32_t(1)<<edge;
        traversal.push_back(char('0'+symbol));
        enumerate_circuits(edge&15,depth+1);
        traversal.pop_back();
        used_edges^=uint32_t(1)<<edge;
    }
}

int main(){
    for(int first=0;first<=4;first++)
        make_candidates(first,6,uint64_t(1)<<first);
    require(candidates.size()==120,"unexpected number of window hitting sets");
    set<uint64_t> distinct(candidates.begin(),candidates.end());
    require(distinct.size()==120,"repeated candidate sets");
    enumerate_circuits(0,1);
    require(cycles==2048,"incomplete Eulerian circuit census");
    require(unfoldings==65536,"incomplete unfolding census");
    require(witness_checks==unfoldings,"not every cut fully checked");
    require(min_multiplicity==30 && max_multiplicity==120,"multiplicity extrema disagree");
    long long total=0;
    for(long long count:histogram)total+=count;
    require(total==65536,"invalid multiplicity histogram");
    require(histogram[30]==4 && histogram[120]==22,"extremal multiplicity frequencies disagree");
    cout<<"VERIFY_OK cycles="<<cycles<<" unfoldings="<<unfoldings
        <<" candidates="<<candidates.size()<<" full_factor_witnesses="<<witness_checks
        <<" min_seven_attractors="<<min_multiplicity
        <<" max_seven_attractors="<<max_multiplicity
        <<" cuts_with_30="<<histogram[30]<<" cuts_with_120="<<histogram[120]<<'\n';
}
