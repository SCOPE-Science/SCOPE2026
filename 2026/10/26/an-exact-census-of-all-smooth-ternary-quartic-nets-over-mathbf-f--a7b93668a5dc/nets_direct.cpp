#include <bits/stdc++.h>
using namespace std;
uint64_t permxor(uint64_t x,int l){
 const uint64_t m[6]={0x5555555555555555ull,0x3333333333333333ull,0x0f0f0f0f0f0f0f0full,0x00ff00ff00ff00ffull,0x0000ffff0000ffffull,0x00000000ffffffffull};
 for(int k=0;k<6;k++)if(l>>k&1)x=((x&m[k])<<(1<<k)) | ((x>>(1<<k))&m[k]);
 return x;
}
int main(){
 vector<uint8_t> ok(32768);ifstream in("smoothquartic.bin",ios::binary);in.read((char*)ok.data(),32768);
 vector<int> S;for(int f=1;f<32768;f++)if(ok[f])S.push_back(f);
 ifstream in2("quartic_reps.csv");string line;getline(in2,line);
 long long answer=0;int rep_count=0;
 while(getline(in2,line)){
  if(line.empty())continue;
  auto pos=line.find(',');int a=stoi(line.substr(0,pos)),weight=stoi(line.substr(pos+1));
  uint64_t B[512]{};for(int h=0;h<32768;h++)if(ok[h]&&ok[h^a])B[h>>6]|=1ull<<(h&63);
  uint64_t xorlow[64][512];
  for(int k=0;k<64;k++)for(int i=0;i<512;i++)xorlow[k][i]=permxor(B[i],k);
  uint64_t total=0;
  for(int b:S)if(ok[b^a]){
   int lo=b&63,hi=b>>6;
   uint64_t sum=0;
   for(int j=0;j<512;j++)sum+=__builtin_popcountll(B[j]&xorlow[lo][j^hi]);
   total+=sum;
  }
  answer+=weight*total;
  rep_count++;
 }
 assert(answer%168==0);
 cout<<"rep_count="<<rep_count<<" ordered_triples="<<answer<<" nets="<<answer/168<<"\n";
}
