#include <bits/stdc++.h>
using namespace std;
const int u[8]={0,0,1,1,2,2,3,3};const int v[8]={0,1,2,3,0,1,2,3};
int multinomial(const vector<int>&m){int val=1,s=0;for(int x:m)for(int j=1;j<=x;j++){s++;int tmp=1;for(int k=1;k<=j;k++)tmp=tmp*(s-k+1)/k; //unused
}return 0;}
int local(const array<int,8>&m,int vertex,int last){int a=0,b=0;for(int e=0;e<8;e++)if(u[e]==vertex){int t=m[e]-(e==last);if(t<0)return 0;if(a==0)a=t;else b=t;} // 2 outgoing types
 int d=a+b;if(a==0||b==0)return 1;long long bin=1;for(int j=1;j<=min(a,b);j++){bin=bin*(d-j+1)/j;if(bin>2)return 3;}return (int)bin;
}
int ways(const array<int,8>&m,int s,int t){int out[4]={},in[4]={},active[4]={},V[4],k=0;for(int i=0;i<8;i++){out[u[i]]+=m[i];in[v[i]]+=m[i];}for(int i=0;i<4;i++){if(out[i]-in[i]!=(i==s)-(i==t))return 0;if(out[i]+in[i]||i==s||i==t)active[i]=1,V[k++]=i;}
int nr[4],r=0;for(int i=0;i<k;i++)if(V[i]!=t)nr[r++]=V[i];int opts[4][2],sizes[4];for(int i=0;i<r;i++){sizes[i]=0;for(int e=0;e<8;e++)if(m[e]>0&&u[e]==nr[i]&&u[e]!=v[e])opts[i][sizes[i]++]=e;if(!sizes[i])return 0;}
int rootways=local(m,t,-1),ans=0;
for(int mask=0;mask<(1<<r);mask++){int chosen[4],parent[4];bool valid=1;for(int i=0;i<r;i++){int z=(mask>>i)&1;if(z>=sizes[i]){valid=0;break;}chosen[i]=opts[i][z];parent[nr[i]]=v[chosen[i]];}if(!valid)continue;
for(int i=0;i<r;i++){int z=nr[i];bool seen[4]={};while(z!=t){if(seen[z]){valid=0;break;}seen[z]=1;z=parent[z];}if(!valid)break;}if(!valid)continue;
int q=rootways;for(int i=0;i<r;i++)q=min(3,q*local(m,nr[i],chosen[i]));ans=min(3,ans+q);}return ans;
}
vector<vector<int>> getcycles(const array<int,8>&m){vector<vector<int>>ret;for(int e=0;e<8;e++)if(m[e]>=2){int start=u[e],cur=v[e];vector<int>cyc{e};bool seen[4]={};seen[start]=1;while(cur!=start){if(seen[cur])break;seen[cur]=1;int next=-1;for(int j=0;j<8;j++)if(m[j]>=2&&u[j]==cur){if(next!=-1){next=-2;break;}next=j;}if(next<0)break;cyc.push_back(next);cur=v[next];}if(cur==start){int low=*min_element(cyc.begin(),cyc.end());if(e==low)ret.push_back(cyc);}}return ret;}
int main(int argc,char**argv){int B=argc>1?atoi(argv[1]):12;set<tuple<int,int,array<int,8>>> uniq;long long checked=0,valid=0;for(int s=0;s<4;s++)for(int t=0;t<4;t++){int dA=(s==0)-(t==0),dB=(s==1)-(t==1),dD=(s==3)-(t==3);for(int a=0;a<=B;a++)for(int h=0;h<=B;h++)for(int b=0;b<=B;b++)for(int c=0;c<=B;c++)for(int d=0;d<=B;d++){int e=b-dA,f=c+d-b-dB,g=d+dD;if(e<0||f<0||g<0||e>B||f>B||g>B)continue;array<int,8>m={a,b,c,d,e,f,g,h};checked++;if(ways(m,s,t)!=2)continue;valid++;auto cycles=getcycles(m);for(auto&cyc:cycles){int minimum=10000;for(int i:cyc)minimum=min(minimum,m[i]);for(int i:cyc)m[i]-=minimum-2;}uniq.insert({s,t,m});}}cerr<<"B "<<B<<" checked "<<checked<<" valid "<<valid<<" bases "<<uniq.size()<<endl;
for(auto [s,t,m]:uniq){int w=ways(m,s,t);if(w!=2){cerr<<"wrong normalized "<<w<<endl;return 1;}cout<<s<<" "<<t;for(int e:m)cout<<" "<<e;cout<<" :";for(auto&c:getcycles(m)){auto m1=m;for(int e:c)m1[e]++;if(ways(m1,s,t)==2)cout<<" "<<c.size();}cout<<"\n";}}
