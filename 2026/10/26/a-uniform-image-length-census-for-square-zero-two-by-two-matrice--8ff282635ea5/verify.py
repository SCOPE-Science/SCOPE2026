"""Reproduce counts of square-zero 2x2 matrices over F_q[t]/t^n.
No non-standard Python packages required.  Usage: python3 verify.py
"""
from collections import Counter
from itertools import product


def predicted(n, q):
    def primitive(e):
        G=(q*q-1)*(q*q-q)*q**(4*(e-1))
        U=(q-1)*(q+1)**2*q**(3*(e-1))
        out=Counter({2*e:G,e:U})
        for v in range(1,e):
            out[2*e-v]+=U*(q-1)*q**(e-v-1)
        return out
    out=Counter({0:1})
    for e in range(1,n//2+1): out.update(primitive(e))
    for k in range((n-1)//2+1):
        c=(q*q-1)*q**(2*n-2-k)
        out[n-k]+=c
        for j in range(1,k+1): out[n-k+j]+=c*(q-1)*q**(j-1)
    return {i:out[i] for i in range(n+1) if out[i]}


def field_add(a,b,q): return a^b if q in (2,4) else (a+b)%q

def field_mul(a,b,q):
    if q!=4: return a*b%q
    val=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&(b>>j)&1: val ^= (1<<(i+j))
    if val&8: val ^= 0b1100 # x^3+x^2+x; x^2=x+1
    if val&4: val ^= 0b0111 # x^2+x+1
    return val


def ring(q,n):
    Q=q**n
    digits=[]
    for x in range(Q):
        a=x;d=[]
        for j in range(n): d.append(a%q);a//=q
        digits.append(tuple(d))
    powers=[q**i for i in range(n)]
    add=[[0]*Q for _ in range(Q)];mul=[[0]*Q for _ in range(Q)]
    for x in range(Q):
        dx=digits[x]
        for y in range(Q):
            dy=digits[y]
            add[x][y]=sum(field_add(dx[i],dy[i],q)*powers[i] for i in range(n))
            z=0
            for i in range(n):
                c=0
                for j in range(i+1):
                    c=field_add(c,field_mul(dx[j],dy[i-j],q),q)
                z+=c*powers[i]
            mul[x][y]=z
    valuations=[next((j for j,t in enumerate(d) if t),n) for d in digits]
    return Q,add,mul,valuations,digits


def enumerate_case(q,n):
    Q,add,mul,val,digits=ring(q,n)
    actual=Counter()
    # Independent test uses square conditions, and Smith rank from primitive determinant.
    for a,b,c,d in product(range(Q),repeat=4):
        ab=mul[b][c]
        if add[mul[a][a]][ab] or add[ab][mul[d][d]]: continue
        ad=add[a][d]
        if mul[b][ad] or mul[c][ad]: continue
        k=min(val[a],val[b],val[c],val[d])
        if k==n:
            r=0
        else:
            e=n-k
            power=q**k
            aa=a//power;bb=b//power;cc=c//power;dd=d//power
            # det modulo t^e, computed via field extension ring directly
            _,a2,m2,vl2,_=ring_cache[(q,e)]
            bc=m2[bb][cc];diff=m2[aa][dd]
            # opposite of bc via additive inverse; in char two it is itself
            negbc=bc if q in (2,4) else sum(((-x)%q)*(q**i) for i,x in enumerate(ring_cache[(q,e)][4][bc]))
            det=a2[diff][negbc]
            r=e+(e-vl2[det])
        actual[r]+=1
    expect=predicted(n,q)
    assert dict(sorted(actual.items()))==expect, (q,n,actual,expect)
    total=sum(actual.values())
    f=n//2
    closed=q**(4*f)+((n+1)//2)*(q*q-1)*q**(2*n-2)
    assert total==closed,(q,n,total,closed)
    assert max(actual)<=n
    print('PASS',q,n,total,dict(sorted(actual.items())))


if __name__=='__main__':
    cases=[(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(4,1),(4,2)]
    ring_cache={(q,e):ring(q,e) for q,n in cases for e in range(1,n+1)}
    for q,n in cases: enumerate_case(q,n)
    print('SQUARE_ZERO_CHAIN_RING_ALL_OK',len(cases))


def verify_mixed_characteristic():
    """Completely independent modular-integer enumeration for Z/p^n."""
    for p, n in [(2,1), (2,2), (2,3), (2,4), (3,1), (3,2), (3,3), (5,1), (5,2)]:
        modulus=p**n
        valuations=[n if i==0 else next(k for k in range(n) if i%(p**(k+1))) for i in range(modulus)]
        out=Counter()
        for a in range(modulus):
            for b in range(modulus):
                for c in range(modulus):
                    for d in range(modulus):
                        if (a*a+b*c)%modulus or b*(a+d)%modulus or c*(a+d)%modulus or (d*d+b*c)%modulus:
                            continue
                        k=min(valuations[a], valuations[b], valuations[c], valuations[d])
                        if k==n:
                            rank=0
                        else:
                            submod=p**(n-k)
                            # Divide out a common p-adic factor before computing Smith minors.
                            aa=(a//p**k)%submod
                            bb=(b//p**k)%submod
                            cc=(c//p**k)%submod
                            dd=(d//p**k)%submod
                            determinant=(aa*dd-bb*cc)%submod
                            v=n-k if determinant==0 else next(t for t in range(n-k) if determinant % p**(t+1))
                            rank=2*(n-k)-v
                        out[rank]+=1
        assert dict(out)==predicted(n,p), (p,n,dict(out),predicted(n,p))
        print('PASS_MIXED',p,n,sum(out.values()),dict(sorted(out.items())))
    print('SQUARE_ZERO_MIXED_CHARACTERISTIC_OK 9')


verify_mixed_characteristic()
