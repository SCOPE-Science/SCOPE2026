// Complete constructions and direct neighborhood checks for identifying codes.
// C++17 standard library only.
#include <bits/stdc++.h>
using namespace std;
using ULL=unsigned long long;
const string BX="000010101", BB="011010001";
const vector<string> X={
 "000010101", "0001010101", "00001010101", "101000010101", "0100001010101",
 "10100001010101", "010101000010101", "0100101000010101", "01010100001010101"};
const vector<string> B={
 "011010001", "1101000001", "01101000001", "001011010001", "0101101000001",
 "00101101000001", "010001011010001", "0100101011010001", "01000101101000001"};
const int VAL[9]={0,1,1,3,3,4,5,6,6};

bool local(const string&x,const string&b,int *cnt=nullptr){
 int n=x.size(),def=0;
 auto X=[&](int z){return x[(z%n+n)%n]=='1';};
 auto B=[&](int z){return b[(z%n+n)%n]=='1';};
 for(int i=0;i<n;i++){
  if(!(X(i-1)||X(i)||B(i)||X(i+1)))return false;
  if(!(X(i-1)||B(i)||B(i+1)||X(i+2)))return false;
  if(!(X(i-1)||X(i)||B(i)||X(i+2)||B(i+2)||X(i+3)))return false;
  if(!(B(i-1)||X(i)||X(i+2)||B(i+3)))return false;
  if(!(B(i-1)||X(i)||B(i+1)))def++;
 }
 if(cnt)*cnt=def;
 return def<=1;
}

bool identify(const string&x,const string&b){
 int n=x.size();if(n<5||b.size()!=size_t(n))return false;
 // for n up to 120, identify by std::vector<int> without machine bit assumptions
 vector<vector<int>> sig(2*n);
 for(int i=0;i<n;i++){
  for(int j=0;j<n;j++){
   bool v=i==j || (i+1)%n==j || (j+1)%n==i;
   if(v && x[j]=='1')sig[i].push_back(j);
   if(i==j && b[j]=='1')sig[i].push_back(j+n);
   bool bv=(i==j || ((i+1)%n!=j && (j+1)%n!=i));
   if(bv && b[j]=='1')sig[i+n].push_back(j+n);
   if(i==j && x[j]=='1')sig[i+n].push_back(j);
  }
  sort(sig[i].begin(),sig[i].end());
  sort(sig[i+n].begin(),sig[i+n].end());
 }
 for(int i=0;i<2*n;i++){
  if(sig[i].empty())return false;
  for(int j=0;j<i;j++)if(sig[i]==sig[j])return false;
 }
 return true;
}
// Verify the common four-column transition state and the defect budget.
bool state19_path(const string&x,const string&b,int *defects){
 int q=19,n=int(x.size()),dd=0;
 for(int i=0;i<n;i++){
  int c[5],u=q;
  for(int t=3;t>=0;t--){c[t]=u%4;u/=4;}
  c[4]=(x[i]=='1')+2*(b[i]=='1');
  auto X=[&](int j){return (c[j]&1)!=0;};
  auto B=[&](int j){return (c[j]&2)!=0;};
  if(!(X(0)||X(1)||B(1)||X(2)))return false;
  if(!(X(0)||B(1)||B(2)||X(3)))return false;
  if(!(X(0)||X(1)||B(1)||X(3)||B(3)||X(4)))return false;
  if(!(B(0)||X(1)||X(3)||B(4)))return false;
  if(!(B(0)||X(1)||B(2)))dd++;
  q=(q*4+c[4])&255;
 }
 if(defects)*defects=dd;
 return q==19;
}
int main(){
 int coredef=-1;
 assert(state19_path(BX,BB,&coredef)&&coredef==0);
 for(int r=0;r<9;r++){
  assert(X[r].size()==size_t(9+r)&&B[r].size()==size_t(9+r));
  int defect=-1;
  assert(local(X[r],B[r],&defect));
  int graphdef=-1; assert(state19_path(X[r],B[r],&graphdef));assert(graphdef==defect);
  int weight=count(X[r].begin(),X[r].end(),'1')+count(B[r].begin(),B[r].end(),'1');
  assert(weight==7+VAL[r]);
  assert(count(B[r].begin(),B[r].end(),'1')>=4);
  assert(identify(X[r],B[r]));
  cout<<"base n="<<9+r<<" weight="<<weight<<" defects="<<defect<<" identified=1\n";
  for(int k=1;k<=9;k++){
   string x,b;
   for(int t=1;t<k;t++){x+=BX;b+=BB;}
   x+=X[r];b+=B[r];
   int dd=-1;
   assert(local(x,b,&dd));
   assert(dd<=1);
   assert(count(B[r].begin(),B[r].end(),'1')+4*(k-1)>=4);
   assert(identify(x,b));
   assert(int(count(x.begin(),x.end(),'1')+count(b.begin(),b.end(),'1'))==7*k+VAL[r]);
  }
 }
 cout<<"all splice/direct tests n=9..89 PASS\n";
 // independent all-subsets search on n=9,10 (2n labeled vertices)
 for(int n: {9,10}){
  ULL optimum=ULL(2*n+1), num=0;
  // Search all 2^(2n) binary choices; n=10 -> 1,048,576 candidates.
  ULL limit=(1ULL<<(2*n));
  for(ULL mask=0;mask<limit;mask++){
   int w=__builtin_popcountll(mask);
   if(w>int(optimum))continue;
   string x(n,'0'),b(n,'0');
   for(int i=0;i<n;i++){
    if(mask&(1ULL<<i))x[i]='1';
    if(mask&(1ULL<<(n+i)))b[i]='1';
   }
   if(!identify(x,b))continue;
   if(w<optimum){optimum=w;num=0;}
   num++;
  }
  assert(optimum==unsigned(7+VAL[n-9]));
  cout<<"direct all-subsets n="<<n<<" optimum="<<optimum<<" optima="<<num<<" exhaustive=1\n";
 }
 cout<<"DIRECT_OK\n";
}
