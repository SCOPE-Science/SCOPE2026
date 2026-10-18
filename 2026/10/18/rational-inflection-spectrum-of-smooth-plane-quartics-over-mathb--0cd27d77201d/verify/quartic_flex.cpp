#include <bits/stdc++.h>
using namespace std;
struct Exp {int x,y,z;};
vector<Exp> mon4, mon7;
int index4[5][5][5],index7[8][8][8];
int pp[16];
int coefN[4][15][15];
int binom[5][5];
int nr=0;
struct Pt{int x,y,z;};
vector<Pt> pts;
int pmul(int a,int b){return (a*b)%3;}
int m3(int a){a%=3; return a<0?a+3:a;}
void init(){
 memset(index4,-1,sizeof(index4));memset(index7,-1,sizeof(index7));
 for(int x=4;x>=0;x--)for(int y=4-x;y>=0;y--){int z=4-x-y;index4[x][y][z]=mon4.size();mon4.push_back({x,y,z});}
 for(int x=7;x>=0;x--)for(int y=7-x;y>=0;y--){int z=7-x-y;index7[x][y][z]=mon7.size();mon7.push_back({x,y,z});}
 pp[0]=1; for(int i=1;i<=15;i++)pp[i]=pp[i-1]*3;
 for(int i=0;i<=4;i++){binom[i][0]=binom[i][i]=1;for(int j=1;j<i;j++)binom[i][j]=(binom[i-1][j-1]+binom[i-1][j])%3;}
 for(int j=0;j<15;j++){
   auto e=mon4[j];
   coefN[0][index4[e.y][e.x][e.z]][j]=1; // swap x/y
   coefN[1][index4[e.x][e.z][e.y]][j]=1; // swap y/z
   for(int k=0;k<=e.x;k++){int tar=index4[k][e.y+e.x-k][e.z];coefN[2][tar][j]=(coefN[2][tar][j]+binom[e.x][k])%3;}
   coefN[3][j][j]=(e.x%2?2:1);
 }
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
    if(!(x||y||z))continue;
    int d=(x?x:(y?y:z)); if(d==2)continue;
    pts.push_back({x,y,z});
 }
 assert(pts.size()==13);
}
int pack(const int a[15]){int first=0;while(first<15 && a[first]==0)first++;if(first==15)return 0;int scale=a[first]==2?2:1;int r=0;for(int j=0;j<15;j++)r+=pp[j]*((a[j]*scale)%3);return r;}
void unpack(int r,int a[15]){for(int j=0;j<15;j++){a[j]=r%3;r/=3;}}
int act(int enc,int t){int a[15],b[15]={};unpack(enc,a);
 for(int i=0;i<15;i++){
    int v=0;for(int j=0;j<15;j++)v+=coefN[t][i][j]*a[j];b[i]=v%3;
 }
 return pack(b);
}
int value(const int a[15],const Pt&p){int xs[5]={1,p.x,p.x*p.x%3,p.x*p.x*p.x%3,p.x*p.x*p.x*p.x%3},ys[5]={1,p.y,p.y*p.y%3,p.y*p.y*p.y%3,p.y*p.y*p.y*p.y%3},zs[5]={1,p.z,p.z*p.z%3,p.z*p.z*p.z%3,p.z*p.z*p.z*p.z%3};int r=0;
 for(int i=0;i<15;i++){auto e=mon4[i];r+=a[i]*xs[e.x]*ys[e.y]*zs[e.z];}return r%3;
}
int gradient(const int a[15],const Pt &p,int grad[3]){int xs[5]={1,p.x,p.x*p.x%3,p.x*p.x*p.x%3,p.x*p.x*p.x*p.x%3},ys[5]={1,p.y,p.y*p.y%3,p.y*p.y*p.y%3,p.y*p.y*p.y*p.y%3},zs[5]={1,p.z,p.z*p.z%3,p.z*p.z*p.z%3,p.z*p.z*p.z*p.z%3}; grad[0]=grad[1]=grad[2]=0;
 for(int i=0;i<15;i++){auto e=mon4[i];int c=a[i];if(e.x)grad[0]+=c*e.x*xs[e.x-1]*ys[e.y]*zs[e.z];if(e.y)grad[1]+=c*e.y*xs[e.x]*ys[e.y-1]*zs[e.z];if(e.z)grad[2]+=c*e.z*xs[e.x]*ys[e.y]*zs[e.z-1];}
 for(int i=0;i<3;i++)grad[i]%=3;
 return (grad[0]||grad[1]||grad[2]);
}
int coeff_t(const int a[15],const Pt&p,const Pt&q,int power){int r=0;int x[5][5],y[5][5],z[5][5];auto put=[&](int M[5][5],int s,int t){int S[5]={1,s,s*s%3,s*s*s%3,s*s*s*s%3};int T[5]={1,t,t*t%3,t*t*t%3,t*t*t*t%3};for(int d=0;d<=4;d++)for(int j=0;j<=d;j++)M[d][j]=binom[d][j]*S[d-j]*T[j]%3;};
 put(x,p.x,q.x);put(y,p.y,q.y);put(z,p.z,q.z);
 for(int i=0;i<15;i++){auto e=mon4[i];int c=0;for(int m=0;m<=e.x;m++)for(int n=0;n<=e.y;n++){int k=power-m-n;if(k<0||k>e.z)continue;c+=x[e.x][m]*y[e.y][n]*z[e.z][k];}r+=a[i]*(c%3);}
 return r%3;
}
int rank36(const int a[15]){
 int M[36][45]={};
 for(int j=0;j<15;j++){auto e=mon4[j];for(int k=0;k<3;k++){
   int expo[3]={e.x,e.y,e.z}; if(!expo[k])continue;
   expo[k]--;
   int coeff=a[j]*(expo[k]+1)%3; // degree 3 partial
   for(int f=0;f<15;f++){auto u=mon4[f];int idx=index7[expo[0]+u.x][expo[1]+u.y][expo[2]+u.z];M[idx][k*15+f]=(M[idx][k*15+f]+coeff)%3;}
 }}
 int rank=0;
 for(int col=0;col<45&&rank<36;col++){
    int pivot=rank;while(pivot<36 && M[pivot][col]==0)pivot++;
    if(pivot==36)continue;
    if(pivot!=rank)for(int k=col;k<45;k++)swap(M[pivot][k],M[rank][k]);
    int inv=(M[rank][col]==2?2:1);
    for(int k=col;k<45;k++)M[rank][k]=M[rank][k]*inv%3;
    for(int row=rank+1;row<36;row++)if(M[row][col]){int m=M[row][col];for(int k=col;k<45;k++)M[row][k]=m3(M[row][k]-m*M[rank][k]);}
    rank++;
 }
 return rank;
}
int main(int argc,char**argv){init();
 vector<unsigned char> seen(pp[15],0);vector<int> queue; queue.reserve(6000);
 long long total=0,smooth=0;map<pair<int,int>,array<long long,2>> counts;
 int norbit=0, nsmoothorb=0;int maxflex=-1;vector<pair<int,int>> maximizers;
 auto start=chrono::steady_clock::now();
 ofstream out("flex_orbits.tsv");out<<"enc\torbit_size\tsmooth\tpoints\tordinary_flex\thyperflex\n";
 for(int v=1;v<pp[15];v++){
     if(seen[v])continue;
     int a[15];unpack(v,a);int first=0;while(first<15&&a[first]==0)first++;
     if(first==15||a[first]!=1)continue;
     queue.clear();queue.push_back(v);seen[v]=1;
     for(size_t i=0;i<queue.size();i++){
       int enc=queue[i];for(int t=0;t<4;t++){
         int z=act(enc,t);if(!seen[z]){seen[z]=1;queue.push_back(z);}
       }
     }
     int sz=queue.size();total+=sz;norbit++;
     int rk=rank36(a);bool smooth_here=(rk==36);
     int npt=0,nflex=0,nhyper=0;
     if(smooth_here){
       smooth+=sz;nsmoothorb++;
       for(auto &p:pts)if(value(a,p)==0){npt++;int grad[3];if(!gradient(a,p,grad)){cerr<<"nonsmooth rational point!!";return 4;}
         Pt q={0,0,0};bool got=false;for(auto candidate:pts){
           if((grad[0]*candidate.x+grad[1]*candidate.y+grad[2]*candidate.z)%3 !=0)continue;
           if(candidate.x==p.x&&candidate.y==p.y&&candidate.z==p.z)continue;
           q=candidate;got=true;break;
         }
         if(!got){cerr<<"tangent line basis error";return 5;}
         if(coeff_t(a,p,q,1)!=0){cerr<<"tangent derivative inconsistency";return 6;}
         if(coeff_t(a,p,q,2)==0){if(coeff_t(a,p,q,3)==0)nhyper++;else nflex++;}
       }
       counts[{nflex,nhyper}][0]+=sz;counts[{nflex,nhyper}][1]++;
       if(nflex+nhyper>maxflex){maxflex=nflex+nhyper;maximizers.clear();}
       if(nflex+nhyper==maxflex)maximizers.push_back({v,sz});
     }
     out<<v<<'\t'<<sz<<'\t'<<smooth_here<<'\t'<<npt<<'\t'<<nflex<<'\t'<<nhyper<<'\n';
     if(norbit%100==0)cerr<<"orbits="<<norbit<<" total="<<total<<" smooth="<<smooth<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 }
 cout<<"total_forms "<<total<<" orbits "<<norbit<<" smooth_forms "<<smooth<<" smooth_orbits "<<nsmoothorb<<"\n";
 cout<<"ordinary_flex hyperflex equations projective_orbits\n";
 for(auto &it:counts)cout<<it.first.first<<" "<<it.first.second<<" "<<it.second[0]<<" "<<it.second[1]<<"\n";
 cout<<"max_total_flex "<<maxflex<<" maximizers_orbits ";for(auto x:maximizers)cout<<"("<<x.first<<","<<x.second<<") ";cout<<"\n";
 cerr<<"time="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
