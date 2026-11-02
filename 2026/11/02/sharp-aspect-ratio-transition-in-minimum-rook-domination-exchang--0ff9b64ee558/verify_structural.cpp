// Exhaustive finite corroboration for rook minimum-domination exchange graphs.
// Compile: c++ -O2 -std=c++17 verify_structural.cpp -o verify_structural
#include <bits/stdc++.h>
using namespace std;
using U=unsigned long long;

void check(int n){
    int total=1;
    for(int i=0;i<n;i++) total*=n;
    vector<U> states;
    unordered_map<U,int> ids;
    map<vector<int>,int> representatives;
    auto insert=[&](U mask){
        auto p=ids.emplace(mask,(int)states.size());
        if(p.second) states.push_back(mask);
        return p.first->second;
    };
    for(int k=0;k<total;k++){
        int x=k; U mask=0; vector<int> freq(n);
        for(int i=0;i<n;i++){
            int j=x%n; x/=n; mask|=1ULL<<(i*n+j);freq[j]++;
        }
        int idx=insert(mask);
        sort(freq.begin(),freq.end(),greater<int>());
        while(!freq.empty() && freq.back()==0) freq.pop_back();
        representatives.emplace(freq,idx);
    }
    for(int k=0;k<total;k++){
        int x=k; U mask=0;
        for(int j=0;j<n;j++){
            int i=x%n; x/=n; mask|=1ULL<<(i*n+j);
        }
        insert(mask);
    }
    int fact=1;
    for(int i=2;i<=n;i++) fact*=i;
    assert(states.size()==(size_t)(2*total-fact));
    vector<vector<int>> adj(states.size());
    long long sumdeg=0;
    map<int,int> degreecounts;
    for(int a=0;a<(int)states.size();a++){
        U mask=states[a]; auto &nbs=adj[a];
        for(U rem=mask;rem;rem&=rem-1){
            U bit=rem&-rem; U smaller=mask^bit;
            for(int j=0;j<n*n;j++){
                U added=1ULL<<j;
                if(added==bit || (smaller&added)) continue;
                auto q=ids.find(smaller|added);
                if(q!=ids.end())nbs.push_back(q->second);
            }
        }
        sort(nbs.begin(),nbs.end());
        nbs.erase(unique(nbs.begin(),nbs.end()),nbs.end());
        for(int b:nbs) assert(b!=a);
        sumdeg+=nbs.size();degreecounts[nbs.size()]++;
    }
    long long expected=1LL*n*(n-1)*total+1LL*fact*n*(n-1)*(n-1);
    assert(sumdeg==2*expected);
    for(int a=0;a<(int)states.size();a++)
       for(int b:adj[a])assert(binary_search(adj[b].begin(),adj[b].end(),a));
    int radius=INT_MAX,diameter=0;
    map<vector<int>,int> orbit_ecc;
    for(auto [partition,start]:representatives){
        vector<int> d(states.size(),-1), q(states.size());
        int head=0,tail=0;q[tail++]=start;d[start]=0;
        while(head<tail){
            int v=q[head++];
            for(int w:adj[v])if(d[w]==-1){d[w]=d[v]+1;q[tail++]=w;}
        }
        assert(tail==(int)states.size());
        int e=*max_element(d.begin(),d.end());
        radius=min(radius,e);diameter=max(diameter,e);orbit_ecc[partition]=e;
    }
    int radtarget=n,diamtarget=max(n,2*n-3);
    assert(radius==radtarget && diameter==diamtarget);
    cout<<"STRUCTURAL_PASS n="<<n<<" vertices="<<states.size()<<" edges="<<expected
        <<" radius="<<radius<<" diameter="<<diameter<<" degree_classes="<<degreecounts.size()
        <<" orbit_ecc={";
    for(auto [p,e]:orbit_ecc){cout<<"[";for(int t:p)cout<<t<<",";cout<<"]:"<<e<<";";}
    cout<<"}\n";
}
int main(){for(int n=2;n<=6;n++)check(n);cout<<"ROOK_STRUCTURAL_PASS\n";}
