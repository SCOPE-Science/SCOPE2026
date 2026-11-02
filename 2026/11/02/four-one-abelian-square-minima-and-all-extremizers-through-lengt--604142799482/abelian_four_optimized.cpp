#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <array>
using namespace std;

// Binary word with exactly four 1s: zero-run lengths r[0]...r[4].
// Count distinct abelian squares, not occurrences. A nonzero abelian square
// contains exactly two (one in each half), or four (two in each half) ones.
static int parity_points(int lo, int hi, int parity){
    if(lo>hi) return 0;
    if((lo&1)!=parity) ++lo;
    return lo>hi ? 0 : 1+(hi-lo)/2;
}
static int count_sq(const array<int,5>&r){
    int g[3]={r[1],r[2],r[3]};
    int L[3]={r[0],r[1],r[2]};
    int R[3]={r[2],r[3],r[4]};
    int count=*max_element(r.begin(),r.end())/2;
    for(int i=0;i<3;i++){
        bool prior=false; for(int j=0;j<i;j++) if(g[i]==g[j]) prior=true;
        if(prior) continue;
        int mL=-1; for(int j=i;j<3;j++) if(g[j]==g[i]) mL=max(mL,L[j]);
        for(int u=0;u<=mL;u++){
            int maxR=-1;
            for(int j=0;j<3;j++) if(g[j]==g[i] && L[j]>=u) maxR=max(maxR,R[j]);
            int lo=max(0,u-g[i]), hi=min(maxR,u+g[i]);
            count+=parity_points(lo,hi,(u-g[i])&1);
        }
    }
    int deltaLo=r[1]-r[2]-r[3];
    int deltaHi=r[1]+r[2]-r[3];
    int parity=(r[1]+r[2]+r[3])&1;
    for(int u=0;u<=r[0];u++){
        int lo=max(0,u+deltaLo), hi=min(r[4],u+deltaHi);
        count+=parity_points(lo,hi,(u+parity)&1);
    }
    return count;
}
int main(int argc,char**argv){
    int top=64; if(argc>1) top=atoi(argv[1]);
    if(top<4 || top>128) return 3;
    // Each integer 4-tuple of one positions occurs exactly once.
    printf("# n  minimum  labeled_minimizers  lexicographic_ones_positions  all_four_one_words\n");
    for(int n=4;n<=top;n++){
        int mn=n+1; unsigned long long ct=0, total=0;
        array<int,4> best{};
        for(int a=0;a<n-3;a++) for(int b=a+1;b<n-2;b++)
        for(int c=b+1;c<n-1;c++) for(int d=c+1;d<n;d++){
            array<int,5> r={a,b-a-1,c-b-1,d-c-1,n-1-d};
            int val=count_sq(r);
            ++total;
            if(val<mn){mn=val;ct=1;best={a,b,c,d};}
            else if(val==mn){++ct;}
        }
        printf("%d %d %llu %d,%d,%d,%d %llu\n",n,mn,ct,best[0],best[1],best[2],best[3],total);
        fflush(stdout);
    }
}
