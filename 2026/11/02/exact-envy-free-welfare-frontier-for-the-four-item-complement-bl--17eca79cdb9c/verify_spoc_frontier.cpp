// Exact independent small-instance enumeration for a family of binary pair-complement utilities.
// Compile: c++ -std=c++17 -O2 verify_spoc_frontier.cpp -o verifier && ./verifier
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int valuation(const vector<int>& a, int target, int player, int t, int omitted=-1) {
    int total=0;
    for(int s=0;s<t;s++) {
        int z=4*s;
        if(player==0) {
            if(a[z]==target && a[z+2]==target && z!=omitted && z+2!=omitted) total++;
            if(a[z+1]==target && a[z+3]==target && z+1!=omitted && z+3!=omitted) total++;
        } else if(a[z]==target && a[z+1]==target && z!=omitted && z+1!=omitted) total++;
    }
    return total;
}
int main(){
    long long all_cases=0;
    for(int n=2;n<=4;n++) for(int t=1;t<=(n==2?5:(n==3?3:2));t++) {
        int m=4*t;
        unsigned long long total=1;
        for(int k=0;k<m;k++)total*=n;
        vector<int> a(m,0);
        int bestEF=-1,bestEFX=-1,bestL[4]={-1,-1,-1,-1};
        for(unsigned long long code=0;code<total;code++) {
            unsigned long long v=code;
            for(int k=0;k<m;k++){a[k]=v%n;v/=n;}
            int u[4][4]={{0}};
            int w=0;
            for(int i=0;i<n;i++)for(int j=0;j<n;j++){
                u[i][j]=valuation(a,j,i,t);
                if(i==j)w+=u[i][j];
            }
            bool ef=true,efx=true,L[4]={true,true,true,true};
            for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){
                if(u[i][i]<u[i][j])ef=false;
                for(int g=0;g<m;g++) if(a[g]==j && u[i][i]<valuation(a,j,i,t,g))efx=false;
                for(int ell=1;ell<=3;ell++){
                    // For each observer, desired complementary pairs are disjoint:
                    // one removed item destroys at most one completed pair.
                    if(u[i][i]<max(0,u[i][j]-ell))L[ell]=false;
                }
            }
            if(ef)bestEF=max(bestEF,w);
            if(efx)bestEFX=max(bestEFX,w);
            for(int ell=1;ell<=3;ell++)if(L[ell])bestL[ell]=max(bestL[ell],w);
        }
        int expected=t+t/n;
        if(bestEF!=expected||bestEFX!=expected){
            cerr<<"FAIL EF/EFX n="<<n<<" t="<<t<<" observed "<<bestEF<<","<<bestEFX<<" expected "<<expected<<"\n";return 1;
        }
        for(int ell=1;ell<=3;ell++){
            int target=t+min(t,(t+(n-1)*ell)/n);
            if(bestL[ell]!=target){cerr<<"FAIL EF-l n="<<n<<" t="<<t<<" ell="<<ell<<" observed "<<bestL[ell]<<" expected "<<target<<"\n";return 1;}
        }
        all_cases+=total;
        cout<<"OK n="<<n<<" t="<<t<<" complete_allocations="<<total<<" EF="<<bestEF<<" EFX="<<bestEFX<<" EF1="<<bestL[1]<<" EF2="<<bestL[2]<<" EF3="<<bestL[3]<<"\n";
    }
    cout<<"VERIFY_OK complete_allocations="<<all_cases<<"\n";
}
