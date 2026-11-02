#include <bits/stdc++.h>
using namespace std;
struct Sig {uint64_t a,b;bool operator==(const Sig &x)const{return a==x.a&&b==x.b;}};
struct H {size_t operator()(const Sig&x)const{return hash<uint64_t>{}(x.a ^ (x.b * 0x9e3779b97f4a7c15ULL));}};
struct VH {size_t operator()(const vector<int>&v)const {uint64_t x=1469598103934665603ULL;for(int a:v){x^=uint64_t(a)+0x9e3779b97f4a7c15ULL; x*=1099511628211ULL;}return x;}};
unordered_map<Sig,int,H> atoms;unordered_map<vector<int>,int,VH> twos,ones,roots;
int intern_a(Sig x){auto [it,ins]=atoms.emplace(x,(int)atoms.size()); return it->second;}
int intern_v(unordered_map<vector<int>,int,VH>&d,vector<int>& v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());auto [it,ins]=d.emplace(v,(int)d.size());return it->second;}
int main(int argc,char**argv){int mx=argc>1?atoi(argv[1]):20;for(int n=1;n<=mx;n++){
 vector<pair<int,int>> elems={{-1,-1}};
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)elems.push_back({i,j});
 int sz=elems.size();
 vector<int> prod(sz*sz,0);
 for(int a=1;a<sz;a++)for(int b=1;b<sz;b++)if(elems[a].second==elems[b].first){int i=elems[a].first,l=elems[b].second; for(int c=1;c<sz;c++)if(elems[c].first==i&&elems[c].second==l){prod[a*sz+b]=c;break;}}
 auto atom=[&](int x,int y,int z){int w[4]={0,x,y,z};Sig s{0,0};int shift=0;auto add=[&](bool q){if(q){if(shift<64)s.a|=1ULL<<shift; else s.b|=1ULL<<(shift-64);}shift++;}; for(int i=0;i<4;i++)for(int j=0;j<4;j++)add(w[i]==w[j]);for(int i=0;i<4;i++)for(int j=0;j<4;j++)for(int k=0;k<4;k++)add(prod[w[i]*sz+w[j]]==w[k]);return s;};
 vector<int> pairtype(sz*sz);vector<int> singletype(sz);
 for(int x=0;x<sz;x++)for(int y=0;y<sz;y++){
   vector<int> next;next.reserve(sz);
   for(int z=0;z<sz;z++)next.push_back(intern_a(atom(x,y,z)));
   pairtype[x*sz+y]=intern_v(twos,next);
 }
 for(int x=0;x<sz;x++){
    vector<int> next;next.reserve(sz);
    for(int y=0;y<sz;y++)next.push_back(pairtype[x*sz+y]);
    singletype[x]=intern_v(ones,next);
 }
 vector<int> final=singletype;int root=intern_v(roots,final);
 printf("n=%d elements=%d root=%d atom_types=%zu pair_types=%zu singled_types=%zu distinct_singles=%zu\n",n,sz,root,atoms.size(),twos.size(),ones.size(),set<int>(final.begin(),final.end()).size());fflush(stdout);
 }
}
