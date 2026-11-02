// Exhaustive exact-integer four-school/agent Kendall consensus census.
// Build: c++ -O2 -std=c++17 verify_kemeny.cpp -o verify_kemeny && ./verify_kemeny
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int main() {
    vector<array<int,4>> rankings;
    array<int,4> order={0,1,2,3};
    do { rankings.push_back(order); } while(next_permutation(order.begin(),order.end()));
    assert(rankings.size()==24);
    int distance[24][24]={};
    for(int r=0;r<24;r++) for(int s=0;s<24;s++) {
        int pos[4];for(int i=0;i<4;i++)pos[rankings[s][i]]=i;
        for(int i=0;i<4;i++) for(int j=i+1;j<4;j++)
            if(pos[rankings[r][i]]>pos[rankings[r][j]])distance[r][s]++;
    }
    long long scoreHist[13]={}, argminHist[25]={};
    long long profiles=0, totalMinScore=0, flat=0;
    for(int a=0;a<24;a++)for(int b=0;b<24;b++)
    for(int c=0;c<24;c++)for(int d=0;d<24;d++) {
        int minimum=100, minimizers=0;
        int first=0, last=0;
        for(int r=0;r<24;r++) {
            int score=distance[r][a]+distance[r][b]+distance[r][c]+distance[r][d];
            if(r==0)first=score;
            last=score;
            if(score<minimum){minimum=score;minimizers=1;}
            else if(score==minimum)minimizers++;
        }
        assert(minimum>=0 && minimum<=12 && minimizers>=1 && minimizers<=24);
        scoreHist[minimum]++;
        argminHist[minimizers]++;
        profiles++;
        totalMinScore+=minimum;
        if(minimizers==24) {assert(minimum==12);flat++;}
    }
    const long long requiredScore[13]={24,288,1560,5472,14232,28800,46896,
                                       62208,66744,56160,34056,12960,2376};
    const long long requiredMinimizers[25]={0,51192,74232,74592,37224,25200,
         26136,0,26784,0,0,0,14040,0,0,0,0,0,0,0,0,0,0,0,2376};
    for(int j=0;j<=12;j++)assert(scoreHist[j]==requiredScore[j]);
    for(int j=0;j<=24;j++)assert(argminHist[j]==requiredMinimizers[j]);
    assert(profiles==331776 && totalMinScore==2488608 && flat==2376);
    cout << "profiles " << profiles << " score_sum " << totalMinScore << "\n";
    for(int j=0;j<=12;j++)cout << "min_K "<<j<<" "<<scoreHist[j]<<"\n";
    for(int j=1;j<=24;j++)if(argminHist[j])
        cout << "number_of_optimal_orders "<<j<<" "<<argminHist[j]<<"\n";
    cout << "PASS: exhaustive exact-integer histogram and minimizer counts\n";
}
