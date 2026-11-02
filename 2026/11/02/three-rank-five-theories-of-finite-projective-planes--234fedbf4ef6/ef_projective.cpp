#include <bits/stdc++.h>
using namespace std;
struct Plane {int q,n; vector<array<int,3>> P; vector<array<int,3>> L; vector<vector<unsigned char>> I;
int add(int a,int b)const{return q==4?a^b:(a+b)%q;}int mul(int a,int b)const{if(q!=4)return (a*b)%q; int r=0;for(int i=0;i<2;i++)if((b>>i)&1)r ^= (a<<i); if(r&8)r^=0b1100; if(r&4)r^=0b111;return r;}
int inv(int a)const{for(int x=1;x<q;x++)if(mul(x,a)==1)return x;throw runtime_error("inv");}
array<int,3> norm(array<int,3>a)const{int t=0;while(t<3&&a[t]==0)t++;if(t==3)throw runtime_error("zero");int v=inv(a[t]);for(int&i:a)i=mul(i,v);return a;}
Plane(int z):q(z){set<array<int,3>>pts;for(int x=0;x<q;x++)for(int y=0;y<q;y++)for(int z=0;z<q;z++){if(x||y||z)pts.insert(norm({x,y,z}));}P.assign(pts.begin(),pts.end());L=P;n=P.size();I.assign(n,vector<unsigned char>(n));for(int i=0;i<n;i++)for(int j=0;j<n;j++){int v=0;for(int k=0;k<3;k++)v=add(v,mul(P[i][k],L[j][k]));I[i][j]=(v==0);}if(n!=q*q+q+1)throw runtime_error("count");for(int i=0;i<n;i++){int deg=accumulate(I[i].begin(),I[i].end(),0);if(deg!=q+1)throw runtime_error("deg");}for(int j=0;j<n;j++){int deg=0;for(int i=0;i<n;i++)deg+=I[i][j];if(deg!=q+1)throw runtime_error("deg dual");}for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int pp=0,ll=0;for(int k=0;k<n;k++){pp+=I[i][k]&&I[j][k];ll+=I[k][i]&&I[k][j];}if(pp!=1||ll!=1)throw runtime_error("unique");}}
};
static inline uint16_t atom(const Plane &p,const int *v,int len){ // 5 sorts + 10 atomic pairs, 15 bits for <=5
 unsigned a=0;for(int i=0;i<len;i++)a |= unsigned(v[i]>=p.n)<<i;
 int k=0;for(int i=0;i<len;i++)for(int j=i+1;j<len;j++){bool on=(v[i]>=p.n)==(v[j]>=p.n)?(v[i]==v[j]): (v[i]<p.n?p.I[v[i]][v[j]-p.n]:p.I[v[j]][v[i]-p.n]);a|=unsigned(on)<<(5+k++);}
 return a;
}
struct VecHash {size_t operator()(const vector<uint32_t>&v)const noexcept{uint64_t h=0xcbf29ce484222325ULL;for(uint32_t a:v){h ^= a+0x9e3779b9+(h<<6)+(h>>2);h*=0x100000001b3ULL;}return h;}};

