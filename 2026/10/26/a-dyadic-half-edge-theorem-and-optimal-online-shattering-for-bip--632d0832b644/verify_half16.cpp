#include <bits/stdc++.h>
using namespace std;
long long examined=0, edgepass=0, impossible=0; vector<int> rm,cm,choices[7],rows; bool counter=false;
int nrows,ncols;
int choose_mask(int mask){return __builtin_popcount((unsigned)mask);}
bool has8(){
  for(int A=1; A<(1<<nrows);A++){
    int can=1;
    for(int j=0;j<ncols;j++){
      int w=0;
      for(int i=0;i<nrows;i++)if((A>>i&1)&&(rows[i]>>j&1))w++;
      can |= can<<w;
      if(can & (1<<8)) return true;
    }
  }
  return false;
}
void dfs(int i, vector<int>&colLeft){
 if(counter)return;
 if(i==nrows){
    for(int v:colLeft)if(v)return;
    edgepass++;
    if(!has8()){
      cerr<<"COUNTER ";for(int r:rows)cerr<<r<<" ";cerr<<"\n";counter=true;impossible++;
    }
    return;
 }
 for(int mask:choices[i]){
    bool ok=true;
    for(int j=0;j<ncols;j++) if((mask>>j&1) && colLeft[j]==0){ok=false;break;}
    if(!ok)continue;
    for(int j=0;j<ncols;j++)if(mask>>j&1)colLeft[j]--;
    int remainRows=nrows-i-1;
    for(int j=0;j<ncols;j++)if(colLeft[j]>remainRows)ok=false;
    if(ok){rows[i]=mask;dfs(i+1,colLeft);}
    for(int j=0;j<ncols;j++)if(mask>>j&1)colLeft[j]++;
    if(counter)return;
 }
}
void run(vector<int> r, vector<int> c){
 rm=r;cm=c;nrows=r.size();ncols=c.size();rows.assign(nrows,0);
 for(int i=0;i<nrows;i++){
  choices[i].clear();for(int a=0;a<(1<<ncols);a++)if(choose_mask(a)==r[i])choices[i].push_back(a);
 }
 long long before=edgepass;
 auto colLeft=c;dfs(0,colLeft);
 cout<<"degrees ";for(int x:r)cout<<x<<",";cout<<" vs ";for(int x:c)cout<<x<<",";cout<<" matrices "<<(edgepass-before)<<" counter "<<counter<<"\n";
}
int main(){
 vector<int> P={4,3,3,3,3},Q={3,3,3,3,3,1};
 run(P,P);if(counter)return 1;
 run(P,Q);if(counter)return 1;
 run(Q,P);if(counter)return 1;
 run(Q,Q);if(counter)return 1;
 cout<<"TOTAL_CASES "<<edgepass<<" ALL_HALF_EIGHT\n";
}
