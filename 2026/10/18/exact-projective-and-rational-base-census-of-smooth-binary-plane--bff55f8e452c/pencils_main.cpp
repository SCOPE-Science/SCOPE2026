#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
struct B66 {ull lo=0, hi=0; void flip(int i){if(i<64)lo ^= 1ULL<<i; else hi ^= 1ULL<<(i-64);} bool at(int i)const{return i<64 ? (lo>>i)&1ULL : (hi>>(i-64))&1ULL;} void xor_with(const B66&o){lo^=o.lo;hi^=o.hi;} bool nonzero()const{return lo||hi;}};
vector<array<int,3>> mon(int d){ vector<array<int,3>> v; for(int i=d;i>=0;i--)for(int j=d-i;j>=0;j--)v.push_back({i,j,d-i-j});return v; }
int main(){
 auto m4=mon(4),m3=mon(3),m6=mon(6),m7=mon(7),m10=mon(10);
 auto idx=[&](array<int,3> a)->int{for(int i=0;i<66;i++)if(m10[i]==a)return i;abort();};
 B66 contribution[4][15][36];
 for(int t=0;t<15;t++){
  for(int k=0;k<28;k++){
   array<int,3> a={m4[t][0]+m6[k][0],m4[t][1]+m6[k][1],m4[t][2]+m6[k][2]};contribution[0][t][k].flip(idx(a));
  }
  for(int d=0;d<3;d++) if(m4[t][d]&1)for(int k=0;k<36;k++){
   auto a=m4[t];a[d]--;for(int j=0;j<3;j++)a[j]+=m7[k][j];contribution[d+1][t][k].flip(idx(a));
  }
 }
 static uint8_t is_smooth[1<<15];
 static uint8_t pointmask[1<<15];
 vector<array<int,3>> points;
 for(int i=1;i<8;i++){array<int,3> p={!!(i&1),!!(i&2),!!(i&4)};points.push_back(p);}
 uint16_t peval[7]={};for(int j=0;j<7;j++)for(int t=0;t<15;t++){
  int z=1;for(int k=0;k<3;k++)if(m4[t][k]>0 && points[j][k]==0)z=0; if(z)peval[j] |= uint16_t(1)<<t;
 }
 for(int f=1;f<(1<<15);f++){
  B66 basis[66];int rank=0;
  for(int b=0;b<4;b++)for(int k=0;k<(b==0?28:36);k++){
   B66 v;for(int t=0;t<15;t++)if(f>>t&1)v.xor_with(contribution[b][t][k]);
   while(v.nonzero()){
     int pivot = v.hi ? 64+63-__builtin_clzll(v.hi) : 63-__builtin_clzll(v.lo);
     if(!basis[pivot].nonzero()){basis[pivot]=v;rank++;break;}
     v.xor_with(basis[pivot]);
   }
   if(rank==66)break;
  }
  is_smooth[f]=(rank==66);
  for(int j=0;j<7;j++)if(!(__builtin_parity(f & peval[j])))pointmask[f] |= 1<<j;
 }
 vector<int> good;for(int i=1;i<(1<<15);i++)if(is_smooth[i])good.push_back(i);
 cout<<"smooth="<<good.size()<<"\n";
 {ofstream out("smooth_form_masks.txt");for(int f:good)out<<f<<"\n";}

 // Explicit PGL_3(F_2) action. All scalar matrices are 1 in characteristic two.
 vector<array<int,3>> mats;
 auto matmul=[](array<int,3> a,array<int,3> b){array<int,3> c={0,0,0};for(int i=0;i<3;i++)for(int j=0;j<3;j++)if((a[i]>>j)&1)c[i]^=b[j];return c;};
 array<int,3> id={1,2,4};
 auto rankmat=[&](array<int,3> a){int r=0;for(int z=2;z>=0;z--){int k=-1;for(int i=r;i<3;i++)if(a[i]>>z&1){k=i;break;}if(k<0)continue;swap(a[r],a[k]);for(int i=0;i<3;i++)if(i!=r&&(a[i]>>z&1))a[i]^=a[r];r++;}return r;};
 for(int i=0;i<512;i++){array<int,3> a={i&7,(i>>3)&7,(i>>6)&7};if(rankmat(a)==3)mats.push_back(a);}
 assert(mats.size()==168);
 auto getorder=[&](array<int,3> m){auto x=id;for(int d=1;d<=168;d++){x=matmul(x,m);if(x==id)return d;}return -1;};
 map<int,int> orderhist;map<int,array<int,3>> repre;
 for(auto m:mats){int ord=getorder(m);orderhist[ord]++;repre[ord]=m;}
 cout<<"group_order_distribution";for(auto it:orderhist)cout<<" "<<it.first<<":"<<it.second;cout<<"\n";
 auto basis_action=[&](array<int,3> m){
  array<uint16_t,15> result={};
  for(int t=0;t<15;t++){
   vector<unsigned char> poly={1};int d=0;
   for(int var=0;var<3;var++)for(int e=0;e<m4[t][var];e++){
    auto old=mon(d);auto next=mon(d+1);vector<unsigned char> np(next.size());
    for(int j=0;j<(int)old.size();j++)if(poly[j])for(int v=0;v<3;v++)if(m[var]>>v&1){auto a=old[j];a[v]++;for(int k=0;k<(int)next.size();k++)if(a==next[k])np[k]^=1;}
    poly=np;d++;
   }
   for(int k=0;k<15;k++)if(poly[k])result[t]^=1<<k;
  }
  return result;
 };

 // Refine odd-order stabilizers via the normalizer of a Sylow-7 subgroup.
 auto g7=repre[7];array<array<int,3>,7> powers;powers[0]=id;
 for(int k=1;k<7;k++)powers[k]=matmul(powers[k-1],g7);
 array<int,3> normalizer3={0,0,0};
 for(auto m:mats)if(getorder(m)==3){
  if(matmul(m,g7)==matmul(powers[2],m) || matmul(m,g7)==matmul(powers[4],m)){normalizer3=m;break;}
 }
 assert(normalizer3[0]||normalizer3[1]||normalizer3[2]);
 auto translist=[&](array<int,3> mat){auto ac=basis_action(mat);vector<uint16_t> t(1<<15);for(int f=1;f<(1<<15);f++){int low=f&-f;t[f]=t[f^low]^ac[__builtin_ctz((unsigned)low)];}return t;};
 auto t7=translist(g7),t3=translist(normalizer3);
 ull fixed7=0,fixed21=0;vector<array<int,3>> fixed7p;
 for(int ii=0;ii<(int)good.size();ii++){
  int a=good[ii],ga=t7[a];
  for(int jj=ii+1;jj<(int)good.size();jj++){
   int b=good[jj],c=a^b;if(c<b||!is_smooth[c])continue;
   if((ga==a||ga==b||ga==c) && (t7[b]==a||t7[b]==b||t7[b]==c)){
    fixed7++;fixed7p.push_back({a,b,c});
    int ta=t3[a],tb=t3[b];if((ta==a||ta==b||ta==c)&&(tb==a||tb==b||tb==c))fixed21++;
   }
  }
 }
 cout<<"fixed_by_normalizer21 "<<fixed21<<" fixed_sylow7 "<<fixed7<<"\n";
 for(auto trio:fixed7p){int r=__builtin_popcount(pointmask[trio[0]]&pointmask[trio[1]]);
   cout<<"sylow7_fixed_pencil "<<trio[0]<<","<<trio[1]<<","<<trio[2]<<" base_rational="<<r<<" normalizer21="<<((t3[trio[0]]==trio[0]||t3[trio[0]]==trio[1]||t3[trio[0]]==trio[2])&&(t3[trio[1]]==trio[0]||t3[trio[1]]==trio[1]||t3[trio[1]]==trio[2]))<<"\n";}


 // Independent projective-orbit partition of the smooth individual quartics.
 vector<uint8_t> seen(1<<15);vector<int> smooth_reps;
 vector<array<uint16_t,15>> full_actions;
 for(auto m:mats)full_actions.push_back(basis_action(m));
 for(int a:good)if(!seen[a]){
  smooth_reps.push_back(a);
  for(auto ac:full_actions){int x=0;for(int t=0;t<15;t++)if(a>>t&1)x^=ac[t];assert(is_smooth[x]);seen[x]=1;}
 }
 assert(smooth_reps.size()==78);
 cout<<"smooth_form_projective_orbits="<<smooth_reps.size()<<"\n";
 {ofstream out("smooth_representatives.txt");for(int a:smooth_reps)out<<a<<"\n";}
 map<int,ull> fixed;
 for(auto pp:repre){
  int ord=pp.first;auto action=basis_action(pp.second);
  static uint16_t transformed[1<<15];transformed[0]=0;
  for(int f=1;f<(1<<15);f++){
   int low=f&-f;int b=__builtin_ctz((unsigned)low);transformed[f]=transformed[f^low]^action[b];
  }
  ull fpairs=0;
  for(int ii=0;ii<(int)good.size();ii++){
   int a=good[ii],ga=transformed[a];
   for(int jj=ii+1;jj<(int)good.size();jj++){
    int b=good[jj],c=a^b;if(!is_smooth[c])continue;
    if(ga!=a&&ga!=b&&ga!=c)continue;
    int gb=transformed[b];if(gb!=a&&gb!=b&&gb!=c)continue;
    fpairs++;
   }
  }
  assert(fpairs%3==0);fixed[ord]=fpairs/3;
  cout<<"fixed_by_order "<<ord<<" "<<fixed[ord]<<"\n";
 }
 ull burn=0;for(auto h:orderhist)burn+=(ull)h.second*fixed[h.first];
 assert(burn%168==0);cout<<"projective_orbits="<<burn/168<<"\n";

 ull pens=0,pensB[8]={};ull pensRx[128]={},membersR[8]={};
 for(int f:good)membersR[__builtin_popcount(pointmask[f])]++;
 for(int ii=0;ii<(int)good.size();ii++){
  int a=good[ii];for(int jj=ii+1;jj<(int)good.size();jj++){
   int b=good[jj];if(!is_smooth[a^b])continue;
   pens++;int bs=(int)(pointmask[a]&pointmask[b]);pensRx[bs]++;pensB[__builtin_popcount((unsigned)bs)]++;
  }
 }
 cout<<"good unordered pair count="<<pens<<" divisible by3="<<(pens%3==0)<<"\n";
 cout<<"pencils="<<pens/3<<"\n";
 for(int r=0;r<8;r++)cout<<"base_rational "<<r<<" pencils "<<pensB[r]/3<<"\n";
 for(int r=0;r<8;r++)cout<<"smooth_rational "<<r<<" equations "<<membersR[r]<<"\n";
 for(int r=0;r<128;r++)if(pensRx[r])cout<<"base_mask "<<r<<" pens "<<pensRx[r]/3<<"\n";
}
