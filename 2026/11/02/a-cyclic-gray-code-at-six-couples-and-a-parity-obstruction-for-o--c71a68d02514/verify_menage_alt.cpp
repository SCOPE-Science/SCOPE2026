#include <array>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
int main(){
 for(int n=3;n<=9;n++){
   vector<int> p(n);iota(p.begin(),p.end(),0);
   long long pos=0,neg=0;
   do{
     bool valid=true;
     for(int i=0;i<n;i++)if(p[i]==i||p[i]==(i+1)%n){valid=false;break;}
     if(!valid)continue;
     int inv=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)inv+=(p[i]>p[j]);
     ((inv&1)?neg:pos)++;
   }while(next_permutation(p.begin(),p.end()));
   assert(pos-neg==(n%2?n-2:0));
   cout<<"SIGNED_MENAGE_OK n="<<n<<" even="<<pos<<" odd="<<neg<<"\n";
 }
 int n=6;vector<array<int,6>> ps;array<int,6> p={0,1,2,3,4,5};
 do{
   bool good=true;for(int i=0;i<n;i++)if(p[i]==i||p[i]==(i+1)%n)good=false;
   if(good)ps.push_back(p);
 }while(next_permutation(p.begin(),p.end()));
 assert(ps.size()==80);
 ifstream f("hamiltonian_cycle.txt");assert(f.good());string line;getline(f,line);stringstream ss(line);
 vector<int> cyc;string t;while(getline(ss,t,','))cyc.push_back(stoi(t));
 assert(cyc.size()==80);
 set<int> uniq(cyc.begin(),cyc.end());assert(uniq.size()==80&&*uniq.begin()==0&&*uniq.rbegin()==79);
 for(int k=0;k<80;k++){
    auto a=ps[cyc[k]],b=ps[cyc[(k+1)%80]];
    vector<int> changed;for(int i=0;i<n;i++)if(a[i]!=b[i])changed.push_back(i);
    assert(changed.size()==2&&a[changed[0]]==b[changed[1]]&&a[changed[1]]==b[changed[0]]);
    for(int i=0;i<n;i++)assert(b[i]!=i&&b[i]!=(i+1)%n);
 }
 vector<set<int>> adj(80);
 for(int u=0;u<80;u++)for(int v=u+1;v<80;v++){
   vector<int> diff;for(int i=0;i<n;i++)if(ps[u][i]!=ps[v][i])diff.push_back(i);
   if(diff.size()==2){adj[u].insert(v);adj[v].insert(u);}
 }
 long long e=0;map<int,int> ecc;
 for(int u=0;u<80;u++){
   e+=adj[u].size();vector<int>d(80,-1);queue<int>q;q.push(u);d[u]=0;
   while(!q.empty()){int x=q.front();q.pop();for(int y:adj[x])if(d[y]==-1){d[y]=d[x]+1;q.push(y);}}
   assert(all_of(d.begin(),d.end(),[](int z){return z>=0;}));ecc[*max_element(d.begin(),d.end())]++;
 }
 assert(e==414 && ecc.at(5)==48 && ecc.at(6)==32 && ecc.size()==2);
 cout<<"ALTERNATE_HAMILTON_CYCLE_OK vertices=80 edges=207 eccentricities=5:48,6:32\n";
}
