#include <bits/stdc++.h>
using namespace std;
static const int E[10][2]={{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}};
int edge[5][5];
uint32_t zeroMask[32768];
uint8_t smooth[32768];
int qeval(int m,int x){int y=__builtin_parity((unsigned)(m&x&31)); for(int k=0;k<10;k++) if((m>>(5+k)&1) && (x>>E[k][0]&1) && (x>>E[k][1]&1)) y^=1; return y;}
int rank5(int v[5]){int r=0;for(int bit=4;bit>=0;--bit){int row=r;while(row<5 && !(v[row]>>bit&1))row++;if(row==5)continue;swap(v[row],v[r]);for(int i=0;i<5;i++)if(i!=r&&(v[i]>>bit&1))v[i]^=v[r];r++;}return r;}
int radical(int m){int v[5]={0};for(int k=0;k<10;k++)if(m>>(5+k)&1){int i=E[k][0],j=E[k][1];v[i]^=1<<j;v[j]^=1<<i;}
int v0[5];copy(v,v+5,v0);if(rank5(v)!=4)return 0;for(int r=1;r<32;r++){bool ok=true;for(int i=0;i<5;i++)if(__builtin_parity((unsigned)(r&v0[i]))) {ok=false;break;}if(ok)return r;}abort();}
inline uint16_t mul(uint16_t a,uint16_t b){uint16_t r=0; while(b){if(b&1)r^=a; b>>=1;a<<=1;}return r;}
uint8_t delta(int a,int b){uint16_t pf[5];for(int om=0;om<5;om++){int ix[4],ct=0;for(int i=0;i<5;i++)if(i!=om)ix[ct++]=i;
 auto line=[&](int i,int j)->uint16_t{int k=edge[i][j];return ((a>>(5+k)&1) | ((b>>(5+k)&1)<<1));};
 pf[om]=mul(line(ix[0],ix[1]),line(ix[2],ix[3])) ^mul(line(ix[0],ix[2]),line(ix[1],ix[3])) ^mul(line(ix[0],ix[3]),line(ix[1],ix[2]));}
 uint16_t d=0;for(int i=0;i<5;i++){uint16_t x=pf[i];d^=mul( ((a>>i&1)|((b>>i&1)<<1)),mul(x,x));}
 for(int k=0;k<10;k++){int i=E[k][0],j=E[k][1];d^=mul(((a>>(5+k)&1)|((b>>(5+k)&1)<<1)),mul(pf[i],pf[j]));}
 if(d>63)abort();return d;
}
uint16_t mod_poly(uint16_t f,int g){for(int j=5;j>=2;j--)if(f>>j&1)f ^= g <<(j-2);return f;}
int main(){for(int k=0;k<10;k++)edge[E[k][0]][E[k][1]]=edge[E[k][1]][E[k][0]]=k;
vector<int> good;for(int m=1;m<32768;m++){int r=radical(m);if(!r||!qeval(m,r))continue;smooth[m]=1;good.push_back(m);uint32_t mask=0;for(int p=1;p<32;p++)if(!qeval(m,p))mask|=(1u<<(p-1));zeroMask[m]=mask;}
cerr<<"smooth="<<good.size()<<"\n";map<tuple<int,int,int>,long long> hist;long long pairCount=0,dcnt[2]={0,0}; int samples[2][2]={{0,0},{0,0}};long long bad=0;
for(int a:good)for(int b:good){if(b<=a)continue;int c=a^b;if(!smooth[c])continue;pairCount++;
// invariant computed once per unordered pencil: smallest element a among {a,b,c}
if(!(a<b && b<c))continue;
int pts=__builtin_popcount(zeroMask[a]&zeroMask[b]);int d=delta(a,b);if((d&1)==0 || (__builtin_parity((unsigned)d)==0) || !(d>>5&1)){// account degree-five could leading coeff zero, but all individual quadrics smooth => t=infty root impossible
 bad++;}
int reducible=(mod_poly(d,0b111)==0);
hist[{reducible,pts,d}]++;
if(samples[reducible][0]==0){samples[reducible][0]=a;samples[reducible][1]=b;}
}
cout<<"smooth_quadrics "<<good.size()<<"\n"<<"eligible_unordered_pairs "<<pairCount<<"\n"<<"pencils "<<pairCount/3<<"\n"<<"bad_discriminant "<<bad<<"\n";
map<pair<int,int>,long long> h2;map<int,long long> hd;for(auto [k,n]:hist){auto [re,pts,d]=k;h2[{re,pts}]+=n;hd[d]+=n;dcnt[re]+=n;}
cout<<"discriminant split (5)="<<dcnt[0]<<" (2,3)="<<dcnt[1]<<"\n";
for(auto [k,n]:h2)cout<<"type="<<(k.first?"2+3":"5")<<" points="<<k.second<<" count="<<n<<"\n";
cout<<"representatives type5 "<<samples[0][0]<<" "<<samples[0][1]<<" type2+3 "<<samples[1][0]<<" "<<samples[1][1]<<"\n";
for(auto [d,n]:hd)cout<<"delta_bits="<<d<<" count="<<n<<"\n";
}
