"""Exact enumeration and algebra checks for isolated-chord crossing suppression.

Run with Python 3: python verify.py
Uses only the standard library. No pseudorandomness or external dependencies.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def odd_double_factorial(n):
    out = 1
    for j in range(1, n + 1):
        out *= 2*j - 1
    return out


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for j in range(1, len(vertices)):
        for sub in matchings(vertices[1:j] + vertices[j+1:]):
            yield ((first, vertices[j]),) + sub


def crosses(x, y):
    a,b=x; c,d=y
    return a<c<b<d or c<a<d<b


def crossing_count(diagram):
    return sum(crosses(x,y) for j,x in enumerate(diagram) for y in diagram[j+1:])


def isolated_count(diagram):
    return sum(not any(crosses(x,y) for y in diagram if y != x) for x in diagram)


def distribution(n):
    counts = Counter()
    for diagram in matchings(tuple(range(2*n))):
        counts[crossing_count(diagram)] += 1
    assert sum(counts.values()) == odd_double_factorial(n)
    return {k:Fraction(v,odd_double_factorial(n)) for k,v in counts.items()}


def convex_convolve(a,b):
    out=Counter()
    for x, px in a.items():
        for y, py in b.items():
            out[x+y]+=px*py
    return dict(out)


def tail(d, threshold):
    return sum((p for j,p in d.items() if j>=threshold),Fraction())


def closed_form(n):
    m=n-1
    den=odd_double_factorial(n)
    w=[odd_double_factorial(k)*odd_double_factorial(m-k) for k in range(n)]
    E_I=Fraction(n*sum(w),den)
    E_C=Fraction(n*(n-1),6)
    E_CI=Fraction(n,6*den)*sum(w[k]*(k*(k-1)+(m-k)*(m-k-1)) for k in range(n))
    cov=E_CI-E_I*E_C
    assert cov == -Fraction(n,3*den)*sum(w[k]*(m+k*(m-k)) for k in range(n))
    return E_I,E_C,E_CI,cov,w


def verify():
    assertions=0
    all_dists={0:{0:Fraction(1)}}
    for n in range(1,8):
        all_dists[n]=distribution(n)
        assert sum(all_dists[n].values())==1;assertions+=1
    for n in range(2,8):
        den=odd_double_factorial(n)
        nc=ci=i=c=0
        palm=Counter()
        conditional=Counter()
        candidates=[]
        for x in range(2*n):
            for y in range(x+1,2*n):
                if (y-x-1)%2 == 0:
                    candidates.append((x,y))
        assert len(candidates)==n*n;assertions+=1
        event_counts=Counter()
        for diagram in matchings(tuple(range(2*n))):
            ct=crossing_count(diagram)
            iso=isolated_count(diagram)
            c+=ct; i+=iso; ci+=ct*iso; nc+=1
            palm[ct]+=iso
            for x,y in diagram:
                if (y-x-1)%2 == 0 and not any(crosses((x,y),q) for q in diagram if q!=(x,y)):
                    event_counts[(x,y,ct)] += 1
        assert nc==den;assertions+=1
        E_I,E_C,E_CI,cov,w=closed_form(n)
        assert Fraction(i,nc)==E_I;assertions+=1
        assert Fraction(c,nc)==E_C;assertions+=1
        assert Fraction(ci,nc)==E_CI;assertions+=1
        assert Fraction(ci,nc)-Fraction(i*c,nc*nc)==cov;assertions+=1
        assert cov<0;assertions+=1
        for k in range(n):
            conditional[k]=convex_convolve(all_dists[k],all_dists[n-1-k])
            # Identical split law for every one of the n candidate chords of this arc size.
            selected=[]
            for x,y in candidates:
                kk=(y-x-1)//2
                if kk==k or n-1-kk==k:
                    selected.append((x,y))
            for x,y in selected[:2]:
                num=sum(cnt for (a,b,ct),cnt in event_counts.items() if (a,b)==(x,y))
                assert num==w[k];assertions+=1
                for t in range(comb(n-1,2)+1):
                    true=Fraction(event_counts.get((x,y,t),0),num)
                    assert true==conditional[k].get(t,Fraction());assertions+=1
            for t in range(comb(n,2)+2):
                assert tail(conditional[k],t)<=tail(all_dists[n],t);assertions+=1
        palm_dist={ct:Fraction(count,i) for ct,count in palm.items()}
        for t in range(comb(n,2)+2):
            assert tail(palm_dist,t)<=tail(all_dists[n],t);assertions+=1
        print(f'n={n}, diagrams={nc}, E[I]={E_I}, Cov(C,I)={cov}')
    # Exact algebra and asymptotic coefficient sanity checks, n well beyond enumeration.
    for n in (8,9,10,20,40,80,160,320):
        E_I,E_C,E_CI,cov,w=closed_form(n)
        assert cov<0;assertions+=1
        residual=cov+Fraction(n,3)+Fraction(1,6)+Fraction(5,6*n)
        assert abs(residual)<Fraction(100,n*n);assertions+=1
    print(f'PASS: {assertions} exact arithmetic assertions; full matching enumeration n=2..7; all stochastic tails checked.')

if __name__=='__main__':
    verify()
