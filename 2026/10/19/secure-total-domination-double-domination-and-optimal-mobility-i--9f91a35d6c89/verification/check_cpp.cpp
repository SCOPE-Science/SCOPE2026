// Independent exhaustive verification using integer bit masks (C++17).
// Run: c++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
for(int n:{13,17}){
 int U=(1<<n)-1; vector<int>N(n,0);
 for(int v=0;v<n;v++)for(int w=0;w<n;w++){
  int dif=(w-v+n)%n;
  bool res=false;
  for(int z=1;z<n;z++)if(z*z%n==dif)res=true;
  if(res)N[v]|=(1<<w);
 }
 auto total=[&](int s)->bool{
  for(int v=0;v<n;v++)if(!(N[v]&s))return false;
  return true;
 };
 auto secure=[&](int s)->bool{
  if(!total(s))return false;
  for(int v=0;v<n;v++)if(!(s>>v&1)){
   bool defended=false;
   int candidates=N[v]&s;
   while(candidates){int b=candidates&-candidates;candidates^=b;
      int after=(s^b)|(1<<v);
      if(total(after)){defended=true;break;}
   }
   if(!defended)return false;
  }
  return true;
 };
 array<int,6> count{};
 vector<int>X;
 vector<int>db(n+1,0),sec(n+1,0);int mismatch=0;
 for(int s=0;s<=U;s++){
   int k=__builtin_popcount((unsigned)s);
   bool d=true;
   for(int v=0;v<n;v++)if(__builtin_popcount((unsigned)(s&(N[v]|(1<<v))))<2){d=false;break;}
   bool st=secure(s);
   if(d)db[k]++;
   if(st)sec[k]++;
   if(d!=st)mismatch++;
   if(k<=5 && st){count[k]++;if(k==5)X.push_back(s);}
 }
 unordered_map<int,int>index;
 for(int i=0;i<(int)X.size();i++)index[X[i]]=i;
 cout<<"prime="<<n<<" totals_by_size=";
 for(int k=0;k<=5;k++)cout<<(k?",":"")<<count[k];
 cout<<" first_min_mask="<<(X.empty()?-1:X.front());
 cout<<" double_poly=";
 for(int k=0;k<=n;k++)if(db[k])cout<<k<<":"<<db[k]<<",";
 cout<<" secure_poly=";
 for(int k=0;k<=n;k++)if(sec[k])cout<<k<<":"<<sec[k]<<",";
 cout<<" all_subset_mismatch="<<mismatch;
 for(int type=0;type<=1;type++){
   vector<vector<int>>g(X.size());int edges=0;
   for(int i=0;i<(int)X.size();i++){
     int s=X[i];
     for(int rem=0;rem<n;rem++)if(s>>rem&1){
       for(int ins=0;ins<n;ins++)if(!(s>>ins&1)){
         if(type==1 && !(N[rem]>>ins&1))continue;
         int t=s^(1<<rem)^(1<<ins);
         auto it=index.find(t);
         if(it!=index.end() && i<it->second){
           int j=it->second;g[i].push_back(j);g[j].push_back(i);edges++;
         }
       }
     }
   }
   map<int,int>degrees,component_sizes,eccentricities;
   vector<int>seen(X.size(),0);
   for(int i=0;i<(int)X.size();i++)degrees[g[i].size()]++;
   for(int i=0;i<(int)X.size();i++)if(!seen[i]){
     queue<int>q;q.push(i);seen[i]=1;int cnt=0;
     while(!q.empty()){
       int u=q.front();q.pop();cnt++;
       for(int v:g[u])if(!seen[v]){seen[v]=1;q.push(v);}
     }
     component_sizes[cnt]++;
   }
   for(int i=0;i<(int)X.size();i++){
     vector<int>d(X.size(),-1);queue<int>q;q.push(i);d[i]=0;
     while(!q.empty()){
       int u=q.front();q.pop();
       for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}
     }
     eccentricities[*max_element(d.begin(),d.end())]++;
   }
   auto outmap=[](const map<int,int>&m){string s;for(auto [k,v]:m){if(!s.empty())s+=",";s+=to_string(k)+":"+to_string(v);}return s;};
   cout<<" "<<(type==0?"jump":"slide")<<"_edges="<<edges
       <<" degree="<<outmap(degrees)<<" components="<<outmap(component_sizes)
       <<" ecc="<<outmap(eccentricities);
 }
 cout<<"\n";
}
}
