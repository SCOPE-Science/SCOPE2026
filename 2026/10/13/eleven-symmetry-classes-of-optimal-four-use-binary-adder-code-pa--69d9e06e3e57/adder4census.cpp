#include <bits/stdc++.h>
using namespace std;
const int N=16; int dif[16][16];
int main(){
 for(int a=0;a<N;a++)for(int b=0;b<N;b++){int k=0,scale=1;for(int j=0;j<4;j++){k+=((((a>>j)&1)-((b>>j)&1))+1)*scale;scale*=3;}dif[a][b]=k;}
 vector<pair<int,int>> rooted;
 for(int A=1;A<(1<<N);A+=2){int k=__builtin_popcount((unsigned)A); if(36%k)continue;int target=36/k;if(target>16)continue;
 bitset<81> ds;for(int a=0;a<N;a++)if(A>>a&1)for(int b=0;b<N;b++)if((A>>b&1)&&a!=b)ds.set(dif[a][b]);
 int cf[N]={};for(int a=0;a<N;a++)for(int b=0;b<N;b++)if(a!=b&&ds[dif[a][b]])cf[a]|=1<<b;
 for(int B=1;B<(1<<N);B++)if(__builtin_popcount((unsigned)B)==target){bool good=1;for(int b=0;b<N;b++)if(B>>b&1)if(cf[b]&B){good=0;break;}if(good)rooted.emplace_back(A,B);}
 }
 cout<<"rooted ordered pairs "<<rooted.size()<<"\n";map<pair<int,int>,int> siz;for(auto &[a,b]:rooted)siz[{__builtin_popcount((unsigned)a),__builtin_popcount((unsigned)b)}]++;for(auto [p,c]:siz)cout<<p.first<<"x"<<p.second<<":"<<c<<"\n";
 ofstream out("adder4_root_pairs.txt");for(auto &[a,b]:rooted)out<<a<<" "<<b<<"\n";
}
