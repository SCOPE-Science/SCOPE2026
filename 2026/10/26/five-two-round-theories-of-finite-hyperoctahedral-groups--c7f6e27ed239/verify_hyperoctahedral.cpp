// Direct relational atomic-extension verification for finite signed-permutation groups.
// Build: g++ -O3 -std=c++17 verify_hyperoctahedral.cpp -o verify_hyperoctahedral
// Run:   ./verify_hyperoctahedral
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Element=vector<int>;

Element multiply(const Element &a,const Element &b){
    int n=(int)a.size(); Element z(n);
    for(int i=0;i<n;i++) z[i]=(b[i]<0?-1:1)*a[abs(b[i])-1];
    return z;
}

struct CycleData {string id; int ord; bool square;};
CycleData type(const Element &a){
    int n=(int)a.size();vector<int>seen(n);vector<pair<int,int>>cycles;
    int ord=1;map<pair<int,int>,int> count;
    for(int i=0;i<n;i++) if(!seen[i]){
        int j=i,len=0,neg=0;
        do {seen[j]=1;len++;neg^=(a[j]<0);j=abs(a[j])-1;} while(j!=i);
        cycles.push_back({len,neg});count[{len,neg}]++;
        ord=lcm(ord,len*(neg?2:1));
    }
    sort(cycles.begin(),cycles.end());string s;for(auto [l,sign]:cycles)s+=to_string(l)+char('a'+sign)+",";
    bool square=true;
    for(auto [key,k]:count) if((key.second==1 || key.first%2==0) && k%2) square=false;
    return {s,ord,square};
}
int mask(const Element &v,const Element &e,const Element &x,const Element &y){
    return (v==e)|((v==x)<<1)|((v==y)<<2);
}
int atomic(const Element &e,const Element &x,const Element &x2,const Element &y){
    int t=(x==e)|((y==e)<<1)|((x==y)<<2);
    t|=mask(x2,e,x,y)<<3;
    t|=mask(multiply(y,y),e,x,y)<<6;
    t|=mask(multiply(x,y),e,x,y)<<9;
    t|=mask(multiply(y,x),e,x,y)<<12;
    return t;
}
string key(CycleData d){
    int c=d.ord<=4?d.ord:5;
    return to_string(c)+string(d.square?"S":"N");
}
int main(){
    vector<set<vector<int>>> all;
    for(int n=1;n<=6;n++){
        vector<Element> elements;
        Element p(n);iota(p.begin(),p.end(),1);
        do {for(int mask=0;mask<(1<<n);mask++){
            Element a(n);for(int i=0;i<n;i++)a[i]=((mask>>i)&1)?-p[i]:p[i];
            elements.push_back(move(a));
        }}while(next_permutation(p.begin(),p.end()));
        assert(elements.size()==(size_t)((1<<n)*([n]{int a=1;for(int j=1;j<=n;j++)a*=j;return a;}())));
        map<string,Element> reps;
        for(const auto &x:elements) {auto t=type(x);if(!reps.count(t.id))reps.emplace(t.id,x);}
        Element e(n);iota(e.begin(),e.end(),1);
        map<string,vector<int>> profile_by_key;
        set<vector<int>> profiles;
        for(auto &[label,x]:reps){
            auto d=type(x);auto x2=multiply(x,x);
            set<int> atoms;bool root=false;
            for(const auto &y:elements){atoms.insert(atomic(e,x,x2,y));if(multiply(y,y)==x)root=true;}
            assert(root==d.square); // Independently verify the signed-cycle root criterion.
            vector<int> profile(atoms.begin(),atoms.end());
            auto k=key(d);
            if(n>=5){
                if(profile_by_key.count(k))assert(profile_by_key[k]==profile);
                else profile_by_key.emplace(k,profile);
            }
            profiles.insert(move(profile));
        }
        cout << "EXACT_PROFILES_OK n="<<n<<" order="<<elements.size()
             <<" signed_cycle_types="<<reps.size()<<" pointed_profiles="<<profiles.size()<<"\n";
        if(n>=5){assert(profile_by_key.size()==8 && profiles.size()==8);
            cout<<"EIGHT_CATEGORY_REDUCTION_OK n="<<n<<"\n";
        }
        all.push_back(profiles);
    }
    for(int i=0;i<4;i++)for(int j=i+1;j<5;j++) assert(all[i]!=all[j]);
    assert(all[4]==all[5]);
    cout<<"TWO_ROUND_CLASSES_OK n=1,2,3,4,5plus count=5\n";
    cout<<"SIGNED_SQUARE_ROOT_CRITERION_OK ranks=1..6\n";
    cout<<"VERIFY_OK\n";
}
