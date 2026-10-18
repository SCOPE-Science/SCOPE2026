"""Finite exact-rational checks for section-face enumeration; proof is in RESULT.md."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from random import Random

def rank(rows):
    if not rows: return 0
    a=[list(map(Q,row)) for row in rows]
    nr,nc=len(a),len(a[0]); r=0
    for j in range(nc):
        pivot=next((i for i in range(r,nr) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        t=a[r][j];a[r]=[z/t for z in a[r]]
        for i in range(nr):
            if i!=r and a[i][j]:
                t=a[i][j];a[i]=[v-t*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==nr:break
    return r

def section_vertices(scores):
    n=len(scores); order=sorted(range(n),key=lambda j:scores[j]); out=set()
    for low,middle,high in combinations(order,3):
        a=Q(scores[middle]-scores[low]); b=Q(scores[high]-scores[middle]);
        x=[Q(0) for _ in range(n)]
        x[low]=-b/(a+b);x[middle]=Q(1);x[high]=-a/(a+b)
        out.add(tuple(x));out.add(tuple(-y for y in x))
    return out

def faces_by_subsets(n):
    f=[0]*(n-2)
    for m in range(3,n+1):
        count=0
        for union in combinations(range(n),m):
            for b in range(1,(1<<m)-1):
                I=[union[j] for j in range(m) if b>>j&1]
                J=[union[j] for j in range(m) if not (b>>j&1)]
                if min(I)<max(J) and min(J)<max(I): count+=1
        f[m-3]=count
    return f

def check(n,scores):
    expected=[comb(n,m)*(2**m-2*m) for m in range(3,n+1)]
    assert faces_by_subsets(n)==expected
    v=section_vertices(scores)
    assert len(v)==expected[0]
    assert all(sum(x)==0 and sum(x[i]*scores[i] for i in range(n))==0 for x in v)
    for mask in range(1,(1<<n)-1):
        I=[i for i in range(n) if mask>>i&1]
        contact=[x for x in v if sum(x[i] for i in I)==1]
        # Polar inequalities of the root polytope, checked at every section vertex.
        assert all(sum(x[i] for i in I)<=1 for x in v)
        separated= max(scores[i] for i in I)<min(scores[i] for i in range(n) if i not in I) or min(scores[i] for i in I)>max(scores[i] for i in range(n) if i not in I)
        assert bool(contact)==(not separated)
        if contact:
            assert rank([tuple(xi-yi for xi,yi in zip(x,contact[0])) for x in contact[1:]])==n-3
    return expected,len(v)

if __name__=='__main__':
    rng=Random(311)
    cases=0
    for n in range(3,8):
        for k in range(3):
            vals=[j*137+j*j*3 for j in range(n)]
            rng.shuffle(vals)
            result,count=check(n,vals)
            print(f'n={n} normal={k} section_f_vector={result} vertices={count}')
            cases+=1
    print(f'ROOT_CENTRAL_SECTION_OK cases={cases}')

# Additional exact facet polygon-size spectrum for the 3-dimensional case.
def facet_size_spectrum(n=5):
    scores=list(range(n)); vertices=section_vertices(scores)
    counts={}
    for mask in range(1,(1<<n)-1):
        I=[i for i in range(n) if mask>>i&1]
        count=sum(sum(x[i] for i in I)==1 for x in vertices)
        if count:
            counts[count]=counts.get(count,0)+1
            # Independent rank-order expression: three alternating membership labels.
            alt=0
            for a,b,c in combinations(range(n),3):
                bit=lambda t:int(t in I)
                if bit(a)==bit(c)!=bit(b):alt+=1
            assert count==alt
    assert counts=={3:10,4:10,5:2},counts
    print('A4_SECTION_FACET_SIZE_SPECTRUM_OK',counts)
facet_size_spectrum()
