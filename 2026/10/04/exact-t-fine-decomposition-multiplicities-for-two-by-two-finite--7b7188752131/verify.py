from itertools import product

def det(A,q):
    a,b,c,d=A
    return (a*d-b*c)%q

def mul(A,B,q):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)

def sub(A,B,q):
    return tuple((x-y)%q for x,y in zip(A,B))

def is_nilpotent(A,q):
    return mul(A,A,q)==(0,0,0,0)

def eigenline_count(A,q):
    a,b,c,d=A
    lines=[(1,t) for t in range(q)]+[(0,1)]
    total=0
    for x,y in lines:
        u=(a*x+b*y)%q
        v=(c*x+d*y)%q
        if (x*v-y*u)%q==0:
            total+=1
    return total

def predicted(A,q):
    e=eigenline_count(A,q)
    if det(A,q)!=0:
        return q*q-q-1+e
    return q*q-1-(q-1)*e

def run(q):
    matrices=list(product(range(q),repeat=4))
    nils=[A for A in matrices if is_nilpotent(A,q)]
    assert len(nils)==q*q
    total=0
    minimum=None
    type_counts={}
    for A in matrices:
        if A==(0,0,0,0):
            continue
        actual=sum(det(sub(A,N,q),q)!=0 for N in nils)
        expected=predicted(A,q)
        assert actual==expected,(q,A,actual,expected)
        e=eigenline_count(A,q)
        key=(det(A,q)!=0,e,actual)
        type_counts[key]=type_counts.get(key,0)+1
        total+=actual
        minimum=actual if minimum is None else min(minimum,actual)
    gl2=(q*q-1)*(q*q-q)
    assert total==gl2*q*q
    assert minimum==(q-1)*(q-1)
    print(f'q={q}: nilpotents={len(nils)}, minimum={minimum}, total={total}')
    for key in sorted(type_counts):
        print('  type',key,'matrices',type_counts[key])

for q in (2,3,5,7):
    run(q)
print('CHECK_OK')
