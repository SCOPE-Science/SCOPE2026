"""Exact integer verification of finite-graph conditional-expectation commutators.
Requires Python 3.10 or later; no third-party packages.
Run: python verify.py
"""
from fractions import Fraction
from itertools import product

assertions=0

def check(condition, context):
    global assertions
    assert condition, context
    assertions+=1

def projective_plane(q):
    # q prime in these tests. Points and lines are projective classes in F_q^3.
    def representative(v):
        first=next((z for z in v if z), None)
        if first is None:return None
        return tuple(z*pow(first,-1,q)%q for z in v)
    classes=sorted({representative(v) for v in product(range(q),repeat=3)}-{None})
    return [[int(sum(x*y for x,y in zip(a,b))%q==0) for b in classes]
            for a in classes]

def verify(A, name):
    n=len(A)
    degree=sum(A[0])
    check(degree>=2,(name,'degree'))
    check(all(len(row)==n and sum(row)==degree for row in A),(name,'left degrees'))
    check(all(sum(row[j] for row in A)==degree for j in range(n)),(name,'right degrees'))
    E=[(i,j) for i in range(n) for j in range(n) if A[i][j]]
    check(len(E)==n*degree,(name,'edge count'))
    P=[[int(i==a) for a,b in E] for i,j in E]
    Q=[[int(j==b) for a,b in E] for i,j in E]
    min4=degree*degree
    max4=0
    maxrow=0
    for r,(i,j) in enumerate(E):
        c4=sum(A[a][b] for a in range(n) for b in range(n)
               if a!=i and b!=j and A[a][j] and A[i][b])
        min4=min(min4,c4)
        max4=max(max4,c4)
        check(0<=c4<=(degree-1)**2,(name,'four cycles',r))
        rowabs=0
        for s,(a,b) in enumerate(E):
            kernel=A[i][b]-A[a][j]
            # Check the two compositions directly as integer-scale operators.
            if len(E)<=60:
                pq=sum(P[r][t]*Q[t][s] for t in range(len(E)))
                qp=sum(Q[r][t]*P[t][s] for t in range(len(E)))
                check(kernel==pq-qp,(name,'composition',r,s))
            reverse=A[a][j]-A[i][b]
            check(kernel==-reverse,(name,'skew',r,s))
            rowabs+=abs(kernel)
        check(rowabs==2*((degree-1)**2-c4),(name,'exact row identity',r))
        maxrow=max(maxrow,rowabs)
    check(maxrow==2*((degree-1)**2-min4),(name,'sharp endpoint norm'))
    check(0<=maxrow<=2*(degree-1)**2,(name,'universal bound'))
    return degree,min4,max4,str(Fraction(maxrow,degree**2))

if __name__=='__main__':
    examples=[('K22',[[1]*2 for _ in range(2)]),
      ('K44',[[1]*4 for _ in range(4)]),
      ('crown4',[[int(i!=j) for j in range(4)] for i in range(4)]),
      ('C8',[[int(j in (i,(i+1)%4)) for j in range(4)] for i in range(4)]),
      ('crown5',[[int(i!=j) for j in range(5)] for i in range(5)])]
    for q in (2,3,5): examples.append((f'PG2_{q}',projective_plane(q)))
    for name,A in examples:
        degree,min4,max4,norm=verify(A,name)
        print(name,'left_size',len(A),'degree',degree,
              'min_four_cycles',min4,'max_four_cycles',max4,'endpoint_norm',norm)
        if name.startswith('PG2_'):
            q=int(name.split('_')[-1]);n=len(A)
            check(degree==q+1,(name,'incidence degree'))
            check(n==q*q+q+1,(name,'incidence size'))
            check(min4==max4==0,(name,'no squares'))
            check(norm==str(Fraction(2*q*q,(q+1)**2)),(name,'endpoint formula'))
            # Verify AA^T=qI+J, giving singular values q+1 and sqrt(q).
            for i in range(n):
                for j in range(n):
                    check(sum(A[i][k]*A[j][k] for k in range(n))==q*int(i==j)+1,
                          (name,'incidence spectrum',i,j))
    print('ALL_CHECKS_OK',assertions)
