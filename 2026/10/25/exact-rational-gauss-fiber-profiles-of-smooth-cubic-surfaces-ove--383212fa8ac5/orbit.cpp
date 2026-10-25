#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
vector<array<int,4>> exps;
map<array<int,4>,int> idx;
array<array<U,20>,4> transforms;

U subst_monom(int i,int kind){
 // substitute into monomial by brute polynomial over F2 with encoded exponents packed 3 bits each
 map<array<int,4>,int> p; array<int,4> z={0,0,0,0};p[z]=1;
 for(int v=0;v<4;v++)for(int n=0;n<exps[i][v];n++){
  map<array<int,4>,int> q;
  for(auto [e,c]:p){
   if(!c)continue;
   auto t=e;
   int w=v;
   if(kind<3){if(v==kind)w=kind+1;else if(v==kind+1)w=kind;}
   t[w]++;q[t]^=1;
   if(kind==3&&v==0){t=e;t[1]++;q[t]^=1;}
  }
  p=q;
 }
 U y=0;
 for(auto [e,c]:p)if(c){auto it=idx.find(e);if(it==idx.end()){cerr<<"bad exp";exit(1);}y^=1u<<it->second;}
 return y;
}
U action(U mask,int kind){U out=0;while(mask){int i=__builtin_ctz(mask);mask&=mask-1;out^=transforms[kind][i];}return out;}
int main(){
 for(int i=0;i<=3;i++)for(int j=0;j+i<=3;j++)for(int k=0;k+i+j<=3;k++){
  int l=3-i-j-k;array<int,4> e={i,j,k,l};idx[e]=exps.size();exps.push_back(e);
 }
 for(int t=0;t<4;t++)for(int i=0;i<20;i++)transforms[t][i]=subst_monom(i,t);
 vector<unsigned char> seen(1<<20,0);vector<U> reps;
 vector<int> orbit_sizes;
 for(U x=1;x<(1u<<20);x++){
  if(seen[x])continue;
  vector<U> q={x};seen[x]=1;
  for(size_t pos=0;pos<q.size();pos++){
   U y=q[pos];for(int g=0;g<4;g++){
    U z=action(y,g);if(!seen[z]){seen[z]=1;q.push_back(z);}
   }
  }
  reps.push_back(x);orbit_sizes.push_back(q.size());
 }
 cout<<"mask,orbit_size\n";
 for(size_t i=0;i<reps.size();i++)cout<<reps[i]<<","<<orbit_sizes[i]<<"\n";
}
