#include <bits/stdc++.h>
using namespace std;int n,Q,scale=1,w[24],u[24];long long total=0,bad=0;bool anybad=false;
int gcd_(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
long long score(int*v){long long ret=0;for(int p=1;2*p<=n;p++){int t=0;while(t<n-p){if(v[t]!=v[t+p]){t++;continue;}int i=t;while(t<n-p&&v[t]==v[t+p])t++;int L=t-i;if(L<p)continue;bool valid=true;for(int d=1;d<p;d++){if(p%d)continue;bool smaller=true;for(int k=i;k<i+L+p-d;k++)if(v[k]!=v[k+d]){smaller=false;break;}if(smaller){valid=false;break;}}if(valid)ret+=(L+p)*(scale/p);}}return ret;}
void visit(int idx,int mx){if(idx==n){if(mx<2)return;total++;long long s=score(w);bool ok=false;for(int a=0;a<=mx;a++)for(int b=a+1;b<=mx;b++){for(int i=0;i<n;i++)u[i]=w[i]==b?a:w[i];if(score(u)>=s){ok=true;break;}}if(!ok){bad++;if(bad<10){cout<<"bad=";for(int i=0;i<n;i++)cout<<w[i];cout<<" score="<<s<<"/"<<scale<<"\n";}}return;}for(int k=0;k<=min(mx+1,Q-1);k++){w[idx]=k;visit(idx+1,max(mx,k));}}
int main(int argc,char**argv){n=atoi(argv[1]);Q=atoi(argv[2]);for(int i=2;i<=n/2;i++)scale=scale/gcd_(scale,i)*i;w[0]=0;visit(1,0);cout<<"n="<<n<<" checked="<<total<<" bad="<<bad<<"\n";}
