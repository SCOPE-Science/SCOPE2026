#include <bits/stdc++.h>
using namespace std;
struct Bits { uint64_t a[2]{0,0}; };
using Code = array<unsigned char,10>;
static vector<array<int,3>> V;
static vector<Bits> ADJ;
static vector<Code> maxima;
static long long nodes9=0,nodes10=0;
static inline int pc(const Bits& b){ return __builtin_popcountll(b.a[0])+__builtin_popcountll(b.a[1]); }
static inline bool emptyb(const Bits& b){ return !(b.a[0]|b.a[1]); }
static inline void clearbit(Bits& b,int i){ b.a[i>>6]&=~(1ULL<<(i&63)); }
static inline bool testbit(const Bits& b,int i){ return (b.a[i>>6]>>(i&63))&1ULL; }
static inline Bits band(const Bits& x,const Bits& y){ return {{x.a[0]&y.a[0],x.a[1]&y.a[1]}}; }
static int dist5(int a,int b){ int d=abs(a-b); return min(d,5-d); }
static bool compatible(const array<int,3>& x,const array<int,3>& y){
    for(int k=0;k<3;k++) if(dist5(x[k],y[k])==2) return true;
    return false;
}
static int id3(int a,int b,int c){ return 25*a+5*b+c; }
static array<int,3> xyz(int z){ return {z/25,(z/5)%5,z%5}; }
static void color_sort(Bits P, vector<int>& vs, vector<int>& bounds){
    vs.clear(); bounds.clear(); int color=0; Bits rem=P;
    while(!emptyb(rem)){
        ++color; Bits q=rem;
        while(!emptyb(q)){
            int v=q.a[0]?__builtin_ctzll(q.a[0]):64+__builtin_ctzll(q.a[1]);
            vs.push_back(v); bounds.push_back(color); clearbit(rem,v); clearbit(q,v);
            q.a[0]&=~ADJ[v].a[0]; q.a[1]&=~ADJ[v].a[1];
        }
    }
}
static void expand(Bits P, vector<int>& R,int target,long long& nodes,bool save){
    ++nodes;
    if((int)R.size()==target){
        if(save){ Code c{}; c[0]=0; for(int i=0;i<target;i++){auto p=V[R[i]]; c[i+1]=id3(p[0],p[1],p[2]);} sort(c.begin(),c.end()); maxima.push_back(c); }
        return;
    }
    if((int)R.size()+pc(P)<target) return;
    vector<int> vs,bounds; color_sort(P,vs,bounds);
    for(int i=(int)vs.size()-1;i>=0;i--){
        if((int)R.size()+bounds[i]<target) return;
        int v=vs[i]; if(!testbit(P,v)) continue;
        R.push_back(v); expand(band(P,ADJ[v]),R,target,nodes,save); R.pop_back(); clearbit(P,v);
    }
}
static vector<array<int,3>> perms3(){ vector<array<int,3>> p; array<int,3>a{0,1,2}; do p.push_back(a); while(next_permutation(a.begin(),a.end())); return p; }
static Code canonical(const Code& c,const vector<array<int,3>>& perms){
    Code best; best.fill(255); array<array<int,3>,10> pts; for(int i=0;i<10;i++)pts[i]=xyz(c[i]);
    for(int ai=0;ai<10;ai++) for(auto perm:perms) for(int sm=0;sm<8;sm++){
        Code t{};
        for(int j=0;j<10;j++){
            int y[3]; for(int k=0;k<3;k++){ int s=((sm>>k)&1)?-1:1; int v=s*(pts[j][perm[k]]-pts[ai][perm[k]]); v%=5;if(v<0)v+=5; y[k]=v; }
            t[j]=id3(y[0],y[1],y[2]);
        }
        sort(t.begin(),t.end()); if(t<best) best=t;
    }
    return best;
}
static int stabilizer(const Code& c,const vector<array<int,3>>& perms){
    array<bool,125> want{}; for(auto z:c)want[z]=true; array<array<int,3>,10> pts; for(int i=0;i<10;i++)pts[i]=xyz(c[i]);
    int stab=0;
    for(auto perm:perms) for(int sm=0;sm<8;sm++) for(int b0=0;b0<5;b0++)for(int b1=0;b1<5;b1++)for(int b2=0;b2<5;b2++){
        int bb[3]{b0,b1,b2}; array<bool,125> got{}; bool ok=true;
        for(int j=0;j<10;j++){
            int y[3]; for(int k=0;k<3;k++){ int s=((sm>>k)&1)?-1:1; int v=s*pts[j][perm[k]]+bb[k]; v%=5;if(v<0)v+=5; y[k]=v; }
            int z=id3(y[0],y[1],y[2]); if(got[z]){ok=false;break;} got[z]=true;
        }
        if(ok && got==want) ++stab;
    }
    return stab;
}
struct Rec{int cls,origin,stab,orbit; string rep;};
static string repstr(const Code& c){ string s; for(int i=0;i<10;i++){auto p=xyz(c[i]); if(i)s+=';'; s+=char('0'+p[0]);s+=char('0'+p[1]);s+=char('0'+p[2]);} return s; }
int main(int argc,char**argv){
    if(argc!=2){cerr<<"usage: verify ORBITS.csv\n"; return 2;}
    for(int a=0;a<5;a++)for(int b=0;b<5;b++)for(int c=0;c<5;c++){ array<int,3>x{a,b,c}; if(a==0&&b==0&&c==0)continue; if(compatible(x,{0,0,0}))V.push_back(x); }
    if(V.size()!=98){cerr<<"candidate count mismatch\n"; return 3;}
    ADJ.assign(V.size(),{}); for(int i=0;i<(int)V.size();i++)for(int j=0;j<(int)V.size();j++)if(i!=j&&compatible(V[i],V[j])) ADJ[i].a[j>>6]|=1ULL<<(j&63);
    Bits P{{~0ULL,~0ULL}}; for(int i=V.size();i<128;i++)clearbit(P,i); vector<int> R;
    expand(P,R,10,nodes10,false); if(nodes10<=0){return 4;} // tests a size-11 code including the fixed word
    expand(P,R,9,nodes9,true);
    if(maxima.size()!=31328){cerr<<"origin census mismatch "<<maxima.size()<<"\n";return 5;}
    // Directly recheck every saved code from the defining nonconfusability condition.
    set<Code> unique;
    for(auto &c:maxima){
        if(!unique.insert(c).second){cerr<<"duplicate maximum\n";return 6;}
        for(int i=0;i<10;i++)for(int j=i+1;j<10;j++)if(!compatible(xyz(c[i]),xyz(c[j]))){cerr<<"invalid maximum\n";return 7;}
    }
    auto perms=perms3(); map<Code,int> classes; for(auto &c:maxima)classes[canonical(c,perms)]++;
    if(classes.size()!=85){cerr<<"class count mismatch\n";return 8;}
    ifstream f(argv[1]); string line; getline(f,line); vector<Rec> expected;
    while(getline(f,line)){
        if(line.empty())continue; vector<string>x; size_t p=0; while(true){size_t q=line.find(',',p); if(q==string::npos){x.push_back(line.substr(p));break;}x.push_back(line.substr(p,q-p));p=q+1;}
        if(x.size()!=5){cerr<<"bad csv\n";return 9;} expected.push_back({stoi(x[0]),stoi(x[1]),stoi(x[2]),stoi(x[3]),x[4]});
    }
    if(expected.size()!=85){cerr<<"csv rows mismatch\n";return 10;}
    map<int,int> stabdist; long long orbit_sum=0; int ix=0;
    for(auto &[c,origin]:classes){
        int stab=stabilizer(c,perms), orbit=6000/stab; stabdist[stab]++; orbit_sum+=orbit;
        auto &e=expected[ix]; if(e.cls!=ix||e.origin!=origin||e.stab!=stab||e.orbit!=orbit||e.rep!=repstr(c)){cerr<<"orbit row mismatch "<<ix<<"\n";return 11;} ++ix;
    }
    if(orbit_sum!=391600){cerr<<"orbit sum mismatch\n";return 12;}
    long long by_incidence=125LL*maxima.size()/10; if(by_incidence!=391600){cerr<<"incidence count mismatch\n";return 13;}
    map<int,int> want{{1,53},{2,19},{3,2},{4,7},{8,1},{10,2},{40,1}}; if(stabdist!=want){cerr<<"stabilizer distribution mismatch\n";return 14;}
    Code special{}; string rr="000;002;120;122;240;242;310;312;430;432"; int z=0; for(int i=0;i<10;i++){int a=rr[z]-'0',b=rr[z+1]-'0',c=rr[z+2]-'0';special[i]=id3(a,b,c);z+=3;if(i<9)z++;} sort(special.begin(),special.end()); if(stabilizer(special,perms)!=40){cerr<<"special rep mismatch\n";return 15;}
    // target-10 search must have produced no solution; expand() saves only when save=true, so repeat with a counter-free dedicated test via the absence of side effects is not enough.
    // Its recursion reaches a solution only at target size; to certify zero, use a tiny second routine count below through a lambda.
    long long sol10=0,n2=0; function<void(Bits,int)> count10=[&](Bits Q,int depth){++n2;if(depth==10){++sol10;return;}if(depth+pc(Q)<10)return;vector<int>vs,bd;color_sort(Q,vs,bd);for(int i=(int)vs.size()-1;i>=0;i--){if(depth+bd[i]<10)return;int v=vs[i];if(!testbit(Q,v))continue;count10(band(Q,ADJ[v]),depth+1);clearbit(Q,v);}}; count10(P,0); if(sol10!=0){cerr<<"size-11 code exists\n";return 16;}
    cout<<"VERIFY_OK vertices=125 origin_candidates=98 origin_maxima="<<maxima.size()<<" maximum=10 labeled_maxima="<<by_incidence
        <<" natural_group=6000 orbits="<<classes.size()<<" stabilizers=1x53,2x19,3x2,4x7,8x1,10x2,40x1"
        <<" nodes9="<<nodes9<<" nodes10="<<n2<<" special_stabilizer=40\n";
}
