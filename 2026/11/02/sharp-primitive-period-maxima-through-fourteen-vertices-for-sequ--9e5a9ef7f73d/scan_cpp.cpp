// Exact primitive-period census for the closed-neighborhood (up=1,down=3)
// bi-threshold graph rule with permutation sequential scan. Standard C++17.
#include <bits/stdc++.h>
using namespace std;
struct Witness{int n=0, period=0, state=0, max_tree_count=0, orbit_count=0; vector<pair<int,int>> edges;};
int main(){
  ifstream f("tree_catalog.txt");
  if(!f){cerr<<"missing tree_catalog.txt\n";return 1;}
  map<int,int> classcounts;
  map<int,Witness> best;
  string line; int record=0;
  while(getline(f,line)) {
    if(line.empty()) continue;
    istringstream input(line); int n; input>>n;
    vector<pair<int,int>> edges; vector<int> neighbors(n,0);
    int u,v;
    while(input>>u>>v){
      if(u<0||v<0||u>=n||v>=n||u==v){cerr<<"bad edge";return 2;}
      edges.push_back({u,v}); neighbors[u]|=1<<v;neighbors[v]|=1<<u;
    }
    if((int)edges.size()!=n-1){cerr<<"not tree edge count";return 3;}
    ++classcounts[n];++record;
    int N=1<<n;
    vector<int> successor(N);
    for(int state=0;state<N;++state){
      int x=state;
      for(int vertex=0;vertex<n;++vertex){
        int k=__builtin_popcount((unsigned)(x&neighbors[vertex]));
        if((x>>vertex)&1){if(k<2)x &= ~(1<<vertex);}
        else if(k>=1)x|=1<<vertex;
      }
      successor[state]=x;
    }
    vector<int> seen(N,0), pos(N,-1);
    int localmax=0,localfirst=-1,localcount=0;
    vector<int> trail;trail.reserve(N);
    for(int s=0;s<N;++s){
      if(seen[s]!=0)continue;
      trail.clear();int x=s;int stamp=s+1;
      while(seen[x]==0){
        seen[x]=stamp;pos[x]=(int)trail.size();trail.push_back(x);x=successor[x];
      }
      if(seen[x]==stamp){
        int p=(int)trail.size()-pos[x];
        if(p>localmax){localmax=p;localfirst=x;localcount=1;}
        else if(p==localmax)localcount++;
      }
      for(int t:trail)seen[t]=-1;
    }
    auto &res=best[n];
    if(localmax>res.period){res={n,localmax,localfirst,1,localcount,edges};}
    else if(localmax==res.period){res.max_tree_count++;res.orbit_count+=localcount;}
  }
  const int counts[]={1,1,1,2,3,6,11,23,47,106,235,551,1301,3159};
  ofstream out("cpp_certificate.txt");
  for(int n=1;n<=14;++n){
    auto w=best[n];
    if(classcounts[n]!=counts[n-1]){cerr<<"incorrect class count n="<<n<<"\n";return 4;}
    ostringstream o;o<<"n="<<n<<" classes="<<classcounts[n]<<" max="<<w.period
      <<" maximizer_classes="<<w.max_tree_count<<" extremal_orbits="<<w.orbit_count
      <<" witness_state="<<w.state<<" edges=";
    for(auto e:w.edges)o<<"("<<e.first<<","<<e.second<<")";
    cout<<o.str()<<'\n';out<<o.str()<<'\n';
    int state=w.state;
    // Direct witness replay independently of the successor graph used in the scan.
    state=w.state;
    vector<int> mask(n,0);
    for(auto [a,b]:w.edges){mask[a]|=1<<b;mask[b]|=1<<a;}
    set<int> trace;
    for(int step=0;step<w.period;++step){
      if(!trace.insert(state).second){cerr<<"premature witness repeat n="<<n<<"\n";return 5;}
      for(int v=0;v<n;++v){int c=__builtin_popcount((unsigned)(state&mask[v]));
        if(state&(1<<v)){if(c<2)state ^=1<<v;}
        else if(c>0)state^=1<<v;
      }
    }
    if(state!=w.state){cerr<<"not a full witness cycle n="<<n<<"\n";return 6;}
  }
  cout<<"CPP_VERIFY_OK: "<<record<<" unlabelled trees n=1..14\n";
}
