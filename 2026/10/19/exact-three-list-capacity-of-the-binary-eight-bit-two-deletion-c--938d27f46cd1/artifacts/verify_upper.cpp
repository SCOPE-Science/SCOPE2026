#include <bits/stdc++.h>
using namespace std;
using U=unsigned long long;
// fixed integer LP dual, denominator 135
// A received word is indexed by its six binary bits, in lexicographic order.
// The integer certificate weight is nonnegative, with denominator 135.
U rowmask[64]; int ww[64]; int ps[64]; int wt[256],disty[256][64],ntight;long long nodes=0;const long long maxnodes=250000000;
int pc(U x){return __builtin_popcountll(x);} 
bool dfs(U sel,U avail,int fixedcount,int budget){
  nodes++; if(nodes>maxnodes) return false;
  // Every unselected codeword has at most one subsequent branch; forced
  // output counts of three are maintained exactly.
  int cnt=fixedcount+pc(sel);
  if(cnt>24||cnt+pc(avail)<24)return false;
  U sa=avail,ss=sel;
  while(true){
   bool changed=false;
   int mind=999999, best=-1,bestneed=0;
   // Lower bound on the sum of final output-capacity defects.
   int mincost=0;
   for(int y=0;y<64;y++){
    int c=ps[y]+pc(rowmask[y]&ss); if(c>3)return false;
    U rmask=rowmask[y]&sa;int d=pc(rmask);int need=3-c;
    if(ww[y]>0){mincost +=ww[y]*max(0,need-d);if(mincost>budget)return false;}
    // If a positive-weight output has unused capacity and weight
    // exceeding the entire remaining defect budget, it must be saturated.
    bool exact=ww[y]>budget;
    if(exact&&d<need)return false;
    if(need==0){if(rmask){sa &= ~rmask;changed=true;break;}continue;}
    if(exact){
      if(d==need){ss|=rmask;sa&=~rmask;changed=true;break;}
      // num combinations min; degree up to 20
      int choices=1;for(int i=1;i<=need;i++){choices=choices*(d-i+1)/i;if(choices>mind) break;}
      if(choices<mind){mind=choices;best=y;bestneed=need;}
    }
   }
   if(changed)continue;
   int cnt2=fixedcount+pc(ss);if(cnt2>24||cnt2+pc(sa)<24)return false;
   if(best==-1){
    if(cnt2==24){return true;}
    if(sa==0)return false;
    // fallback: choose any candidate and branch
    U bit=sa&-sa;
    if(dfs(ss|bit,sa^bit,fixedcount,budget))return true;
    return dfs(ss,sa^bit,fixedcount,budget);
   }
   U rm=rowmask[best]&sa;
   vector<int> bs;while(rm){int i=__builtin_ctzll(rm);rm&=rm-1;bs.push_back(i);}
   // select exactly need and exclude rest; combinations recursion
   U bits[64];int d=bs.size();for(int i=0;i<d;i++)bits[i]=1ULL<<bs[i];
   auto process=[&](U pick)->bool{
      U candidates=rowmask[best]&sa;
      return dfs(ss|pick,sa&~candidates,fixedcount,budget);
   };
   if(bestneed==1){for(int i=0;i<d;i++)if(process(bits[i]))return true;}
   else if(bestneed==2){for(int i=0;i<d;i++)for(int j=i+1;j<d;j++)if(process(bits[i]|bits[j]))return true;}
   else if(bestneed==3){for(int i=0;i<d;i++)for(int j=i+1;j<d;j++)for(int k=j+1;k<d;k++)if(process(bits[i]|bits[j]|bits[k]))return true;}
   else {cerr<<"unexpected need "<<bestneed<<"\n";exit(4);}
   return false;
  }
}
int main(){
 // Exact integer dual coefficients; the proof does not depend on how they were found.
 const int yy[64]={99,36,4,36,16,0,0,63,16,0,0,0,4,17,32,36,4,0,0,17,0,5,18,0,0,30,18,0,32,0,10,36,36,10,0,32,0,18,30,0,0,18,5,0,17,0,0,4,36,32,17,4,0,0,0,16,63,0,0,16,36,4,36,99};
 int sum_w=0; for(int j=0;j<64;j++){if(yy[j]<0)return 7; ww[j]=yy[j];sum_w+=yy[j];}
 if(3*sum_w+2*36!=3246)return 7;
 // binary subsequence membership
 auto contains=[](int x,int y){int i=0;for(int p=7;p>=0;p--){if(i<6 && ((x>>p)&1)==((y>>(5-i))&1))i++;}return i==6;};
 for(int x=0;x<256;x++)for(int y=0;y<64;y++)disty[x][y]=contains(x,y);
 int zz[256]={};zz[0]=zz[255]=36;
 vector<int>tight,other;
 for(int x=0;x<256;x++){
  int s=zz[x]-135;for(int y=0;y<64;y++)s+=ww[y]*disty[x][y];
  if(s<0){cerr<<"NOT DUAL "<<x<<" "<<s<<"\n";return 3;}
  wt[x]=s;
  if(s==0)tight.push_back(x); else if(s<=6)other.push_back(x);
 }
 ntight=tight.size();if(ntight!=54||other.size()!=32)return 4;
 for(int k=0;k<ntight;k++)for(int y=0;y<64;y++)if(disty[tight[k]][y])rowmask[y] |=1ULL<<k;
 int i0=-1,i1=-1;for(int j=0;j<ntight;j++){if(tight[j]==0)i0=j;if(tight[j]==255)i1=j;}
 if(i0<0||i1<0)return 4;
 U initial=(1ULL<<i0)|(1ULL<<i1),all=(1ULL<<ntight)-1;
 vector<vector<int>>sets;sets.push_back({});
 // All low positive slack words in a size-24 code form a subset
 // with total slack <=6. Minimum positive slack is two; hence
 // all such subsets have at most three elements.
 for(int i=0;i<(int)other.size();i++){
   auto s=vector<int>{other[i]};sets.push_back(s);
   for(int j=i+1;j<(int)other.size();j++)if(wt[other[i]]+wt[other[j]]<=6){sets.push_back({other[i],other[j]});
    for(int k=j+1;k<(int)other.size();k++)if(wt[other[i]]+wt[other[j]]+wt[other[k]]<=6)sets.push_back({other[i],other[j],other[k]});
   }
 }
 if(sets.size()!=113){cerr<<"BAD_CASE_COUNT "<<sets.size()<<"\n";return 8;}
 long long cases=0;
 for(auto &P:sets){
  int s=0;for(int x:P)s+=wt[x];
  if(s>6)continue;
  for(int y=0;y<64;y++){ps[y]=0;for(int x:P)ps[y]+=disty[x][y];}
  bool bad=false;
  for(int y=0;y<64;y++) if(ps[y]>3)bad=true;
  if(bad)continue;
  cases++;
  if(dfs(initial,all&~initial,(int)P.size(),6-s)){
   cout<<"FOUND_24 Unexpected, candidate set = ";for(int x:P)cout<<x<<" ";cout<<"\n";return 2;
  }
  if(nodes>maxnodes){cout<<"LIMIT_REACHED "<<nodes<<" cases "<<cases<<"\n";return 5;}
 }
 if(cases!=113)return 9;
 cout<<"INFEASIBLE_24_EXACT cases="<<cases<<" total_sets="<<sets.size()<<" nodes="<<nodes<<" tight="<<ntight<<" other="<<other.size()<<"\n";
 return 0;
}
