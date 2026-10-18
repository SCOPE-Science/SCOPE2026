// Exact finite simplicial computation for the domination complex D_{7,3}.
// Requires only C++17; compile g++ -std=c++17 -O2 d73_verify.cpp -o d73_verify
#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 bool reverse=(argc>=2 && string(argv[1])=="--reverse");
 constexpr int n=7, m=21;
 int edge[7][7];vector<pair<int,int>> e;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){edge[i][j]=edge[j][i]=e.size();e.emplace_back(i,j);}
 vector<array<uint32_t,5>> test;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
    array<uint32_t,5> a{};int q=0;
    for(int k=0;k<n;k++)if(k!=i && k!=j) a[q++]=(1u<<edge[i][k])|(1u<<edge[j][k]);
    test.push_back(a);
 }
 vector<uint32_t> faces;vector<uint32_t> fcount(22);faces.reserve(300000);
 for(uint32_t mask=0;mask<(1u<<m);mask++){
   bool valid=true;
   for(const auto &row:test){bool dominates=true;
     for(auto k:row)if(!(mask&k)){dominates=false;break;}
     if(dominates){valid=false;break;}
   }
   if(valid){faces.push_back(mask);fcount[__builtin_popcount(mask)]++;}
 }
 if(faces.size()!=287277 || fcount[0]!=1) throw runtime_error("face enumeration discrepancy");
 unordered_map<uint32_t,int> idx;idx.reserve(faces.size()*2);
 for(int i=0;i<(int)faces.size();i++)idx.emplace(faces[i],i);
 vector<int> mate(faces.size(),-1); // index of other face in each matched pair
 vector<char> alive(faces.size(),true);alive[0]=false;
 for(int it=0;it<m;it++){int b=reverse?(m-1-it):it;
   auto bit=1u<<b;
   for(int u=1;u<(int)faces.size();u++){
     auto x=faces[u];if((x&bit)||!alive[u])continue;
     auto it=idx.find(x|bit);
     if(it!=idx.end() && alive[it->second]){
       int v=it->second; mate[u]=v;mate[v]=u;alive[u]=false;alive[v]=false;
     }
   }
 }
 vector<vector<int>> critical(22);vector<vector<int>> level(22);
 for(int u=1;u<(int)faces.size();u++){
   int k=__builtin_popcount(faces[u]);level[k].push_back(u);
   if(alive[u])critical[k].push_back(u);
 }
 vector<int> critical_expected(22); critical_expected[1]=1;critical_expected[7]=reverse?161:162;
 critical_expected[8]=reverse?760:941;critical_expected[9]=reverse?85:269;critical_expected[10]=reverse?37:41;
 for(int k=1;k<=m;k++)if((int)critical[k].size()!=critical_expected[k])throw runtime_error("critical faces discrepancy");
 // Verify the matching's entire oriented Hasse graph, not only its critical counts.
 vector<int> indeg(faces.size());size_t oriented_edges=0;
 for(int u=1;u<(int)faces.size();u++){
   auto x=faces[u];for(uint32_t s=x;s;s&=s-1){uint32_t y=x^(s&-s);if(y==0)continue;
     int v=idx.at(y);
     if(mate[u]==v)indeg[u]++;else indeg[v]++;oriented_edges++;
   }
 }
 queue<int> qu;for(int u=1;u<(int)faces.size();u++)if(!indeg[u])qu.push(u);
 size_t visited=0;
 while(!qu.empty()){
   int u=qu.front();qu.pop();visited++;
   auto x=faces[u];
   for(uint32_t s=x;s;s&=s-1){uint32_t y=x^(s&-s);if(y==0)continue;int v=idx.at(y);
      if(mate[u]!=v && --indeg[v]==0)qu.push(v);
   }
   if(mate[u]>=0 && __builtin_popcount(faces[mate[u]])==__builtin_popcount(x)+1){
     int v=mate[u];if(--indeg[v]==0)qu.push(v);
   }
 }
 if(visited!=faces.size()-1) throw runtime_error("matching not acyclic");
 cout<<"ORDER "<<(reverse?"reverse":"forward")<<"\n";
 cout<<"FACES ";for(int k=0;k<=m;k++)if(fcount[k])cout<<k<<":"<<fcount[k]<<" ";cout<<"\n";
 cout<<"CRITICAL ";for(int k=1;k<=m;k++)if(!critical[k].empty())cout<<k-1<<":"<<critical[k].size()<<" ";cout<<"\n";
 cout<<"HASSE_VERTICES "<<visited<<" HASSE_ARCS "<<oriented_edges<<"\n";
 // Compute chain projection to critical generators over F_2 by solving matched-cell boundary relations.
 vector<int> ranks(22);
 for(int d=7;d<=10;d++){
   int k=d-1;int sz=critical[k].size();int words=(sz+63)/64;
   vector<int> ord(faces.size(),-1);for(int i=0;i<sz;i++)ord[critical[k][i]]=i;
   vector<char> state(faces.size(),0);
   // values for each face in degree k-1 (number of edges k)
   vector<vector<uint64_t>> P(faces.size());
   function<const vector<uint64_t>&(int)> expand=[&](int u)->const vector<uint64_t>&{
     if(state[u]==2)return P[u];
     if(state[u]==1)throw runtime_error("gradient recurrence cyclic");
     state[u]=1;P[u].assign(words,0);
     if(ord[u]>=0)P[u][ord[u]/64]^=1ull<<(ord[u]%64);
     else if(mate[u]>=0 && __builtin_popcount(faces[mate[u]])==k+1){
       int top=mate[u];uint32_t X=faces[top];
       for(uint32_t s=X;s;s&=s-1){uint32_t sub=X^(s&-s);int v=idx.at(sub);
         if(v==u)continue;
         const auto &r=expand(v);for(int z=0;z<words;z++)P[u][z]^=r[z];
       }
     }
     state[u]=2;return P[u];
   };
   vector<vector<uint64_t>> piv(sz);vector<char> taken(sz,0);int rank=0;
   for(int u:critical[d]){
     vector<uint64_t> row(words,0);uint32_t X=faces[u];
     for(uint32_t s=X;s;s&=s-1){int v=idx.at(X^(s&-s));auto &a=expand(v);
       for(int z=0;z<words;z++)row[z]^=a[z];
     }
     for(;;){int bit=-1;
       for(int j=words-1;j>=0;j--)if(row[j]){bit=j*64+63-__builtin_clzll(row[j]);break;}
       if(bit<0)break;
       if(!taken[bit]){piv[bit]=std::move(row);taken[bit]=1;rank++;break;}
       for(int j=0;j<words;j++)row[j]^=piv[bit][j];
     }
   }
   ranks[d]=rank;cout<<"MORSE_BOUNDARY_RANK_MOD2 d="<<d-1<<" to="<<d-2<<" rank="<<rank<<"\n";
 }
 vector<int> expectedBetti{106,623,1,35};
 for(int d=7;d<=10;d++){
   int betti=critical[d].size()-ranks[d]-ranks[d+1];
   if(betti!=expectedBetti[d-7])throw runtime_error("homology discrepancy");
   cout<<"BETTI_MOD2 degree="<<d-1<<" value="<<betti<<"\n";
 }
 cout<<"VERIFY_OK\n";
}
