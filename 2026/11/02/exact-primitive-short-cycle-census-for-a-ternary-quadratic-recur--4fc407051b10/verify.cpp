// Finite independent check of the closed divisor-period formula.
#include <cstdint>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
long long choose(int n,int r){if(r<0||r>n)return 0;long long v=1;for(int i=1;i<=r;i++)v=v*(n-i+1)/i;return v;}
long long fixed_formula(int k,int d){
  if(k%d)throw runtime_error("d does not divide k");
  int r=(k/d)%4;if(r==0||r==2)return 1;
  int required=(r==1?3-d:3-2*d); required=(required%4+4)%4;
  long long ans=1;
  for(int e=0;e<=d;e++)if(e%4==required)ans+=4*choose(d,e);
  return ans;
}
int main(){
 long long checks=0, nonzero_orbits=0, states_tested=0;
 for(int k=2;k<=12;k++){
  int pk=1;for(int i=0;i<k;i++)pk*=3;int pw=pk/3;
  vector<int> ds;for(int d=1;d<=k;d++)if(k%d==0)ds.push_back(d);
  vector<long long> fixed(ds.size()),exact(ds.size());
  for(int v=0;v<pk;v++){
   int cur=v;int first=0;
   for(int t=1;t<=4*k;t++){
    int y=(cur%3)+((cur/pw)!=0);cur=cur/3+pw*(y%3);
    if(cur==v && !first)first=t;
    if(cur==v && t%4==0)
      for(size_t j=0;j<ds.size();j++)if(t==4*ds[j])fixed[j]++;
   }
   if(first>=4 && first%4==0 && (4*k)%first==0){
      for(size_t j=0;j<ds.size();j++)if(first==4*ds[j])exact[j]++;
   }
   states_tested++;
  }
  for(size_t j=0;j<ds.size();j++){
   int d=ds[j];if(fixed[j]!=fixed_formula(k,d)){
      cerr<<"FIXED_FAIL k="<<k<<" d="<<d<<" seen="<<fixed[j]<<" expected="<<fixed_formula(k,d)<<"\n";return 2;}
   long long mob=0;
   for(size_t i=0;i<ds.size();i++)if(d%ds[i]==0){
     int ratio=d/ds[i],pr=0,z=ratio;
     for(int p=2;p*p<=z;p++)if(z%p==0){z/=p;pr++;if(z%p==0){pr=-100;break;}while(z%p==0)z/=p;}
     if(pr==-100) continue;
     if(z>1) pr++;
     mob+= (pr%2?-1:1)*(fixed_formula(k,ds[i])-1);
   }
   if(mob!=exact[j] || mob%(4*d)!=0){cerr<<"ORBIT_FAIL k="<<k<<" d="<<d<<" observed="<<exact[j]<<" mob="<<mob<<"\n";return 3;}
   checks++;nonzero_orbits+=exact[j]/(4*d);
  }
 }
 cout<<"VERIFY_OK k_range=2..12 divisor_fixed_and_primitive_checks="<<checks<<" states_examined="<<states_tested<<" short_orbits_total="<<nonzero_orbits<<"\n";
}
