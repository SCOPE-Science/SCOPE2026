// Plane-cubic all-smooth pencil census over F3; exact projective finite-field test.
#include <bits/stdc++.h>
using namespace std;
constexpr int P=59049,D=10;
array<array<uint8_t,D>,P> digits; int pw3[D];
vector<array<int,3>> M3; int gen[4][D][D]={};
vector<int> smoothV, smoothClass, orbitRep, orbitSize;
vector<unsigned short> rational;
int enc(const array<uint8_t,D>& a){int v=0;for(int i=0;i<D;i++)v+=a[i]*pw3[i];return v;}
int unit(int v){auto d=digits[v];int c=0;for(int i=0;i<D;i++)if(d[i]){c=d[i];break;}if(c==2){for(int i=0;i<D;i++)d[i]=(d[i]*2)%3;return enc(d);}return v;}
int mi(const array<int,3> &m){for(int i=0;i<D;i++)if(M3[i]==m)return i;abort();}
void mats(){for(int g=0;g<4;g++)for(int i=0;i<10;i++){
 auto e=M3[i];if(g==0)swap(e[0],e[1]);if(g==1)swap(e[1],e[2]);
 if(g==3){gen[g][i][i]=e[0]%2?2:1;continue;}
 if(g==2){int r=e[0];for(int t=0;t<=r;t++){
  array<int,3> f={t,e[1]+r-t,e[2]};int bin=(r==3&&(t==1||t==2))?0:(r==2&&t==1)?2:1;
  gen[g][i][mi(f)]=(gen[g][i][mi(f)]+bin)%3;
 }continue;}
 gen[g][i][mi(e)]=1;
}}
int tr(int v,int g){int d[D]={};for(int i=0;i<D;i++)if(digits[v][i])for(int j=0;j<D;j++)d[j]=(d[j]+digits[v][i]*gen[g][i][j])%3;int out=0;for(int i=0;i<D;i++)out+=d[i]*pw3[i];return unit(out);}
int add(int u,int v,int cv){int x=0;for(int i=0;i<10;i++)x+=((digits[u][i]+cv*digits[v][i])%3)*pw3[i];return x;}
struct GF{
 int n,q; vector<int> am,bm;
 GF(int n):n(n){q=1;for(int k=0;k<n;k++)q*=3;am.resize(q*q);bm.resize(q*q);
  int mod[4]={0,0,0,0};
  if(n==2){mod[0]=1;mod[2]=1;} // t^2+1
  if(n==3){mod[0]=1;mod[1]=2;mod[3]=1;} // t^3-t+1
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int A[3]={},B[3]={};int x=a,y=b;for(int k=0;k<n;k++){A[k]=x%3;B[k]=y%3;x/=3;y/=3;}
   int C[6]={},S[3]={};for(int k=0;k<n;k++){S[k]=(A[k]+B[k])%3;for(int j=0;j<n;j++)C[k+j]=(C[k+j]+A[k]*B[j])%3;}
   if(n>1)for(int k=2*n-2;k>=n;k--){int t=C[k];if(t)for(int j=0;j<n;j++)C[k-n+j]=(C[k-n+j]+3-t*mod[j]%3)%3;C[k]=0;}
   int sum=0,prod=0,p=1;for(int k=0;k<n;k++){sum+=S[k]*p;prod+=C[k]*p;p*=3;}
   am[a*q+b]=sum;bm[a*q+b]=prod;
  }
 }
 inline int a(int x,int y)const{return am[x*q+y];}
 inline int m(int x,int y)const{return bm[x*q+y];}
 inline int s(int x,int c)const{int r=0;for(int i=0;i<c;i++)r=a(r,x);return r;}
};

