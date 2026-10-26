#include <bits/stdc++.h>
using namespace std;
struct Term{int a,b,c;};
const vector<Term> terms={{4,0,0},{3,1,0},{3,0,1},{2,2,0},{2,1,1},{2,0,2},{1,3,0},{1,2,1},{1,1,2},{1,0,3},{0,4,0},{0,3,1},{0,2,2},{0,1,3},{0,0,4}};
struct Point{int n,x,y,z;array<unsigned char,15> f,fx,fy,fz;};
int mul(int a,int b,int k){ int poly=(k==1?3:k==2?7:k==3?11:19),n=1<<k,r=0;while(b){if(b&1)r^=a;b>>=1;a<<=1;if(a&n)a^=poly;}return r;}
int power(int x,int n,int k){int r=1;while(n--)r=mul(r,x,k);return r;}
vector<Point> all_points(int k){int q=1<<k;vector<array<int,3>> pts;for(int y=0;y<q;y++)for(int z=0;z<q;z++)pts.push_back({1,y,z});for(int z=0;z<q;z++)pts.push_back({0,1,z});pts.push_back({0,0,1});vector<Point> out;for(auto p:pts){Point t{};t.n=k;t.x=p[0];t.y=p[1];t.z=p[2];for(int i=0;i<15;i++){auto [a,b,c]=terms[i];int v=mul(mul(power(p[0],a,k),power(p[1],b,k),k),power(p[2],c,k),k);t.f[i]=v;t.fx[i]=a%2?mul(mul(power(p[0],a-1,k),power(p[1],b,k),k),power(p[2],c,k),k):0;t.fy[i]=b%2?mul(mul(power(p[0],a,k),power(p[1],b-1,k),k),power(p[2],c,k),k):0;t.fz[i]=c%2?mul(mul(power(p[0],a,k),power(p[1],b,k),k),power(p[2],c-1,k),k):0;}out.push_back(t);}return out;}
int main(){vector<Point> ps;for(int k=1;k<=4;k++){auto p=all_points(k);cerr<<"k="<<k<<" points="<<p.size()<<"\n";ps.insert(ps.end(),p.begin(),p.end());}int count=0;ofstream o("smooth_quartics.txt");ofstream cert("nonsmooth_certificates.tsv");for(int mask=1;mask<(1<<15);mask++){bool good=true;for(auto &p:ps){int v=0,vx=0,vy=0,vz=0;for(int i=0;i<15;i++)if(mask&(1<<i)){v^=p.f[i];vx^=p.fx[i];vy^=p.fy[i];vz^=p.fz[i];}if((v|vx|vy|vz)==0){good=false;cert<<mask<<"\t"<<p.n<<"\t"<<p.x<<"\t"<<p.y<<"\t"<<p.z<<"\n";break;}}if(good){o<<mask<<"\n";count++;}}cout<<"smooth_count="<<count<<"\n";}
