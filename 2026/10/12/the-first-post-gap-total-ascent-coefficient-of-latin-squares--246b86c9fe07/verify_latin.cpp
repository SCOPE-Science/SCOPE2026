#include <bits/stdc++.h>
using namespace std;
long long countLatin(int n, bool verbose) {
 vector<vector<int>> ps; vector<int> p(n); iota(p.begin(),p.end(),0);
 do { ps.push_back(p); } while(next_permutation(p.begin(),p.end()));
 vector<vector<int>> asc(ps.size(), vector<int>(ps.size(),0));
 vector<vector<bool>> disj(ps.size(), vector<bool>(ps.size(),false));
 for(size_t i=0;i<ps.size();i++) for(size_t j=0;j<ps.size();j++){
  bool ok=true; int a=0;
  for(int z=0;z<n;z++){if(ps[i][z]==ps[j][z])ok=false;if(ps[i][z]<ps[j][z])a++;}
  asc[i][j]=a;disj[i][j]=ok;
 }
 vector<int> colmask(n,0);for(int z=0;z<n;z++)colmask[z]=1<<z;
 unsigned long long leaves=0;long long answer=0; vector<int> rows{0};
 function<void(int,int)> dfs=[&](int d,int excess){
  if(d==n){leaves++; if(excess==2){answer++;if(verbose && answer<=3){cerr<<"example ";for(int k:rows) cerr<<k<<' ';cerr<<'\n';}}return;}
  for(int j=1;j<(int)ps.size();j++){
   int a=asc[rows.back()][j]; int e=a-1;
   if(e<0 || excess+e>2 || a==0) continue;
   bool valid=true;for(int z=0;z<n;z++){if(colmask[z]&(1<<ps[j][z])){valid=false;break;}}
   if(!valid)continue;
   for(int z=0;z<n;z++)colmask[z] |= 1<<ps[j][z];rows.push_back(j);
   dfs(d+1,excess+e);
   rows.pop_back();for(int z=0;z<n;z++)colmask[z] ^= 1<<ps[j][z];
  }
 };
 dfs(1,0);
 cout<<"n="<<n<<" normalized_count="<<answer<<" completed_leaves="<<leaves<<"\n";
 return answer;
}
int main(){for(int n=3;n<=6;n++)countLatin(n,true);}
