"""Exact direct checks for random double-occurrence palindrome means."""
from itertools import combinations
from fractions import Fraction
from math import comb, factorial, prod, sqrt, exp, sinh

def words(q):
    used=[False]*(2*q); mate=[-1]*(2*q)
    def gen():
        try: i=used.index(False)
        except ValueError:
            labels=[-1]*(2*q); lab=0
            for k in range(2*q):
                if labels[k]<0:
                    labels[k]=labels[mate[k]]=lab;lab+=1
            yield tuple(labels);return
        used[i]=True
        for j in range(i+1,2*q):
            if not used[j]:
                used[j]=True;mate[i]=j;mate[j]=i
                yield from gen()
                used[j]=False
        used[i]=False
    yield from gen()

def count_pal(w):
    n=len(w);s=set()
    for mask in range(1,1<<n):
        t=tuple(w[i] for i in range(n) if mask>>i&1)
        if t==t[::-1]: s.add(t)
    return len(s)

def exact(q):
    return sum((Fraction(comb(q,m)*2*m,prod(range(1,2*m,2))) for m in range(1,q+1)),Fraction())

if __name__=='__main__':
    sizes=[]
    for q in range(1,6):
        vals=[count_pal(w) for w in words(q)]
        avg=Fraction(sum(vals),len(vals))
        assert avg==exact(q), (q,avg,exact(q))
        sizes.append(len(vals))
        print('EXACT_MEAN',q,len(vals),str(avg))
    for q in [20,100,400,1600]:
        t=Fraction(1); total=Fraction(0)
        for m in range(1,q+1):
            t*=Fraction(2*(q-m+1), (2*m-1)*(2*m-2)) if m>1 else 2*q
            total+=t
        lam=sqrt(2*q)
        ratio=float(total)/(exp(-0.25)*lam*sinh(lam))
        assert 0.90<ratio<1.03, (q,ratio)
        print('ASYMPTOTIC_RATIO',q,format(ratio,'.10f'))
    print('ALL_RANDOM_DOUBLE_OCCURRENCE_MEAN_CHECKS_PASSED canonical_cases',sum(sizes))
