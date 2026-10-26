// Exact finite-subspace enumeration and deletion-list verification.
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

struct Census {
    uint64_t examined=0, passing=0;
    vector<int> first_witness;
};
static int n, k;
static int pivot[10], row[10];
static Census census;

// Distinct received words are counted once for each candidate codeword.
static bool admissible(const vector<int>& generator, int length, int *hist=nullptr) {
    const int dimension = int(generator.size());
    vector<uint8_t> multiplicity(1u<<(length-1),0);
    for (int mask=0;mask<(1<<dimension);++mask) {
        int word=0;
        for(int i=0;i<dimension;++i)
            if((mask>>i)&1) word^=generator[i];
        int distinct[10], num=0;
        for(int j=0;j<length;++j) {
            const int output=(word & ((1<<j)-1)) | ((word>>(j+1))<<j);
            bool duplicate=false;
            for(int h=0;h<num;++h) if(distinct[h]==output) {duplicate=true;break;}
            if(!duplicate) distinct[num++]=output;
        }
        for(int h=0;h<num;++h)
            if(++multiplicity[distinct[h]]>2) return false;
    }
    if(hist) {
        for(uint8_t v : multiplicity) ++hist[v];
    }
    return true;
}
static void assign_free(size_t index,const vector<pair<int,int>>& free_positions) {
    if(index==free_positions.size()) {
        ++census.examined;
        vector<int> g(row,row+k);
        if(admissible(g,n)) {
            ++census.passing;
            if(census.first_witness.empty()) census.first_witness=g;
        }
        return;
    }
    assign_free(index+1,free_positions);
    auto [i,j]=free_positions[index];
    row[i]^=(1<<j);
    assign_free(index+1,free_positions);
    row[i]^=(1<<j);
}
static void choose_pivots(int index,int first) {
    if(index==k) {
        vector<pair<int,int>> free_positions;
        for(int i=0;i<k;++i) {
            row[i]=1<<pivot[i];
            for(int j=pivot[i]+1;j<n;++j) {
                bool other_pivot=false;
                for(int h=0;h<k;++h) if(pivot[h]==j) other_pivot=true;
                if(!other_pivot) free_positions.push_back({i,j});
            }
        }
        assign_free(0,free_positions);
        return;
    }
    for(int j=first;j<=n-(k-index);++j) {
        pivot[index]=j;
        choose_pivots(index+1,j+1);
    }
}
static Census enumerate(int length,int dimension) {
    n=length;k=dimension;census=Census{};
    choose_pivots(0,0);
    return census;
}
static void require(bool truth,const char* msg) {
    if(!truth){ cerr<<"FAILED: "<<msg<<'\n';exit(1); }
}
int main() {
    // Exact maximum dimensions for each length from 1 through 10.
    const int maxima[11]={0,1,1,2,2,3,3,4,5,5,6};
    const uint64_t total_max[10]={0,1,3,7,35,155,1395,11811,97155,3309747};
    const uint64_t good_max[10]={0,1,3,3,27,28,715,1406,286,438503};
    const uint64_t total_next[10]={0,0,1,1,15,31,651,2667,10795,788035};
    for(int length=1;length<=9;++length) {
        const int dim=maxima[length];
        auto r=enumerate(length,dim);
        require(r.examined==total_max[length],"RREF count at feasible dimension");
        require(r.passing==good_max[length],"feasible-dimension count");
        require(!r.first_witness.empty(),"missing feasible generator");
        if(dim<length) {
            auto s=enumerate(length,dim+1);
            require(s.examined==total_next[length],"RREF count at excluded dimension");
            require(s.passing==0,"forbidden larger dimension exists");
        }
        cout<<"length="<<length<<" maximum_dimension="<<dim
            <<" number_of_maximum_dimension_subspaces="<<r.passing<<'\n';
    }
    // A six-dimensional length-ten linear code. Coordinate zero is the low bit.
    const vector<int> g={513,770,452,328,464,928};
    for(int i=0;i<6;++i) require(((g[i]>>i)&1)==1,"pivot bit absent");
    for(int i=0;i<6;++i) for(int j=0;j<6;++j)
        if(i!=j) require(((g[i]>>j)&1)==0,"nonpivot row entry");
    int hist[3]={0,0,0};
    require(admissible(g,10,hist),"length-ten generator not two-list decodable");
    require(hist[0]==220 && hist[1]==232 && hist[2]==60,"length-ten histogram");
    const auto upper=enumerate(10,7);
    require(upper.examined==6347715,"RREF count for 10-by-7");
    require(upper.passing==0,"a 10-by-7 code passed");
    cout<<"length=10 maximum_dimension=6"<<'\n';
    cout<<"length-ten list histogram: "<<hist[0]<<' '<<hist[1]<<' '<<hist[2]<<'\n';
    cout<<"VERIFY_OK"<<'\n';
}
