// Finite exhaustive verifier for Kempe-switch metrics of the dodecahedral graph.
// Standard C++17; no external libraries or graph datasets.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr int N=20;
using State=string;
vector<int> adj[N];
vector<State> canonical_states;
static void add_edge(int u,int v){adj[u].push_back(v);adj[v].push_back(u);}
static State canonical(const State& a){
  array<int,3> label={-1,-1,-1}; State b=a; int next=0;
  for(int i=0;i<N;i++){
    int c=a[i]-'0'; if(label[c]<0)label[c]=next++;
    b[i]=char('0'+label[c]);
  }
  return b;
}
static void generate(State& a,int i,int used){
  if(i==N){ if(used==3)canonical_states.push_back(a);return; }
  for(int c=0;c<=used && c<3;c++){
    bool valid=true;
    for(int j:adj[i])if(j<i && a[j]==char('0'+c)){valid=false;break;}
    if(!valid)continue;
    a[i]=char('0'+c);
    generate(a,i+1,max(used,c+1));
  }
}
static vector<State> kempe_moves(const State& a){
  vector<State> moves;
  for(int c=0;c<3;c++)for(int d=c+1;d<3;d++){
    array<bool,N> seen={};
    for(int start=0;start<N;start++){
      if(seen[start] || (a[start]!='0'+c && a[start]!='0'+d))continue;
      queue<int> q; q.push(start); seen[start]=true;
      vector<int> component;
      while(!q.empty()){
        int u=q.front();q.pop();component.push_back(u);
        for(int v:adj[u]){
          if(!seen[v]&&(a[v]=='0'+c||a[v]=='0'+d)){
            seen[v]=true;q.push(v);
          }
        }
      }
      State b=a;
      for(int u:component)b[u]=char('0'+c+d-(a[u]-'0'));
      moves.push_back(b);
    }
  }
  sort(moves.begin(),moves.end());
  moves.erase(unique(moves.begin(),moves.end()),moves.end());
  return moves;
}
static vector<vector<int>> make_graph(const vector<State>& states,bool quotient){
  unordered_map<string,int> index;
  for(int i=0;i<(int)states.size();i++)index.emplace(states[i],i);
  vector<vector<int>> graph(states.size());
  for(int i=0;i<(int)states.size();i++){
    for(const auto& b:kempe_moves(states[i])){
      auto c=quotient?canonical(b):b;
      auto it=index.find(c);
      if(it==index.end()){cerr<<"Missing colouring!"<<endl;abort();}
      if(it->second!=i)graph[i].push_back(it->second);
    }
    auto& a=graph[i];sort(a.begin(),a.end());
    a.erase(unique(a.begin(),a.end()),a.end());
  }
  for(int i=0;i<(int)graph.size();i++)for(int j:graph[i]){
    if(!binary_search(graph[j].begin(),graph[j].end(),i)){
      cerr<<"Not symmetric"<<endl;abort();
    }
  }
  return graph;
}
struct Stats{
  long long vertices=0,edges=0;
  map<int,int> degrees,eccentricities;
  int radius=1000000,diameter=0;
};
static Stats analyze(const vector<vector<int>>& graph){
  const int n=graph.size();Stats s;s.vertices=n;
  for(auto& neighbors:graph){s.edges+=(int)neighbors.size();s.degrees[(int)neighbors.size()]++;}
  assert(s.edges%2==0);s.edges/=2;
  vector<int> dist(n,-1),seen(n,0),queue(n);
  int stamp=0;
  for(int start=0;start<n;start++){
    stamp++;int head=0,tail=1;queue[0]=start;seen[start]=stamp;dist[start]=0;
    int ecc=0;
    while(head<tail){
      int u=queue[head++];int d=dist[u];ecc=max(ecc,d);
      for(int v:graph[u])if(seen[v]!=stamp){
        seen[v]=stamp;dist[v]=d+1;queue[tail++]=v;
      }
    }
    if(tail!=n){cerr<<"Disconnected!"<<endl;abort();}
    s.radius=min(s.radius,ecc);s.diameter=max(s.diameter,ecc);s.eccentricities[ecc]++;
  }
  return s;
}
static void print(const string& title,const Stats& s){
  cout<<title<<": V="<<s.vertices<<" E="<<s.edges<<" radius="<<s.radius<<" diameter="<<s.diameter<<" degrees=";
  for(auto [k,v]:s.degrees)cout<<k<<":"<<v<<",";
  cout<<" eccentricities=";
  for(auto [k,v]:s.eccentricities)cout<<k<<":"<<v<<",";
  cout<<"\n";
}
int main(){
  // Explicit generalized Petersen model GP(10,2) of the dodecahedral graph:
  // vertices u_i=i, v_i=10+i; edges u_i u_(i+1), u_i v_i, v_i v_(i+2).
  for(int i=0;i<10;i++){
    add_edge(i,(i+1)%10);
    add_edge(i,10+i);
    add_edge(10+i,10+(i+2)%10);
  }
  for(int i=0;i<N;i++)if(adj[i].size()!=3){cerr<<"Not cubic"<<endl;return 1;}
  State blank(N,'?');generate(blank,0,0);
  sort(canonical_states.begin(),canonical_states.end());
  assert(canonical_states.size()==1200);
  auto Q=make_graph(canonical_states,true);
  Stats qs=analyze(Q);print("QUOTIENT",qs);
  assert(qs.vertices==1200 && qs.edges==5360 && qs.radius==6 && qs.diameter==7);
  assert((qs.degrees==map<int,int>{{8,140},{9,1020},{10,20},{11,20}}));
  assert((qs.eccentricities==map<int,int>{{6,460},{7,740}}));
  vector<State> labeled;
  array<int,3> p={0,1,2};
  for(auto& x:canonical_states){
    do{
      State y=x;
      for(char& c:y)c=char('0'+p[c-'0']);
      labeled.push_back(y);
    }while(next_permutation(p.begin(),p.end()));
  }
  sort(labeled.begin(),labeled.end());
  labeled.erase(unique(labeled.begin(),labeled.end()),labeled.end());
  assert(labeled.size()==7200);
  auto F=make_graph(labeled,false);
  Stats fs=analyze(F);print("LABELED",fs);
  assert(fs.vertices==7200 && fs.edges==36120 && fs.radius==7 && fs.diameter==8);
  assert((fs.degrees==map<int,int>{{10,6960},{11,240}}));
  assert((fs.eccentricities==map<int,int>{{7,5280},{8,1920}}));
  cout<<"VERIFY_OK\n";
}
