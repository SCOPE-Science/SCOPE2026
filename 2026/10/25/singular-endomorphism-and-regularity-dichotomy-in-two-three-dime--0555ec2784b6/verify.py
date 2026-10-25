"""Finite-field verification of endomorphism rank and regularity laws.
Run: python verify.py. Uses the Leibniz multiplication table, not the claimed normal forms.
"""
from itertools import product
from collections import Counter


def mm(a,b,p):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%p for j in range(3)) for i in range(3))


def rank(a,p):
    a=[list(r) for r in a]; z=0
    for col in range(3):
        ind=next((i for i in range(z,3) if a[i][col]%p),None)
        if ind is None: continue
        a[z],a[ind]=a[ind],a[z]
        inv=pow(a[z][col],-1,p)
        a[z]=[(t*inv)%p for t in a[z]]
        for i in range(z+1,3):
            if a[i][col]:
                c=a[i][col]
                a[i]=[(a[i][k]-c*a[z][k])%p for k in range(3)]
        z+=1
    return z


def forms(family,p,lam=1):
    if family=='J': return ((0,1),(0,0))
    return ((1,0),(0,lam))


def bval(x,y,b,p):
    return sum(x[i]*b[i][j]*y[j] for i in range(2) for j in range(2))%p


def enumerate_endo(family,p,lam=1):
    b=forms(family,p,lam)
    out=[]
    for a,b0,c,d in product(range(p), repeat=4):
        x=(a,b0); y=(c,d)
        # Derive required central scalar from one nonzero bracket and test ALL four basis pairs.
        s=bval(x,y,forms(family,p,lam),p) if family=='J' else bval(x,x,forms(family,p,lam),p)
        pair=(x,y)
        if any(bval(pair[i],pair[j],forms(family,p,lam),p)!=(s*forms(family,p,lam)[i][j])%p
               for i in range(2) for j in range(2)): continue
        for u,v in product(range(p),repeat=2):
            f=((a,c,0),(b0,d,0),(u,v,s))
            out.append(f)
    return out


def check(family,p,lam,regular_bruteforce):
    end=enumerate_endo(family,p,lam)
    hist=Counter(rank(x,p) for x in end)
    idem=sum(mm(x,x,p)==x for x in end)
    if family=='J':
        want={0:1,1:(p*p-1)*(2*p+1),2:2*p*(p-1)*(p*p-1),3:p*p*(p-1)**2}
        ni=2*p*p+2
        nr=p**4+p*p-2*p+1
    else:
        want={0:1,1:p*p-1,2:0,3:2*p*p*(p*p-1)}
        ni=2
        nr=1+2*p*p*(p*p-1)
    assert sum(want.values())==len(end) and all(hist[r]==want[r] for r in range(4)), (family,p,dict(hist),want)
    assert idem==ni,(family,p,idem,ni)
    if regular_bruteforce:
        regular=sum(any(mm(mm(f,g,p),f,p)==f for g in end) for f in end)
        assert regular==nr,(family,p,regular,nr)
    print(f'PASS {family} F_{p} lambda={lam}: endomorphisms={len(end)}, ranks={tuple(hist[i] for i in range(4))}, idempotents={idem}, regular_count={nr}'+(' brute-verified' if regular_bruteforce else ' proved-formula'))


if __name__=='__main__':
    check('J',2,1,True)
    check('J',3,1,True)
    check('J',5,1,False)
    check('H',3,1,True) # -1 nonsquare modulo 3
    check('H',5,2,False) # -2 nonsquare modulo 5
    check('H',7,4,False) # -4=3 nonsquare modulo 7
    print('VERIFY_OK')
