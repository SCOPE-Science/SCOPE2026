/* Direct labelled-state enumeration for three-state threshold-two excitation.
   Build: c++ -std=c++17 -O2 verify_microscopic.cpp -o verify_microscopic
   Run: ./verify_microscopic
*/
#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <stdexcept>
#include <algorithm>
using namespace std;
using u64=uint64_t;

u64 powu(u64 a,int b){u64 r=1;while(b--)r*=a;return r;}
struct Vec {vector<unsigned char> v;bool operator==(Vec const& o)const{return v==o.v;}};
Vec advance(Vec const& s,int a,int b){
    int ex0=0,ex1=0;
    for(int i=0;i<a;i++) ex0+=(s.v[i]==1);
    for(int i=a;i<a+b;i++) ex1+=(s.v[i]==1);
    Vec t=s;
    for(int i=0;i<a+b;i++){
        if(s.v[i]==1) t.v[i]=2;
        else if(s.v[i]==2)t.v[i]=0;
        else t.v[i]=((i<a?ex1:ex0)>=2)?1:0;
    }
    return t;
}
long long H(int n){if(n<4)return 0;return (long long)powu(3,n)-3LL*powu(2,n)-3LL*n*powu(2,n-1)+3LL*(n*n+n+1);}
long long P(int n){if(n<4)return 0;return (n+2LL)*powu(2,n-1)-2LL*n*n-2LL*n-2;}
long long Q(int n){return n<4?0LL:(long long)n*(n-1);}
long long B4(int a,int b){
    long long pa=P(a),pb=P(b),qa=Q(a),qb=Q(b),ha=H(a),hb=H(b);
    return 6*pa*pb+3*(pa*qb+qa*pb)+2*qa*qb+(3*pa+qa)*hb+ha*(3*pb+qb);
}
int main(){
  const array<pair<int,int>,8> cases = {{{2,2},{3,4},{4,4},{4,5},{5,5},{5,6},{6,6},{4,8}}};
  u64 total_checked=0;
  for(auto [a,b]:cases){
    int n=a+b;u64 nstates=powu(3,n);total_checked+=nstates;
    u64 cycles[5]={}, maxentry=0;
    for(u64 serial=0;serial<nstates;serial++){
        Vec s; s.v.resize(n);u64 d=serial;
        for(int j=0;j<n;j++){s.v[j]=d%3;d/=3;}
        vector<Vec> traj;traj.reserve(20);
        int entry=-1,period=-1;
        for(int k=0;k<18;k++){
            auto it=find(traj.begin(),traj.end(),s);
            if(it!=traj.end()){
                entry=int(it-traj.begin());period=k-entry;break;
            }
            traj.push_back(s);
            s=advance(s,a,b);
        }
        if(entry<0 || entry>5 || (period!=1 && period!=3 && period!=4)) {
            cerr<<"FAIL dynamics: a="<<a<<" b="<<b<<" config="<<serial<<" entry="<<entry<<" period="<<period<<'\n';return 1;
        }
        cycles[period]++;
        if((u64)entry>maxentry) maxentry=entry;
    }
    if(cycles[3]!=(u64)(H(a)*H(b)) || cycles[4]!=(u64)B4(a,b) ||
         cycles[1]!=nstates-cycles[3]-cycles[4]){
         cerr<<"FAIL census a="<<a<<" b="<<b<<" observed "<<cycles[1]<<","<<cycles[3]<<","<<cycles[4]<<'\n';return 1;
    }
    cout<<"PASS K_"<<a<<","<<b<<" configurations="<<nstates
        <<" periods(1,3,4)="<<cycles[1]<<","<<cycles[3]<<","<<cycles[4]
        <<" maximal first entry="<<maxentry<<'\n';
  }
  cout<<"PASS independently enumerated "<<total_checked<<" labelled initial states\n";
}
