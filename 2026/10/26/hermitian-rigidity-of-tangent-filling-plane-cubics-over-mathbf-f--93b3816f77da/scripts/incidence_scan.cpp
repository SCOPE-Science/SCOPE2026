// Exact exhaustive incidence search over F4, represented by F2[a]/(a^2+a+1).
#include <bits/stdc++.h>
using namespace std;
// F4 field bits, alpha^2=alpha+1
int mul(int a,int b){int v=0;for(int i=0;i<2;i++)if(b>>i&1)v ^= a<<i;if(v&8)v^=0b1100;if(v&4)v^=0b111;return v;}
int pw(int a,int n){int r=1;for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r;}
int main(){int mx[10][3], k=0; for(int i=3;i>=0;i--)for(int j=3-i;j>=0;j--){int l=3-i-j;mx[k][0]=i;mx[k][1]=j;mx[k++][2]=l;}
 vector<array<int,3>> pts;
 for(int y=0;y<4;y++)for(int z=0;z<4;z++)pts.push_back({1,y,z});for(int z=0;z<4;z++)pts.push_back({0,1,z});pts.push_back({0,0,1});
 int mon[21][10],dx[21][10],dy[21][10],dz[21][10];for(int p=0;p<21;p++)for(int m=0;m<10;m++){int x=pts[p][0],y=pts[p][1],z=pts[p][2],a=mx[m][0],b=mx[m][1],c=mx[m][2];mon[p][m]=mul(mul(pw(x,a),pw(y,b)),pw(z,c));dx[p][m]=(a&1)?mul(mul(pw(x,a-1),pw(y,b)),pw(z,c)):0;dy[p][m]=(b&1)?mul(mul(pw(x,a),pw(y,b-1)),pw(z,c)):0;dz[p][m]=(c&1)?mul(mul(pw(x,a),pw(y,b)),pw(z,c-1)):0;}

 int Pline[21][21];for(int l=0;l<21;l++)for(int p=0;p<21;p++){auto q=pts[l];auto t=pts[p];Pline[l][p]=(mul(q[0],t[0])^mul(q[1],t[1])^mul(q[2],t[2]))==0;}
 long counts[22]={};long raw=0,tangent=0;map<int,int> pointdist;vector<uint32_t> solutions, no_line;long line_divisible=0;
 for(uint32_t code=1;code<1048576u;code++){uint32_t co=code;int coeff[10];int last=0;for(int i=0;i<10;i++){coeff[i]=co&3;co>>=2;if(coeff[i])last=i;}if(coeff[last]!=1)continue;raw++;
  uint32_t mask=0,rationalmask=0;int nn=0; for(int p=0;p<21;p++){int f=0;for(int m=0;m<10;m++)f^=mul(coeff[m],mon[p][m]);if(f)continue;nn++;rationalmask|=1u<<p;int vx=0,vy=0,vz=0;for(int m=0;m<10;m++){vx^=mul(coeff[m],dx[p][m]);vy^=mul(coeff[m],dy[p][m]);vz^=mul(coeff[m],dz[p][m]);}if(!(vx|vy|vz))continue;int lid=-1;for(int l=0;l<21;l++)if(pts[l]==array<int,3>{vx,vy,vz})lid=l; if(lid<0){int inv=pw(vx?vx:(vy?vy:vz),2);for(int l=0;l<21;l++)if(pts[l]==array<int,3>{mul(vx,inv),mul(vy,inv),mul(vz,inv)})lid=l;}if(lid<0)abort(); mask|=1u<<lid; }
 int covered=0;for(int p=0;p<21;p++)for(int l=0;l<21;l++)if(mask>>l&1 && Pline[l][p]){covered++;break;}
 counts[covered]++;if(covered==21){tangent++;pointdist[nn]++;solutions.push_back(code); bool hasline=false;for(int l=0;l<21;l++){uint32_t linebits=0;for(int p=0;p<21;p++)if(Pline[l][p])linebits|=1u<<p; if((rationalmask&linebits)==linebits)hasline=true;} if(hasline)line_divisible++;else no_line.push_back(code);}
 }
 cout<<"#normalized "<<raw<<" #tangent "<<tangent<<"\n";for(int i=0;i<=21;i++)if(counts[i])cout<<i<<":"<<counts[i]<<" ";cout<<"\npoint distributions ";for(auto [x,y]:pointdist)cout<<x<<":"<<y<<" ";cout<<"\nline_divisible "<<line_divisible<<" no_rational_line "<<no_line.size()<<"\nmonomials";for(int i=0;i<10;i++)cout<<" ("<<mx[i][0]<<","<<mx[i][1]<<","<<mx[i][2]<<")";cout<<"\n";ofstream out("tangent_codes.txt");for(auto x:solutions)out<<x<<"\n";ofstream out2("tangent_noline_codes.txt");for(auto x:no_line)out2<<x<<"\n";
}
