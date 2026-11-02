#include <bits/stdc++.h>
using namespace std;
struct M {int a,b,c,d;bool operator<(M const&o)const{return tie(a,b,c,d)<tie(o.a,o.b,o.c,o.d);}bool operator==(M const&o)const{return tie(a,b,c,d)==tie(o.a,o.b,o.c,o.d);} };
int p,f,q; vector<int> poly; int A[32][32],P[32][32],Neg[32]; M I{1,0,0,1};
vector<int> toPoly(int v,int l){vector<int> a(l);for(int i=0;i<l;i++){a[i]=v%p;v/=p;}return a;}
int fromPoly(vector<int> const &a){int o=0,m=1;for(int x:a){o+=x*m;m*=p;}return o;}
void field(){for(int a=0;a<q;a++){auto u=toPoly(a,f);for(int b=0;b<q;b++){auto v=toPoly(b,f);vector<int>w(f),z(2*f-1);for(int i=0;i<f;i++){w[i]=(u[i]+v[i])%p;for(int j=0;j<f;j++)z[i+j]=(z[i+j]+u[i]*v[j])%p;}for(int i=2*f-2;i>=f;i--)for(int j=0;j<f;j++)z[i-f+j]=((z[i-f+j]-z[i]*poly[j])%p+p)%p;z.resize(f);A[a][b]=fromPoly(w);P[a][b]=fromPoly(z);}Neg[a]=0;for(int b=0;b<q;b++)if(A[a][b]==0)Neg[a]=b;}}
M neg(M z){return{Neg[z.a],Neg[z.b],Neg[z.c],Neg[z.d]};}
M can(M z){auto w=neg(z);return min(z,w);}
M mul(M x,M y){return can({A[P[x.a][y.a]][P[x.b][y.c]],A[P[x.a][y.b]][P[x.b][y.d]],A[P[x.c][y.a]][P[x.d][y.c]],A[P[x.c][y.b]][P[x.d][y.d]]});}
int main(int argc,char**argv){p=atoi(argv[1]);f=atoi(argv[2]);q=1;for(int i=0;i<f;i++)q*=p;poly.clear();for(int i=3;i<argc;i++)poly.push_back(atoi(argv[i]));if((int)poly.size()!=f) {cerr<<"need f poly coefficients\n";return 1;}field();set<M> S;
 for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)for(int d=0;d<q;d++)if(A[P[a][d]][Neg[P[b][c]]]==1) S.insert(can({a,b,c,d}));
 vector<M> v(S.begin(),S.end()); M e=can(I);vector<M> sq(v.size());for(int j=0;j<(int)v.size();j++)sq[j]=mul(v[j],v[j]);
 set<string> roottypes;map<string,int> freq;
 for(int j=0;j<(int)v.size();j++){
  M x=v[j],xx=sq[j];set<unsigned long long> diagrams;
  for(int k=0;k<(int)v.size();k++){
   M y=v[k],yy=sq[k];M xy=mul(x,y),yx=mul(y,x); M t[3]={e,x,y};
   unsigned long long z=0;int h=0;
   for(int u=0;u<3;u++)for(int w=0;w<3;w++)z|=(unsigned long long)(t[u]==t[w])<<h++;
   M prod[3][3]={{e,x,y},{x,xx,xy},{y,yx,yy}};
   for(int u=0;u<3;u++)for(int w=0;w<3;w++)for(int r=0;r<3;r++)z|=(unsigned long long)(prod[u][w]==t[r])<<h++;
   diagrams.insert(z);
  }
  ostringstream o;for(auto z:diagrams)o<<hex<<z<<",";
  string st=o.str();roottypes.insert(st);freq[st]++;
 }
 cout<<"GROUP "<<q<<" "<<v.size()<<" "<<roottypes.size()<<"\n";
 for(auto s:roottypes) cout<<"SIG "<<s<<"\n";
}
