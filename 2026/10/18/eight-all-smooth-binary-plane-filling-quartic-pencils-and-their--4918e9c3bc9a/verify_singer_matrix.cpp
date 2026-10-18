#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
// A three-by-three binary matrix is encoded row-major in nine bits.
static const int I=(1<<0)|(1<<4)|(1<<8);
int apply(int a,int v){int r=0;for(int i=0;i<3;i++){int row=(a>>(3*i))&7;int b=__builtin_parity(unsigned(row&v));r|=b<<i;}return r;}
int mul(int a,int b){int c=0;for(int j=0;j<3;j++){int col=apply(a,apply(b,1<<j));for(int i=0;i<3;i++)c|=((col>>i)&1)<<(3*i+j);}return c;}
bool invertible(int a){int im[8]={};for(int v=0;v<8;v++)im[apply(a,v)]++;for(int k=0;k<8;k++)if(im[k]!=1)return false;return true;}
bool irreducible_charpoly(int a){for(int v=1;v<8;v++)if(apply(a,v)==0 || apply(a,v)==v)return false;return true;}
int canon(int a){return min(a,a^I);}
int main(){
 vector<int> GL;for(int a=0;a<512;a++)if(invertible(a))GL.push_back(a);assert(GL.size()==168);
 map<int,int> inv;for(int g:GL)for(int h:GL)if(mul(g,h)==I){inv[g]=h;break;}assert(inv.size()==168);
 set<int> curves;int irreducible_matrices=0;for(int a=0;a<512;a++)if(irreducible_charpoly(a)){irreducible_matrices++;curves.insert(canon(a));}
 assert(irreducible_matrices==48);assert(curves.size()==24);
 set<array<int,3>> pencils;for(int a:curves)for(int b:curves)if(a<b && curves.count(canon(a^b))){array<int,3> W={a,b,canon(a^b)};sort(W.begin(),W.end());pencils.insert(W);}
 assert(pencils.size()==8);
 auto W0=*pencils.begin();set<array<int,3>> orbit;int stabilizer=0;
 for(int g:GL){array<int,3> W;
  for(int k=0;k<3;k++)W[k]=canon(mul(mul(inv[g],W0[k]),g));
  sort(W.begin(),W.end());orbit.insert(W);if(W==W0)stabilizer++;
 }
 assert(orbit==pencils);assert(stabilizer==21);
 cout<<"IRREDUCIBLE_MATRICES "<<irreducible_matrices<<"\n";
 cout<<"SMOOTH_CURVES "<<curves.size()<<"\n";
 cout<<"PENCILS "<<pencils.size()<<"\n";
 cout<<"GL3_ORDER "<<GL.size()<<"\n";
 cout<<"PROJECTIVE_ORBIT "<<orbit.size()<<"\n";
 cout<<"PENCIL_STABILIZER "<<stabilizer<<"\n";
 cout<<"PASS\n";
}
