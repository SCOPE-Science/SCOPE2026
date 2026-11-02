// Independent finite verification of minimum dominating-set classification for F_2(K_{3,n}).
// Build: c++ -std=c++17 -O3 verify_minimum_token_domination.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;
using U = uint64_t;
struct Check {
    int n, nv;
    vector<pair<int,int>> p;
    vector<U> closed;
    explicit Check(int size): n(size), nv((size+3)*(size+2)/2) {
        for (int i=0;i<n+3;i++) for(int j=i+1;j<n+3;j++) p.push_back({i,j});
        assert((int)p.size()==nv && nv<64);
        closed.resize(nv);
        for(int k=0;k<nv;k++) {
            closed[k]=U(1)<<k;
            for(int j=0;j<nv;j++) {
                const auto [a,b]=p[k]; const auto [c,d]=p[j];
                int shared=(a==c)+(a==d)+(b==c)+(b==d);
                if(shared!=1)continue;
                int x=(a==c||a==d)?b:a;
                int y=(c==a||c==b)?d:c;
                if ((x<3)!=(y<3)) closed[k]|=U(1)<<j;
            }
        }
    }
    bool dominates(U mask) const {
        U d=0;
        for(U a=mask;a;a&=a-1) d|=closed[__builtin_ctzll(a)];
        return d==((U(1)<<nv)-1);
    }
    int family(U mask) const {
        vector<pair<int,int>> aa,bb,ab;
        for(U a=mask;a;a&=a-1){auto q=p[__builtin_ctzll(a)];
            if(q.second<3)aa.push_back(q);
            else if(q.first>=3)bb.push_back(q);
            else ab.push_back(q);
        }
        if(aa.size()==1 && bb.size()==1 && (int)ab.size()==n-2){
            const auto [u,v]=aa[0];
            int lone=3-u-v; // since A={0,1,2}
            int b0=bb[0].first,b1=bb[0].second;
            bool valid=true;
            for(int b=3;b<n+3;b++){
                if(b==b0||b==b1)continue;
                if(find(ab.begin(),ab.end(),make_pair(lone,b))==ab.end())valid=false;
            }
            if(valid)return 1;
        }
        if(n==4 && aa.empty() && bb.size()==2 && ab.size()==2){
            if(bb[0].first==bb[1].first||bb[0].first==bb[1].second||bb[0].second==bb[1].first||bb[0].second==bb[1].second)return 0;
            int j=ab[0].second,k=ab[1].second;
            if(j==k || ab[0].first==ab[1].first)return 0;
            // The B-B pair disjoint from {j,k} must be present.
            vector<int> omitted;
            for(int b=3;b<7;b++)if(b!=j&&b!=k)omitted.push_back(b);
            if (find(bb.begin(),bb.end(),make_pair(omitted[0],omitted[1]))!=bb.end()) return 2;
        }
        return 0;
    }
    void verify() const {
        U stop=(U(1)<<nv);
        long long counts[3]={0,0,0};
        for(U mask=(U(1)<<n)-1;mask<stop&&mask;){
            if(dominates(mask)){
                int f=family(mask);
                if(f==0){ cerr<<"UNCLASSIFIED n="<<n<<" mask="<<mask<<"\n";exit(2);}
                counts[f]++;
            }
            U bit=mask & (~mask+1),r=mask+bit;
            if(!r)break;
            mask=(((r^mask)>>2)/bit)|r;
        }
        long long ordinary=3LL*n*(n-1)/2;
        assert(counts[1]==ordinary);
        assert(counts[2]==(n==4?36:0));
        cout<<"n="<<n<<" ordinary="<<counts[1]<<" exceptional="<<counts[2]<<" total="<<counts[1]+counts[2]<<"\n";
    }
};
int main(){
    for(int n=3;n<=7;n++)Check(n).verify();
    cout<<"VERIFY_OK complete_enumeration_n=3..7 with exact family classification\n";
}
