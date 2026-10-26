#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<array<int,4>> ex;
 for(int a=0;a<4;a++) for(int b=a;b<4;b++)for(int c=b;c<4;c++){array<int,4> e{};e[a]++;e[b]++;e[c]++;ex.push_back(e);}if(ex.size()!=20)abort();
 uint32_t val[16]={},der[16][4]={},hyper[16]={};
 for(int p=1;p<16;p++){
 for(int j=0;j<20;j++){bool v=1;for(int k=0;k<4;k++) if(ex[j][k] && !(p>>k&1))v=0;if(v)val[p]|=1u<<j;
 for(int k=0;k<4;k++)if(ex[j][k]&1){bool vv=1;for(int l=0;l<4;l++){int e=ex[j][l]-(k==l);if(e && !(p>>l&1))vv=0;} if(vv)der[p][k]|=1u<<j;}
 }
 for(int q=1;q<16;q++)if(!(__builtin_parity((unsigned)(p&q))))hyper[p]|=1u<<(q-1);
 }
 cerr<<"20 monomials:";for(int j=0;j<20;j++){cerr<<" ";for(int k=0;k<4;k++)for(int a=0;a<ex[j][k];a++)cerr<<(char)('w'+k);}cerr<<"\n";
 uint64_t tally[16][2]{}; uint64_t smoothQ[16][2]{};

 for(uint32_t f=1; f<(1u<<20);f++){
 int n=0;unsigned cov=0;bool qr=1;
 for(int p=1;p<16;p++)if(!__builtin_parity((unsigned)(f&val[p]))){n++;
 int g=0;for(int k=0;k<4;k++)g|=(__builtin_parity((unsigned)(f&der[p][k]))<<k);
 if(!g) qr=0;else cov|=hyper[g];
 }
 bool tf=(cov==32767);
 tally[n][tf]++;if(qr){smoothQ[n][tf]++;}
 }
 for(int n=0;n<16;n++)if(tally[n][0]+tally[n][1])cerr<<"N="<<n<<" all_nonfill="<<tally[n][0]<<" all_fill="<<tally[n][1]<<" rational_smooth_nonfill="<<smoothQ[n][0]<<" rational_smooth_fill="<<smoothQ[n][1]<<"\n";
 if(smoothQ[3][1]!=1540 || smoothQ[1][1]!=0){cerr<<"unexpected count\n";return 1;}
 cout<<"PASS: exactly 1540 rationally nonsingular tangent-filling cubics with 3 rational points; none with 1\n";
 return 0;
}
