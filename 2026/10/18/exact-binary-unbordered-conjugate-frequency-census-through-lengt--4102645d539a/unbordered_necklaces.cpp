#include <bits/stdc++.h>
using namespace std;
int n;vector<int> a;vector<uint64_t>hist;
void necklace(int t,int p){
 if(t>n){
  if(n%p!=0)return;
  if(p<n){hist[0]+=p;return;}
  int c=0;
  for(int s=0;s<n;s++){
    bool unbordered=true;
    for(int b=1;b<=n/2;b++){
      bool border=true;
      for(int i=0;i<b;i++)if(a[1+((s+i)%n)]!=a[1+((s+n-b+i)%n)]){border=false;break;}
      if(border){unbordered=false;break;}
    }
    if(unbordered)c++;
  }
  hist[c]+=n;
  return;
 }
 a[t]=a[t-p];necklace(t+1,p);
 for(int j=a[t-p]+1;j<2;j++){a[t]=j;necklace(t+1,t);}
}
int main(int argc,char**argv){int N=atoi(argv[1]);for(n=1;n<=N;n++){a.assign(n+1,0);hist.assign(n+1,0);necklace(1,1);cout<<n;for(auto c:hist)cout<<" "<<c;cout<<"\n"<<flush;}}
