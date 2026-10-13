#include <bits/stdc++.h>
using namespace std;
array<int,3> w(int x){return {x/16,(x/4)%4,x%4};}
bool direct_ipp(const vector<int>& C){
 int n=C.size(); vector<array<int,3>> a(n); for(int i=0;i<n;i++)a[i]=w(C[i]);
 unsigned inter[64]{}; bool seen[64]{};
 for(int i=0;i<n;i++) for(int j=i;j<n;j++){
   unsigned pm=(1u<<i)|(1u<<j);
   for(int m=0;m<8;m++){
     int dig[3];
     for(int t=0;t<3;t++) dig[t]=((m>>t)&1)?a[j][t]:a[i][t];
     int y=16*dig[0]+4*dig[1]+dig[2];
     if(!seen[y]){seen[y]=1;inter[y]=pm;} else inter[y]&=pm;
   }
 }
 for(int y=0;y<64;y++) if(seen[y]&&inter[y]==0) return false;
 return true;
}
string canon(const vector<int>& C){
 int n=C.size(); vector<array<int,3>> a(n); for(int i=0;i<n;i++)a[i]=w(C[i]);
 vector<int> p(n); iota(p.begin(),p.end(),0); string best(1000,'~');
 int cp[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
 do{for(auto &co:cp){string s;for(int jj=0;jj<3;jj++){int j=co[jj],mp[4]={-1,-1,-1,-1},nx=0;for(int ii=0;ii<n;ii++){int v=a[p[ii]][j];if(mp[v]<0)mp[v]=nx++;s+=char('0'+mp[v]);}s+='|';}best=min(best,s);}}while(next_permutation(p.begin(),p.end()));
 return best;
}
int main(){
 long long cnt0=0; map<string,long long> cls; map<string,vector<int>> rep;
 for(int a=1;a<64;a++)for(int b=a+1;b<64;b++)for(int c=b+1;c<64;c++)for(int d=c+1;d<64;d++){
   vector<int>C={0,a,b,c,d}; if(direct_ipp(C)){cnt0++; auto k=canon(C); cls[k]++; if(!rep.count(k))rep[k]=C;}
 }
 const long long group=6LL*24*24*24; long long total=cnt0*64/5;
 cout<<"VERIFY_OK containing_zero="<<cnt0<<" labeled_maxima="<<total<<" classes="<<cls.size()<<" group="<<group<<"\n";
 long long sum=0; int i=0; for(auto &kv:cls){long long orb=kv.second*64/5,stab=group/orb;sum+=orb;cout<<"class"<<++i<<" normalized="<<kv.second<<" orbit="<<orb<<" stabilizer="<<stab<<" canon="<<kv.first<<" rep=";for(int x:rep[kv.first]){auto a=w(x);cout<<a[0]<<a[1]<<a[2]<<",";}cout<<"\n";}
 cout<<"orbit_sum="<<sum<<"\n";
 if(cnt0!=4320||total!=55296||cls.size()!=3||sum!=total) return 2;
}
