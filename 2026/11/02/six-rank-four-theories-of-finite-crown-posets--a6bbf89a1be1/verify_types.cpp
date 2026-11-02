#include <bits/stdc++.h>
using namespace std;
// rank-4 first-order types for height-two crown posets X_n: A_i<B_i,B_{i-1}.
map<vector<int>,int> intern[5];
int get(int k,vector<int>&v){auto &m=intern[k]; auto it=m.find(v);if(it!=m.end())return it->second;int id=m.size();m.emplace(v,id);return id;}
int n,N;
int norm(int v,int shift){int c=v/2,par=v%2; return 2*((c-shift+n)%n)+par;}
int rel(int u,int v){if(u==v)return 0; if(!(u%2)&&(v%2)){int a=u/2,b=v/2; if(b==a||b==(a+n-1)%n)return 1;}if((u%2)&&!(v%2)){int a=v/2,b=u/2; if(b==a||b==(a+n-1)%n)return 2;}return 3;}
int atcode(int a,int b,int c,int d){int p[4]={a,b,c,d},v=0;for(int i=0;i<4;++i)for(int j=i+1;j<4;++j)v=v*4+rel(p[i],p[j]);return v;}
int calc(int m){n=m;N=2*n; vector<vector<vector<int>>> t1(2,vector<vector<int>>(N,vector<int>(N)));vector<vector<int>> t2(2,vector<int>(N));int t3[2];
for(int s=0;s<2;++s)for(int a=0;a<N;++a)for(int b=0;b<N;++b){vector<int> v;v.reserve(N);for(int z=0;z<N;++z)v.push_back(atcode(s,a,b,z));sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());t1[s][a][b]=get(1,v);}
for(int s=0;s<2;++s)for(int a=0;a<N;++a){vector<int>v;v.reserve(N);for(int z=0;z<N;++z){int sh=s/2; (void)sh;v.push_back(t1[s][a][z]);}sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());t2[s][a]=get(2,v);}
for(int s=0;s<2;++s){vector<int> v;v.reserve(N);for(int z=0;z<N;++z)v.push_back(t2[s][z]);sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());t3[s]=get(3,v);}
vector<int>v={t3[0],t3[1]};sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return get(4,v);
}
int main(int argc,char **argv){int maxn=(argc>1?atoi(argv[1]):45); for(int m=2;m<=maxn;++m){auto now=chrono::steady_clock::now();int id=calc(m);cerr<<"n="<<m<<" class="<<id<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-now).count()<<"\n";cout<<m<<" "<<id<<"\n";}}
