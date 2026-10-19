#include <cstdlib>
#include <cstdio>
#include <vector>
#include <numeric>
using namespace std;
int n, w[16],v[16],scale,totalbad;long long checked; char lone[32];
int gcdx(int a,int b){return b?gcdx(b,a%b):a;}
// Distinct method: enumerate every start, period, maximally extended interval,
// and test all strictly shorter periods (not only divisors).
long long energy(int *x){
 long long ans=0;
 for(int start=0;start<n;start++)for(int p=1;start+2*p<=n;p++){
  if(start>0 && x[start-1]==x[start+p-1])continue;
  int end=start+p;
  while(end<n && x[end]==x[end-p])end++;
  if(end-start<2*p)continue;
  bool minimal=true;
  for(int d=1;d<p;d++){
   bool smaller=true;
   for(int j=start+d;j<end;j++) if(x[j]!=x[j-d]){smaller=false;break;}
   if(smaller){minimal=false;break;}
  }
  if(minimal)ans+=(end-start)*(scale/p);
 }
 return ans;
}
void enumerate(int pos,int mx){
 if(pos==n){
  if(mx<2)return;
  checked++;long long orig=energy(w);bool all_strict=true;
  for(int a=0;a<=mx && all_strict;a++)for(int b=a+1;b<=mx && all_strict;b++){
   for(int j=0;j<n;j++)v[j]=(w[j]==b)?a:w[j];
   if(energy(v)>=orig)all_strict=false;
  }
  if(all_strict){totalbad++;if(totalbad==1)for(int j=0;j<n;j++)lone[j]='0'+w[j];}
  return;
 }
 for(int a=0;a<=mx+1;a++){w[pos]=a;enumerate(pos+1,(a>mx)?a:mx);}
}
int main(int argc,char**argv){n=(argc>1)?atoi(argv[1]):12;scale=1;for(int p=2;p<=n/2;p++)scale=scale/gcdx(scale,p)*p;w[0]=0;enumerate(1,0);
 lone[n]=0;printf("INDEPENDENT_N=%d CHECKED=%lld BAD=%d WITNESS=%s\n",n,checked,totalbad,totalbad?lone:"none");
 return 0;
}
