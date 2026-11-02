#include <bits/stdc++.h>
using namespace std;
int main(){
 for(int n:{3,4}){
  vector<array<int,4>> perms;
  array<int,4> x{};iota(x.begin(),x.begin()+n,0);
  do{perms.push_back(x);}while(next_permutation(x.begin(),x.begin()+n));
  int m=perms.size();map<int,long long> counts;map<pair<int,int>,long long> joint;map<int,array<int,4>> sampleidx;map<int,int> pidx;
  long long seen=0;
  int profiles=1;for(int i=1;i<n;i++)profiles*=m;
  for(int idx=0;idx<profiles;idx++){
   int q=idx;array<int,4> pids{};pids[0]=0;
   for(int i=1;i<n;i++){pids[i]=q%m;q/=m;}
   int ranks[4][4];
   for(int i=0;i<n;i++)for(int j=0;j<n;j++)ranks[i][perms[pids[i]][j]]=j;
   uint32_t reach[24]{};
   for(int a=0;a<m;a++){
    reach[a]|=(1u<<a);
    for(int b=0;b<m;b++){
     if(a==b)continue;
     int margin=0;
     for(int i=0;i<n;i++){
      if(ranks[i][perms[a][i]]<ranks[i][perms[b][i]])margin++;
      else if(ranks[i][perms[a][i]]>ranks[i][perms[b][i]])margin--;
     }
     if(margin>=0)reach[a]|=(1u<<b);
    }
   }
   for(int k=0;k<m;k++)for(int i=0;i<m;i++)if(reach[i]&(1u<<k))reach[i]|=reach[k];
   int size=0;uint32_t all=(1u<<m)-1;
   for(int i=0;i<m;i++)if(reach[i]==all)size++;
   int po=0;
   for(int a=0;a<m;a++){
    bool dominated=false;
    for(int b=0;b<m && !dominated;b++){
     if(a==b)continue;
     bool all=true,strict=false;
     for(int i=0;i<n;i++){
       int ra=ranks[i][perms[a][i]],rb=ranks[i][perms[b][i]];
       if(rb>ra){all=false;break;}
       if(rb<ra)strict=true;
     }
     if(all&&strict)dominated=true;
    }
    if(!dominated)po++;
   }
   joint[{size,po}]++;counts[size]++;if(!sampleidx.count(size))sampleidx[size]=pids;
   seen++;
  }
  cout<<"n="<<n<<" fixed_first="<<seen<<" full="<<seen*m<<"\n";
  cout<<"joint sizeTC,sizePO,countLabeled\n";for(auto [z,cnt]:joint)cout<<z.first<<","<<z.second<<","<<cnt*m<<"\n";
  for(auto [k,v]:counts){cout<<"size "<<k<<" fixed "<<v<<" labeled "<<v*m<<" prob "<<setprecision(10)<<(double)v/seen<<" sample ";for(int i=0;i<n;i++){if(i)cout<<"/";for(int j=0;j<n;j++)cout<<perms[sampleidx[k][i]][j];}cout<<"\n";}
 }
}
