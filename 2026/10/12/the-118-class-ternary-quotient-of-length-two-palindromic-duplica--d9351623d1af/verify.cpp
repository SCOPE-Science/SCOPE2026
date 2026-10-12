// Deterministic finite multiplication-table certificate for the ternary
// two-letter palindromic-duplication congruence.
// Build: c++ -O2 -std=c++17 -Wall -Wextra verify.cpp -o verify
// Run:   ./verify
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

struct DSU {
    vector<int> parent;
    vector<unsigned char> rank;
    explicit DSU(int n): parent(n), rank(n,0) {iota(parent.begin(),parent.end(),0);}
    int root(int v) {
        while(parent[v]!=v){parent[v]=parent[parent[v]];v=parent[v];}
        return v;
    }
    void join(int v, int w) {
        v=root(v);w=root(w);
        if(v==w)return;
        if(rank[v]<rank[w])swap(v,w);
        parent[w]=v;
        if(rank[v]==rank[w])++rank[v];
    }
};
static string word(int length,int code) {
    string s(length,'0');
    for(int i=length-1;i>=0;--i){s[i]=char('0'+code%3);code/=3;}
    return s;
}
static int number(const string& s) {
    int value=0;for(char c:s)value=3*value+(c-'0');return value;
}
static string invariant(const string& s) {
    if(s.size()<2)return string("short:")+s;
    string k="first-two:"+s.substr(0,2)+";length-parity:"+to_string(s.size()%2)+";novel:";
    bool seen[3]={false,false,false};
    for(size_t i=0;i<s.size();++i) {
        int a=s[i]-'0';
        if(!seen[a]) {seen[a]=true;k+=char('0'+a);k+=char('0'+i%2);}
    }
    return k;
}
static void require(bool b, const string& msg) {
    if(!b){cerr<<"FAIL "<<msg<<'\n';exit(1);}
}
int main() {
    constexpr int q=3, bound=14;
    array<int,bound+3> power{};
    array<int,bound+2> offset{};
    power[0]=1;
    for(int i=1;i<=bound+2;i++)power[i]=q*power[i-1];
    for(int i=1;i<=bound+1;i++)offset[i]=offset[i-1]+power[i-1];
    DSU graph(offset[bound+1]);
    long long elementary_edges=0;
    for(int length=2;length<=bound-2;length++) {
        for(int code=0;code<power[length];code++) {
            for(int at=0;at<length-1;at++) {
                // Original word: prefix a b suffix.
                // Expanded word: prefix a b b a suffix.
                int suffix_len=length-at-2;
                int prefix=code/power[suffix_len];
                int suffix=code%power[suffix_len];
                int a=(prefix/3)%3,b=prefix%3;
                int expanded=prefix*power[suffix_len+2]
                             +b*power[suffix_len+1]
                             +a*power[suffix_len]+suffix;
                graph.join(offset[length]+code,offset[length+2]+expanded);
                ++elementary_edges;
            }
        }
    }
    // The shortest representative in length-lexicographic order for each
    // attainable signature. Each has length at most 7.
    map<string,string> representative;
    for(int length=0;length<=7;length++)
        for(int code=0;code<power[length];code++) {
            string s=word(length,code);
            representative.emplace(invariant(s),s);
        }
    require(representative.size()==118,"total signature count");
    int certified=0;
    for(const auto& entry:representative) {
        for(char a='0';a<='2';a++) {
            string extended=entry.second+a;
            auto it=representative.find(invariant(extended));
            require(it!=representative.end(),"missing signature representative");
            const string& target=it->second;
            bool connected=graph.root(offset[extended.size()]+number(extended))
                          ==graph.root(offset[target.size()]+number(target));
            require(connected,"unproved right-generator transition: "+extended+" to "+target);
            ++certified;
        }
    }
    require(certified==354,"right multiplication table size");
    // The first genuinely three-symbol example uses different disjoint-
    // pair summaries, so the known pair-summary sufficiency theorem does
    // not directly give this particular equality.
    require(graph.root(offset[4]+number("0120"))==graph.root(offset[4]+number("0121")),"three-symbol test");
    const array<int,8> expected{1,3,9,21,39,51,57,57};
    for(int length=0;length<=7;length++) {
        set<string> signatures;
        for(int code=0;code<power[length];code++)
            signatures.insert(invariant(word(length,code)));
        require(int(signatures.size())==expected[length],"length-class count "+to_string(length));
    }
    // Independent finite sanity check of the invariant on every local edge
    // with source length at most 7.
    long long invariant_edges=0;
    for(int length=2;length<=7;length++)
        for(int code=0;code<power[length];code++) {
            string s=word(length,code);
            for(int at=0;at<length-1;at++) {
                string t=s.substr(0,at+2)+s[at+1]+s[at]+s.substr(at+2);
                require(invariant(s)==invariant(t),"invariant edge");
                invariant_edges++;
            }
        }
    cout<<"VERIFY_OK ternary_classes=118 table_transitions="<<certified
        <<" graph_vertices="<<offset[bound+1]
        <<" graph_edges="<<elementary_edges
        <<" invariant_edges="<<invariant_edges
        <<" stable_length_classes=57 length_bound="<<bound<<'\n';
}
