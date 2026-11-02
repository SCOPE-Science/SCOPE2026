// Independent implementation: generate both graphs by edges of their Cayley factors.
// Build and reduce over prime-power residue rings with alternative pivot order.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
using Matrix = vector<vector<int>>;
static constexpr int N=64;
int index3(int x,int y,int z) { return (x*4+y)*4+z; }
Matrix laplacian(bool doob) {
    Matrix a(N, vector<int>(N,0));
    auto edge=[&](int u,int v){ assert(u!=v); a[u][v]=1; a[v][u]=1; };
    for(int x=0;x<4;x++) for(int y=0;y<4;y++) for(int z=0;z<4;z++) {
        int u=index3(x,y,z);
        for(int w=0;w<4;w++) if(z!=w) edge(u,index3(x,y,w));
        if(doob) {
            edge(u,index3((x+1)%4,y,z));
            edge(u,index3(x,(y+1)%4,z));
            edge(u,index3((x+1)%4,(y+1)%4,z));
        } else {
            for(int w=0;w<4;w++) if(w!=x) edge(u,index3(w,y,z));
            for(int w=0;w<4;w++) if(w!=y) edge(u,index3(x,w,z));
        }
    }
    Matrix L(63,vector<int>(63));
    for(int i=0;i<N;i++) {
        assert(a[i][i]==0);
        assert(accumulate(a[i].begin(),a[i].end(),0)==9);
        for(int j=0;j<N;j++) assert(a[i][j]==a[j][i]);
    }
    for(int i=0;i<63;i++) for(int j=0;j<63;j++) L[i][j]=9*(i==j)-a[i][j];
    return L;
}
int valuation(int x,int p,int cap) {
    if(x==0) return cap;
    int e=0; while(x%p==0) {x/=p; e++;} return e;
}
int inv_mod(int x,int modulus) {
    x=(x%modulus+modulus)%modulus;
    for(int i=1;i<modulus;i++) if((x*i)%modulus==1) return i;
    assert(false); return -1;
}
map<int,int> smith_local(Matrix M,int prime,int precision) {
    int modulus=1; for(int i=0;i<precision;i++) modulus*=prime;
    const int size=(int)M.size();
    for(auto &row:M) for(auto &x:row) x=(x%modulus+modulus)%modulus;
    map<int,int> result;
    for(int k=0;k<size;k++) {
        int pi=-1,pj=-1,least=precision;
        // Descending ties are deliberate: a different elimination path.
        for(int i=size-1;i>=k;i--) for(int j=size-1;j>=k;j--) {
            int e=valuation(M[i][j],prime,precision);
            if(e<least) {least=e;pi=i;pj=j;}
        }
        assert(pi>=0);
        swap(M[k],M[pi]);
        for(int i=0;i<size;i++) swap(M[i][k],M[i][pj]);
        int scale=1;for(int i=0;i<least;i++) scale*=prime;
        int scalar=inv_mod(M[k][k]/scale,modulus);
        for(int j=k;j<size;j++) M[k][j]=(M[k][j]*scalar)%modulus;
        assert(M[k][k]==scale);
        for(int i=k+1;i<size;i++) {
            assert(M[i][k]%scale==0);
            int q=M[i][k]/scale;
            for(int j=k;j<size;j++) M[i][j]=(M[i][j]-q*M[k][j]%modulus+modulus)%modulus;
            assert(M[i][k]==0);
        }
        for(int j=k+1;j<size;j++) {
            assert(M[k][j]%scale==0);
            int q=M[k][j]/scale;
            for(int i=k;i<size;i++) M[i][j]=(M[i][j]-q*M[i][k]%modulus+modulus)%modulus;
            assert(M[k][j]==0);
        }
        result[least]++;
    }
    for(int i=0;i<size;i++) for(int j=0;j<size;j++) if(i!=j) assert(M[i][j]==0);
    return result;
}
void test(bool doob,const map<int,int>& want2) {
    Matrix L=laplacian(doob);
    auto v2=smith_local(L,2,9), v3=smith_local(L,3,5);
    assert(v2==want2);
    const map<int,int> expected3={{0,36},{1,27}};
    assert(v3==expected3);
    auto sum=[](const map<int,int>& v){int n=0;for(auto [e,k]:v)n+=e*k;return n;};
    assert(sum(v2)==147 && sum(v3)==27);
    cout<<(doob?"DOOB":"HAMMING")<<" INDEPENDENT_SMITH_OK";
    for(auto [e,k]:v2) cout<<" 2^"<<e<<":"<<k;
    cout<<"\n";
}
int main(){
    test(true, {{0,28},{1,3},{2,4},{3,2},{4,6},{5,14},{6,6}});
    test(false,{{0,28},{1,1},{2,8},{4,6},{5,14},{6,6}});
    cout<<"INDEPENDENT_CERTIFICATE_OK\n";
}
