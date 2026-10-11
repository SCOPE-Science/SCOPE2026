#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
int pop(int a){return __builtin_popcount((unsigned)a);} 
struct Four {array<int,4> a; ull delta; bool plane;};
vector<Four> foursets(int d){vector<Four> out;int n=1<<d;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)for(int l=k+1;l<n;l++){Four q{{i,j,k,l},0,((i^j^k^l)==0)};for(int x=0;x<4;x++)for(int y=x+1;y<4;y++)q.delta|=1ULL<<(q.a[x]^q.a[y]);out.push_back(q);}return out;}
ull zero(const Four &a,int d){int n=1<<d;ull z=0;for(int f=1;f<n;f++){int sum=0;for(int x:a.a)sum+=((pop(f&x)&1)?-1:1);if(sum==0)z|=1ULL<<f;}return z;}
int common_ann_size(const vector<Four>& as,int d){int n=1<<d,c=0;for(int t=0;t<n;t++){bool ok=true;for(auto a:as){for(int i=1;i<4;i++)if(pop(t&(a.a[i]^a.a[0]))&1)ok=false;}if(ok)c++;}return c;}
void check_family(const vector<Four>& as,const vector<Four>& bs,const vector<array<int,3>>& planes,int d,long long &checks){ull z=(1ULL<<(1<<d))-1;for(auto a:as)z &=zero(a,d);int t=0;for(auto W:planes)if(((z>>W[0])&1)&&((z>>W[1])&1)&&((z>>W[2])&1))t++;int h=common_ann_size(as,d),np=0,nn=0;for(auto b:bs)if((b.delta &z)==b.delta){if(b.plane)np++;else nn++;}
long long expected_plane=(1LL<<(d-2))*t, expected_other=expected_plane*(h-1);if(np!=expected_plane || nn!=expected_other){cerr<<"FAIL d="<<d<<" family="<<as.size()<<" T="<<t<<" ann="<<h<<" plane="<<np<<" other="<<nn<<" exp="<<expected_plane<<","<<expected_other<<"\n";exit(2);}checks++;}
int main(){long long checks=0;for(int d=2;d<=4;d++){auto as=foursets(d);auto bs=as;vector<array<int,3>> planes;int n=1<<d;for(int x=1;x<n;x++)for(int y=x+1;y<n;y++){int z=x^y;if(y<z)planes.push_back({x,y,z});}
if(d<=3){for(auto a:as)check_family({a},bs,planes,d,checks);for(int i=0;i<(int)as.size();i++)for(int j=i+1;j<(int)as.size();j++)check_family({as[i],as[j]},bs,planes,d,checks);} else {for(auto a:as)check_family({a},bs,planes,d,checks);std::mt19937 rng(271828);for(int v=0;v<700;v++){vector<Four> f;int m=2+v%5;for(int j=0;j<m;j++)f.push_back(as[rng()%as.size()]);check_family(f,bs,planes,d,checks);}}
cout<<"d="<<d<<" sets="<<as.size()<<" planes="<<planes.size()<<" CHECKED\n";}
// A_i are planes span(e1,e2), span(e1,e3), span(e1,e2+e3); translated through 0.
vector<Four> A={Four{{0,1,2,3},0,true},Four{{0,1,4,5},0,true},Four{{0,1,6,7},0,true}};
auto bs=foursets(3);vector<array<int,3>> planes;for(int x=1;x<8;x++)for(int y=x+1;y<8;y++){int z=x^y;if(y<z)planes.push_back({x,y,z});}
for(int mask=1;mask<8;mask++){vector<Four> f;for(int j=0;j<3;j++)if(mask&(1<<j))f.push_back(A[j]);int count=0;for(auto b:bs){ull z=(1ULL<<8)-1;for(auto a:f)z&=zero(a,3);if((b.delta&z)==b.delta)count++;}cout<<"obstruction subset="<<mask<<" count="<<count<<"\n";check_family(f,bs,planes,3,checks);}
cout<<"CHECK_PASS families="<<checks<<"\n";
}
