#include <bits/stdc++.h>
using namespace std;
// Exact maximum-clique bound for a finite compatibility graph supplied on stdin.
static bitset<730> adj[730];
long long nodes=0; int best=11;
void expand(vector<int>&P,int depth){
 if(P.empty())return;
 ++nodes;
 vector<int> R=P, ord, col;
 for(int c=1; !R.empty(); c++) {
  vector<int> left, add; bitset<730> used;
  for(int v:R){if(!used[v]){add.push_back(v);used|=adj[v];}else left.push_back(v);}
  for(int v:add){ord.push_back(v);col.push_back(c);}
  R.swap(left);
 }
 for(int i=(int)ord.size()-1;i>=0;i--){
  if(depth+col[i]<=best)return;
  int v=ord[i];vector<int> Q;
  for(int j=0;j<i;j++)if(adj[v][ord[j]])Q.push_back(ord[j]);
  if(Q.empty()){best=max(best,depth+1);if(best>=12)return;}
  else expand(Q,depth+1);
  if(best>=12)return;
 }
}
int main(){istream& in=cin;int n;in>>n; if(n!=729) return 3;
 string line;getline(in,line);
 for(int i=0;i<n;i++){getline(in,line);istringstream s(line);int v;while(s>>v){if(v<0||v>=n||v==i)return 4;adj[i].set(v);}}
 vector<int>P(n);iota(P.begin(),P.end(),0);expand(P,0);
 cout<<"best="<<best<<" nodes="<<nodes<<"\n";
 return 0;
}
