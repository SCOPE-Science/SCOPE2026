"""Exact-rational checks for the weighted single-shortcut path theorem.
Run with Python 3.11 or newer and SymPy (tested against SymPy 1.13).
The finite checks support, but do not replace, the general proof.
"""
from fractions import Fraction as F
from itertools import product
from sympy import symbols, factor, simplify, Matrix, Rational


def amplitude(n, ell):
    assert 1 <= ell <= n - 1
    eps = int((n-1-ell) % 2)
    return F(n*ell*(3*n*ell-2*ell*ell+2)-3*eps*ell*ell, 12)


def actual_amplitude(n, i, j):
    v = [min(max(x-i, 0),j-i) for x in range(n)]
    return F(n*sum(x*x for x in v)-sum(v)**2)


def score(n, ell, w):
    return w*amplitude(n, ell)/(1+w*ell)


def cutoff(n, k):
    return F(12*(k+1)*(n-2*k-2),
             (n-2*k-1)*(n-2*k-3)*(n-8*k-8))


def fast_best(n,w):
    values = [(score(n, n-1-2*k,w),k) for k in range((n-1)//8+1)]
    maximum = max(v for v,k in values)
    return tuple(k for v,k in values if v == maximum)


def direct_kirchhoff(n, i,j,w):
    L=Matrix.zeros(n)
    for a,b,c in [(x,x+1,Rational(1)) for x in range(n-1)]+[(i,j,Rational(w.numerator,w.denominator))]:
        L[a,a]+=c;L[b,b]+=c;L[a,b]-=c;L[b,a]-=c
    M=L + Matrix.ones(n)/n
    return n*(sum(M.inv()[a,a] for a in range(n))-1)


def run():
    checks=0
    n,l=symbols('n l', integer=True, positive=True)
    A0=lambda x: n*x*(3*n*x-2*x*x+2)/12
    assert simplify(A0(l)-A0(l-2)-n*(l-1)*(n+1-l)) == 0; checks+=1
    assert simplify(l*A0(l-2)-(l-2)*A0(l)-n*l*(l-2)*(4*l-3*n-4)/6)==0; checks+=1
    # The formula for balanced end-tails is independently recovered from the voltage ramp.
    k=(n-1-l)/2
    S1=l*(k+(l+1)/2)
    S2=l*l*k+l*(l+1)*(2*l+1)/6
    assert factor(n*S2-S1*S1-A0(l))==0; checks+=1
    # The exactly-one-vertex imbalance penalty, and its positive second difference.
    A_bad=lambda x: A0(x)-x*x/4
    assert factor(A0(l-1)+A0(l+1)-2*A_bad(l)-(n-l)**2/2)==0;checks+=1
    # Direct electrical-network and enumeration tests, with ties exactly retained.
    for nn in range(4,33):
        K=(nn-1)//8
        breaks=[cutoff(nn,k) for k in range(K)]
        assert all(breaks[x]<breaks[x+1] for x in range(len(breaks)-1))
        checks+=1
        candidates=[F(1,nn**3),F(1,100),F(1,nn),F(1),F(100),F(nn**3)]
        for b in breaks:
            candidates.extend([b, b*F(999,1000),b*F(1001,1000)])
        for w in candidates:
            all_vals={}
            for i in range(nn):
                for j in range(i+2,nn):
                    ell=j-i
                    v=actual_amplitude(nn,i,j)
                    assert v <= amplitude(nn,ell)
                    if i == (nn-1-ell)/2:
                        assert v == amplitude(nn,ell)
                    all_vals[i,j]=w*v/(1+w*ell)
                    checks+=1
            best=max(all_vals.values())
            true_pairs={ij for ij,sc in all_vals.items() if sc==best}
            pred_ks=fast_best(nn,w)
            pred_pairs={(kk,nn-1-kk) for kk in pred_ks}
            assert true_pairs==pred_pairs,(nn,w,true_pairs,pred_pairs)
            checks+=1
            if w in breaks:
                idx=breaks.index(w)
                assert pred_ks == (idx,idx+1),(nn,idx,pred_ks)
                checks+=1
    for nn in range(4,10):
        for w in [F(1,3),F(1),F(7,2)]:
            for i in range(nn):
                for j in range(i+2,nn):
                    K=direct_kirchhoff(nn,i,j,w)
                    expected=F(nn**3-nn,6)-w*actual_amplitude(nn,i,j)/(1+w*(j-i))
                    assert K==expected,(nn,i,j,w,K,expected)
                    checks+=1
    print(f'VERIFY_OK {checks} exact symbolic, rational placement, tie, and direct-matrix checks')

if __name__=='__main__':
    run()
