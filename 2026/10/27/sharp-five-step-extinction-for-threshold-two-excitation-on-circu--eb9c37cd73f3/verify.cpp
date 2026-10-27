// Exact finite enumeration for threshold-two Greenberg--Hastings dynamics
// on the two-row periodic ladder. ISO C++17; no external libraries.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
using Rung = int; // a+3*b, a,b in {0,1,2} are the two vertex states.
static int g[9][9][9];
static bool allowed[9][9]{};
static uint64_t language_count=0, output_count[9]{};
static void require(bool b,const char* why){if(!b)throw runtime_error(why);}
static int local(int a,int b,int c){
 int ans=0;
 for(int r=0;r<2;r++){
  int x=(r?b/3:b%3), west=(r?a/3:a%3), east=(r?c/3:c%3), vertical=(r?b%3:b/3);
  int nb=(west==1)+(east==1)+(vertical==1);
  int y=(x==1?2:(x==2?0:(nb>=2?1:0)));
  ans+=y*(r?3:1);
 }
 return ans;
}
static void step(const vector<int>&in, vector<int>&out){
 int n=(int)in.size();out.resize(n);
 for(int i=0;i<n;i++)out[i]=g[in[(i+n-1)%n]][in[i]][in[(i+1)%n]];
}
static int death_time(const vector<int>&initial){
 vector<int>x=initial,y;
 for(int t=0;t<=6;t++){
  bool nonzero=false;
  for(int q:x)if(q)nonzero=true;
  if(!nonzero)return t;
  step(x,y);x.swap(y);
 }
 throw runtime_error("survival beyond six updates");
}
static bool has_excited_at_3(const vector<int>&initial,int col){
 vector<int>x=initial,y;
 for(int t=0;t<3;t++){step(x,y);x.swap(y);}
 return (x[col]%3==1);
}
static void check_len_7(const array<int,7>&w){
 int a[5],b[3];
 for(int i=0;i<5;i++)a[i]=g[w[i]][w[i+1]][w[i+2]];
 for(int i=0;i<3;i++)b[i]=g[a[i]][a[i+1]][a[i+2]];
 int out=g[b[0]][b[1]][b[2]];
 ++language_count;++output_count[out];
 require(out%3!=1 && out/3!=1,"late excitation on locally admissible history");
}
static void walk(int k,array<int,7>&w){
 if(k==7){check_len_7(w);return;}
 for(int next=0;next<9;next++){
  if(k>0 && !allowed[w[k-1]][next])continue;
  w[k]=next;walk(k+1,w);
 }
}
int main(){
 for(int a=0;a<9;a++)for(int b=0;b<9;b++)for(int c=0;c<9;c++)g[a][b][c]=local(a,b,c);
 // Every adjacent pair of t=1 rungs is the image of four t=0 rungs.
 for(int a=0;a<9;a++)for(int b=0;b<9;b++)for(int c=0;c<9;c++)for(int d=0;d<9;d++)
  allowed[g[a][b][c]][g[b][c][d]]=true;
 int pair_count=0;for(auto &row:allowed)for(bool p:row)pair_count+=p;
 require(pair_count==50,"pair-language count");
 array<int,7>w{};walk(0,w);
 require(language_count==589781,"length-seven locally admissible language count");
 require(output_count[0]==589585 && output_count[2]==98 && output_count[6]==98,"time-three local output counts");
 for(int i=0;i<9;i++)if(i!=0 && i!=2 && i!=6)require(output_count[i]==0,"unexpected local output");
 // All possible initial states on the three short cyclic prisms are tested.
 uint64_t enumerated=0;int sizes[3]={3,4,5};
 for(int n:sizes){int total=1;for(int j=0;j<n;j++)total*=9;int maximum=0;
  for(int z=0;z<total;z++){int v=z;vector<int>x(n);for(int i=0;i<n;i++){x[i]=v%9;v/=9;}int d=death_time(x);if(d>maximum)maximum=d;enumerated++;}
  require(maximum==4,"short-cylinder sharp extinction time");
 }
 vector<int>special={1,3,0,3,0,3};
 require(death_time(special)==5 && has_excited_at_3(special,3),"six-column witness");
 for(int n=7;n<=80;n++){
  vector<int>x(n,0);int witness[]={1,3,0,3,0,3,1};
  for(int j=0;j<7;j++)x[j]=witness[j];
  require(death_time(x)==5 && has_excited_at_3(x,3),"long-cylinder witness");
 }
 cout<<"ALLOWED_PAIRS="<<pair_count<<"\n";
 cout<<"LOCAL_WORDS="<<language_count<<"\n";
 cout<<"LATE_OUTPUT_COUNTS=0:"<<output_count[0]<<",2:"<<output_count[2]<<",6:"<<output_count[6]<<"\n";
 cout<<"SHORT_STATES_ENUMERATED="<<enumerated<<"\n";
 cout<<"SHARP_WITNESSES_N=6..80_OK\n";
 cout<<"VERIFY_OK\n";
}
