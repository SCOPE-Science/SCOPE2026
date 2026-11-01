// Independent bit-matrix verification of characteristic-two edge dynamics.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using U = uint64_t;

int rank2(vector<U> rows) {
    U piv[64]{};
    int r=0;
    for(U x:rows) {
        while(x) {
            int j=63-__builtin_clzll(x);
            if(piv[j]) x ^= piv[j];
            else {piv[j]=x; ++r; break;}
        }
    }
    return r;
}
U step(const vector<U>& a, U x) {
    U y=0;
    for(size_t i=0;i<a.size();++i)
        if(__builtin_parityll(x & a[i])) y |= U(1)<<i;
    return y;
}
void check(vector<int> sizes) {
    int N=1;
    for(int s:sizes) N*=s;
    vector<vector<int>> coord(N);
    for(int v=0;v<N;++v){
        int t=v;
        for(int s:sizes){coord[v].push_back(t%s);t/=s;}
    }
    vector<pair<int,int>> edges;
    for(int i=0;i<N;++i)for(int j=i+1;j<N;++j){
        int dif=0;
        for(size_t c=0;c<sizes.size();++c) dif += coord[i][c]!=coord[j][c];
        if(dif==1) edges.emplace_back(i,j);
    }
    int E=edges.size();
    if(E>60) return;
    vector<U> A(E);
    for(int i=0;i<E;++i)for(int j=0;j<E;++j){
        if(i==j) continue;
        auto [a,b]=edges[i];auto [c,d]=edges[j];
        if(a==c||a==d||b==c||b==d)A[i]|=U(1)<<j;
    }
    vector<U> A2(E),A3(E);
    for(int i=0;i<E;++i) {
        A2[i]=step(A,A[i]);
        A3[i]=step(A,A2[i]);
    }
    int r1=rank2(A),r2=rank2(A2),r3=rank2(A3);
    int H=1, D=0;
    for(int s:sizes){H*=s-2;D+=s-1;}
    int pred2=sizes.size()>=2?(N-H)/2-2:0;
    assert(E==N*D/2 && r1==N-2 && r2==pred2 && r3==0);
    if(E<=16){
        uint64_t cnt[4]{};
        for(U x=0;x<(U(1)<<E);++x){
            U u=x;
            int t=0;
            while(u && t<3) {u=step(A,u);++t;}
            assert(u==0);
            ++cnt[t];
        }
        U expected[4]={1,U(1)<<(E-r1),U(1)<<(E-r2),U(1)<<E};
        assert(cnt[0]==1);
        assert(cnt[0]+cnt[1]==expected[1]);
        assert(cnt[0]+cnt[1]+cnt[2]==expected[2]);
        assert(cnt[0]+cnt[1]+cnt[2]+cnt[3]==expected[3]);
        cout<<"exhaustive: E="<<E<<" exact first-zero time="<<cnt[0]<<","<<cnt[1]<<","<<cnt[2]<<","<<cnt[3]<<"\n";
    }
    cout<<"sizes=";
    for(int s:sizes)cout<<s<<",";
    cout<<" V="<<N<<" E="<<E<<" rank(F,F²,F³)="<<r1<<","<<r2<<","<<r3<<" PASS\n";
}
int main(){
    for(auto ss:vector<vector<int>>{{2,2},{2,4},{2,6},{4,4},{2,2,2},{2,2,4},{2,2,2,2},{2,2,2,2,2}})check(ss);
    cout<<"PASS independent incidence-free graph construction and rank/exhaustion checks\n";
}
