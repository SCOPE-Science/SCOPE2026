#include <bits/stdc++.h>
using namespace std;
struct GCtx{int n,m;vector<pair<int,int>>E;int id[8][8];GCtx(int N):n(N){memset(id,-1,sizeof(id));for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){id[i][j]=id[j][i]=E.size();E.push_back({i,j});}m=E.size();}
bool adj(uint64_t g,int a,int b)const{return (g>>id[a][b])&1ULL;}
bool has_matching2(uint64_t g,const vector<int>&v)const{for(int a=0;a<(int)v.size();a++)for(int b=a+1;b<(int)v.size();b++) if(adj(g,v[a],v[b])) for(int c=0;c<(int)v.size();c++) if(c!=a&&c!=b) for(int d=c+1;d<(int)v.size();d++) if(d!=a&&d!=b&&adj(g,v[c],v[d])) return true;return false;}
bool hasH(uint64_t g)const{for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++) if(adj(g,a,b)&&adj(g,a,c)&&adj(g,b,c)){vector<int>r;for(int v=0;v<n;v++)if(v!=a&&v!=b&&v!=c)r.push_back(v);if(has_matching2(g,r))return true;}return false;}
bool added_creates(uint64_t g,int e)const{auto [u,v]=E[e]; // role 1: uv is an isolated K2 edge
 vector<int> rem;for(int x=0;x<n;x++)if(x!=u&&x!=v)rem.push_back(x);
 for(int i=0;i<(int)rem.size();i++)for(int j=i+1;j<(int)rem.size();j++)for(int k=j+1;k<(int)rem.size();k++){int a=rem[i],b=rem[j],c=rem[k];if(adj(g,a,b)&&adj(g,a,c)&&adj(g,b,c)){vector<int>r;for(int x:rem)if(x!=a&&x!=b&&x!=c)r.push_back(x);for(int p=0;p<(int)r.size();p++)for(int q=p+1;q<(int)r.size();q++)if(adj(g,r[p],r[q])) return true;}}
 // role 2: uv is a triangle edge
 for(int w=0;w<n;w++) if(w!=u&&w!=v&&adj(g,u,w)&&adj(g,v,w)){vector<int>r;for(int x=0;x<n;x++)if(x!=u&&x!=v&&x!=w)r.push_back(x);if(has_matching2(g,r))return true;}
 return false;}
bool saturated(uint64_t g)const{if(hasH(g))return false;for(int e=0;e<m;e++)if(!((g>>e)&1ULL)&&!added_creates(g,e))return false;return true;}
};
uint64_t nextc(uint64_t x){uint64_t u=x&-x,v=x+u;if(v==0)return 0;return v+(((v^x)/u)>>2);} 
uint64_t countk(const GCtx&C,int k){if(k==0)return C.saturated(0);uint64_t lim=1ULL<<C.m,g=(1ULL<<k)-1,c=0;while(g<lim){if(C.saturated(g))c++;auto h=nextc(g);if(h<=g||h>=lim)break;g=h;}return c;}
int main(){for(auto [n,kmin,want]:vector<tuple<int,int,uint64_t>>{{7,9,840},{8,10,11760}}){GCtx C(n);for(int k=0;k<kmin;k++){auto c=countk(C,k);if(c){cerr<<"unexpected n="<<n<<" k="<<k<<" count="<<c<<"\n";return 2;}}auto c=countk(C,kmin);cout<<"n="<<n<<" k="<<kmin<<" count="<<c<<"\n";if(c!=want)return 3;}cout<<"CROSSCHECK_OK\n";}
