// Independent bounded-state checker for ordinary parallel chip firing.
// Every primitive two-cycle vertex has between zero and 2 degree minus one chips.
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
using ll = long long;

vector<int> step(const vector<int>& x, const vector<vector<int>>& A, const vector<int>& d) {
    int n=x.size();vector<int> fire(n),y(n);
    for(int i=0;i<n;i++)fire[i]=(x[i]>=d[i]);
    for(int i=0;i<n;i++){
        int z=x[i]-d[i]*fire[i];
        for(int j:A[i]) z+=fire[j];
        y[i]=z;
    }
    return y;
}
ll direct(int n,int k){
    vector<vector<int>> A(n);vector<int>d(n);
    for(int i=0;i<n;i++)for(int j=0;j<n;j++){
        if(i==j)continue;
        if(i<2*k && j==(i^1))continue;
        A[i].push_back(j);
    }
    ll total=1;
    for(int i=0;i<n;i++){
        d[i]=A[i].size();
        total*=2*d[i];
    }
    ll states=0;
    vector<int>x(n);
    for(ll z=0;z<total;z++){
        ll tmp=z;
        for(int i=0;i<n;i++){
            x[i]=int(tmp%(2*d[i]));tmp/=(2*d[i]);
        }
        auto y=step(x,A,d);
        if(y==x)continue;
        if(step(y,A,d)==x)states++;
    }
    if(states%2)throw 1;
    return states/2;
}
int main(){
    const ll truth[7][4]={
        {0,0,0,0},{0,0,0,0},{0,0,0,0},
        {6,2,0,0},{60,30,18,0},{740,444,276,0},{11160,7440,5020,3400}
    };
    ll checked=0;
    for(int n=3;n<=6;n++)for(int k=0;k<=n/2;k++){
        ll total=1;
        for(int i=0;i<n;i++)total*=2*(n-1-(i<2*k));
        checked+=total;
        ll v=direct(n,k);
        if(v!=truth[n][k]){
            cerr<<"FAILED "<<n<<" "<<k<<" "<<v<<" expected "<<truth[n][k]<<"\n";
            return 1;
        }
        cout<<"n="<<n<<" k="<<k<<" primitive_two_orbits="<<v<<" PASS\n";
    }
    cout<<"ALL PASSED: "<<checked<<" bounded labelled chip vectors tested\n";
}
