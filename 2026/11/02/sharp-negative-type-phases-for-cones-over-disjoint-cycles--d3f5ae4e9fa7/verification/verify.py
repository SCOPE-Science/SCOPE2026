"""Independent finite checks for Hilbert-snowflake thresholds on cycle cones.

Run with Python 3 standard library: python verify.py
"""
from itertools import combinations_with_replacement
from math import cos, pi, log2, isfinite, atan2, sin, sqrt


def jacobi_eigenvalues(mat):
    a=[row[:] for row in mat]
    m=len(a)
    if m==1: return [a[0][0]]
    for _ in range(60*m*m):
        i,j=max(((i,j) for i in range(m) for j in range(i+1,m)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[i][j])<3e-12: break
        ang=0.5*atan2(2*a[i][j],a[j][j]-a[i][i]); c=cos(ang); s=sin(ang)
        u,v,w=a[i][i],a[j][j],a[i][j]
        a[i][i]=c*c*u+s*s*v-2*c*s*w
        a[j][j]=s*s*u+c*c*v+2*c*s*w
        a[i][j]=a[j][i]=0.0
        for z in range(m):
            if z not in (i,j):
                x,y=a[z][i],a[z][j]
                a[z][i]=a[i][z]=c*x-s*y
                a[z][j]=a[j][z]=s*x+c*y
    else:
        raise AssertionError('Jacobi did not converge')
    return sorted(a[i][i] for i in range(m))


def q_threshold(lengths):
    n=sum(lengths)
    if len(lengths)==1 and lengths[0]==3: return float('inf'),0,'complete'
    global_q=2*(n-1)/(n-3)
    if any(m%2==0 for m in lengths): return 2.,sum(m%2==0 for m in lengths),'even-cycle'
    longest=max(lengths)
    if longest==3: return global_q,1,'global'
    c=cos(pi/longest)
    local_q=2*c/(2*c-1)
    if global_q<local_q: return global_q,1,'global'
    return local_q,2*sum(m==longest for m in lengths),'local'


def gram(lengths,q):
    n=sum(lengths)
    adj=[[False]*n for _ in range(n)]
    offset=0
    for ell in lengths:
        for i in range(ell):
            a,b=offset+i, offset+(i+1)%ell
            adj[a][b]=adj[b][a]=True
        offset+=ell
    return [[1. if i==j else .5 if adj[i][j] else 1.-q/2 for j in range(n)] for i in range(n)]


def pred_eigs(lengths,q):
    n=sum(lengths)
    spec=[(2*(n-1)-q*(n-3))/2]
    spec += [(3*q-2)/2]*(len(lengths)-1)
    for ell in lengths:
        for j in range(1,ell):
            lam=2*cos(2*pi*j/ell)
            spec.append((q+(q-1)*lam)/2)
    assert len(spec)==n
    return sorted(spec)

count=0
for r in range(1,4):
    for lengths in combinations_with_replacement(range(3,10),r):
        if sum(lengths)>30:continue
        qstar,rankdrop,regime=q_threshold(lengths)
        if not isfinite(qstar):
            for q in (1,2,10):
                assert min(jacobi_eigenvalues(gram(lengths,q)))>0.1
                count+=1
            continue
        for q in (1.,1+(qstar-1)*0.8,qstar,qstar+.15):
            measured=jacobi_eigenvalues(gram(lengths,q))
            expected=pred_eigs(lengths,q)
            assert max(abs(x-y) for x,y in zip(measured,expected))<2e-7,(lengths,q,'spectrum mismatch')
            if q<qstar-1e-8:assert measured[0]>1e-7,(lengths,q,'before')
            elif abs(q-qstar)<1e-8:
                assert sum(abs(x)<2e-7 for x in measured)==rankdrop,(lengths,q,'nullity',measured)
                assert measured[0]>-2e-7,(lengths,q,'at')
            else:assert measured[0]<-1e-4,(lengths,q,'beyond')
            count+=1

# Multi-cycle tests beyond the three-component sweep include critical
# eigenspaces of dimension four and six, plus a hub-global transition.
for lengths in ((7,7),(9,9,9),(5,5,3,3),(6,5,3,3),(5,3,3),(11,11),(7,3,3,3,3),(7,3,3,3,3,3)):
    qstar, rankdrop, regime = q_threshold(lengths)
    for q in (1.5, qstar, qstar+0.2):
        e=jacobi_eigenvalues(gram(lengths,q))
        predicted=pred_eigs(lengths,q)
        assert max(abs(x-y) for x,y in zip(e,predicted)) < 3e-7
        if abs(q-qstar)<1e-9:
            assert sum(abs(z)<3e-7 for z in e)==rankdrop
        else:
            assert (e[0]>0) if q<qstar else (e[0]<0)
        count+=1
assert q_threshold((7,7))[1:]==(4,'local')
assert q_threshold((9,9,9))[1:]==(6,'local')
assert q_threshold((5,5,3,3))[1:]==(1,'global')
assert q_threshold((7,3,3,3,3))[2]=='local'
assert q_threshold((7,3,3,3,3,3))[2]=='global'

# A five-cycle retains its critical exponent when one triangle is appended,
# then the global mode takes over after appending a second triangle.
assert q_threshold((5,))[2]=='local'
assert q_threshold((3,5))[2]=='local'
assert q_threshold((3,3,5))[2]=='global'
assert abs(q_threshold((3,3,5))[0]-2.5)<1e-12
assert abs(q_threshold((5,))[0]-(3+sqrt(5))/2)<1e-12
print('VERIFY_OK:',count,'independent finite Gram-eigenvalue tests over cone cycles; locality-to-global transition verified')
