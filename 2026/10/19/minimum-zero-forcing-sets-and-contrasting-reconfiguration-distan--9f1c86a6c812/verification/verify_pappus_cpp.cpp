#include <bits/stdc++.h>
using namespace std;
int adjbits[18];
const int FULL=(1<<18)-1;
int bc(int m){return __builtin_popcount((unsigned)m);}
int close_all(int m){
 while(true){int seen=m, add=0;
  for(int i=0;i<18;i++) if(m&(1<<i)){
   int w=adjbits[i]&~m; if(w && !(w&(w-1)))add|=w;
  }
  m|=add; if(m==seen)return m;
 }
}
struct stats{int count,edges,components,radius,diameter;map<int,int>sizes,degrees,ecc;};
int main(){
 // Point (x,y) has index 3x+y. Line (m,b) has index 9+3m+b.
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int m=0;m<3;m++){
  int b=(y-m*x+9)%3,u=3*x+y,v=9+3*m+b;
  adjbits[u]|=1<<v;adjbits[v]|=1<<u;
 }
 for(int i=0;i<18;i++)if(bc(adjbits[i])!=3)abort();
 vector<int> states; vector<int> minCounts;
 for(int k=1;k<=8;k++){
  vector<int> cur;
  for(int mask=0;mask<=FULL;mask++) if(bc(mask)==k && close_all(mask)==FULL)cur.push_back(mask);
  minCounts.push_back((int)cur.size());
  if(!cur.empty()){states=move(cur);break;}
 }
 int n=(int)states.size(),k=bc(states[0]);
 unordered_map<int,int> pos;pos.reserve(n*2);
 for(int i=0;i<n;i++)pos[states[i]]=i;
 cout << "minimum="<<k<<" configurations="<<n<<" scan=";
 for(auto c:minCounts)cout<<c<<",";cout<<"\n";
 map<int,int> bip;
 for(int m:states)bip[bc(m&511)]++;
 cout << "point_lines";for(auto [a,b]:bip)cout <<" "<<a<<":"<<b;cout<<"\n";
 for(int slide=0;slide<2;slide++){
  vector<vector<int>> links(n);
  for(int i=0;i<n;i++){
   int mask=states[i];
   for(int u=0;u<18;u++)if(mask&(1<<u)){
    int poss=((slide?adjbits[u]:FULL)&~mask);
    while(poss){int v=__builtin_ctz((unsigned)poss);poss&=poss-1;
     auto it=pos.find(mask^(1<<u)^(1<<v)); if(it!=pos.end())links[i].push_back(it->second);
    }
   }
   sort(links[i].begin(),links[i].end());
  }
  long long edge=0;map<int,int> degree;
  for(auto &x:links){edge+=x.size();degree[x.size()]++;}
  edge/=2;
  vector<char> visited(n,false);
  map<int,int> components,ecc;
  int rad=100000,dia=0;
  vector<int> q(n),dist(n),mark(n,0);
  int current=1;
  for(int s=0;s<n;s++) if(!visited[s]){
   int front=0,back=0;q[back++]=s;visited[s]=true;
   while(front<back){int u=q[front++];for(int v:links[u])if(!visited[v]){visited[v]=true;q[back++]=v;}}
   components[back]++;
  }
  for(int s=0;s<n;s++){
   int front=0,back=0;q[back++]=s;mark[s]=current;dist[s]=0;
   int e=0;
   while(front<back){int u=q[front++];e=max(e,dist[u]);for(int v:links[u])if(mark[v]!=current){mark[v]=current;dist[v]=dist[u]+1;q[back++]=v;}}
   current++;
   ecc[e]++; rad=min(rad,e);dia=max(dia,e);
  }
  cout << (slide?"slide":"jump")<<" edges="<<edge<<" comp=";
  for(auto [a,b]:components)cout<<a<<":"<<b<<",";
  cout<<" radius="<<rad<<" diameter="<<dia<<" degrees=";
  for(auto [a,b]:degree)cout<<a<<":"<<b<<",";
  cout<<" ecc=";
  for(auto [a,b]:ecc)cout<<a<<":"<<b<<",";
  cout<<"\n";
 }
}
