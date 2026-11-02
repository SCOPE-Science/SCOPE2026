#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
static const int A[4]={0,1,2,5};
static int word[87];
static uint64_t widths[88]={0};
static vector<string> best;
bool ok(int n){
 int k=1;
 int left=word[n-2],right=word[n-1];
 if(left==right) return false;
 while(2*(k+1)<=n){
    left+=word[n-2*k-2]+word[n-2*k-1]-word[n-k-1];
    right+=word[n-k-1];
    ++k;
    if(left==right) return false;
 }
 return true;
}
void search(int n){
 ++widths[n];
 if(n==86){
   string s;for(int i=0;i<n;i++)s+=char('0'+word[i]);best.push_back(s);
 }
 if(n==87)return;
 for(int a:A){word[n]=a;if(n==0||ok(n+1))search(n+1);}
}
int main(){search(0);uint64_t total=0;for(auto x:widths)total+=x;
 cout<<"nodes="<<total<<" valid86="<<best.size()<<" next87="<<widths[87]<<"\n";
 for(int n=80;n<=86;n++)cout<<"depth="<<n<<" count="<<widths[n]<<"\n";
 sort(best.begin(),best.end());for(auto &s:best)cout<<s<<"\n";
}
