// Independent finite verification of rectangular-swap transition rates on labelled
// bipartite degree-two graphs. Standard C++17; no external dependencies.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
using Part=vector<int>;

int n;
array<unsigned char, 8> rows, degrees;
map<Part,long long> census;
long long visited=0, validated=0;

Part component_sizes() {
    bool used[16] = {};
    Part ret;
    for (int start=0; start<n; ++start) if (!used[start]) {
        vector<int> todo{start}; used[start]=true;
        int rcnt=0;
        while (!todo.empty()) {
            int v=todo.back();todo.pop_back();
            if (v<n) ++rcnt;
            if (v<n) {
                for (int c=0;c<n;c++) if ((rows[v]>>c)&1) {
                    int w=n+c;
                    if (!used[w]) {used[w]=true;todo.push_back(w);}
                }
            } else {
                int c=v-n;
                for (int r=0;r<n;r++) if ((rows[r]>>c)&1) {
                    if (!used[r]) {used[r]=true;todo.push_back(r);}
                }
            }
        }
        assert(rcnt>=2);ret.push_back(rcnt);
    }
    sort(ret.begin(),ret.end());
    return ret;
}

map<Part,int> expected(Part p) {
    map<Part,int> out;
    int h=p.size();
    for(int i=0;i<h;i++) {
        int a=p[i];
        if(a>2)out[p]+=a*(a-2);
        for(int j=i+1;j<h;j++) {
            int b=p[j];Part q;
            for(int z=0;z<h;z++) if(z!=i&&z!=j)q.push_back(p[z]);
            q.push_back(a+b);sort(q.begin(),q.end());out[q]+=4*a*b;
        }
        for(int b=2;b<=a/2;b++) if(a-b>=2) {
            Part q;
            for(int z=0;z<h;z++)if(z!=i)q.push_back(p[z]);
            q.push_back(b);q.push_back(a-b);sort(q.begin(),q.end());
            out[q]+= (b==a-b? a: 2*a);
        }
    }
    return out;
}

long long factorial(int z) {long long a=1;for(int j=1;j<=z;j++)a*=j;return a;}
long long expected_census(Part p) {
    long long num=factorial(n)*factorial(n), den=1;
    for(int i=0;i<(int)p.size();) {
        int k=p[i], m=0;
        while(i<(int)p.size()&&p[i]==k)++i,++m;
        for(int j=0;j<m;j++)den*=2*k;
        den*=factorial(m);
    }
    assert(num%den==0);return num/den;
}

void check() {
    ++visited;
    Part original=component_sizes();
    census[original]++;
    map<Part,int> got;
    int count=0;
    // Inspect every 2x2 submatrix, not a representation of pairwise edge swaps.
    for(int r=0;r<n;r++)for(int s=r+1;s<n;s++)
      for(int c=0;c<n;c++)for(int d=c+1;d<n;d++) {
        bool ac=(rows[r]>>c)&1, ad=(rows[r]>>d)&1;
        bool bc=(rows[s]>>c)&1, bd=(rows[s]>>d)&1;
        if (!((ac&&!ad&&!bc&&bd)||(!ac&&ad&&bc&&!bd)))continue;
        int toggle=(1<<c)|(1<<d);
        rows[r]^=toggle;rows[s]^=toggle;
        Part after=component_sizes();got[after]++;++count;
        rows[r]^=toggle;rows[s]^=toggle;
      }
    assert(got==expected(original));
    int sq=std::count(original.begin(),original.end(),2);
    assert(count==n*(2*n-5)+2*sq);
    ++validated;
}

void rec(int r) {
    if(r==n) {
        for(int c=0;c<n;c++)if(degrees[c]!=2)return;
        check();return;
    }
    int remaining=n-r-1;
    for(int c=0;c<n;c++)for(int d=c+1;d<n;d++) {
        degrees[c]++;degrees[d]++;
        bool okay=true;
        for(int x=0;x<n;x++) if(degrees[x]>2||degrees[x]+remaining<2)okay=false;
        if(okay){rows[r]=(1<<c)|(1<<d);rec(r+1);}
        degrees[c]--;degrees[d]--;
    }
}
int main(){
    for(n=2;n<=6;n++) {
        rows.fill(0);degrees.fill(0);census.clear();visited=validated=0;
        rec(0);
        long long checktot=0;
        for(auto &[p,c]:census){assert(c==expected_census(p));checktot+=c;}
        assert(checktot==validated && validated==visited);
        cout<<"n="<<n<<" states="<<visited<<" types="<<census.size()<<" confirmed"<<'\n';
    }
    cout<<"CPP_RECTANGLE_CYCLE_LUMPING_PASS"<<'\n';
}
