// Independent enumeration by unique collision-pair, missing output and duplicate output.
// Independent wavefront recursion for shortest-image lengths and multiplicities.
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
using namespace std;
int main(){
 constexpr int n=8, full=255;
 array<int,256> cyclic{},weight{};
 for(int m=0;m<256;m++){cyclic[m]=(m<<1&255)|(m>>7);weight[m]=__builtin_popcount((unsigned)m);}
 uint64_t enumerated=0,completely=0,violating=0;map<int,uint64_t> words_hist,badcount_hist,subset_hist,delta_hist,hardlen_hist;uint64_t other_violations=0;
 for(int p=0;p<n;p++)for(int q=p+1;q<n;q++)
 for(int missing=0;missing<n;missing++)for(int duplic=0;duplic<n;duplic++){
  if(duplic==missing)continue;
  array<int,6> inputs{},outputs{};int ii=0,oo=0;
  for(int i=0;i<n;i++){if(i!=p&&i!=q)inputs[ii++]=i;if(i!=missing&&i!=duplic)outputs[oo++]=i;}
  sort(outputs.begin(),outputs.end());
  do{
   array<int,8> f{};f[p]=duplic;f[q]=duplic;
   for(int i=0;i<6;i++)f[inputs[i]]=outputs[i];
   enumerated++;
   array<unsigned char,256> fm{},dist{};
   fm[0]=0;for(int s=1;s<=full;s++){
     int bit=__builtin_ctz((unsigned)s);
     fm[s]=fm[s&(s-1)] | (1<<f[bit]);
   }
   dist.fill(255);dist[full]=0;
   array<uint64_t,256> ways{};ways[full]=1;
   int found=1;
   for(int level=0;level<255;level++){
     bool any=false;
     for(int state=1;state<=full;state++) if(dist[state]==level){
       for(int letter=0;letter<2;letter++){
         int nxt=letter?fm[state]:cyclic[state];
         if(dist[nxt]==255){dist[nxt]=level+1;found++;}
         if(dist[nxt]==level+1){ways[nxt]+=ways[state];any=true;}
       }
     }
     if(!any)break;
   }
   if(found!=255)continue;
   completely++;
   int hardnum=0,hard=0;
   for(int state=1;state<full;state++){
      if(weight[state]!=6){if(dist[state]>8*(8-weight[state]))other_violations++;continue;}
      if(dist[state]>16){hardnum++;hard=state;hardlen_hist[dist[state]]++;}
   }
   if(!hardnum)continue;
   violating++;
   badcount_hist[hardnum]++;
   if(hardnum!=1){cerr<<"unexpected multiple";return 3;}
   words_hist[(int)ways[hard]]++;
   subset_hist[hard]++;
   delta_hist[(duplic-missing+n)%n]++;
  }while(next_permutation(outputs.begin(),outputs.end()));
 }
 cout<<"enumerated="<<enumerated<<" completely="<<completely<<" violating="<<violating<<" other_size_violations="<<other_violations<<"\n";
 auto print=[](const char *name,const auto &mp){cout<<name<<": ";for(auto [k,v]:mp)cout<<k<<"="<<v<<" ";cout<<"\n";};
 print("shortest_words",words_hist);print("hard_sets",badcount_hist);print("hard_targets",subset_hist);print("hard_lengths",hardlen_hist);print("excluded_to_duplicated",delta_hist);
}
