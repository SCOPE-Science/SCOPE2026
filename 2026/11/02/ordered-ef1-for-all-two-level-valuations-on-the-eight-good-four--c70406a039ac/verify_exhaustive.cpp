#include <bits/stdc++.h>
using namespace std;
using ull=uint64_t;
constexpr int G[8]={0,0,0,1,1,1,2,2};
constexpr int WORDS=14, MAXA=864;
vector<array<uint8_t,4>> A;
void rec(vector<int> rem,vector<int> pairs){
 if(rem.empty()){
  sort(pairs.begin(),pairs.end());
  do {array<uint8_t,4> a;for(int j=0;j<4;j++)a[j]=pairs[j];A.push_back(a);}while(next_permutation(pairs.begin(),pairs.end()));return;
 }
 int a=rem[0];for(int j=1;j<(int)rem.size();j++){
  int b=rem[j];if(G[a]==G[b])continue;
  vector<int> nr;for(int k=1;k<(int)rem.size();k++)if(k!=j)nr.push_back(rem[k]);
  pairs.push_back((1<<a)|(1<<b));rec(nr,pairs);pairs.pop_back();
 }
}
int main(int argc,char**argv){rec({0,1,2,3,4,5,6,7},{});
 if(A.size()!=MAXA){cerr<<"wrong alloc count "<<A.size()<<"\n";return 2;}
 static uint8_t pc[256][256];for(int v=0;v<256;v++)for(int p=0;p<256;p++)pc[v][p]=__builtin_popcount((unsigned)(v&p));
 static ull valid[3][256][WORDS],win[MAXA][4];
 for(int a=0;a<MAXA;a++){
  for(int v=0;v<256;v++){
   int x[4];for(int i=0;i<4;i++)x[i]=pc[v][A[a][i]];
   if(x[0]>=max(x[1],max(x[2],x[3])))win[a][v>>6]|=1ull<<(v&63);
   for(int i=1;i<4;i++){
    bool ok=true;
    for(int j=0;j<4;j++)if(j!=i){
     if((i<j&&x[i]<x[j])||(x[i]==0&&x[j]==2)){ok=false;break;}
    }
    if(ok)valid[i-1][v][a>>6]|=1ull<<(a&63);
   }
  }
 }
 ull total=0,fail=0,minEligible=ULLONG_MAX;
 for(int v1=0;v1<256;v1++)for(int v2=0;v2<256;v2++){
  ull BC[WORDS];for(int w=0;w<WORDS;w++)BC[w]=valid[0][v1][w]&valid[1][v2][w];
  for(int v3=0;v3<256;v3++){
   ull cover[4]={};unsigned num=0;
   for(int w=0;w<WORDS;w++){
    ull mask=BC[w]&valid[2][v3][w];
    while(mask){int bit=__builtin_ctzll(mask);int a=w*64+bit;num++;
      for(int u=0;u<4;u++)cover[u]|=win[a][u];
      if((cover[0]&cover[1]&cover[2]&cover[3])==~0ull)goto done;
      mask&=mask-1;
    }
   }
   done:;
   total++;
   if(num<minEligible)minEligible=num;
   if((cover[0]&cover[1]&cover[2]&cover[3])!=~0ull){
    fail++;if(fail<=3){int v0=-1;for(int i=0;i<256;i++)if(!(cover[i>>6]>>(i&63)&1)){v0=i;break;}
     cerr<<"COUNTEREXAMPLE "<<v0<<" "<<v1<<" "<<v2<<" "<<v3<<" candidates="<<num<<"\n";}
    if(argc>1&&string(argv[1])=="--first")return 1;
   }
  }
 }
 cout<<"allocations="<<MAXA<<" checked triples="<<total<<" binary preference profiles="<<total*256ull<<" failed triples="<<fail<<" min_used="<<minEligible<<"\n";
 return fail?1:0;
}
