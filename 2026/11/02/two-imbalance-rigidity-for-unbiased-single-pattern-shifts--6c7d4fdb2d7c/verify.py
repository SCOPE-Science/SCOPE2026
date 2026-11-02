#!/usr/bin/env python3
"""Independent finite-state and border-polynomial checks for single-word avoidance."""
from itertools import product


def borders(w):
    return [(j, w[:j].count('1')) for j in range(1, len(w)+1)
            if w[:j] == w[-j:]]


def polynomial_data(w):
    bc = borders(w)
    def h(x):
        return (x - 2) * sum(x**(j-1) for j, _ in bc) + 1
    def dh(x):
        s = sum(x**(j-1) for j, _ in bc)
        return s + (x-2)*sum((j-1)*x**(j-2) for j, _ in bc if j >= 2)
    lo, hi = 1.1, 2.0
    assert h(lo)<0 and h(hi)>0
    for _ in range(70):
        mid=(lo+hi)/2
        if h(mid)<0: lo=mid
        else: hi=mid
    lam=(lo+hi)/2
    T=sum(lam**j for j, _ in bc)
    P=sum((j-2*c)*lam**j for j,c in bc)
    rho=.5 + P/(2*lam*T*dh(lam))
    return lam, rho, P, bc


def finite_state_density(w, iterations=500):
    k=len(w)
    trans=[[] for _ in range(k)]
    for i in range(k):
        for b in '01':
            s=w[:i]+b
            if s.endswith(w):
                continue
            j=max(t for t in range(k) if s.endswith(w[:t]))
            trans[i].append((j,int(b)))
    right=[1.0]*k
    left=[1.0]*k
    for _ in range(iterations):
        nxt=[sum(right[j] for j,b in trans[i]) for i in range(k)]
        sc=max(nxt);right=[a/sc for a in nxt]
        nxt=[0.0]*k
        for i in range(k):
            for j,b in trans[i]:nxt[j]+=left[i]
        sc=max(nxt);left=[a/sc for a in nxt]
    lr=sum(left[i]*right[i] for i in range(k))
    mean_eigen=sum(left[i]*right[j] for i in range(k) for j,b in trans[i])/lr
    mean_ones=sum(left[i]*right[j] for i in range(k) for j,b in trans[i] if b)/lr
    return mean_eigen,mean_ones/mean_eigen


def run():
    cases=0;max_error=0.0;max_lam_error=0.0
    for k in range(4,9):
        for bits in product('01',repeat=k):
            w=''.join(bits)
            if min(w.count('0'),w.count('1'))<2:continue
            lam,rho,P,b=polynomial_data(w)
            lam2,rho2=finite_state_density(w)
            max_error=max(max_error,abs(rho-rho2))
            max_lam_error=max(max_lam_error,abs(lam-lam2))
            assert abs(rho-rho2)<1e-9,(w,rho,rho2)
            assert abs(lam-lam2)<1e-9,(w,lam,lam2)
            assert b[-1][0]==k
            assert (1 if b[0][0]!=1 else -1) in (-1,1)
            cases+=1
    print('exhaustive two-of-each-letter cases length 4..8:', cases)
    print('max formula/automaton density discrepancy:',format(max_error,'.3g'))
    print('max formula/automaton eigenvalue discrepancy:',format(max_lam_error,'.3g'))
    for w in ('10001','100011110001','011100001110'):
        lam,rho,P,b=polynomial_data(w)
        lam2,rho2=finite_state_density(w)
        assert abs(rho-rho2)<1e-10 and abs(lam-lam2)<1e-10
        print(f'{w}: borders={b}, lambda={lam:.15f}, rho={rho:.15f}, P={P:.10g}')

if __name__=='__main__':run()
