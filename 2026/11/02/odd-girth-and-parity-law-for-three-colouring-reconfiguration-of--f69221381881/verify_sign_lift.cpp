#include <bits/stdc++.h>
using namespace std;
struct DSU {
    vector<int> p,sz;
    explicit DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);}
    int root(int x){return p[x]==x?x:p[x]=root(p[x]);}
    void join(int a,int b){a=root(a);b=root(b);if(a!=b){if(sz[a]<sz[b])swap(a,b);p[b]=a;sz[a]+=sz[b];}}
};
static long long binom(int n,int k){if(k<0||k>n)return 0;long long r=1;for(int i=1;i<=k;++i)r=r*(n-k+i)/i;return r;}

static void test_lift(int n,int mask,int p){
    const int w=2*p-n;
    vector<int> h(n),t(n);
    for(int i=1;i<n;i++)h[i]=h[i-1]+((mask>>(i-1)&1)?1:-1);
    t=h;for(auto &x:t)x+=6;
    auto col=[&](const vector<int>&v){string s;for(int x:v)s.push_back(char('0'+((x%3+3)%3)));return s;};
    string initial=col(h);
    set<string> seen;seen.insert(initial);
    for(int step=0;step<3*n;step++){
        int pos=-1;
        for(int i=0;i<n;i++){
            int left=(i==0?h[n-1]-w:h[i-1]);
            int right=(i==n-1?h[0]+w:h[i+1]);
            if(h[i]<t[i]&&left==h[i]+1&&right==h[i]+1){pos=i;break;}
        }
        if(pos<0){cerr<<"LIFT_FAILED n="<<n<<" mask="<<mask<<" step="<<step<<"\n";exit(1);}
        h[pos]+=2;
        for(int i=0;i<n;i++){
            int j=(i+1)%n;
            int diff=(j==0?h[0]+w-h[i]:h[j]-h[i]);
            if(abs(diff)!=1){cerr<<"INVALID_SLOPE";exit(1);}
        }
        string s=col(h);
        if(step<3*n-1){if(!seen.insert(s).second){cerr<<"REPEAT_BEFORE_3N";exit(1);}}
        else if(s!=initial){cerr<<"WRONG_FINAL";exit(1);}
    }
    if(h!=t){cerr<<"NOT_TARGET";exit(1);}
}

int main(){
    for(int n=3;n<=16;n++){
        int N=1<<n,total=3*N;
        vector<vector<int>> adj(total);
        DSU d(total);
        vector<int> groupCount(n+1,0);vector<long long> degsum(n+1,0);
        vector<int> representative(n+1,-1);
        vector<int> valid;
        for(int mask=0;mask<N;mask++){
            int p=__builtin_popcount((unsigned)mask);
            if((2*p-n)%3!=0)continue;
            groupCount[p]+=3;valid.push_back(mask);
            if(representative[p]<0)representative[p]=3*mask;
            if(p>0&&p<n)test_lift(n,mask,p);
            for(int c=0;c<3;c++){
                int u=3*mask+c;
                for(int i=0;i<n;i++){
                    int prev=(i+n-1)%n;
                    int s=(mask>>prev)&1,t=(mask>>i)&1;
                    if(s==t)continue;
                    int mask2=mask^(1<<prev)^(1<<i);
                    int c2=(i==0?(c+(s?1:2))%3:c);
                    int v=3*mask2+c2;
                    adj[u].push_back(v); d.join(u,v);
                    degsum[p]++;
                }
            }
        }
        for(int p=0;p<=n;p++)if(groupCount[p]){
            if(groupCount[p]!=3*binom(n,p)){cerr<<"COUNT_FAIL";return 1;}
            long long expected=(p==0||p==n?0:6LL*n*binom(n-2,p-1));
            if(degsum[p]!=expected){cerr<<"EDGE_FAIL n="<<n<<" p="<<p;return 1;}
            set<int> roots;
            for(int mask:valid)if(__builtin_popcount((unsigned)mask)==p)
                for(int c=0;c<3;c++)roots.insert(d.root(3*mask+c));
            int expectedComponents=(p==0||p==n?3:1);
            if((int)roots.size()!=expectedComponents){cerr<<"COMP_FAIL n="<<n<<" p="<<p;return 1;}
            if(p==0||p==n)continue;
            int source=representative[p];
            vector<int> dist(2*total,-1);deque<int> q;
            dist[2*source]=0;q.push_back(2*source);
            while(!q.empty()){
                int id=q.front();q.pop_front();int u=id/2,par=id%2;
                for(int v:adj[u]){int j=2*v+(par^1);if(dist[j]<0){dist[j]=dist[id]+1;q.push_back(j);}}
            }
            int odd=dist[2*source+1];
            if(n%2?(odd!=3*n):(odd!=-1)){cerr<<"ODD_FAIL n="<<n<<" p="<<p<<" odd="<<odd;return 1;}
            if(min(p,n-p)==1){
                for(int mask:valid)if(__builtin_popcount((unsigned)mask)==p)
                    for(int c=0;c<3;c++)if(adj[3*mask+c].size()!=2){cerr<<"CYCLE_FAIL";return 1;}
            }
        }
        long long verts=0,edges=0;
        for(int p=0;p<=n;p++){verts+=groupCount[p];edges+=degsum[p]/2;}
        cout<<"SIGN_LIFT_PASS n="<<n<<" vertices="<<verts<<" edges="<<edges<<"\n";
    }
}
