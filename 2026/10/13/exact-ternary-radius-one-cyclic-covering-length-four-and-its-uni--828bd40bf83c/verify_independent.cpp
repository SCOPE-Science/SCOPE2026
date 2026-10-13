#include <bits/stdc++.h>
using namespace std; using U=uint64_t;
struct B{U lo=0,hi=0;}; B ball[81];
B unite(B x,B y){return {x.lo|y.lo,x.hi|y.hi};}
int pc(B s){return __builtin_popcountll(s.lo)+__builtin_popcountll(s.hi);}
string canonical(const string &s){int m=s.size();string best(50,'9');int perm[]={0,1,2};do{for(int dir=0;dir<2;dir++){string t;for(char c:s)t+=char('0'+perm[c-'0']);if(dir)reverse(t.begin(),t.end());for(int r=0;r<m;r++){string x=t.substr(r)+t.substr(0,r);if(x<best)best=x;}}}while(next_permutation(perm,perm+3));return best;}
int main(){for(int w=0;w<81;w++)for(int t=0;t<81;t++){int a=w,b=t,d=0;for(int j=0;j<4;j++){if(a%3!=b%3)d++;a/=3;b/=3;}if(d<=1){if(t<64)ball[w].lo|=1ull<<t;else ball[w].hi|=1ull<<(t-64);}}
for(int m=9;m<=12;m++){uint64_t lim=1;for(int j=0;j<m;j++)lim*=3;long long covers=0;int maxcoverage=0;string ex;map<string,int> classes;int countUnique=0;for(uint64_t z=0;z<lim;z++){int a[20];string s(m,'0');uint64_t v=z;for(int j=0;j<m;j++){a[j]=v%3;s[j]='0'+a[j];v/=3;}B seen;for(int j=0;j<m;j++){int id=0;for(int k=0;k<4;k++)id=3*id+a[(j+k)%m];seen=unite(seen,ball[id]);}int k=pc(seen);maxcoverage=max(k,maxcoverage);if(k==81){covers++;if(ex.empty())ex=s;if(m==12) classes[canonical(s)]++;}}cerr<<"m="<<m<<" exhaustive="<<lim<<" covers="<<covers<<" max_covered="<<maxcoverage<<" first="<<ex<<" classes="<<classes.size()<<"\n";if(m==12){for(auto &[c,n]:classes) cout<<c<<" "<<n<<"\n";}}
}
