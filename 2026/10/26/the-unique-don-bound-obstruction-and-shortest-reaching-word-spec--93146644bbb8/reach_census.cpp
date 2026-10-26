#include <bits/stdc++.h>
using namespace std;
int main(int argc,char **argv){
 int n=argc>1?atoi(argv[1]):8;
 if(n<3||n>8)return 2;
 int U=1<<n, full=U-1; vector<uint8_t> rot(U),bits(U),sz(U);
 for(int m=0;m<U;m++){rot[m]=((m<<1)&full) | (m>>(n-1));sz[m]=__builtin_popcount((unsigned)m);}
 long long base=1;for(int j=0;j<n;j++)base*=n;
 long long rankm=0,cr=0,donviol=0;vector<int> M(n+1,-1); vector<long long> extcnt(n+1,0),violsize(n+1,0);
 vector<map<int,long long>> sizew(n+1); map<int,long long> maxprof;
 vector<long long> allw(n+1);vector<array<int,8>> examples(n+1);
 int donexsize=0;long long donexcode=-1; vector<uint8_t> bmap(U),dist(U),queue(U);array<int,8> f{};
 for(long long id=0;id<base;id++){
   long long x=id;unsigned int im=0;
   for(int i=0;i<n;i++){f[i]=x%n;x/=n;im|=1u<<f[i];}
   if(__builtin_popcount(im)!=n-1) continue;
   rankm++;
   bmap[0]=0;
   for(int m=1;m<U;m++){int low=__builtin_ctz((unsigned)m);bmap[m]=bmap[m&(m-1)] | (1<<f[low]);}
   std::fill(dist.begin(),dist.end(),255);
   int hd=0,tl=1;queue[0]=full;dist[full]=0;
   while(hd<tl){int s=queue[hd++];int ns1=rot[s],ns2=bmap[s];
     if(dist[ns1]==255){dist[ns1]=dist[s]+1;queue[tl++]=ns1;}
     if(dist[ns2]==255){dist[ns2]=dist[s]+1;queue[tl++]=ns2;}
   }
   if(tl!=U-1)continue;
   cr++;
   vector<int> cur(n+1,0);
   bool violation=false;
   for(int s=1;s<full;s++){
     int k=sz[s];int d=dist[s];cur[k]=max(cur[k],d);
     if(d>n*(n-k)){if(!violation){donexsize=k;donexcode=id;}violation=true;violsize[k]++;}
   }
   if(violation)donviol++;
   for(int k=1;k<n;k++){
     sizew[k][cur[k]]++;
     if(cur[k]>M[k]){M[k]=cur[k];extcnt[k]=1;examples[k]=f;}
     else if(cur[k]==M[k])extcnt[k]++;
   }
   int maxv=*max_element(cur.begin()+1,cur.begin()+n);
   maxprof[maxv]++;
 }
 cout<<"{\"n\":"<<n<<",\"rank_n_minus_1_maps\":"<<rankm<<",\"completely_reachable_normalized\":"<<cr<<",\"don_violating_normalized\":"<<donviol<<",\"first_violation_code\":"<<donexcode<<",\"last_violation_size\":"<<donexsize<<",\"per_size\":[";
 for(int k=1;k<n;k++){
  if(k>1)cout<<",";
  cout<<"{\"k\":"<<k<<",\"max\":"<<M[k]<<",\"extremizers\":"<<extcnt[k]<<",\"example_f\":[";
  for(int i=0;i<n;i++){if(i)cout<<",";cout<<examples[k][i];}
  cout<<"],\"threshold_distribution\":{";bool first=true;for(auto &it:sizew[k]){if(!first)cout<<",";first=false;cout<<"\""<<it.first<<"\":"<<it.second;}cout<<"}}";
 }
 cout<<"],\"max_profile\":{";bool first=true;for(auto &it:maxprof){if(!first)cout<<",";first=false;cout<<"\""<<it.first<<"\":"<<it.second;}cout<<"}}\n";
}
