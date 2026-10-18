// Exact finite enumeration for binary power-spectrum reconstruction through support size six.
// Usage: c++ -O2 -std=c++17 checker.cpp -o check && ./check
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
static constexpr int N=32;
using Subset=vector<int>;
using Fibers=map<string, vector<Subset>>;
static Subset canonical(const Subset& a){
    Subset best;
    for(int z:a){
        Subset b;
        for(int x:a) b.push_back(x^z);
        sort(b.begin(),b.end());
        if(best.empty() || b<best) best=move(b);
    }
    return best;
}
static string autocorr(const Subset& a){
    string v(N, char(0));
    v[0]=char(a.size());
    for(size_t i=0;i<a.size();++i)
      for(size_t j=i+1;j<a.size();++j)
        v[a[i]^a[j]]=char(v[a[i]^a[j]]+2);
    return v;
}
static int rank_of_differences(const Subset& a){
    int pivots[5]={0},r=0;
    for(int x:a){
        int v=x^a.front();
        for(int b=4;b>=0;--b)if((v>>b)&1){
            if(pivots[b])v^=pivots[b];
            else{pivots[b]=v;++r;break;}
        }
    }
    return r;
}
static void visit(const Subset& a,Fibers& f,size_t& classes){
    if(canonical(a)!=a) return;
    ++classes;
    f[autocorr(a)].push_back(a);
}
static void recur(int next,int need,Subset& a,Fibers& f,size_t& classes){
    if(need==0){visit(a,f,classes);return;}
    for(int v=next;v<=N-need;++v){a.push_back(v);recur(v+1,need-1,a,f,classes);a.pop_back();}
}
static void ensure(bool p,const string& why){if(!p)throw runtime_error(why);}
int main(){
    try {
        for(int k=1;k<=6;++k){
            Fibers f;size_t classes=0;Subset a={0};
            recur(1,k-1,a,f,classes);
            size_t counted=0, ambiguous=0, different=0;
            for(const auto& [corr,sets]:f){
                counted+=sets.size();
                if(sets.size()<=1)continue;
                ++ambiguous;
                ensure(k==6,"collision below six points");
                ensure(sets.size()==28,"unexpected ambiguity-fiber size");
                ensure((unsigned char)corr[0]==6,"wrong autocorrelation origin");
                int nonzero=0;vector<int>support;
                for(int t=1;t<N;++t){
                    int v=(unsigned char)corr[t];
                    ensure(v==0||v==2,"unexpected nonzero difference count");
                    if(v==2){++nonzero;support.push_back(t);}
                }
                ensure(nonzero==15,"ambiguous support not a 4-flat difference set");
                for(int t:support)for(int u:support)
                    ensure(t==u || find(support.begin(),support.end(),t^u)!=support.end(),"differences not a subspace");
                for(const auto& s:sets){
                    ensure(rank_of_differences(s)==4,"ambiguous support of wrong rank");
                    int xor_total=0;
                    for(int t:s)xor_total^=t;
                    ensure(xor_total==0,"ambiguous support not a six-circuit");
                }
                different+=sets.size();
            }
            ensure(counted==classes,"enumeration discrepancy");
            if(k<=5)ensure(ambiguous==0,"not injective through five");
            if(k==6)ensure(ambiguous==31 && different==868,"not precisely the 31 four-subspaces");
            cout<<"k="<<k<<" translation_classes="<<classes
                <<" power_spectrum_fibers="<<f.size()
                <<" ambiguous_fibers="<<ambiguous
                <<" classes_in_ambiguous_fibers="<<different<<"\n";
        }
        const Subset a={0,1,2,4,8,15},b={0,1,2,4,9,14};
        ensure(a!=canonical(b),"example canonical mismatch logic");
        ensure(canonical(a)!=canonical(b),"example related by translation");
        ensure(autocorr(a)==autocorr(b),"example differs in Fourier magnitude");
        cout<<"CHECK_PASS\n";
    }catch(const exception& e){cerr<<"CHECK_FAIL "<<e.what()<<"\n";return 1;}
}
