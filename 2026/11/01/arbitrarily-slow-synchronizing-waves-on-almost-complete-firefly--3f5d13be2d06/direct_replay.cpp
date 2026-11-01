// Standalone vertex-level finite replay; does not assume the symbolic wave identity.
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    long long trials=0, updates=0;
    for(int r: {1,2,4,9,33}) for(int n=2;n<=48;++n) for(int a=1;a<n;++a){
        int b=n-a-1, N=r+n;
        vector<vector<int>> adj(N);
        auto edge=[&](int i,int j){adj[i].push_back(j);adj[j].push_back(i);};
        for(int i=0;i<r;++i)for(int j=i+1;j<r;++j)edge(i,j);
        for(int i=0;i<r;++i)for(int j=r;j<N;++j)edge(i,j);
        for(int j=r;j<N-1;++j)edge(j,j+1);
        vector<int> s(N,2);
        s[r+a]=0;
        for(int j=r+a+1;j<N;++j)s[j]=1;
        int initialDelay=-1;
        for(int t=0;t<=3*(b+1);++t){
            bool sync=true;
            for(int j=1;j<N;++j)if(s[j]!=s[0])sync=false;
            if(sync){initialDelay=t;break;}
            vector<int> next=s;
            for(int i=0;i<N;++i){
                bool blink=false;
                for(int j:adj[i])blink |= (s[j]==1);
                if(s[i]!=2 || !blink)next[i]=(s[i]+1)%3;
            }
            s.swap(next);updates++;
        }
        if(initialDelay!=3*(b+1)){
          cerr<<"FAIL r="<<r<<" n="<<n<<" a="<<a<<" t="<<initialDelay<<"\n";return 1;
        }
        trials++;
    }
    cout<<"PASS: "<<trials<<" graph/initial-state cases; "<<updates<<" individual graph updates; independent adjacency-list simulator.\n";
    cout<<"Finite instances corroborate but do not prove the all-parameter statement.\n";
}
