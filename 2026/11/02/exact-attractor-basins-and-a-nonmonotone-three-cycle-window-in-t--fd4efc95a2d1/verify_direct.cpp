// Independent labelled-state verification of threshold-two three-color
// cyclic cellular automata on complete bipartite graphs.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;

int J(int n) {return n>=4 ? (1<<n)-2*n-2:0;}
int U(int n) {return n==1?3:(n==2||n==3?6:0);}
int64_t fact(int n){int64_t r=1;for(int i=2;i<=n;i++)r*=i;return r;}
int64_t H(int n){int64_t r=0;for(int x=2;x<=n-4;x++)for(int y=2;y<=n-x-2;y++){int z=n-x-y;r+=fact(n)/(fact(x)*fact(y)*fact(z));}return r;}
int64_t K(int n){return J(n)+(int64_t)n*J(n-1);}
int64_t L(int n){return n>=4?(int64_t)n*(n-1):0;}
int64_t predict(int a,int b,int p){
  int64_t b3=H(a)*H(b)+H(a)*U(b)+U(a)*H(b);
  int64_t b4=3*H(a)*K(b)+3*K(a)*H(b)+6*K(a)*K(b)+3*K(a)*L(b)+3*L(a)*K(b);
  int64_t all=1;for(int i=0;i<a+b;i++)all*=3;
  return p==3?b3:(p==4?b4:all-b3-b4);
}
// Recompute every vertex's opposite-shore color-neighbor count from the
// labelled state, without using any cohort quotient.
int advance(int state,int a,int b,const vector<int>& pow3){
  int n=a+b;
  vector<int> col(n);int v=state;
  for(int i=0;i<n;i++){col[i]=v%3;v/=3;}
  int countL[3]={},countR[3]={};
  for(int i=0;i<a;i++)++countL[col[i]];
  for(int i=a;i<n;i++)++countR[col[i]];
  int ret=0;
  for(int i=0;i<n;i++){
    int c=col[i], d=(c+1)%3;
    int nc=(((i<a)?countR[d]:countL[d])>=2)?d:c;
    ret+=pow3[i]*nc;
  }
  return ret;
}
int main(){
  uint64_t total=0;
  for(int a=2;a<=6;a++)for(int b=2;b<=6;b++){
    int n=a+b;vector<int> pow3(n+1,1);
    for(int i=1;i<=n;i++)pow3[i]=pow3[i-1]*3;
    map<pair<int,int>,int64_t> hist;
    for(int s=0;s<pow3[n];s++){
      int states[18]={};int k=0, x=s;int t=-1, p=-1;
      while(true){
        bool hit=false;
        for(int j=0;j<k;j++)if(states[j]==x){t=j;p=k-j;hit=true;break;}
        if(hit)break;
        assert(k<18);
        states[k++]=x;
        x=advance(x,a,b,pow3);
      }
      assert(t<=3 && (p==1||p==3||p==4));
      ++hist[{t,p}];++total;
    }
    for(int p:{1,3,4}){
      int64_t count=0;for(auto [tp,num]:hist)if(tp.second==p)count+=num;
      assert(count==predict(a,b,p));
    }
    assert((hist[{0,4}]==6LL*J(a)*J(b)));
    assert((hist[{2,4}]==3LL*(H(a)*b*J(b-1)+a*J(a-1)*H(b))));
    if((a==4 && b==4)||(a==6 && b==6)){
      cout<<"K("<<a<<","<<b<<") "
          <<"B1="<<predict(a,b,1)<<" B3="<<predict(a,b,3)<<" B4="<<predict(a,b,4)
          <<" entry_period_hist:";
      for(auto [tp,v]:hist)if(v)cout<<" ("<<tp.first<<","<<tp.second<<")="<<v;
      cout<<"\n";
    }
  }
  cout<<"PASS: independently enumerated all "<<total<<" labelled states for 25 graphs, 2<=a,b<=6"<<endl;
}
