// Exhaustive finite-field Jacobian checks for cubic nets over the binary field.
// GF(8) and GF(16) are represented by t^3+t+1 and t^4+t+1.
#include <bits/stdc++.h>
using namespace std;
int ex[10][3]; int degree=3, poly=11;
int mul(int a,int b){int c=0;for(int j=0;j<degree;j++){if((b>>j)&1)c ^=a<<j;}for(int j=2*degree-2;j>=degree;j--){if((c>>j)&1)c^=poly<<(j-degree);}return c;}
int pow3(int a,int n){int b=1;while(n--){b=mul(b,a);}return b;}
vector<array<int,3>> points;
void make_points(){points.clear();int q=(1<<degree); for(int y=0;y<q;y++)for(int z=0;z<q;z++)points.push_back({1,y,z});for(int z=0;z<q;z++)points.push_back({0,1,z});points.push_back({0,0,1});}
int eval(int f,int x,int y,int z,int j){int v=0;for(int k=0;k<10;k++)if((f>>k)&1){int e0=ex[k][0],e1=ex[k][1],e2=ex[k][2];if(j==0){if(!(e0&1))continue;e0--;}if(j==1){if(!(e1&1))continue;e1--;}if(j==2){if(!(e2&1))continue;e2--;}v^=mul(mul(pow3(x,e0),pow3(y,e1)),pow3(z,e2));}return v;}
array<int,3> canonical_basis(int a,int b,int c){int r[3]={a,b,c};int n=0;for(int p=9;p>=0;p--){int k=n;while(k<3 && !((r[k]>>p)&1)) k++;if(k==3)continue;swap(r[n],r[k]);for(int j=0;j<3;j++)if(j!=n && ((r[j]>>p)&1))r[j]^=r[n];n++;if(n==3)break;}return {r[0],r[1],r[2]};}
int main(){int ix=0;for(int a=3;a>=0;a--)for(int b=3-a;b>=0;b--){int c=3-a-b;ex[ix][0]=a;ex[ix][1]=b;ex[ix][2]=c;ix++;}cerr<<"monomials: ";for(int i=0;i<10;i++)cerr<<ex[i][0]<<ex[i][1]<<ex[i][2]<<" ";cerr<<"\n";
make_points();
vector<int> smooth(1024,0),s;
for(int f=1;f<1024;f++){bool ok=true;for(auto [x,y,z]:points){if(eval(f,x,y,z,-1)==0 && eval(f,x,y,z,0)==0 && eval(f,x,y,z,1)==0 && eval(f,x,y,z,2)==0){ok=false;break;}}if(ok){ degree=4;poly=19;make_points(); for(auto [x,y,z]:points){if(eval(f,x,y,z,-1)==0 && eval(f,x,y,z,0)==0 && eval(f,x,y,z,1)==0 && eval(f,x,y,z,2)==0){ok=false;break;}}degree=3;poly=11;make_points();}if(ok){smooth[f]=1;s.push_back(f);}}
cerr<<"Smooth count "<<s.size()<<"\n";
set<pair<int,int>> pencils; // canonical rref rows 
for(int a:s)for(int b:s)if(a<b && smooth[a^b]){auto z=canonical_basis(a,b,0);pencils.insert({z[0],z[1]});}
cerr<<"pencils count "<<pencils.size()<<"\n";
set<array<int,3>> nets;
for(auto [a,b]:pencils){for(int c:s){if(!smooth[c^a]||!smooth[c^b]||!smooth[c^a^b])continue;auto R=canonical_basis(a,b,c);if(R[2]==0)continue;nets.insert(R);}}
cerr<<"nets count "<<nets.size()<<"\n";
if(s.size()!=336 || pencils.size()!=5544 || nets.size()!=864) return 1;
cout << "smooth_cubics=" << s.size() << "\nall_smooth_pencils=" << pencils.size() << "\nall_smooth_nets=" << nets.size() << "\n";
return 0;}
