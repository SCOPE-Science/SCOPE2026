#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int M=argc>1?atoi(argv[1]):40; vector<long long>N(M+1);
 int tail[6]={0,1,1,2,2,3},head[6]={1,2,3,0,1,2};
 for(int s=-1;s<4;s++)for(int t=-1;t<4;t++) {if ((s==-1)!=(t==-1) || (s>=0&&s==t))continue;
  int delta[4]={};if(s>=0){delta[s]=1;delta[t]=-1;}
  for(int a=0;3*a<=M+3;a++)for(int e=0;3*a+2*e<=M+3;e++)for(int c=0;c<=a+e+delta[1]&&3*a+2*e+c+delta[1]-delta[0]+delta[3]<=M;c++){
   int b=a+e+delta[1]-c,d=a-delta[0],f=c+delta[3];if(b<0||d<0||f<0)continue;
   int w[6]={a,b,c,d,e,f};int m=0;for(int x:w)m+=x;if(m>M)continue;
   if(m==0){if(s>=0)continue;for(int L=1;L<=M;L++)N[L]+=2;continue;}
   int par[4]={0,1,2,3};auto root=[&](int v){while(par[v]!=v)v=par[v];return v;};
   int occ=0;for(int i=0;i<6;i++)if(w[i]){occ|=1<<tail[i];occ|=1<<head[i];par[root(tail[i])]=root(head[i]);}
   int r=-1;bool ok=true;for(int v=0;v<4;v++)if(occ>>v&1){if(r<0)r=root(v);else if(root(v)!=r)ok=false;}
   if(!ok)continue;
   bool p0=occ&1,p3=occ&8;
   for(int L=0;m+L<=M;L++){
     if(p0&&p3)N[m+L]+=L+1;
     else if(p0||p3)N[m+L]++;
     else if(L==0)N[m]++;
   }
  }
 }
 for(int m=1;m<=M;m++)cout<<m+2<<" "<<N[m]<<"\n";
}
