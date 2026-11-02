#include <bits/stdc++.h>
using namespace std;
static unordered_map<string,int> pool[4];
static int nxt[4]={0,0,0,0};
struct Type {
 int n; vector<vector<uint8_t>> adj; vector<int> memo[4];
 Type(vector<int> lens){ n=accumulate(lens.begin(),lens.end(),0);adj.assign(n,vector<uint8_t>(n));int st=0;for(auto a:lens){for(int i=st;i<st+a-1;i++)adj[i][i+1]=adj[i+1][i]=1;st+=a;}
 for(int k=1;k<=3;k++){long long sz=1;for(int i=0;i<k;i++)sz*=n;memo[k].assign(sz,-1);}}
 int atom(vector<int>&t){int z=0,j=0;for(int i=0;i<(int)t.size();i++)for(int h=i+1;h<(int)t.size();h++){int a=t[i],b=t[h];int v=a==b?0:(adj[a][b]?1:2);z+=v<<(2*j++);}return z;}
 int typ(vector<int>&t){int k=t.size();if(k==4)return atom(t);int idx=0;for(auto v:t)idx=idx*n+v;if(k && memo[k][idx]>=0)return memo[k][idx];
 vector<int> child;child.reserve(n);for(int v=0;v<n;v++){t.push_back(v);child.push_back(typ(t));t.pop_back();}sort(child.begin(),child.end());child.erase(unique(child.begin(),child.end()),child.end());
 string key;key.reserve(4+4*child.size());int a=atom(t);for(int sh=0;sh<4;sh++)key.push_back(char((a>>(8*sh))&255));for(int x:child)for(int sh=0;sh<4;sh++)key.push_back(char((x>>(8*sh))&255));
 auto &mp=pool[k];auto it=mp.find(key);int id;
 if(it==mp.end()){id=++nxt[k];mp.emplace(move(key),id);}else id=it->second;
 if(k)memo[k][idx]=id;return id;}
 int run(){vector<int> t;return typ(t);}
};
void partitions(int sum, int minp, vector<int>&cur,vector<vector<int>>&out){if(sum==0){if(cur.size()>1)out.push_back(cur);return;}for(int j=minp;j<=sum;j++){cur.push_back(j);partitions(sum-j,j,cur,out);cur.pop_back();}}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):20;vector<pair<int,vector<int>>> path;
 for(int n=2;n<=max(N,35);n++){Type t({n});int c=t.run();path.push_back({c,{n}});cerr<<"PATH "<<n<<" class="<<c<<" pools="<<nxt[1]<<","<<nxt[2]<<","<<nxt[3]<<"\n";}
 for(int n=4;n<=N;n++){vector<vector<int>> ps;vector<int> cur;partitions(n,2,cur,ps);int matches=0;for(auto p:ps){Type t(p);int c=t.run();vector<int> matching;for(auto &[type,lens]:path)if(type==c)matching.push_back(lens[0]);if(!matching.empty()){cout<<"MATCH forest=";for(int a:p)cout<<a<<"+";cout<<" total="<<n<<" path=";for(int x:matching)cout<<x<<",";cout<<"\n";matches++;}}cerr<<"TOTAL "<<n<<" forests="<<ps.size()<<" matches="<<matches<<" pools="<<nxt[1]<<","<<nxt[2]<<","<<nxt[3]<<"\n";}
}
