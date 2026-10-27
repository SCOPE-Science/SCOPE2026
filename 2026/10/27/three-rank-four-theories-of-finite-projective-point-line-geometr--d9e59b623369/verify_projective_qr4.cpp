#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
struct VHash{size_t operator()(const vector<uint32_t>&v)const noexcept{U h=1469598103934665603ull;for(auto x:v){h^=x+0x9e3779b9;h*=1099511628211ull;}return (size_t)h;}};
struct Interner{unordered_map<vector<uint32_t>,uint32_t,VHash> mp; vector<vector<uint32_t>> rev; uint32_t get(vector<uint32_t> &v){auto it=mp.find(v);if(it!=mp.end())return it->second; uint32_t id=rev.size();mp.emplace(v,id);rev.push_back(v);return id;}};
struct Bits{U w[3]={0,0,0};void set(int i){w[i>>6]|=(1ull<<(i&63));}void reset(int i){w[i>>6]&=~(1ull<<(i&63));}bool any()const{return w[0]||w[1]||w[2];} Bits operator&(const Bits&b)const{Bits c;for(int t=0;t<3;t++)c.w[t]=w[t]&b.w[t];return c;} Bits& operator&=(const Bits&b){for(int t=0;t<3;t++)w[t]&=b.w[t];return *this;} }; 
struct Geometry{int d,q,np,nl,n;vector<vector<int>> pts, lines;vector<Bits> incident;Bits full[2];vector<vector<uint8_t>> I;};
int norm(vector<int>& a,int q){int p=-1;for(int i=0;i<(int)a.size();i++)if(a[i]){p=i;break;}if(p==-1)return 0;int inv=1;for(;inv<q;inv++)if((inv*a[p])%q==1)break;for(int &x:a)x=(x*inv)%q;return 1;}
Geometry makegeo(int d,int q){ Geometry G;G.d=d;G.q=q;int size=1;for(int i=0;i<=d;i++)size*=q;set<vector<int>> S;for(int z=1;z<size;z++){int x=z;vector<int> a(d+1);for(int k=0;k<=d;k++){a[k]=x%q;x/=q;}norm(a,q);S.insert(a);}G.pts.assign(S.begin(),S.end()); G.np=G.pts.size();map<vector<int>,int> index;for(int i=0;i<G.np;i++)index[G.pts[i]]=i; set<vector<int>> LS;for(int i=0;i<G.np;i++)for(int j=i+1;j<G.np;j++){vector<int> span;for(int a=0;a<q;a++)for(int b=0;b<q;b++){if(!a&&!b)continue;vector<int> t(d+1);for(int k=0;k<=d;k++)t[k]=(a*G.pts[i][k]+b*G.pts[j][k])%q;norm(t,q);span.push_back(index.at(t));}sort(span.begin(),span.end());span.erase(unique(span.begin(),span.end()),span.end());LS.insert(span);}G.lines.assign(LS.begin(),LS.end());G.nl=G.lines.size();G.n=G.np+G.nl; if(G.np>192||G.nl>192){throw logic_error("over 192 type count");}
G.incident.resize(G.n);G.I.assign(G.np,vector<uint8_t>(G.nl,0));for(int j=0;j<G.nl;j++)for(int p:G.lines[j]){G.incident[p].set(j);G.incident[G.np+j].set(p);G.I[p][j]=1;}
for(int p=0;p<G.np;p++)G.full[0].set(p);for(int j=0;j<G.nl;j++)G.full[1].set(j);return G;}
int kind(const Geometry&G,int i){return i>=G.np;}
int rel(const Geometry&G,int a,int b){if(a==b)return 2;if(kind(G,a)==kind(G,b))return 0;return kind(G,a)?G.I[b][a-G.np]:G.I[a][b-G.np];}
const int pairs[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
uint32_t code4(const Geometry&G,int a,int b,int c,int d){int x[4]={a,b,c,d};uint32_t code=0;for(int t=0;t<4;t++)code|=(kind(G,x[t])<<t);for(int t=0;t<6;t++)code|=(rel(G,x[pairs[t][0]],x[pairs[t][1]])<<(4+2*t));return code;}
struct Result{uint32_t all;vector<uint32_t> t3;vector<uint32_t> t2;vector<uint32_t> t1;size_t nT1,nT2,nT3;};
Result eval(const Geometry&G,Interner& i1,Interner&i2,Interner&i3,Interner&i4){
 int N=G.n;Result R;R.t1.resize((size_t)N*N*N);
 vector<uint32_t> types;types.reserve(24);vector<uint32_t> scratch;for(int a=0;a<N;a++){for(int b=0;b<N;b++)for(int c=0;c<N;c++){
  types.clear();int x[3]={a,b,c};for(int t=0;t<3;t++)types.push_back(code4(G,a,b,c,x[t]));
  uint32_t base=0;for(int t=0;t<3;t++)base|=(kind(G,x[t])<<t);base|=(rel(G,a,b)<<(4+0));base|=(rel(G,a,c)<<(4+2));base|=(rel(G,b,c)<<(4+6));
  for(int s=0;s<2;s++){
   Bits allowed=G.full[s];int opposite[3], nopp=0;
   for(int t=0;t<3;t++){int it=x[t];if(kind(G,it)==s)allowed.reset(s?it-G.np:it);else opposite[nopp++]=it;}
   for(int m=0;m<(1<<nopp);m++){
    Bits cur=allowed;
    for(int t=0;t<nopp;t++){const Bits&inc=G.incident[opposite[t]];if((m>>t)&1){cur&=inc;}else{for(int j=0;j<3;j++)cur.w[j]&=~inc.w[j];}}
    if(!cur.any())continue;
    uint32_t code=base|(s<<3);
    for(int t=0;t<3;t++)if(kind(G,x[t])!=s){int ii=0;for(;ii<nopp;ii++)if(opposite[ii]==x[t])break; if((m>>ii)&1){int pi=(t==0?2:(t==1?4:5));code|=(1<<(4+2*pi));}}
    types.push_back(code);
   }
  }
  sort(types.begin(),types.end());types.erase(unique(types.begin(),types.end()),types.end());R.t1[((size_t)a*N+b)*N+c]=i1.get(types);
 }
 if((a%20)==0){cerr<<"d="<<G.d<<" q="<<G.q<<" t1 "<<a<<"/"<<N<<" ids="<<i1.rev.size()<<"\r";}
 }
 R.nT1=i1.rev.size();R.t2.resize((size_t)N*N);scratch.reserve(N);
 for(int a=0;a<N;a++)for(int b=0;b<N;b++){
  scratch.clear();size_t k=((size_t)a*N+b)*N;for(int c=0;c<N;c++)scratch.push_back(R.t1[k+c]);
  sort(scratch.begin(),scratch.end());scratch.erase(unique(scratch.begin(),scratch.end()),scratch.end());R.t2[(size_t)a*N+b]=i2.get(scratch);
 }
 R.nT2=i2.rev.size();R.t3.resize(N);
 for(int a=0;a<N;a++){
  scratch.clear();for(int b=0;b<N;b++)scratch.push_back(R.t2[(size_t)a*N+b]);
  sort(scratch.begin(),scratch.end());scratch.erase(unique(scratch.begin(),scratch.end()),scratch.end());R.t3[a]=i3.get(scratch);
 }
 R.nT3=i3.rev.size();scratch=R.t3;sort(scratch.begin(),scratch.end());scratch.erase(unique(scratch.begin(),scratch.end()),scratch.end());R.all=i4.get(scratch);return R;
}
int main(int argc,char**argv){Interner a,b,c,d;for(int i=1;i<argc;i++){int D,Q;if(sscanf(argv[i],"%d,%d",&D,&Q)!=2)continue;auto G=makegeo(D,Q);cerr<<"\nPG("<<D<<","<<Q<<") n="<<G.n<<" points="<<G.np<<" lines="<<G.nl<<"\n";auto R=eval(G,a,b,c,d);set<uint32_t> t2(R.t2.begin(),R.t2.end()),t3(R.t3.begin(),R.t3.end()),t1(R.t1.begin(),R.t1.end());cout<<"PG("<<D<<","<<Q<<") |P|="<<G.np<<" |L|="<<G.nl<<" rank4_type="<<R.all<<" local_t1="<<t1.size()<<" local_t2="<<t2.size()<<" local_t3="<<t3.size()<<" all_t1="<<a.rev.size()<<" all_t2="<<b.rev.size()<<" all_t3="<<c.rev.size()<<"\n"<<flush;}
return 0;}
