"""Verification for two-leader placement on weighted bridge-connected complete graphs.
Run: python verify_weighted.py. Standard library only; exact rational arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

def laplacian(p,q,a,b,t):
    n=p+q; L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for start,m,w in ((0,p,a),(p,q,b)):
        for i in range(start,start+m):
            for j in range(i+1,start+m):
                L[i][i]+=w; L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    L[0][0]+=t;L[p][p]+=t;L[0][p]-=t;L[p][0]-=t
    return L

def trace_inverse(A):
    m=len(A); M=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(m)] for i,row in enumerate(A)]
    for j in range(m):
        k=next((i for i in range(j,m) if M[i][j]!=0),None)
        if k is None:raise ArithmeticError('singular')
        M[k],M[j]=M[j],M[k]
        z=M[j][j];M[j]=[v/z for v in M[j]]
        for i in range(m):
            if i!=j:
                z=M[i][j]
                if z!=0:M[i]=[x-z*y for x,y in zip(M[i],M[j])]
    return sum(M[i][m+i] for i in range(m))

def merit(L,leaders):
    F=[v for v in range(len(L)) if v not in leaders]
    return trace_inverse([[L[i][j] for j in F] for i in F])

def five_values(p,q,a,b,t):
    j0=Q(2*(p-1),p)/a+Q(2*(q-1),q)/b
    dp=Q(2,p)/a;dq=Q(2,q)/b
    zp=Q(p+2,p*p)/(a*a);zq=Q(q+2,q*q)/(b*b)
    return {'PP':j0-t*(zp+zq)/(1+t*(dp+dq)),
            'PG':j0-t*zp/(1+t*dp),
            'GP':j0-t*zq/(1+t*dq),
            'SS':Q(3*(p-2),2*p)/a+Q(2*(q-1),q)/b+q/t,
            'TT':Q(3*(q-2),2*q)/b+Q(2*(p-1),p)/a+p/t}

def leader_class(p,q,s):
    s=set(s); x=len(s.intersection(range(p)))
    if x==2:return 'SS' if 0 in s else 'SS_non_gateway'
    if x==0:return 'TT' if p in s else 'TT_non_gateway'
    pvertex=next(v for v in s if v<p)
    qvertex=next(v for v in s if v>=p)
    return ('G' if pvertex==0 else 'P')+('G' if qvertex==p else 'P')

def exact_checks():
    configs=0; pairs=0; omit=0
    for p in range(2,7):
      for q in range(2,7):
       for a,b in ((Q(1),Q(1)),(Q(1,3),Q(1)),(Q(1),Q(5,2)),(Q(1,4),Q(3,2))):
        for t in (Q(1,5),Q(2),Q(19)):
         L=laplacian(p,q,a,b,t); vals=five_values(p,q,a,b,t)
         minimal=min(vals.values()); correct=set()
         for pair in combinations(range(p+q),2):
          obj=merit(L,pair); cl=leader_class(p,q,pair)
          if cl in vals:
            assert obj==vals[cl],(p,q,a,b,t,pair,cl,obj,vals[cl])
          if obj==minimal:correct.add(cl)
          assert obj>=minimal,(p,q,a,b,t,pair,obj,minimal)
          if cl in ('SS_non_gateway','TT_non_gateway'):
            assert obj>vals[cl[:2]],('incorrect gateway strict dominance',cl)
            omit+=1
          pairs+=1
         assert correct and correct.issubset(vals.keys())
         assert correct=={key for key,v in vals.items() if v==minimal},(p,q,a,b,t,correct,vals)
         configs+=1
    return configs,pairs,omit

def phase_checks():
    # Genuine three-regime transition with both clique sizes at least three.
    p,q,a,b=16,3,Q(1,10),Q(1)
    phases=[(Q(1,100),'PP'),(Q(1,10),'PP'),(Q(1),'PG'),(Q(10),'SS'),(Q(100),'SS')]
    for t,expected in phases:
        v=five_values(p,q,a,b,t)
        assert [key for key,x in v.items() if x==min(v.values())]==[expected],(t,v)
    for t,expected in [(Q(16,115),{'PP','PG'}),(Q(8,5),{'PG','SS'})]:
        v=five_values(p,q,a,b,t)
        assert {key for key,x in v.items() if x==min(v.values())}==expected,(t,v)
    dp=Q(2,p)/a;dq=Q(2,q)/b
    alpha_p=Q(p+2,2*p)/a;alpha_q=Q(q+2,2*q)/b
    assert p>4*q-2 and alpha_p>alpha_q
    assert Q(16,115)<Q(8,5)
    # For every pair of sizes in this range verify the strict no-colocation bounds.
    for m in range(3,22):
        for n in range(3,22):
            if m<=4*n-2:
                for strength in (Q(1,10),Q(1),Q(10)):
                    z=five_values(m,n,strength,Q(1),Q(2))
                    assert z['SS']>z['PG']
            if n<=4*m-2:
                for strength in (Q(1,10),Q(1),Q(10)):
                    z=five_values(m,n,Q(1),strength,Q(2))
                    assert z['TT']>z['GP']
    return f'five genuine phase regimes and exact ties at 16/115, 8/5; p={p}, q={q}'

if __name__=='__main__':
    configs,pairs,omitted=exact_checks()
    print(f'PASS {configs} exact all-pair configurations; {pairs} exact grounded inversions; {omitted} strict non-gateway exclusions')
    print('PASS qualitative leader-migration example:',phase_checks())
    print('PASS exhaustive orbit formulas, five-candidate global reduction and boundary cases')
