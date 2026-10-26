// Independent exhaustive checks for local factors in characteristic two.
// c++ -std=c++17 -O2 dihedral_squarezero_extra_checks.cpp -o extra && ./extra
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int add(int a,int b){return a^b;}
int mult4(int a,int b){int z=0;for(int i=0;i<2;i++)for(int j=0;j<2;j++) if((a>>i&1)&&(b>>j&1)) z^=1<<(i+j);if(z&4)z^=7;return z;}
int rank4(array<array<int,8>,8> a){int r=0;for(int c=0;c<8;c++){int p=r;while(p<8 && !a[p][c])p++;if(p==8)continue;swap(a[p],a[r]);int inv=0;for(int k=1;k<4;k++)if(mult4(k,a[r][c])==1)inv=k;for(int j=c;j<8;j++)a[r][j]=mult4(inv,a[r][j]);for(int i=r+1;i<8;i++)if(a[i][c]){int b=a[i][c];for(int j=c;j<8;j++)a[i][j]^=mult4(b,a[r][j]);}r++;}return r;}
int main(){
    // D_8 over F_4, using the presentation r^4=s^2=1, srs=r^-1.
    map<int,int> got;
    for(int idx=0;idx<(1<<16);idx++){
        array<int,8> v{};for(int i=0;i<8;i++)v[i]=(idx>>(2*i))&3;
        auto product=[](int a,int b){int i=a%4,j=b%4,e=a/4,f=b/4;int k=(i+(e?-j:j)+4)%4;return k+4*((e+f)&1);};
        array<int,8> sq{};
        for(int a=0;a<8;a++)for(int b=0;b<8;b++)sq[product(a,b)]^=mult4(v[a],v[b]);
        bool zero=true;for(int t:sq)if(t)zero=false;if(!zero)continue;
        array<array<int,8>,8> M{};
        for(int a=0;a<8;a++)for(int b=0;b<8;b++) M[product(a,b)][b]^=v[a];
        got[rank4(M)]++;
    }
    map<int,int> expect={{0,1},{1,3},{2,60},{4,1728}};
    if(got!=expect){cerr<<"D8_F4_FAIL\n";return 1;}
    cout<<"D8_F4_OK";for(auto [r,v]:got)cout<<" rank"<<r<<"="<<v;cout<<"\n";
    // M_2(F_2[t]/(t^4)), all 65536 matrices: square and left regular rank.
    map<int,int> got2;
    auto rmul=[](int a,int b){int z=0;for(int i=0;i<4;i++)if(a>>i&1)for(int j=0;i+j<4;j++)if(b>>j&1)z^=1<<(i+j);return z;};
    for(int idx=0;idx<(1<<16);idx++){
        int a=idx&15,b=(idx>>4)&15,c=(idx>>8)&15,d=(idx>>12)&15;
        if((rmul(a,a)^rmul(b,c))||(rmul(a,b)^rmul(b,d))||(rmul(c,a)^rmul(d,c))||(rmul(c,b)^rmul(d,d)))continue;
        uint16_t bas[16]={};int rank=0;
        for(int col=0;col<16;col++){
            int e=col/4,t=col%4, row=e&1, column=e>>1;
            int xx[2][2]={{a,b},{c,d}};
            uint16_t vec=0;
            for(int i=0;i<2;i++){
                int v=(xx[i][row]<<t)&15;
                vec ^= (uint16_t)v << (4*(i*2+column));
            }
            while(vec){int pivot=31-__builtin_clz((unsigned)vec);if(!bas[pivot]){bas[pivot]=vec;rank++;break;}vec^=bas[pivot];}
        }
        got2[rank]++;
    }
    map<int,int> expect2={{0,1},{2,9},{4,78},{6,168},{8,384}};
    if(got2!=expect2){cerr<<"M2_R4_F2_FAIL";for(auto [r,c]:got2)cerr<<" "<<r<<":"<<c;cerr<<"\n";return 1;}
    cout<<"M2_R4_F2_OK";for(auto [r,v]:got2)cout<<" rank"<<r<<"="<<v;cout<<"\n";
    return 0;
}
