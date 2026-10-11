#include <bits/stdc++.h>
using namespace std;
const int P=1009;
int imod(int x){x%=P;if(x<0)x+=P;return x;}
int powmod(int a,int b){int r=1;for(;b;b>>=1,a=1LL*a*a%P)if(b&1)r=1LL*r*a%P;return r;}
struct HG{
 int n,D,Q,N;vector<vector<int>> digit,prod;vector<int> inv;
 HG(int n_):n(n_),D(2*n_),Q(1),N(0){for(int j=0;j<D;j++)Q*=3;N=3*Q;digit.resize(Q,vector<int>(D));for(int v=0;v<Q;v++){int x=v;for(int i=0;i<D;i++){digit[v][i]=x%3;x/=3;}}prod.assign(N,vector<int>(N));inv.assign(N,-1);for(int g=0;g<N;g++){int v=g/3,t=g%3;for(int h=0;h<N;h++){int w=h/3,s=h%3,z=0,mul=1,cross=0;for(int i=0;i<D;i++){z+=(digit[v][i]+digit[w][i])%3*mul;mul*=3;}for(int i=0;i<n;i++){cross+=digit[v][i]*digit[w][n+i]-digit[v][n+i]*digit[w][i];}int ct=(t+s+2*cross)%3;if(ct<0)ct+=3;prod[g][h]=3*z+ct;}}
 for(int g=0;g<N;g++)for(int h=0;h<N;h++)if(prod[g][h]==0){inv[g]=h;break;} }
 int symp(int a,int b){int res=0;for(int i=0;i<n;i++)res+=digit[a][i]*digit[b][n+i]-digit[a][n+i]*digit[b][i];return (res%3+3)%3;}
 int classify(int g,int h,int k){int pa=g/3,pb=h/3,pc=k/3;if(pa==pb&&pb==pc)return 2; if(pa==pb||pb==pc||pa==pc)return 1;int a=prod[inv[g]][h], b=prod[inv[g]][k];int va=a/3,vb=b/3; // affine collinearity in projection iff vb = 2*va
 bool col=true;for(int i=0;i<D;i++)if(digit[vb][i]!=(2*digit[va][i])%3){col=false;break;}
 if(col){if(prod[a][b]==0) return 2;return 1;}
 return symp(va,vb)==0?1:0;
 }
 int rank_mod(int a,int b,int c){int M=N;vector<int> m(M*M,0);int ss[3]={a,b,c};for(int g=0;g<M;g++)for(int h:ss){int row=prod[h][g];m[row*M+g]++;}int rk=0;vector<int> pinv(P,0);for(int i=1;i<P;i++)pinv[i]=powmod(i,P-2);for(int j=0;j<M;j++){
 int pick=rk;while(pick<M&&m[pick*M+j]%P==0)pick++;if(pick==M)continue;
 if(pick!=rk){for(int u=j;u<M;u++)swap(m[pick*M+u],m[rk*M+u]);}
 int iv=pinv[m[rk*M+j]%P];for(int u=j;u<M;u++)m[rk*M+u]=m[rk*M+u]*iv%P;
 for(int i=rk+1;i<M;i++){int x=m[i*M+j];if(x==0)continue;for(int u=j+1;u<M;u++)m[i*M+u]=imod(m[i*M+u]-x*m[rk*M+u]);m[i*M+j]=0;}rk++;if(rk==M)break;
 }return rk;}
};
int main(){HG g(1);map<int,int> cnt,wrong;for(int a=0;a<g.N;a++)for(int b=a+1;b<g.N;b++)for(int c=b+1;c<g.N;c++){int t=g.classify(a,b,c),want=(t==2?2*g.Q:(t==1?2*g.Q/3:2*g.Q/9));int got=g.N-g.rank_mod(a,b,c);cnt[got]++;if(got!=want){wrong[got]++;if(wrong[got]<5)cerr<<"FAIL "<<a<<" "<<b<<" "<<c<<" predicted="<<want<<" actual="<<got<<"\n";}}cout<<"N1_COUNTS";for(auto &p:cnt)cout<<" nullity="<<p.first<<":"<<p.second;cout<<" mismatches="<<accumulate(wrong.begin(),wrong.end(),0,[](int a,const auto&b){return a+b.second;})<<"\n";
 if(!wrong.empty()||cnt!=map<int,int>{{2,1944},{6,864},{18,117}})return 3;
 HG h(2);vector<array<int,3>> samp={ {0,1,2}, {0,1,3}, {0,1,4},{0,1,9},{0,1,10},{0,3,6},{0,3,9},{0,9,12},{0,27,30},{0,100,130},{0,91,200},{10,42,200}};map<int,int> scenarios;for(auto u:samp){int t=h.classify(u[0],u[1],u[2]),want=(t==2?2*h.Q:(t==1?2*h.Q/3:2*h.Q/9));int got=h.N-h.rank_mod(u[0],u[1],u[2]);scenarios[t]++;cout<<"N2_SAMPLE ("<<u[0]<<","<<u[1]<<","<<u[2]<<") class="<<t<<" predicted="<<want<<" actual="<<got<<"\n";if(want!=got)return 2;}cout<<"N2_SAMPLE_CLASSES";for(auto &p:scenarios)cout<<" class="<<p.first<<":"<<p.second;cout<<"\n";if(scenarios!=map<int,int>{{0,3},{1,7},{2,2}})return 4;cout<<"VERIFY_OK\n";return 0;}
