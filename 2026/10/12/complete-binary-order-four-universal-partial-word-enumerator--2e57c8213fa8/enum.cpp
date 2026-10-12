#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
int masks[81];
map<pair<int,int>,ull> hist;
size_t nodes=0;
void dfs(int a,int b,int c,int cov,int len,int diamonds){
  ++nodes;
  if(cov==65535){hist[{len,diamonds}]++;return;}
  for(int d=0;d<3;d++){
    int key=((a*3+b)*3+c)*3+d;
    int m=masks[key];
    if((cov&m)!=0)continue;
    dfs(b,c,d,cov|m,len+1,diamonds+(d==2));
  }
}
int main(){
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)for(int d=0;d<3;d++){
  int m=0;
  for(int v=0;v<16;v++){
    int t[]={a,b,c,d};bool ok=true;for(int i=0;i<4;i++)if(t[i]!=2&&t[i]!=((v>>(3-i))&1)){ok=false;break;}if(ok)m|=(1<<v);
  }
  masks[((a*3+b)*3+c)*3+d]=m;
 }
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)dfs(a,b,c,0,3,(a==2)+(b==2)+(c==2));
 for(auto [k,n]:hist)cout<<k.first<<" "<<k.second<<" "<<n<<"\n";
 cerr<<"nodes="<<nodes<<" bins="<<hist.size()<<"\n";
}
