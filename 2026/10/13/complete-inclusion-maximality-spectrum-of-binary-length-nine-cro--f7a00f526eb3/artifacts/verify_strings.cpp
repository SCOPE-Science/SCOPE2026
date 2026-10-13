// Compile: c++ -std=c++17 -O2 verify_strings.cpp -o verify_strings
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
const int N = 9;
vector<string> word;
vector<set<int>> neigh;
map<int,long long> hist;
vector<vector<string>> catalog;

bool can_pair(const string& a,const string& b) {
  for(int k=1;k<N;k++){
    if(a.substr(0,k)==b.substr(N-k,k) || b.substr(0,k)==a.substr(N-k,k))return false;
  }
  return true;
}
void visit(const vector<int>& R){
  vector<string> c;set<int> inside(R.begin(),R.end());
  for(int i:R) c.push_back(word[i]);
  sort(c.begin(),c.end());
  for(int j=0;j<(int)R.size();j++)for(int k=0;k<j;k++)assert(can_pair(word[R[j]],word[R[k]]));
  for(int i=0;i<(int)word.size();i++)if(!inside.count(i)){
    bool can=true;for(int j:R)if(!can_pair(word[i],word[j])){can=false;break;}
    assert(!can);
  }
  hist[R.size()]++;
  catalog.push_back(move(c));
}
// Independent representation: actual bit strings and ordinary set intersection.
void bron(set<int> P,set<int> X,vector<int> R){
  if(P.empty()&&X.empty()){visit(R);return;}
  int pivot=-1,best=-1;
  set<int> unionPX=P; unionPX.insert(X.begin(),X.end());
  for(int u:unionPX){
    int score=0;
    for(int v:P)if(neigh[u].count(v))score++;
    if(score>best){best=score;pivot=u;}
  }
  set<int> choices=P;
  if(pivot!=-1)for(int v:neigh[pivot])choices.erase(v);
  for(int v:choices){
    set<int> nextP,nextX;
    set_intersection(P.begin(),P.end(),neigh[v].begin(),neigh[v].end(),inserter(nextP,nextP.begin()));
    set_intersection(X.begin(),X.end(),neigh[v].begin(),neigh[v].end(),inserter(nextX,nextX.begin()));
    auto nextR=R;nextR.push_back(v);
    bron(move(nextP),move(nextX),move(nextR));
    P.erase(v);X.insert(v);
  }
}
int main(int argc,char**argv){
  for(int x=0;x<(1<<N);x++){
    string s(N,'0');for(int i=0;i<N;i++)s[N-1-i]=char('0'+((x>>i)&1));
    if(can_pair(s,s)) word.push_back(s);
  }
  neigh.resize(word.size());int edges=0;
  for(int i=0;i<(int)word.size();i++)for(int j=0;j<i;j++){
    if(can_pair(word[i],word[j])){neigh[i].insert(j);neigh[j].insert(i);edges++;}
  }
  set<int> P;for(int i=0;i<(int)word.size();i++)P.insert(i);
  bron(P,{},{});
  sort(catalog.begin(),catalog.end());
  assert(adjacent_find(catalog.begin(),catalog.end())==catalog.end());
  assert(catalog.size()==62280);
  cout<<"unbordered "<<word.size()<<" edges "<<edges<<"\n";
  cout<<"histogram ";for(auto [n,c]:hist) cout<<n<<":"<<c<<" "; cout<<"\n";
  if(argc>1&&string(argv[1])=="--catalog"){
    ofstream f("catalog_cpp.txt");
    for(auto&c:catalog){for(size_t i=0;i<c.size();i++){if(i)f<<" ";f<<c[i];}f<<"\n";}
  }
  cout<<"PASS\n";
}
