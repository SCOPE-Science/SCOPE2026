#include <bits/stdc++.h>
using namespace std;
using U=unsigned __int128;
constexpr int N=124, n=7;
constexpr U mask=(U(1)<<N)-1;
long long examined=0, pruned=0, leaf=0, valid=0;
vector<array<int,n>> accepted;
int a[n];
inline U rot(U s,int x){return ((s<<x)|(s>>(N-x))) & mask;}
bool fullvalid(){
 const int target=(accumulate(a,a+n,0))%N;
 // build sum set for exact k chosen, counting duplicates of each element allowed; 0 itself normalized.
 int k[n];
 auto visit=[&](auto&& self,int i,int left,int s,bool changed)->bool{
  if(i==n-1){int q=left;return (changed||q!=1) && ((s+q*a[i])%N==target);}
  for(int q=0;q<=left;q++) if(self(self,i+1,left-q,(s+q*a[i])%N,changed||q!=1)) return true;
  return false;
 };
 return !visit(visit,0,n,0,false);
}
void go(int k,int low,U ss){
 if(k==n){leaf++;if(fullvalid()){valid++;array<int,n> r;copy(a,a+n,r.begin());accepted.push_back(r);}return;}
 for(int x=low;x<=N-(n-k);x++){
   examined++;U shifted=rot(ss,x);
   if((ss&shifted)!=0){pruned++;continue;}
   a[k]=x;
   go(k+1,x+1,ss|shifted);
 }
}
int main(){a[0]=0;a[1]=1;go(2,2,U(3));
 cerr<<"examined="<<examined<<" pruned="<<pruned<<" leaf="<<leaf<<" valid="<<valid<<"\n";
 for(auto&r:accepted){for(int v:r)cout<<v<<" ";cout<<"\n";}
}
