#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
vector<U> faces[14];
U adjm[36];
void rec(U cand,U chosen,int sz){
  if(chosen) faces[sz].push_back(chosen);
  while(cand){U b=cand&-cand; int v=__builtin_ctzll(b); cand^=b; rec(cand & ~adjm[v], chosen|b, sz+1);}
}
vector<int> symdiff(const vector<int>&a,const vector<int>&b){
 vector<int> c; c.reserve(a.size()+b.size()); size_t i=0,j=0;
 while(i<a.size()&&j<b.size()){
  if(a[i]<b[j]) c.push_back(a[i++]);
  else if(b[j]<a[i]) c.push_back(b[j++]);
  else {i++;j++;}
 }
 while(i<a.size()) c.push_back(a[i++]); while(j<b.size()) c.push_back(b[j++]); return c;
}
int main(){
 for(int a=0;a<36;a++) for(int b=0;b<36;b++) if(a!=b){int i=a/6,j=a%6,u=b/6,v=b%6; int di=min((i-u+6)%6,(u-i+6)%6), dj=min((j-v+6)%6,(v-j+6)%6); if(di+dj>4) adjm[a]|=1ULL<<b;}
 rec((1ULL<<36)-1,0,0);
 cerr<<"counts"; for(int s=1;s<=13;s++) cerr<<" "<<faces[s].size(); cerr<<"\n";
 vector<unordered_map<U,int>> ix(14);
 for(int s=1;s<=13;s++){ix[s].reserve(faces[s].size()*1.5); for(int i=0;i<(int)faces[s].size();i++) ix[s][faces[s][i]]=i;}
 for(int d=1;d<=12;d++){
   vector<vector<int>> piv(faces[d].size()); int rank=0;
   for(U m:faces[d+1]){
     vector<int> v; v.reserve(d+1); U bits=m;
     while(bits){U b=bits&-bits; bits^=b; auto it=ix[d].find(m^b); v.push_back(it->second);}
     sort(v.begin(),v.end());
     while(!v.empty()){
       int p=v.back();
       if(piv[p].empty()){piv[p]=move(v); rank++; break;}
       v=symdiff(v,piv[p]);
     }
   }
   cerr<<"d="<<d<<" rank="<<rank<<"\n";
 }
}
