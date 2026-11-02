// Finite exhaustive verification of the sharp two-colour rook placement census.
// c++ -std=c++17 -O3 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using ULL = unsigned long long;

static ULL fact(int n){ULL f=1;for(int i=2;i<=n;i++)f*=i;return f;}
static ULL choose(int n,int r){ULL q=1;for(int i=1;i<=r;i++)q=q*(n-i+1)/i;return q;}
static ULL derange(int n){if(n==0)return 1;if(n==1)return 0;ULL a=1,b=0;for(int i=2;i<=n;i++){ULL c=(i-1)*(a+b);a=b;b=c;}return b;}

struct Exhaust {
 int n,q,N;
 vector<int> selected;
 ULL total=0, examined=0;
 vector<ULL> byU;
 bool classify(const vector<unsigned char>& state){
   vector<int> rR(n),cR(n),rB(n),cB(n);
   for(int v=0;v<N;v++){
     int i=v/n,j=v%n;
     if(state[v]==1){rR[i]++;cR[j]++;}
     if(state[v]==2){rB[i]++;cB[j]++;}
   }
   vector<int> A,B,C,D,U,V;
   for(int i=0;i<n;i++){
     if(!rR[i])A.push_back(i);
     if(!rB[i])C.push_back(i);
     if(rR[i]&&rB[i])U.push_back(i);
     if(!cR[i])B.push_back(i);
     if(!cB[i])D.push_back(i);
     if(cR[i]&&cB[i])V.push_back(i);
   }
   int u=(int)U.size();
   if(u!=(int)V.size()||A.empty()||B.empty()||C.empty()||D.empty())return false;
   if(A.size()+C.size()+U.size()!=size_t(n))return false;
   if(B.size()+D.size()+V.size()!=size_t(n))return false;
   if(!((A.size()==1||B.size()==1)&&(C.size()==1||D.size()==1)))return false;
   vector<bool> ia(n),ib(n),ic(n),id(n),iu(n),iv(n);
   for(int x:A)ia[x]=1;for(int x:B)ib[x]=1;
   for(int x:C)ic[x]=1;for(int x:D)id[x]=1;
   for(int x:U)iu[x]=1;for(int x:V)iv[x]=1;
   vector<int> rRM(n),cRM(n),rBM(n),cBM(n);
   for(int i=0;i<n;i++)for(int j=0;j<n;j++){
     int val=state[i*n+j];
     if(ic[i]&&id[j]){if(val!=1)return false;continue;}
     if(ia[i]&&ib[j]){if(val!=2)return false;continue;}
     if(iu[i]&&iv[j]){
       if(val==1){rRM[i]++;cRM[j]++;}
       if(val==2){rBM[i]++;cBM[j]++;}
     }else if(val!=0)return false;
   }
   for(int i:U)if(rRM[i]!=1||rBM[i]!=1)return false;
   for(int j:V)if(cRM[j]!=1||cBM[j]!=1)return false;
   byU[u]++;
   return true;
 }
 void inspect(){
   for(int mask=0;mask<(1<<q);mask++){
     vector<unsigned char> st(N,0),rr(n),br(n),rc(n),bc(n);
     for(int t=0;t<q;t++){
       int v=selected[t],i=v/n,j=v%n;
       if((mask>>t)&1){st[v]=2;br[i]++;bc[j]++;}
       else {st[v]=1;rr[i]++;rc[j]++;}
     }
     bool feasible=true;
     for(int i=0;i<n&&feasible;i++)for(int j=0;j<n;j++){
       if(st[i*n+j])continue;
       if(rr[i]+rc[j]==0||br[i]+bc[j]==0){feasible=false;break;}
     }
     examined++;
     if(feasible){
       total++;
       if(q==2*n-2 && !classify(st)){
         cerr<<"CLASSIFICATION_FAILED for n="<<n<<"\n";exit(3);
       }
     }
   }
 }
 void rec(int i){
   if((int)selected.size()==q){inspect();return;}
   for(int t=i;t<=N-(q-(int)selected.size());t++){
     selected.push_back(t);rec(t+1);selected.pop_back();
   }
 }
 ULL run(int size){q=size;total=examined=0;selected.clear();byU.assign(n+1,0);rec(0);return total;}
};
int main(){
 for(int n=2;n<=5;n++){
   Exhaust ex;ex.n=n;ex.N=n*n;
   if(ex.run(2*n-3)!=0){cerr<<"LOWER_BOUND_FAILED n="<<n<<"\n";return 1;}
   ULL observed=ex.run(2*n-2),formula=0;
   for(int u=0;u<=n-2;u++){
     ULL expected=(2-(u==n-2))*ULL(n)*n*choose(n-1,u)*choose(n-1,u)*fact(u)*derange(u);
     if(ex.byU[u]!=expected){cerr<<"SHAPE_CENSUS_FAILED n="<<n<<" u="<<u<<" observed="<<ex.byU[u]<<" expected="<<expected<<"\n";return 2;}
     formula+=expected;
   }
   if(observed!=formula){cerr<<"TOTAL_FAILED\n";return 4;}
   cout<<"EXHAUSTIVE_OPTIMA_OK n="<<n<<" tested="<<ex.examined<<" count="<<observed<<"\n";
 }
 cout<<"CLASSIFICATION_AND_DERANGEMENT_CENSUS_OK n=2..5\nVERIFY_OK\n";
}
