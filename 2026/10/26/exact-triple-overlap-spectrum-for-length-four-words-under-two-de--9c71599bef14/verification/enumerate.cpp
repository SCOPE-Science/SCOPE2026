// Exhaustive equality-pattern enumeration for triples of length-four words.
// Every labeling of any finite alphabet is an injective relabeling of one
// restricted-growth (set-partition) pattern on the twelve symbol positions.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
using namespace std;

static array<int,12> word{};
static uint64_t count[13][7] = {};
static uint64_t all_patterns=0, distinct_patterns=0;
static int max_intersection=0;

static void score(int used){
    ++all_patterns;
    bool equal01=true, equal02=true, equal12=true;
    for(int j=0;j<4;j++){
        equal01 &= (word[j]==word[4+j]);
        equal02 &= (word[j]==word[8+j]);
        equal12 &= (word[4+j]==word[8+j]);
    }
    if(equal01||equal02||equal12) return;
    uint64_t bits[3][3] = {};
    for(int w=0;w<3;w++)
       for(int i=0;i<4;i++) for(int j=i+1;j<4;j++){
          int id=12*word[4*w+i]+word[4*w+j];
          bits[w][id/64] |= uint64_t(1)<<(id%64);
       }
    int common=0;
    for(int b=0;b<3;b++)
       common += __builtin_popcountll(bits[0][b]&bits[1][b]&bits[2][b]);
    if(common>6) throw runtime_error("unexpected intersection count");
    ++count[used][common];
    ++distinct_patterns;
    if(common>max_intersection) max_intersection=common;
}

static void partitions(int pos,int used){
    if(pos==12){score(used);return;}
    for(int symbol=0; symbol<=used;symbol++){
        word[pos]=symbol;
        partitions(pos+1,used+(symbol==used));
    }
}

int main(){
    word[0]=0;
    partitions(1,1);
    const uint64_t expected[13][7] = {
        {0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0},
        {432,672,432,132,12,0,0},
        {46864,28038,7200,1466,72,0,0},
        {478688,113890,11868,1936,18,0,0},
        {1256658,114600,4304,688,0,0,0},
        {1282686,39720,384,64,0,0,0},
        {622128,5184,0,0,0,0,0},
        {158808,216,0,0,0,0,0},
        {22275,0,0,0,0,0,0},
        {1705,0,0,0,0,0,0},
        {66,0,0,0,0,0,0},
        {1,0,0,0,0,0,0}
    };
    if(all_patterns!=4213597 || distinct_patterns!=4201207 || max_intersection!=4)
        throw runtime_error("partition or extremal check failed");
    for(int k=1;k<=12;k++)for(int s=0;s<=6;s++)
        if(count[k][s]!=expected[k][s])
            throw runtime_error("normalized histogram does not match");
    cout<<"Bell(12) "<<all_patterns<<"; distinct ordered patterns "<<distinct_patterns<<"\n";
    cout<<"k,s=1,s=2,s=3,s=4\n";
    for(int k=2;k<=8;k++){
        cout<<k;
        for(int s=1;s<=4;s++)cout<<","<<count[k][s];
        cout<<"\n";
    }
    cout<<"maximum=4; no common intersection size above 4\nVERIFY_OK\n";
}
