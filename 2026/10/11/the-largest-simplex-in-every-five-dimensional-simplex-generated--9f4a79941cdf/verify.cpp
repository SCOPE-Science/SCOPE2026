// Exact, self-contained determinant enumeration for the 5D simplex-zonotope.
// C++17, no dependencies outside the standard library.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using V5 = array<int,5>;
using M6 = array<int,6>;
using P3 = array<array<int,2>,3>;
static V5 coord(int mask) {
    int b=mask&1;V5 v{};
    for(int i=0;i<5;i++)v[i]=((mask>>(i+1))&1)-b;
    return v;
}
static long long bareiss(int A[5][5]) {
    long long a[5][5]{};
    for(int i=0;i<5;i++)for(int j=0;j<5;j++)a[i][j]=A[i][j];
    long long prev=1;int sign=1;
    for(int k=0;k<4;k++){
        if(a[k][k]==0){int p=k+1;while(p<5 && a[p][k]==0)p++;
            if(p==5)return 0;
            for(int j=0;j<5;j++)swap(a[k][j],a[p][j]);
            sign=-sign;
        }
        const long long pivot=a[k][k];
        for(int i=k+1;i<5;i++)for(int j=k+1;j<5;j++){
            const long long num=a[i][j]*pivot-a[i][k]*a[k][j];
            assert(prev!=0 && num%prev==0);
            a[i][j]=num/prev;
        }
        for(int i=k+1;i<5;i++)a[i][k]=0;
        prev=pivot;
    }
    return sign*a[4][4];
}
static long long perm_det(int A[5][5]) {
    array<int,5> p={0,1,2,3,4};long long out=0;
    do {
        int inversions=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)inversions+=(p[i]>p[j]);
        long long term=(inversions&1)?-1:1;
        for(int i=0;i<5;i++)term*=A[i][p[i]];
        out+=term;
    }while(next_permutation(p.begin(),p.end()));
    return out;
}
static void matrix(const M6& masks,int a[5][5]) {
    const V5 base=coord(masks[0]);
    for(int j=0;j<5;j++){
        V5 q=coord(masks[j+1]);
        for(int i=0;i<5;i++)a[i][j]=q[i]-base[i];
    }
}
static int pop(int x){return __builtin_popcount((unsigned)x);}
static set<M6> expected_cycles(){
    set<M6> ans;
    vector<P3> matchings;
    // Enumerate unordered perfect matchings of {0,1,2,3,4,5} by pairing smallest unused point.
    for(int j=1;j<6;j++) {
        int free[4],n=0;
        for(int i=1;i<6;i++)if(i!=j)free[n++]=i;
        for(int k=1;k<4;k++){
            int other[2],m=0;
            for(int i=1;i<4;i++)if(i!=k)other[m++]=free[i];
            matchings.push_back(P3{{{{0,j}},{{free[0],free[k]}},{{other[0],other[1]}}}});
        }
    }
    assert(matchings.size()==15);
    for(const auto& P:matchings)for(int dir : {1,2}){
        M6 masks{};int pos=0;
        for(int i=0;i<3;i++){
            const auto& X=P[i];const auto& Y=P[(i+dir)%3];
            for(int point : Y){masks[pos++]=(1<<X[0])|(1<<X[1])|(1<<point);}
        }
        assert(pos==6);
        sort(masks.begin(),masks.end());
        for(int m:masks)assert(pop(m)==3);
        ans.insert(masks);
    }
    assert(ans.size()==30);
    return ans;
}
int main(){
    vector<int> all;for(int mask=1;mask<63;mask++)all.push_back(mask);
    assert(all.size()==62);
    const long long choose615=5949147;
    for(int k=1;k<=3;k++) {
        int base=(1<<k)-1;
        vector<int> m;for(int a:all)if(a!=base)m.push_back(a);
        assert(m.size()==61);
        long long hist[64]{};long long count=0;int best=-1;
        for(int a=0;a<57;a++)for(int b=a+1;b<58;b++)for(int c=b+1;c<59;c++)
          for(int d=c+1;d<60;d++)for(int e=d+1;e<61;e++){
            M6 t={base,m[a],m[b],m[c],m[d],m[e]};int A[5][5];matrix(t,A);
            long long v=llabs(bareiss(A));assert(v>=0&&v<64);
            hist[v]++;count++;best=max(best,(int)v);
          }
        assert(count==choose615);
        long long check=0;for(auto h:hist)check+=h;assert(check==choose615);
        assert(best==((k==1)?14:((k==2)?17:18)));
        if(k==3)assert(hist[18]==9);
        cout << "orbit-base size=" << k << " combinations=" << count
             << " maximum_determinant=" << best
             << " number_at_18=" << hist[18] << '\n';
    }
    vector<int> middle;for(int m:all)if(pop(m)==3)middle.push_back(m);
    assert(middle.size()==20);
    set<M6> winners;long long checked=0;int best=0;
    for(int a=0;a<15;a++)for(int b=a+1;b<16;b++)for(int c=b+1;c<17;c++)
      for(int d=c+1;d<18;d++)for(int e=d+1;e<19;e++)for(int f=e+1;f<20;f++){
        M6 t={middle[a],middle[b],middle[c],middle[d],middle[e],middle[f]};int A[5][5];matrix(t,A);
        const long long v=llabs(bareiss(A));
        // Independent 120-term permutation expansion, for each of 38,760 matrices.
        assert(v==llabs(perm_det(A)));
        checked++;best=max(best,(int)v);
        if(v==18)winners.insert(t);
    }
    assert(checked==38760 && best==18 && winners.size()==30);
    assert(winners==expected_cycles());
    // Shared five vertices would allow a continuum of nonvertex maximizers.
    set<array<int,5>> five_faces;
    for(const auto& s:winners)for(int omit=0;omit<6;omit++){
        array<int,5> face{};int j=0;
        for(int i=0;i<6;i++)if(i!=omit)face[j++]=s[i];
        assert(five_faces.insert(face).second);
    }
    assert(five_faces.size()==180);
    cout << "middle_layer_sixsets=" << checked << " exact_maximum=18"
         << " winners=" << winners.size() << " shared_5_faces=0" << '\n';
    cout << "volume_of_zonotope_in_basis_units=6"
         << " max_simplex_volume_in_basis_units=18/120"
         << " exact_volume_ratio=1/40" << '\n';
    cout << "VERIFY_OK" << '\n';
}
