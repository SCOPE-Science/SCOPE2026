// Exact cyclic discrepancy census by edge-simple Eulerian depth-first search.
// Compile: c++ -O2 -std=c++17 verify_dfs.cpp -o verify_dfs
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct Census {
    int n=0, L=0;
    vector<vector<int>> edge, outgoing;
    vector<int> word;
    map<int,uint64_t> histogram;
    map<int,string> witnesses;
    static int code(const vector<int>& a,int from,int to) {
        int v=0;for(int j=from;j<to;++j)v=3*v+a[j];return v;
    }
    static int power3(int n) {int x=1;while(n--)x*=3;return x;}
    explicit Census(int order):n(order) {
        for(int v=0;v<power3(n);v++) {
            int x=v;vector<int> a(n);
            for(int j=n-1;j>=0;j--){a[j]=x%3;x/=3;}
            bool proper=true;
            for(int j=1;j<n;j++)if(a[j]==a[j-1])proper=false;
            if(proper)edge.push_back(a);
        }
        L=int(edge.size()); assert(L==3*(1<<(n-1)));
        outgoing.resize(power3(n-1));
        for(int e=0;e<L;e++)outgoing[code(edge[e],0,n-1)].push_back(e);
        for(auto& os:outgoing) if(!os.empty()) assert(os.size()==2);
    }
    void traverse(uint64_t used,int vertex,int depth, array<int,3> bal,
                  array<int,3> low,array<int,3> high) {
        if(depth==L) {
            if(vertex!=code(edge[0],0,n-1))return;
            assert(bal[0]==0 && bal[1]==0 && bal[2]==0);
            int disc=0;
            for(int p=0;p<3;p++)disc=max(disc,high[p]-low[p]);
            ++histogram[disc];
            if(!witnesses.count(disc)) {
                string s;for(int x:word)s+=char('0'+x);
                witnesses[disc]=s;
            }
            return;
        }
        for(int e:outgoing[vertex]) {
            if(used&(uint64_t(1)<<e))continue;
            int c=edge[e][0];
            auto b=bal,lo=low,hi=high;
            b[0]+=(c==0)-(c==1);
            b[1]+=(c==0)-(c==2);
            b[2]+=(c==1)-(c==2);
            for(int p=0;p<3;p++){
                lo[p]=min(lo[p],b[p]);hi[p]=max(hi[p],b[p]);
            }
            word.push_back(c);
            traverse(used|(uint64_t(1)<<e),code(edge[e],1,n),depth+1,b,lo,hi);
            word.pop_back();
        }
    }
    void run(){
        int c=edge[0][0];
        array<int,3> bal{int(c==0)-int(c==1),int(c==0)-int(c==2),int(c==1)-int(c==2)};
        array<int,3>lo{min(0,bal[0]),min(0,bal[1]),min(0,bal[2])};
        array<int,3>hi{max(0,bal[0]),max(0,bal[1]),max(0,bal[2])};
        word={c};
        traverse(1,code(edge[0],1,n),1,bal,lo,hi);
    }
};

int main(){
    const vector<map<int,uint64_t>> expected={
        {{2,3}},{{2,12}},{{3,384}},{{3,23700},{4,420924},{5,341808}}
    };
    for(int n=2;n<=5;n++){
        Census c(n);c.run();
        if(c.histogram!=expected[n-2]){
            cerr<<"FAIL order="<<n<<"\n";return 1;
        }
        uint64_t total=0;
        for(auto [d,v]:c.histogram)total+=v;
        cout<<"ORDER "<<n<<" EDGES "<<c.L<<" CYCLES "<<total;
        for(auto [d,v]:c.histogram)cout<<" D"<<d<<"="<<v;
        cout<<"\n";
        if(n==5)for(auto [d,w]:c.witnesses)cout<<"WITNESS "<<d<<" "<<w<<"\n";
    }
    cout<<"VERIFY_DFS_OK\n";
}
