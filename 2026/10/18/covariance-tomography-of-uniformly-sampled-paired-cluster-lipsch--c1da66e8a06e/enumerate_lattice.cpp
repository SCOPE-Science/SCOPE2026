#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
using namespace std;
using int128=__int128_t;
struct Counts{int128 n=0, sw=0,sb=0;};
string s128(int128 x){if(!x)return "0"; bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
Counts count_case(int m,int q,int r){
 Counts o;
 vector<array<int,2>> pairs;
 for(int a=-q;a<=q;a++)for(int b=max(-q,a-r);b<=min(q,a+r);b++) pairs.push_back({a,b});
 for(int x1=-r;x1<=r;x1++){
  int low=min(0,x1),high=max(0,x1);
  if(m==2){
   for(auto ab:pairs){int lo=min({low,ab[0],ab[1]}),hi=max({high,ab[0],ab[1]});if(hi-lo>q)continue;
    int v=x1-ab[0]-ab[1];o.n++;o.sw+=(int128)x1*x1;o.sb+=(int128)v*v;
   }
  }else if(m==3){
   for(auto ab:pairs){int lo=min({low,ab[0],ab[1]}),hi=max({high,ab[0],ab[1]});if(hi-lo>q)continue;
    for(auto cd:pairs){int ll=min({lo,cd[0],cd[1]}),hh=max({hi,cd[0],cd[1]});if(hh-ll>q)continue;
     int v=x1-ab[0]-ab[1];o.n++;o.sw+=(int128)x1*x1;o.sb+=(int128)v*v;
    }
   }
  }
 }
 return o;
}
int main(int argc,char**argv){int m=stoi(argv[1]),a=stoi(argv[2]),b=stoi(argv[3]);int d=2*m-1;
 for(int k=0;k<=d+2;k++){int q=b*k,r=a*k;Counts c=count_case(m,q,r);cout<<k<<" "<<s128(c.n)<<" "<<s128(c.sw)<<" "<<s128(c.sb)<<"\n";}
}
