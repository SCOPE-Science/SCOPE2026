#include<bits/stdc++.h>
using namespace std;
const int adj[20][3]={{1,10,19},{0,2,8},{1,3,6},{2,4,19},{3,5,17},{4,6,15},{2,5,7},{6,8,14},{1,7,9},{8,10,13},{0,9,11},{10,12,18},{11,13,16},{9,12,14},{7,13,15},{5,14,16},{12,15,17},{4,16,18},{11,17,19},{0,3,18}};
uint32_t go(uint32_t s){uint32_t t=0;for(int v=0;v<20;v++){int c=((s>>adj[v][0])&1)+((s>>adj[v][1])&1)+((s>>adj[v][2])&1);t|=uint32_t(c>=2)<<v;}return t;}
int main(){vector<array<int,20>> perms;ifstream fi("automorphisms.csv");string line;while(getline(fi,line)){stringstream ss(line);array<int,20>a;char sep;for(int i=0;i<20;i++){ss>>a[i];if(i<19)ss>>sep;}perms.push_back(a);}if(perms.size()!=120){cerr<<"Not120";return 1;}
 vector<uint32_t> edges(20);for(int v=0;v<20;v++)for(int k=0;k<3;k++)edges[v]|=1u<<adj[v][k];
 for(auto&p:perms){bool taken[20]={};for(int i=0;i<20;i++){if(p[i]<0||p[i]>=20||taken[p[i]])abort();taken[p[i]]=1;}for(int v=0;v<20;v++)for(int k=0;k<3;k++){if(!(edges[p[v]]>>(p[adj[v][k]])&1u)){cerr<<"NOT_AUT";abort();}}}
 auto transform=[](uint32_t x,const array<int,20>&p){uint32_t y=0;while(x){int v=__builtin_ctz(x);y|=1u<<p[v];x&=x-1;}return y;};
 unordered_set<uint32_t> seenFix,seenTwo;int classFix=0,classTwo=0;map<int,int> distribF,distribT;ofstream o("symmetry_classes.tsv");o<<"period\tminimal_state\tclass_size_temporal_orbits\n";
 for(uint32_t x=0;x<(1u<<20);x++){uint32_t y=go(x);if(go(y)!=x)continue;bool fixed=(y==x);auto&seen=fixed?seenFix:seenTwo;if(seen.count(fixed?x:min(x,y)))continue;
  unordered_set<uint32_t> spatial;
  for(auto&p:perms){uint32_t z=transform(x,p);spatial.insert(fixed?z:min(z,go(z)));}
  for(auto z:spatial)seen.insert(z);
  uint32_t minimal=*min_element(spatial.begin(),spatial.end());
  int m=spatial.size();if(fixed){classFix++;distribF[m]++;}else{classTwo++;distribT[m]++;}
  o<<(fixed?1:2)<<"\t"<<minimal<<"\t"<<m<<"\n";
 }
 cout<<"AUT="<<perms.size()<<" GEOMETRIC_FIXED="<<classFix<<" GEOMETRIC_TWOCYCLES="<<classTwo<<"\n";
 cout<<"FIXED_CLASS_SIZE_DIST=";for(auto[k,v]:distribF)cout<<k<<":"<<v<<",";cout<<"\nTWO_CLASS_SIZE_DIST=";for(auto[k,v]:distribT)cout<<k<<":"<<v<<",";cout<<"\n";
 cout<<"FIXED_SPATIAL_SUM="<<seenFix.size()<<" TWO_SPATIAL_ORBITS_SUM="<<seenTwo.size()<<"\n";
}
