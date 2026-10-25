"""Independent checks of color-permutation homology characters of cycle products.
Only standard-library Python is required.
"""
from functools import lru_cache
from itertools import permutations
from math import factorial


def cycles(sigma):
    seen=set(); out=[]
    for a in range(len(sigma)):
        if a in seen: continue
        orb=[]; z=a
        while z not in seen:
            seen.add(z);orb.append(z);z=sigma[z]
        assert z==a
        out.append(tuple(orb))
    return out


def quotient_adj(m,sigma):
    orbit=cycles(sigma); n=len(sigma); c=len(orbit)
    neighbor=[0]*(m*c)
    for i in range(m):
        for a,A in enumerate(orbit):
            z=i*c+a
            for j in ((i-1)%m,(i+1)%m):
                for b,B in enumerate(orbit):
                    if any(x!=y for x in A for y in B):
                        neighbor[z]|=1<<(j*c+b)
    return neighbor


def independent_z_at_minus_one(neighbor):
    N=len(neighbor)
    @lru_cache(None)
    def z(avail):
        if not avail: return 1
        bit=avail&-avail
        v=bit.bit_length()-1
        return z(avail^bit)-z((avail^bit)&~neighbor[v])
    return z((1<<N)-1)


def direct_signed_trace(m,sigma):
    n=len(sigma);N=m*n
    neighbor=[0]*N
    for i in range(m):
        for a in range(n):
            for j in ((i-1)%m,(i+1)%m):
                for b in range(n):
                    if a!=b:neighbor[i*n+a]|=1<<(j*n+b)
    mapv=[i*n+sigma[a] for i in range(m) for a in range(n)]
    out=0; stable_count=0
    def examine(chosen):
        nonlocal out,stable_count
        points=[]; p=chosen
        while p:
            q=p&-p;points.append(q.bit_length()-1);p^=q
        perm_points=[mapv[v] for v in points]
        if set(perm_points)!=set(points):return
        stable_count+=1
        pos={v:i for i,v in enumerate(points)}
        perm=[pos[v] for v in perm_points]
        seen=set();c=0
        for i in range(len(perm)):
            if i not in seen:
                c+=1;j=i
                while j not in seen:
                    seen.add(j);j=perm[j]
        orientation=(-1)**(len(points)-c)
        out+=(-1)**len(points)*orientation
    def rec(avail,chosen):
        if not avail:
            examine(chosen);return
        bit=avail&-avail;v=bit.bit_length()-1
        rec(avail^bit,chosen)
        rec((avail^bit)&~neighbor[v],chosen|bit)
    rec((1<<N)-1,0)
    return out,stable_count


def predicted(m,sigma):
    assert m%3==0
    r=m//3
    f=sum(x==i for i,x in enumerate(sigma))
    return 3*(f-1)**r + (-1)**r*(f-1)


def main():
    count=0; total_stable=0; max_cache=None
    for m,n in ((3,2),(3,3),(3,4),(3,5),(6,2),(6,3),(6,4),(9,2),(9,3)):
        for sigma in permutations(range(n)):
            A=independent_z_at_minus_one(quotient_adj(m,sigma))
            B=predicted(m,sigma)
            assert A==B,(m,n,sigma,A,B)
            if m*n<=18:
                C,k=direct_signed_trace(m,sigma)
                assert A==C,(m,n,sigma,A,C)
                total_stable+=k
            count+=1
    print('COLOR_CHARACTER_CHECKS_OK',count,'direct_invariant_simplices',total_stable)

if __name__=='__main__':main()
