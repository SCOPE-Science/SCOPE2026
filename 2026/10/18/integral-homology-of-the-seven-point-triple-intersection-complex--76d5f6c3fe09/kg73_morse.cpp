#include <bits/stdc++.h>
using namespace std;using ull=uint64_t;
int main(int argc,char**argv){
 bool reverse_order=(argc>1 && string(argv[1])=="reverse");
 vector<int> tr;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)tr.push_back((1<<i)|(1<<j)|(1<<k));
 ull forb[35]={};for(int i=0;i<35;i++)for(int j=0;j<35;j++)if(!(tr[i]&tr[j]))forb[i]|=1ULL<<j;
 vector<ull> all;all.reserve(1300000);
 auto rec=[&](auto&&self,int i,ull s)->void{all.push_back(s);for(int j=i;j<35;j++)if(!(forb[j]&s))self(self,j+1,s|(1ULL<<j));};rec(rec,0,0);
 cerr<<"Enumerated "<<all.size()<<" simplices\n";
 unordered_map<ull,int> id;id.reserve(all.size()*2);for(int i=0;i<(int)all.size();i++)id[all[i]]=i;
 vector<int> mate(all.size(),-1);int pairs=0;
 for(int t=0;t<35;t++)for(int i=0;i<(int)all.size();i++){
  int v=reverse_order?34-t:t;
  ull s=all[i];if(mate[i]!=-1||(s>>v&1)||(s&forb[v]))continue;
  auto jt=id.find(s|1ULL<<v);if(jt!=id.end()&&mate[jt->second]==-1){mate[i]=jt->second;mate[jt->second]=i;pairs++;}
 }

 // Verify all gradient V-paths, not merely those encountered in boundary projection.
 vector<uint8_t> islower(all.size(),0);
 vector<int> lower; lower.reserve(pairs);
 for(int i=0;i<(int)all.size();i++)if(mate[i]>=0 && __builtin_popcountll(all[i]) < __builtin_popcountll(all[mate[i]])){
  islower[i]=1;lower.push_back(i);
 }
 vector<int> indeg(all.size(),0);long long arcs=0;
 for(int i:lower){
   ull U=all[mate[i]], diff=U^all[i],mask=U;
   while(mask){int v=__builtin_ctzll(mask);mask&=mask-1; if((diff>>v)&1)continue;
    int j=id.at(U^(1ULL<<v));if(islower[j]){indeg[j]++;arcs++;}
   }
 }
 deque<int> zero;
 for(int i:lower)if(!indeg[i])zero.push_back(i);
 size_t visitedCount=0;
 while(!zero.empty()){
  int i=zero.front();zero.pop_front();visitedCount++;
  ull U=all[mate[i]],diff=U^all[i],mask=U;
  while(mask){int v=__builtin_ctzll(mask);mask&=mask-1;if((diff>>v)&1)continue;
   int j=id.at(U^(1ULL<<v));if(islower[j] && --indeg[j]==0)zero.push_back(j);
  }
 }
 cerr<<"V-PATH CHECK matched_lowers="<<lower.size()<<" gradient_arcs="<<arcs<<" topologically_visited="<<visitedCount<<"\n";
 if(visitedCount!=lower.size())return 9;

 map<int,long long> facevector;
 for(ull s:all)facevector[__builtin_popcountll(s)]++;
 cout << "FACEVECTOR";
 for(int k=0;k<=15;k++)cout << " " << facevector[k];
 cout << "\n";
 cout << "PAIRS " << pairs << "\n";
 cout << "GRADIENT_ARCS " << arcs << "\n";
 vector<vector<int>> crit(16);
 for(int i=0;i<(int)all.size();i++)if(mate[i]<0)crit[__builtin_popcountll(all[i])].push_back(i);

 cout << "CRITICAL";
 for(int k=0;k<16;k++)cout << " " << crit[k].size();
 cout << "\n";
 for(int i=0;i<16;i++)if(crit[i].size())cerr<<"crit size "<<i<<": "<<crit[i].size()<<"\n";
 auto signIndex=[](ull s, int v){return (__builtin_popcountll(s & ((1ULL<<v)-1))&1)?-1:1;};
 for(int n=7;n<=10;n++){
  int cols=crit[n].size(); int rows=crit[n-1].size();
  if(!rows||!cols)continue;
  unordered_map<int,int> idx;for(int i=0;i<rows;i++)idx[crit[n-1][i]]=i;
  unordered_map<int,vector<long long>> memo;memo.reserve(100000);
  unordered_map<int,char> visited;
  int calls=0;
  function<const vector<long long>&(int)> project;
  project=[&](int k)->const vector<long long>&{
   auto jt=memo.find(k);if(jt!=memo.end())return jt->second;
   if(visited[k]==1){cerr<<"CYCLE detected at "<<k<<"\n";exit(5);}visited[k]=1;calls++;
   vector<long long> res(rows,0);
   ull L=all[k];auto hit=idx.find(k);
   if(hit!=idx.end())res[hit->second]=1;
   else if(mate[k]>=0){
    int u=mate[k];ull U=all[u];
    if(__builtin_popcountll(U)==n){
     int diff=__builtin_ctzll(U^L);
     int c=signIndex(U,diff);
     ull b=U;
     while(b){int v=__builtin_ctzll(b);b&=b-1;if(v==diff)continue;
      ull S=U^(1ULL<<v);int j=id.at(S);int coeff=-c*signIndex(U,v);
      const auto &z=project(j);for(int t=0;t<rows;t++){
        long long term, updated;
        if(__builtin_mul_overflow((long long)coeff,z[t],&term) ||
           __builtin_add_overflow(res[t],term,&updated)){
          cerr << "Integer arithmetic overflow in Morse projection\n"; exit(8);
        }
        res[t]=updated;
      }
     }
    } // if mate is a lower face of k, so upper matched projects zero
   }
   visited[k]=2;
   return memo.emplace(k,move(res)).first->second;
  };
  vector<vector<long long>> matrix(rows,vector<long long>(cols));
  for(int c=0;c<cols;c++){
   ull s=all[crit[n][c]];ull a=s;
   while(a){int v=__builtin_ctzll(a);a&=a-1;auto z=project(id.at(s^(1ULL<<v)));int sg=signIndex(s,v);
    for(int r=0;r<rows;r++){
      long long term,updated;
      if(__builtin_mul_overflow((long long)sg,z[r],&term) ||
         __builtin_add_overflow(matrix[r][c],term,&updated)){
        cerr << "Integer arithmetic overflow in boundary calculation\n"; exit(8);
      }
      matrix[r][c]=updated;
    }
   }
  }
  cerr<<"matrix d_"<<n-1<<" dimension "<<rows<<"x"<<cols<<" memo "<<memo.size()<<" calls "<<calls<<"\n";
  cout << "MATRIX " << n-1 << " " << rows << " " << cols << "\n";
  for(int r=0;r<rows;r++){for(int c=0;c<cols;c++)cout<<matrix[r][c]<<(c+1==cols?'\n':' ');}
  long long maxe=0;int nonzero=0;for(auto&row:matrix)for(auto z:row){maxe=max(maxe,abs(z));nonzero+=(z!=0);}
  cerr<<"max coeff "<<maxe<<" nonzero "<<nonzero<<"\n";
 }
 cout<<"FINISHED\n";
}
