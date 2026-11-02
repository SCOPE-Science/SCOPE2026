// Exhaustive exact certificate for optimal-pebbling transfer graphs of the Heawood graph.
// Compile: g++ -O2 -std=c++17 verify_primary.cpp -o verify_primary && ./verify_primary
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int V=14, MAXT=8;
using State=array<unsigned char,V>;
using Code=uint64_t;
array<vector<int>,V> adj;
unordered_map<Code,uint16_t> reach;
State state{};
Code encode(const State& x){ Code code=0;for(int v:x)code=9*code+v;return code; }
// The recursion is exact: each legal pebbling move reduces total pebble count by one.
uint16_t mask(State &x) {
    Code code=encode(x);
    auto it=reach.find(code);
    if(it!=reach.end())return it->second;
    uint16_t m=0;
    for(int i=0;i<V;i++)if(x[i])m|=uint16_t(1)<<i;
    for(int i=0;i<V;i++)if(x[i]>=2){
        x[i]-=2;
        for(int j:adj[i]){
            x[j]++;m|=mask(x);x[j]--;
            if(m==((1<<V)-1))break;
        }
        x[i]+=2;
        if(m==((1<<V)-1))break;
    }
    reach.emplace(code,m);
    return m;
}
vector<State> good;
uint64_t checked=0;
void compositions(int pos,int remain){
    if(pos==V-1){
        state[pos]=remain;
        checked++;
        if(mask(state)==(1<<V)-1)good.push_back(state);
        return;
    }
    for(int a=0;a<=remain;a++){
        state[pos]=a;
        compositions(pos+1,remain-a);
    }
}
struct DSU{
  vector<int> p,s;
  DSU(int n):p(n),s(n,1){iota(p.begin(),p.end(),0);}
  int find(int i){while(i!=p[i]){p[i]=p[p[i]];i=p[i];}return i;}
  void join(int a,int b){a=find(a);b=find(b);if(a!=b){p[a]=b;s[b]+=s[a];}}
  vector<pair<int,int>> sizes(){
      vector<int> v;for(int i=0;i<(int)p.size();i++)if(i==find(i))v.push_back(s[i]);
      sort(v.begin(),v.end());vector<pair<int,int>> a;
      for(int x:v){if(!a.empty()&&a.back().first==x)a.back().second++;else a.push_back({x,1});}
      return a;
  }
};
string component_signature(const vector<pair<int,int>>& v){
    string s;for(auto [size,count]:v){if(!s.empty())s+=";";s+=to_string(size)+"x"+to_string(count);}return s;
}
void report(int t,uint64_t expected_checked,size_t expected_good,
    long long expected_jump_edges,const string &expect_jump_comps,
    long long expected_slide_edges,const string &expect_slide_comps){
    good.clear();checked=0;
    compositions(0,t);
    assert(checked==expected_checked && good.size()==expected_good);
    unordered_map<Code,int> ids;ids.reserve(good.size()*2);
    for(int i=0;i<(int)good.size();i++)ids.emplace(encode(good[i]),i);
    DSU jump(good.size()),slide(good.size());
    long long ej=0,es=0;
    for(int i=0;i<(int)good.size();i++){
        State tmp=good[i];
        for(int u=0;u<V;u++)if(tmp[u]){
            tmp[u]--;
            for(int v=0;v<V;v++)if(v!=u){
                tmp[v]++;
                auto it=ids.find(encode(tmp));
                if(it!=ids.end() && i<it->second){
                    ej++;jump.join(i,it->second);
                }
                tmp[v]--;
            }
            for(int v:adj[u]){
                tmp[v]++;
                auto it=ids.find(encode(tmp));
                if(it!=ids.end() && i<it->second){
                    es++;slide.join(i,it->second);
                }
                tmp[v]--;
            }
            tmp[u]++;
        }
    }
    string sj=component_signature(jump.sizes()),ss=component_signature(slide.sizes());
    cout<<"T="<<t<<" all_distributions="<<checked<<" solvable="<<good.size()
        <<" jump_edges="<<ej<<" jump_components="<<sj
        <<" slide_edges="<<es<<" slide_components="<<ss<<"\n";
    assert(ej==expected_jump_edges && sj==expect_jump_comps);
    assert(es==expected_slide_edges && ss==expect_slide_comps);
    if(t==6){
        int a=0,b=0,c=0;
        for(const State &x:good){
            vector<int> entries;
            for(int z:x)if(z)entries.push_back(z);
            sort(entries.rbegin(),entries.rend());
            if(entries==vector<int>({4,2}))a++;
            else if(entries==vector<int>({4,1,1}))b++;
            else if(entries==vector<int>({3,3}))c++;
            else assert(false);
        }
        assert(a==98 && b==42 && c==21);
        cout<<"OPTIMUM_PROFILES_OK (4,2):"<<a<<" (4,1,1):"<<b<<" (3,3):"<<c<<"\n";
    }
    if(t==7){
        int bounded=0,heavy=0;
        unordered_map<int,int> group_max;
        for(int i=0;i<(int)good.size();i++){
            bool is_bounded=*max_element(good[i].begin(),good[i].end())<=2;
            if(is_bounded)bounded++;else heavy++;
            int root=jump.find(i);
            int label=is_bounded?1:2;
            assert(!group_max.count(root) || group_max[root]==label);
            group_max[root]=label;
        }
        assert(bounded==2576 && heavy==3360 && group_max.size()==2);
        cout<<"CAPACITY_BARRIER_OK size_7_bounded="<<bounded<<" heavy="<<heavy<<"\n";
    }
}
int main(){
    // Points 0,...,6; lines {i,i+1,i+3} mod 7 (the cyclic Fano plane).
    for(int i=0;i<7;i++)for(int j:{i,(i+1)%7,(i+3)%7}){
        adj[j].push_back(7+i);adj[7+i].push_back(j);
    }
    for(auto &n:adj)assert(n.size()==3);
    reach.reserve(500000);
    report(5,8568,0,0,"",0,"");
    report(6,27132,161,42,"1x98;3x21",42,"1x98;3x21");
    report(7,77520,5936,33726,"2576x1;3360x1",11970,"24x21;74x28;3360x1");
    report(8,203490,71323,1145396,"71323x1",314496,"71323x1");
    cout<<"EXHAUSTIVE_PRIMARY_OK cached_states="<<reach.size()<<"\n";
}
