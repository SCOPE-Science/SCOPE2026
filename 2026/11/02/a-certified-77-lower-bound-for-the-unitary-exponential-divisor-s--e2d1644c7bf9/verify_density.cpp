#include <iostream>
#include <array>
#include <vector>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using namespace boost::multiprecision;
using U=uint256_t;
struct Entry{U num,den,weight;};
struct Prime{int p,E; vector<Entry> entries;};
vector<Prime> v;
U good=0,eqmass=0,strict=0,all=0;
uint64_t ng=0,ne=0,ns=0,na=0;
U pw(unsigned a,unsigned n){U z=1;for(unsigned i=0;i<n;++i)z*=a;return z;}
void rec(int i,U num,U den,U weight){
 if(i==(int)v.size()){
  ++na;all+=weight;
  if(num>=den){good+=weight;++ng;
   if(num==den){eqmass+=weight;++ne;}else{strict+=weight;++ns;}
  }
  return;
 }
 for(const Entry &e:v[i].entries)rec(i+1,num*e.num,den*e.den,weight*e.weight);
}
int main(){
 vector<int> ps={2,3,5,7,11,13,17,19,23,29,31};
 for(int p:ps){int E=p==2?12:p==3?8:p==5?5:p==7?4:2;
 Prime obj{p,E,{}};
 for(int e=0;e<=E;e++){
 U N=1,T=1;
 if(e){N=1+pw(p,e);T=0;for(int d=1;d<=e;d++)if(e%d==0)T+=pw(p,d);}
 obj.entries.push_back({N,T,U(p-1)*pw(p,E-e)});
 }
 v.push_back(obj);
 }
 rec(0,1,1,1);
 U D=1;for(auto &p:v)D*=pw(p.p,p.E+1);
 if(!(all<=D))throw runtime_error("bad mass");
 cout << "patterns=" <<na<<" good_patterns="<<ng<<" strict_patterns="<<ns<<" equal_patterns="<<ne<<"\n";
 cout<<"denominator="<<D<<"\n";
 cout<<"good_numerator="<<good<<"\n";
 cout<<"strict_numerator="<<strict<<"\n";
 cout<<"equal_numerator="<<eqmass<<"\n";
 cout<<"all_numerator="<<all<<"\n";
}
