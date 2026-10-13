// Replays disjoint-output certificates for odd alphabet sizes.
// Compile: c++ -std=c++17 -O2 verify_modular_grain.cpp -o verify_modular_grain
// Run: ./verify_modular_grain
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using Word=array<int,4>;

vector<Word> make_code(int q) {
    vector<Word> code;
    for(int a=0;a<q;a++) {
        code.push_back({a,a,a,a});
        for(int b=0;b<q;b++) if(b!=a)
            for(int c=0;c<q;c++) code.push_back({a,b,c,(2*b-c+q)%q});
    }
    return code;
}
void test(int q) {
    auto code=make_code(q);
    assert((int)code.size()==q*q*q-q*q+q);
    map<Word,int> receiver;
    for(int k=0;k<(int)code.size();k++){
        Word x=code[k];
        for(int j=0;j<4;j++){
            Word y=x;
            if(j>0)y[j]=x[j-1];
            auto it=receiver.find(y);
            assert(it==receiver.end() || it->second==k);
            receiver[y]=k;
        }
    }
    cout << "CHECK q=" << q << " words=" << code.size()
         << " disjoint_outputs=" << receiver.size() << "\n";
}
int main(){for(int q: {3,5,7,9,11})test(q);cout<<"VERIFICATION_OK\n";}
