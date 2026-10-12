#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

static bool append_squarefree(const string& w, char c) {
    string q=w; q.push_back(c);
    int n=(int)q.size();
    for (int h=1; 2*h<=n; ++h)
        if (q.compare(n-2*h,h,q,n-h,h)==0) return false;
    return true;
}
static bool circular_squarefree(const string& w) {
    int n=(int)w.size();
    string ww=w+w;
    for (int i=0;i<n;++i)
        for (int h=1;2*h<=n;++h)
            if (ww.compare(i,h,ww,i+h,h)==0) return false;
    return true;
}
static string inserted(const string& w,int p,char c) {
    return w.substr(0,p)+string(1,c)+w.substr(p);
}
static string canon_rotation(const string& w) {
    string best=w;
    for (int i=1;i<(int)w.size();++i) {
        string q=w.substr(i)+w.substr(0,i);
        if (q<best) best=q;
    }
    return best;
}
static string relabel(const string& w,const array<char,3>& p) {
    string q=w;
    for(char& c:q) c=p[c-'0'];
    return q;
}
int main() {
    const vector<long long> expected={
        1,3,6,12,18,30,42,60,78,108,144,204,264,342,456,618,798,1044,
        1392,1830,2388,3180,4146,5418,7032,9198,11892,15486,20220,26424,
        34422,44862,58446,76122,99276,129516,168546,219516
    };
    vector<vector<string>> levels(38);
    levels[0].push_back("");
    for(int n=1;n<=37;++n) {
        for(const string& w:levels[n-1])
            for(char c='0';c<='2';++c)
                if(append_squarefree(w,c)) levels[n].push_back(w+string(1,c));
        if((long long)levels[n].size()!=expected[n]) return 10+n;
    }

    vector<string> c36,c37;
    for(const auto& w:levels[36]) if(circular_squarefree(w)) c36.push_back(w);
    for(const auto& w:levels[37]) if(circular_squarefree(w)) c37.push_back(w);
    if(c36.size()!=16416 || c37.size()!=18870) return 50;

    // Engine A: insertion membership in the independently enumerated length-37 circular language.
    unordered_set<string> s37(c37.begin(),c37.end());
    vector<string> A;
    for(const auto& w:c36) {
        bool ext=true;
        for(int p=0;p<36 && ext;++p) for(char c='0';c<='2';++c)
            if(s37.count(inserted(w,p,c))) { ext=false; break; }
        if(ext) A.push_back(w);
    }

    // Engine B: direct circular-square test on every insertion.
    vector<string> B;
    for(const auto& w:c36) {
        bool ext=true;
        for(int p=0;p<36 && ext;++p) for(char c='0';c<='2';++c)
            if(circular_squarefree(inserted(w,p,c))) { ext=false; break; }
        if(ext) B.push_back(w);
    }
    if(A!=B || A.size()!=540) return 51;

    set<string> classes;
    for(const auto& w:A) classes.insert(canon_rotation(w));
    if(classes.size()!=15) return 52;

    // Every circular-square-free word is primitive: a nontrivial exact power
    // would contain a square. Thus every class has exactly 36 rotations.
    for(const auto& w:classes) {
        set<string> rots;
        for(int i=0;i<36;++i) rots.insert(w.substr(i)+w.substr(0,i));
        if(rots.size()!=36) return 53;
    }

    vector<array<char,3>> perms;
    array<char,3> p={'0','1','2'};
    do { perms.push_back(p); } while(next_permutation(p.begin(),p.end()));

    set<string> remaining=classes;
    vector<int> orbit_sizes;
    vector<string> orbit_reps;
    while(!remaining.empty()) {
        string w=*remaining.begin();
        set<string> orb;
        for(const auto& pm:perms) {
            string q=relabel(w,pm);
            orb.insert(canon_rotation(q));
            reverse(q.begin(),q.end());
            orb.insert(canon_rotation(q));
        }
        set<string> in;
        for(const auto& q:orb) if(classes.count(q)) in.insert(q);
        orbit_sizes.push_back((int)in.size());
        orbit_reps.push_back(*in.begin());
        for(const auto& q:in) remaining.erase(q);
    }
    sort(orbit_sizes.begin(),orbit_sizes.end());
    if(orbit_sizes!=vector<int>({3,6,6})) return 54;

    const vector<string> expected_reps={
        "010201202101201020121021202101210212",
        "010201202102010210120102012102010212",
        "010210120102120121020120210201210212"
    };
    sort(orbit_reps.begin(),orbit_reps.end());
    if(orbit_reps!=expected_reps) return 55;

    cout<<"VERIFY_OK linear36=168546 linear37=219516 circular36=16416 circular37=18870 "
        <<"extremal_linear36=540 circular_classes=15 symmetry_orbits=3 orbit_sizes=3,6,6 engines=2\n";
    return 0;
}
