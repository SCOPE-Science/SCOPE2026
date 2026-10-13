#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// A factor has exponent at least 8/3 iff some period p supports a
// subfactor of length ceil(8p/3).  Testing only that threshold length
// is therefore exact.
static bool periodic(const string& w,int a,int L,int p){
    for(int i=a+p;i<a+L;i++) if(w[i]!=w[i-p]) return false;
    return true;
}
static bool bad_direct(const string& w){
    int n=(int)w.size();
    for(int a=0;a<n;a++){
        for(int p=1;;p++){
            int L=(8*p+2)/3;
            if(a+L>n) break;
            if(periodic(w,a,L,p)) return true;
        }
    }
    return false;
}
// Independent definition-level check: compute the least period of every factor.
static bool bad_minperiod(const string& w){
    int n=(int)w.size();
    for(int a=0;a<n;a++) for(int b=a+1;b<=n;b++){
        int L=b-a, mp=L;
        for(int p=1;p<=L;p++){
            bool ok=true;
            for(int i=a+p;i<b;i++) if(w[i]!=w[i-p]){ok=false;break;}
            if(ok){mp=p;break;}
        }
        if(3*L>=8*mp) return true;
    }
    return false;
}
static bool append_free(const string& s,char bit){
    string w=s; w.push_back(bit); int n=(int)w.size();
    // Since s is free, a new forbidden factor must be a suffix.
    for(int p=1;;p++){
        int L=(8*p+2)/3;
        if(L>n) break;
        if(periodic(w,n-L,L,p)) return false;
    }
    return true;
}
static bool extremal_direct(const string& w){
    if(bad_direct(w)) return false;
    for(int pos=0;pos<=(int)w.size();pos++) for(char b: {'0','1'}){
        string z=w.substr(0,pos)+b+w.substr(pos);
        if(!bad_direct(z)) return false;
    }
    return true;
}
int main(){
    const vector<long long> expected={2,4,6,10,16,24,36,50,72,102,142,202,282,384,536,744,1026,1414,1944,2688,3704,5106,7046,9704,13372,18416,25334,34880,48020,66102};
    const string A="011011001101100110010011001001";
    const string B="100100110010011001101100110110";
    vector<string> cur(1,"");
    vector<string> e30;
    for(int n=1;n<=30;n++){
        vector<string> nxt; nxt.reserve(cur.size()*2);
        for(const string& s:cur) for(char b: {'0','1'}) if(append_free(s,b)) nxt.push_back(s+b);
        cur.swap(nxt);
        assert((long long)cur.size()==expected[n-1]);
        long long ecount=0;
        for(const string& s:cur){
            // Cross-check the optimized suffix generation against a direct test.
            assert(!bad_direct(s));
            if(extremal_direct(s)){ecount++; if(n==30) e30.push_back(s);}
        }
        if(n<30) assert(ecount==0);
        else assert(ecount==2);
    }
    assert(e30.size()==2 && e30[0]==A && e30[1]==B);
    string rev=A, comp=A;
    reverse(rev.begin(),rev.end());
    for(char& c:comp) c=(c=='0'?'1':'0');
    assert(rev==B && comp==B);
    // Definition-level independent check on both witnesses and all 124 insertions.
    for(const string& s: e30){
        assert(!bad_minperiod(s));
        for(int pos=0;pos<=(int)s.size();pos++) for(char b: {'0','1'}){
            string z=s.substr(0,pos)+b+s.substr(pos);
            assert(bad_minperiod(z));
        }
    }
    cout << "VERIFY_OK shortest=30 free30=66102 extremal30=2 symmetry_orbits=1" << '\n';
}
