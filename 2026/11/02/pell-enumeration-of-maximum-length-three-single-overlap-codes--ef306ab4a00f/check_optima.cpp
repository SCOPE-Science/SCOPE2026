// Independent brute-force context cut census for single-length overlap-two codes.
// Compile: g++ -std=c++17 -O3 check_optima.cpp -o check_optima
#include <bits/stdc++.h>
using namespace std;
int main(){
 for(int q=1;q<=5;q++){
  uint64_t top=1ULL<<(q*q);int best=-1;uint64_t masks=0;
  unordered_set<string> code_sets;
  for(uint64_t bits=0;bits<top;bits++){
    int outgoing[6]={},incoming[6]={};
    for(int i=0;i<q;i++)for(int j=0;j<q;j++) if((bits>>(i*q+j))&1ULL){outgoing[i]++;incoming[j]++;}
    int score=0;for(int b=0;b<q;b++)score+=incoming[b]*(q-outgoing[b]);
    if(score>best){best=score;masks=0;code_sets.clear();}
    if(score==best){masks++;string code(q*q*q,'0');
      for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)
       if(((bits>>(a*q+b))&1ULL) && !((bits>>(b*q+c))&1ULL))code[a*q*q+b*q+c]='1';
      code_sets.insert(code);
    }
  }
  uint64_t pell[8]={0,1};for(int k=2;k<=q+1;k++)pell[k]=2*pell[k-1]+pell[k-2];
  uint64_t fact=1;for(int k=1;k<=q;k++)fact*=k;
  int want=(q*q*q-q)/3;
  uint64_t wantm=fact*pell[q+1],wantc=fact*(pell[q+1]-pell[q]);
  cout<<"q="<<q<<" size="<<best<<" partitions="<<masks<<" codes="<<code_sets.size()<<"\n";
  if(best!=want||masks!=wantm||code_sets.size()!=wantc)return 2;
 }
 cout<<"EXHAUSTIVE_CONTEXT_CENSUS_OK\n";
}
