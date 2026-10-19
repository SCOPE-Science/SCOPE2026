"""Standalone exact and finite geometric checks for cyclic component-count identities.

No external modules. This checks independent finite representations; the analytic
limit and positivity proof in RESULT.md remain necessary for an infinite theorem.
"""
from fractions import Fraction
from math import comb, exp, log, isclose
from itertools import combinations


def fall(k, m):
    z = 1
    for i in range(m):
        z *= k - i
    return z


def pattern_counts(bits, j):
    n = len(bits)
    return sum(int(bits[i] == 1 and bits[(i+j) % n] == 1 and
                   all(bits[(i+h) % n] == 0 for h in range(1, j)))
               for i in range(n))


def exact_moments(n, r, j):
    def q(k):
        return max(Fraction(0), 1-k*r)**(n-1)
    a = sum((-1)**v*comb(j-1,v)*q(v+2) for v in range(j))
    b = sum((-1)**v*comb(j-1,v)*q(v+3) for v in range(j))
    ec = n*a
    ex = n*q(1)
    ecx = n*(2*a+(n-j-1)*b)
    p_zero = sum((-1)**k*comb(n,k)*q(k) for k in range(n+1))
    return ec,ex,ecx,ecx-ec*ex,ecx-ec*ex-ec*p_zero


def mask_law(n, r):
    # Exact inclusion-exclusion of the event that a specified gap pattern
    # exceeds the radius; independent of the covariance algebra.
    p = [max(Fraction(0),1-k*r)**(n-1) for k in range(n+1)]
    ans={}
    for mask in range(1<<n):
        ones=mask.bit_count()
        zeros=n-ones
        z=sum((-1)**k*comb(zeros,k)*p[ones+k] for k in range(zeros+1))
        ans[mask]=z
    assert sum(ans.values())==1
    assert all(v>=0 for v in ans.values())
    return ans


def check_conditional():
    total=0
    for n in range(4,12):
        for j in range(1,n-1):
            for k in range(n+1):
                masks=[sum(1<<i for i in c) for c in combinations(range(n),k)]
                s=sum(pattern_counts([(m>>i)&1 for i in range(n)],j) for m in masks)
                rhs=Fraction(k*(k-1)*fall(n-k,j-1),fall(n-1,j))
                assert Fraction(s,len(masks))==rhs,(n,j,k,s,rhs)
                total+=1
    return total


def check_moments():
    total=0
    for n in range(4,10):
        for r in [Fraction(1,8),Fraction(3,17),Fraction(3,10),Fraction(7,16)]:
            m=mask_law(n,r)
            EX=sum(w*mask.bit_count() for mask,w in m.items())
            for j in range(1,n-1):
                EC=ECX=EK=ECK=Fraction(0)
                for mask,w in m.items():
                    b=[(mask>>i)&1 for i in range(n)]
                    x=mask.bit_count()
                    c=pattern_counts(b,j)
                    kk=max(x,1)
                    EC+=w*c
                    ECX+=w*c*x
                    EK+=w*kk
                    ECK+=w*c*kk
                ec,ex,ecx,covx,covk=exact_moments(n,r,j)
                assert (EC,EX,ECX)==(ec,ex,ecx),(n,r,j,EC,ec)
                assert ECX-EC*EX==covx
                assert ECK-EC*EK==covk,(n,r,j,ECK-EC*EK,covk)
                total+=5
    return total


def check_geometry():
    # Exact finite point configurations on a circle, compared to BFS in a
    # geodesic-distance graph. These are not distributional/infinite proofs.
    total=0
    from itertools import combinations
    from math import isclose
    for n in range(4,9):
        den=11
        for sep in combinations(range(1,den),n-1):
            pos=(0,)+sep
            gaps=[Fraction(pos[i+1]-pos[i],den) for i in range(n-1)]
            gaps.append(Fraction(den-pos[-1],den))
            for r in [Fraction(1,8),Fraction(5,18),Fraction(2,5)]:
                if r in gaps: continue
                bits=[int(g>r) for g in gaps]
                adj=[set() for _ in range(n)]
                for i in range(n):
                    for k in range(i+1,n):
                        d=Fraction(pos[k]-pos[i],den)
                        if min(d,1-d)<r:
                            adj[i].add(k);adj[k].add(i)
                unseen=set(range(n)); sizes=[]
                while unseen:
                    u=unseen.pop();stack=[u];size=1
                    while stack:
                        v=stack.pop()
                        for w in adj[v] & unseen:
                            unseen.remove(w);stack.append(w);size+=1
                    sizes.append(size)
                assert len(sizes)==max(1,sum(bits)),(n,pos,r,sizes,bits)
                for j in range(1,n-1):
                    assert sizes.count(j)==pattern_counts(bits,j),(n,pos,r,j,sizes,bits)
                    total+=1
    return total


def check_limits():
    total=0
    for j in range(1,8):
        for t in [0.15,0.35,0.6,1.0,1.5,2.2]:
            p=exp(-t)
            v=p*(1-p)-t*t*p*p
            if j==1:
                predicted=2*p*v
            else:
                predicted=p*(1-p)**(j-2)*(2-(j+1)*p)*v
            for n in [1000,2000,4000]:
                r=t/n
                def q(k):return max(0.0,1-k*r)**(n-1)
                a=sum((-1)**s*comb(j-1,s)*q(s+2) for s in range(j))
                b=sum((-1)**s*comb(j-1,s)*q(s+3) for s in range(j))
                actual=2*a+(n-j-1)*b-n*q(1)*a
                assert abs(actual-predicted)<0.025,(j,t,n,actual,predicted)
                total+=1
    for j in range(2,100):
        t=log((j+1)/2)
        p=exp(-t)
        assert abs(2-(j+1)*p)<1e-12
        assert exp(t)-1-t*t>0
        total+=1
    return total


def main():
    parts=(check_conditional(),check_moments(),check_geometry(),check_limits())
    print('PASS; verification groups',parts,'total',sum(parts))

if __name__=='__main__': main()
