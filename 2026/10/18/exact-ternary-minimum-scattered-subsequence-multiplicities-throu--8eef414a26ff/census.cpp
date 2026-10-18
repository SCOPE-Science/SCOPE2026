// Exact exhaustive ternary scattered-subsequence frequency census.
// Counts subsequences by a base-four encoding of their symbols.
// The first-occurrence canonicalization covers all ternary words modulo alphabet relabeling.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
using P=pair<U,uint32_t>;
const int MAXN=16;
uint64_t counts[20]={}, nodes[20]={}, best[20];
string reps[20];uint64_t minnum[20]={};
vector<string> allmin[20];
vector<P> grow(const vector<P>& v,int sym){
  vector<P> out;out.reserve(v.size()*2+1);
  size_t i=0,j=0; size_t N=v.size();
  while(i<N || j<=N){
    U a=i<N?v[i].first:UINT64_MAX;
    U b=j==0?(U)sym:(j<=N ? v[j-1].first*4+(U)sym:UINT64_MAX);
    if (a<b){out.push_back(v[i++]);}
    else if(b<a){out.push_back({b,j==0?1:v[j-1].second});j++;}
    else{out.push_back({a,(uint32_t)(v[i].second+(j==0?1:v[j-1].second))});i++;j++;}
  }
  return out;
}
void dfs(int n,int maxsymbol, const vector<P>& v,string& word){
  if(n){
    nodes[n]++;uint32_t val=1;for(auto &p:v)val=max(val,p.second);
    if(val<best[n]){best[n]=val;minnum[n]=1;reps[n]=word;allmin[n].clear();allmin[n].push_back(word);}
    else if(val==best[n]){minnum[n]++;if(allmin[n].size()<10000)allmin[n].push_back(word);}
  }
  if(n==MAXN) return;
  for(int a=1;a<=min(3,maxsymbol+1);a++){
    auto w=grow(v,a);word+=char('0'+a-1);dfs(n+1,max(maxsymbol,a),w,word);word.pop_back();
  }
}

const uint64_t EXPECT_MIN[] = {0,1,1,1,2,2,2,3,5,6,8,9,15,18,24,33,46};
const uint64_t EXPECT_COUNT[] = {0,1,1,1,7,5,1,2,10,26,12,1,9,10,1,1,4};
const uint64_t EXPECT_NODES[] = {0,1,2,5,14,41,122,365,1094,3281,9842,29525,88574,265721,797162,2391485,7174454};

int main(){fill(begin(best),end(best),UINT64_MAX);string w;vector<P> v;dfs(0,0,v,w);
for(int n=1;n<=MAXN;n++){
 if(best[n]!=EXPECT_MIN[n] || minnum[n]!=EXPECT_COUNT[n] || nodes[n]!=EXPECT_NODES[n]) { cerr << "CENSUS_MISMATCH n="<<n<<"\n"; return 1; }
 cout<<n<<" "<<best[n]<<" "<<nodes[n]<<" "<<minnum[n]<<" "<<reps[n];
 cout<<" all=";for(auto &s:allmin[n])cout<<s<<",";
 cout<<"\n";
}
cout<<"CENSUS_VERIFY_OK range=1.."<<MAXN<<"\n";
}
