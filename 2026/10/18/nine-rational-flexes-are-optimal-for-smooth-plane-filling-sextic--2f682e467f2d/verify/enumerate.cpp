#include <iostream>
#include <cstdint>
#include <array>
#include <fstream>
#include "jet_data.h"
using namespace std;
inline int mod3(int n){ n%=3;return n<0?n+3:n; }
int main(){
 int dig[15]={0}, Z[13][5]={};
 uint64_t freq[14]={},count_ok=0,nonzero=0;
 uint64_t profile[14][14]={};
 int maxflex=-1; array<int,15> winner{}; array<int,15> lastwinner{};
 ofstream out("flex_masks_9_11.txt");
 const int total=14348907;
 for(int index=0;index<total;index++){
  if(index){
   int k=0;while(dig[k]==2){dig[k]=0;k++;}dig[k]++;
   for(int p=0;p<13;p++)for(int j=0;j<5;j++)Z[p][j]=mod3(Z[p][j]+J[k][p][j]);
   // lower digits went 2 -> 0, equivalent +1 modulo3
   for(int m=0;m<k;m++)for(int p=0;p<13;p++)for(int j=0;j<5;j++)Z[p][j]=mod3(Z[p][j]+J[m][p][j]);
  }
  if(index==0)continue;
  int flex=0,sing=0;
  for(int p=0;p<13;p++){
   int a=Z[p][0],b=Z[p][1];
   if(!a&&!b){sing++;continue;}
   int c=Z[p][2],d=Z[p][3],e=Z[p][4];
   int H=(c*(b!=0)-d*a*b+e*(a!=0))%3;
   if(H==0)flex++;
  }
  profile[sing][flex]++;
  if(sing==0){count_ok++;freq[flex]++;if(flex>maxflex){maxflex=flex;for(int i=0;i<15;i++)winner[i]=dig[i];cerr<<"NEW MAX "<<maxflex<<" index "<<index<<"\n";}
   if(flex==9 || flex==11){for(int i=0;i<15;i++)out<<dig[i];out<<' '<<flex<<'\n';}
  }
 }
 cout<<"total="<<total-1<<" rational-smooth="<<count_ok<<" maxflex="<<maxflex<<"\n";
 for(int f=0;f<=13;f++)if(freq[f])cout<<"f "<<f<<" count "<<freq[f]<<"\n";
 cout<<"winner=";for(int k:winner)cout<<k;cout<<'\n';
 for(int s=0;s<=13;s++){uint64_t tot=0;for(int f=0;f<=13;f++)tot+=profile[s][f]; if(tot)cout<<"sing "<<s<<" count "<<tot<<'\n';}
}
