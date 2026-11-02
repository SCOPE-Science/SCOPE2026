#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <stdexcept>
using namespace std;

static vector<uint8_t> next_state(const vector<uint8_t>& a) {
    int N=(int)a.size(); vector<uint8_t> b=a;
    for (int i=0;i<N;i++){
        int target=(a[i]+1)%3;
        bool enabled=false;
        for (int j=0;j<N;j++) {
            if(j!=i && j!=(i^1) && a[j]==target) { enabled=true;break; }
        }
        if(enabled) b[i]=target;
    }
    return b;
}
static uint64_t power(int b,int n){uint64_t a=1;while(n--)a*=b;return a;}
int main(){
  for(int n=3;n<=7;n++){
    uint64_t total=power(3,2*n);map<pair<int,int>,uint64_t> count;
    for(uint64_t id=0;id<total;id++){
       vector<uint8_t> v(2*n);uint64_t z=id;
       for(int j=0;j<2*n;j++){v[j]=z%3;z/=3;}
       vector<vector<uint8_t>> seq={v};
       for(int j=0;j<5;j++)seq.push_back(next_state(seq.back()));
       if(seq[2]!=seq[5])throw runtime_error("F5!=F2");
       int t=-1,p=0;
       for(int j=0;j<=2;j++){
           if(seq[j]==seq[j+1]){t=j;p=1;break;}
           if(seq[j]==seq[j+3]){t=j;p=3;break;}
       }
       if(t<0)throw runtime_error("no bounded class");
       count[{t,p}]++;
    }
    uint64_t four=power(4,n);
    map<pair<int,int>,uint64_t> expected;
    expected[{0,1}]=3;
    expected[{1,1}]=3*four-6*(n+1);
    expected[{2,1}]=12*n;
    expected[{1,3}]=6*n*(power(4,n-1)-2*n);
    expected[{2,3}]=12*n*(n-1);
    uint64_t subtotal=0;for(auto [k,v]:expected)subtotal+=v;
    expected[{0,3}]=total-subtotal;
    if(expected!=count){for(auto [k,v]:count)cerr<<k.first<<" "<<k.second<<" "<<v<<"\n";throw runtime_error("bad exact count");}
    cout<<"n="<<n<<" states="<<total<<" class_counts=";
    for(auto [k,v]:count)cout<<" ("<<k.first<<","<<k.second<<")="<<v;
    cout<<"\n";
  }
  cout<<"PASS independent direct vertex enumeration\n";
}
