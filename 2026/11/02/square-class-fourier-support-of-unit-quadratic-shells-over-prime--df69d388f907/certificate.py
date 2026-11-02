"""Exact cyclotomic tests for primitive and imprimitive Fourier multipliers of unit quadratic shells."""
from collections import defaultdict

def chi(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def zero_at_primitive_p2(c,p):
    return all(len({c[r+p*j] for j in range(p)})==1 for r in range(p))

def pred_vector(p,t,M):
    n=p*p; u,v,w=M; d=u*u+4*v*w
    c=[0]*n
    if (u,v,w)==(0,0,0):
        c[0]=p**4+p**3*chi(t,p)
    elif all(v%p==0 for v in M):
        d0=((u//p)**2+4*(v//p)*(w//p))%p
        for r in range(p):
            if r*r%p==(t*d0)%p:c[p*r]+=p**3*chi(t,p)
    elif (t*d)%p:
        for r in range(n):
            if r*r%n==(t*d)%n:c[r]+=p*p
    return c

def case(p,t,full=False):
    n=p*p
    shell=[(a,b,c) for a in range(n) for b in range(n) for c in range(n) if (a*a+b*c-t)%n==0]
    assert len(shell)==p**4 + chi(t,p)*p**3
    freqs=[(u,v,w) for u in range(n) for v in range(n) for w in range(n)] if full else [ (u,v,w) for u in range(n) for v in range(n) for w in range(n) if ((u*13+v*7+w*5+1)% (37 if p==5 else 317)==0)]
    nonzero=0
    for M in freqs:
        u,v,w=M
        c=[0]*n
        for a,b,d in shell:c[(u*a+v*b+w*d)%n]+=1
        ep=pred_vector(p,t,M)
        assert zero_at_primitive_p2([x-y for x,y in zip(c,ep)],p),('AMPLITUDE_MISMATCH',p,t,M)
        is_nonzero=not zero_at_primitive_p2(c,p)
        ep_nonzero=not zero_at_primitive_p2(ep,p)
        assert is_nonzero==ep_nonzero, ('ZERO_MISMATCH',p,t,M)
        nonzero+=is_nonzero
    eps=chi(t,p)
    rank=p*p+(p**3+1)*p*(p-1)*(p+eps)//2
    if full:assert nonzero==rank,('RANK',p,t,rank,nonzero)
    print('EXACT_UNIT_SHELL_AMPLITUDES_OK',p,t,'sample',len(freqs),'support',nonzero,'rank_formula',rank)

for p,ts in [(3,[1,2]),(5,[1,2]),(7,[1,3])]:
    for t in ts:case(p,t,p<=5)
