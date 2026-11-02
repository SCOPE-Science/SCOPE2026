#include<bits/stdc++.h>
using namespace std;
struct VHash{size_t operator()(vector<int> const&v)const noexcept{size_t s=0xabcdef123456789ULL;for(int x:v)s^=(size_t)(x+0x9e3779b9)+ (s<<6)+(s>>2);return s;}};
struct Intern{unordered_map<vector<int>,int,VHash> m;int operator()(vector<int> v){auto it=m.find(v);if(it!=m.end())return it->second;int id=(int)m.size()+1; m.emplace(move(v),id);return id;}};
Intern p30,p40,p21,p31,p12,p22,p03,p13,p04;
int base(const vector<int>& t){int b=0;for(int i=0;i<(int)t.size();i++)for(int j=i+1;j<(int)t.size();j++){int status=(t[i]==t[j]?0:(abs(t[i]-t[j])<=2?1:2));b=3*b+status;}return b;}
int base2(int a,int b){return a==b?0:(abs(a-b)<=2?1:2);}
int base3(int a,int b,int c){int st0=base2(a,b),st1=base2(a,c),st2=base2(b,c);return st0*9+st1*3+st2;}
int base4(int a,int b,int c,int d){int st0=base2(a,b),st1=base2(a,c),st2=base2(a,d),st3=base2(b,c),st4=base2(b,d),st5=base2(c,d);return ((((st0*3+st1)*3+st2)*3+st3)*3+st4)*3+st5;}
int getkey(Intern& I,int bas,vector<int>&v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());v.insert(v.begin(),bas);return I(move(v));}
int main(int argc,char**argv){int MAX=argc>1?atoi(argv[1]):47;for(int n=1;n<=MAX;n++){
 vector<int> T30(n*n*n),T31(n*n*n),T21(n*n),T22(n*n),T12(n),T13(n);
 auto i3=[n](int a,int b,int c){return (a*n+b)*n+c;};
 auto i2=[n](int a,int b){return a*n+b;};
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++)T30[i3(a,b,c)]=p30(vector<int>{base3(a,b,c)});
 for(int a=0;a<n;a++)for(int b=0;b<n;b++){
   vector<int> v;v.reserve(n);for(int c=0;c<n;c++)v.push_back(T30[i3(a,b,c)]);
   T21[i2(a,b)]=getkey(p21,base2(a,b),v);
 }
 for(int a=0;a<n;a++){vector<int> v;v.reserve(n);for(int b=0;b<n;b++)v.push_back(T21[i2(a,b)]);T12[a]=getkey(p12,0,v);}
 {vector<int> v(T12);int t=getkey(p03,0,v);if(t!=min(n,11)){cerr<<"RANK3_CLASSIFICATION_FAILURE n="<<n<<" type="<<t<<"\n";return 3;}cout<<"rank3 "<<n<<" "<<t;}
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++){
  vector<int> v;v.reserve(n);for(int d=0;d<n;d++)v.push_back(p40(vector<int>{base4(a,b,c,d)}));
  T31[i3(a,b,c)]=getkey(p31,base3(a,b,c),v);
 }
 for(int a=0;a<n;a++)for(int b=0;b<n;b++){
  vector<int> v;v.reserve(n);for(int c=0;c<n;c++)v.push_back(T31[i3(a,b,c)]);
  T22[i2(a,b)]=getkey(p22,base2(a,b),v);
 }
 for(int a=0;a<n;a++){vector<int> v;v.reserve(n);for(int b=0;b<n;b++)v.push_back(T22[i2(a,b)]);T13[a]=getkey(p13,0,v);}
 {vector<int> v(T13);int t=getkey(p04,0,v);if(t!=min(n,26)){cerr<<"RANK4_CLASSIFICATION_FAILURE n="<<n<<" type="<<t<<"\n";return 4;}cout<<" rank4 "<<t<<"\n";}
 }
 if(MAX>=47)cout<<"COMPLETE_RANK_THREE_AND_FOUR_FINITE_TYPE_CHECK_PASS through_n="<<MAX<<"\n";
}
