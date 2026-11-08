"""Exact checks for the 3x3 minimum-support Birkhoff formula (Python 3 stdlib)."""
from itertools import permutations, combinations_with_replacement
from math import comb

PERMS = list(permutations(range(3)))
EVEN = [(0,1,2),(1,2,0),(2,0,1)]
ODD = [(0,2,1),(1,0,2),(2,1,0)]
ORDER = EVEN + ODD
assert set(ORDER) == set(PERMS)

def add_matrix(c):
    D = [[0]*3 for _ in range(3)]
    for w,p in zip(c,ORDER):
        for i,j in enumerate(p):
            D[i][j]+=w
    return tuple(x for row in D for x in row)

def endpoint_weights(D):
    a,b,c,d,e,f,g,h,i=D
    # c0=t; c1=b-i+t; c2=c-e+t;
    # c3=a-t; c4=i-t; c5=e-t.
    lo=max(0,i-b,e-c)
    hi=min(a,i,e)
    assert lo<=hi
    def w(t):return (t,b-i+t,c-e+t,a-t,i-t,e-t)
    return w(lo),w(hi),lo,hi

checks=0; cases=0
for q in range(1,13):
    opt={}
    for c0 in range(q+1):
      for c1 in range(q-c0+1):
       for c2 in range(q-c0-c1+1):
        for c3 in range(q-c0-c1-c2+1):
         for c4 in range(q-c0-c1-c2-c3+1):
          c5=q-c0-c1-c2-c3-c4
          c=(c0,c1,c2,c3,c4,c5)
          D=add_matrix(c)
          supp=sum(x>0 for x in c)
          opt[D]=min(opt.get(D,7),supp)
    for D,ref in opt.items():
        w0,w1,lo,hi=endpoint_weights(D)
        assert all(x>=0 for x in w0+w1)
        assert add_matrix(w0)==D and add_matrix(w1)==D
        got=min(sum(x>0 for x in w0),sum(x>0 for x in w1))
        assert got==ref, (q,D,got,ref)
        assert sum(D[j] for j in (0,1,2))==q
        checks+=5
    cases+=len(opt)
    print('q',q,'distinct_matrices',len(opt))
print('PASS',cases,'distinct integer transportation matrices across q; ',checks,'assertions')
# A dense generic 3x3 example has sharp k=5, and is attained by both endpoints.
co=(1,2,3,1,2,4)
D=add_matrix(co)
w0,w1,lo,hi=endpoint_weights(D)
print('example D normalized denominator',sum(co),'numerator', [D[i:i+3] for i in (0,3,6)])
print('endpoints',w0,w1,'supports',sum(x>0 for x in w0),sum(x>0 for x in w1))
