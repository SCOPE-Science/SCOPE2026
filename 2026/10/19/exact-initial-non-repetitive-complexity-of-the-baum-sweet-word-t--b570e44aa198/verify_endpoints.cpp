#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
// Direct base-two digit run criterion, not substitution.
int digit_bit(int x){if(x==0)return 1;bool in_zero=false;int zero_run=0;while(x){if(x&1){if(zero_run&1)return 0;zero_run=0;}else ++zero_run;x>>=1;}return !(zero_run&1);}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: verify_endpoints N profile.csv\n";return 2;}
 const int M=stoi(argv[1]), L=4*M+2;
 string s(L,'0');for(int i=0;i<L;i++)s[i]=char('0'+digit_bit(i));
 const U B=11400714819323198485ull;
 vector<U> pref(L+1),power(L+1);power[0]=1;
 for(int i=0;i<L;i++){pref[i+1]=pref[i]*B+U(s[i]-'0'+1);power[i+1]=power[i]*B;}
 auto hash=[&](int i,int n)->U{return pref[i+n]-pref[i]*power[n];};
 auto first_repeat=[&](int n)->pair<int,int>{
   unordered_map<U,vector<int>> d;d.reserve(4*M);
   for(int j=0;j<3*M+1;j++){
     if(j+n>L)throw runtime_error("prefix too short");
     U h=hash(j,n);auto& x=d[h];
     for(int i:x) if(memcmp(s.data()+i,s.data()+j,n)==0)return {j,i};
     x.push_back(j);
   }
   throw runtime_error("no repetition through 3*M");
 };
 ifstream in(argv[2]);string line;getline(in,line);
 int previous_end=0, count=0;vector<array<int,4>> intervals;
 while(getline(in,line)){
   if(line.empty())continue;replace(line.begin(),line.end(),',',' ');istringstream f(line);
   int a,b,r,p;if(!(f>>a>>b>>r>>p))return 3;
   if(a!=previous_end+1||a>b||b>M)return 4;
   for(int n: {a,b}){
     auto actual=first_repeat(n);
     if(actual!=make_pair(r,p)){
       cerr<<"MISMATCH at n="<<n<<" found ("<<actual.first<<","<<actual.second<<") expected ("<<r<<","<<p<<")\n";return 5;
     }
   }
   intervals.push_back({a,b,r,p});
   previous_end=b; count++;
 }
 if(previous_end!=M)return 6;
 // Independent table checks from the two boundary values plus monotonicity.
 // Exact collision at b and earliest collision at a imply same first collision
 // for all integers a <= n <= b; prior occurrence is unique.
 for(auto e:intervals){if(!(e[0]<=e[1]&&e[2]>=e[3]+1))return 7;}
 cout<<"VERIFY_OK M="<<M<<" intervals="<<count<<" boundary_cases="<<2*count<<"\n";
}
