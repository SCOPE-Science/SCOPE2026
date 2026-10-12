#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
static const pair<int,int> edges[36]={{0,1},{0,2},{0,3},{1,4},{1,5},{2,6},{2,7},{3,4},{3,8},{4,9},{5,10},{5,11},{6,11},{6,12},{7,12},{7,13},{8,13},{8,14},{9,15},{9,16},{10,16},{10,17},{11,17},{12,18},{13,19},{14,15},{14,19},{15,20},{16,20},{17,21},{18,21},{18,22},{19,22},{20,23},{21,23},{22,23}};
struct Dom{int nb; U bundle[16];};
vector<Dom> ds; vector<array<int,5>> found;
int main(){
 U nn[24]={};for(int u=0;u<24;u++)nn[u]=1ull<<u;
 for(auto [u,v]:edges){nn[u]|=1ull<<v;nn[v]|=1ull<<u;}
 int dcount=0;
 for(U s=0;s<(1ull<<24);s++){if(__builtin_popcountll(s)!=8)continue;U cov=0;for(int u=0;u<24;u++)if((s>>u)&1)cov|=nn[u];if(cov!=(1ull<<24)-1)continue;
 Dom d{}; for(int v=0;v<24;v++)if(!((s>>v)&1)){ U mask=0;for(int e=0;e<36;e++) {auto [a,b]=edges[e];if((a==v&&((s>>b)&1))||(b==v&&((s>>a)&1)))mask|=1ull<<e;}assert(mask);d.bundle[d.nb++]=mask;}
 ds.push_back(d);dcount++;}
 fprintf(stderr,"dominating sets = %d\n",dcount);
 int minSurv=2000;unsigned long total=0;int numsurvive4min=2000;
 for(int i=0;i<36;i++)for(int j=i+1;j<36;j++)for(int k=j+1;k<36;k++)for(int l=k+1;l<36;l++)for(int m=l+1;m<36;m++){
    U f=(1ull<<i)|(1ull<<j)|(1ull<<k)|(1ull<<l)|(1ull<<m);
    bool survive=false;
    for(const auto &d:ds){bool lost=false;for(int a=0;a<d.nb;a++)if((d.bundle[a]&f)==d.bundle[a]){lost=true;break;}if(!lost){survive=true;break;}}
    if(!survive){found.push_back({i,j,k,l,m});}
    total++;
 }
 fprintf(stderr,"five-edge sets=%lu; bondage five-edge sets=%lu\n",total,found.size());
 for(auto a:found){for(int i=0;i<5;i++)cout<<a[i]<<(i==4?'\n':' ');}
}
