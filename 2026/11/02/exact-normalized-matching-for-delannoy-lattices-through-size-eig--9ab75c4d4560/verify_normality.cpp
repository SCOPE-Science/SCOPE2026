#include <bits/stdc++.h>
using namespace std;
struct Edge{int to,next;long long cap;};
struct Dinic{
 vector<int> head,lev,it;vector<Edge> E;
 Dinic(int n,int hint=0):head(n,-1),lev(n),it(n){E.reserve(hint);}
 void add(int a,int b,long long cap){int p=E.size();E.push_back({b,head[a],cap});head[a]=p;E.push_back({a,head[b],0});head[b]=p+1;}
 bool bfs(int s,int t){fill(lev.begin(),lev.end(),-1);queue<int> q;q.push(s);lev[s]=0;while(!q.empty()){int u=q.front();q.pop();for(int p=head[u];p!=-1;p=E[p].next){auto&e=E[p];if(e.cap>0 && lev[e.to]<0){lev[e.to]=lev[u]+1;q.push(e.to);}}}return lev[t]!=-1;}
 long long dfs(int u,int t,long long f){if(u==t)return f;for(int &p=it[u];p!=-1;p=E[p].next){auto&e=E[p];if(e.cap>0 && lev[e.to]==lev[u]+1){long long x=dfs(e.to,t,min(f,e.cap));if(x>0){e.cap-=x;E[p^1].cap+=x;return x;}}}return 0;}
 long long flow(int s,int t){long long f=0;while(bfs(s,t)){it=head;while(auto x=dfs(s,t,LLONG_MAX/4)) f+=x;}return f;}
};
void generate(int n,string &s,vector<vector<string>>&layer,int rank=0){
 if(n==0){layer[rank].push_back(s);return;}
 s.push_back('H');generate(n-1,s,layer,rank);s.back()='V';generate(n-1,s,layer,rank+1);s.pop_back();
 if(n>=2){s.push_back('D');generate(n-2,s,layer,rank+1);s.pop_back();}
}
// Returns the Delannoy number D(a,b), independently of the word generator.
long long delannoy(int a,int b){
 vector<vector<long long>> d(a+1,vector<long long>(b+1,0));
 for(int i=0;i<=a;i++) for(int j=0;j<=b;j++) {
  if(i==0 || j==0)d[i][j]=1;
  else d[i][j]=d[i-1][j]+d[i][j-1]+d[i-1][j-1];
 }
 return d[a][b];
}
// In odd rank, the first unmatched H maps bijectively to the next rank.
void central_check(const vector<vector<string>>&a,int n){
 if(n%2==0)return;
 int k=n/2;
 unordered_map<string,int> ids;
 ids.reserve(a[k+1].size()*1.4);
 for(int i=0;i<(int)a[k+1].size();i++) ids.emplace(a[k+1][i],i);
 vector<unsigned char> seen(a[k+1].size(),0);
 for(const auto&w:a[k]){
  vector<int> open;
  for(int j=0;j<(int)w.size();j++){
   if(w[j]=='H')open.push_back(j);
   if(w[j]=='V' && !open.empty())open.pop_back();
  }
  if(open.empty())throw runtime_error("missing unmatched H in odd middle rank");
  string q=w;q[open.front()]='V';
  auto it=ids.find(q);
  if(it==ids.end() || seen[it->second])throw runtime_error("central matching is not a bijection");
  seen[it->second]=1;
 }
 if(find(seen.begin(),seen.end(),0)!=seen.end())throw runtime_error("central matching not surjective");
 cout<<"CENTRAL "<<n<<" "<<a[k].size()<<" MATCHED\n"<<flush;
}
void test(int n){
 vector<vector<string>> a(n+1);string s;generate(n,s,a);cerr<<"N "<<n<<" total ";long long total=0;for(auto &x:a) total+=x.size();cerr<<total<<"\n";
 for(int k=0;k<=n;k++){
  if((long long)a[k].size()!=delannoy(n-k,k))
   throw runtime_error("rank size mismatch with independent Delannoy recurrence");
 }
 for(int k=0;k<n/2;k++){
  int L=a[k].size(),R=a[k+1].size();unordered_map<string,int> ids;ids.reserve(R*1.4);
  for(int i=0;i<R;i++)ids.emplace(a[k+1][i],i);
  int S=L+R,T=S+1;Dinic g(T+1,(L*9+L+R)*2);
  for(int i=0;i<L;i++){
   g.add(S,i,R); auto &w=a[k][i];string q;
   for(int j=0;j<(int)w.size();j++){
    if(w[j]=='H'){q=w;q[j]='V';auto it=ids.find(q);if(it==ids.end())throw runtime_error("missing H V");g.add(i,L+it->second,R);}
    if(w[j]=='D'){q=w.substr(0,j)+"VV"+w.substr(j+1);auto it=ids.find(q);if(it==ids.end())throw runtime_error("missing D VV");g.add(i,L+it->second,R);}
    if(j+1<(int)w.size() && w[j]=='H'&&w[j+1]=='H'){q=w.substr(0,j)+"D"+w.substr(j+2);auto it=ids.find(q);if(it==ids.end())throw runtime_error("missing HH D");g.add(i,L+it->second,R);}
   }
  }
  for(int j=0;j<R;j++)g.add(L+j,T,L);
  long long fl=g.flow(S,T);cout<<n<<" "<<k<<" "<<L<<" "<<R<<" "<<fl<<" "<<1LL*L*R<<"\n"<<flush;
  if(fl!=1LL*L*R)throw runtime_error("normalized matching violated");
 }
 central_check(a,n);
}
int main(int argc,char**argv){
 try {
  int low=argc>1?atoi(argv[1]):0,hi=argc>2?atoi(argv[2]):18;
  if(low<0 || hi<low || hi>18)throw runtime_error("range must be within 0..18");
  for(int n=low;n<=hi;n++)test(n);
  cout<<"VERIFY_OK 0_to_"<<hi<<"\n";
 }catch(const exception&e){cerr<<"VERIFY_FAILED: "<<e.what()<<"\n";return 1;}
 return 0;
}
