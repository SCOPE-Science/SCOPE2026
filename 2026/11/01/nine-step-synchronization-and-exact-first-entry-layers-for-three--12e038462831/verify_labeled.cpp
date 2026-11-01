// Independent labelled-state check for three-color firefly dynamics on two
// cliques joined by a distinguished bridge. No symbolic quotient is used.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
using namespace std;

static const int COEFF[10][3][3] = {
 {{3,0,0},{0,0,0},{0,0,0}},
 {{8,6,0},{6,4,0},{0,0,0}},
 {{10,17,10},{17,25,15},{10,15,9}},
 {{8,6,0},{6,4,0},{0,0,0}},
 {{4,1,0},{1,0,0},{0,0,0}},
 {{12,10,3},{10,8,2},{3,2,0}},
 {{8,8,4},{8,6,2},{4,2,0}},
 {{4,5,0},{5,4,0},{0,0,0}},
 {{12,14,7},{14,12,4},{7,4,0}},
 {{12,14,3},{14,18,4},{3,4,0}}
};
long long w(int k, int n) {
    long long val=0;
    // Integer onto-map counts for three possible cohort sizes.
    for (int x=0; x<(1<<k); ++x) {
        int bits=__builtin_popcount((unsigned)x);
        long long pow=1;
        for(int t=0;t<n;t++) pow*=bits;
        val+= ((k-bits)&1) ? -pow : pow;
    }
    return val;
}
vector<unsigned char> fire(const vector<unsigned char>& x,int a,int b){
    int n=a+b;
    vector<unsigned char> y(n);
    for(int i=0;i<n;i++){
        bool blinking=false;
        for(int j=0;j<n;j++){
            if(i==j) continue;
            bool edge=(i<a && j<a) || (i>=a && j>=a) ||
                      (i==0 && j==a) || (i==a && j==0);
            if(edge && x[j]==1) blinking=true;
        }
        y[i]=(x[i]==2 && blinking)?2:(x[i]+1)%3;
    }
    return y;
}
bool sync(const vector<unsigned char>& x){for(auto c:x)if(c!=x[0])return false;return true;}
int main(){
    long long checked=0;
    for(int a=2;a<=6;a++)for(int b=2;b<=6;b++) {
        int n=a+b;
        long long all=1;
        for(int j=0;j<n;j++)all*=3;
        array<long long,10> actual{};
        for(long long index=0;index<all;index++){
            vector<unsigned char> x(n);
            long long z=index;
            for(int i=0;i<n;i++) {x[i]=z%3; z/=3;}
            int t=0;
            while(!sync(x) && t<=9){x=fire(x,a,b);t++;}
            assert(t<=9 && sync(x));
            actual[t]++;
            checked++;
        }
        for(int t=0;t<=9;t++){
            long long expected=0;
            for(int i=0;i<3;i++)for(int j=0;j<3;j++)
                expected+=COEFF[t][i][j]*w(i+1,a-1)*w(j+1,b-1);
            if(actual[t]!=expected) {
                cerr<<"FAIL "<<a<<" "<<b<<" time "<<t
                    <<" actual "<<actual[t]<<" expected "<<expected<<"\n";
                return 1;
            }
        }
        assert(actual[9]>0);
    }
    cout<<"LABELLED_OK: "<<checked<<" labelled configurations, "
        <<25<<" graph sizes, a,b=2..6\n";
}