vector<uint32_t> faststep4(const Plane&p,unordered_map<vector<uint32_t>,uint32_t,VecHash>&dict){
 int n=p.n,N=2*n;size_t total=1;for(int k=0;k<4;k++)total*=N;vector<uint32_t>cur(total);
 vector<vector<int>> pp(n,vector<int>(n,-1)),ll(n,vector<int>(n,-1));
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j)for(int k=0;k<n;k++){if(p.I[i][k]&&p.I[j][k]) pp[i][j]=k; if(p.I[k][i]&&p.I[k][j]) ll[i][j]=k;}
 vector<uint32_t>sig;sig.reserve(20);int v[5]={};const int bitpos[4]={8,11,13,14};
 for(size_t a=0;a<total;a++){
  size_t s=a;for(int i=3;i>=0;i--){v[i]=s%N;s/=N;}
  int base=0;for(int i=0;i<4;i++)base|=(v[i]>=n)<<i;
  int pairidx=0;for(int i=0;i<4;i++)for(int j=i+1;j<5;j++){if(j==4){pairidx++;continue;}bool on=(v[i]>=n)==(v[j]>=n)?v[i]==v[j]:(v[i]<n?p.I[v[i]][v[j]-n]:p.I[v[j]][v[i]-n]);base|=int(on)<<(5+pairidx++);}
  sig.clear();
  for(int i=0;i<4;i++){v[4]=v[i];sig.push_back(atom(p,v,5));}
  auto emit=[&](bool line,int obj){int z=base|(int(line)<<4);for(int i=0;i<4;i++){if(line&&(v[i]<n)){if(obj<0 ||p.I[v[i]][obj]) z|=1<<bitpos[i];}else if(!line&&(v[i]>=n)){if(obj<0 ||p.I[obj][v[i]-n])z|=1<<bitpos[i];}}sig.push_back(z);};
  auto zeros=[&](bool line){sig.push_back(base | (int(line)<<4));};
  // generic nonincidence, valid for q>=4
  zeros(false);zeros(true);
  for(int i=0;i<4;i++)if(v[i]>=n){int z=base;for(int j=0;j<4;j++)if(v[j]==v[i])z|=1<<bitpos[j];sig.push_back(z);}
  for(int i=0;i<4;i++)if(v[i]<n){int z=base|(1<<4);for(int j=0;j<4;j++)if(v[j]==v[i])z|=1<<bitpos[j];sig.push_back(z);}
  for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){
   if(v[i]>=n&&v[j]>=n&&v[i]!=v[j]){int obj=ll[v[i]-n][v[j]-n];bool found=false;for(int t=0;t<4;t++)if(v[t]==obj) found=true; if(!found)emit(false,obj);}
   if(v[i]<n&&v[j]<n&&v[i]!=v[j]){int obj=pp[v[i]][v[j]];bool found=false;for(int t=0;t<4;t++)if(v[t]==obj+n)found=true;if(!found)emit(true,obj);}
  }
  sort(sig.begin(),sig.end());sig.erase(unique(sig.begin(),sig.end()),sig.end());auto [it,newsig]=dict.try_emplace(sig,dict.size());cur[a]=it->second;
 }
 return cur;
}
vector<uint32_t> step(const Plane &p,int k,const vector<uint32_t>*prev,int&num,unordered_map<vector<uint32_t>,uint32_t,VecHash>&dict){
 int N=2*p.n;size_t total=1;for(int i=0;i<k;i++)total*=N;vector<uint32_t>cur(total);
 vector<uint32_t>sig;sig.reserve(N);int v[5]={};for(size_t a=0;a<total;a++){size_t s=a;for(int i=k-1;i>=0;i--){v[i]=s%N;s/=N;}sig.clear();for(int u=0;u<N;u++){v[k]=u; if(k==4) sig.push_back(atom(p,v,5)); else sig.push_back((*prev)[a*N+u]);}sort(sig.begin(),sig.end());sig.erase(unique(sig.begin(),sig.end()),sig.end());auto [it,newone]=dict.try_emplace(sig,dict.size());cur[a]=it->second;}
 num=dict.size();return cur;
}
int main(int argc,char**argv){if(argc==3&&string(argv[1])=="check"){Plane p(atoi(argv[2]));unordered_map<vector<uint32_t>,uint32_t,VecHash>dict;int num;auto full=step(p,4,nullptr,num,dict);auto fast=faststep4(p,dict);size_t mismatches=0;int N=p.n*2;for(size_t i=0;i<full.size();i++)if(full[i]!=fast[i]){if(mismatches<12){size_t s=i;int v[4];for(int j=3;j>=0;j--){v[j]=s%N;s/=N;}cerr<<"MISMATCH ";for(int j:v)cerr<<j<<",";cerr<<" expected "<<full[i]<<" actual "<<fast[i]<<"\n";}mismatches++;}cout<<"FAST_FULL_MISMATCHES "<<mismatches<<" of "<<full.size()<<"\n";return mismatches?1:0;}
vector<unique_ptr<Plane>> planes;vector<vector<uint32_t>>prev;for(int i=1;i<argc;i++){int q=atoi(argv[i]);planes.emplace_back(make_unique<Plane>(q));prev.emplace_back();}
for(int k=4;k>=0;k--){unordered_map<vector<uint32_t>,uint32_t,VecHash>dict;dict.reserve(1000);for(size_t j=0;j<planes.size();j++){auto &p=*planes[j];int n; auto cur=(k==4&&p.q>=5?faststep4(p,dict):step(p,k,k==4?nullptr:&prev[j],n,dict));int unique=unordered_set<uint32_t>(cur.begin(),cur.end()).size();cerr<<"q="<<p.q<<" rank="<<5-k<<" free="<<k<<" types="<<unique<<" union="<<n<<" root="<<(k==0?int(cur[0]):-1)<<"\n";prev[j].swap(cur);}}
for(size_t j=0;j<planes.size();j++)cout<<"RANK5_ROOT q="<<planes[j]->q<<" class="<<prev[j][0]<<"\n";
{
vector<vector<uint32_t>> old(planes.size());
for(int k=3;k>=0;k--){unordered_map<vector<uint32_t>,uint32_t,VecHash>dict;dict.reserve(1000);
 for(size_t j=0;j<planes.size();j++){
 auto &p=*planes[j];int N=2*p.n;size_t total=1;for(int t=0;t<k;t++)total*=N;
 vector<uint32_t>cur(total);vector<uint32_t>sig;sig.reserve(N);int v[5]={};
 for(size_t a=0;a<total;a++){size_t s=a;for(int t=k-1;t>=0;t--){v[t]=s%N;s/=N;}
 sig.clear();for(int u=0;u<N;u++){v[k]=u;sig.push_back(k==3?atom(p,v,4):old[j][a*N+u]);}
 sort(sig.begin(),sig.end());sig.erase(unique(sig.begin(),sig.end()),sig.end());auto[it,fresh]=dict.try_emplace(sig,dict.size());cur[a]=it->second;
 }
 old[j].swap(cur);
 }
}
for(size_t j=0;j<planes.size();j++)cout<<"RANK4_ROOT q="<<planes[j]->q<<" class="<<old[j][0]<<"\n";
}
cout<<"VERIFY_OK\n";
}
