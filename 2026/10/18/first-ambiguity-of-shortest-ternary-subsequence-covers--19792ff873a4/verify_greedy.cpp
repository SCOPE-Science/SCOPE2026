// Independent greedy-frontier s-cover certificate over ALL labeled ternary words.
// C++17: g++ -std=c++17 -O2 verify_greedy.cpp -o verify_greedy
#include <algorithm>
#include <array>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

// A position i is covered by a candidate C iff it can serve as a matched
// occurrence of some C[j], with C[0..j-1] in S[0..i-1] and C[j+1..] in S[i+1..].
// Earliest prefix / latest suffix greedy embeddings decide the two conditions.
static bool is_cover(const string& s,const string& c) {
    const int n=s.size(),m=c.size();
    vector<int> first(m),last(m);
    int pos=0;
    for(int j=0;j<m;++j){
        while(pos<n && s[pos]!=c[j]) ++pos;
        if(pos==n)return false;
        first[j]=pos++;
    }
    pos=n-1;
    for(int j=m-1;j>=0;--j){
        while(pos>=0 && s[pos]!=c[j]) --pos;
        if(pos<0)return false;
        last[j]=pos--;
    }
    for(int i=0;i<n;++i){
        bool covered=false;
        for(int j=0;j<m;++j){
            if(c[j]==s[i] && (j==0 || first[j-1]<i) &&
                               (j+1==m || i<last[j+1])) {covered=true;break;}
        }
        if(!covered)return false;
    }
    return true;
}
int main(){
    vector<string> by_ends[3][3][9];
    // Any shortest s-cover is s-primitive and has no repeated adjacent letters.
    // The published equality gamma(3)=8 bounds a ternary shortest s-cover by 8.
    for(int m=1;m<=8;++m){
        int possibilities=1;for(int i=0;i<m;++i)possibilities*=3;
        for(int raw=0;raw<possibilities;++raw){
            int v=raw;string c(m,'0');
            for(int i=m-1;i>=0;--i){c[i]=char('0'+v%3);v/=3;}
            bool reduced=true;
            for(int i=1;i<m;++i) if(c[i]==c[i-1]){reduced=false;break;}
            if(reduced)by_ends[c.front()-'0'][c.back()-'0'][m].push_back(c);
        }
    }
    for(int n=1;n<=11;++n){
        int words=1;for(int i=0;i<n;++i)words*=3;
        int ambiguous=0,unique=0;
        for(int raw=0;raw<words;++raw){
            int v=raw;string s(n,'0');
            for(int i=n-1;i>=0;--i){s[i]=char('0'+v%3);v/=3;}
            int count=1; // s is always an s-cover of itself.
            vector<string> shortest_cover_strings{s};
            for(int m=1;m<=min(n-1,8);++m){
                vector<string> covers;
                for(const auto& c:by_ends[s.front()-'0'][s.back()-'0'][m])
                    if(is_cover(s,c))covers.push_back(c);
                if(!covers.empty()){
                    count=(int)covers.size();shortest_cover_strings=covers;break;
                }
            }
            if(count==1){++unique;continue;}
            ++ambiguous;
            sort(shortest_cover_strings.begin(),shortest_cover_strings.end());
            int symbol_map[3]={-1,-1,-1}, next=0;
            string normalized_s;
            for(char letter:s){int &mapped=symbol_map[letter-'0'];
                if(mapped<0)mapped=next++;
                normalized_s+=char('0'+mapped);
            }
            vector<string> normalized_covers;
            for(const auto& c:shortest_cover_strings){
                string mapped_c;
                for(char letter:c)mapped_c+=char('0'+symbol_map[letter-'0']);
                normalized_covers.push_back(mapped_c);
            }
            sort(normalized_covers.begin(),normalized_covers.end());
            if(!(n==11 && count==2 && normalized_s=="01012021010" &&
                 normalized_covers==vector<string>{"010210","012010"}))
                throw runtime_error("unexpected cover minimizers");
            // This equality of cover sets occurs only in six alphabet relabelings.
        }
        if(ambiguous!=(n==11?6:0) || unique+ambiguous!=words)
            throw runtime_error("unexpected labeled ambiguity census");
        cout<<"length="<<n<<" words="<<words
            <<" unique_shortest="<<unique<<" ambiguous="<<ambiguous<<"\n";
    }
    cout<<"GREEDY_CERTIFICATE_PASSED\n";
}
