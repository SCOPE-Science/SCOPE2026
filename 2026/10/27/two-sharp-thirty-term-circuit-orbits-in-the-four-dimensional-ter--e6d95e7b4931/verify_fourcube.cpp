// Reproducible exhaustive certificate for positive rank-four circuits in the four-dimensional ternary cube.
// Compile: c++ -O2 -std=c++17 verify_fourcube.cpp -o verify_fourcube
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using V = array<int,4>;
using Five = array<int,5>;

// Fraction-free elimination; unlike a Laplace determinant expansion, pivoting is explicit.
int det4(const array<V,4>& cols) {
    long long a[4][4];
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)a[i][j]=cols[j][i];
    long long prev=1;int sign=1;
    for(int k=0;k<3;k++) {
        int p=k;while(p<4&&a[p][k]==0)p++;
        if(p==4)return 0;
        if(p!=k){for(int j=0;j<4;j++)swap(a[p][j],a[k][j]);sign=-sign;}
        const long long pivot=a[k][k];
        for(int i=k+1;i<4;i++)for(int j=k+1;j<4;j++) {
            long long numerator=a[i][j]*pivot-a[i][k]*a[k][j];
            assert(numerator%prev==0);
            a[i][j]=numerator/prev;
        }
        for(int i=k+1;i<4;i++)a[i][k]=0;
        prev=pivot;
    }
    return int(sign*a[3][3]);
}
Five sorted_image(const Five& q,const array<int,80>& action) {
    Five p;for(int j=0;j<5;j++)p[j]=action[q[j]];
    sort(p.begin(),p.end());return p;
}
int main() {
    vector<V> point; map<V,int> index;
    for(int a=-1;a<=1;a++)for(int b=-1;b<=1;b++)for(int c=-1;c<=1;c++)for(int d=-1;d<=1;d++) {
        V v={a,b,c,d};if(v==V{0,0,0,0})continue;
        index[v]=int(point.size());point.push_back(v);
    }
    assert(point.size()==80);
    int best=0;long long attempted=0,positive=0;array<int,5> rooted_best={};
    vector<Five> best_sets;
    for(int nonzeros=1;nonzeros<=4;nonzeros++) {
        V root={0,0,0,0};for(int j=0;j<nonzeros;j++)root[j]=1;
        int anchor=index.at(root);
        vector<int> others;for(int j=0;j<80;j++)if(j!=anchor)others.push_back(j);
        for(int a=0;a<76;a++)for(int b=a+1;b<77;b++)for(int c=b+1;c<78;c++)for(int d=c+1;d<79;d++) {
            attempted++;
            Five ids={anchor,others[a],others[b],others[c],others[d]};
            int relation[5];bool valid=true;
            for(int skip=0;skip<5;skip++) {
                array<V,4> cols;int z=0;for(int j=0;j<5;j++)if(j!=skip)cols[z++]=point[ids[j]];
                int determinant=det4(cols);
                if(determinant==0){valid=false;break;}
                relation[skip]=(skip%2 ? -determinant : determinant);
            }
            if(!valid)continue;
            int sign=(relation[0]>0?1:-1);
            for(int x:relation)if(x*sign<=0){valid=false;break;}
            if(!valid)continue;
            positive++;
            int gcd=0,sum=0;for(int x:relation){gcd=std::gcd(gcd,abs(x));sum+=abs(x);}
            int length=sum/gcd;
            if(length>best){best=length;best_sets.clear();rooted_best.fill(0);}
            if(length==best){best_sets.push_back(ids);rooted_best[nonzeros]++;}
        }
    }
    assert(attempted==6010004LL);
    assert(positive==120560LL);
    assert(best==30);
    assert((rooted_best==array<int,5>{0,0,0,84,72}));
    assert(best_sets.size()==156);
    vector<array<int,80>> actions;
    array<int,4> p={0,1,2,3};
    do {for(int mask=0;mask<16;mask++) {
        array<int,80> action;
        for(int j=0;j<80;j++) {
            V image;for(int k=0;k<4;k++)image[k]=((mask>>k)&1?-1:1)*point[j][p[k]];
            action[j]=index.at(image);
        }
        actions.push_back(action);
    }}while(next_permutation(p.begin(),p.end()));
    assert(actions.size()==384);
    map<Five,int> classes;
    for(const Five& ids:best_sets) {
        Five canonical={80,80,80,80,80};
        for(const auto& act:actions)canonical=min(canonical,sorted_image(ids,act));
        classes[canonical]++;
    }
    assert(classes.size()==2);
    set<Five> complete;
    vector<int> orbits;
    for(auto [base,rooted_multiplicity]:classes) {
        set<Five> orbit;
        for(const auto& act:actions)orbit.insert(sorted_image(base,act));
        assert(orbit.size()==384);
        orbits.push_back(int(orbit.size()));
        complete.insert(orbit.begin(),orbit.end());
    }
    assert(complete.size()==768);
    cout<<"CERTIFICATE_OK tested="<<attempted<<" positive="<<positive
        <<" max="<<best<<" rooted_max="<<best_sets.size()
        <<" orbit_count="<<orbits.size()<<" orbit_sizes="<<orbits[0]<<","<<orbits[1]
        <<" distinct_maximizers="<<complete.size()<<'\n';
    return 0;
}
