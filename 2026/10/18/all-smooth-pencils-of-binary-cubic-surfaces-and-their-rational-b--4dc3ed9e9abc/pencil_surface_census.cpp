#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
int main(){
 const int N=1<<20;
 ifstream b("cubic_surface_smooth.bin",ios::binary);
 vector<unsigned char>s(N);b.read((char*)s.data(),N);if(b.gcount()!=N)throw runtime_error("smooth file missing");
 vector<U>good;good.reserve(N/3);for(int i=1;i<N;i++)if(s[i])good.push_back(i);
 vector<array<int,4>> mon;
 for(int a=0;a<=3;a++)for(int c=0;c<=3-a;c++)for(int d=0;d<=3-a-c;d++)mon.push_back({a,c,d,3-a-c-d});
 if(mon.size()!=20)throw runtime_error("mon size");
 U eval[15];for(int p=1;p<16;p++){U q=0;for(int j=0;j<20;j++){bool ok=true;for(int x=0;x<4;x++)if(mon[j][x]&&!(p>>x&1)){ok=false;break;}if(ok)q |= (1U<<j);}eval[p-1]=q;}
 vector<uint16_t>zeros(N);
 for(U f:good){uint16_t z=0;for(int p=0;p<15;p++)if(!(__builtin_parity(f&eval[p])))z|=(1<<p);zeros[f]=z;}
 ifstream t("cubic_surface_orbits.tsv");string header;getline(t,header);
 unsigned long long weightedPairs=0;long long weightedHist[16]={};int r=0;
 U f;unsigned long long orb;int pts,ls,eck,sc;
 while(t>>f>>orb>>pts>>ls>>eck>>sc){r++;unsigned long long subtotal=0;
  for(U g:good)if(s[f^g]){subtotal++;
   int z=__builtin_popcount((unsigned)(zeros[f] & zeros[g]));weightedHist[z]+=orb;
  }
  weightedPairs+=orb*subtotal;
 }
 cout<<"smooth_count "<<good.size()<<" representatives "<<r<<" weighted_ordered_pairs "<<weightedPairs<<" pencils "<<weightedPairs/6<<" mod6 "<<weightedPairs%6<<"\n";
 long long tally=0;
 for(int k=0;k<16;k++){if(weightedHist[k]){cout<<"base_points "<<k<<" pencils "<<weightedHist[k]/6<<" ordered "<<weightedHist[k]<<" mod6 "<<weightedHist[k]%6<<"\n";}tally+=weightedHist[k];}
 cout<<"hist_ordered_sum "<<tally<<"\n";
}
