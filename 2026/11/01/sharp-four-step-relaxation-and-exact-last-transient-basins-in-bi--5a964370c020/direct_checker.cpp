// Independent vertex-wise evolution of the synchronous closed-neighborhood
// bi-threshold rule on complete bipartite graphs. No symbolic order types.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

uint32_t transition(uint32_t state, int a, int b, int up, int down) {
    int count_a=0, count_b=0;
    for(int k=0;k<a;k++) count_a+=(state>>k)&1u;
    for(int k=a;k<a+b;k++) count_b+=(state>>k)&1u;
    uint32_t next=0;
    for(int k=0;k<a+b;k++) {
        bool old=(state>>k)&1u;
        int sum=(k<a?count_b:count_a)+(int)old;
        bool newer=old?(sum>=down):(sum>=up);
        if(newer) next |= 1u<<k;
    }
    return next;
}

int main(){
    uint64_t configurations=0, instances=0, transient_four=0;
    for(int a=1;a<=7;a++) for(int b=1;b<=7;b++) {
        int H=max(a,b)+2;
        for(int up=1;up<=H;up++) for(int down=1;down<=H;down++) {
            uint64_t count4=0;
            int h=down-1;
            for(uint32_t x=0;x<(1u<<(a+b));x++) {
                uint32_t y=x;
                uint32_t path[7]={x};
                for(int t=1;t<=6;t++) {y=transition(y,a,b,up,down);path[t]=y;}
                assert(path[6]==path[4]);
                bool last = path[5]!=path[3];
                int i=0,j=0;
                for(int k=0;k<a;k++) i+=(x>>k)&1u;
                for(int k=a;k<a+b;k++) j+=(x>>k)&1u;
                bool four=(up<=i && up<=a-i && up<=j && up<=b-j)
                     && ((h>max(b,i) && h<=a-i) || (h>max(a,j) && h<=b-j));
                assert(four==last);
                if(last) {
                    const uint32_t leftOn=(1u<<a)-1u;
                    const uint32_t rightOn=((1u<<b)-1u)<<a;
                    assert(path[4]==leftOn || path[4]==rightOn);
                }
                count4+=last;
                configurations++;
            }
            // Closed binomial formula; build coefficients independently by Pascal recursion.
            vector<uint64_t> ca(a+1),cb(b+1); ca[0]=cb[0]=1;
            for(int i=1;i<=a;i++)ca[i]=ca[i-1]*(a-i+1)/i;
            for(int j=1;j<=b;j++)cb[j]=cb[j-1]*(b-j+1)/j;
            auto sum = [](const vector<uint64_t>& c,int lo,int hi){uint64_t v=0;
                for(int k=max(0,lo);k<=hi && k<(int)c.size();k++) v+=c[k];
                return v;};
            uint64_t formula=0;
            if(h>b)formula+=sum(ca,up,min(a-h,h-1))*sum(cb,up,b-up);
            if(h>a)formula+=sum(ca,up,a-up)*sum(cb,up,min(b-h,h-1));
            assert(formula==count4);
            transient_four+=count4;
            instances++;
        }
    }
    cout<<"PASS graph/threshold instances: "<<instances<<"\n";
    cout<<"PASS labelled configurations: "<<configurations<<"\n";
    cout<<"PASS exact T=4 and binomial formulas, F^6=F^4\n";
    cout<<"Observed four-step labelled cases: "<<transient_four<<"\n";
}
