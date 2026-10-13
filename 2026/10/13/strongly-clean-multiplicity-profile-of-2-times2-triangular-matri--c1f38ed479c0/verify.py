from collections import Counter


def matmul(A,B,q):
    a,b,c=A; d,e,f=B
    return ((a*d)%q,(a*e+b*f)%q,(c*f)%q)

def idem(E,q):
    return matmul(E,E,q)==E

def commute(A,E,q):
    return matmul(A,E,q)==matmul(E,A,q)

def unit(A,q):
    a,b,c=A
    return a%q!=0 and c%q!=0

def sub(A,E,q):
    return tuple((x-y)%q for x,y in zip(A,E))

def mu(A,q):
    a,b,c=A
    if a!=c: return 1
    return q if b==0 else 0

def predicted(A,q):
    a,b,c=A
    m=mu(A,q)
    return int(a!=0 and c!=0)+int(a!=1 and c!=1)+m*(int(a!=1 and c!=0)+int(a!=0 and c!=1))

def expected_hist(q):
    if q==2:
        return Counter({1:8})
    return Counter({1:4*q,2:(q-2)*(5*q-1),4:q*(q-2)*(q-3),2*q+2:q-2})

def run(q):
    els=[(a,b,c) for a in range(q) for b in range(q) for c in range(q)]
    idems=[E for E in els if idem(E,q)]
    hist=Counter()
    for A in els:
        count=sum(1 for E in idems if commute(A,E,q) and unit(sub(A,E,q),q))
        p=predicted(A,q)
        if count!=p:
            raise AssertionError((q,A,count,p))
        hist[count]+=1
    if hist!=expected_hist(q):
        raise AssertionError((q,hist,expected_hist(q)))
    print(f'q={q} elements={len(els)} idempotents={len(idems)} histogram={dict(sorted(hist.items()))}')

for q in (2,3,5,7):
    run(q)
print('VERIFY_OK')
