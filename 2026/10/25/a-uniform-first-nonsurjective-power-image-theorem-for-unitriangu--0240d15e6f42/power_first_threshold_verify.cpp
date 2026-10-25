#include <bits/stdc++.h>
using namespace std;
struct Field {
 int q,p;
 int add(int a,int b) const {return q==4?(a^b):((a+b)%p);}
 int sub(int a,int b) const {return q==4?(a^b):((a-b+p)%p);}
 int mul(int a,int b) const {if(q!=4)return a*b%p;int x=0;for(int i=0;i<2;i++) if((b>>i)&1) x^=a<<i; if(x&8)x^=0b1100; if(x&4)x^=0b111;return x&3;}
 int inv(int a) const {if(!a)throw runtime_error("inverse zero");for(int b=1;b<q;b++)if(mul(a,b)==1)return b;throw runtime_error("inverse absent");}
 int div(int a,int b) const {return mul(a,inv(b));}
};
struct Calc {
 int p,n,q,K;Field F;vector<vector<vector<int>>> terms;
 Calc(int prime,int field):p(prime),n(prime+3),q(field),F{field,prime}{K=(n-1)+(n-2)+(n-3);int src[]={1,2,3,1,2,1},dst[]={p+1,p+2,p+3,p+2,p+3,p+3};terms.resize(6);for(int t=0;t<6;t++){vector<int> e;dfs(src[t],dst[t],p,e,terms[t]);}}
 int idx(int i,int j) const {int d=j-i; if(d==1)return i-1; if(d==2)return n-1+i-1;if(d==3)return n-1+n-2+i-1;throw runtime_error("large diagonal");}
 void dfs(int pos,int end,int steps,vector<int>& path,vector<vector<int>>& out){if(!steps){if(pos==end)out.push_back(path);return;}for(int d=1;d<=3 && pos+d<=end;d++){if((end-pos-d)<steps-1 || (end-pos-d)>3*(steps-1))continue;path.push_back(idx(pos,pos+d));dfs(pos+d,end,steps-1,path,out);path.pop_back();}}
 vector<int> eval(const vector<int>&x) const {vector<int> out(6);for(int j=0;j<6;j++){int sum=0;for(const auto&mon:terms[j]){int pr=1;for(int k:mon)pr=F.mul(pr,x[k]);sum=F.add(sum,pr);}out[j]=sum;}return out;}
 int encode(const vector<int>& x) const {int v=0;for(int i=0;i<6;i++)v=v*q+x[i];return v;}
 vector<int> decode(int code) const {vector<int>a(6);for(int i=5;i>=0;i--){a[i]=code%q;code/=q;}return a;}
 bool allowed(const vector<int>& y)const {auto[u,v,w,s,t,z]=tuple{y[0],y[1],y[2],y[3],y[4],y[5]};if(!v)return !(u && w);if(!u && !w)return F.mul(v,z)==F.mul(s,t);return true;}
 vector<int> reversed(const vector<int>&x)const{vector<int> z(K);for(int i=1;i<=n;i++)for(int d=1;d<=3 && i+d<=n;d++) z[idx(i,i+d)]=x[idx(n+1-i-d,n+1-i)];return z;}
 vector<int> witness(const vector<int>& y)const{
   auto[u,v,w,s,t,z]=tuple{y[0],y[1],y[2],y[3],y[4],y[5]};
   if(!allowed(y))throw runtime_error("not allowed");
   vector<int>x(K,0);
   auto a=[&](int i,int val){x[idx(i,i+1)]=val;};
   auto b=[&](int i,int val){x[idx(i,i+2)]=val;};
   auto c=[&](int i,int val){x[idx(i,i+3)]=val;};
   if(v){for(int i=2;i<=p+1;i++)a(i,1);a(2,v);a(1,F.div(u,v));a(p+2,w);b(1,s);b(p+1,F.div(t,v));
     if(u){auto old=eval(x);int coef=1;for(int i=1;i<=p-1;i++)coef=F.mul(coef,x[idx(i,i+1)]);c(p,F.div(F.sub(z,old[5]),coef));}
     else if(w){auto old=eval(x);int coef=1;for(int i=4;i<=p+2;i++)coef=F.mul(coef,x[idx(i,i+1)]);c(1,F.div(F.sub(z,old[5]),coef));}
   } else if(u){a(1,u);for(int i=2;i<=p;i++)a(i,1);b(p,F.div(s,u));b(p+1,t);auto old=eval(x);c(p,F.div(F.sub(z,old[5]),u));}
   else if(w){vector<int> yr{w,0,0,t,s,z};return reversed(witness(yr));}
   else if(s && t){if(p==2){a(1,1);a(4,F.div(t,s));b(2,s);c(2,z);}else {for(int i=1;i<=p+2;i++)a(i,1);a(3,0);a(p+2,F.div(t,s));b(2,s);c(2,F.div(z,F.div(t,s)));}}
   else if(s){for(int i=1;i<=p+2;i++)a(i,1);a(2,0);a(p+2,0);b(1,s);b(p+1,F.div(z,s));}
   else if(t){vector<int> yr{0,0,0,t,0,z};return reversed(witness(yr));}
   else{for(int i=4;i<=p+2;i++)a(i,1);c(1,z);}
   return x;
 }
 void check(bool brute){long long count=1;for(int i=0;i<6;i++)count*=q;long long accepted=0;for(int i=0;i<count;i++){auto y=decode(i);if(!allowed(y))continue;accepted++;auto x=witness(y);if(eval(x)!=y){cerr<<"FAIL witness p="<<p<<" q="<<q<<" code="<<i<<" got="<<encode(eval(x))<<"\n";exit(1);}}
   long long expect=1LL*q*q*q*q*q*q-1LL*q*q*q*q*q+1LL*q*q*q*q+1LL*q*q*q-1LL*q*q;
   if(accepted!=expect){cerr<<"FAIL total "<<accepted<<" vs "<<expect<<"\n";exit(1);}
   if(brute){vector<char> seen(count,false);long long inputs=1;for(int i=0;i<K;i++)inputs*=q;vector<int>x(K);for(long long i=0;i<inputs;i++){long long z=i;for(int j=0;j<K;j++){x[j]=z%q;z/=q;}auto y=eval(x);if(!allowed(y)){cerr<<"FAIL necessary p="<<p<<" q="<<q<<"\n";exit(1);}seen[encode(y)]=true;}long long actual=count_if(seen.begin(),seen.end(),[](char z){return z;});if(actual!=expect){cerr<<"FAIL exhaustive p="<<p<<" q="<<q<<" count="<<actual<<" expected="<<expect<<"\n";exit(1);}cout<<"EXHAUSTIVE p="<<p<<" q="<<q<<" inputs="<<inputs<<" images="<<actual<<"; ";}
   cout<<"WITNESSES p="<<p<<" q="<<q<<" images="<<accepted<<" OK\n";
 }
};
int main(){Calc(2,2).check(true);Calc(2,4).check(true);Calc(3,3).check(true);Calc(5,5).check(false);Calc(7,7).check(false);cout<<"VERIFY_OK_UNIFORM_P_POWER_FIRST_FAILURE\n";}
