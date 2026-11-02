#include <bits/stdc++.h>
using namespace std;
static int C[9], nxt[9], tags[9], statecnt[9];
// Exact finite saturation and tagged-origin certificate for the three-state,
// two-neighbor-threshold excitable update on matching-deleted K(n,n).
// Every category count is saturated at 3. The nine original categories
// retain their own trajectories; absent categories never contribute.
// All loops use integer arithmetic; no sampling or numerical approximation.
int main(){
 map<pair<int,int>, vector<int>> samples;
 map<pair<int,int>,long long> dc;map<pair<int,int>,int> ex;long long cnt=0;int maxT=0;set<int> pers;
 for(int key=1;key<(1<<18);key++){
  int x=key;int sum=0;bool present[9]={};
  for(int i=0;i<9;i++){statecnt[i]=x&3;x>>=2;sum+=statecnt[i];present[i]=statecnt[i]>0;tags[i]=present[i]?i:0;}
  if(!sum)continue;
  unordered_map<uint64_t,int> seen;
  int T=-1,p=-1;
  for(int t=0;t<100;t++){
    uint64_t sk=0;for(int i=8;i>=0;i--)sk=sk*4+statecnt[i];
    uint64_t sig=0;
    for(int i=8;i>=0;i--)sig=sig*9+tags[i];
    uint64_t full=sk+(sig<<18);
    auto z=seen.find(full);
    if(z!=seen.end()){T=z->second;p=t-T;break;}
    seen.emplace(full,t);
    int ea=0,eb=0;for(int i=0;i<9;i++){if(i/3==1)ea+=statecnt[i];if(i%3==1)eb+=statecnt[i];}
    for(int i=0;i<9;i++){
      int a=i/3,b=i%3;
      int aa=a?(a+1)%3:(eb-(b==1)>=2?1:0);
      int bb=b?(b+1)%3:(ea-(a==1)>=2?1:0);
      nxt[i]=aa*3+bb;
    }
    int out[9]={};for(int i=0;i<9;i++)out[nxt[i]]=min(3,out[nxt[i]]+statecnt[i]);
    for(int i=0;i<9;i++)statecnt[i]=out[i];
    for(int i=0;i<9;i++)if(present[i])tags[i]=nxt[tags[i]];
  }
  if(T<0){cerr<<"failed "<<key<<"\n";return 1;}
  dc[{T,p}]++;maxT=max(maxT,T);pers.insert(p);if(!ex.count({T,p}))ex[{T,p}]=key; if(p==30 || (T==0 && p==10)) samples[{T,p}].push_back(key);
  cnt++;
 }
 cout<<"states="<<cnt<<" maxT="<<maxT<<" periods:";for(int p:pers)cout<<" "<<p;cout<<"\n";
 for(auto [tp,c]:dc){auto[t,p]=tp;cout<<"T="<<t<<" p="<<p<<" types="<<c<<" sample="<<ex[tp]<<"\n";}
 if(cnt!=262143 || maxT!=9 || pers!=set<int>({1,3,4,6,10,12,30})) {cerr<<"Global census disagrees\n";return 2;}
 if(dc[{0,30}]!=2 || dc[{9,4}]!=2 || dc[{0,10}]!=2) {cerr<<"Exceptional census disagrees\n";return 3;}
 for(auto [tp,keys]:samples){
   if(tp.second!=30) continue;
   for(int key:keys){int nonzero=0,k=key;
     for(int i=0;i<9;i++){int d=k&3;k>>=2;if(d>1){cerr<<"Period-30 multiplicity obstruction\n";return 4;}nonzero+=d;}
     if(nonzero!=8){cerr<<"Period-30 not restricted to n=8\n";return 5;}
   }
 }
 cout<<"CROWN_GHM2_VERIFY_OK\n";
 for(auto [tp,keys]:samples){cout<<"detail T="<<tp.first<<" p="<<tp.second<<" keys=";for(auto k:keys){cout<<k<<":";int sum=0;int aa=k;for(int i=0;i<9;i++){sum+=aa&3;cout<<(aa&3);aa>>=2;}cout<<":"<<sum<<" ";}cout<<"\n";}
}
