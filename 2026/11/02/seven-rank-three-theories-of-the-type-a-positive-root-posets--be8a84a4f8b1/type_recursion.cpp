#include<bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 int maxn=argc>1?atoi(argv[1]):27;
 map<vector<int>,int> global1,global2,global3; // deterministic type IDs
 vector<vector<int>> groups;
 for(int n=1;n<=maxn;n++){
  vector<pair<int,int>> a; for(int i=0;i<n;i++)for(int j=i;j<n;j++)a.emplace_back(i,j);
  int N=a.size();
  vector<uint8_t> less(N*N,0);for(int i=0;i<N;i++)for(int j=0;j<N;j++){
   less[i*N+j]=(a[j].first<=a[i].first && a[i].second<=a[j].second && i!=j);
  }
  vector<int> pairtypes(N*N);
  vector<int> buf;buf.reserve(512);
  for(int x=0;x<N;x++)for(int y=0;y<N;y++){
   bool seen[512]={0};
   for(int z=0;z<N;z++){
    int o[3]={x,y,z},b=0;
    b+=(x==y)<<0;b+=(x==z)<<1;b+=(y==z)<<2;
    b+=less[x*N+y]<<3;b+=less[y*N+x]<<4;
    b+=less[x*N+z]<<5;b+=less[z*N+x]<<6;
    b+=less[y*N+z]<<7;b+=less[z*N+y]<<8;
    seen[b]=true;
   }
   buf.clear();for(int i=0;i<512;i++)if(seen[i])buf.push_back(i);
   auto [it,ins]=global1.emplace(buf,global1.size());
   pairtypes[x*N+y]=it->second;
  }
  vector<int> pointtypes(N);
  for(int x=0;x<N;x++){
   buf.clear();for(int y=0;y<N;y++)buf.push_back(pairtypes[x*N+y]);
   sort(buf.begin(),buf.end());buf.erase(unique(buf.begin(),buf.end()),buf.end());
   auto [it,ins]=global2.emplace(buf,global2.size());
   pointtypes[x]=it->second;
  }
  sort(pointtypes.begin(),pointtypes.end());pointtypes.erase(unique(pointtypes.begin(),pointtypes.end()),pointtypes.end());
  auto[it,ins]=global3.emplace(pointtypes,global3.size());
  printf("n=%02d N=%3d rank3=%d singleton-types=%d rank1-global=%zu rank2-global=%zu\n",n,N,it->second,(int)pointtypes.size(),global1.size(),global2.size());fflush(stdout);
 }
}
