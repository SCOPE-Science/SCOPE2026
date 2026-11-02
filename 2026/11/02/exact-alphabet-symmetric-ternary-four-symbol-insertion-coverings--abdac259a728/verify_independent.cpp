// Exact orbit-cover enumeration using base-three indexing and bit masks.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
string decode(int x, int n) { string r(n,'0'); for(int i=n-1;i>=0;--i){r[i]=char('0'+x%3); x/=3;} return r; }
int encode(const string& s) { int r=0; for(char c:s)r=3*r+c-'0';return r; }
vector<array<int,3>> permutations3(){vector<array<int,3>> v;array<int,3> a{0,1,2};do{v.push_back(a);}while(next_permutation(a.begin(),a.end()));return v;}
vector<vector<int>> make_orbits(int length){int total=1;for(int i=0;i<length;i++)total*=3;vector<int> visited(total);vector<vector<int>> out;
 for(int i=0;i<total;i++)if(!visited[i]){set<int> orb;for(auto p:permutations3()){auto s=decode(i,length);for(char &c:s)c=char('0'+p[c-'0']);orb.insert(encode(s));}vector<int> v(orb.begin(),orb.end());for(int j:v)visited[j]=1;out.push_back(v);}return out;}
int main(){auto A=make_orbits(4),B=make_orbits(5);assert(A.size()==14&&B.size()==41);assert(A[0].size()==3);for(int i=1;i<14;i++)assert(A[i].size()==6);vector<int> oi(81,-1);
 for(int i=0;i<14;i++)for(int j:A[i])oi[j]=i;
 vector<uint16_t> obs;for(auto t:B){uint16_t mask=0;for(int v:t){uint16_t x=0;string s=decode(v,5);for(int k=0;k<5;k++){auto q=s;q.erase(k,1);x|=uint16_t(1u<<oi[encode(q)]);}if(mask)assert(mask==x);mask=x;}obs.push_back(mask);}
 vector<uint16_t> sol;int lower=0;for(int mask=0;mask<8192;mask++){int n=__builtin_popcount((unsigned)mask);if(n>6)continue;uint16_t chosen=uint16_t(1|(mask<<1));bool ok=true;for(uint16_t c:obs)if(!(chosen&c)){ok=false;break;}if(ok){if(n<6)lower++;else sol.push_back(chosen);}}
 assert(lower==0&&sol.size()==37);
 vector<int> reversal(14);for(int i=0;i<14;i++){string w=decode(A[i][0],4);reverse(w.begin(),w.end());reversal[i]=oi[encode(w)];}
 set<uint16_t> ss(sol.begin(),sol.end());int fixed=0;for(uint16_t chosen:sol){uint16_t rev=0;for(int i=0;i<14;i++)if(chosen&(1<<i))rev|=uint16_t(1<<reversal[i]);assert(ss.count(rev));if(chosen==rev)fixed++;}assert(fixed==5);
 const string witness="0000 0011 0012 0021 0022 0100 0111 0122 0210 0220 1000 1011 1022 1100 1102 1111 1120 1122 1201 1220 2001 2002 2110 2112 2120 2121 2200 2211 2212 2221 2222";
 set<int> chosen;for(size_t i=0;i<witness.size();i+=5){chosen.insert(encode(witness.substr(i,4)));}assert(chosen.size()==31);
 for(int i=0;i<243;i++){string w=decode(i,5);bool found=false;for(int j=0;j<5;j++){string t=w;t.erase(j,1);if(chosen.count(encode(t)))found=true;}assert(found);}
 cout<<"independent_orbit_implementation=PASS\n"<<"source_orbits=14 target_orbits=41\n"<<"symmetric_minimum=39 number_of_optima=37\n"<<"reversal_fixed=5 reversal_pairs=16\n"<<"asymmetric_31_word_witness=PASS\n";
}
