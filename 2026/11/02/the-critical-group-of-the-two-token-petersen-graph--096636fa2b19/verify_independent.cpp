// Independent Kneser-labelled construction of the 2-token Petersen graph.
// Compile: g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
using i64 = long long;
using i128 = __int128_t;
i64 powi(i64 p,int e){i64 t=1;while(e--)t*=p;return t;}
i64 mod(i128 x,i64 m){i64 r=(i64)(x%m);return r<0?r+m:r;}
i64 inverse(i64 a,i64 m){ // Extended Euclidean algorithm, gcd(a,m)=1.
    i64 b=m,x=1,y=0;
    while(b){i64 q=a/b; i64 t=a-q*b;a=b;b=t;
        t=x-q*y;x=y;y=t;}
    assert(a==1);return mod(x,m);
}
int vp(i64 x,i64 p,int E){if(x==0)return E;int e=0;while(x%p==0){x/=p;e++;}return e;}
vector<int> smith_p(vector<vector<i64>> A,int p,int E){
    i64 Q=powi(p,E);int n=(int)A.size();
    for(auto &row:A)for(auto &x:row)x=mod(x,Q);
    vector<int> valuations;
    for(int k=0;k<n;k++){
        int best=E,ri=-1,cj=-1;
        for(int i=k;i<n;i++)for(int j=k;j<n;j++){
            int e=vp(A[i][j],p,E);
            if(e<best){best=e;ri=i;cj=j;}}
        assert(ri>=0);
        swap(A[k],A[ri]);
        for(int i=0;i<n;i++)swap(A[i][k],A[i][cj]);
        i64 divisor=powi(p,best),modSmall=Q/divisor;
        i64 inv=inverse(A[k][k]/divisor,modSmall);
        for(int i=k+1;i<n;i++){
            i64 q=mod((i128)(A[i][k]/divisor)*inv,modSmall);
            for(int j=k;j<n;j++)A[i][j]=mod((i128)A[i][j]-(i128)q*A[k][j],Q);
            assert(A[i][k]==0);
        }
        for(int j=k+1;j<n;j++){
            i64 q=mod((i128)(A[k][j]/divisor)*inv,modSmall);
            for(int i=k;i<n;i++)A[i][j]=mod((i128)A[i][j]-(i128)q*A[i][k],Q);
            assert(A[k][j]==0);
        }
        valuations.push_back(best);
    }
    assert(is_sorted(valuations.begin(),valuations.end()));
    return valuations;
}
int main(){
    vector<int> base;
    for(int mask=0;mask<(1<<5);mask++)if(__builtin_popcount((unsigned)mask)==2)base.push_back(mask);
    assert(base.size()==10);
    bool adj[10][10]{};
    for(int i=0;i<10;i++)for(int j=0;j<10;j++)adj[i][j]=(i!=j && !(base[i]&base[j]));
    for(int i=0;i<10;i++)assert(accumulate(adj[i],adj[i]+10,0)==3);
    vector<pair<int,int>> state;int id[10][10];
    for(int i=0;i<10;i++)for(int j=0;j<10;j++)id[i][j]=-1;
    for(int i=0;i<10;i++)for(int j=i+1;j<10;j++){
        id[i][j]=id[j][i]=(int)state.size();state.push_back({i,j});}
    assert(state.size()==45);
    vector<vector<i64>> L(45,vector<i64>(45,0));
    for(int s=0;s<45;s++){
        auto [a,b]=state[s];
        for(auto [moving,fixed]:vector<pair<int,int>>{{a,b},{b,a}})
            for(int t=0;t<10;t++)if(adj[moving][t] && t!=fixed){
                L[s][s]++;L[s][id[t][fixed]]--;}
    }
    int degreeSum=0;
    for(int i=0;i<45;i++){
        degreeSum+=L[i][i];i64 sum=accumulate(L[i].begin(),L[i].end(),(i64)0);assert(sum==0);
        for(int j=0;j<45;j++)assert(L[i][j]==L[j][i]);}
    assert(degreeSum==240);
    vector<vector<i64>> A(44,vector<i64>(44));
    for(int i=0;i<44;i++)for(int j=0;j<44;j++)A[i][j]=L[i][j];
    map<int,pair<int,map<int,int>>> target={
       {2,{36,{{0,28},{1,8},{2,4},{5,4}}}},
       {3,{9,{{0,39},{1,1},{2,4}}}},
       {5,{3,{{0,41},{1,3}}}},
       {7,{6,{{0,38},{1,6}}}},
       {19,{5,{{0,39},{1,5}}}}
    };
    vector<i64> diagonal(44,1);
    for(const auto &[p,edata]:target){
        auto [E,profile]=edata;
        vector<int> result=smith_p(A,p,E+1);
        map<int,int> counts;int total=0;
        for(int i=0;i<44;i++){counts[result[i]]++;total+=result[i];diagonal[i]*=powi(p,result[i]);}
        assert(counts==profile && total==E);
        cout<<"INDEPENDENT_P_ADIC "<<p<<" ";
        for(auto [v,n]:counts)cout<<"("<<v<<":"<<n<<")";
        cout<<"\n";
    }
    vector<i64> expected(28,1);expected.insert(expected.end(),8,2);expected.insert(expected.end(),2,4);
    expected.insert(expected.end(),{28,1596,38304,191520,191520,191520});
    assert(diagonal==expected);
    for(int i=0;i<43;i++)assert(diagonal[i+1]%diagonal[i]==0);
    cout<<"INDEPENDENT_KNESER_AND_SMITH_PASS order=45 edges=120 nontrivial=16\n";
}
