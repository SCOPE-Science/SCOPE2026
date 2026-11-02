// Independent cyclic-composition generation and direct exchange-graph enumeration.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

long long gaps_count(int sum,int count) {
    if (count==0) return sum==0 ? 1 : 0;
    if (sum<3*count || sum>5*count) return 0;
    vector<long long> cur(sum+1,0),next(sum+1,0);cur[0]=1;
    for(int i=0;i<count;i++){
        fill(next.begin(),next.end(),0);
        for(int t=0;t<=sum;t++) if(cur[t])
            for(int d=3;d<=5;d++) if(t+d<=sum)next[t+d]+=cur[t];
        cur.swap(next);
    }
    return cur[sum];
}

void generate(int n,int k,int at,int sum,vector<int>&g,unordered_set<uint64_t>&out) {
    if (at==k) {
        if(sum!=n)return;
        for(int start=0;start<n;start++){
            uint64_t mask=0;int x=start;
            for(int i=0;i<k;i++) {
                mask|=uint64_t(1)<<x;
                x=(x+g[i])%n;
            }
            assert(x==start);
            out.insert(mask);
        }
        return;
    }
    for(int v=3;v<=5;v++) {
        if(sum+v+3*(k-at-1)>n ||sum+v+5*(k-at-1)<n)continue;
        g[at]=v; generate(n,k,at+1,sum+v,g,out);
    }
}

void verify(int n,int k){
    vector<int>g(k);
    unordered_set<uint64_t>unique;
    generate(n,k,0,0,g,unique);
    vector<uint64_t>v(unique.begin(),unique.end());
    sort(v.begin(),v.end());
    int m=(int)v.size();
    assert(m==(long long)n*gaps_count(n,k)/k);
    unordered_map<uint64_t,int>id;
    for(int i=0;i<m;i++)id[v[i]]=i;
    vector<vector<int>>adj(m);
    for(int i=0;i<m;i++) {
        for(int a=0;a<n;a++)if((v[i]>>a)&1ULL){
            for(int b=0;b<n;b++)if(!((v[i]>>b)&1ULL)){
                uint64_t t=v[i]^(uint64_t(1)<<a)^(uint64_t(1)<<b);
                auto it=id.find(t);
                if(it!=id.end())adj[i].push_back(it->second);
            }
        }
        sort(adj[i].begin(),adj[i].end());
        auto end=unique_copy(adj[i].begin(),adj[i].end(),adj[i].begin());
        adj[i].erase(end,adj[i].end());
    }
    long long degsum=0,triangles=0;
    for(int i=0;i<m;i++) {
        assert(adj[i].size()%2==0);
        degsum+=adj[i].size();
        for(int j:adj[i])if(i<j){
            assert(binary_search(adj[j].begin(),adj[j].end(),i));
            for(int z:adj[j])if(z>j && binary_search(adj[i].begin(),adj[i].end(),z))triangles++;
        }
    }
    long long edges=degsum/2;
    long long expected_edges=(long long)n*(gaps_count(n-7,k-2)+3*gaps_count(n-8,k-2)+gaps_count(n-9,k-2));
    assert(edges==expected_edges);
    assert(triangles==(long long)n*gaps_count(n-8,k-2));
    vector<char>seen(m,0);vector<int>components;
    for(int i=0;i<m;i++)if(!seen[i]){
        queue<int>q;seen[i]=1;q.push(i);int count=0;
        while(!q.empty()){
            int a=q.front();q.pop();count++;
            for(int b:adj[a])if(!seen[b]){seen[b]=1;q.push(b);}
        }
        components.push_back(count);
    }
    int excess=n-3*k;
    if(excess==0){assert(m==3);assert(components.size()==3);assert(edges==0);}
    else if(excess==2*k){assert(m==5);assert(components.size()==5);assert(edges==0);}
    else {
        assert(components.size()==1);
        if(excess==1||excess==2*k-1){
            assert(m==n);assert(edges==n);assert(triangles==0);
            for(auto a:adj)assert(a.size()==2);
        }else assert(triangles>0);
    }
    cout<<n<<' '<<k<<' '<<m<<' '<<edges<<' '<<triangles<<' '<<components.size()<<'\n';
}
int main(){
    int t=0;
    for(int n=7;n<=27;n++)
        for(int k=(n+4)/5;k<=n/3;k++){
            verify(n,k);t++;
        }
    cout<<"INDEPENDENT_GAP_EXCHANGE_PASS "<<t<<'\n';
}
