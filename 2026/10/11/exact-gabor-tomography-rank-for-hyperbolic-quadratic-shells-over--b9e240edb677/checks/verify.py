"""Exact checks for Fourier-zero classification of a hyperbolic sphere Gabor window.

Requires Python 3 and NumPy. In prime fields every ambiguity coefficient is a
sum of p-th roots of unity with integral multiplicities; that sum vanishes
exactly when all p residue multiplicities coincide. No tolerance is used.
"""
from itertools import product
from random import Random
import numpy as np


def quadratic_character_prime(a, p):
    a = int(a) % p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)


def predicted_rank(q, r):
    m = 2*r
    N = q**m
    n_star = q**(m-1)-q**(r-1)
    iso_nonzero = q**(m-1)+(q-1)*q**(r-1)-1
    # All nonzero quadratic-level fibers contain n_star translation vectors.
    # The discriminant character sum over t != 0,4 equals -1.
    return (N + iso_nonzero*q**(m-1) + n_star*(
        N-q**(m-1)+q + (q-2)*(N-(q-1)*q**(m-1)//2)
        -(q-1)*q**r//2))


def verify_prime(p, r):
    m = 2*r
    coords = np.array(list(product(range(p), repeat=m)), dtype=np.int16)
    N = len(coords)
    x,y = coords[:,:r], coords[:,r:]
    Q = np.sum(x*y, axis=1) % p
    sphere = Q == 1
    B = (x @ y.T + y @ x.T) % p  # B[b,x] in characteristic p
    dual_rows = np.arange(N, dtype=np.int64)[:,None] * p
    inv2,inv4 = pow(2,-1,p),pow(4,-1,p)
    chi=np.array([quadratic_character_prime(v,p) for v in range(p)])
    observed=0
    for a_idx,a in enumerate(coords):
        t=int(Q[a_idx]); h=B[:,a_idx]
        if a_idx==0: predicted_zero=np.zeros(N,dtype=bool)
        elif t==0: predicted_zero = (h != 0)
        else:
            wnorm=(Q-h*h*pow(4*t,-1,p)) % p
            c=(1-t*inv4)%p
            if c==0:
                alpha=(h*pow(2*t,-1,p))%p
                w=(coords-alpha[:,None]*a)%p
                predicted_zero=(wnorm==0) & np.any(w!=0,axis=1)
            else: predicted_zero=(chi[(c*wnorm)%p] == -1)
        differences=(coords-a)%p
        intersect=sphere & (np.sum(differences[:,:r]*differences[:,r:],axis=1)%p == 1)
        bins=np.bincount((dual_rows+B[:,intersect]).ravel(),minlength=N*p).reshape(N,p)
        actual_zero=np.all(bins==bins[:,0,None],axis=1)
        bad=np.flatnonzero(actual_zero != predicted_zero)
        if len(bad):
            raise AssertionError((p,r,'first mismatch at',int(a_idx),int(bad[0]),bins[bad[0]].tolist()))
        observed += N-int(actual_zero.sum())
    expected=predicted_rank(p,r)
    assert observed==expected,(p,r,observed,expected)
    print('PRIME_EXACT',p,r,'ambiguity_pairs',N*N,'nonzero',observed,'zeros',N*N-observed)

# F_9 = F_3[z]/(z^2+1), represented by a+3*b with z^2=2.
P=3

def pair(a):return a%3,a//3

def fadd(a,b):
    aa,ab=pair(a);ba,bb=pair(b)
    return (aa+ba)%3 + 3*((ab+bb)%3)

def fneg(a):
    aa,ab=pair(a)
    return (-aa)%3 + 3*((-ab)%3)

def fsub(a,b):return fadd(a,fneg(b))

def fmul(a,b):
    aa,ab=pair(a);ba,bb=pair(b)
    return (aa*ba+2*ab*bb)%3 + 3*((aa*bb+ab*ba)%3)

def fpow(a,n):
    out=1
    while n:
        if n&1:out=fmul(out,a)
        a=fmul(a,a);n//=2
    return out

def finv(a):
    assert a
    return fpow(a,7)

def fdiv(a,b):return fmul(a,finv(b))

def fchi(a):
    return 0 if a==0 else (1 if fpow(a,4)==1 else -1)

def trace(a):return (2*(a%3))%3

def q4(v):return fadd(fmul(v[0],v[2]),fmul(v[1],v[3]))

def b4(v,w):
    z=0
    for i in range(2):
        z=fadd(z,fadd(fmul(v[i],w[i+2]),fmul(v[i+2],w[i])))
    return z


def verify_gf9():
    fieldvectors=list(product(range(9),repeat=4))
    sphere=[x for x in fieldvectors if q4(x)==1]
    assert len(sphere)==9**3-9
    zero=(0,0,0,0)
    rng=Random(78293)
    labels=set(); total=0
    for a,b in [(zero,zero)]+[(rng.choice(fieldvectors),rng.choice(fieldvectors)) for _ in range(500)]:
        t=q4(a)
        if a==zero: expected_zero=False; label='zero_shift'
        elif t==0: expected_zero=(b4(a,b)!=0);label='isotropic_shift'
        else:
            c=fsub(1,fdiv(t,1))  # 4 in characteristic 3 is field element 1
            h=b4(a,b)
            alpha=fdiv(h,fmul(2,t))
            w=tuple(fsub(b[i],fmul(alpha,a[i])) for i in range(4))
            hnorm=q4(w)
            if c==0:
                expected_zero=(w!=zero and hnorm==0)
                label='zero_section'
            else:
                expected_zero=(fchi(fmul(c,hnorm))==-1)
                label='nonzero_section'
        bins=[0,0,0]
        for x in sphere:
            xa=tuple(fsub(x[i],a[i]) for i in range(4))
            if q4(xa)==1:
                bins[trace(b4(b,x))]+=1
        actual_zero=bins[0]==bins[1]==bins[2]
        assert actual_zero==expected_zero,(a,b,label,bins,expected_zero)
        labels.add(label); total+=1
    assert labels=={'zero_shift','isotropic_shift','zero_section','nonzero_section'},labels
    print('GF9_EXACT',total,'character_trace_fiber_checks','all_four_cases',sorted(labels))

if __name__=='__main__':
    for p,r in [(3,2),(5,2),(3,3)]:verify_prime(p,r)
    verify_gf9()
    print('VERIFY_OK')
