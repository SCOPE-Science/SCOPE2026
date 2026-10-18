#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
using namespace std;
constexpr int E[21][2]={{1,8},{1,9},{1,10},{2,8},{2,11},{2,12},{3,8},{3,13},{3,14},{4,9},{4,11},{4,13},{5,9},{5,12},{5,14},{6,10},{6,11},{6,14},{7,10},{7,12},{7,13}};
constexpr int P[8][21]={{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20},{0,1,2,3,5,4,6,8,7,12,13,14,9,10,11,18,19,20,15,16,17},{0,2,1,6,8,7,3,4,5,15,17,16,18,20,19,12,14,13,9,11,10},{1,2,0,9,10,11,12,14,13,15,16,17,18,20,19,3,4,5,6,7,8},{4,3,5,10,11,9,16,17,15,6,7,8,0,1,2,19,20,18,13,12,14},{10,4,16,9,1,12,11,7,20,3,0,6,5,13,19,15,2,18,17,14,8},{10,4,16,9,12,1,11,20,7,5,13,19,3,0,6,17,14,8,15,2,18},{10,16,4,9,12,1,11,7,20,17,14,8,15,2,18,5,13,19,3,0,6}};
int main(){
 long long tr[8]={}; long long count=0;
 for(unsigned mask=0;mask<(1u<<21);++mask){
  int parent[15]; for(int i=0;i<15;i++)parent[i]=i; bool forest=true;
  for(int i=0;i<21;i++)if(mask&(1u<<i)){
   int a=E[i][0],b=E[i][1];while(parent[a]!=a)a=parent[a];while(parent[b]!=b)b=parent[b];
   if(a==b){forest=false;break;}parent[b]=a;
  }
  if(!forest)continue;count++;
  for(int j=0;j<8;j++){
   bool invariant=true;int cyc=0;unsigned seen=0;
   for(int i=0;i<21;i++)if(mask&(1u<<i)){if(!(mask&(1u<<P[j][i]))){invariant=false;break;}}
   if(!invariant)continue;
   for(int i=0;i<21;i++)if((mask&(1u<<i))&&!(seen&(1u<<i))){int a=i;do{seen|=1u<<a;a=P[j][a];}while(a!=i);cyc++;}
   tr[j] += (cyc%2==0) ? -1 : 1;
  }
 }
 cout<<"forest_count "<<count<<"\n";
 for(int j=0;j<8;j++)cout<<"class "<<j<<" character "<<tr[j]<<"\n";
}
