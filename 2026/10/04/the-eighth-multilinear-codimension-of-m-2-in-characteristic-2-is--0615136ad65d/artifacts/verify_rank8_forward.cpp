#include <bits/stdc++.h>
using namespace std;
struct Basis {
 int ROWS,W,rank=0; vector<uint64_t*> piv; vector<unique_ptr<uint64_t[]>> store;
 Basis(int rows):ROWS(rows),W((rows+63)/64),piv(rows,nullptr){store.reserve(6000);} 
 bool add(const uint64_t* src){
   vector<uint64_t> x(src,src+W);
   while(true){
     int wi=W-1; while(wi>=0 && x[wi]==0) --wi;
     if(wi<0) return false;
     int bit=63-__builtin_clzll(x[wi]); int p=(wi<<6)+bit;
     auto b=piv[p];
     if(!b){auto mem=make_unique<uint64_t[]>(W); memcpy(mem.get(),x.data(),W*8); piv[p]=mem.get(); store.push_back(move(mem)); rank++; return true;}
     for(int j=0;j<=wi;++j) x[j]^=b[j];
   }
 }
 bool addMove(vector<uint64_t>& x){
   while(true){int wi=W-1; while(wi>=0&&x[wi]==0)--wi; if(wi<0)return false; int bit=63-__builtin_clzll(x[wi]);int p=(wi<<6)+bit;auto b=piv[p];if(!b){auto mem=make_unique<uint64_t[]>(W);memcpy(mem.get(),x.data(),W*8);piv[p]=mem.get();store.push_back(move(mem));rank++;return true;} for(int j=0;j<=wi;++j)x[j]^=b[j];}
 }
};
void makecol(const array<int,8>& perm, vector<uint64_t>& x){const int n=8; fill(x.begin(),x.end(),0);for(int path=0;path<(1<<(n+1));++path){unsigned assign=0;for(int k=0;k<n;++k){int a=(path>>k)&1,b=(path>>(k+1))&1,e=(a<<1)|b;assign|=(unsigned)e<<(2*perm[k]);}int out=((path&1)<<1)|((path>>n)&1);unsigned row=(assign<<2)|out;x[row>>6]^=1ULL<<(row&63);}}
int main(){const int n=8,ROWS=4*(1<<(2*n)),W=(ROWS+63)/64;Basis global(ROWS);vector<uint64_t>x(W);
for(int first=0;first<8;++first){
 vector<int> rest;for(int i=0;i<8;++i)if(i!=first)rest.push_back(i);
 Basis local(ROWS); long long cnt=0;
 do{array<int,8> p; p[0]=first;for(int i=0;i<7;++i)p[i+1]=rest[i];makecol(p,x);local.addMove(x);cnt++;}while(next_permutation(rest.begin(),rest.end()));
 cerr<<"chunk "<<first<<" localrank "<<local.rank<<"\n";
 for(auto &u:local.store){memcpy(x.data(),u.get(),W*8);global.addMove(x);} 
 cerr<<" merged global "<<global.rank<<"\n";
 }
cout<<"rank "<<global.rank<<" kernel "<<40320-global.rank<<"\n";
}
