#include <bits/stdc++.h>
using namespace std;
int main(){vector<pair<int,int>> params={{2,0x7},{4,0x13},{6,0x43},{8,0x11b},{10,0x409},{12,0x1053}};
 for(auto [m,poly]:params){int Q=1<<m;
  auto mul=[&](int a,int b){int r=0;while(b){if(b&1)r^=a;b>>=1;a<<=1;if(a&Q)a^=poly;}return r;};
  vector<int> sq(Q),cube(Q),fourth(Q),fifth(Q);
  for(int i=0;i<Q;i++){sq[i]=mul(i,i);cube[i]=mul(sq[i],i);fourth[i]=mul(sq[i],sq[i]);fifth[i]=mul(fourth[i],i);}
  int a=0;for(int i=2;i<Q;i++)if((sq[i]^i^1)==0){a=i;break;}
  assert(a);int ac=a^1;long long N=0;
  for(int x=0;x<Q;x++){
    int A=x^1,B=cube[x]^x,C=cube[x]^1,D=mul(ac,fifth[x])^cube[x]^x;
    for(int y=0;y<Q;y++)if((mul(A,fourth[y])^mul(B,sq[y])^mul(C,y)^D)==0)N++;
  }
  for(int x=0;x<Q;x++)if((mul(ac,fifth[x])^cube[x]^x)==0)N++;
  cout<<"m="<<m<<" a="<<a<<" N="<<N<<"\n";
 }
}
