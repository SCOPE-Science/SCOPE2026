// Exact sharp centered maximal-variation certificate for paths on 5 and 6 vertices.
// Build: c++ -std=c++17 -O2 path_maximal_exact.cpp -o path_maximal_exact
// All computations use exact signed integer arithmetic.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using ll=long long;
constexpr ll SCALE=60; // divisible by every ball size for N <= 6
ll d3(ll a,ll b,ll c,ll d,ll e,ll f,ll g,ll h,ll i) {
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g);
}
ll d4(const array<array<ll,4>,4>& a) {
    return a[0][0]*d3(a[1][1],a[1][2],a[1][3],a[2][1],a[2][2],a[2][3],a[3][1],a[3][2],a[3][3])
         - a[0][1]*d3(a[1][0],a[1][2],a[1][3],a[2][0],a[2][2],a[2][3],a[3][0],a[3][2],a[3][3])
         + a[0][2]*d3(a[1][0],a[1][1],a[1][3],a[2][0],a[2][1],a[2][3],a[3][0],a[3][1],a[3][3])
         - a[0][3]*d3(a[1][0],a[1][1],a[1][2],a[2][0],a[2][1],a[2][2],a[3][0],a[3][1],a[3][2]);
}
template<size_t D>array<ll,D> primitive(array<ll,D> a){
    ll g=0;for(ll x:a)g=gcd(g,llabs(x));assert(g);
    for(ll &x:a)x/=g;
    for(ll x:a)if(x){if(x<0)for(ll &y:a)y=-y;break;}
    return a;
}
template<int N>void verify(){
    constexpr int D=N-1;
    using V=array<ll,D>;
    array<vector<V>,N> avg;
    set<V> H;
    for(int i=0;i<N;i++){
        for(int r=0;r<=max(i,N-1-i);r++){
            int count=0;for(int k=0;k<N;k++)if(abs(i-k)<=r)count++;
            V v{};
            for(int j=0;j<D;j++){
                int cnt=0;for(int k=0;k<N;k++)if(abs(i-k)<=r && k>j)cnt++;
                v[j]=(SCALE/count)*cnt;
            }
            if(find(avg[i].begin(),avg[i].end(),v)==avg[i].end())avg[i].push_back(v);
        }
        for(const V &a:avg[i])for(const V &b:avg[i]){
            V diff{};for(int j=0;j<D;j++)diff[j]=a[j]-b[j];
            if(any_of(diff.begin(),diff.end(),[](ll x){return x!=0;})) H.insert(primitive(diff));
        }
    }
    for(int j=0;j<D;j++){V e{};e[j]=1;H.insert(e);}
    vector<V> h(H.begin(),H.end());
    assert(h.size()==(N==5?27u:46u));
    auto out_variation=[&](const V &x){
        array<ll,N> y{};
        for(int i=0;i<N;i++){
            ll top=-(1LL<<60);
            for(const V &v:avg[i]){
                ll a=0;for(int j=0;j<D;j++)a+=v[j]*x[j];
                top=max(top,a);
            }
            y[i]=top;
        }
        ll sum=0;for(int i=0;i<D;i++)sum+=llabs(y[i+1]-y[i]);
        return sum;
    };
    ll tuples=0,rank_full=0,rays=0,ties=0;
    vector<int> selected;
    auto search=[&](auto &&self, int next)->void{
        if((int)selected.size()==D-1){
            tuples++;
            V x{};
            for(int omit=0;omit<D;omit++){
                array<array<ll,4>,4> a{};
                int col=0;
                for(int j=0;j<D;j++)if(j!=omit){
                    for(int r=0;r<D-1;r++)a[r][col]=h[selected[r]][j];
                    col++;
                }
                ll det=0;
                if constexpr (D==4) {
                    det=d3(a[0][0],a[0][1],a[0][2],a[1][0],a[1][1],a[1][2],a[2][0],a[2][1],a[2][2]);
                } else {
                    det=d4(a);
                }
                x[omit]=(omit%2?-det:det);
            }
            ll L=0;for(ll v:x)L+=llabs(v);
            if(!L)return;
            rank_full++;
            for(int s:{1,-1}){
                V u{};for(int j=0;j<D;j++)u[j]=s*x[j];
                ll upper=out_variation(u);
                if(N*upper > (N-1)*SCALE*L){
                    cerr<<"Counterexample N="<<N<<" increments ";for(ll z:u)cerr<<z<<' ';cerr<<'\n';exit(1);
                }
                if(N*upper==(N-1)*SCALE*L)ties++;
                rays++;
            }
            return;
        }
        for(int j=next;j<=(int)h.size()-(D-1-(int)selected.size());j++){
            selected.push_back(j);self(self,j+1);selected.pop_back();
        }
    };
    search(search,0);
    V spike{};spike[D-1]=1;
    assert(out_variation(spike)==SCALE*(N-1)/N);
    if constexpr(N==6)assert(tuples==163185 && rank_full==151429 && rays==302858 && ties==7268);
    cout<<"CERTIFICATE_OK N="<<N<<" planes="<<h.size()<<" tuples="<<tuples<<" rank_full="<<rank_full<<" rays="<<rays<<" ties="<<ties<<'\n';
}
int main(){verify<5>();verify<6>();}
