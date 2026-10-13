#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
int main(){
 const int n=26; const uint32_t all=(1u<<n)-1;
 uint32_t A[n]={9584640u,925696u,21168128u,35815424u,122880u,38289408u,19152896u,58728448u,11075584u,12877824u,7348224u,18382848u,34930688u,67093650u,67084401u,67070488u,67039508u,66969615u,66843202u,66578722u,66059265u,65004872u,62907940u,58712961u,50325700u,33550504u};
 auto forces=[&](uint32_t blue){while(blue!=all){bool moved=false;uint32_t b=blue;while(b){int i=__builtin_ctz(b);b&=b-1;uint32_t w=A[i]&~blue;if(w && !(w&(w-1))){blue|=w;moved=true;break;}}if(!moved)return false;}return true;};
 unsigned long long cnt[27]={0};
 #pragma omp parallel
 { unsigned long long local[27]={0};
   #pragma omp for schedule(static)
   for(uint64_t mm=0;mm<(1ull<<n);++mm){if(forces((uint32_t)mm))local[__builtin_popcount((uint32_t)mm)]++;}
   #pragma omp critical
   for(int k=0;k<=n;k++)cnt[k]+=local[k];
 }
 cout<<"polynomial";for(int k=0;k<=n;k++)if(cnt[k])cout<<" "<<k<<":"<<cnt[k];cout<<"\n";
 vector<uint32_t> good; good.reserve(cnt[13]);
 uint32_t comb=(1u<<13)-1,limit=1u<<26;
 while(comb<limit){if(forces(comb))good.push_back(comb);uint32_t x=comb&-comb,y=comb+x;if(y>=limit)break;comb=(((comb&~y)/x)>>1)|y;}
 if(good.size()!=cnt[13]) return 3;
 int P[4][26]={{0,4,5,6,1,2,3,7,8,9,10,12,11,13,17,18,19,14,15,16,20,21,22,23,25,24},{4,0,5,6,1,7,10,2,8,12,3,9,11,17,13,18,19,14,20,23,15,21,25,16,22,24},{0,7,8,9,4,5,6,10,12,11,1,3,2,13,14,15,16,23,24,25,17,18,19,20,21,22},{0,1,2,3,4,6,5,10,12,11,7,9,8,13,14,15,16,17,19,18,23,25,24,20,22,21}};
 auto act=[&](uint32_t x,int g){uint32_t y=0;while(x){int i=__builtin_ctz(x);x&=x-1;y|=1u<<P[g][i];}return y;};
 unordered_set<uint32_t> G;G.reserve(good.size()*2);for(auto x:good)G.insert(x);
 unordered_set<uint32_t> seen;seen.reserve(good.size()*2);map<int,int> hist;map<int,unsigned long long> pointcount;
 int orbits=0;
 for(auto seed:good){if(seen.count(seed))continue;orbits++;vector<uint32_t> q={seed};seen.insert(seed);size_t h=0;while(h<q.size()){auto x=q[h++];for(int g=0;g<4;g++){auto y=act(x,g);if(!G.count(y))return 4;if(seen.insert(y).second)q.push_back(y);}}hist[(int)q.size()]++;}
 for(auto x:good)pointcount[__builtin_popcount(x&((1u<<13)-1))]++;
 cout<<"minimum_sets="<<good.size()<<" orbits="<<orbits<<" orbit_hist";for(auto [z,c]:hist)cout<<" "<<z<<":"<<c;cout<<"\n";
 cout<<"minimum_point_profile";for(auto [z,c]:pointcount)cout<<" "<<z<<":"<<c;cout<<"\nENUMERATE_OK\n";
}
