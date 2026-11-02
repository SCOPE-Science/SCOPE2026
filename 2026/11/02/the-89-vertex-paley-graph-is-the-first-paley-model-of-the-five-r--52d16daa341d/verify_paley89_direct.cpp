#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <chrono>
using namespace std;
int main(){
 const int q=89;
 vector<int> square(q,0);
 for(int a=1;a<q;a++)square[(a*a)%q]=1;
 bool edge[q][q]={};
 for(int x=0;x<q;x++)for(int y=0;y<q;y++)if(x!=y)edge[x][y]=square[(x-y+q)%q];
 uint64_t tested=0; int minpatterns=16; int min_witness[4]={};
 auto st=chrono::steady_clock::now();
 for(int a=0;a<q;a++)for(int b=a+1;b<q;b++)for(int c=b+1;c<q;c++)for(int d=c+1;d<q;d++){
  uint16_t seen=0;
  for(int z=0;z<q;z++){
   if(z==a||z==b||z==c||z==d)continue;
   int pattern=(edge[z][a]<<0)|(edge[z][b]<<1)|(edge[z][c]<<2)|(edge[z][d]<<3);
   seen|=uint16_t(1u<<pattern);
   if(seen==65535u)break;
  }
  int cnt=__builtin_popcount((unsigned)seen);
  if(cnt<minpatterns){minpatterns=cnt;min_witness[0]=a;min_witness[1]=b;min_witness[2]=c;min_witness[3]=d;}
  if(seen!=65535u){cout<<"FAIL "<<a<<" "<<b<<" "<<c<<" "<<d<<" mask "<<seen<<endl;return 1;}
  tested++;
 }
 auto sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();
 cout<<"PASS exhaustive-89 all-four-subsets="<<tested<<" min-pattern-count="<<minpatterns<<" witness="<<min_witness[0]<<","<<min_witness[1]<<","<<min_witness[2]<<","<<min_witness[3]<<" seconds="<<sec<<"\n";
 return 0;
}
