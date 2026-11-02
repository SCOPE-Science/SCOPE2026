"""Check five symbolic extension tables in finite coordinate projective planes.
The theorem uses these tables from the projective-plane axioms; tests are examples.
"""
from collections import Counter

def field(q):
    if q in (2, 3, 5, 7):
        return (lambda x,y:(x+y)%q), (lambda x,y:(x*y)%q)
    if q == 4:
        def times(a,b):
            out=0
            while b:
                if b&1:out ^= a
                b>>=1
                a<<=1
                if a&4:a ^= 7
            return out
        return (lambda x,y:x^y), times
    raise ValueError(q)

def model(q):
    plus,times=field(q)
    points=[('a',x,y) for x in range(q) for y in range(q)]+[('i',m) for m in range(q)]+[('v',)]
    lines=[('s',m,b) for m in range(q) for b in range(q)]+[('v',a) for a in range(q)]+[('i',)]
    def incident(p,l):
        if l[0]=='i':return p[0]!='a'
        if p[0]=='a':
            if l[0]=='v':return p[1]==l[1]
            return p[2]==plus(times(l[1],p[1]),l[2])
        if l[0]=='v':return p[0]=='v'
        return p[0]=='i' and p[1]==l[1]
    return points,lines,incident

def inspect(q):
    points,lines,I=model(q)
    D=set(points)
    tests=0
    def test(observed,expected,name):
        nonlocal tests
        keys=set(observed)|set(expected)
        for key in keys:
            assert observed.get(key,0)==expected.get(key,0),(q,name,key,observed.get(key,0),expected.get(key,0))
            tests+=1
    A=('a',0,0);B=('a',1,0);C=('a',0,1)
    assert A!=B!=C!=A
    join=next(l for l in lines if I(A,l) and I(B,l))
    collinear_pts=next((tuple(p for p in points if I(p,l))[:3] for l in lines if len([p for p in points if I(p,l)])>=3))
    X,Y,Z=collinear_pts
    base=next(l for l in lines if I(X,l) and I(Y,l))
    newpts=Counter('on' if I(p,base) else 'off' for p in points if p not in (X,Y,Z))
    test(newpts,{'on':q-2,'off':q*q},'collinear new points')
    mask=Counter(tuple(I(t,l) for t in (X,Y,Z)) for l in lines)
    predicted={(1,1,1):1,(0,0,0):q*(q-2)}
    for bit in range(3):predicted[tuple(int(i==bit) for i in range(3))]=q
    test(mask,predicted,'collinear new lines')

    triple=(A,B,C)
    linesides={tuple(sorted((u,v))):next(l for l in lines if I(u,l) and I(v,l)) for u,v in [(A,B),(A,C),(B,C)]}
    assert len(set(linesides.values()))==3
    newpts=Counter(tuple(int(I(p,l)) for l in linesides.values()) for p in points if p not in triple)
    predicted={(0,0,0):(q-1)**2,(1,0,0):q-1,(0,1,0):q-1,(0,0,1):q-1}
    test(newpts,predicted,'noncollinear new points')
    newlines=Counter(tuple(int(I(p,l)) for p in triple) for l in lines)
    predicted={(0,0,0):(q-1)**2}
    for bit in range(3):
        predicted[tuple(int(i==bit) for i in range(3))]=q-1
        predicted[tuple(int(i!=bit) for i in range(3))]=1
    test(newlines,predicted,'noncollinear new lines')

    casepoint={
        2:{(1,1):q-1,(1,0):0,(0,1):0,(0,0):q*q},
        1:{(1,1):0,(1,0):q,(0,1):q-1,(0,0):q*(q-1)},
        0:{(1,1):1,(1,0):q,(0,1):q-2,(0,0):q*(q-1)}
    }
    caseline={
        2:{(1,1):0,(1,0):q,(0,1):q,(0,0):q*(q-1)},
        1:{(1,1):1,(1,0):q-1,(0,1):q,(0,0):q*(q-1)},
        0:{(1,1):1,(1,0):q,(0,1):q,(0,0):q*(q-1)-1}
    }
    for n in (0,1,2):
        chosen=next(l for l in lines if int(I(A,l))+int(I(B,l))==n and (n!=1 or I(A,l)))
        pprof=Counter((int(I(p,chosen)),int(I(p,join))) for p in points if p not in (A,B))
        test(pprof,casepoint[n],f'two points and line containing {n}: new points')
        lprof=Counter((int(I(A,l)),int(I(B,l))) for l in lines if l!=chosen)
        test(lprof,caseline[n],f'two points and line containing {n}: new lines')
    return len(points),len(lines),tests

if __name__=='__main__':
    for q in (2,3,4,5,7):
        np,nl,checks=inspect(q)
        print(f'order={q} points={np} lines={nl} checked_category_cells={checks} mismatches=0')
    print('All five configuration families and their duals agree with the polynomial counts.')
