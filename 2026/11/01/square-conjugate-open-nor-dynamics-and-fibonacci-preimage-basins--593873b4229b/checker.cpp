// Direct-state enumeration for open-neighborhood NOR on paths.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using U=uint64_t;
U step(U s,int n){U t=0;for(int i=0;i<n;++i){bool seen=(i>0&&(s&(U(1)<<(i-1))))||(i+1<n&&(s&(U(1)<<(i+1))));if(!seen)t|=U(1)<<i;}return t;}
std::vector<U> fibs(int n){std::vector<U> f(n+1);f[0]=0;f[1]=1;for(int i=2;i<=n;++i)f[i]=f[i-1]+f[i-2];return f;}
U one(const std::vector<int>& v,bool left,bool right,const std::vector<U>& f){U z=1;int k=v.size();for(int i=0;i<k;){if(v[i]){++i;continue;}int j=i;while(j<k&&!v[j])++j;int L=j-i;int t=int(i==0&&left)+int(j==k&&right);z*=f[L-1+2*t];i=j;}return z;}
U formula(U s,int n,const std::vector<U>&f){std::vector<int>a,b;for(int i=0;i<n;++i)((i%2)?b:a).push_back((s>>i)&1);if(n%2)return one(a,0,0,f)*one(b,1,1,f);return one(a,0,1,f)*one(b,1,0,f);}
int main(){auto f=fibs(32);U total=0;for(int n=2;n<=19;++n){const U max=U(1)<<n;std::map<U,U>freq;for(U s=0;s<max;++s){U a=step(s,n);freq[a]++;assert(step(step(a,n),n)==a);}U fixed=0;for(U s=0;s<max;++s)if(step(s,n)==s)++fixed;assert(freq.size()==fixed*fixed);for(U s=0;s<max;++s){auto it=freq.find(s);U actual=it==freq.end()?0:it->second;assert(actual==formula(s,n,f));}std::cout<<"PASS n="<<n<<" fixed="<<fixed<<" periodic="<<freq.size()<<" states="<<max<<"\n";total+=max;}std::cout<<"PASS total_initial_configurations="<<total<<"\n";}
