// Exact six-point Fourier-algebra-norm census on Boolean groups.
// C++17: g++ -O2 -std=c++17 checker.cpp -o checker && ./checker
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

static int affine_rank(const vector<int>& a, int d) {
    array<int, 8> piv{};
    int r=0;
    for (size_t j=1;j<a.size();++j) {
        int x=a[j]^a[0];
        for(int bit=d-1;bit>=0;--bit) if((x>>bit)&1) {
            if(!piv[bit]){piv[bit]=x;++r;break;}
            x^=piv[bit];
        }
    }
    return r;
}

static int norm_times_eight(const vector<int>& a,int d) {
    const int n=1<<d;
    int s=0;
    for(int u=0;u<n;++u){
        int v=0;
        for(int x:a) v+= __builtin_parity((unsigned)(x&u))?-1:1;
        s+=v>=0?v:-v;
    }
    assert((8*s)%n==0);
    return 8*s/n;
}

int main(){
    map<int, map<int, uint64_t>> all, six;
    for(int d=3;d<=5;++d){
        const int n=1<<d;
        for(int k=1;k<=6;++k){
            vector<int> a(k);
            for(int i=0;i<k;++i)a[i]=i;
            while(true){
                int r=affine_rank(a,d);
                int e=0;for(int x:a)e^=x;
                int expect=-1;
                if(k<=2)expect=8;
                if(k==3)expect=12;
                if(k==4)expect=r==2?8:12;
                if(k==5)expect=r==3?14:15;
                if(k==6)expect=r==3?12:r==5?15:e==0?18:14;
                assert(expect!=-1);
                int got=norm_times_eight(a,d);
                if(got!=expect){
                    cerr<<"counterexample d="<<d<<" k="<<k<<" rank="<<r
                        <<" got="<<got<<" expected="<<expect<<"\n";
                    return 1;
                }
                all[k][got]++;
                if(k==6)six[d][got]++;
                int i=k-1;
                while(i>=0 && a[i]==n-k+i)--i;
                if(i<0)break;
                ++a[i];for(int j=i+1;j<k;++j)a[j]=a[j-1]+1;
            }
        }
        static const uint64_t target[3][4]={
            {28,0,0,0},
            {840,6720,0,448},
            {17360,416640,444416,27776}
        };
        const int norms[4]={12,14,15,18};
        for(int j=0;j<4;++j) {
            if(six[d][norms[j]]!=target[d-3][j]) {
                cerr<<"bad dimension count d="<<d<<" norm8="<<norms[j]
                    <<" found="<<six[d][norms[j]]<<" expected="<<target[d-3][j]<<"\n";
                return 2;
            }
        }
        cout<<"dimension="<<d;
        for(int j=0;j<4;++j)cout<<" norm8="<<norms[j]<<":"<<six[d][norms[j]];
        cout<<" PASS\n";
    }
    cout<<"All cases of support size at most five have norm <= 15/8; "
        <<"six-point threshold and affine-circuit equality pass.\nCHECK_PASS\n";
}