bool sing(int id,const GF &K,int x,int y,int z);
bool geom_smooth(int id,const vector<GF>&fields){
 for(const GF &field:fields){
  for(int t=0;t<field.q;t++){
   for(int u=0;u<field.q;u++)if(sing(id,field,t,u,1))return false;
   if(sing(id,field,t,1,0))return false;
  }
  if(sing(id,field,1,0,0))return false;
 }
 return true;
}
// Nonzero common zero of F,F_X,F_Y,F_Z, evaluated in a chosen projective coordinate chart.
bool sing(int id,const GF &K,int x,int y,int z){
 int xyz[3]={x,y,z};int powa[3][4];for(int k=0;k<3;k++){powa[k][0]=1;for(int h=1;h<=3;h++)powa[k][h]=K.m(powa[k][h-1],xyz[k]);}
 int v[4]={};
 for(int i=0;i<D;i++){
  int c=digits[id][i];if(!c)continue; auto e=M3[i];
  int val=K.m(K.m(powa[0][e[0]],powa[1][e[1]]),powa[2][e[2]]);
  v[0]=K.a(v[0],K.s(val,c));
  for(int j=0;j<3;j++)if(e[j]%3){auto ee=e;ee[j]--;int w=K.m(K.m(powa[0][ee[0]],powa[1][ee[1]]),powa[2][ee[2]]);v[j+1]=K.a(v[j+1],K.s(w,c*e[j]%3));}
 }
 return v[0]==0&&v[1]==0&&v[2]==0&&v[3]==0;
}
int main(int argc,char**argv){
 pw3[0]=1;for(int i=1;i<D;i++)pw3[i]=pw3[i-1]*3;
 for(int i=0;i<P;i++){int t=i;for(int j=0;j<D;j++){digits[i][j]=t%3;t/=3;}}
 for(int i=0;i<=3;i++)for(int j=0;j<=3-i;j++)M3.push_back({i,j,3-i-j});mats();
 vector<GF> fields;fields.emplace_back(1);fields.emplace_back(2);fields.emplace_back(3);
 vector<int> seen(P),orbitIdx(P,-1),pReps,pSizes;vector<vector<int>>orbitMembers;
 for(int f=1;f<P;f++)if(unit(f)==f&&!seen[f]){
  vector<int> mem;deque<int> q={f};seen[f]=1;
  while(!q.empty()){int x=q.front();q.pop_front();mem.push_back(x);
   for(int g=0;g<4;g++){int y=tr(x,g);if(!seen[y]){seen[y]=1;q.push_back(y);}}
  }
  int r=orbitMembers.size();for(int v:mem)orbitIdx[v]=r;
  pReps.push_back(f);pSizes.push_back(mem.size());orbitMembers.push_back(move(mem));
 }
 cerr<<"projective cubic orbits (all): "<<orbitMembers.size()<<"\n";
 smoothV.assign(P,0);rational.assign(P,0);
 vector<array<int,3>> pts;for(int x=0;x<3;x++)for(int y=0;y<3;y++)pts.push_back({x,y,1});for(int x=0;x<3;x++)pts.push_back({x,1,0});pts.push_back({1,0,0});
 for(int r=0;r<(int)orbitMembers.size();r++){
  bool ok=geom_smooth(pReps[r],fields);
  cerr<<"all_orbit "<<r<<" rep="<<pReps[r]<<" size="<<pSizes[r]<<" smooth="<<ok<<"\n";
  if(ok){
  orbitRep.push_back(pReps[r]);orbitSize.push_back(pSizes[r]);
  for(int id:orbitMembers[r]){smoothV[id]=smoothV[add(id,id,1)]=1;smoothClass.push_back(id);}
  }
 }
 for(int id:smoothClass){int mask=0;for(int j=0;j<13;j++){
  auto p=pts[j];int val=0;for(int i=0;i<D;i++)if(digits[id][i]){
   auto e=M3[i];int c=digits[id][i];for(int k=0;k<3;k++)for(int t=0;t<e[k];t++)c=(c*p[k])%3;val=(val+c)%3;
  }
  if(!val)mask|=1<<j;
 }rational[id]=mask;rational[add(id,id,1)]=mask;}
 cerr<<"smooth projective cubics: "<<smoothClass.size()<<", smooth orbits "<<orbitRep.size()<<"\n";
 if(argc==2){ofstream fd(argv[1]);for(int id:smoothClass)fd<<id<<"\n";}
 unsigned long long hist[10]={},total=0;
 vector<array<unsigned long long,10>> rows(orbitRep.size());
 for(int r=0;r<(int)orbitRep.size();r++){
  int f=orbitRep[r];unsigned long long sub=0;
  for(int g:smoothClass)if(g!=f && smoothV[add(f,g,1)]&&smoothV[add(f,g,2)]){
    int k=__builtin_popcount((unsigned)rational[f]&rational[g]);
    if(k==4 && r==3){static bool once=false;if(!once){once=true;cerr<<"extremal_pair f="<<f<<" g="<<g<<" base_mask="<<((unsigned)rational[f]&rational[g])<<"\n";}}
    if(k>9)abort();hist[k]+=orbitSize[r];rows[r][k]++;total+=orbitSize[r];sub++;
  }
  cerr<<"orbit "<<r<<" f="<<f<<" size="<<orbitSize[r]<<" N1="<<__builtin_popcount((unsigned)rational[f])<<" partner_count="<<sub<<"\n";
 }
 cout<<"all_orbits="<<orbitMembers.size()<<" smooth_cubics="<<smoothClass.size()<<" smooth_cubic_orbits="<<orbitRep.size()<<"\n";
 cout<<"ordered_generator_pairs="<<total<<" pencils="<<total/12<<" remainder="<<total%12<<"\n";
 for(int k=0;k<=9;k++)cout<<"base="<<k<<" ordered="<<hist[k]<<" pencils="<<hist[k]/12<<" rem="<<hist[k]%12<<"\n";
 cout<<"orbit_summary: id size rationalpoints & basecount-per-fixed-rep\n";
 for(int r=0;r<(int)orbitRep.size();r++){
  cout<<orbitRep[r]<<" "<<orbitSize[r]<<" "<<__builtin_popcount((unsigned)rational[orbitRep[r]]);for(int k=0;k<=9;k++)cout<<" "<<rows[r][k];cout<<"\n";
 }
}
