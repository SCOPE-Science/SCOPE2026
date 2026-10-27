#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
// Exhaustive finite-state certificate for Roman domination on GP(n,2).
// A column digit q is the pair (outer=q/3, inner=q%3).
struct Arc {int s,t,w;};
int main() {
  constexpr int B=9, S=9*9*9*9;
  vector<Arc> arcs; arcs.reserve(S*9);
  for(int s=0;s<S;++s) {
    const int a=s/729,b=(s/81)%9,c=(s/9)%9,d=s%9;
    for(int e=0;e<B;++e) {
      const bool outer_ok=c/3 != 0 || b/3==2 || d/3==2 || c%3==2;
      const bool inner_ok=c%3 != 0 || a%3==2 || e%3==2 || c/3==2;
      if(outer_ok && inner_ok)
        arcs.push_back({s, (s%729)*9+e, 7*(e/3+e%3)-8});
    }
  }
  // The zero-valued super-source has a zero arc to every state.
  // In-place Bellman-Ford produces an integral potential h.
  vector<int> h(S,0);
  int rounds=0;
  for(;rounds<S;++rounds) {
    bool changed=false;
    for(const auto& a:arcs) if(h[a.t]>h[a.s]+a.w) {
      h[a.t]=h[a.s]+a.w; changed=true;
    }
    if(!changed)break;
  }
  assert(rounds<S); // A negative circuit would prevent stabilization.
  vector<vector<int>> g(S),gt(S);
  int tight_arcs=0;
  for(const auto& a:arcs) {
    const int slack=a.w+h[a.s]-h[a.t];
    assert(slack>=0); // Checked finite dual certificate.
    if(slack==0){g[a.s].push_back(a.t);gt[a.t].push_back(a.s);++tight_arcs;}
  }
  // Kosaraju SCC decomposition of the tight-edge digraph.
  vector<int> vis(S,0),order;order.reserve(S);
  for(int v=0;v<S;++v)if(!vis[v]){
    vector<pair<int,int>> stk{{v,0}};vis[v]=1;
    while(!stk.empty()) {
      auto &[x,i]=stk.back();
      if(i<int(g[x].size())){
        int y=g[x][i++];if(!vis[y]){vis[y]=1;stk.push_back({y,0});}
      }else{order.push_back(x);stk.pop_back();}
    }
  }
  vector<int> comp(S,-1);vector<vector<int>> members;
  for(int j=S-1;j>=0;--j) {
    int v=order[j];if(comp[v]>=0)continue;
    int ci=int(members.size()); members.push_back({});
    vector<int> stk{v};comp[v]=ci;
    while(!stk.empty()){
      int x=stk.back();stk.pop_back();members[ci].push_back(x);
      for(int y:gt[x])if(comp[y]<0){comp[y]=ci;stk.push_back(y);}
    }
  }
  int cyclic=0, cycle_component=-1,internal=0;
  for(int i=0;i<int(members.size());++i){
    int links=0;
    for(int x:members[i])for(int y:g[x])if(comp[y]==i)++links;
    if(members[i].size()>1||links){++cyclic;cycle_component=i;internal=links;}
  }
  assert(cyclic==1);
  assert(members[cycle_component].size()==7 && internal==7);
  for(int x:members[cycle_component]){
    int indeg=0,outdeg=0;
    for(int y:g[x])if(comp[y]==cycle_component)++outdeg;
    for(int y:gt[x])if(comp[y]==cycle_component)++indeg;
    assert(indeg==1 && outdeg==1);
  }
  int v=*min_element(members[cycle_component].begin(),members[cycle_component].end());
  vector<int> digits;
  int curr=v;
  do{
    digits.push_back(curr/729);
    int next=-1;
    for(int y:g[curr])if(comp[y]==cycle_component){assert(next==-1);next=y;}
    curr=next;
  }while(curr!=v);
  assert(digits.size()==7);
  cout<<"states="<<S<<" admissible_arcs="<<arcs.size()<<"\n";
  cout<<"bellman_rounds="<<rounds<<" potential_min="<<*min_element(h.begin(),h.end())
      <<" potential_max="<<*max_element(h.begin(),h.end())<<"\n";
  cout<<"tight_arcs="<<tight_arcs<<" total_scc="<<members.size()
      <<" cyclic_scc="<<cyclic<<" cyclic_vertices=7 cyclic_arcs=7\n";
  cout<<"unique_7_word_pairs=";
  for(int q:digits)cout<<'('<<q/3<<','<<q%3<<')';
  cout<<"\n";
  // Canonical published seven-column pattern, direct validity and weight test.
  for(int n: {7,14,21,28,35}){
    vector<int> outer(n,0),inner(n,0);
    for(int i=0;i<n;++i){
      int r=i%7;outer[i]=(r==0?2:((r==2||r==5)?1:0));
      inner[i]=((r==3||r==4)?2:0);
    }
    int weight=0;
    for(int i=0;i<n;++i){
      weight+=outer[i]+inner[i];
      if(outer[i]==0)assert(outer[(i+n-1)%n]==2||outer[(i+1)%n]==2||inner[i]==2);
      if(inner[i]==0)assert(inner[(i+n-2)%n]==2||inner[(i+2)%n]==2||outer[i]==2);
    }
    assert(weight==8*(n/7));
    cout<<"pattern_check_n="<<n<<" weight="<<weight<<" passed\n";
  }
  array<pair<int,int>,7> template_labels{{{2,0},{0,0},{1,0},{0,2},{0,2},{1,0},{0,0}}};
  for(int shift=1;shift<=6;++shift){
    int disagreements=0;
    for(int i=0;i<7;++i){
      const auto& a=template_labels[i];
      const auto& b=template_labels[(i+shift)%7];
      disagreements+=(a.first!=b.first)+(a.second!=b.second);
    }
    assert(disagreements==8);
  }
  cout<<"all_six_nonzero_shift_Hamming_distances_per_period=8\n";
  cout<<"PASS: all zero-excess closed walks are repetitions of the sole 7-cycle\n";
}
