// Independent count by exhaustive topologically ordered 3-color monotone assignments.
#include <iostream>
#include <cstdint>
using namespace std;
static uint64_t count_morph=0,count_all=0;
static int n,N,values[32];
void rec(int x){
 if(x==N){
  if(values[0]!=0 || values[N-1]!=2) return;
  bool present1=false;
  for(int i=0;i<N;i++)if(values[i]==1){present1=true;break;}
  if(!present1)return;
  count_all++;
  for(int i=0;i<N;i++)if(values[i]==0){
   bool ok=false;
   for(int j=0;j<N;j++)if(values[j]==1 && (i&j)==i){ok=true;break;}
   if(!ok)return;
  }
  count_morph++;return;
 }
 int minimum=0;
 for(int b=0;b<n;b++)if(x&(1<<b)){
  int y=x^(1<<b);if(values[y]>minimum)minimum=values[y];
 }
 for(int c=minimum;c<=2;c++){
  if(x==0 && c!=0)continue;
  values[x]=c;rec(x+1);
 }
}
int main(int argc,char**argv){n=argc>1?atoi(argv[1]):5;N=1<<n;if(n>5)return 1;rec(0);cout<<"n="<<n<<" surjective_monotone="<<count_all<<" bounded_morphisms="<<count_morph<<"\n";}
