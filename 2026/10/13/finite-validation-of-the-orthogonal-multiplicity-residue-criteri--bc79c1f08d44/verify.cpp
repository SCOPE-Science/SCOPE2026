// Exact verifier for the finite criterion stated in RESULT.md.
// Polynomials over F_2 are encoded by coefficient bitmasks.
#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
int degp(U a){ return a?31-__builtin_clz(a):-1; }
U modp(U a,U b){int db=degp(b); while(a && degp(a)>=db) a^=b<<(degp(a)-db); return a;}
U gcdp(U a,U b){while(b){U r=modp(a,b);a=b;b=r;}return a;}
U divexact(U a,U b){U q=0;int db=degp(b);while(a&&degp(a)>=db){int s=degp(a)-db;q^=1u<<s;a^=b<<s;}return q;}
U mulmod(U a,U b,U m){U r=0;while(b){if(b&1)r^=a;b>>=1;a<<=1;if(degp(a)>=degp(m))a^=m;}return r;}
U sqmod(U a,U m){return mulmod(a,a,m);} 
U derivative(U f){U r=0;for(int i=1;i<=degp(f);i+=2) if((f>>i)&1) r^=1u<<(i-1);return r;}
U invmod(U a,U m){int n=degp(m); uint64_t e=(1ull<<n)-2; U r=1,b=a; while(e){if(e&1) r=mulmod(r,b,m); e>>=1; if(e)b=sqmod(b,m);} return r;}
bool irreducible(U f){int n=degp(f); if(n<=0)return false; U x=2, h=x; for(int i=1;i<=n/2;i++){h=sqmod(h,f); if(gcdp(h^x,f)!=1)return false;} h=x; for(int i=0;i<n;i++)h=sqmod(h,f); return h==x;}
int tracebit(U a,U P){int n=degp(P);U s=0,x=a;for(int i=0;i<n;i++){s^=x;x=sqmod(x,P);} return s&1;}
int psi(U f,U P){int n=degp(P); if(n<=1)return 0; U cof=divexact(f,P); U Tp=modp(2,P), T1p=modp(3,P); U den=mulmod(Tp,T1p,P); den=mulmod(den,modp(cof,P),P); den=mulmod(den,modp(derivative(P),P),P); if(!den){cerr<<"zero den\n";exit(2);} U inv=invmod(den,P); return tracebit(inv,P);}
vector<U> small_irreds(int maxd){vector<U> v;for(int d=1;d<=maxd;d++){U lo=1u<<d,hi=1u<<(d+1);for(U f=lo|1;f<hi;f+=2) if(irreducible(f))v.push_back(f);}return v;}
vector<char> posset(int d){size_t N=1u<<d;vector<char> pos(N); function<void(int,U,U)> rec=[&](int k,U km1,U km2){if(k==d){pos[km1^(1u<<d)]=1;return;} // index remove leading term
 U aT=(km1<<1)^km2; rec(k+1,aT,km1); U aT1=(km1<<1)^km1^km2; rec(k+1,aT1,km1);
 }; rec(0,1,0);return pos;}
int main(){int D=22; auto irr=small_irreds(D/2); long long totalA=0,misA=0;
 for(int d=15;d<=D;d++){
  auto pos=posset(d); long long A=0,mA=0; U lo=1u<<d, hi=1u<<(d+1);
  for(U f=lo;f<hi;f++){
   U der=derivative(f); if(gcdp(f,der)!=1) continue;
   bool divT=(f&1)==0; bool divT1=modp(f,3)==0; if(divT||divT1) continue;
   U rem=f; vector<U> fac;
   for(U P:irr){int dp=degp(P); if(dp*2>d) break; if(modp(rem,P)==0){fac.push_back(P); rem=divexact(rem,P);} }
   if(rem!=1) fac.push_back(rem);
   bool crit=true;for(U P:fac)if(degp(P)>=2 && psi(f,P)){crit=false;break;}
   bool positive=pos[f^lo];
   A++; if(crit!=positive) mA++;
  }
  cout<<"d="<<d<<" cases="<<A<<" mismatches="<<mA<<"\n";
  totalA+=A; misA+=mA;
 }
 cout<<"VERIFY_OK degrees=15..22 coprime_squarefree_cases="<<totalA<<" mismatches="<<misA<<"\n";
 return misA?1:0;
}
