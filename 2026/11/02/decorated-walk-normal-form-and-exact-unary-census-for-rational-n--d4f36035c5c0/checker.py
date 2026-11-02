"""Exact checks of bounded rational unary min-max fuzzy terms."""
from itertools import product

def grammar_closure(d):
    m=2*d
    vals={tuple(range(m+1))}
    vals.update({(2*k,)*(m+1) for k in range(d+1)})
    passes=[]
    while True:
        z=set(vals)
        for v in vals:
            z.add(tuple(m-t for t in v))
            for k in range(d+1):
                z.add(tuple(min(m,t+2*k) for t in v))
                z.add(tuple(max(0,t-2*k) for t in v))
        allv=list(z)
        for i,u in enumerate(allv):
            for v in allv[:i]:
                z.add(tuple(min(a,b) for a,b in zip(u,v)))
                z.add(tuple(max(a,b) for a,b in zip(u,v)))
        passes.append(len(z))
        if z == vals: return vals,passes
        vals=z

def expected(d):
    W=set()
    def extend(k, h, pts):
        if k==d:
            W.add(tuple(pts));return
        for step in (-1,1):
            if 0<=h+step<=d:
                extend(k+1,h+step,pts+[2*h+step,2*(h+step)])
        for z in (-1,0,1):
            if 0<=2*h+z<=2*d:
                extend(k+1,h,pts+[2*h+z,2*h])
    for h in range(d+1):extend(0,h,[2*h])
    return W

def matrix(d):
    a=[1]*(d+1)
    for _ in range(d):
        a=[(2 if i in (0,d) else 3)*a[i]+(a[i-1] if i>0 else 0)+(a[i+1] if i<d else 0) for i in range(d+1)]
    return sum(a)

if __name__=='__main__':
    for d in (1,2,3):
        actual,steps=grammar_closure(d)
        patterns=expected(d)
        count=matrix(d)
        assert actual==patterns, (d,len(actual),len(patterns),len(actual-patterns),len(patterns-actual))
        assert count==len(actual)
        print('grid',d,'closure=',len(actual),'passes=',steps,'matrix=',count)
    print('census', [(d,matrix(d)) for d in range(1,9)])
    print('ALL_CHECKS_OK')
