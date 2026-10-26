#include <bits/stdc++.h>
using namespace std;
using A=array<int,3>;using B=array<int,4>;
int mm(int x,int y,int irr,int deg){int s=0;for(int j=0;j<deg;j++)for(int k=0;k<deg;k++)if((x>>j&1)&&(y>>k&1))s^=1<<(j+k);for(int i=2*deg-2;i>=deg;i--)if(s>>i&1)s^=irr<<(i-deg);return s;}
int pw(int x,int k,int irr,int deg){int z=1;while(k--)z=mm(z,x,irr,deg);return z;}
vector<A> points(int deg,int irr){int q=1<<deg;vector<A> v;for(int x=0;x<q;x++)for(int y=0;y<q;y++)for(int z=0;z<q;z++){if(!(x|y|z))continue;int w=x?x:(y?y:z);int iv=pw(w,q-2,irr,deg);A p={mm(x,iv,irr,deg),mm(y,iv,irr,deg),mm(z,iv,irr,deg)};if(find(v.begin(),v.end(),p)==v.end())v.push_back(p);}return v;}
int main(){vector<A> m3;for(int a=0;a<=3;a++)for(int b=0;b<=3-a;b++)m3.push_back({a,b,3-a-b});vector<B> m4;for(int a=0;a<=3;a++)for(int b=0;b<=3-a;b++)for(int c=0;c<=3-a-b;c++)m4.push_back({a,b,c,3-a-b-c});assert(m3.size()==10&&m4.size()==20);
 // Singular curve criterion: evaluate all closed points of degrees 1,2,3.
 bool good[1024];fill(good,good+1024,true);
 for(auto [deg,irr]:vector<pair<int,int>>{{1,3},{2,7},{3,11}}){auto ps=points(deg,irr);int q=1<<deg;for(A p:ps){int vv[10],dd[3][10];for(int j=0;j<10;j++){auto [a,b,c]=m3[j];vv[j]=mm(mm(pw(p[0],a,irr,deg),pw(p[1],b,irr,deg),irr,deg),pw(p[2],c,irr,deg),irr,deg);for(int k=0;k<3;k++)dd[k][j]=m3[j][k]%2?mm(mm(pw(p[0],a-(k==0),irr,deg),pw(p[1],b-(k==1),irr,deg),irr,deg),pw(p[2],c-(k==2),irr,deg),irr,deg):0;}
 for(int f=1;f<1024;f++)if(good[f]){int d[3]={};for(int j=0;j<10;j++)if(f>>j&1)for(int k=0;k<3;k++)d[k]^=dd[k][j];if(!(d[0]||d[1]||d[2]))good[f]=false;}
 }cout<<"checked extension "<<q<<" points "<<ps.size()<<"\n";}
 good[0]=false; int ngood=count(good,good+1024,true);cout<<"smooth ternary cubics = "<<ngood<<"\n";
 // Build gradient ideal degree-five, test rank 56 for surface smoothness.
 vector<B> m5;for(int a=0;a<=5;a++)for(int b=0;b<=5-a;b++)for(int c=0;c<=5-a-b;c++)m5.push_back({a,b,c,5-a-b-c}); assert(m5.size()==56);
 uint64_t block[4][20][20]={};for(int j=0;j<20;j++)for(int k=0;k<4;k++)if(m4[j][k]%2)for(int r=0;r<20;r++) {B v=m4[j];v[k]--;for(int t=0;t<4;t++)v[t]+=m4[r][t];int c=find(m5.begin(),m5.end(),v)-m5.begin();if(c<0||c>=56)abort();block[k][r][j]=1ull<<c;}
 auto isSmooth=[&](int f){uint64_t basis[56]={};int rank=0;for(int k=0;k<4;k++)for(int r=0;r<20;r++){uint64_t v=0;int g=f;while(g){int j=__builtin_ctz((unsigned)g);v^=block[k][r][j];g&=g-1;}for(int b=55;b>=0;b--)if((v>>b)&1){if(basis[b])v^=basis[b];else {basis[b]=v;rank++;break;}}}return rank==56;};
 // 15 rational planes, 3 independent vectors in kernel each.
 vector<B> pts4;for(int z=1;z<16;z++)pts4.push_back({z&1,(z>>1)&1,(z>>2)&1,(z>>3)&1});
 uint16_t transform[15][20]={};int pi=0;for(auto l:pts4){vector<B> kern;for(auto v:pts4){int dp=0;for(int k=0;k<4;k++)dp^=l[k]&v[k];if(dp==0)kern.push_back(v);}vector<B> basis;vector<int> rb;for(auto v:kern){int vcode=v[0]|v[1]<<1|v[2]<<2|v[3]<<3;int x=vcode;for(int e:rb)x=min(x,x^e);if(x){rb.push_back(x);basis.push_back(v);}if(basis.size()==3)break;}assert(basis.size()==3);
 int forms[4]={};for(int k=0;k<4;k++)for(int j=0;j<3;j++)if(basis[j][k]){A mono={};mono[j]=1;int ii=find(m3.begin(),m3.end(),mono)-m3.begin();(void)ii;forms[k]|=1<<j;}
 // polys in (y0,y1,y2), represented monomial exponent triple and parity.
 for(int h=0;h<20;h++){map<A,int> poly;poly[A{0,0,0}]=1;for(int v=0;v<4;v++)for(int exp=0;exp<m4[h][v];exp++){map<A,int> nxt;for(auto [a,c]:poly)if(c)for(int k=0;k<3;k++)if(forms[v]>>k&1){A b=a;b[k]++;nxt[b]^=1;}poly=nxt;}
 int mask=0;for(auto [a,c]:poly)if(c){int ix=find(m3.begin(),m3.end(),a)-m3.begin();if(ix==10)abort();mask^=1<<ix;}transform[pi][h]=mask;}
 pi++;}assert(pi==15);
 // rational derivatives at all P3 F2
 int dg[15][4][20]={};for(int i=0;i<15;i++)for(int j=0;j<20;j++)for(int k=0;k<4;k++){if(!(m4[j][k]&1))continue;int val=1;for(int v=0;v<4;v++)if(m4[j][v]-(v==k)>0&&!pts4[i][v])val=0;dg[i][k][j]=val;}
 uint16_t restriction[15]={};int grad[15][4]={};ofstream ex("zero_cubics.txt");long long surface_count=0, geo_count=0;map<int,long long> distribution,geodistribution;map<int,int> min_example,geomin_example;int minv=15,mingeo=15;long long fmincount=0;
 for(int it=1;it<(1<<20);it++){int j=__builtin_ctz((unsigned)it); // Gray g=it^(it>>1) flips bit ctz(it)
 for(int k=0;k<15;k++){restriction[k]^=transform[k][j];for(int d=0;d<4;d++)grad[k][d]^=dg[k][d][j];}
 bool locally_smooth=true;for(int k=0;k<15;k++)if(!(grad[k][0]||grad[k][1]||grad[k][2]||grad[k][3])){locally_smooth=false;break;}
 if(!locally_smooth)continue;
 int sn=0;for(int k=0;k<15;k++)sn+=good[restriction[k]];
 distribution[sn]++;surface_count++;
 if(sn<minv){minv=sn;fmincount=0;}if(sn==minv)fmincount++;
 if(!min_example.count(sn))min_example[sn]=it^(it>>1);
 int gf=it^(it>>1);if(isSmooth(gf)) {if(sn==0)ex<<gf<<"\n";geo_count++;geodistribution[sn]++;if(!geomin_example.count(sn))geomin_example[sn]=gf;mingeo=min(mingeo,sn);}
 }
 cout<<"rational-nonsingular surfaces="<<surface_count<<" min transverse planes="<<minv<<" min_count="<<fmincount<<"\n";
 for(auto [n,c]:distribution)cout<<n<<" : "<<c<<" e="<<min_example[n]<<"\n";
 cout<<"geometrically smooth="<<geo_count<<" min="<<mingeo<<"\n";for(auto [n,c]:geodistribution)cout<<"geo "<<n<<" : "<<c<<" witness="<<geomin_example[n]<<"\n";
}
