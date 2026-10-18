// Independent count over F_(11^4) for every coefficient class from F_(11^2).
// F_(11^4) is represented as F_11[X]/(X^4+X+2), which is irreducible.
// The two rational points over t=0 and infinity on the normalization are counted.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>

constexpr int p=11, Q=14641, ONE=1;
int add(int x,int y) {
    int z=0, scale=1;
    for(int i=0;i<4;i++) {
        z+=((x%p+y%p)%p)*scale;
        x/=p; y/=p; scale*=p;
    }
    return z;
}
int neg(int x) {
    int z=0, scale=1;
    for(int i=0;i<4;i++) {
        z+=((p-x%p)%p)*scale;
        x/=p; scale*=p;
    }
    return z;
}
int mul(int x,int y) {
    int a[4],b[4],c[7]={0};
    for(int i=0;i<4;i++){a[i]=x%p; b[i]=y%p; x/=p; y/=p;}
    for(int i=0;i<4;i++) for(int j=0;j<4;j++) c[i+j]+=a[i]*b[j];
    for(int k=6;k>=4;k--) {
        c[k-3]-=c[k];
        c[k-4]-=2*c[k];
    }
    int z=0,scale=1;
    for(int i=0;i<4;i++) {
        int digit=(c[i]%p+p)%p;
        z+=digit*scale;
        scale*=p;
    }
    return z;
}
int power(int a, int n) {
    int z=ONE;
    while(n){if(n&1) z=mul(z,a); a=mul(a,a); n/=2;}
    return z;
}
int gcd(int a,int b) {while(b){int t=a%b; a=b; b=t;} return a;}
int main(){
    // Certify that X^4+X+2 has neither a root nor a monic quadratic factor.
    for(int x=0;x<p;x++) {int x4=x*x%p; x4=x4*x4%p; assert((x4+x+2)%p!=0);}
    for(int A=0;A<p;A++) for(int B=0;B<p;B++) {
        int D=(A*A-B+p)%p;
        bool coefficient_x=((A*(D-B)-1)%p+p)%p==0;
        bool constant_term=((B*D-2)%p+p)%p==0;
        assert(!(coefficient_x&&constant_term));
    }
    int primitive=0;
    for(int candidate=2;candidate<Q;candidate++) {
        bool okay=true;
        for(int prime : {2,3,5,61})
            if(power(candidate,(Q-1)/prime)==ONE){okay=false;break;}
        if(okay){primitive=candidate;break;}
    }
    assert(primitive!=0);
    int gamma=power(primitive,122); // order 120, generator of the quadratic subfield.
    assert(power(gamma,120)==ONE);
    for(int ell : {2,3,5}) assert(power(gamma,120/ell)!=ONE);
    std::vector<int> cubic_roots(Q,0);
    for(int x=0;x<Q;x++){
        int cube=mul(mul(x,x),x);
        cubic_roots[cube]++;
    }
    assert(cubic_roots[0]==1);
    long long total_roots=0;
    for(int n:cubic_roots) total_roots+=n;
    assert(total_roots==Q);
    std::vector<int> t2(Q),t5(Q);
    for(int t=1;t<Q;t++) {
        t2[t]=mul(t,t);
        t5[t]=mul(mul(t2[t],t2[t]),t);
    }
    std::vector<int> observed;
    for(int r=0;r<15;r++){
        int a=power(gamma,r);
        int count=2;
        for(int t=1;t<Q;t++) {
            int rhs=neg(mul(t2[t],add(a,t5[t])));
            count+=cubic_roots[rhs];
        }
        int gr=gcd(r,15);
        int expected=0;
        if(gr==15) expected=Q+1-10*p*p;
        else if(gr==1||gr==3) expected=Q+1;
        else if(gr==5) expected=Q+1+5*p*p;
        assert(count==expected);
        observed.push_back(count);
    }
    std::cout<<"F11_4_MODULUS X^4+X+2; GENERATOR_INDEX "<<primitive<<"; SUBFIELD_GENERATOR "<<gamma<<"\n";
    std::cout<<"R0_TO_R14_EXTENSION2_COUNTS ";
    for(size_t i=0;i<observed.size();i++) std::cout<<(i?",":"")<<observed[i];
    std::cout<<"\nVERIFY_EXTENSIONS_OK\n";
}
