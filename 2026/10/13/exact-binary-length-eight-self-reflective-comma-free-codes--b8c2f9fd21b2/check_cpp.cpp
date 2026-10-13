// Exhaustive integer-bit implementation of reversal-closed binary comma-free codes.
// Uses overlap masks and pivoted Bron--Kerbosch, independently of the string checker.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
static constexpr int N=8, MASK=(1<<N)-1;
static vector<vector<int>> groups;
static vector<uint64_t> adj;
static int maximal=0,pairwise_best=0,pairwise_opt=0,true_best=0;
static set<string> opt;

int rev(int x) {int r=0;for(int j=0;j<N;j++){r=(r<<1)|(x&1);x>>=1;}return r;}
string bits(int x) {string t;for(int j=N-1;j>=0;j--)t.push_back('0'+((x>>j)&1));return t;}
bool valid(const vector<int>& s) {
    bool contains[1<<N]={};
    for(int x:s)contains[x]=true;
    for(int x:s)for(int y:s)for(int j=1;j<N;j++)
        if(contains[(((x<<N)|y)>>(N-j))&MASK])return false;
    return true;
}
string code_line(const vector<int>& chosen) {
    vector<string> all;
    for(int i:chosen)for(int x:groups[i])all.push_back(bits(x));
    sort(all.begin(),all.end());
    string s;
    for(size_t j=0;j<all.size();j++){if(j)s+=',';s+=all[j];}
    return s;
}
void bron(vector<int>& chosen,uint64_t P,uint64_t X,int weight) {
    if(!P&&!X) {
        ++maximal;
        if(weight>pairwise_best){pairwise_best=weight;pairwise_opt=0;}
        if(weight==pairwise_best)++pairwise_opt;
        vector<int> all;
        for(int v:chosen)for(int x:groups[v])all.push_back(x);
        if(valid(all)) {
            string line=code_line(chosen);
            if(weight>true_best){true_best=weight;opt.clear();opt.insert(line);}
            else if(weight==true_best)opt.insert(line);
        }
        return;
    }
    uint64_t px=P|X;
    int pivot=-1, maxcnt=-1;
    while(px){int u=__builtin_ctzll(px);px&=px-1;
        int cnt=__builtin_popcountll(P&adj[u]);
        if(cnt>maxcnt){maxcnt=cnt;pivot=u;}
    }
    uint64_t candidates=P & ~(pivot<0?0:adj[pivot]);
    while(candidates){int v=__builtin_ctzll(candidates);uint64_t b=uint64_t(1)<<v;
        candidates&=~b;
        chosen.push_back(v);
        bron(chosen,P&adj[v],X&adj[v],weight+(int)groups[v].size());
        chosen.pop_back();
        P&=~b; X|=b;
    }
}
int main(){
    for(int x=0;x<(1<<N);x++){
        int y=rev(x);
        if(x<=y){vector<int> g={x};if(x!=y)g.push_back(y);
            if(valid(g))groups.push_back(g);
        }
    }
    assert(groups.size()<64);
    adj.assign(groups.size(),0);
    int edges=0,single=0,pair=0;
    for(size_t i=0;i<groups.size();i++){
        if(groups[i].size()==1)++single;else ++pair;
        for(size_t j=0;j<i;j++){
            vector<int> both=groups[i];
            both.insert(both.end(),groups[j].begin(),groups[j].end());
            if(valid(both)){
                adj[i]|=uint64_t(1)<<j;
                adj[j]|=uint64_t(1)<<i;
                ++edges;
            }
        }
    }
    vector<int> chosen;
    bron(chosen,(uint64_t(1)<<groups.size())-1,0,0);
    ostringstream ss;
    ss<<"N_GROUPS="<<groups.size()<<" SINGLE_GROUPS="<<single
      <<" PAIR_GROUPS="<<pair<<" COMPAT_EDGES="<<edges
      <<" MAXIMAL="<<maximal<<" PAIRWISE_MAX="<<pairwise_best
      <<" PAIRWISE_OPT="<<pairwise_opt<<" TRUE_MAX="<<true_best
      <<" TRUE_OPT="<<opt.size()<<'\n';
    for(const string& line:opt)ss<<line<<'\n';
    string out=ss.str();
    assert(groups.size()==56&&single==12&&pair==44&&edges==929);
    assert(maximal==2107&&pairwise_best==18&&pairwise_opt==16
           &&true_best==18&&opt.size()==12);
    cout<<out;
}
