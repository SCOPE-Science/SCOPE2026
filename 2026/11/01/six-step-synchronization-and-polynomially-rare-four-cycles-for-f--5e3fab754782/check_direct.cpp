// Independent vertex-level exhaustive checker for firefly dynamics.
// Build: c++ -std=c++17 -O2 check_direct.cpp -o check_direct && ./check_direct
#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cstdint>
using namespace std;

static vector<unsigned char> next_graph(const vector<unsigned char> &x) {
    int N=(int)x.size();
    vector<unsigned char> y(N);
    for(int i=0;i<N;i++){
        if(x[i]<2) y[i]=x[i]+1;
        else {
            bool blink=false;
            for(int j=0;j<N;j++)if(i!=j && i/2!=j/2 && x[j]==1){blink=true;break;}
            y[i]=blink?2:0;
        }
    }
    return y;
}
static bool sync(const vector<unsigned char> &v) {
    for(auto z:v)if(z!=v[0])return false;
    return true;
}
static bool trap(const vector<unsigned char> &x){
    int two=0, mixed02=0,mixed12=0;
    for(int i=0;i<(int)x.size();i+=2){
        int a=x[i],b=x[i+1];
        if(a==2 && b==2)two++;
        else if((a==0&&b==2)||(a==2&&b==0))mixed02++;
        else if((a==1&&b==2)||(a==2&&b==1))mixed12++;
        else return false;
    }
    return mixed02==1 && mixed12==1;
}
static long long ipow(int x,int k){long long z=1;while(k--)z*=x;return z;}
static long long count_formula(int n,int t){
    long long a=ipow(4,n),b=ipow(4,n-1),c=ipow(9,n);
    switch(t){
    case 0:return 3;
    case 1:case 3:return a-2*n-2;
    case 2:return c-6LL*n*b-2*a+4LL*n*(n-1)+4*n+1;
    case 4:return 2*n;
    case 5:return 4LL*n*b-4LL*n*(n-1)-2*n;
    case 6:return 2LL*n*b-4LL*n*(n-1);
    }
    return -1;
}
int main(){
    long long total=0;
    for(int n=2;n<=6;n++){
        long long cats[2][7] = {};
        const long long totalstates=ipow(9,n);
        for(long long mask=0;mask<totalstates;mask++){
            vector<unsigned char> x(2*n);long long v=mask;
            for(auto &a:x){a=v%3;v/=3;}
            vector<unsigned char> y=x;
            bool caught=false;
            for(int t=0;t<=6;t++){
                if(sync(y)){
                    cats[0][t]++;
                    caught=true;
                    break;
                }
                if(t==0 && trap(y)){
                    auto z=y;
                    for(int k=0;k<4;k++)z=next_graph(z);
                    assert(z==y);
                    z=next_graph(next_graph(y));
                    assert(z!=y); // primitive 4
                    cats[1][0]++;
                    caught=true;
                    break;
                }
                y=next_graph(y);
            }
            if(!caught){cerr<<"UNCLASSIFIED n="<<n<<" state="<<mask<<"\n";return 1;}
        }
        long long sum=0;
        for(int t=0;t<=6;t++){
            assert(cats[0][t]==count_formula(n,t));sum+=cats[0][t];
        }
        assert(cats[1][0]==4LL*n*(n-1));sum+=cats[1][0];
        assert(sum==totalstates);
        total+=sum;
        cout<<"n="<<n<<" total="<<totalstates<<" period4="<<cats[1][0]
            <<" sync_t6="<<cats[0][6]<<" PASS\n";
    }
    cout<<"DIRECT_PASS: "<<total<<" labelled initial states, n=2..6\n";
}
