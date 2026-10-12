#include <bits/stdc++.h>
using namespace std;
vector<unsigned> m;vector<int> ids[27];unordered_set<uint64_t> seen;unsigned full=(1u<<27)-1;long long nodes=0;bool found=false;
bool dfs(unsigned uncovered,int left){
 ++nodes;
 if(!uncovered)return true;
 if(left<=0||__builtin_popcount(uncovered)>4*left)return false;
 uint64_t key=((uint64_t)uncovered<<4)|left;
 if(!seen.insert(key).second)return false;
 int target=-1,minc=100000;vector<int> choices;
 for(unsigned tmp=uncovered;tmp;tmp&=tmp-1){int t=__builtin_ctz(tmp);int cnt=0;for(int j:ids[t]){
  int hits=__builtin_popcount(m[j]&uncovered);
  if(hits>=max(1,__builtin_popcount(uncovered)-4*(left-1)))++cnt;
 }
 if(cnt<minc){minc=cnt;target=t;if(cnt==0)return false;}
 }
 for(int j:ids[target])if(__builtin_popcount(m[j]&uncovered)>=max(1,__builtin_popcount(uncovered)-4*(left-1)))choices.push_back(j);
 sort(choices.begin(),choices.end(),[&](int a,int b){return __builtin_popcount(m[a]&uncovered)>__builtin_popcount(m[b]&uncovered);});
 for(int j:choices)if(dfs(uncovered&~m[j],left-1))return true;
 return false;
}
int main(){for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)for(int d=0;d<3;d++)for(int e=0;e<3;e++){
 int x[5]={a,b,c,d,e};unsigned bits=0;
 for(int i=0;i<4;i++){int t=0;for(int j=0;j<5;j++)if(j!=i&&j!=i+1)t=3*t+x[j];bits|=1u<<t;}
 int id=m.size();m.push_back(bits);for(int t=0;t<27;t++)if(bits>>t&1)ids[t].push_back(id);
 }
 auto tic=chrono::steady_clock::now();bool f=dfs(full,7);auto dur=chrono::duration<double>(chrono::steady_clock::now()-tic).count();cout<<"SEVEN_WORD_COVER_EXISTS? "<<f<<" NODES "<<nodes<<" STATES "<<seen.size()<<" SEC "<<dur<<"\n";return f?1:0;}
