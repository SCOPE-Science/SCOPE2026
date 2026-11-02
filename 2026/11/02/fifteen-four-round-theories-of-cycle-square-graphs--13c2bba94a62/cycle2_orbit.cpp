#include <bits/stdc++.h>
using namespace std;
struct HVec {size_t operator()(vector<int> const& a)const noexcept {size_t h=1469598103934665603ULL;for(int x:a){h ^= (uint32_t)x+0x9e3779b9;h*=1099511628211ULL;}return h;}};
static unordered_map<vector<int>,int,HVec> types;
static int nextid=1,n;
static unordered_map<uint64_t,int> memo;
static long long ncalls=0;
static vector<int> canon(vector<int> a){if(a.empty())return a;int z=a[0];for(int& x:a) x=(x-z+n)%n;vector<int> b=a;for(int &x:b)x=(n-x)%n;return (b<a)?b:a;}
static uint64_t key(vector<int> const&a) {uint64_t k=a.size();for(int x:a)k=(k<<7)|x;return k;}
static int atom(vector<int> const&a){int z=0,p=1;for(int i=0;i<(int)a.size();++i)for(int j=i+1;j<(int)a.size();++j){int d=(a[j]-a[i]+n)%n;int v= a[i]==a[j]?0: ((d<=2||d>=n-2)?1:2); z+=p*v;p*=3;}return z;}
static int intern(vector<int> &&v){auto it=types.find(v);if(it!=types.end())return it->second;int id=nextid++;types.emplace(std::move(v),id);return id;}
static int eval(vector<int> a){a=canon(std::move(a));uint64_t k=key(a);auto it=memo.find(k);if(it!=memo.end())return it->second;int rem=4-(int)a.size(), klen=(int)a.size(); vector<int> v={rem,klen,atom(a)};if(rem){vector<int> child; child.reserve(n);for(int x=0;x<n;x++){a.push_back(x);child.push_back(eval(a));a.pop_back();}sort(child.begin(),child.end());child.erase(unique(child.begin(),child.end()),child.end());v.insert(v.end(),child.begin(),child.end());}int id=intern(std::move(v));memo.emplace(k,id);ncalls++;return id;}
int main(int argc,char**argv){int N=(argc>1)?atoi(argv[1]):65;for(n=5;n<=N;n++){memo.clear();int ans=eval({});cerr<<n<<" "<<ans<<" types="<<types.size()<<" memo="<<memo.size()<<"\n";cout<<n<<","<<ans<<"\n";}}
