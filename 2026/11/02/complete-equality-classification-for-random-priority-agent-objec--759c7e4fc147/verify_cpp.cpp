// Exhaustive exact-arithmetic certificate for the four-agent, three-object
// random-serial-dictatorship agent-object waste boundary.
// Public scientific data; no external dependencies beyond ISO C++17.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Pref = array<int,4>; // 0,1,2 are objects; -1 is the outside option
using Profile = array<int,4>; // indices into the lexicographic list of rankings

int main() {
    vector<Pref> types;
    Pref p{-1,0,1,2};
    do { types.push_back(p); } while (next_permutation(p.begin(),p.end()));
    vector<Pref> orders;
    Pref pi{0,1,2,3};
    do { orders.push_back(pi); } while (next_permutation(pi.begin(),pi.end()));
    assert(types.size()==24 && orders.size()==24);

    array<long long,25> histogram{};
    set<Profile> extremals;
    for(int a=0;a<24;++a) for(int b=0;b<24;++b)
    for(int c=0;c<24;++c) for(int d=0;d<24;++d) {
        Profile profile{a,b,c,d};
        int unassigned_agent[4]{};
        int unassigned_object[3]{};
        for(const auto &order:orders) {
            int used=0;
            for(int i:order) {
                int obj=-1;
                for(int x:types[profile[i]]) {
                    if(x==-1) break;
                    if(!(used&(1<<x))) { obj=x; break; }
                }
                if(obj<0) ++unassigned_agent[i];
                else used|=(1<<obj);
            }
            for(int x=0;x<3;++x) if(!(used&(1<<x))) ++unassigned_object[x];
        }
        int w=0, n_witnesses=0;
        for(int i=0;i<4;++i) for(int x:types[profile[i]]) {
            if(x==-1) break;
            w=max(w,min(unassigned_agent[i],unassigned_object[x]));
        }
        for(int i=0;i<4;++i) for(int x:types[profile[i]]) {
            if(x==-1) break;
            if(w>0 && min(unassigned_agent[i],unassigned_object[x])==w) ++n_witnesses;
        }
        assert(w<=24);
        ++histogram[w];
        if(w==4) {
            assert(n_witnesses==1);
            extremals.insert(profile);
        }
    }
    assert(extremals.size()==432);

    // Quotient by all agent and object relabelings, using exact orbit formation.
    map<Pref,int> index;
    for(int i=0;i<24;++i) index[types[i]]=i;
    set<Profile> unseen=extremals;
    vector<pair<Profile,int>> orbit_reps;
    do {
        Profile rep=*unseen.begin();
        set<Profile> orbit;
        Pref agents{0,1,2,3};
        do {
            array<int,3> objects{0,1,2};
            do {
                Profile transformed{};
                for(int k=0;k<4;++k) {
                    Pref renamed{};
                    for(int t=0;t<4;++t) {
                        int x=types[rep[agents[k]]][t];
                        renamed[t]=(x<0?-1:objects[x]);
                    }
                    transformed[k]=index.at(renamed);
                }
                orbit.insert(transformed);
            } while(next_permutation(objects.begin(),objects.end()));
        } while(next_permutation(agents.begin(),agents.end()));
        for(const auto &v:orbit) {
            assert(unseen.erase(v)==1);
        }
        assert(orbit.size()==72);
        orbit_reps.push_back({rep,(int)orbit.size()});
    } while(!unseen.empty());
    assert(orbit_reps.size()==6);
    // The exact normal forms are verified, rather than merely printing them.
    const vector<array<string,4>> normal_forms = {
      {"ab_c","ab_c","ac_b","bac_"},
      {"ab_c","ab_c","ac_b","bc_a"},
      {"ab_c","ab_c","ac_b","bca_"},
      {"ab_c","ab_c","acb_","bac_"},
      {"ab_c","ab_c","acb_","bc_a"},
      {"ab_c","ab_c","acb_","bca_"}
    };
    set<array<string,4>> expected_reps(normal_forms.begin(),normal_forms.end());
    set<array<string,4>> obtained_reps;
    for(const auto &q:orbit_reps) {
        array<string,4> norm{};
        for(int i=0;i<4;++i) for(int x:types[q.first[i]])
            norm[i].push_back(x<0?'_':char('a'+x));
        obtained_reps.insert(norm);
    }
    assert(obtained_reps==expected_reps);

    const array<long long,5> expected{317664,1728,5040,6912,432};
    for(int i=0;i<=4;++i) assert(histogram[i]==expected[i]);
    for(int i=5;i<=24;++i) assert(histogram[i]==0);

    cout<<"VERIFY_CPP_OK profiles=331776 priority_orders_per_profile=24";
    for(int i=0;i<=4;++i) cout<<" w"<<i<<"="<<histogram[i];
    cout<<" extremal_orbits="<<orbit_reps.size()<<" orbit_sizes=";
    for(auto &q:orbit_reps) cout<<q.second<<",";
    cout<<"\n";
    for(auto &q:orbit_reps) {
        cout<<"ORBIT "<<q.second;
        for(int i:q.first) {
            cout<<" ";
            for(int x:types[i]) cout<<(x<0?'_':char('a'+x));
        }
        cout<<"\n";
    }
}
