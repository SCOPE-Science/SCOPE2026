// Exact finite-field computation for transverse binary cubic-surface sections.
// Usage: c++ -std=c++17 -O2 verify_census.cpp -o verify_census
//        ./verify_census > census_output.txt
// Writes extremal_coefficients.txt in the working directory.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using UInt = uint32_t;
using Exp = array<int,4>;
int parity(UInt n){ return __builtin_parity(n); }
int eval_monomial(int x, Exp e){
    for(int j=0;j<4;j++) if(e[j]>0 && !(x&(1<<j))) return 0;
    return 1;
}
int derivative(int x,Exp e,int j){
    if(e[j]%2==0)return 0;
    e[j]--;
    return eval_monomial(x,e);
}
int multiply_binary_binaryforms(int lhs,int rhs){
    int out=0;
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)
        if((lhs&(1<<i))&&(rhs&(1<<j))&&(i+j<4)) out^=1<<(i+j);
    return out;
}
int restrict_monomial(int a,int b,Exp e){
    int out=1;
    for(int j=0;j<4;j++){
        int variable=((a&(1<<j))?2:0)^((b&(1<<j))?1:0);
        for(int k=0;k<e[j];k++)out=multiply_binary_binaryforms(out,variable);
    }
    return out;
}
int main(){
    vector<Exp> exps;
    for(int a=0;a<=3;a++)for(int b=0;b<=3-a;b++)
    for(int c=0;c<=3-a-b;c++)exps.push_back({a,b,c,3-a-b-c});
    if(exps.size()!=20) return 2;
    vector<pair<int,int>> lines;
    for(int a=1;a<16;a++)for(int b=a+1;b<16;b++)
        if(b<(a^b))lines.push_back({a,b});
    if(lines.size()!=35) return 3;
    UInt point_mask[16]={0}, derivative_mask[16][4]={{0}};
    for(int p=1;p<16;p++)for(int j=0;j<20;j++){
        if(eval_monomial(p,exps[j]))point_mask[p]|=1u<<j;
        for(int k=0;k<4;k++)if(derivative(p,exps[j],k))
            derivative_mask[p][k]|=1u<<j;
    }
    UInt line_mask[35][4]={{0}};
    for(int l=0;l<35;l++)for(int j=0;j<20;j++){
        int r=restrict_monomial(lines[l].first,lines[l].second,exps[j]);
        for(int k=0;k<4;k++)if(r&(1<<k))line_mask[l][k]|=1u<<j;
    }
    bool squarefree[16]={false};
    for(int x:{6,7,9,11,13,14})squarefree[x]=true;
    long long number[36]={0}, rational_smooth[36]={0};
    vector<UInt> extremal;
    for(UInt f=1;f<(1u<<20);f++){
        int T=0;
        for(int l=0;l<35;l++){
            int m=0;
            for(int k=0;k<4;k++)
                if(parity(f & line_mask[l][k]))m|=1<<k;
            if(squarefree[m])T++;
        }
        number[T]++;
        bool smooth_at_rational_points=true;
        for(int p=1;p<16;p++){
            if(parity(f & point_mask[p])) continue;
            bool gradient_zero=true;
            for(int k=0;k<4;k++)
                if(parity(f & derivative_mask[p][k]))gradient_zero=false;
            if(gradient_zero){
                smooth_at_rational_points=false;
                break;
            }
        }
        if(smooth_at_rational_points){
            rational_smooth[T]++;
            if(T==8)extremal.push_back(f);
        }
    }
    cout<<"total_nonzero_forms "<<((1<<20)-1)<<"\n";
    cout<<"rational_lines "<<lines.size()<<"\n";
    cout<<"T all_forms rationally_nonsingular\n";
    for(int t=0;t<=35;t++)if(number[t])
        cout<<t<<" "<<number[t]<<" "<<rational_smooth[t]<<"\n";
    cout<<"extremal_count "<<extremal.size()<<"\n";
    cout<<"extremal_min "<<(extremal.empty()?0:extremal.front())<<"\n";
    ofstream out("extremal_coefficients.txt");
    for(UInt f:extremal)out<<f<<"\n";
    if(!out.good() || extremal.size()!=840)return 4;
    return 0;
}
