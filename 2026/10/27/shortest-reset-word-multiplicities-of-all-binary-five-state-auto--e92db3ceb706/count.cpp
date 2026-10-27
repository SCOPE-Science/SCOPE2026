#include <bits/stdc++.h>
using namespace std;
const int N=5, MAPS=3125, SS=32;
static uint8_t act[MAPS][SS];
static unsigned long long hist[18][2], unique_hist[18][2], totalw[18][2];
static map<unsigned long long,unsigned long long> mult_hist;
static unsigned long long total=0,non=0,unique_count=0,max_mult=0,nmax=0;
static int max_mult_len=0,max_a=0,max_b=0;
int main(){
 for(int a=0;a<MAPS;a++){
  int m=a, t[5]; for(int i=0;i<5;i++){t[i]=m%5;m/=5;}
  act[a][0]=0;
  for(int s=1;s<32;s++){int l=__builtin_ctz((unsigned)s);act[a][s]=act[a][s&(s-1)]|(1<<t[l]);}
 }
 auto start=chrono::steady_clock::now();
 for(int a=0;a<MAPS;a++) for(int b=0;b<MAPS;b++){
  uint8_t dist[32]; unsigned int ways[32]={0};
  memset(dist,255,sizeof(dist));
  uint8_t queue[32]; int head=0,tail=0;
  queue[tail++]=31;dist[31]=0;ways[31]=1;
  int best=99; unsigned long long num=0;
  while(head<tail){
   int s=queue[head++],d=dist[s];
   if(d>=best) break;
   int nxt[2]={act[a][s],act[b][s]};
   for(int z=0;z<2;z++){
    int t=nxt[z];
    if((t&(t-1))==0){
     if(d+1<best){best=d+1;num=0;}
     if(d+1==best)num+=ways[s];
    } else if(d+1<best){
     if(dist[t]==255){dist[t]=d+1;ways[t]=ways[s];queue[tail++]=t;}
     else if(dist[t]==d+1)ways[t]+=ways[s];
    }
   }
  }
  if(best==99){non++;continue;}
  total++; hist[best][0]++;
  totalw[best][0]+=num;
  if(num==1){unique_hist[best][0]++;unique_count++;}
  if(num>max_mult){max_mult=num;nmax=1;max_mult_len=best;max_a=a;max_b=b;}
  else if(num==max_mult)nmax++;
  mult_hist[num]++;
 }
 cerr<<"elapsed "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<" seconds\n";
 cout<<"TOTAL "<<total<<" NON "<<non<<" UNIQUE "<<unique_count<<" MAX_MULT "<<max_mult<<" NMAX "<<nmax<<" MAX_LEN "<<max_mult_len<<" WITNESS "<<max_a<<","<<max_b<<"\n";
 for(int d=1;d<18;d++)if(hist[d][0])cout<<"LEN "<<d<<" "<<hist[d][0]<<" UNIQUE "<<unique_hist[d][0]<<" TOTAL_WAYS "<<totalw[d][0]<<"\n";
 cout<<"MULT DISTINCT "<<mult_hist.size()<<"\n";
 for(auto [m,c]:mult_hist)cout<<"M "<<m<<" "<<c<<"\n";
}
