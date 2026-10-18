"""Independent checks for two-motif covariances in order-two de Bruijn cycles.
Uses exact rational arithmetic and complete enumeration at alphabet sizes 3 and 4.
"""
from fractions import Fraction
from itertools import product, permutations
from math import factorial

def formula(q,a,d,c,e):
    x,y,u,v = int(a==c),int(d==e),int(d==c),int(a==e)
    t=q*q-q*(2+x+y)+x+y+x*y-u-v-u*v
    p12=Fraction(t,q*q*(q-1)*(q-2))
    p1=Fraction(q-1-x,q*(q-1))
    p2=Fraction(q-1-y,q*(q-1))
    cov=p12-p1*p2
    n=x+y+u+v
    if n==0: expected=Fraction(1,q*q*(q-1))
    elif n==1: expected=Fraction(q-3,q*q*(q-1)*(q-2))
    elif x==y==1: expected=Fraction(q*q-5*q+5,q*q*(q-1)**2*(q-2))
    else:
        assert u==v==1
        expected=Fraction(q-5,q*q*(q-1)*(q-2))
    assert cov==expected,(q,a,d,c,e,cov,expected)
    return p12,p1,p2,cov

def motifs(q):
    for a,d in permutations(range(1,q),2):
        for c,e in permutations(range(1,q),2):
            yield a,d,c,e

def full_tour_counts(q):
    edges=list(product(range(q),repeat=2))
    idx={e:i for i,e in enumerate(edges)}
    inc=[[idx[(a,b)] for a in range(q)] for b in range(q)]
    out=[[idx[(b,c)] for c in range(q)] for b in range(q)]
    keys=list(motifs(q)); pairs=[(idx[(a,0)],idx[(0,c)],idx[(d,0)],idx[(0,e)]) for a,d,c,e in keys]
    counts=[0]*len(keys);total=0
    for local in product(permutations(range(q)),repeat=q):
        suc=[None]*(q*q)
        for b,pp in enumerate(local):
            for ai,ci in enumerate(pp):suc[inc[b][ai]]=out[b][ci]
        at=0;seen=0
        while True:
            seen+=1;at=suc[at]
            if at==0:break
        if seen!=q*q:continue
        total+=1
        for j,(ia,oc,id_,oe) in enumerate(pairs):
            if suc[ia]==oc and suc[id_]==oe: counts[j]+=1
    assert total==factorial(q)**q//q**2
    for key,cnt in zip(keys,counts):
        expected=formula(q,*key)[0]
        assert Fraction(cnt,total)==expected,(q,key,cnt,total,expected)
    return total,len(keys)

def det(M):
    a=[[int(x) for x in row] for row in M];n=len(a)
    if n==0:return 1
    sign=1;pr=1
    for k in range(n-1):
        if not a[k][k]:
            p=next((j for j in range(k+1,n) if a[j][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numer%pr==0
                a[i][j]=numer//pr
            a[i][k]=0
        pr=pivot
    return sign*a[-1][-1]

def cofactor_check(q):
    cases=0
    for a,d,c,e in motifs(q):
        # Explicitly contract (a,0)->(0,c) and (d,0)->(0,e).
        edges=list(product(range(q),repeat=2))
        edges.remove((a,0));edges.remove((0,c))
        edges.remove((d,0));edges.remove((0,e))
        edges.extend(((a,c),(d,e)))
        L=[[0]*q for _ in range(q)]
        for v,w in edges:
            L[v][v]+=1;L[v][w]-=1
        minor=[row[1:] for row in L[1:]]
        trees=det(minor)
        p=Fraction(trees,q**(q-2)*(q-1)*(q-2))
        assert p==formula(q,a,d,c,e)[0],(q,(a,d,c,e),p)
        cases+=1
    return cases

if __name__=='__main__':
    for q in (3,4):
        N,tests=full_tour_counts(q)
        print('EXHAUSTIVE_EULER',q,'cycles',N,'ordered_two_motifs',tests,'PASS')
    for q in (3,4,5,6):
        cases=cofactor_check(q)
        c={'+':0,'0':0,'-':0}
        for key in motifs(q):
            v=formula(q,*key)[3]
            c['+' if v>0 else '-' if v<0 else '0']+=1
        print('INDEPENDENT_COFATORS',q,'cases',cases,'covariance_signs',c,'PASS')
    print('ALL_COVARIANCE_CHECKS_PASSED')
