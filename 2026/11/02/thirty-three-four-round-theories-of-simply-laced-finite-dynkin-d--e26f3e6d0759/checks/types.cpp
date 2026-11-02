#include <bits/stdc++.h>
using namespace std;
using Vec=vector<int>;
map<Vec,int> dictionaries[5];
int intern(int depth, Vec key) {
 auto &dict=dictionaries[depth]; auto it=dict.find(key);
 if(it!=dict.end())return it->second;
 int id=(int)dict.size()+1;
 dict.emplace(move(key),id);
 return id;
}
vector<Vec> path(int n) {vector<Vec> a(n,Vec(n));for(int i=1;i<n;i++)a[i-1][i]=a[i][i-1]=1;return a;}
vector<Vec> spider(int a,int b,int c) {int n=1+a+b+c; vector<Vec> G(n,Vec(n));int nxt=1;for(int len:{a,b,c}){int parent=0;for(int k=0;k<len;k++){G[parent][nxt]=G[nxt][parent]=1;parent=nxt++;}}return G;}
int atomic_signature(const vector<Vec>& G,int a,int b,int c,int d) {
 int s=0;int p[4]={a,b,c,d};for(int i=0;i<4;i++)for(int j=0;j<i;j++)s=s*3+(p[i]==p[j]?1:(G[p[i]][p[j]]?2:0));return s;
}
int root_type(const vector<Vec>& G){
 int n=G.size();
 vector<int> T1(n*n*n),T2(n*n),T3(n);
 Vec children;children.reserve(n);
 auto canon=[&](int depth,Vec &v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());return intern(depth,v);};
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++){
  children.clear();for(int d=0;d<n;d++)children.push_back(atomic_signature(G,a,b,c,d));
  T1[(a*n+b)*n+c]=canon(1,children);
 }
 for(int a=0;a<n;a++)for(int b=0;b<n;b++){
  children.clear();for(int c=0;c<n;c++)children.push_back(T1[(a*n+b)*n+c]);
  T2[a*n+b]=canon(2,children);
 }
 for(int a=0;a<n;a++){
  children.clear();for(int b=0;b<n;b++)children.push_back(T2[a*n+b]);
  T3[a]=canon(3,children);
 }
 children.clear();for(int a=0;a<n;a++)children.push_back(T3[a]);
 return canon(4,children);
}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):37;
 map<int,Vec> clusters;map<int,vector<string>> names;
 for(int n=1;n<=N;n++){
  int id=root_type(path(n));names[id].push_back("A"+to_string(n));
  if(n>=4){id=root_type(spider(1,1,n-3));names[id].push_back("D"+to_string(n));}
  if(n>=6&&n<=8){id=root_type(spider(1,2,n-4));names[id].push_back("E"+to_string(n));}
 }
 cout<<"CLUSTERS "<<names.size()<<"\n";
 for(auto &[id,labels]:names){cout<<id<<":";for(auto &s:labels)cout<<" "<<s;cout<<"\n";}
 for(int k=1;k<=4;k++)cout<<"TYPE_COUNT "<<k<<" "<<dictionaries[k].size()<<"\n";
}
