#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;

static constexpr int N=8, M=28, K=9;
vector<pair<int,int>> E;
array<uint8_t,N> A{};
array<int,N> D{};

bool connected(){
    uint8_t seen=1, front=1;
    while(front){
        uint8_t next=0;
        for(int v=0;v<N;v++) if(front&(1u<<v)) next |= A[v];
        next &= (uint8_t)~seen; seen |= next; front=next;
    }
    return seen==0xff;
}

bool has_simple_path_len(int s,int t,int L){
    struct S{uint8_t v,d,seen;};
    S st[512]; int top=0; st[top++]={(uint8_t)s,0,(uint8_t)(1u<<s)};
    while(top){
        S q=st[--top];
        if(q.d==L){ if(q.v==t) return true; continue; }
        uint8_t nb=A[q.v] & (uint8_t)~q.seen;
        for(int w=0;w<N;w++) if(nb&(1u<<w)){
            if(w==t && q.d+1<L) continue;
            st[top++]={(uint8_t)w,(uint8_t)(q.d+1),(uint8_t)(q.seen|(1u<<w))};
        }
    }
    return false;
}

bool forbidden_cycle_free(){
    // Enumerate each simple cycle with its least vertex as the start.
    for(int s=0;s<N;s++){
        struct S{uint8_t v,d,seen;};
        S st[512]; int top=0; st[top++]={(uint8_t)s,0,(uint8_t)(1u<<s)};
        while(top){
            S q=st[--top];
            if(q.d>=3 && q.d<=5 && (A[q.v]&(1u<<s))) return false; // C4,C5,C6
            if(q.d==5) continue;
            uint8_t nb=A[q.v] & (uint8_t)~q.seen;
            for(int w=s+1;w<N;w++) if(nb&(1u<<w))
                st[top++]={(uint8_t)w,(uint8_t)(q.d+1),(uint8_t)(q.seen|(1u<<w))};
        }
    }
    return true;
}

bool saturated(){
    for(int u=0;u<N;u++) for(int v=u+1;v<N;v++) if(!(A[u]&(1u<<v))){
        if(!(has_simple_path_len(u,v,3)||has_simple_path_len(u,v,4)||has_simple_path_len(u,v,5)))
            return false;
    }
    return true;
}

uint32_t relabel_mask(const array<int,N>& lab){
    uint32_t z=0;
    for(int i=0;i<M;i++){
        auto [u,v]=E[i]; if(!(A[u]&(1u<<v))) continue;
        int x=lab[u], y=lab[v]; if(x>y) swap(x,y);
        int idx=0;
        for(int a=0;a<N;a++) for(int b=a+1;b<N;b++,idx++) if(a==x && b==y) z|=(1u<<idx);
    }
    return z;
}

uint32_t canonical_mask(){
    map<int,vector<int>> bydeg;
    for(int v=0;v<N;v++) bydeg[D[v]].push_back(v);
    vector<pair<vector<int>,vector<int>>> groups;
    int pos=0;
    for(auto &kv:bydeg){
        vector<int> targets;
        for(size_t j=0;j<kv.second.size();j++) targets.push_back(pos++);
        groups.push_back({kv.second,targets});
    }
    array<int,N> lab{}; uint32_t best=UINT32_MAX;
    auto rec = [&](auto&& self,int gi)->void{
        if(gi==(int)groups.size()){ best=min(best,relabel_mask(lab)); return; }
        auto src=groups[gi].first; auto tgt=groups[gi].second;
        sort(src.begin(),src.end());
        do{
            for(size_t j=0;j<src.size();j++) lab[src[j]]=tgt[j];
            self(self,gi+1);
        }while(next_permutation(src.begin(),src.end()));
    };
    rec(rec,0); return best;
}

string edge_list(uint32_t mask){
    string s="{"; bool first=true;
    for(int i=0;i<M;i++) if(mask&(1u<<i)){
        if(!first) s += ","; first=false;
        s += to_string(E[i].first)+to_string(E[i].second);
    }
    return s+"}";
}

int main(){
    for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) E.push_back({i,j});
    map<uint32_t,long long> classes;
    uint32_t x=(1u<<K)-1, limit=(1u<<M); long long checked=0, hits=0;
    while(x<limit){
        checked++; A.fill(0); D.fill(0);
        uint32_t y=x; while(y){ int b=__builtin_ctz(y); y&=y-1; auto [u,v]=E[b]; A[u]|=1u<<v; A[v]|=1u<<u; D[u]++; D[v]++; }
        bool isolated=false; for(int v=0;v<N;v++) if(D[v]==0){isolated=true;break;}
        if(!isolated && connected() && forbidden_cycle_free() && saturated()){
            hits++; classes[canonical_mask()]++;
        }
        uint32_t c=x&-x, r=x+c; if(!r || r>=limit) break;
        x=(((r^x)>>2)/c)|r;
    }
    cout << "checked=" << checked << "\n";
    cout << "saturated_hits=" << hits << "\n";
    cout << "isomorphism_classes=" << classes.size() << "\n";
    int j=0;
    for(auto [mask,count]:classes){
        A.fill(0); D.fill(0);
        for(int i=0;i<M;i++) if(mask&(1u<<i)){auto [u,v]=E[i];A[u]|=1u<<v;A[v]|=1u<<u;D[u]++;D[v]++;}
        vector<int> ds(D.begin(),D.end()); sort(ds.begin(),ds.end());
        int tri=0; for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++) if((A[a]&(1u<<b))&&(A[a]&(1u<<c))&&(A[b]&(1u<<c))) tri++;
        cout << "class=" << (++j) << " labeled=" << count << " aut=" << (40320/count) << " degrees=";
        for(int i=0;i<N;i++){if(i)cout<<",";cout<<ds[i];}
        cout << " triangles=" << tri << " edges=" << edge_list(mask) << "\n";
    }
}
