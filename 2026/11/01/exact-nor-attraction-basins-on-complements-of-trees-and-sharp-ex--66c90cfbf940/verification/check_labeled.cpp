// Standalone labeled-tree census of open-neighborhood NOR on complements.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <utility>
#include <vector>
using U=std::uint64_t;
using Key=std::pair<U,U>;
using Graph=std::vector<std::vector<int>>;
static U seed=0x9e3779b97f4a7c15ULL;
U rand64(){seed^=seed<<13;seed^=seed>>7;seed^=seed<<17;return seed;}
Graph prufer(const std::vector<int>& seq,int n){
  Graph g(n); std::vector<int> deg(n,1);
  for(int a:seq)++deg[a];
  for(int a:seq){
    int leaf=0;while(deg[leaf]!=1)++leaf;
    g[leaf].push_back(a);g[a].push_back(leaf);--deg[leaf];--deg[a];
  }
  int a=-1,b=-1;
  for(int i=0;i<n;++i)if(deg[i]==1){if(a<0)a=i;else b=i;}
  g[a].push_back(b);g[b].push_back(a);return g;
}
void test(const Graph& g,std::uint64_t& states){
  int n=(int)g.size();U lim=U(1)<<n,all=lim-1;
  std::vector<U> closed(n);int internal=0,leaf=0,center=-1;U phi=0;
  for(int v=0;v<n;++v){
    closed[v]=U(1)<<v;
    for(int u:g[v])closed[v]|=U(1)<<u;
    int d=(int)g[v].size();
    if(d==1)++leaf;
    if(d>1){++internal;phi+=(U(1)<<(d+1))-2*d-2;}
    if(d==n-1)center=v;
  }
  auto update=[&](U S){U ans=0;for(int v=0;v<n;++v)if(!(S&(all^closed[v])))ans|=U(1)<<v;return ans;};
  auto key=[](U x,U y){return Key(std::min(x,y),std::max(x,y));};
  std::map<Key,U> predicted,actual;
  if(center>=0){
    predicted[key(U(1)<<center,all)]=lim-2*(n-1);
    for(int v=0;v<n;++v)for(int u:g[v])if(u>v)
      predicted[key((U(1)<<u)|(U(1)<<v),(U(1)<<u)|(U(1)<<v))]=2;
  }else{
    predicted[key(0,all)]=lim-2*n+1-phi;
    for(int v=0;v<n;++v){
      if(g[v].size()>1)
        predicted[key(U(1)<<v,closed[v])]=(U(1)<<(g[v].size()+1))-2*g[v].size()-1;
      for(int u:g[v])if(u>v)
        predicted[key((U(1)<<u)|(U(1)<<v),(U(1)<<u)|(U(1)<<v))]=1+(g[u].size()==1)+(g[v].size()==1);
    }
  }
  for(U S=0;S<lim;++S){
    U y=update(S),z=update(y);
    if(update(z)!=y)throw std::runtime_error("failure of third-iterate identity");
    ++actual[key(y,z)];
  }
  if(actual!=predicted){
    std::cerr<<"n="<<n<<" center="<<center<<" expected="<<predicted.size()<<" actual="<<actual.size()<<"\n";
    throw std::runtime_error("orbit basin mismatch");
  }
  states+=lim;
}
int main(){
  std::uint64_t trees=0,states=0;
  for(int n=4;n<=7;++n){
    U total=1;for(int j=0;j<n-2;++j)total*=n;
    for(U index=0;index<total;++index){
      U t=index;std::vector<int> seq(n-2);
      for(int j=0;j<n-2;++j){seq[j]=int(t%n);t/=n;}
      test(prufer(seq,n),states);++trees;
    }
    std::cout<<"all labeled trees n="<<n<<" count="<<total<<" passed\n";
  }
  for(int n=8;n<=12;++n){
    for(int trial=0;trial<100;++trial){
      std::vector<int> seq(n-2);for(int& a:seq)a=int(rand64()%n);
      test(prufer(seq,n),states);++trees;
    }
    std::cout<<"seeded labeled trees n="<<n<<" samples=100 passed\n";
  }
  std::cout<<"PASS trees="<<trees<<" configurations="<<states<<"\n";
}
