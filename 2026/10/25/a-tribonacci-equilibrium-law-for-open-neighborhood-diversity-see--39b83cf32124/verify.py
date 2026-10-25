"""Exact verification of cyclic two-colour swap-equilibrium theorem.
Python 3. SymPy is needed only for the symbolic determinant check.
"""
from collections import Counter
from itertools import product
from sympy import Matrix, eye, symbols, factor, Poly


def transfer(z):
    words=list(product((0,1),repeat=3))
    M=Matrix.zeros(8)
    for i,(a,b,c) in enumerate(words):
        for d in (0,1):
            if (a,b,c,d) in {(0,1,0,1),(1,0,1,0)}: continue
            j=words.index((b,c,d))
            M[i,j]+=z**d
    return M


def payoff(x,i):
    n=len(x)
    return int((int(x[(i-1)%n]==x[i]) + int(x[(i+1)%n]==x[i]))==1)


def directly_stable(x):
    n=len(x)
    for i in range(n):
        for j in range(i+1,n):
            if x[i]==x[j]:continue
            ui,uj=payoff(x,i),payoff(x,j)
            if ui==1 or uj==1:continue
            y=list(x);y[i],y[j]=y[j],y[i]
            if payoff(y,j)>ui and payoff(y,i)>uj:return False
    return True


def locally_stable(x):
    n=len(x)
    return all(tuple(x[(i+r)%n] for r in range(4)) not in
               {(0,1,0,1),(1,0,1,0)} for i in range(n))


def trace(M):return sum(M[i,i] for i in range(M.rows))


def main():
    z,t,L=symbols('z t L')
    M=transfer(z)
    want=(1+z*t**2)*(1-(1+z)*t+z**2*t**4)
    assert factor((eye(8)-t*M).det()-want)==0
    assert factor(M.charpoly(L).as_expr() - L**2*(L**2+z)*(L**4-(1+z)*L**3+z**2))==0
    print('PASS: 8-state weighted transfer determinant and characteristic identity (symbolic).')
    samples={}
    for n in range(3,15):
        counts=Counter()
        for x in product((0,1),repeat=n):
            d=directly_stable(x)
            assert d==locally_stable(x), (n,x)
            if d:counts[sum(x)]+=1
        tr=Poly(trace(M**n),z)
        expected=[tr.nth(k) for k in range(n+1)]
        actual=[counts[k] for k in range(n+1)]
        assert actual==expected,(n,actual,expected)
        samples[n]=sum(actual)
    print('PASS: independent swap tests, forbidden-word tests and every coefficient for n=3..14.')
    print('Equilibrium totals:',samples)
    # independent order-four/Newton-sum recurrence for the unrestricted count
    tri=[3,1,3]
    for n in range(3,15):tri.append(sum(tri[-3:]))
    for n in range(3,15):
        expected=1+tri[n]+(2 if n%4==0 else -2 if n%4==2 else 0)
        assert samples[n]==expected
    print('PASS: tribonacci-Lucas closed total and mod-four correction n=3..14.')

if __name__=='__main__':main()
