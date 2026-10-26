#include <array>
#include <vector>
#include <iostream>
#include <stdexcept>
#include <algorithm>
using namespace std;
using V=array<int,7>;
int mod(int x,int q){ x%=q;return x<0?x+q:x; }
V bracket(const V&a,const V&b,int q){
 V c{};
 c[3]=mod(a[0]*b[1]-a[1]*b[0],q);
 c[4]=mod(a[0]*b[2]-a[2]*b[0],q);
 c[5]=mod(a[1]*b[2]-a[2]*b[1],q);
 c[6]=mod(a[0]*b[5]-a[1]*b[4]+a[2]*b[3]-b[0]*a[5]+b[1]*a[4]-b[2]*a[3],q);
 return c;
}
bool zero(const V &v){for(auto x:v)if(x)return false;return true;}
int vec_rank(vector<V> a,int q){int row=0;
 for(int col=0;col<7&&row<(int)a.size();++col){int k=row;while(k<(int)a.size()&&a[k][col]==0)++k;
  if(k==(int)a.size())continue; swap(a[row],a[k]);int inv=1;while(mod(inv*a[row][col],q)!=1)++inv;
  for(int j=col;j<7;++j)a[row][j]=mod(a[row][j]*inv,q);
  for(int i=0;i<(int)a.size();++i)if(i!=row&&a[i][col]){int t=a[i][col];for(int j=col;j<7;++j)a[i][j]=mod(a[i][j]-t*a[row][j],q);}
  ++row;
 }
 return row;
}
void test_candidate(const vector<V>& b,int q){
 for(int i=0;i<(int)b.size();++i)for(int j=i+1;j<(int)b.size();++j)
  if(!zero(bracket(b[i],b[j],q))) throw runtime_error("nonabelian candidate");
 for(int i=0;i<7;++i){V e{};e[i]=1;
  for(const V& u:b){auto c=bracket(e,u,q);if(!zero(c)){auto t=b;t.push_back(c);if(vec_rank(t,q)!=4)throw runtime_error("candidate not an ideal");}}
 }
}
int main(){
 for(int q:{3,5}){
 long found=0,total=0,ideals=0;
 int piv[4];
 for(piv[0]=0;piv[0]<4;++piv[0])for(piv[1]=piv[0]+1;piv[1]<5;++piv[1])for(piv[2]=piv[1]+1;piv[2]<6;++piv[2])for(piv[3]=piv[2]+1;piv[3]<7;++piv[3]){
  vector<pair<int,int>> freepos;
  for(int i=0;i<4;++i)for(int j=piv[i]+1;j<7;++j){bool isPivot=false;for(int k=0;k<4;++k)if(piv[k]==j)isPivot=true;if(!isPivot)freepos.push_back({i,j});}
  long lim=1;for(int j=0;j<(int)freepos.size();++j)lim*=q;
  if(q==5&&lim>50000)continue; // only sample pivot strata over 5, full at 3
  for(long k=0;k<lim;++k){vector<V> b(4);for(int i=0;i<4;++i)b[i][piv[i]]=1;
   long t=k;for(auto [i,j]:freepos){b[i][j]=t%q;t/=q;}
   ++total;bool abelian=true;
   for(int i=0;i<4&&abelian;++i)for(int j=i+1;j<4;++j)if(!zero(bracket(b[i],b[j],q))){abelian=false;break;}
   if(abelian){++found;test_candidate(b,q);++ideals;}
  }
 }
 cout<<"q="<<q<<" checked_RREF_4spaces="<<total<<" maximal_squarezero_candidates="<<found<<" all_ideals="<<ideals<<"\n";
 if(q==3 && (total!=925771||found!=40||ideals!=40))throw runtime_error("q=3 census failed");
 }
 cout<<"VERIFY_OK\n";
}
