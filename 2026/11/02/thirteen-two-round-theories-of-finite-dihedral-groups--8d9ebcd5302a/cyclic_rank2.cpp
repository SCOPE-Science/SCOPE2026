#include<bits/stdc++.h>
using namespace std;
struct Key{uint64_t a;vector<int>child;bool operator==(Key const& b)const{return a==b.a&&child==b.child;}};
struct KH{size_t operator()(Key const&k) const {uint64_t h=k.a+0x9e3779b97f4a7c15;for(int a:k.child)h=(h^(a+1))*0x100000001b3ull;return h;}};
int prod(int n,int a,int b){return (a+b)%n;}
uint64_t atom(int n, int x,int y,int k){int a[]={0,x,y};uint64_t h=0;int bit=0;for(int i=0;i<=k;i++)for(int j=i+1;j<=k;j++){if(a[i]==a[j])h|=1ull<<bit;bit++;}for(int i=0;i<=k;i++)for(int j=0;j<=k;j++)for(int l=0;l<=k;l++){if(prod(n,a[i],a[j])==a[l])h|=1ull<<bit;bit++;}return h;}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):120;unordered_map<uint64_t,int>A;unordered_map<Key,int,KH>B,C;map<int,vector<int>> classes;
for(int n=1;n<=N;n++){
 int cnt=n;vector<int>t1(cnt);
 for(int x=0;x<cnt;x++){
  vector<int> child;child.reserve(cnt);
  for(int y=0;y<cnt;y++){uint64_t a=atom(n,x,y,2);auto p=A.emplace(a,A.size());child.push_back(p.first->second);}
  sort(child.begin(),child.end());child.erase(unique(child.begin(),child.end()),child.end());
  Key k{atom(n,x,0,1),move(child)};auto p=B.emplace(k,B.size());t1[x]=p.first->second;
 }
 sort(t1.begin(),t1.end());t1.erase(unique(t1.begin(),t1.end()),t1.end());Key k{0,move(t1)};auto p=C.emplace(k,C.size());int cl=p.first->second;classes[cl].push_back(n);
 if(n<45||n%10==0)cerr<<n<<" "<<cl<<" types "<<A.size()<<","<<B.size()<<","<<C.size()<<"\n";
}
for(auto &[id,ns]:classes){cout<<id<<" ("<<ns.size()<<"): ";for(int n:ns)cout<<n<<",";cout<<"\n";}
}
