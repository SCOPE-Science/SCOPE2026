#include <bits/stdc++.h>
using namespace std;

static uint64_t nested_count(int n, uint64_t &poset_count) {
    vector<pair<int,int>> pairs;
    for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) pairs.push_back({i,j});
    const int m=(int)pairs.size();
    vector<uint32_t> pow3(m+1,1);
    for(int i=1;i<=m;i++) pow3[i]=pow3[i-1]*3u;
    const uint32_t N=pow3[m];
    vector<uint32_t> zeta(N,0);
    poset_count=0;
    auto valid=[&](uint32_t s){
        uint8_t row[6]={0};
        uint32_t x=s;
        for(int k=0;k<m;k++){
            int d=x%3u; x/=3u;
            if(!d) continue;
            auto [i,j]=pairs[k];
            if(d==1) row[i]|=(1u<<j); else row[j]|=(1u<<i);
        }
        for(int i=0;i<n;i++){
            uint8_t r=row[i];
            for(int j=0;j<n;j++) if(r&(1u<<j))
                if(row[j] & (uint8_t)(~r)) return false;
        }
        return true;
    };
    for(uint32_t s=0;s<N;s++) if(valid(s)){ zeta[s]=1; ++poset_count; }
    for(int k=0;k<m;k++){
        uint32_t p=pow3[k], block=3u*p;
        for(uint32_t base=0;base<N;base+=block)
            for(uint32_t off=0;off<p;off++){
                uint32_t a=base+off;
                zeta[a+p]+=zeta[a];
                zeta[a+2u*p]+=zeta[a];
            }
    }
    uint64_t total=0;
    for(uint32_t s=0;s<N;s++) if(valid(s)) total+=zeta[s];
    return total;
}

int main(){
    const uint64_t expected_posets[7]={1,1,3,19,219,4231,130023};
    const uint64_t expected_nested[7]={1,1,5,79,3221,301831,60305525};
    vector<uint64_t> a(7); a[0]=1;
    for(int n=1;n<=6;n++){
        uint64_t p=0; a[n]=nested_count(n,p);
        if(p!=expected_posets[n] || a[n]!=expected_nested[n]) return 1;
    }
    uint64_t S[7][7]={{0}}; S[0][0]=1;
    for(int n=1;n<=6;n++) for(int k=1;k<=n;k++) S[n][k]=S[n-1][k-1]+k*S[n-1][k];
    const uint64_t expected_all[7]={1,1,6,95,3731,336092,65049621};
    for(int n=1;n<=6;n++){
        uint64_t b=0; for(int k=1;k<=n;k++) b+=S[n][k]*a[k];
        if(b!=expected_all[n]) return 2;
    }
    cout << "injective: 1 1 5 79 3221 301831 60305525\n";
    cout << "all-tuples: 1 1 6 95 3731 336092 65049621\n";
    cout << "VERIFY_OK\n";
}
