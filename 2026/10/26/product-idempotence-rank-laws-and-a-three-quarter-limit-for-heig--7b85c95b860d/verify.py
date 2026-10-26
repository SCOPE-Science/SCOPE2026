"""Independent checks for idempotent-product census in height-two poset incidence algebras."""
from itertools import product
from collections import Counter

LABELS=list(product((0,1),repeat=2))

def weights(q,edges,n):
    totals=Counter()
    for colors in product(LABELS,repeat=n):
        dim=0
        for i,j in edges:
            a,b=colors[i]; c,d=colors[j]
            x=int(a!=c); y=int(b!=d)
            equation=(a*b==c*d) and ((x and d) or (y and a))
            dim+=x+y-int(equation)
        rank=(sum(a for a,b in colors),sum(b for a,b in colors),sum(a*b for a,b in colors))
        totals[rank]+=q**dim
    return totals

def brute(q,edges,n):
    diagonals=[(i,i) for i in range(n)]
    slots=diagonals+edges
    mats=[]
    def mul(a,b):
        return tuple(sum(a[i][k]*b[k][j] for k in range(n))%q for i in range(n) for j in range(n))
    def pack(a): return tuple(x for row in a for x in row)
    for vals in product(range(q),repeat=len(slots)):
        mat=[[0]*n for _ in range(n)]
        for (i,j),x in zip(slots,vals):mat[i][j]=x
        if mul(mat,mat)==pack(mat):mats.append((mat,sum(mat[i][i] for i in range(n))))
    total=Counter()
    for e,re in mats:
        for f,rf in mats:
            prod=mul(e,f)
            prodmat=[prod[i*n:(i+1)*n] for i in range(n)]
            if mul(prodmat,prodmat)==prod:
                total[(re,rf,sum(prod[i*n+i] for i in range(n)))]+=1
    return len(mats),total

def run():
    tests=[('edge',2,[(0,1)],2),('edge',3,[(0,1)],2),
        ('star2',2,[(0,1),(0,2)],3),('star2',3,[(0,1),(0,2)],3),
        ('star3',2,[(0,1),(0,2),(0,3)],4),
        ('K22',2,[(0,2),(0,3),(1,2),(1,3)],4),
        ('twoedges',2,[(0,1),(2,3)],4),
        ('fork',2,[(0,2),(0,3),(1,3)],4),
        ('isolated',3,[(0,1)],3)]
    for name,q,edges,n in tests:
        ni, actual=brute(q,edges,n)
        expected=weights(q,edges,n)
        assert actual==expected,(name,q,[(k,actual[k],expected[k]) for k in actual.keys()|expected.keys() if actual[k]!=expected[k]])
        print(name,q,'idempotents',ni,'product-idempotent ordered pairs',sum(actual.values()),'joint rank strata',len(actual),'PASS')
    for q in (2,3,4,5):
        for m in range(1,6):
            actual=sum(weights(q,[(0,i) for i in range(1,m+1)],m+1).values())
            expected=3*(1+q)**(2*m)+(1+3*q)**m
            assert actual==expected,(q,m,actual,expected)
    print('star formula symbolic-integer checks: 20 PASS')
    print('VERIFY_OK')
if __name__=='__main__': run()
