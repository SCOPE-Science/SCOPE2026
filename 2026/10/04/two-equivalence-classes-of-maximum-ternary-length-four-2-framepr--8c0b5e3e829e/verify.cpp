#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using U=__uint128_t;
struct Tri{int a,b,c;};
vector<array<int,4>> W; vector<Tri> bad; U pf[81][81];
unsigned long long nodes=0,count12=0; vector<U> sols; int target=13; bool found=false;
inline int pc(U x){return __builtin_popcountll((unsigned long long)x)+__builtin_popcountll((unsigned long long)(x>>64));}
inline int fb(U x){auto lo=(unsigned long long)x;if(lo)return __builtin_ctzll(lo);return 64+__builtin_ctzll((unsigned long long)(x>>64));}
int ub(U sel,U cand){
    int n=pc(cand),m=0; U rem=cand;
    while(rem){int u=fb(rem);rem&=~((U)1<<u);U nbr=0,ss=sel;while(ss){int s=fb(ss);ss&=~((U)1<<s);nbr|=pf[u][s];}nbr&=rem;if(nbr){int v=fb(nbr);rem&=~((U)1<<v);m++;}}
    int p=0; U used=0; for(auto&t:bad){U tm=((U)1<<t.a)|((U)1<<t.b)|((U)1<<t.c);if((tm&cand)==tm&&!(tm&used)){used|=tm;p++;}}
    return n-max(m,p);
}
bool search13(U sel,U cand){
    nodes++; int k=pc(sel); if(k>=target)return true; if(k+pc(cand)<target||k+ub(sel,cand)<target||!cand)return false;
    int v=-1,bs=-1;U cc=cand;while(cc){int x=fb(cc);cc&=~((U)1<<x);U nbr=0,ss=sel;while(ss){int s=fb(ss);ss&=~((U)1<<s);nbr|=pf[x][s];}int sc=pc(nbr&cand);if(sc>bs){bs=sc;v=x;}}
    U nc=cand&~((U)1<<v),ss=sel;while(ss){int s=fb(ss);ss&=~((U)1<<s);nc&=~pf[v][s];}
    if(search13(sel|((U)1<<v),nc))return true; return search13(sel,cand&~((U)1<<v));
}
void enum12(U sel,U cand){
    nodes++;int k=pc(sel);if(k==12){count12++;sols.push_back(sel);return;}if(k+pc(cand)<12||k+ub(sel,cand)<12||!cand)return;
    int v=-1,bs=-1;U cc=cand;while(cc){int x=fb(cc);cc&=~((U)1<<x);U nbr=0,ss=sel;while(ss){int s=fb(ss);ss&=~((U)1<<s);nbr|=pf[x][s];}int sc=pc(nbr&cand);if(sc>bs){bs=sc;v=x;}}
    U nc=cand&~((U)1<<v),ss=sel;while(ss){int s=fb(ss);ss&=~((U)1<<s);nc&=~pf[v][s];}
    enum12(sel|((U)1<<v),nc);enum12(sel,cand&~((U)1<<v));
}
bool valid(U s){for(auto&t:bad)if(((s>>t.a)&1)&&((s>>t.b)&1)&&((s>>t.c)&1))return false;return true;}
struct Key{array<unsigned char,12>a;bool operator<(Key const&o)const{return a<o.a;}};
int main(){
    for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)for(int d=0;d<3;d++)W.push_back({a,b,c,d}); memset(pf,0,sizeof(pf));
    for(int a=0;a<81;a++)for(int b=a+1;b<81;b++)for(int c=b+1;c<81;c++){
        int ids[3]={a,b,c};bool fail=false;for(int t=0;t<3;t++){auto x=W[ids[t]],y=W[ids[(t+1)%3]],z=W[ids[(t+2)%3]];bool ok=true;for(int j=0;j<4;j++)if(x[j]!=y[j]&&x[j]!=z[j]){ok=false;break;}if(ok){fail=true;break;}}
        if(fail){bad.push_back({a,b,c});pf[a][b]|=(U)1<<c;pf[b][a]|=(U)1<<c;pf[a][c]|=(U)1<<b;pf[c][a]|=(U)1<<b;pf[b][c]|=(U)1<<a;pf[c][b]|=(U)1<<a;}
    }
    if(bad.size()!=18792){cerr<<"bad triple mismatch\n";return 1;}
    unsigned long long n13[4];
    for(int d=1;d<=4;d++){int sec=0;for(int j=0;j<4;j++)sec=sec*3+(j<d?1:0);U sel=((U)1)|((U)1<<sec),cand=0;for(int i=0;i<81;i++)if(i&&i!=sec)cand|=(U)1<<i;cand&=~pf[0][sec];nodes=0;if(search13(sel,cand)){cerr<<"found forbidden 13-code at distance "<<d<<"\n";return 2;}n13[d-1]=nodes;}
    U cand=0;for(int i=1;i<81;i++)cand|=(U)1<<i;nodes=0;count12=0;sols.clear();enum12((U)1,cand);auto enum_nodes=nodes;
    if(count12!=832){cerr<<"normalized maximum count mismatch\n";return 3;}
    unsigned long long total=count12*81/12;if(total!=5616){cerr<<"total count mismatch\n";return 4;}
    array<int,3> p3={0,1,2};array<array<int,3>,6> perms3{};int pi=0;do{perms3[pi++]={p3[0],p3[1],p3[2]};}while(next_permutation(p3.begin(),p3.end()));
    vector<array<int,4>> perms4;array<int,4> p4={0,1,2,3};do{perms4.push_back(p4);}while(next_permutation(p4.begin(),p4.end()));
    vector<array<unsigned char,81>> maps;maps.reserve(31104);for(auto cp:perms4)for(int s0=0;s0<6;s0++)for(int s1=0;s1<6;s1++)for(int s2=0;s2<6;s2++)for(int s3=0;s3<6;s3++){array<unsigned char,81> mp{};int ss[4]={s0,s1,s2,s3};for(int i=0;i<81;i++){array<int,4> y;for(int j=0;j<4;j++)y[j]=perms3[ss[j]][W[i][cp[j]]];mp[i]=((y[0]*3+y[1])*3+y[2])*3+y[3];}maps.push_back(mp);}
    map<Key,int> cnt;for(U sol:sols){vector<int> ids;for(int i=0;i<81;i++)if((sol>>i)&1)ids.push_back(i);Key best;best.a.fill(255);for(auto&mp:maps){array<unsigned char,12>a;for(int k=0;k<12;k++)a[k]=mp[ids[k]];sort(a.begin(),a.end());if(a<best.a)best.a=a;}cnt[best]++;}
    if(cnt.size()!=2){cerr<<"orbit count mismatch\n";return 5;}
    vector<int> orbit_sizes,stabs,norm_counts;vector<Key> reps;for(auto&kv:cnt){U set=0;for(auto x:kv.first.a)set|=(U)1<<x;int stab=0;for(auto&mp:maps){U t=0;for(auto x:kv.first.a)t|=(U)1<<mp[x];if(t==set)stab++;}norm_counts.push_back(kv.second);stabs.push_back(stab);orbit_sizes.push_back(31104/stab);reps.push_back(kv.first);if(!valid(set)){cerr<<"invalid representative\n";return 6;}}
    if(norm_counts!=vector<int>({768,64})||stabs!=vector<int>({6,72})||orbit_sizes!=vector<int>({5184,432})){cerr<<"orbit data mismatch\n";return 7;}
    if(orbit_sizes[0]+orbit_sizes[1]!=(int)total){cerr<<"orbit sum mismatch\n";return 8;}
    if(orbit_sizes[0]*12/81!=norm_counts[0]||orbit_sizes[1]*12/81!=norm_counts[1]){cerr<<"incidence mismatch\n";return 9;}
    cout<<"VERIFY_OK bad_triples="<<bad.size()<<" maximum=12 labeled_maxima="<<total<<" normalized_with_0000="<<count12<<" orbits=2 orbit_sizes=5184,432 stabilizers=6,72 normalized_orbit_counts=768,64 search13_nodes="<<n13[0]<<","<<n13[1]<<","<<n13[2]<<","<<n13[3]<<" enum_nodes="<<enum_nodes<<"\n";
    cout<<"REP1=";for(auto x:reps[0].a){auto w=W[x];cout<<w[0]<<w[1]<<w[2]<<w[3]<<" ";}cout<<"\nREP2=";for(auto x:reps[1].a){auto w=W[x];cout<<w[0]<<w[1]<<w[2]<<w[3]<<" ";}cout<<"\n";
}
