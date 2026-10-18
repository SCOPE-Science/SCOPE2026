#include <bits/stdc++.h>
using namespace std;
struct Field {int k,q,poly; vector<vector<int>> mul; Field(int kk,int pp):k(kk),q(1<<kk),poly(pp),mul(q,vector<int>(q)){for(int x=0;x<q;x++)for(int y=0;y<q;y++){int z=0,a=x,b=y;while(b){if(b&1)z^=a;b>>=1;a<<=1;if(a&q)a^=poly;}mul[x][y]=z;}}};
array<int,3> powers(int a,int b,Field&f){return {f.mul[a][a], f.mul[a][b], f.mul[b][b]};}
int eval(int mask, array<int,3> U, array<int,3> V,Field &f){int acc=0;for(int i=0;i<9;i++)if(mask>>i&1)acc ^= f.mul[U[i/3]][V[i%3]];return acc;}
int main(){vector<array<int,4>> reps;int a,b,c,size;while(cin>>a>>b>>c>>size)reps.push_back({a,b,c,size});int polys[]={0,0x3,0x7,0xb,0x13,0x25,0x43,0x83,0x11b};
 for(auto rep:reps){int cnt[9]={};for(int k=1;k<=8;k++){Field f(k,polys[k]);vector<array<int,3>> P;for(int t=0;t<f.q;t++)P.push_back(powers(t,1,f));P.push_back(powers(1,0,f));for(auto U:P)for(auto V:P)if(eval(rep[0],U,V,f)==0&&eval(rep[1],U,V,f)==0)cnt[k]++;}
 vector<int> orb(9);int sup=0;for(int k=1;k<=8;k++){int m=cnt[k];for(int d=1;d<k;d++)if(k%d==0)m-=d*orb[d];if(m%k){cerr<<"BAD DIVISIBILITY\n";return 1;}orb[k]=m/k;sup+=k*orb[k];}cout<<"REP "<<rep[0]<<" "<<rep[1]<<" "<<rep[2]<<" size "<<rep[3]<<" support "<<sup<<" degrees";for(int k=1;k<=8;k++)if(orb[k])cout<<" "<<k<<":"<<orb[k];cout<<" counts";for(int k=1;k<=8;k++)cout<<" "<<cnt[k];cout<<"\n";}
}
