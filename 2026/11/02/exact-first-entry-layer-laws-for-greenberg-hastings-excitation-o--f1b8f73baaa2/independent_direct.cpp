// Direct labelled-configuration verification of a three-state excitation rule
// on two complete graphs joined by a single bridge edge.
// Uses no capped color counts or symbolic-polynomial reasoning.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <vector>
using U = long long;

U power(U a, int n) { U r=1; while(n--) r*=a; return r; }

U evolve(U code, int a, int b) {
    const int N=a+b;
    std::array<int,20> v{}, w{};
    U k=code;
    int alive_a=0, alive_b=0;
    for(int i=0;i<N;i++) {
        v[i]=int(k%3); k/=3;
        if(v[i]==1) { if(i<a) ++alive_a; else ++alive_b; }
    }
    for(int i=0;i<N;i++) {
        if(v[i] == 1) w[i]=2;
        else if(v[i] == 2) w[i]=0;
        else {
            int neighbor_one = i<a ? alive_a : alive_b;
            if(i==0 && v[a]==1) ++neighbor_one;
            if(i==a && v[0]==1) ++neighbor_one;
            w[i]=int(neighbor_one>0);
        }
    }
    U ans=0, factor=1;
    for(int i=0;i<N;i++) { ans+=factor*w[i]; factor*=3; }
    return ans;
}

U predicted(int a,int b,int p,int t) {
    U x=power(2,a), y=power(2,b);
    U u=power(3,a), v=power(3,b);
    U xy=x*y, s=x+y;
    if(p==1) {
        if(t==0) return 1;
        if(t==1) return xy-1;
        if(t==2) return (5*xy-4*s+2)/2;
        if(t==3) return (6*xy-9*s+12)/2;
        if(t==4) return (2*xy-s)/2;
        if(t==5) return (3*xy-4*s+4)/2;
        return 0;
    }
    if(p==3) {
        if(t==0) {
            U A=power(3,a-1)-power(2,a)+1;
            U B=power(3,b-1)-power(2,b)+1;
            return 9*A*B+3*(A+B);
        }
        if(t<1 || t>6) return 0;
        int j = t<7-t ? t : 7-t;
        U six = (2*j-1)*(u*y+x*v)-2*j*(u+v)-6*(2*j-1)*xy
              +3*(4*j-1)*s-12*j;
        if(six%6) throw std::logic_error("nonintegral predicted count");
        return six/6;
    }
    return 0;
}

void check(int a,int b) {
    U total=power(3,a+b);
    U classes[4][7]{};
    for(U initial=0;initial<total;initial++) {
        std::array<U,20> seq{};
        int size=0, pre=-1, period=-1;
        U s=initial;
        while(size < 17) {
            int old=0;
            while(old<size && seq[old]!=s) ++old;
            if(old<size) { pre=old;period=size-old; break; }
            seq[size++]=s;
            s=evolve(s,a,b);
        }
        if(pre<0 || (period!=1 && period!=3) || pre>6)
            throw std::logic_error("unexpected orbit length or first-entry time");
        classes[period][pre]++;
    }
    for(int p: {1,3})
        for(int t=0;t<=6;t++)
            if(classes[p][t]!=predicted(a,b,p,t)) {
                std::cerr << "Mismatch a=" << a << " b=" << b << " p=" << p
                          << " t=" << t << " actual=" << classes[p][t]
                          << " expected=" << predicted(a,b,p,t) << "\n";
                throw std::logic_error("period-entry formula mismatch");
            }
    std::cout << "PASS cliques " << a << "+" << b << ": " << total
              << " labelled states; extinction=";
    U extinct=0;for(int t=0;t<=6;t++) extinct+=classes[1][t];
    std::cout << extinct << ", period3=" << total-extinct << ", max entry=";
    int mx=0;for(int t=0;t<=6;t++) if(classes[1][t]||classes[3][t]) mx=t;
    std::cout << mx << "\n";
}

int main() {
    for(auto [a,b]: std::vector<std::pair<int,int>>{
        {2,2},{2,3},{2,4},{2,7},{3,3},{3,4},{3,6},{4,4},{4,5},{5,5},{5,6},{6,6}})
       check(a,b);
}
