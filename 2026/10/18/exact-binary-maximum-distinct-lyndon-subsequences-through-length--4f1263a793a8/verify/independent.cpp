#include <bits/stdc++.h>
using namespace std;
struct Word{unsigned bits; int len;};
int main(int argc, char**argv){
 const int MAXN=20;
 vector<Word> lynd;
 for(int l=1;l<=MAXN;l++){
  int top=1<<l,mask=top-1;
  for(int v=0;v<top;v++){
   bool pass=true;
   for(int shift=1;shift<l;shift++){
    int rot=((v<<shift)&mask)|(v>>(l-shift));
    if(v>=rot){pass=false;break;}
   }
   if(pass)lynd.push_back({(unsigned)v,l});
  }
 }
 auto count=[&](unsigned host,int n){
  int next[22][2];next[n][0]=next[n][1]=n;
  for(int i=n-1;i>=0;i--){next[i][0]=next[i+1][0];next[i][1]=next[i+1][1];next[i][(host>>(n-1-i))&1]=i;}
  int cnt=0;
  for(auto& item:lynd){
   if(item.len>n)break;
   int p=0; bool valid=true;
   for(int j=item.len-1;j>=0;j--){
    p=next[p][(item.bits>>j)&1];
    if(p==n){valid=false;break;}
    p++;
   }
   if(valid)cnt++;
  }
  return cnt;
 };
 const int targets[]={0,1,3,4,6,8,13,18,28,41,63,96,141,225,335,538};
 for(int n=1;n<=15;n++){
  int maxv=-1,countv=0;
  for(unsigned host=0;host<(1u<<n);host++){
   int c=count(host,n);
   if(c>maxv){maxv=c;countv=0;}if(c==maxv)countv++;
  }
  if(maxv!=targets[n]){cerr<<"FAIL n="<<n<<" c="<<maxv;return 1;}
  cout<<"INDEPENDENT_FULL n="<<n<<" max="<<maxv<<" optimizers="<<countv<<"\n";
 }
 const char* witness[]={"0001010101101011","00010101010101011","000101010101101011","0001010101010101011","00010101010101101011"};
 const int vals[]={803,1292,1941,3132,4701};
 for(int i=0;i<5;i++){
  unsigned v=0;for(char const* p=witness[i];*p;p++)v=(v<<1)|(*p-'0');
  int n=strlen(witness[i]);int c=count(v,n);
  if(c!=vals[i]){cerr<<"WITNESS_FAIL n="<<n<<" expected="<<vals[i]<<" observed="<<c<<"\n";return 1;}
  cout<<"INDEPENDENT_WITNESS n="<<n<<" count="<<c<<"\n";
 }
 cout<<"INDEPENDENT_OK\n";
}
