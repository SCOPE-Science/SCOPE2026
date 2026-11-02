// Exact finite enumeration for double Roman domination on P(5k,k).
// No third-party libraries: compile with c++ -O3 -std=c++17 petersen_exact.cpp -o petersen_exact.
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <limits>
#include <cstdlib>
using namespace std;
constexpr int Q=243,INF=1000;
using Vec=array<int,5>;
array<Vec,Q> states;
int sum_u[Q], min_v[Q][Q], base_lb[Q];
struct Option {int code,lb;};
vector<Option> options;
int k_global,cap_global,chosen[10];
unsigned long long visited=0,complete=0,found=0;

bool protected_zero(int a,int b,int c){return a==3||b==3||c==3||(a==2)+(b==2)+(c==2)>=2;}
int codeof(const Vec &a){int s=0,mul=1;for(int t=0;t<5;t++){int d=(a[t]==0?0:a[t]==2?1:2);s+=mul*d;mul*=3;}return s;}

void init(){
 for(int s=0;s<Q;s++){
  int tmp=s;
  for(int t=0;t<5;t++){int d=tmp%3;tmp/=3;states[s][t]=(d==0?0:d==1?2:3);}
  sum_u[s]=0;for(int t=0;t<5;t++)sum_u[s]+=states[s][t];
 }
 for(int c=0;c<Q;c++){
  for(int d=0;d<Q;d++) min_v[c][d]=INF;
  for(int v=0;v<Q;v++){
   const Vec &U=states[c], &V=states[v];
   bool ok=true;
   for(int t=0;t<5;t++)if(V[t]==0 && !protected_zero(V[(t+4)%5],V[(t+1)%5],U[t])){ok=false;break;}
   if(!ok)continue;
   int vweight=0;for(int a:V)vweight+=a;
   for(int d=0;d<Q;d++){
    bool works=true;const Vec &D=states[d];
    // Demand codes: 0=no demand, 2=must have 2 or 3, 3=must have 3.
    for(int t=0;t<5;t++) if(V[t]<D[t]){works=false;break;}
    if(works) min_v[c][d]=min(min_v[c][d],vweight);
   }
  }
  base_lb[c]=sum_u[c]+min_v[c][0];
 }
 options.clear();for(int c=0;c<Q;c++)options.push_back({c,base_lb[c]});
 sort(options.begin(),options.end(),[](Option a,Option b){return a.lb<b.lb;});
}

int localDemand(int j){
 Vec D={}; const Vec &cur=states[chosen[j]];
 const Vec &prev=states[chosen[(j+k_global-1)%k_global]];
 const Vec &next=states[chosen[(j+1)%k_global]];
 for(int t=0;t<5;t++){
  int a=(j==0 ? prev[(t+4)%5] : prev[t]);
  int b=(j==k_global-1 ? next[(t+1)%5] : next[t]);
  if(cur[t]!=0 || protected_zero(a,b,0))D[t]=0;
  else D[t]=(a==2||b==2?2:3);
 }
 return codeof(D);
}

void testTuple(){
 complete++;
 int full=0;
 for(int j=0;j<k_global;j++){
  int c=chosen[j], v=min_v[c][localDemand(j)];
  full+=sum_u[c]+v;
  if(full>cap_global)return;
 }
 if(full<=cap_global){
  found++;
  if(found<3){cerr<<"COUNTEREXAMPLE: ";for(int j=0;j<k_global;j++)cerr<<chosen[j]<<",";cerr<<" w="<<full<<"\n";}
 }
}
void recurse(int j,int bound){
 if(j==k_global){testTuple();return;}
 for(auto [c,lb]:options){
  if(lb>bound)break;
  chosen[j]=c;visited++;
  recurse(j+1,bound-lb);
 }
}

bool directCheck(int k,const vector<int> &a,const vector<int> &b){
 int n=5*k; if(int(a.size())!=n||int(b.size())!=n)return false;
 int weight=0;
 for(int i=0;i<n;i++){
  weight+=a[i]+b[i];
  if(a[i]==0&&!protected_zero(a[(i+n-1)%n],a[(i+1)%n],b[i]))return false;
  if(b[i]==0&&!protected_zero(b[(i+n-k)%n],b[(i+k)%n],a[i]))return false;
 }
 cout<<"WITNESS k="<<k<<" weight="<<weight<<" VALID=true\n";
 return true;
}

int main(int argc,char**argv){
 init();
 for(int t=1;t<Q;t++) if(base_lb[t]<6){cerr<<"incorrect bound";return 4;}
 if(argc<2){cerr<<"usage: petersen_exact k [cap]\n";return 2;}
 int k=atoi(argv[1]); int cap=(argc>2?atoi(argv[2]):8*k+1);
 if(k<2||k>8){cerr<<"supported 2<=k<=8\n";return 2;}
 k_global=k;cap_global=cap;
 recurse(0,cap);
 cout<<"LOWER_EXHAUSTIVE k="<<k<<" cap="<<cap<<" explored_partial="<<visited<<" complete_tuples="<<complete<<" feasible_at_most_cap="<<found<<"\n";
 if(found==0)cout<<"CERTIFIED_LOWER_BOUND "<<cap+1<<"\n";
 // Independent upper witnesses obtained directly from graph definition, not local-state tables.
 if(k==4){
  vector<int>a(20),b(20);for(int i:{2,5,9,12,15,19})a[i]=3;for(int i:{4,7,10,17})b[i]=3;for(int i:{16,18})b[i]=2;
  if(!directCheck(4,a,b))return 3;
 }
 if(k==5){
  vector<int>a(25),b(25);for(int i:{1,5,7,9,14,16,18,22,24})a[i]=2;
  for(int i:{2,4,10,13,19,21})b[i]=2;
  for(int i:{3,11,12,20})b[i]=3;
  if(!directCheck(5,a,b))return 3;
 }
 return found==0?0:1;
}
