"""Reproducible exact checks of conditional inversion laws for forced successions.
Only Python standard library; finite tests support, do not replace, the proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial


def parts(n, joins):
    lens=[]
    run=1
    for i in range(1,n):
        if i in joins:
            run+=1
        else:
            lens.append(run)
            run=1
    lens.append(run)
    return lens


def inv(a):
    return sum(x>y for j,x in enumerate(a) for y in a[j+1:])


def predicted_dist(lengths):
    b=len(lengths)
    return Counter(sum(lengths[i]*lengths[j] for i in range(b) for j in range(i+1,b) if sig[i]>sig[j]) for sig in permutations(range(b)))


def formula_mean_var(lengths):
    n=sum(lengths)
    mean=Fraction(n*n-sum(z*z for z in lengths),4)
    pref=0
    sq=0
    for ell in lengths:
        sq+=ell*ell*(n-ell-2*pref)**2
        pref+=ell
    sq+=sum(lengths[i]**2*lengths[j]**2 for i in range(len(lengths)) for j in range(i+1,len(lengths)))
    return mean,Fraction(sq,12)


def moments(dist):
    total=sum(dist.values())
    m=Fraction(sum(x*k for x,k in dist.items()),total)
    v=Fraction(sum((x-m)**2*k for x,k in dist.items()),total)
    return m,v


def forced_dist_brute(n,joins):
    return Counter(inv(p) for p in permutations(range(1,n+1)) if all(p[i]==p[i-1]+1 for i in joins))


def specialized_var(n,L,a):
    h=n-L
    return (Fraction(h*(6*L*L*h+12*L*L+2*h*h+3*h-5),72)
            -Fraction(L*(L-1)*a*(h-a),3))


def run():
    c=0
    for n in range(2,8):
        for mask in range(1<<(n-1)):
            joins={i for i in range(1,n) if mask & (1<<(i-1))}
            lens=parts(n,joins)
            brute=forced_dist_brute(n,joins)
            expected=predicted_dist(lens)
            # b! permutations under the event, including incidental extra successions
            assert brute==expected,(n,joins,lens,brute,expected)
            assert sum(brute.values())==factorial(len(lens))
            assert moments(brute)==formula_mean_var(lens),(n,joins,lens)
            c+=3
        for L in range(2,n+1):
            h=n-L
            vals=[]
            for a in range(h+1):
                lens=[1]*a+[L]+[1]*(h-a)
                _,actual=formula_mean_var(lens)
                assert actual==specialized_var(n,L,a),(n,L,a,actual,specialized_var(n,L,a))
                vals.append(actual)
                c+=1
            assert vals==vals[::-1]
            assert all(vals[a]>=vals[a+1] for a in range(h//2))
            assert vals[0]-min(vals)==Fraction(L*(L-1)*(h*h//4),3)
            c+=3
    # Larger word, non-exhaustive block order distributions but still exact enumeration of b! blocks
    for n in (8,9):
        for joins in ({1,3,4}, {2,3,5,6}, set(range(1,n)), set()):
            joins={i for i in joins if i<n}
            ls=parts(n,joins)
            assert formula_mean_var(ls)==moments(predicted_dist(ls))
            c+=1
    print(f'PASS: {c} exact assertions; all block event laws, means, variances and threshold extrema checked')


if __name__=='__main__':
    run()
