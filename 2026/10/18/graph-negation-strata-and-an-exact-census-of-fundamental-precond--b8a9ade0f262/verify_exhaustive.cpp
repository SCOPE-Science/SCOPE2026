// Exact census of F-preconditionals on the Boolean lattice P({0,1,2}).
// Compile: g++ -std=c++17 -O2 verify_exhaustive.cpp -o verify && ./verify
// This enumerates candidate rows directly, without assuming graph classification.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int W=7, S=8;
using Row=array<unsigned char,S>;
array<vector<Row>,S> options;
array<Row,S> rows;
array<uint64_t,8> by_graph{};
array<uint64_t,6> fixcounts{};
uint64_t total_T=0,total_F=0;

void make_rows(int a){
    vector<int> inputs;
    for(int b=0;b<S;++b)if((b&a)==b)inputs.push_back(b);
    Row row{};
    auto recur=[&](auto&&self,int k)->void{
        if(k==(int)inputs.size()){
            for(int b:inputs)for(int c:inputs)
                if((b&c)==b && (row[b]&row[c])!=row[b])return;
            options[a].push_back(row);return;
        }
        int b=inputs[k];
        if(a==0){row[b]=W;self(self,k+1);return;}
        if(a==W){row[b]=b;self(self,k+1);return;}
        if(b==a){row[b]=W;self(self,k+1);return;}
        for(int v=0;v<S;++v){
            if((v&b)!=b)continue;           // P2
            if(b==0 && (v&a))continue;       // semicomplementation
            row[b]=(unsigned char)v;self(self,k+1);
        }
    };
    recur(recur,0);
}
int arr(int a,int b){return rows[a][a&b];}
bool law5(){
    // P5 can be reduced to d subset a, c subset d, since only a cap b matters.
    for(int a=0;a<S;++a)for(int d=0;d<S;++d)if((d&a)==d)
        for(int c=0;c<S;++c)if((c&d)==c){
            int y=rows[d][c];
            int z=rows[a][a&y];
            if((z&y)!=z)return false;
        }
    return true;
}
int mask_perm(int m,const array<int,3>&p){
    int ans=0;for(int i=0;i<3;++i)if(m&(1<<i))ans|=1<<p[i];return ans;
}
void examine(){
    if(!law5())return;
    ++total_T;
    for(int a=0;a<S;++a){
        int b=rows[a][0],bb=rows[b][0];
        if((a&bb)!=a)return;                 // double-negation inflation
    }
    ++total_F;
    int edge=0,bit=0;
    for(int i=0;i<3;++i)for(int j=i+1;j<3;++j,++bit){
        bool ij=(rows[1<<i][0] & (1<<j));
        bool ji=(rows[1<<j][0] & (1<<i));
        assert(ij==ji);                      // independently checks graph symmetry
        if(ij)edge|=1<<bit;
    }
    for(int a=0;a<S;++a){                    // graph really reconstructs negation
        int n=W;
        for(int i=0;i<3;++i)if(a&(1<<i))n&=rows[1<<i][0];
        assert(rows[a][0]==n);
    }
    ++by_graph[edge];
    constexpr array<array<int,3>,6> perms{{
        {{0,1,2}},{{0,2,1}},{{1,0,2}},{{1,2,0}},{{2,0,1}},{{2,1,0}}}};
    for(int pi=0;pi<6;++pi){
        const auto&p=perms[pi];bool invariant=true;
        for(int a=0;a<S && invariant;++a)for(int b=0;b<S;++b){
            int pa=mask_perm(a,p),pb=mask_perm(b,p);
            if(arr(pa,pb)!=mask_perm(arr(a,b),p)){invariant=false;break;}
        }
        fixcounts[pi]+=invariant;
    }
}
void enumer(int a){
    if(a==S){examine();return;}
    for(const auto&r:options[a]){rows[a]=r;enumer(a+1);}
}
int main(){
    for(int a=0;a<S;++a)make_rows(a);
    enumer(0);
    assert(total_T==7820);
    assert(total_F==1021);
    constexpr array<uint64_t,8> graph_counts{{729,81,81,16,81,16,16,1}};
    assert(by_graph==graph_counts);
    constexpr array<uint64_t,6> fix_counts{{1021,41,41,10,10,41}};
    assert(fixcounts==fix_counts);
    uint64_t sum=0;for(auto x:fixcounts)sum+=x;
    assert(sum%6==0 && sum/6==194);
    cout<<"DIRECT_CENSUS_OK T="<<total_T<<" F="<<total_F
        <<" graph_counts=729,81,81,16,81,16,16,1"
        <<" fixed_points=1021,41,41,10,10,41"
        <<" isomorphism_classes="<<sum/6<<"\n";
}
