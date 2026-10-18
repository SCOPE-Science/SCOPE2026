#include <bits/stdc++.h>
using namespace std;
struct GF {int d,q,poly; unsigned char mul[64][64];GF(int dd,int pp):d(dd),q(1<<dd),poly(pp){memset(mul,0,sizeof(mul));for(int a=0;a<q;a++)for(int b=0;b<q;b++){int v=0,aa=a,bb=b;while(bb){if(bb&1)v^=aa; bb>>=1;aa<<=1;if(aa&q)aa^=poly;}mul[a][b]=v;}}};
int main(){const int irr[]={0,3,7,11,19,37,67};vector<unsigned char> nonsmooth(65536,0);nonsmooth[0]=1;vector<unsigned char> wd(65536,0),wx(65536,0),wy(65536,0);
for(int d=1;d<=6;d++){GF g(d,irr[d]); long long pt=0,codes=0;int q=g.q;for(int xx=0;xx<=q;xx++)for(int yy=0;yy<=q;yy++){int powx[4]={1,1,1,1},powy[4]={1,1,1,1};bool ix=(xx==q),iy=(yy==q);if(ix)for(int j=1;j<4;j++)powx[j]=0;if(iy)for(int j=1;j<4;j++)powy[j]=0;if(!ix)for(int j=1;j<4;j++)powx[j]=g.mul[powx[j-1]][xx];if(!iy)for(int j=1;j<4;j++)powy[j]=g.mul[powy[j-1]][yy];int rows[18]={};for(int j=0;j<4;j++)for(int i=0;i<4;i++){int a=ix?3-i:i,b=iy?3-j:j;int f=g.mul[powx[a]][powy[b]];int fx=(a&1)?g.mul[powx[a-1]][powy[b]]:0;int fy=(b&1)?g.mul[powx[a]][powy[b-1]]:0;int v[3]={f,fx,fy};int k=4*j+i;for(int z=0;z<3;z++)for(int bit=0;bit<d;bit++)if((v[z]>>bit)&1)rows[z*d+bit]^=(1<<k);}
int basis[16]={};int rank=0;for(int z=0;z<3*d;z++){int w=rows[z];while(w){int k=31-__builtin_clz((unsigned)w);if(!basis[k]){basis[k]=w;rank++;break;}w^=basis[k];}}
int freevar[16],nf=0;for(int i=0;i<16;i++)if(!basis[i])freevar[nf++]=i;int nullv[16];for(int l=0;l<nf;l++){int w=1<<freevar[l];for(int i=0;i<16;i++)if(basis[i]&&(__builtin_parity((unsigned)(w&basis[i]))))w^=(1<<i);nullv[l]=w;}
int n=(1<<nf),v=0;for(int mask=1;mask<n;mask++){int bit=__builtin_ctz((unsigned)mask);v^=nullv[bit];if(!nonsmooth[v]){wd[v]=d;wx[v]=xx;wy[v]=yy;}nonsmooth[v]=1;codes++;}
pt++;}
int smooth=0;for(int v=1;v<65536;v++)if(!nonsmooth[v])smooth++;cerr<<"degree="<<d<<" points="<<pt<<" enumerated="<<codes<<" smooth_remaining="<<smooth<<"\n";
}
ofstream out("data/smooth_bitset.bin",ios::binary);out.write((char*)nonsmooth.data(),nonsmooth.size());ofstream ww("data/witness.bin",ios::binary);for(int v=0;v<65536;v++){ww.put(wd[v]);ww.put(wx[v]);ww.put(wy[v]);}
}
