// Independent sitewise exact finite-size verifier. No symbolic support reduction used.
// Each state is a base-3 string of 2*n site colors; the two n-vertex cliques are paired.
#include <iostream>
#include <vector>
#include <array>
#include <cassert>
#include <cstdint>
using namespace std;
uint32_t step(uint32_t z,int n,const vector<uint32_t>& pw) {
    vector<int> a(2*n); uint32_t x=z;
    for(int i=0;i<2*n;++i) {a[i]=x%3; x/=3;}
    vector<int> b(2*n);
    for(int i=0;i<2*n;++i) {
        if(a[i]==1) {b[i]=2;continue;}
        if(a[i]==2) {b[i]=0;continue;}
        bool active=(a[i<n?i+n:i-n]==1);
        const int start=(i<n?0:n),end=start+n;
        for(int j=start;j<end;++j) if(j!=i && a[j]==1) active=true;
        b[i]=active?1:0;
    }
    uint32_t r=0;
    for(int i=0;i<2*n;++i) r+=b[i]*pw[i];
    return r;
}
int main() {
 for(int n=2;n<=6;++n) {
   vector<uint32_t> pw(2*n+1,1);
   for(int i=1;i<=2*n;++i)pw[i]=pw[i-1]*3;
   uint32_t total=pw[2*n];
   array<uint64_t,3> bas={0,0,0};
   uint64_t states3=0,states4=0,states1=0;
   array<uint64_t,5> entrance={0,0,0,0,0};
   for(uint32_t z=0;z<total;++z) {
       uint32_t orbit[17];orbit[0]=z;
       for(int t=1;t<=16;++t)orbit[t]=step(orbit[t-1],n,pw);
       assert(orbit[4]==orbit[16]);
       int period=0;
       for(int p:{1,3,4})if(orbit[4]==orbit[4+p]){period=p;break;}
       assert(period);
       int first=0;
       while(first<=4 && orbit[first]!=orbit[first+period])++first;
       assert(first<=4);
       ++entrance[first];
       if(period==1){++bas[0];if(first==0)++states1;}
       if(period==3){++bas[1];if(first==0)++states3;}
       if(period==4){++bas[2];if(first==0)++states4;}
   }
   uint64_t a=1,b=1,c=1,d=1;
   for(int i=0;i<n;++i){a*=2;b*=3;c*=4;d*=9;}
   assert(bas[0]==3*c+6*b-12*a+3);
   assert(bas[1]==d-9*c+18*a-9);
   assert(bas[2]==6*(c-b-a+1));
   assert(states1==1 && states4==4*(a-2));
   uint64_t sur=b-3*a+3;
   uint64_t cyc=sur*sur+6*(c-3*b+3*a-1);
   assert(states3==cyc);
   cout<<"n="<<n<<" initial="<<total<<" basin1="<<bas[0]
       <<" basin3="<<bas[1]<<" basin4="<<bas[2]
       <<" recurrent3="<<states3<<" recurrent4="<<states4
       <<" entrance=(";
   for(int t=0;t<=4;++t)cout<<(t?",":"")<<entrance[t];
   cout<<") PASS\n";
 }
 cout<<"ALL INDEPENDENT SITEWISE ASSERTIONS PASS\n";
}
