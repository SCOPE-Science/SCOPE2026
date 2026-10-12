#include <bits/stdc++.h>
using namespace std;
struct Solver {
 int n,N, nv, best=0; long long nodes=0;
 vector<bitset<256>> allowed; vector<int> found, bestv;
 vector<bitset<128>> B;
 Solver(int n_,int N_):n(n_),N(N_),nv(1<<n_),allowed(nv),B(nv) {
  for(int x=0;x<nv;x++){
   for(int del=0;del<n;del++){
    int top=x>>(n-del),bottom=x&((1<<(n-del-1))-1);
    int t=(top<<(n-del-1))|bottom;
    B[x].set(t);
    for(int k=0;k<n-1;k++) B[x].set(t^(1<<k));
   }
  }
  for(int x=0;x<nv;x++) for(int y=x+1;y<nv;y++)
    if((B[x]&B[y]).count() < (size_t)N) {allowed[x].set(y);allowed[y].set(x);}
 }
 void expand(vector<int> P) {
  nodes++;
  if(P.empty()) {if((int)found.size()>best){best=found.size();bestv=found;}return;}
  vector<int> sorted,colors;
  vector<int> remain=P;
  for(int k=1; !remain.empty();k++) {
   vector<int> next,independent;
   for(int v:remain){
    bool ok=true;
    for(int u:independent)if(allowed[v].test(u)){ok=false;break;}
    if(ok){independent.push_back(v);sorted.push_back(v);colors.push_back(k);}
    else next.push_back(v);
   }
   remain=move(next);
  }
  for(int i=(int)sorted.size()-1;i>=0;i--){
   if((int)found.size()+colors[i]<=best) return;
   int v=sorted[i]; found.push_back(v);
   vector<int> Q;
   for(int j=0;j<i;j++)if(allowed[v].test(sorted[j])) Q.push_back(sorted[j]);
   if(Q.empty()) {if((int)found.size()>best){best=found.size();bestv=found;}}
   else expand(Q);
   found.pop_back();
  }
 }
 void run(){
  vector<int> p(nv);iota(p.begin(),p.end(),0);
  stable_sort(p.begin(),p.end(),[&](int a,int b){return allowed[a].count()>allowed[b].count();});
  auto t=chrono::steady_clock::now();expand(p);
  cout<<"n="<<n<<" N="<<N<<" best="<<best<<" nodes="<<nodes<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<" witness=";
  sort(bestv.begin(),bestv.end());for(int i:bestv) cout<<bitset<8>(i).to_string().substr(8-n)<<",";cout<<"\n"<<flush;
 }
};
int main(){int expected[]={0,0,0,0,5,5,6,8,12};for(int n=4;n<=8;n++){Solver s(n,5);s.run(); if(s.best!=expected[n]){cerr<<"CAPACITY_MISMATCH n="<<n<<"\n";return 1;}}cout<<"VERIFY_OK\n";}
