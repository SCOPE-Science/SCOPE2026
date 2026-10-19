#include <bits/stdc++.h>
using namespace std;
struct Arc {int to,w,a,defect;};
const int Q=256,R=9,L=Q*2*R,INF=100000000;
int id(int q,int k,int r){return (k*Q+q)*R+r;}
struct Item {int to,c,a,defect;};
vector<vector<Item>> adj(L);
bool valid(int q[5]){
 auto x=[&](int i){return (q[i]&1)!=0;}; auto b=[&](int i){return (q[i]&2)!=0;};
 return (x(0)||x(1)||b(1)||x(2))&&
        (x(0)||b(1)||b(2)||x(3))&&
        (x(0)||x(1)||b(1)||x(3)||b(3)||x(4))&&
        (b(0)||x(1)||x(3)||b(4));
}
int main(){
 vector<vector<Arc>> base(Q);
 int E=0;
 for(int s=0;s<Q;s++)for(int a=0;a<4;a++){
  int q[5];int u=s;for(int k=3;k>=0;k--){q[k]=u%4;u/=4;}q[4]=a;
  if(valid(q)){int to=(s*4+a)&255,w=(a&1)+((a&2)!=0),d=!(((q[0]&2)!=0)||((q[1]&1)!=0)||((q[2]&2)!=0));base[s].push_back({to,w,a,d}); E++;}
 }
 for(int k=0;k<2;k++)for(int q=0;q<Q;q++)for(int r=0;r<R;r++){
  int u=id(q,k,r);
  for(auto e:base[q])if(k+e.defect<=1){adj[u].push_back({id(e.to,k+e.defect,(r+1)%R),9*e.w-7,e.a,e.defect});}
 }
 int EE=0;for(auto &v:adj)EE+=v.size();
 cerr<<"states="<<L<<" base_edges="<<E<<" expanded_edges="<<EE<<"\n";
 // SPFA super source all vertices have initial distance zero
 vector<int> h(L,0), cnt(L,0);vector<unsigned char> inq(L,1);deque<int> dq;
 for(int u=0;u<L;u++)dq.push_back(u);
 long long relax=0;
 while(!dq.empty()){
  int u=dq.front();dq.pop_front();inq[u]=0;
  for(auto e:adj[u])if(h[e.to]>h[u]+e.c){
   h[e.to]=h[u]+e.c;relax++;
   if(++cnt[e.to]>L*3){cerr<<"No finite potential found"<<"\n";return 2;}
   if(!inq[e.to]){inq[e.to]=1;dq.push_back(e.to);}
  }
 }
 for(int u=0;u<L;u++)for(auto e:adj[u])assert(h[e.to]<=h[u]+e.c);
 cerr<<"potential relax="<<relax<<" range="<<*min_element(h.begin(),h.end())<<".."<<*max_element(h.begin(),h.end())<<"\n";
 vector<int> lower(R,INF), witness(R,-1),pathlen(R,INF);
 for(int s=0;s<Q;s++){
  vector<int> dist(L,INF),steps(L,INF),pr(L,-1);int start=id(s,0,0);dist[start]=0;steps[start]=0;
  priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;pq.push({0,start});
  while(!pq.empty()){
   auto [dv,u]=pq.top();pq.pop();if(dv!=dist[u])continue;
   for(auto e:adj[u]){
    int cc=e.c+h[u]-h[e.to];if(cc<0){cerr<<"BAD reduced "<<cc<<"\n";return 5;}
    int nd=dv+cc;
    if(nd<dist[e.to]){dist[e.to]=nd;steps[e.to]=steps[u]+1;pr[e.to]=u;pq.push({nd,e.to});}
   }
  }
  for(int r=0;r<R;r++)for(int k=0;k<2;k++){
   int t=id(s,k,r);if(dist[t]>=INF)continue;
   int c=dist[t]+h[t]-h[start];
   if(c<lower[r] || (c==lower[r]&&steps[t]<pathlen[r])){lower[r]=c;witness[r]=s;pathlen[r]=steps[t];}
  }
 }
 int expect[R]={0,2,-5,6,-1,1,3,5,-2}; for(int r=0;r<R;r++)assert(lower[r]==expect[r]);
 for(int r=0;r<R;r++)cout<<"residue "<<r<<" minadjust "<<lower[r]<<" witness-state "<<witness[r]<<" witness-length "<<pathlen[r]<<" normalized f="<<(7*r+lower[r])/9<<"\n";
 cout<<"LOWER_CERT_OK\n";
}
