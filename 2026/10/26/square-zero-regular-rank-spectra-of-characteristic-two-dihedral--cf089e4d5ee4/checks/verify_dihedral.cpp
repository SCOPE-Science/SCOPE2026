// Enumerates square-zero elements and regular-module differential ranks over F_2.
// Usage: c++ -O2 -std=c++17 verify_dihedral.cpp -o check && ./check 3
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main(int argc,char**argv){
    int m=(argc>1)?atoi(argv[1]):3;
    if(m<1 || (m%2)!=1 || 8*m>24){cerr<<"odd m required, 8m<=24\n";return 2;}
    int n=4*m, N=2*n;
    auto mul=[&](int a,int b){
        int i=a%n,e=a/n,j=b%n,f=b/n;
        int h=(i+(e?-j:j))%n;if(h<0)h+=n;
        return h+n*((e+f)&1);
    };
    vector<uint32_t> diag(N);
    vector<vector<uint32_t>> pairing(N,vector<uint32_t>(N)), shift(N,vector<uint32_t>(N));
    for(int i=0;i<N;++i){
        diag[i]=uint32_t(1)<<mul(i,i);
        for(int j=0;j<N;++j){
            pairing[i][j]=(uint32_t(1)<<mul(i,j))^(uint32_t(1)<<mul(j,i));
            shift[j][i]=uint32_t(1)<<mul(i,j);
        }
    }
    uint32_t limit=uint32_t(1)<<N;
    vector<uint32_t> squares(limit,0);
    map<int,uint64_t> counts;
    for(uint32_t mask=0;mask<limit;++mask){
        if(mask){
            int i=__builtin_ctz(mask);uint32_t prev=mask&(mask-1);
            uint32_t v=squares[prev]^diag[i];
            for(uint32_t bits=prev;bits;bits&=bits-1)v^=pairing[i][__builtin_ctz(bits)];
            squares[mask]=v;
        }
        if(squares[mask])continue;
        uint32_t basis[24]={};int rank=0;
        for(int j=0;j<N;++j){
            uint32_t col=0;
            for(uint32_t bits=mask;bits;bits&=bits-1)col^=shift[j][__builtin_ctz(bits)];
            while(col){
                int row=31-__builtin_clz(col);
                if(!basis[row]){basis[row]=col;++rank;break;}
                col^=basis[row];
            }
        }
        counts[rank]++;
    }
    map<int,uint64_t> expected = (m==1) ? map<int,uint64_t>{{0,1},{1,1},{2,6},{4,40}} : map<int,uint64_t>{{0,1},{1,1},{2,15},{3,9},{4,172},{5,78},{6,996},{7,168},{8,4512},{9,384},{10,9024},{12,15360}};
    if(counts!=expected){cerr<<"DIRECT_DIHEDRAL_ENUM_FAIL\n";return 1;}
    cout<<"m="<<m<<", q=2, regular dimension="<<N<<"\n";
    uint64_t total=0;
    for(auto [r,c]:counts){cout<<r<<":"<<c<<"\n";total+=c;}
    cout<<"square_zero_total="<<total<<"\n";
}
