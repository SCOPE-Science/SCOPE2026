#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;
int k,limit,a[9],lastseen[70]={},stamp=0;
int smallest[37]; long long total=0;
void visit(int pos,int smallest_next){
 if(pos==k){
  ++stamp;int distinct=0;
  for(int u=0;u<k;u++)for(int v=0;v<=u;v++){
   int sum=a[u]+a[v];
   if(lastseen[sum]!=stamp){lastseen[sum]=stamp;distinct++;}
  }
  if(smallest[distinct]>a[k-1])smallest[distinct]=a[k-1];
  ++total; return;
 }
 for(int x=smallest_next;x<=limit-(k-1-pos);x++){
  a[pos]=x;visit(pos+1,x+1);
 }
}
int main(int argc,char**argv){
 k=stoi(argv[1]);limit=stoi(argv[2]);
 fill(begin(smallest),end(smallest),INT_MAX);
 a[0]=0;visit(1,1);
 cout<<"sets "<<total<<"\n";
 for(int i=2*k-1;i<=k*(k+1)/2;i++)cout<<i<<' '<<(smallest[i]==INT_MAX ? -1:smallest[i])<<'\n';
}
