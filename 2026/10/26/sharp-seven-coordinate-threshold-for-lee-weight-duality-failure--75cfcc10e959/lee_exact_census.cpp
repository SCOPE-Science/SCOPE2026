#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct E{ll a=0,b=0;};
E operator+(E x,E y){return {x.a+y.a,x.b+y.b};}
E mul(E x,E y){return {x.a*y.a+x.b*y.b,x.a*y.b+x.b*y.a-x.b*y.b};}
const int Q=5,MAXN=10,MAXW=20;
vector<array<int,2>> types;
array<array<int,13>,25> typ;
array<array<int,13>,25> val;
array<array<array<vector<E>,11>,11>,11> pol;
int c[13];int n;
struct Val {array<ll,21> dual{}; array<int,13> counts{};};
map<array<int,21>,Val> seen;
long long tested=0;bool found=false;
int weight(int x){x%=5;return min(x,5-x);}
vector<E> times(const vector<E>& v,const vector<E>& f){vector<E> y(v.size()+2); for(size_t i=0;i<v.size();i++)for(int j=0;j<3;j++)y[i+j]=y[i+j]+mul(v[i],f[j]);return y;}
const vector<E> f0={{1,0},{2,0},{2,0}};
const vector<E> f1={{1,0},{0,1},{-1,-1}};
const vector<E> f2={{1,0},{-1,-1},{0,1}};
vector<E> powerpoly(int a,int b,int z){auto &p=pol[a][b][z];if(!p.empty())return p;
 if(a)p=times(powerpoly(a-1,b,z),f0);
 else if(b)p=times(powerpoly(a,b-1,z),f1);
 else p=times(powerpoly(a,b,z-1),f2);
 return p;
}
bool rank2(){int j=-1;for(int i=1;i<13;i++)if(c[i]){
 if(j<0){j=i;continue;}
 if((types[i][0]*types[j][1]-types[i][1]*types[j][0])%5)return true;
}return false;}
array<int,21> primary(){array<int,21> v{};for(int u=0;u<25;u++){
 int s=0;for(int i=0;i<13;i++)s+=c[i]*val[u][i];assert(s<=2*n);v[s]++;
}return v;}
array<ll,21> dual(){array<ll,21> d{},alpha{};for(int u=0;u<25;u++){
 int a=0,b=0,z=0;for(int i=0;i<13;i++){
 if(typ[u][i]==0)a+=c[i];else if(typ[u][i]==1)b+=c[i];else z+=c[i];
}
 auto &p=pol[a][b][z];for(int k=0;k<=2*n;k++){d[k]+=p[k].a;alpha[k]+=p[k].b;}
}for(int k=0;k<=2*n;k++){assert(alpha[k]==0);assert(d[k]%25==0);d[k]/=25;}return d;}
// Check also the coefficient of alpha is zero, by exact symbolic arithmetic.

void evaluate(){if(found||!rank2())return;tested++;auto s=primary();auto it=seen.find(s);
 if(it==seen.end()){
  Val v;v.dual=dual();copy(c,c+13,v.counts.begin());seen.emplace(s,v);
 }else{
  auto d=dual();if(d!=it->second.dual){
   cout<<"WITNESS n="<<n<<" tested="<<tested<<"\nA ";for(int x:it->second.counts)cout<<x<<" ";cout<<"\nB ";for(int x:c)cout<<x<<" ";cout<<"\nprimary ";for(int i=0;i<=2*n;i++)if(s[i])cout<<i<<":"<<s[i]<<" ";
   cout<<"\ndual_A ";for(int i=0;i<=2*n;i++)if(it->second.dual[i])cout<<i<<":"<<it->second.dual[i]<<" ";
   cout<<"\ndual_B ";for(int i=0;i<=2*n;i++)if(d[i])cout<<i<<":"<<d[i]<<" ";cout<<"\n";
   found=true;
  }
 }
}
void enumerate(int i,int remain){if(found)return;if(i==12){c[i]=remain;evaluate();return;}
 for(int x=0;x<=remain&&!found;x++){c[i]=x;enumerate(i+1,remain-x);}}
int main(){
 for(int a=0;a<5;a++)for(int b=0;b<5;b++){
  array<int,2> v={a,b},other={(5-a)%5,(5-b)%5};if(v<=other)types.push_back(v);
 }
 sort(types.begin(),types.end());assert(types.size()==13 && types[0]==(array<int,2>{0,0}));
 cout<<"COL_TYPES ";for(auto t:types)cout<<"("<<t[0]<<","<<t[1]<<") ";cout<<"\n";
 for(int u=0;u<25;u++)for(int i=0;i<13;i++){
  int x=(u/5*types[i][0]+u%5*types[i][1])%5;
  typ[u][i]=weight(x);val[u][i]=weight(x);
 }
 pol[0][0][0]={{1,0}};
 for(int s=1;s<=MAXN;s++)for(int a=0;a<=s;a++)for(int b=0;b<=s-a;b++)powerpoly(a,b,s-a-b);
 for(n=2;n<=MAXN;n++){
  seen.clear();tested=0;found=false;auto start=chrono::steady_clock::now();enumerate(0,n);
  cout<<"SUMMARY n="<<n<<" rank2_multisets="<<tested<<" primary_signatures="<<seen.size()<<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"s"<<"\n"<<flush;
  if(found)break;
 }
}
