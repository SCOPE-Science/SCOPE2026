// Counts the successor-neighbor phase colorings without evolving the dynamics.
#include <iostream>
using namespace std;
int main(){
 const int N=12;
 int E[][2]={{0,1},{0,5},{0,7},{0,8},{0,11},{1,2},{1,5},{1,6},{1,8},{2,3},{2,6},{2,8},{2,9},{3,4},{3,6},{3,9},{3,10},{4,5},{4,6},{4,10},{4,11},{5,6},{5,11},{7,8},{7,9},{7,10},{7,11},{8,9},{9,10},{10,11}};
 unsigned nbr[12]={};for(auto &e:E){nbr[e[0]]|=1u<<e[1];nbr[e[1]]|=1u<<e[0];}
 long count=0;
 for(int s=0;s<531441;s++){
  int a[12],q=s;unsigned colors[3]={};
  for(int i=0;i<N;i++){a[i]=q%3;q/=3;colors[a[i]]|=1u<<i;}
  bool valid=true;
  for(int i=0;i<N;i++)if(!(nbr[i]&colors[(a[i]+1)%3])){valid=false;break;}
  if(valid)count++;
 }
 cout<<"successor_neighbor_phase_colorings="<<count<<"\n";
 if(count!=145200)return 1;
 cout<<"CHECK_OK\n";
}
