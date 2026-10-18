// Exact finite enumeration of cyclic covers of binary reverse-complement palindromes.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify_antipal
// Run:   ./verify_antipal
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <queue>
#include <string>
#include <vector>
using namespace std;
struct Answer { int length; uint64_t rooted; string witness; int visited; };
string bits(int x,int k){string s(k,'0');for(int i=k-1;i>=0;i--){s[i]=char('0'+(x&1));x>>=1;}return s;}
vector<int> patterns(int m){
    int k=2*m; vector<int> p;
    for(int e=0;e<(1<<k);++e){
        bool anti=true;
        for(int i=0;i<m;++i)if(((e>>i)&1)==((e>>(k-i-1))&1))anti=false;
        if(anti)p.push_back(e);
    }
    assert((int)p.size()==(1<<m));return p;
}
bool covers(const string& s,int m){
    int k=2*m, n=(int)s.size(); if(n<k)return false;
    vector<unsigned char> seen(1<<k,0);
    for(int i=0;i<n;++i){int x=0;for(int j=0;j<k;++j)x=2*x+s[(i+j)%n]-'0';seen[x]=1;}
    for(int p:patterns(m))if(!seen[p])return false;
    return true;
}
Answer exact_state_bfs(int m){
    int k=2*m,V=1<<(k-1),B=1<<(1<<m),full=B-1;
    vector<int> list=patterns(m),where(1<<k,-1);
    for(int j=0;j<(int)list.size();++j)where[list[j]]=j;
    int p=list[0], origin=p>>1, destination=p&(V-1),firstmask=1<<where[p];
    int nstates=B*V,source=firstmask*V+destination;
    vector<int16_t> distance(nstates,-1);
    vector<uint64_t> count(nstates,0);
    vector<int32_t> pred(nstates,-1);
    queue<int32_t> frontier;
    distance[source]=1;count[source]=1;frontier.push(source);
    int goal=-1, visited=1;
    while(!frontier.empty()){
        int state=frontier.front();frontier.pop();
        int mask=state/V,v=state%V;
        if(mask==full&&v==origin){goal=state;break;}
        for(int b=0;b<2;++b){
            int edge=2*v+b;
            int nextmask=mask|(where[edge]<0?0:(1<<where[edge]));
            int next=nextmask*V+(edge&(V-1));
            if(distance[next]<0){
                distance[next]=distance[state]+1;
                count[next]=count[state];pred[next]=state;
                frontier.push(next);++visited;
            } else if(distance[next]==distance[state]+1){
                assert(count[next]<=numeric_limits<uint64_t>::max()-count[state]);
                count[next]+=count[state];
            }
        }
    }
    assert(goal>=0);
    vector<int> appended;
    for(int x=goal;x!=source;x=pred[x]){assert(x>=0); appended.push_back((x%V)&1);}
    reverse(appended.begin(),appended.end());
    string total=bits(origin,k-1); // explicit source prefix
    total+=char('0'+(p&1));
    for(int b:appended)total+=char('0'+b);
    assert(total.size()==(size_t)(distance[goal]+k-1));
    assert(total.substr(0,k)==bits(p,k));
    assert(total.substr(distance[goal],k-1)==bits(origin,k-1));
    string witness=total.substr(0,distance[goal]);
    assert(covers(witness,m));
    return {distance[goal],count[goal],witness,visited};
}
int overlap_tsp(int m){
    int k=2*m;vector<int> ints=patterns(m);
    int n=(int)ints.size(),full=(1<<n)-1;
    vector<string> s;for(int x:ints)s.push_back(bits(x,k));
    vector<vector<int>> d(n,vector<int>(n,k));
    for(int i=0;i<n;++i)for(int j=0;j<n;++j){
        if(i==j)continue;
        for(int overlap=k-1;overlap>=0;--overlap){
            if(s[i].substr(k-overlap)==s[j].substr(0,overlap)){
                d[i][j]=k-overlap;break;
            }
        }
    }
    const int INF=1000000;
    vector<int> dp((1<<n)*n,INF);
    dp[n]=0; // mask=1, end=0
    for(int mask=1;mask<=full;mask+=2){
        for(int last=0;last<n;++last)if(mask&(1<<last)){
            int z=dp[mask*n+last];if(z==INF)continue;
            for(int next=1;next<n;++next)if(!(mask&(1<<next))){
                int idx=(mask|(1<<next))*n+next;
                dp[idx]=min(dp[idx],z+d[last][next]);
            }
        }
    }
    int best=INF;
    for(int last=1;last<n;++last)best=min(best,dp[full*n+last]+d[last][0]);
    if(n==2)assert(best==2);
    return best;
}
int main(){
    const int expected_length[]={0,2,9,26,67};
    const uint64_t expected_rooted[]={0,1,2,14,1232};
    for(int m=1;m<=4;++m){
        Answer a=exact_state_bfs(m);
        int independent=overlap_tsp(m);
        assert(a.length==expected_length[m]);
        assert(a.rooted==expected_rooted[m]);
        assert(independent==a.length);
        assert(a.witness.size()==(size_t)a.length);
        assert(a.witness.substr(0,2*m)==bits(patterns(m)[0],2*m));
        cout<<"k="<<2*m<<" patterns="<<(1<<m)<<" C="<<a.length<<" rooted="<<a.rooted
            <<" visited="<<a.visited<<" independent_overlap="<<independent<<" witness="<<a.witness<<'\n';
    }
    cout<<"VERIFY_OK antipal_cover_k=2,4,6,8 independent_overlap_TSP_and_rooted_BFS\n";
}
