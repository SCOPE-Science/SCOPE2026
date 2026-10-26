// Exact enumeration of ternary cubic equations over F4.
// Finite-field encoding: a^2+a+1=0 and 0,1,a,a+1 are 0,1,2,3.
#include <array>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
int times(int a,int b) {
    int out=0;
    for(int i=0;i<2;i++) if((b>>i)&1) out ^= a<<i;
    if(out&4) out^=7; // a^2 = a+1
    return out;
}
int pow4(int a,int k){int r=1;for(int i=0;i<k;i++)r=times(r,a);return r;}
int main(){
    vector<array<int,3>> p;
    for(int y=0;y<4;y++) for(int z=0;z<4;z++) p.push_back({1,y,z});
    for(int z=0;z<4;z++)p.push_back({0,1,z});
    p.push_back({0,0,1});
    const array<array<int,3>,10> mon={{{3,0,0},{2,1,0},{2,0,1},{1,2,0},
        {1,1,1},{1,0,2},{0,3,0},{0,2,1},{0,1,2},{0,0,3}}};
    array<array<int,10>,21> vals{};
    array<int,21> hermitian{};
    int ptsH=0;
    for(int j=0;j<21;j++){
        auto [x,y,z]=p[j];
        for(int i=0;i<10;i++) {
            auto e=mon[i];
            vals[j][i]=times(times(pow4(x,e[0]),pow4(y,e[1])),pow4(z,e[2]));
        }
        int h=vals[j][0]^vals[j][7]^vals[j][8]; // X^3+Y^2 Z+Y Z^2
        if(!h){hermitian[j]=1;ptsH++;}
    }
    if(ptsH!=9) return 1;
    vector<array<int,5>> linepts;
    for(auto l:p){
        array<int,5> a{};int k=0;
        for(int j=0;j<21;j++){
            auto x=p[j];
            if(!(times(l[0],x[0])^times(l[1],x[1])^times(l[2],x[2]))){
                if(k>=5)return 2;
                a[k++]=j;
            }
        }
        if(k!=5)return 3;
        linepts.push_back(a);
    }
    long long by_intersection[10]={}, no_line[10]={};
    long long curve_points[22]={};
    int pair_counts[21][21]={}, pair_7pts[21][21]={},pair_8pts[21][21]={};
    int forms=0;
    bool witness=false;
    for(int word=1;word<(1<<20);word++){
        int c[10];for(int i=0;i<10;i++)c[i]=(word>>(2*i))&3;
        int last=9;while(!c[last])last--;
        if(c[last]!=1)continue; // one representative of each nonzero scalar orbit
        forms++;
        array<int,21> z{};
        int h=0,rational=0;
        for(int j=0;j<21;j++){
            int out=0;
            for(int i=0;i<10;i++)out ^=times(c[i],vals[j][i]);
            z[j]=out;
            if(out==0){rational++;h+=hermitian[j];}
        }
        by_intersection[h]++;
        if(h<7)continue;
        bool has_line=false;
        for(auto l:linepts){
            bool all=true;
            for(int a:l) if(z[a]!=0){all=false;break;}
            if(all){has_line=true;break;}
        }
        if(has_line)continue;
        no_line[h]++;
        curve_points[rational]++;
        if(h==7){
            int missing[2]={-1,-1},num=0;
            for(int j=0;j<21;j++)if(hermitian[j]&&z[j]!=0){if(num<2)missing[num]=j;num++;}
            if(num!=2)return 4;
            int a=missing[0],b=missing[1];
            pair_counts[a][b]++;
            if(rational==7)pair_7pts[a][b]++;
            if(rational==8)pair_8pts[a][b]++;
            if(!witness){
                witness=true;
                printf("WITNESS:");for(int i=0;i<10;i++)printf(" %d",c[i]);puts("");
            }
        }
    }
    if(forms!=349525) return 5;
    if(by_intersection[7]!=576 || by_intersection[8]!=0 || by_intersection[9]!=5) return 6;
    if(no_line[7]!=180 || no_line[8]!=0 || no_line[9]!=1)return 7;
    if(curve_points[7]!=72 || curve_points[8]!=108 || curve_points[9]!=1)return 8;
    int pairs=0;
    for(int a=0;a<21;a++)for(int b=a+1;b<21;b++){
        if(hermitian[a] && hermitian[b]){
            pairs++;
            if(pair_counts[a][b]!=5 || pair_7pts[a][b]!=2 || pair_8pts[a][b]!=3)return 9;
        }
    }
    if(pairs!=36)return 10;
    printf("FORMS %d; INTERSECTION_7 %lld; INTERSECTION_8 %lld; INTERSECTION_9 %lld\n",
        forms,by_intersection[7],by_intersection[8],by_intersection[9]);
    printf("SMOOTH_COMPANIONS %lld; POINT_COUNTS 7:%lld 8:%lld\n",no_line[7],curve_points[7],curve_points[8]);
    printf("PAIRS %d EACH_FIVE_TWO_THREE\n",pairs);
    puts("VERIFY_EXHAUSTIVE_OK");
}
