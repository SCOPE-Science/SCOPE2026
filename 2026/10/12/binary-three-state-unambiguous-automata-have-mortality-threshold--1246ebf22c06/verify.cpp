#include <bits/stdc++.h>
using namespace std;

static int multtab[512][512];

static inline int bit(int code,int r,int c){ return (code>>(3*r+c))&1; }

static int ordinary_product_code(int A,int B){
    int out=0;
    for(int i=0;i<3;i++) for(int j=0;j<3;j++){
        int s=0;
        for(int k=0;k<3;k++) s += bit(A,i,k)*bit(B,k,j);
        if(s>1) return -1;
        if(s) out |= 1<<(3*i+j);
    }
    return out;
}

static int boolean_product_code_independent(int A,int B){
    int out=0;
    for(int i=0;i<3;i++){
        int row=(A>>(3*i))&7;
        for(int j=0;j<3;j++){
            int col = ((B>>j)&1) | (((B>>(3+j))&1)<<1) | (((B>>(6+j))&1)<<2);
            if(row & col) out |= 1<<(3*i+j);
        }
    }
    return out;
}

struct Eval { bool unamb; int mortal_dist; string word; };

static Eval eval_pair(int A,int B){
    const int I=(1<<0)|(1<<4)|(1<<8);
    array<int,512> dist; dist.fill(-1);
    array<short,512> par; par.fill(-1);
    array<char,512> pcl; pcl.fill(0);
    queue<int> q; dist[I]=0; q.push(I);
    bool unamb=true;
    while(!q.empty()){
        int X=q.front(); q.pop();
        int gens[2]={A,B};
        for(int s=0;s<2;s++){
            int Y=multtab[X][gens[s]];
            if(Y<0){ unamb=false; continue; }
            // independent relational composition must agree whenever integer product is 0/1
            if(boolean_product_code_independent(X,gens[s])!=Y){ cerr<<"semiring disagreement\n"; exit(20); }
            if(dist[Y]<0){ dist[Y]=dist[X]+1; par[Y]=X; pcl[Y]=char('a'+s); q.push(Y); }
        }
    }
    if(!unamb) return {false,-1,""};
    if(dist[0]<0) return {true,-1,""};
    string w; int x=0;
    while(x!=I){ w.push_back(pcl[x]); x=par[x]; }
    reverse(w.begin(),w.end());
    return {true,dist[0],w};
}

static int relabel(int A,const array<int,3>& p){
    int out=0;
    for(int i=0;i<3;i++) for(int j=0;j<3;j++) if(bit(A,i,j)) out |= 1<<(3*p[i]+p[j]);
    return out;
}

static pair<int,int> canonical_pair(int A,int B){
    array<int,3> p={0,1,2};
    pair<int,int> best={1000,1000};
    do{
        int X=relabel(A,p), Y=relabel(B,p);
        best=min(best,{X,Y}); best=min(best,{Y,X});
    }while(next_permutation(p.begin(),p.end()));
    return best;
}

static bool partial_deterministic(int A){
    for(int i=0;i<3;i++) if(__builtin_popcount((A>>(3*i))&7)>1) return false;
    return true;
}

static bool strongly_connected_union(int A,int B){
    for(int s=0;s<3;s++){
        bool seen[3]={0,0,0}; queue<int>q; q.push(s);seen[s]=1;
        while(!q.empty()){
            int x=q.front();q.pop();
            for(int G: {A,B}) for(int y=0;y<3;y++) if(bit(G,x,y)&&!seen[y]){seen[y]=1;q.push(y);} 
        }
        for(bool z:seen) if(!z) return false;
    }
    return true;
}

static int word_product(const string& w,int A,int B){
    int X=(1<<0)|(1<<4)|(1<<8);
    for(char c:w){ X=ordinary_product_code(X,c=='a'?A:B); if(X<0) return -2; }
    return X;
}

int main(){
    for(int A=0;A<512;A++) for(int B=0;B<512;B++) multtab[A][B]=ordinary_product_code(A,B);
    long long unamb=0,mortal=0; map<int,long long> hist; vector<pair<int,int>> ext;
    int maxd=-1;
    for(int A=0;A<512;A++) for(int B=0;B<512;B++){
        Eval e=eval_pair(A,B);
        if(!e.unamb) continue;
        unamb++;
        if(e.mortal_dist>=0){ mortal++; hist[e.mortal_dist]++; maxd=max(maxd,e.mortal_dist); if(e.mortal_dist==6) ext.push_back({A,B}); }
        if(e.mortal_dist>6){ cerr<<"distance above six\n"; return 2; }
    }
    map<int,long long> expected={{1,271},{2,3552},{3,3192},{4,540},{5,132},{6,12}};
    if(unamb!=12502 || mortal!=7699 || hist!=expected || maxd!=6 || ext.size()!=12){
        cerr<<"census mismatch unamb="<<unamb<<" mortal="<<mortal<<" max="<<maxd<<" ext="<<ext.size()<<"\n";
        for(auto &kv:hist) cerr<<kv.first<<":"<<kv.second<<" "; cerr<<"\n"; return 3;
    }
    set<pair<int,int>> cls;
    for(auto [A,B]:ext) cls.insert(canonical_pair(A,B));
    if(cls.size()!=1 || *cls.begin()!=make_pair(10,98)){ cerr<<"canonical mismatch\n"; return 4; }
    if(!partial_deterministic(10)||!partial_deterministic(98)||!strongly_connected_union(10,98)) return 5;
    Eval e=eval_pair(10,98);
    if(!e.unamb || e.mortal_dist!=6 || e.word!="abaaba"){
        cerr<<"witness mismatch d="<<e.mortal_dist<<" word="<<e.word<<"\n"; return 6;
    }
    for(int n=0;n<6;n++){
        for(int code=0;code<(1<<n);code++){
            string w(n,'a'); for(int i=0;i<n;i++) if((code>>(n-1-i))&1) w[i]='b';
            if(word_product(w,10,98)==0){ cerr<<"shorter killer "<<w<<"\n"; return 7; }
        }
    }
    if(word_product("abaaba",10,98)!=0) return 8;
    cout<<"VERIFY_OK states=3 alphabet=2 labeled_pairs=262144 unambiguous=12502 mortal=7699 "
        <<"threshold_hist=1:271,2:3552,3:3192,4:540,5:132,6:12 max=6 extremizers=12 "
        <<"isomorphism_classes=1 canonical=10,98 witness=abaaba deterministic_extremal=1 transitive_extremal=1 engines=2\n";
}
