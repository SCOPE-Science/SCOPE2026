#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>
using namespace std;
int qv,pv,nv;
int addf(int a,int b){ if(pv==2) return a^b; return (a+b)%pv; }
int negf(int a){return pv==2?a:(pv-a)%pv;}
int mulf(int a,int b){
 if(qv!=4)return (a*b)%pv;
 int r=0;
 for(int i=0;i<2;i++)for(int j=0;j<2;j++)if((a>>i&1)&&(b>>j&1))r^=(1<<(i+j));
 if(r&8) r^=0b1110;
 if(r&4) r^=0b111;
 return r;
}
long long ipow(int a,int b){long long x=1;while(b--)x*=a;return x;}
int binom(int a,int b){int x=1;for(int i=0;i<b;i++)x=x*(a-i)/(i+1);return x;}
int Kcalc(int n,int p){int m=n-2,v=1;do {v*=1+m%p;m/=p;} while(m);return v;}
void action(const vector<int>& X,const vector<int>& Y,vector<int>& Z){
 int n=nv; fill(Z.begin(),Z.end(),0);
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
   int v=0;
   for(int k=i+1;k<j;k++)v=addf(v,addf(mulf(X[i*n+k],Y[k*n+j]),negf(mulf(Y[i*n+k],X[k*n+j]))));
   Z[i*n+j]=v;
 }
}
void one(int q,int n,long long limit){
 qv=q;pv=(q==4?2:q);nv=n;
 int N=n*(n-1)/2;long long all=ipow(q,N),seen=min(all,limit),got=0,mis=0,cofmis=0;
 vector<pair<int,int>> P;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)P.push_back({i,j});
 vector<int>X(n*n),Y(n*n),Z(n*n);
 for(long long state=0;state<seen;state++){
   auto z=state;fill(X.begin(),X.end(),0);
   for(auto [i,j]:P){X[i*n+j]=z%q;z/=q;}
   bool actual=false;
   for(int i=0;i<n-1;i++){
     fill(Y.begin(),Y.end(),0);Y[i*n+i+1]=1;
     for(int step=0;step<n-2;step++){action(X,Y,Z);Y.swap(Z);}
     int prod=1;
     for(int j=0;j<n-1;j++)if(j!=i)prod=mulf(prod,X[j*n+j+1]);
     int k=n-2, sign=((n-i-2)%2 ? negf(1):1);
     int expected=mulf(mulf(binom(k,n-i-2)%pv,sign),prod);
     if(Y[n-1]!=expected)cofmis++;
     for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)if(a!=0 || b!=n-1)if(Y[a*n+b]!=0)cofmis++;
     if(Y[n-1]!=0)actual=true;
   }
   int zeros=0,where=-1;
   for(int i=0;i<n-1;i++)if(X[i*n+i+1]==0){zeros++;where=i;}
   bool pred=(zeros==0)||(zeros==1 && binom(n-2,where)%pv!=0);
   if(actual!=pred)mis++;
   if(actual)got++;
 }
 long long expected=ipow(q,N-n+1)*(ipow(q-1,n-1)+(long long)Kcalc(n,pv)*ipow(q-1,n-2));
 cout<<"field="<<q<<" n="<<n<<" tested="<<seen<<" full="<<all<<" observed="<<got<<" predicted="<<expected<<" mismatches="<<mis<<" coefficient_mismatches="<<cofmis<<" K="<<Kcalc(n,pv)<<"\n";
 if(mis||cofmis||(seen==all&&got!=expected))exit(2);
}
int main(){
 one(2,3,1000000);one(2,4,1000000);one(2,5,1000000);one(2,6,1000000);
 one(3,3,1000000);one(3,4,1000000);one(3,5,1000000);
 one(4,3,1000000);one(4,4,1000000);
 one(5,4,1000000);
 cout<<"VERIFY_OK\n";
}
