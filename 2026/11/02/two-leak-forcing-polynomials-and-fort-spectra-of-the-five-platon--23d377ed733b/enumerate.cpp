#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<uint32_t>a(n,0);for(int i=0,x,y;i<m;i++){cin>>x>>y;a[x]|=1u<<y;a[y]|=1u<<x;}uint32_t full=(1u<<n)-1;
vector<uint8_t> exposure(full+1,3);auto bc=[](uint32_t x){return __builtin_popcount(x);};
for(uint32_t W=1;W<=full;W++){int count=0;for(int v=0;v<n;v++){if(W>>v&1)continue;if(bc(a[v]&W)==1){if(++count>=3)break;}}exposure[W]=min(count,3);}
for(int leaks=0;leaks<=2;leaks++){vector<uint8_t>hasbad(full+1,0);vector<uint32_t>forced(n+1,0), minimal(n+1,0);uint32_t minbad=0;int minsize=n+1;unsigned long long num=0;uint32_t witness=0;for(uint32_t W=1;W<=full;W++){bool sub=false;for(uint32_t t=W;t;t&=t-1)if(hasbad[W^(t&-t)]){sub=true;break;} bool bad=(exposure[W]<=leaks); hasbad[W]=(bad||sub); if(bad&&!sub){minimal[bc(W)]++;if(!minbad)minbad=W;}}
for(uint32_t S=0;S<=full;S++)if(!hasbad[full^S]){int size=bc(S);forced[size]++;if(size<minsize){minsize=size;num=1;witness=S;}else if(size==minsize)num++;}
cout<<"leaks="<<leaks<<" Z="<<minsize<<" optimal="<<num<<" witness="<<witness<<" minimal_bad_size:";for(int s=1;s<=n;s++)if(minimal[s])cout<<" "<<s<<":"<<minimal[s];cout<<" goodSizes:";for(int s=0;s<=n;s++)if(forced[s])cout<<" "<<s<<":"<<forced[s];cout<<"\n";
}
}
