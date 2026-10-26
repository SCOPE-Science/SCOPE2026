#include <bits/stdc++.h>
using namespace std;
int main(){
  vector<uint8_t> ok(32768);ifstream in("smoothquartic.bin",ios::binary);in.read((char*)ok.data(),32768);
  vector<int> S; for(int f=1;f<32768;f++)if(ok[f])S.push_back(f);
  int mono[15][3], j=0;
  for(int a=4;a>=0;a--)for(int b=4-a;b>=0;b--) {mono[j][0]=a;mono[j][1]=b;mono[j][2]=4-a-b;j++;}
  int pts[7],pid=0;for(int p=1;p<8;p++)pts[pid++]=p;
  int evmono[7]{};
  for(int p=1;p<8;p++)for(int k=0;k<15;k++){
    bool val=true;for(int i=0;i<3;i++)if(mono[k][i]>0&&!(p&(1<<i)))val=false;
    if(val)evmono[p-1]|=1<<k;
  }
  vector<uint8_t> eva(32768);
  for(int f:S)for(int p=0;p<7;p++)if(__builtin_parity(f&evmono[p]))eva[f]|=1<<p;
  uint64_t dist[8]{}; uint64_t pencils=0;
  for(size_t i=0;i<S.size();i++){
    int a=S[i];
    for(size_t j=i+1;j<S.size();j++){
      int b=S[j],c=a^b;
      if(c>b&&ok[c]){pencils++; int k=__builtin_popcount((~(eva[a]|eva[b]))&127);dist[k]++;}
    }
  }
  cout<<"smooth_forms="<<S.size()<<" pencils="<<pencils<<"\n";
  for(int k=0;k<8;k++)cout<<k<<" "<<dist[k]<<"\n";
}
