// Independent exhaustive verification through order nine using automorphisms
// of the clique-by-independent-set incidence matrix, not pinned graph isomorphism.
// Build: g++ -std=c++17 -O3 verify_split_small_independent.cpp -o verify_split_small_independent
#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

struct UnionFind {
    vector<int> p;
    explicit UnionFind(int n):p(n){iota(p.begin(),p.end(),0);}
    int root(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
    void unite(int a,int b){p[root(a)]=root(b);}
    bool same(int a,int b){return root(a)==root(b);}
};

int main(){
    for(int n=1;n<=9;n++){
        long long examined=0, mixed_twins=0, nontrivial=0;
        for(int k=0;k<=n;k++){
            const int m=n-k, maximum=1<<k;
            vector<int> columns(m,0);
            auto go=[&](auto&&self,int j,int lower)->void{
                if(j<m){for(int x=lower;x<maximum;x++){columns[j]=x;self(self,j+1,x);}return;}
                examined++;
                array<unsigned short,10> adj{};
                for(int a=0;a<k;a++)for(int b=a+1;b<k;b++){
                    adj[a]|=1u<<b;adj[b]|=1u<<a;
                }
                for(int t=0;t<m;t++)for(int a=0;a<k;a++)if(columns[t]>>a&1){
                    adj[a]|=1u<<(k+t);adj[k+t]|=1u<<a;
                }
                // Independent implementation: each color is a pair containing
                // the previous color and the full neighbor-color frequency row.
                vector<int> colors(n,0);
                for(;;){
                    map<vector<int>,int> lookup;vector<int> next(n);
                    for(int a=0;a<n;a++){
                        vector<int> sig(n+1);sig[0]=colors[a];
                        for(int b=0;b<n;b++)if(adj[a]>>b&1)sig[1+colors[b]]++;
                        auto it=lookup.find(sig);
                        if(it==lookup.end())it=lookup.emplace(sig,(int)lookup.size()).first;
                        next[a]=it->second;
                    }
                    bool same=true;
                    for(int a=0;a<n;a++)for(int b=0;b<a;b++)
                        if((colors[a]==colors[b])!=(next[a]==next[b]))same=false;
                    colors=next;
                    if(same)break;
                }
                // Same-colored vertices across the chosen split partition
                // happen to be graph twins in this exhaustive range.
                for(int a=0;a<k;a++)for(int b=k;b<n;b++)if(colors[a]==colors[b]){
                    bool twins=true;
                    for(int x=0;x<n;x++)if(x!=a&&x!=b && ((adj[a]>>x&1)!=(adj[b]>>x&1)))twins=false;
                    if(!twins || ((adj[a]>>b&1)!=(adj[b]>>a&1))){
                        cerr<<"Cross-part non-twin at n="<<n<<"\n";exit(4);
                    }
                    mixed_twins++;
                }
                bool require=false;
                for(int a=0;a<n;a++)for(int b=0;b<a;b++)if(colors[a]==colors[b]){
                    if((a<k)!=(b<k))continue;
                    bool twins=true;
                    for(int x=0;x<n;x++)if(x!=a&&x!=b && ((adj[a]>>x&1)!=(adj[b]>>x&1)))twins=false;
                    if(!twins)require=true;
                }
                if(!require) return;
                nontrivial++;
                // An automorphism preserving the two split parts is exactly a
                // permutation of clique vertices preserving the multiset of
                // independent-neighborhood masks, with free permutations of
                // columns that share a mask.
                UnionFind uf(n);
                map<int,int> first_of_mask;
                for(int t=0;t<m;t++){
                    auto [it,is_new]=first_of_mask.emplace(columns[t],k+t);
                    if(!is_new)uf.unite(k+t,it->second);
                }
                vector<int> row_perm(k);iota(row_perm.begin(),row_perm.end(),0);
                vector<int> incidence_degree(k,0);
                for(int x:columns)for(int a=0;a<k;a++)if(x>>a&1)incidence_degree[a]++;
                do {
                    bool maybe=true;
                    for(int a=0;a<k;a++)if(incidence_degree[a]!=incidence_degree[row_perm[a]]){maybe=false;break;}
                    if(!maybe)continue;
                    vector<int> translated;
                    translated.reserve(m);
                    for(int mask:columns){
                        int mapped=0;
                        for(int a=0;a<k;a++)if(mask>>a&1)mapped|=1<<row_perm[a];
                        translated.push_back(mapped);
                    }
                    vector<int> sorted=translated;sort(sorted.begin(),sorted.end());
                    if(sorted!=columns)continue;
                    for(int a=0;a<k;a++)uf.unite(a,row_perm[a]);
                    for(int t=0;t<m;t++)uf.unite(k+t,first_of_mask.at(translated[t]));
                }while(next_permutation(row_perm.begin(),row_perm.end()));
                for(int a=0;a<n;a++)for(int b=0;b<a;b++)if(colors[a]==colors[b] && (a<k)==(b<k)){
                    if(!uf.same(a,b)){
                        cerr<<"Unmatched within-part color class: n="<<n<<" k="<<k<<"\n";
                        exit(5);
                    }
                }
            };
            go(go,0,0);
        }
        cout<<"INDEPENDENT n="<<n<<" representations="<<examined
            <<" difficult_matrices="<<nontrivial<<" mixed_color_twin_pairs="<<mixed_twins
            <<" orbit_exact=YES\n";
    }
    cout<<"INDEPENDENT_VERIFIED_THROUGH_NINE\n";
}
