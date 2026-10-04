#include <bits/stdc++.h>
using namespace std;
struct Solver{
 int n,m; unordered_map<unsigned long long,char> memo;
 unsigned long long key(vector<pair<int,int>> p,int rem){
   sort(p.begin(),p.end()); unsigned long long k=rem | ((unsigned long long)p.size()<<3); int sh=6;
   for(auto [a,b]:p){k|=(unsigned long long)a<<sh; sh+=5; k|=(unsigned long long)b<<sh; sh+=5;} return k;
 }
 bool iso(const vector<pair<int,int>>& p){for(auto [a,b]:p) for(auto [c,d]:p){if((a==c)!=(b==d)) return false; if((c==a+1)!=(d==b+1)) return false;} return true;}
 bool rec(vector<pair<int,int>> p,int rem){
   if(!iso(p))return false; if(rem==0)return true; auto K=key(p,rem); auto it=memo.find(K); if(it!=memo.end())return it->second;
   vector<char> ua(n),ub(m); for(auto [a,b]:p){ua[a]=1;ub[b]=1;}
   for(int side=0;side<2;side++){int N=side?m:n,M=side?n:m; auto &uN=side?ub:ua; auto &uM=side?ua:ub;
     for(int x=0;x<N;x++) if(!uN[x]){bool ok=false; for(int y=0;y<M;y++) if(!uM[y]){auto q=p; if(!side) q.push_back({x,y}); else q.push_back({y,x}); if(rec(q,rem-1)){ok=true;break;}} if(!ok){memo[K]=0;return false;}}
   }
   memo[K]=1; return true;
 }
};
bool theorem(int n,int m,int q){ if(q<=1) return true; int T=1<<q; return n==m || (n>=T && m>=T); }
int main(){
 long long cases=0,states=0; string boundary="unknown";
 for(int q=1;q<=4;q++) for(int n=1;n<=17;n++) for(int m=n;m<=17;m++){
   Solver s{n,m}; bool got=s.rec({},q), exp=theorem(n,m,q); states+=s.memo.size(); cases++;
   if(got!=exp){cout<<"VERIFY_FAIL q="<<q<<" n="<<n<<" m="<<m<<" got="<<got<<" expected="<<exp<<"\n"; return 1;}
   if(q==3 && n==7 && m==8) boundary=got?"duplicator":"spoiler";
 }
 cout<<"VERIFY_OK cases="<<cases<<" states="<<states<<" boundary_7_8="<<boundary<<"\n";
}
