// Exact finite verification of ternary deletion-covering claims.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<string> words(int n) {
    vector<string> v;
    int sz=1; for(int i=0;i<n;i++)sz*=3;
    for(int x=0;x<sz;x++) {
        int z=x; string w(n,'0');
        for(int i=n-1;i>=0;i--){w[i]='0'+z%3;z/=3;}
        v.push_back(w);
    }
    return v;
}
set<string> shadow(const string& w) {
    set<string> out;
    int len=int(w.size())-2;
    // Positions of survivors; all choices are strictly increasing.
    if(len==2) {
        for(int i=0;i<(int)w.size();i++)for(int j=i+1;j<(int)w.size();j++)
            out.insert(string(1,w[i])+w[j]);
    } else if(len==3) {
        for(int i=0;i<(int)w.size();i++)for(int j=i+1;j<(int)w.size();j++)
          for(int k=j+1;k<(int)w.size();k++)
            out.insert(string(1,w[i])+w[j]+w[k]);
    } else if(len==4) {
        for(int i=0;i<(int)w.size();i++)for(int j=i+1;j<(int)w.size();j++)
          for(int k=j+1;k<(int)w.size();k++)for(int l=k+1;l<(int)w.size();l++)
            out.insert(string(1,w[i])+w[j]+w[k]+w[l]);
    } else assert(false);
    return out;
}
string pattern(const string& w) {
    int seen[3]={-1,-1,-1},fresh=0;string s;
    for(char c:w) {int a=c-'0';if(seen[a]==-1)seen[a]=fresh++;s+=char('0'+seen[a]);}
    return s;
}
string canon(const string& w) {
    string r=w;reverse(r.begin(),r.end());return min(pattern(w),pattern(r));
}
int main() {
    const vector<string> c4={"1201","2020"};
    const vector<string> c5={"01010","12012","12101","20202","20212"};
    const vector<string> bases={"010010","010121","010202"};
    vector<string> c6;
    for(const auto& b:bases)for(int d=0;d<3;d++) {
        string s=b;for(char& c:s)c='0'+(c-'0'+d)%3;c6.push_back(s);
    }
    for(const auto& c:vector<vector<string>>{c4,c5,c6}) {
        int n=(int)c.front().size();set<string> target;
        for(const auto& w:c) {
            auto desc=shadow(w);target.insert(desc.begin(),desc.end());
        }
        int expected=1;for(int i=0;i<n-2;i++)expected*=3;
        assert((int)target.size()==expected);
        cout<<"cover "<<n<<" "<<c.size()<<" "<<target.size()<<"\n";
    }
    // A source of length four has at most C(4,2)=6 survivors, fewer than 9.
    int max4=0;for(const auto& w:words(4))max4=max(max4,int(shadow(w).size()));
    assert(max4==6);
    cout<<"n4_single_center_max "<<max4<<"\n";

    const auto w5=words(5);
    vector<uint32_t> masks(w5.size());array<vector<int>,3> grp;
    for(int j=0;j<(int)w5.size();j++) {
        for(const auto& y:shadow(w5[j])) {
            int v=0;for(char c:y)v=3*v+(c-'0');
            masks[j] |= 1u<<v;
        }
        for(int a=0;a<3;a++)
            if(count(w5[j].begin(),w5[j].end(),char('0'+a))>=3)grp[a].push_back(j);
    }
    assert(grp[0].size()==51 && grp[1].size()==51 && grp[2].size()==51);
    int best=0; uint64_t checks=0;
    for(int a:grp[0])for(int b:grp[1])for(int c:grp[2]) {
        uint32_t m=masks[a]|masks[b]|masks[c];
        for(uint32_t d:masks) {
            int covered=__builtin_popcount(m|d);
            best=max(best,covered);++checks;
        }
    }
    assert(checks==32234193 && best==26);
    cout<<"n5_max_four_coverage "<<best<<" examined "<<checks<<"\n";

    const map<string,int> weight={{"0000",2},{"0001",2},{"0010",1},
       {"0011",1},{"0012",2},{"0101",0},{"0102",0},{"0110",1},
       {"0112",1},{"0120",1}};
    int total=0;
    for(const auto& y:words(4))total+=weight.at(canon(y));
    int largest=0;
    for(const auto& x:words(6)) {
        int z=0;for(const auto& y:shadow(x))z+=weight.at(canon(y));
        largest=max(largest,z);
    }
    assert(total==90 && largest==11);
    cout<<"n6_weight_total "<<total<<" max_shadow_weight "<<largest<<"\n";
    cout<<"verified_exact_profile 2 5 9\n";
}
