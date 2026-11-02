#include <bits/stdc++.h>
using namespace std;
uint64_t get(uint64_t s,int j){return (s>>(6*j))&63;}
uint64_t put(uint64_t s,int j,int v){return s|((uint64_t)v<<(6*j));}
int pairing(int a,int b){return (__builtin_parity((a&7)&(b>>3)) ^ __builtin_parity((a>>3)&(b&7)));}
int q0(int a){return __builtin_parity((a&7)&(a>>3));}
int arf(int c){return q0(c);}
int main(){ vector<int>ws={1,2,4,8,16,32,3,6,24,48,9,18,36,17,34,12,7,56};
vector<int>odd;int idx[64];fill(idx,idx+64,-1);for(int c=0;c<64;c++)if(arf(c)){idx[c]=odd.size();odd.push_back(c);}assert(odd.size()==28);
uint64_t id=0;for(int j=0;j<6;j++)id=put(id,j,1<<j);
vector<uint64_t> a; a.reserve(1500000);a.push_back(id);
unordered_set<uint64_t>seen;seen.reserve(1800000);seen.insert(id);
for(size_t z=0;z<a.size();z++){
 uint64_t g=a[z];for(int w:ws){uint64_t t=0;for(int j=0;j<6;j++){int v=get(g,j);if(pairing(v,w))v^=w;t=put(t,j,v);}if(seen.insert(t).second)a.push_back(t);}
}
map<int,int>cnt;map<string,int>spec;
for(auto s:a){array<int,28>p;
for(int i=0;i<28;i++){
 int c=odd[i];int cp=0;
 for(int j=0;j<6;j++){
   int v=get(s,j);int val=q0(v)^pairing(c,v);
   cp^=(val<<(j<3?j+3:j-3));
 }
 assert(idx[cp]>=0);p[i]=idx[cp];
}
array<bool,28>v{};vector<int>cycs;int mn=29;
for(int i=0;i<28;i++)if(!v[i]){int j=i,d=0;do{v[j]=true;j=p[j];d++;}while(j!=i);cycs.push_back(d);mn=min(mn,d);}cnt[mn]++;
sort(cycs.begin(),cycs.end());string t;for(auto d:cycs)t+=to_string(d)+",";spec[t]++;
}
cout<<"size "<<a.size()<<"\n";for(auto [m,n]:cnt)cout<<"min "<<m<<" count "<<n<<"\n";for(auto &[m,n]:spec)cout<<"cycle "<<m<<" count "<<n<<"\n";
}
