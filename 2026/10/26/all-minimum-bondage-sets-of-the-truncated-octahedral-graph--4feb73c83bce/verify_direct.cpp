#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;
int main(){
 vector<array<int,4>> v;
 array<int,4> p={0,1,2,3};
 do{v.push_back(p);}while(next_permutation(p.begin(),p.end()));
 int E[36][2],m=0;uint32_t adj[24]={};
 for(int i=0;i<24;++i){
  for(int t=0;t<3;++t){auto w=v[i]; swap(w[t],w[t+1]);
   int j=int(find(v.begin(),v.end(),w)-v.begin());
   if(i<j){E[m][0]=i;E[m][1]=j;++m;}
  }
 }
 if(m!=36)return 1;
 for(int e=0;e<36;++e){int a=E[e][0],b=E[e][1];adj[a]|=1u<<b;adj[b]|=1u<<a;}
 const uint32_t FULL=(1u<<24)-1;
 vector<array<unsigned char,8>> opt;
 int min6=0,min7=0;
 for(int k=6;k<=8;++k){
  vector<int> chosen(k);for(int i=0;i<k;++i)chosen[i]=i;
  while(true){
   uint32_t dom=0;for(int i:chosen)dom|=(adj[i]|(1u<<i));
   if(dom==FULL){if(k==6)++min6;else if(k==7)++min7;else{
    array<unsigned char,8> a;for(int q=0;q<8;++q)a[q]=(unsigned char)chosen[q];opt.push_back(a);
   }}
   int r=k-1;while(r>=0 && chosen[r]==24-k+r)--r;
   if(r<0)break;
   ++chosen[r];for(int s=r+1;s<k;++s)chosen[s]=chosen[s-1]+1;
  }
 }
 printf("minimum layers size6=%d size7=%d size8=%zu\n",min6,min7,opt.size());
 if(min6||min7||opt.size()!=1767)return 2;
 int wins=0;vector<uint64_t> winners;
 for(int a=0;a<32;++a)for(int b=a+1;b<33;++b)for(int c=b+1;c<34;++c)for(int d=c+1;d<35;++d)for(int e=d+1;e<36;++e){
  int F[]={a,b,c,d,e};uint32_t cur[24];for(int i=0;i<24;++i)cur[i]=adj[i]|(1u<<i);
  for(int i:F){int u=E[i][0],w=E[i][1];cur[u]&=~(1u<<w);cur[w]&=~(1u<<u);}
  bool survived=false;
  for(auto &S:opt){
   uint32_t dom=0;
   for(int x:S){dom|=cur[x];if(dom==FULL)break;}
   if(dom==FULL){survived=true;break;}
  }
  if(!survived){++wins;uint64_t mask=0;for(int i:F)mask|=1ull<<i;winners.push_back(mask);}
 }
 printf("FAILURE_COUNT=%d TOTAL=%zu FIRST=%llu LAST=%llu\n",wins,winners.size(),(unsigned long long)winners.front(),(unsigned long long)winners.back());
 if(wins!=276)return 3;
 return 0;
}
