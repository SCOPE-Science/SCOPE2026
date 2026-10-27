"""Exhaustive independent grading check for small finite Heisenberg Lie algebras."""
from itertools import product
from math import prod

def span_gens(gens,q,n):
    S={(0,)*n}
    for v in gens:
        S={tuple((a[i]+t*v[i])%q for i in range(n)) for a in S for t in range(q)}
    return frozenset(S)

def subspaces(q,n):
    zero=(0,)*n
    V=list(product(range(q),repeat=n))
    levels=[{frozenset([zero])}]
    for d in range(n):
        nxt=set()
        for sub in levels[-1]:
            for v in V:
                if v not in sub:
                    nxt.add(frozenset(tuple((a[i]+t*v[i])%q for i in range(n)) for a in sub for t in range(q)))
        levels.append(nxt)
    return levels

def lie_bracket(a,b,q,m):
    s=sum(a[i]*b[m+i]-a[m+i]*b[i] for i in range(m))%q
    return (0,)*(2*m)+(s,)

def count_brute(q,m):
    n=2*m+1; levels=subspaces(q,n)
    sub_by_dim=[[(sub, sorted(sub)[1:] if sub else []) for sub in lev] for lev in levels]
    total=0; cases={}
    zero=(0,)*n;z=(0,)*(n-1)+(1,)
    for d in range(n+1):
        for a, _ in sub_by_dim[d]:
            if z in a and d!=0:
                kind='even'; r=(n-d)//2
            else:
                kind='odd'
                r=None
            for b,_ in sub_by_dim[n-d]:
                if len(a.intersection(b))!=1:
                    continue
                # all square brackets within a must lie in a, within b must lie in a, cross must lie in b
                # use all elements to avoid reliance on grading formulas
                if any(lie_bracket(x,y,q,m) not in a for x in a for y in a):continue
                if any(lie_bracket(x,y,q,m) not in a for x in b for y in b):continue
                if any(lie_bracket(x,y,q,m) not in b for x in a for y in b):continue
                cat=('center_even',r) if z in a else ('center_odd',None)
                cases[cat]=cases.get(cat,0)+1;total+=1
    return total,cases,[len(x) for x in levels]

def sp(q,m):return q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))
def gl(q,m):return prod(q**m-q**i for i in range(m))
def count_closed(q,m):
    M=sp(q,m)
    cases={('center_even',r):q**(2*r)*M//(sp(q,r)*sp(q,m-r)) for r in range(m+1)}
    cases[('center_odd',None)]=q**m*M//gl(q,m)
    return sum(cases.values()),cases

if __name__=='__main__':
    for q,m in [(2,1),(3,1),(2,2)]:
        a,breakdown,subspaces_counts=count_brute(q,m)
        b,expected=count_closed(q,m)
        assert a==b and breakdown==expected,(q,m,a,b,breakdown,expected)
        print(f'field={q} Heisenberg_dimension={2*m+1} subspace_numbers={subspaces_counts} grading_total={a} strata={sorted((str(k),v) for k,v in breakdown.items())}')
    print('ALL_HEISENBERG_PARITY_GRADING_CHECKS_PASSED')
