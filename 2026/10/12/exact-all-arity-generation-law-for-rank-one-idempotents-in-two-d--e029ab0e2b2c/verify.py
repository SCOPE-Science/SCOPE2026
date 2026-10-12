"""Exhaustive tests for the rank-one idempotent generation formula.
Only Python's standard library is required.
"""
from itertools import product


def add(a,b,q):
    return a^b if q == 4 else (a+b)%q

def neg(a,q):
    return a if q == 4 else (-a)%q

def mul(a,b,q):
    if q != 4: return a*b%q
    z=0
    while b:
        if b&1: z^=a
        a<<=1
        if a&4: a^=7
        b>>=1
    return z

def inv(a,q):
    assert a
    return next(x for x in range(1,q) if mul(a,x,q)==1)

def matmul(A,B,q):
    a,b,c,d=A; e,f,g,h=B
    return (add(mul(a,e,q),mul(b,g,q),q),add(mul(a,f,q),mul(b,h,q),q),
            add(mul(c,e,q),mul(d,g,q),q),add(mul(c,f,q),mul(d,h,q),q))

def rank(vectors,q):
    rows=[list(v) for v in vectors]
    i=0
    for col in range(4):
        pivot=next((k for k in range(i,len(rows)) if rows[k][col]),None)
        if pivot is None: continue
        rows[i],rows[pivot]=rows[pivot],rows[i]
        fac=inv(rows[i][col],q)
        rows[i]=[mul(fac,x,q) for x in rows[i]]
        for k in range(len(rows)):
            if k != i and rows[k][col]:
                fac=rows[k][col]
                rows[k]=[add(x,neg(mul(fac,y,q),q),q) for x,y in zip(rows[k],rows[i])]
        i+=1
        if i==len(rows): break
    return i

def projective_lines(q):
    return [(1,t) for t in range(q)]+[(0,1)]

def projections(q):
    lines=projective_lines(q)
    ans=[]
    for image in lines:
        for kernel in lines:
            if image==kernel: continue
            a,c=image; b,d=kernel
            delta=add(mul(a,d,q),neg(mul(b,c,q),q),q)
            di=inv(delta,q)
            # S diag(1,0) S^-1: first column of S times first row S^-1
            P=(mul(mul(a,d,q),di,q),mul(mul(a,neg(b,q),q),di,q),
               mul(mul(c,d,q),di,q),mul(mul(c,neg(b,q),q),di,q))
            assert matmul(P,P,q)==P
            ans.append((P,image,kernel))
    assert len({P for P,_,_ in ans})==q*(q+1)
    return ans

def generates(mats,q):
    I=(1,0,0,1)
    basis=[I]
    for P in mats:
        if rank(basis+[P],q)>len(basis):basis.append(P)
    k=0
    while k<len(basis) and len(basis)<4:
        for P in mats:
            prod=matmul(basis[k],P,q)
            if rank(basis+[prod],q)>len(basis):basis.append(prod)
        k+=1
    return len(basis)==4

def formula(q,r):
    v=q+1
    return (q*v)**r - v*(2*q)**r+(v*(v-1)//2)*2**r

def run():
    for q,r in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2),(7,2)]:
        projs=projections(q)
        full=by_lines=0
        for tup in product(projs,repeat=r):
            mats=[x[0] for x in tup]
            common=set(tup[0][1:])
            for x in tup[1:]:common.intersection_update(x[1:])
            line_result=not common
            assert line_result == generates(mats,q), ('generation-disagreement',q,r,tup)
            full+=generates(mats,q)
            by_lines+=line_result
        target=formula(q,r)
        assert full==target==by_lines,(q,r,full,target,by_lines)
        print('q=%d r=%d total=%d generated=%d' % (q,r,len(projs)**r,full))
    print('VERIFY_OK')

if __name__=='__main__':run()
