#include <bits/stdc++.h>
using namespace std;

set<string> deletion_ball(const string& x) {
    const int n=(int)x.size();
    set<string> out;
    for(int a=0;a+1<n;a++) {
        for(int b=a+2;b+1<n;b++) {
            string y;
            for(int k=0;k<n;k++) if(!(a<=k&&k<a+2)&&!(b<=k&&k<b+2)) y+=x[k];
            out.insert(y);
        }
    }
    return out;
}

string bits(int n,int value) {
    string x(n,'0');
    for(int k=0;k<n;k++) x[k] = (value&(1<<(n-k-1)))?'1':'0';
    return x;
}

void check_code(const vector<string>& code,int n,bool complete=false) {
    set<string> all;
    for(const string& w:code) {
        if((int)w.size()!=n) abort();
        auto b=deletion_ball(w);
        for(const string& y:b) if(!all.insert(y).second) abort();
    }
    if(complete && (int)all.size()!=(1<<(n-4))) abort();
}

int main() {
    for(int n=5;n<=9;n++) {
        for(int v=0;v<(1<<n);v++) {
            string x=bits(n,v);
            auto B=deletion_ball(x);
            bool hit=false;
            for(const string& y:B) {
                bool good=true;
                if(n==7) good=(y[0]==y[2]);
                if(n==8) good=(y[0]==y[2]&&y[1]==y[3]);
                if(n==9) good=(y[0]==y[2]&&y[2]==y[4]);
                hit|=good;
            }
            if(!hit) abort();
        }
    }
    check_code({"00000","11111"},5);
    for(int n=6;n<=8;n++) {
        vector<string> C;
        for(int a=0;a<2;a++) for(int b=0;b<2;b++) {
            string w;
            for(int i=0;i<n;i++) w+=char('0'+((i%2)?b:a));
            C.push_back(w);
        }
        check_code(C,n);
    }
    const array<string,3> G={"100000111","010101010","001010010"};
    vector<string> C;
    for(int v=0;v<8;v++) {
        string w(9,'0');
        for(int i=0;i<9;i++) {
            int t=0;
            for(int j=0;j<3;j++) t^=(((v>>j)&1) && G[j][i]=='1');
            w[i]=char('0'+t);
        }
        C.push_back(w);
    }
    set<string> unique(C.begin(),C.end());
    if(unique.size()!=8) abort();
    check_code(C,9,true);
    cout<<"VERIFY_OK"<<endl;
}
