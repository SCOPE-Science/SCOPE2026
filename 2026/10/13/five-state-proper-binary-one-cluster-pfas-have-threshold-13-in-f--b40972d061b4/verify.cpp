#include <bits/stdc++.h>
using namespace std;

static const int N=5, BASE=6, MAPS=7776, MASKS=1<<N;
struct Map { array<int,N> f; bool total=false; bool one_cluster=false; };

bool is_one_cluster(const array<int,N>& f){
    for(int x:f) if(x<0) return false;
    int seen[N]={0}; int cycles=0;
    for(int s=0;s<N;s++) if(!seen[s]){
        int pos[N]; fill(pos,pos+N,-1); int path[N], L=0, v=s;
        while(!seen[v] && pos[v]<0){ pos[v]=L; path[L++]=v; v=f[v]; }
        if(pos[v]>=0) cycles++;
        for(int i=0;i<L;i++) seen[path[i]]=1;
    }
    return cycles==1;
}

vector<Map> build_maps(){
    vector<Map> V(MAPS);
    for(int code=0; code<MAPS; code++){
        int z=code; Map m; m.total=true;
        for(int i=0;i<N;i++){
            int d=z%BASE; z/=BASE; m.f[i]=d-1; if(d==0) m.total=false;
        }
        m.one_cluster=is_one_cluster(m.f); V[code]=m;
    }
    return V;
}

int trans_mask(const Map& m,int mask){
    int out=0;
    for(int s=0;s<N;s++) if(mask&(1<<s)){
        int y=m.f[s]; if(y<0) return -1; out|=1<<y;
    }
    return out;
}

int threshold_forward(const Map& a,const Map& b){
    int dist[MASKS]; fill(dist,dist+MASKS,-1);
    int q[MASKS],h=0,t=0; int start=MASKS-1;
    q[t++]=start; dist[start]=0;
    while(h<t){
        int m=q[h++]; if((m&(m-1))==0) return dist[m];
        int oa=trans_mask(a,m), ob=trans_mask(b,m);
        if(oa>=0 && dist[oa]<0){dist[oa]=dist[m]+1;q[t++]=oa;}
        if(ob>=0 && dist[ob]<0){dist[ob]=dist[m]+1;q[t++]=ob;}
    }
    return -1;
}

int threshold_reverse(const Map& a,const Map& b){
    int ta[MASKS],tb[MASKS];
    for(int m=1;m<MASKS;m++){ ta[m]=trans_mask(a,m); tb[m]=trans_mask(b,m); }
    int dist[MASKS]; fill(dist,dist+MASKS,-1);
    int q[MASKS],h=0,t=0;
    for(int s=0;s<N;s++){int m=1<<s;dist[m]=0;q[t++]=m;}
    while(h<t){
        int target=q[h++];
        for(int src=1;src<MASKS;src++) if(dist[src]<0 && (ta[src]==target || tb[src]==target)){
            dist[src]=dist[target]+1; q[t++]=src;
        }
    }
    return dist[MASKS-1];
}

array<int,N> relabel(const array<int,N>& f,const array<int,N>& p){
    array<int,N> g; g.fill(-1);
    for(int old=0;old<N;old++){
        int nw=p[old], y=f[old]; g[nw]=(y<0?-1:p[y]);
    }
    return g;
}

using Pair=array<array<int,N>,2>;
Pair canonical(const Map&a,const Map&b){
    array<int,N> p={0,1,2,3,4}; bool first=true; Pair best;
    do{
        auto aa=relabel(a.f,p), bb=relabel(b.f,p);
        Pair x={aa,bb}, y={bb,aa};
        if(first || x<best){best=x;first=false;}
        if(y<best) best=y;
    }while(next_permutation(p.begin(),p.end()));
    return best;
}

int main(){
    auto V=build_maps();
    long long oc=0; for(auto&m:V) oc+=m.one_cluster;
    if(oc!=1569) return 2;

    map<int,long long> hist; long long candidates=0, sync=0, boundary=0;
    map<Pair,long long> classes;
    for(int i=0;i<MAPS;i++) for(int j=0;j<MAPS;j++){
        const auto&a=V[i]; const auto&b=V[j];
        if(!(a.one_cluster||b.one_cluster)) continue;
        if(a.total&&b.total) continue;
        candidates++;
        int x=threshold_forward(a,b);
        int y=threshold_reverse(a,b);
        if(x!=y) return 3;
        if(x>=0){hist[x]++;sync++;}
        if(x==13){boundary++;classes[canonical(a,b)]++;}
        if(x>13) return 4;
    }

    map<int,long long> expected={{1,46510},{2,2023800},{3,3416160},{4,1715520},{5,432840},
        {6,276240},{7,163440},{8,64320},{9,36000},{10,22320},{11,4800},{12,3120},{13,1200}};
    if(candidates!=14594838LL || sync!=8206270LL || hist!=expected) return 5;
    if(boundary!=1200 || classes.size()!=5) return 6;

    vector<Pair> expected_classes={
        Pair{array<int,N>{-1,0,1,2,3},array<int,N>{2,4,3,1,3}},
        Pair{array<int,N>{-1,0,1,2,3},array<int,N>{4,4,1,2,3}},
        Pair{array<int,N>{-1,0,1,2,4},array<int,N>{2,3,4,4,1}},
        Pair{array<int,N>{-1,0,1,3,4},array<int,N>{2,3,4,4,1}},
        Pair{array<int,N>{-1,0,1,4,3},array<int,N>{2,3,4,4,1}}
    };
    for(auto&p:expected_classes){
        auto it=classes.find(p);
        if(it==classes.end() || it->second!=240) return 7;
    }
    for(auto&kv:classes) if(kv.second!=240) return 8;

    cout<<"VERIFY_OK states=5 alphabet=2 proper=1 one_cluster_maps=1569 "
        <<"candidates=14594838 synchronizing=8206270 max_threshold=13 "
        <<"boundary_labeled=1200 isomorphism_classes=5 "
        <<"orbit_sizes=240,240,240,240,240 engines=2 histogram=";
    bool first=true;
    for(auto&kv:expected){if(!first)cout<<",";first=false;cout<<kv.first<<":"<<kv.second;}
    cout<<"\n";
    return 0;
}
