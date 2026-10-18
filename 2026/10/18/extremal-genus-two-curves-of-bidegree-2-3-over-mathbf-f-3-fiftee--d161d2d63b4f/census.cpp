#include <array>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int md(int x){x%=3;return x<0?x+3:x;}
int deg(const array<int,7>&a){for(int i=6;i>=0;--i)if(a[i])return i;return -1;}
array<int,7> discr(const array<int,12>&a){array<int,7>d{};for(int i=0;i<4;i++) for(int j=0;j<4;j++){d[6-i-j]=md(d[6-i-j]+a[4+i]*a[4+j]-a[i]*a[8+j]);}return d;}
int gcddegree(array<int,7>a,array<int,7>b){int x=deg(a),y=deg(b);while(y>=0){while(x>=y){int factor=md(a[x]*b[y]); // if b[y]==2, inverse 2
 for(int j=0;j<=y;j++) a[x-y+j]=md(a[x-y+j]-factor*b[j]);x=deg(a);
}swap(a,b);x=deg(a);y=deg(b);}return x;}
bool sf(const array<int,7>&c){if(c[6]==0&&c[5]==0)return false; // coefficient t=0 root repeated; c stored reversed powers t^i?
// discr at S=1,T=0 equals c[6], so yes
array<int,7>d{};for(int i=1;i<=6;i++)d[i-1]=md(i*c[i]);return gcddegree(c,d)==0;}
int value3(const array<int,12>&a,int block,int s,int t){int v=0;for(int j=0;j<4;j++){int w=1;for(int k=0;k<3-j;k++)w=md(w*s);for(int k=0;k<j;k++)w=md(w*t);v+=a[block*4+j]*w;}return md(v);}
int rootsQuad(int a,int b,int c){int n=0;int us[4]={1,0,1,2},vs[4]={0,1,1,1};for(int i=0;i<4;i++)if(md(a*us[i]*us[i]+b*us[i]*vs[i]+c*vs[i]*vs[i])==0)n++;return n;}
int main(){long long dist[9][5]{};ofstream out("smooth_models.csv");long long smooth=0,all=0;vector<int> firstMax;array<int,12>v{};for(int n=1;n<531441;n++){int k=n;for(int j=0;j<12;j++){v[j]=k%3;k/=3;}int j=0;while(v[j]==0)j++;if(v[j]!=1)continue;all++;auto d=discr(v);if(!sf(d))continue;smooth++;int N=0,r=0;int ss[4]={1,0,1,2},tt[4]={0,1,1,1};for(int i=0;i<4;i++){int A=value3(v,0,ss[i],tt[i]),B=value3(v,1,ss[i],tt[i]),C=value3(v,2,ss[i],tt[i]);N+=rootsQuad(A,B,C);if(md(B*B-A*C)==0)r++;}if(N>8||r>4){cerr<<"BUG\n";exit(1);}dist[N][r]++;out<<n<<","<<N<<","<<r<<"\n";if(N==8&&firstMax.size()<20)firstMax.push_back(n);
}cout<<"all="<<all<<" smooth="<<smooth<<"\n";for(int i=0;i<=8;i++)for(int r=0;r<=4;r++)if(dist[i][r])cout<<i<<","<<r<<","<<dist[i][r]<<"\n";cout<<"max reps:";for(int n:firstMax)cout<<" "<<n;cout<<"\n";
}
