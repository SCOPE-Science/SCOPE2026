#include <bits/stdc++.h>
using namespace std;
int S[16],n,pref[6][16],plen[6],images[5],pcnt[32]; uint32_t fullmask;
long long nodes=0;
bool dfs(int d,int used,bool moved){
 if(d==5) return moved;
 for(int j=0;j<n;j++)if(!(used>>j&1)){
  images[d]=S[j];
  if(pcnt[1<<d]!=pcnt[S[j]])continue;
  bool pairgood=true;for(int u=0;u<d;u++){if(pcnt[(1<<d)^(1<<u)]!=pcnt[images[d]^images[u]]){pairgood=false;break;}}
  if(!pairgood)continue;
  int b[5]={},rank=0;
  for(int u=0;u<=d;u++){
    int x=images[u];
    for(int h=4;h>=0;h--) if((x>>h)&1){
      if(b[h]) x^=b[h]; else {b[h]=x;rank++;break;}
    }
  }
  if(rank!=d+1)continue;
  bool ok=true;
  for(int m=0;m<plen[d+1];m++){
   int v=pref[d+1][m],y=0;
   for(int k=0;k<=d;k++)if(v>>k&1)y^=images[k];
   if(!((fullmask>>y)&1)){ok=false;break;}
  }
  if(ok && dfs(d+1, used|(1<<j),moved||(S[j]!=(1<<d))))return true;
 }
 return false;
}

bool is_rigid(int k){n=k;fullmask=0;for(int i=0;i<n;i++)fullmask|=1u<<S[i];
 memset(pcnt,0,sizeof(pcnt)); for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)pcnt[S[i]^S[j]]++;
 for(int d=1;d<=5;d++){plen[d]=0;for(int i=0;i<n;i++)if(S[i]<(1<<d))pref[d][plen[d]++]=S[i];}
 return !dfs(0,0,false);
}
int others[26],chosen[20];long long countTotal=0,countRigid=0;bool printFirst=true;
void comb(int at,int start,int size){
 if(at==size){for(int i=0;i<5;i++)S[i]=1<<i;for(int i=0;i<size;i++)S[5+i]=others[chosen[i]];countTotal++;
  if(is_rigid(size+5)){
   countRigid++;
   if(printFirst){cerr<<"RIGID k="<<size+5<<" set=";for(int i=0;i<5+size;i++)cerr<<S[i]<<",";cerr<<"\n";printFirst=false;}
  }
  return;
 }
 for(int i=start;i<=26-(size-at);i++){chosen[at]=i;comb(at+1,i+1,size);}
}
int main(int argc,char**argv){int lo=(argc>1?atoi(argv[1]):9),hi=(argc>2?atoi(argv[2]):11);
 int at=0;for(int x=1;x<32;x++)if(__builtin_popcount((unsigned)x)!=1)others[at++]=x;
 assert(at==26);
 for(int k=lo;k<=hi;k++){auto begin=chrono::steady_clock::now();countTotal=countRigid=0;printFirst=true;comb(0,0,k-5);
 cout<<"size="<<k<<" normalized_cases="<<countTotal<<" rigid="<<countRigid<<" secs="<<chrono::duration<double>(chrono::steady_clock::now()-begin).count()<<"\n"<<flush;
 }
}
