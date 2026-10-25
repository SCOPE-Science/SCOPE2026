#include <bits/stdc++.h>
using namespace std;
int cmp(unsigned x,unsigned y){if(x==y)return 0; if((x&y)==x)return 1; if((x&y)==y)return 2; return 3;}
string theory(int n,int r){
 vector<unsigned> f;
 for(unsigned x=0;x<(1u<<n);++x) if(__builtin_popcount(x)<r || x==((1u<<n)-1)) f.push_back(x);
 vector<string> pointed;
 for(unsigned a:f){set<int> labels;
  for(unsigned b:f){unsigned mask=0;for(unsigned c:f)mask|=1u<<(4*cmp(c,a)+cmp(c,b));
   labels.insert(65536*cmp(a,b)+mask);
  }
  string s;for(int x:labels)s+=to_string(x)+",";
  pointed.push_back(s);
 }
 sort(pointed.begin(),pointed.end());pointed.erase(unique(pointed.begin(),pointed.end()),pointed.end());
 string all;for(auto &s:pointed)all+=s+"|";
 cout<<"n="<<n<<" r="<<r<<" flats="<<f.size()<<" one_types="<<pointed.size()<<" codes="<<all<<"\n";
 return all;
}
int main(){map<string,int> classes;for(int r=1;r<=6;r++) for(int n=r;n<=min(r+1,7);++n){string k=theory(n,r);if(!classes.count(k))classes[k]=classes.size()+1;} cout<<"DIRECT_CLASSES="<<classes.size()<<"\n";}
