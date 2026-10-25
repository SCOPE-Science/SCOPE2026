// Independent synchronous recurrence for all binary maps on five states.
// No reverse-BFS or source-code reuse from the primary enumerator.
#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <algorithm>
#include <cstdint>
using namespace std;
int main(int argc,char **argv) {
  if(argc!=2){cerr<<"usage: check_independent <extremal-ids-output>\n";return 2;}
  constexpr int N=5, P=10, ALL=(1<<P)-1;
  int pairs[P][2],num[N][N],p=0;
  for(int x=0;x<N;x++)for(int y=x+1;y<N;y++){pairs[p][0]=x;pairs[p][1]=y;num[x][y]=num[y][x]=p++;}
  uint64_t histogram[11]={}; uint64_t total_sync=0,extcount=0;
  ofstream out(argv[1]);
  uint64_t LIMIT=1;for(int i=0;i<2*N;i++)LIMIT*=N;
  for(uint64_t enc=0;enc<LIMIT;enc++){
    int f[2][N],son[P][2];uint64_t c=enc;
    for(int j=0;j<2;j++)for(int i=0;i<N;i++){f[j][i]=c%N;c/=N;}
    for(int i=0;i<P;i++)for(int j=0;j<2;j++){
      int x=f[j][pairs[i][0]],y=f[j][pairs[i][1]];
      son[i][j]=(x==y)?P:num[x][y];
    }
    int d[P]={};unsigned mask=0;
    for(int len=1;len<=P && mask!=ALL;len++){
      unsigned next=mask;
      for(int i=0;i<P;i++)if(!(mask&(1<<i))) {
        bool possible=false;
        for(int j=0;j<2;j++)if(son[i][j]==P||(mask&(1<<son[i][j])))possible=true;
        if(possible){next|=1<<i;d[i]=len;}
      }
      if(next==mask)break;
      mask=next;
    }
    if(mask!=ALL)continue;
    total_sync++;
    int tau=0;
    for(int i=0;i<N;i++){
      int best=P+1;
      for(int j=0;j<N;j++)if(j!=i)best=min(best,d[num[i][j]]);
      tau=max(tau,best);
    }
    histogram[tau]++;
    if(tau==5){out<<enc<<'\n';extcount++;}
    if(tau>5){cerr<<"unexpected upper bound violation\n";return 3;}
  }
  cout<<"independent total="<<LIMIT<<" synchronizing="<<total_sync<<" threshold5="<<extcount<<'\n';
  for(int i=0;i<11;i++)if(histogram[i])cout<<"independent tau_"<<i<<'='<<histogram[i]<<'\n';
}
