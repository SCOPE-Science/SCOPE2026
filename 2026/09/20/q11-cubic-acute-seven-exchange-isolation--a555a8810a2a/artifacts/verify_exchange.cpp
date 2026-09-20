#include <bits/stdc++.h>
using namespace std;
static constexpr int D=11, V=1<<D; static constexpr uint32_t VMASK=V-1;
inline bool between(uint32_t y,uint32_t x,uint32_t z){
    uint32_t equal=(~(x^z))&VMASK;
    return ((y^x)&equal)==0;
}
inline bool good3(uint32_t a,uint32_t b,uint32_t c){
    return !between(a,b,c)&&!between(b,a,c)&&!between(c,a,b);
}
static vector<uint32_t> B;
static vector<vector<uint32_t>> conflict_edges;
static vector<int> C, chosen;
static vector<vector<unsigned char>> pair_ok;
static uint32_t rm;

bool candidate_ok(int v){
    for(uint32_t e: conflict_edges[v]) if((e&rm)==0) return false;
    for(int i=0;i<24;i++) if(!(rm>>i&1) && v==(int)B[i]) return false;
    return true;
}
bool pair_compatible(int v,int w){
    for(int i=0;i<24;i++) if(!(rm>>i&1) && !good3(v,w,B[i])) return false;
    return true;
}
bool extend_dfs(int start,int need){
    if(need==0) return true;
    int m=(int)C.size();
    for(int idx=start;idx<=m-need;idx++){
        bool ok=true;
        for(int q:chosen) if(!pair_ok[idx][q]){ok=false;break;}
        if(!ok) continue;
        for(int i=0;i<(int)chosen.size() && ok;i++)
            for(int j=i+1;j<(int)chosen.size();j++)
                if(!good3(C[idx],C[chosen[i]],C[chosen[j]])){ok=false;break;}
        if(!ok) continue;
        chosen.push_back(idx);
        if(extend_dfs(idx+1,need-1)) return true;
        chosen.pop_back();
    }
    return false;
}
long long relevant=0; int max_candidates=0; bool found=false; int current_r;
void process_mask(){
    C.clear();
    for(int v=0;v<V;v++) if(candidate_ok(v)) C.push_back(v);
    int need=current_r+1;
    if((int)C.size()<need) return;
    relevant++; max_candidates=max(max_candidates,(int)C.size());
    int m=C.size(); pair_ok.assign(m,vector<unsigned char>(m,0));
    for(int i=0;i<m;i++) for(int j=i+1;j<m;j++)
        pair_ok[i][j]=pair_ok[j][i]=pair_compatible(C[i],C[j]);
    chosen.clear();
    if(extend_dfs(0,need)) found=true;
}
void enumerate_rm(int next,int left){
    if(found) return;
    if(left==0){process_mask(); return;}
    for(int i=next;i<=24-left;i++){
        rm|=(1u<<i); enumerate_rm(i+1,left-1); rm&=~(1u<<i);
        if(found) return;
    }
}
int main(){
    vector<string> s={
"11000000000","00110100111","00001100000","01111100010","11010101010","10100001001",
"10011000111","11010110111","10001111111","11101011011","01111011101","01000101100",
"10101100101","10010010100","10100110110","10110001110","00001010110","00111011010",
"10011111000","00110010001","11111110001","00000101011","11101000110","01000010011"};
    for(auto &x:s) B.push_back(stoul(x,nullptr,2));
    for(int i=0;i<24;i++) for(int j=i+1;j<24;j++) for(int k=j+1;k<24;k++)
        if(!good3(B[i],B[j],B[k])){ cerr<<"base construction invalid\n"; return 2; }
    conflict_edges.assign(V,{});
    for(int v=0;v<V;v++) for(int i=0;i<24;i++) for(int j=i+1;j<24;j++)
        if(v!=(int)B[i] && v!=(int)B[j] && !good3(v,B[i],B[j]))
            conflict_edges[v].push_back((1u<<i)|(1u<<j));
    cout<<"base_valid 24\n";
    for(current_r=0;current_r<=7;current_r++){
        rm=0; relevant=0; max_candidates=0; found=false;
        enumerate_rm(0,current_r);
        cout<<"removed="<<current_r<<" add="<<(current_r+1)
            <<" improvement="<<(found?"FOUND":"NONE")
            <<" relevant_masks="<<relevant<<" max_candidates="<<max_candidates<<"\n";
        if(found) return 1;
    }
    cout<<"conclusion: no size-25 general-position set intersects the displayed size-24 set in 17 or more vertices\n";
    return 0;
}
