#include <bits/stdc++.h>
using namespace std;
using P=array<uint8_t,28>;
struct H{size_t operator()(P const&a)const noexcept{
 uint64_t h=1469598103934665603ull; for(uint8_t x:a){h^=x;h*=1099511628211ull;}return h;
}};
int main(){ifstream in("theta_generators.txt");int k;in>>k;vector<P> gs;for(int j=0;j<k;j++){int w;in>>w;P a;for(int i=0;i<28;i++){int t;in>>t;a[i]=t;}gs.push_back(a);}
P id;for(int i=0;i<28;i++)id[i]=i;
vector<P> arr;arr.reserve(1500000);arr.push_back(id);
unordered_set<P,H> seen; seen.reserve(1800000);seen.insert(id);
for(size_t j=0;j<arr.size();j++){
 auto a=arr[j];
 for(auto &g:gs){P c;for(int x=0;x<28;x++)c[x]=g[a[x]];if(seen.insert(c).second)arr.push_back(c);}
 
}
map<pair<int,int>,long long> counts;map<string,long long> cyclehist;vector<P> witnesses(29);vector<bool> got(29,false);
for(auto &p:arr){
 bitset<28> vis; int minl=100; vector<int> lens;
 for(int i=0;i<28;i++)if(!vis[i]){int j=i,l=0;do{vis[j]=1;j=p[j];l++;}while(j!=i);minl=min(minl,l);lens.push_back(l);}
 sort(lens.begin(),lens.end());string s;for(int l:lens)s+=to_string(l)+",";
 counts[{minl,lens[0]}]++;
 cyclehist[s]++;
 if(!got[minl]){got[minl]=true;witnesses[minl]=p;}
}
cout<<"order "<<arr.size()<<"\n";
for(auto &[v,c]:counts)cout<<"min "<<v.first<<" count "<<c<<"\n";
for(auto &[v,c]:cyclehist)cout<<"cycle "<<v<<" count "<<c<<"\n";
for(int i=1;i<29;i++)if(got[i]){cout<<"witness "<<i<<" ";for(auto t:witnesses[i])cout<<(int)t<<" ";cout<<"\n";}
}
