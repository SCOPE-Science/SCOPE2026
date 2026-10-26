#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<uint8_t> ok(32768);ifstream s("smoothquartic.bin",ios::binary);s.read((char*)ok.data(),32768);
 uint16_t tr[3][32768];ifstream i("quartic_gentable.bin",ios::binary);i.read((char*)tr,sizeof(tr));
 int mono[15][3],ind=0;for(int a=4;a>=0;a--)for(int b=4-a;b>=0;b--){mono[ind][0]=a;mono[ind][1]=b;mono[ind][2]=4-a-b;ind++;}
 int evmono[7]{}; for(int p=1;p<8;p++)for(int k=0;k<15;k++){bool val=true;for(int a=0;a<3;a++)if(mono[k][a]>0&&!(p&(1<<a)))val=false;if(val)evmono[p-1]|=1<<k;}
 uint8_t ev[32768]{};vector<int> S;for(int f=1;f<32768;f++)if(ok[f]){S.push_back(f);for(int p=0;p<7;p++)if(__builtin_parity((unsigned)(f&evmono[p])))ev[f]|=1<<p;}
 vector<uint64_t> seen(1<<24);auto get=[&](uint32_t key)->bool{return seen[key>>6]>>(key&63)&1;};
 auto add=[&](uint32_t key)->bool{uint64_t &t=seen[key>>6],h=1ULL<<(key&63);if(t&h)return false;t|=h;return true;};
 auto canonical=[](int a,int b,int c)->uint32_t{if(a>b)swap(a,b);if(b>c)swap(b,c);if(a>b)swap(a,b);return ((uint32_t)a<<15)|b;};
 map<pair<int,int>,uint64_t> dist;
 map<int,uint64_t> orbit_sizes;
 uint64_t orbits=0,total=0;
 vector<uint32_t> q;
 for(int a:S){for(int b:S){if(b<=a)continue;int c=a^b;if(c<=b||!ok[c])continue;
  uint32_t key=((uint32_t)a<<15)|b;if(!add(key))continue;
  q.clear();q.push_back(key);
  for(size_t j=0;j<q.size();j++){
   int x=q[j]>>15,y=q[j]&32767,z=x^y;
   for(int k=0;k<3;k++){
    uint32_t t=canonical(tr[k][x],tr[k][y],tr[k][z]);
    if(add(t))q.push_back(t);
   }
  }
  int k=__builtin_popcount((~(ev[a]|ev[b]))&127);
  dist[{k,(int)q.size()}]++;
  orbit_sizes[q.size()]++;
  total+=q.size();orbits++;
 }}
 cout<<"total="<<total<<" orbits="<<orbits<<" size_distro:";for(auto [sz,n]:orbit_sizes)cout<<" "<<sz<<":"<<n;cout<<"\n";
 for(auto [key,n]:dist)cout<<key.first<<" "<<key.second<<" "<<n<<"\n";
}
