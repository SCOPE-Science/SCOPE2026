#include<bits/stdc++.h>
using namespace std;
int rot(int x,int n,int k){int m=(1<<n)-1;return ((x<<k)|(x>>(n-k)))&m;}
int reverse6(int x){int y=0;for(int i=0;i<6;i++)y=(y<<1)|((x>>i)&1);return y;}
int main(){const int n=6; vector<vector<int>> orbit;vector<int> seen(64,0),class_of(64,-1), words;
 for(int x=0;x<64;x++){int p=6;for(int k=1;k<6;k++)if(rot(x,6,k)==x){p=k;break;}if(p!=6||seen[x])continue;vector<int> v;for(int k=0;k<6;k++){int y=rot(x,6,k);v.push_back(y);seen[y]=1;class_of[y]=orbit.size();}orbit.push_back(v);}
 cerr<<"num necklaces "<<orbit.size()<<"\n";for(int i=0;i<(int)orbit.size();i++){cerr<<i<<":";for(auto x:orbit[i])cerr<<" "<<bitset<6>(x);cerr<<"\n";}
 // word packing condition: for all a,b,c codewords, concat a b shifted by k != c
 int ov[64][64][6];for(int a=0;a<64;a++)for(int b=0;b<64;b++)for(int k=1;k<6;k++){ov[a][b][k]=((a<<6)|b)>>(6-k)&63;}
 long long ans=0,visits=0;int choose[9]; vector<array<int,9>> examples;
 auto addok=[&](int depth,int cand){
  int c[9];for(int i=0;i<depth;i++)c[i]=choose[i];c[depth]=cand;
  for(int i=0;i<=depth;i++)for(int j=0;j<=depth;j++)for(int k=1;k<6;k++){
    int v=ov[c[i]][c[j]][k];for(int z=0;z<=depth;z++)if(c[z]==v)return false;
  }
  return true;
 };
 function<void(int)> rec=[&](int d){if(d==(int)orbit.size()){ans++;if(examples.size()<30){array<int,9> a;copy(choose,choose+9,a.begin());examples.push_back(a);}return;}
  for(int w:orbit[d]){visits++;if(addok(d,w)){choose[d]=w;rec(d+1);}}
 };
 rec(0);
 cout<<"COUNT "<<ans<<" VISITS "<<visits<<"\n";
 for(auto& e:examples){for(auto x:e)cout<<bitset<6>(x)<<" ";cout<<"\n";}
 // Independent Hamming-two variant: include-or-skip branching and full triple testing.
 long long by_size[10]={}; long long visits_h=0;
 function<void(int,int)> dfs=[&](int depth,int count){
  if(depth==(int)orbit.size()){by_size[count]++;return;}
  dfs(depth+1,count);
  for(int w:orbit[depth]){
   visits_h++;
   bool good=true;
   for(int i=0;i<count;i++) if(__builtin_popcount((unsigned)(w^choose[i]))<2){good=false;break;}
   if(!good)continue;
   // Test all possible (a,b,c) triples with the new word in the set.
   int a[9];for(int i=0;i<count;i++)a[i]=choose[i];a[count]=w;
   for(int i=0;i<=count&&good;i++)for(int j=0;j<=count&&good;j++)for(int k=1;k<6&&good;k++){
    int v=ov[a[i]][a[j]][k];
    for(int z=0;z<=count;z++)if(a[z]==v){good=false;break;}
   }
   if(good){choose[count]=w;dfs(depth+1,count+1);}
  }
 };
 dfs(0,0);
 cout<<"DISTANCE2 ";for(int j=0;j<10;j++)cout<<j<<":"<<by_size[j]<<" ";cout<<"VISITS "<<visits_h<<"\n";

}
