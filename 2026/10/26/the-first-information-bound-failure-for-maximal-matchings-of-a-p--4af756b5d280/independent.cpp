// Independent enumeration and minimax algorithm for maximal matchings of paths.
// C++17, no external libraries. Vertex i of the line graph represents path edge i.
#include <bits/stdc++.h>
using namespace std;
using B=bitset<128>;
vector<unsigned int> patterns;
vector<B> columns;
unordered_map<string,int> memo;
int m;
void generate(int i, unsigned int state) {
    if(i==m) {
        // Every zero edge must touch a selected edge: maximality.
        for(int j=0;j<m;j++) if(!(state&(1u<<j))) {
            bool neigh=(j>0 && (state&(1u<<(j-1)))) ||
                       (j+1<m && (state&(1u<<(j+1))));
            if(!neigh) return;
        }
        patterns.push_back(state);
        return;
    }
    generate(i+1,state);
    if(i==0 || !(state&(1u<<(i-1)))) generate(i+1,state|(1u<<i));
}
int solve(const B &S){
    string key=S.to_string();
    auto it=memo.find(key);
    if(it!=memo.end())return it->second;
    int best=0;
    for(const auto &Q:columns){
        B a=S&Q,b=S&~Q;
        if(a.any()&&b.any()) best=max(best,1+min(solve(a),solve(b)));
    }
    memo.emplace(key,best);
    return best;
}
int main(){
    for(m=0;m<=15;m++){
        patterns.clear();memo.clear();generate(0,0);
        if(patterns.size()>128)return 2;
        columns.assign(m,B{});
        B all;
        for(size_t t=0;t<patterns.size();t++){
            all.set(t);
            for(int i=0;i<m;i++) if(patterns[t]&(1u<<i))columns[i].set(t);
        }
        int val=solve(all);
        cout<<m<<","<<patterns.size()<<","<<val<<","<<memo.size()<<"\n";
        if(m<=14 && val != (int)(floor(log2(patterns.size()))))return 3;
        if(m==15 && (patterns.size()!=65 || val!=5))return 4;
    }
    cout<<"CPP_INDEPENDENT_PASS\n";
}
