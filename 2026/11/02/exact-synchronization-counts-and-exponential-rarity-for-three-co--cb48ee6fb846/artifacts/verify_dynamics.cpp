// Exhaustive direct dynamics and independent reverse functional-graph check.
// C++17; compile with g++ -O2 -std=c++17 verify_dynamics.cpp -o check.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <vector>
using namespace std;

struct Graph {
    int m, n, N;
    vector<vector<int>> neighbor;
    explicit Graph(int rows, int cols) : m(rows), n(cols), N(rows*cols), neighbor(N) {
        for (int i=0;i<m;i++) for (int j=0;j<n;j++) {
            int u=i*n+j;
            for (int k=0;k<n;k++) if (k!=j) neighbor[u].push_back(i*n+k);
            for (int k=0;k<m;k++) if (k!=i) neighbor[u].push_back(k*n+j);
        }
    }
    uint32_t update(uint32_t code, const vector<uint32_t>& pow3) const {
        vector<int> color(N);
        for(int i=0;i<N;i++) {color[i]=code%3;code/=3;}
        uint32_t next=0;
        for(int i=0;i<N;i++) {
            int successor=(color[i]+1)%3;
            bool changes=false;
            for(int j:neighbor[i]) if(color[j]==successor) {changes=true;break;}
            next+=(changes?successor:color[i])*pow3[i];
        }
        return next;
    }
    bool constant(uint32_t code) const {
        int d=code%3;
        for (int i=0;i<N;i++) {if ((code%3)!=d) return false;code/=3;}
        return true;
    }
};

int main() {
    for(auto dims: vector<pair<int,int>>{{2,2},{2,3},{2,4},{2,5},{2,6},{3,3},{3,4}}) {
        int m=dims.first,n=dims.second;
        Graph g(m,n);
        vector<uint32_t> pow3(g.N+1,1);
        for(int i=1;i<=g.N;i++)pow3[i]=pow3[i-1]*3;
        uint32_t S=pow3[g.N];
        vector<uint32_t> f(S);
        vector<vector<uint32_t>> incoming(S);
        for(uint32_t x=0;x<S;x++){
            f[x]=g.update(x,pow3);
            incoming[f[x]].push_back(x);
        }
        // Route A: exactly two explicit updates, independent of basin enumeration.
        uint32_t by_two=0, entry0=0, entry1=0, entry2=0;
        for(uint32_t x=0;x<S;x++) {
            if(g.constant(x)) entry0++;
            else if(g.constant(f[x])) entry1++;
            else if(g.constant(f[f[x]])) entry2++;
            if(g.constant(f[f[x]]))by_two++;
        }
        // Route B: all predecessors of the three constant terminal states.
        vector<uint8_t> seen(S,0);
        queue<uint32_t> q;
        for(int col=0;col<3;col++){
            uint32_t code=0;
            for(int i=0;i<g.N;i++)code+=col*pow3[i];
            q.push(code);seen[code]=1;
        }
        uint32_t basin=3;
        while(!q.empty()){
            auto y=q.front();q.pop();
            for(auto x:incoming[y]) if(!seen[x]){
                seen[x]=1;q.push(x);basin++;
            }
        }
        if(basin!=by_two || entry0+entry1+entry2!=basin)
            throw runtime_error("a synchronizing orbit enters after time two");
        cout<<"m="<<m<<" n="<<n<<" states="<<S<<" sync="<<basin
            <<" entry0="<<entry0<<" entry1="<<entry1
            <<" entry2="<<entry2<<" basin_equals_two_step=YES\n";
    }
    cout<<"ALL_DYNAMIC_CHECKS_PASS\n";
}
