"""Exact finite checks of the dihedral-cover branch-cycle and crossing-orbit theorem.
Runs with Python 3, no nonstandard dependencies. Finite cases supplement the proof.
"""
from collections import Counter

def mul(x,y,n):
    a,b=x; c,d=y
    return ((a+(-1 if b else 1)*c)%n,(b+d)%2)

def inv(x,n):
    a,b=x
    return ((-a if b==0 else a)%n,b)

def orbits(perms, elements):
    remaining=set(elements); answer=[]
    while remaining:
        start=next(iter(remaining)); remaining.remove(start)
        todo=[start]; orbit={start}
        for x in todo:
            for f in perms:
                y=f(x)
                if y not in orbit:
                    orbit.add(y);remaining.remove(y);todo.append(y)
        answer.append(orbit)
    return answer

def check(n):
    assert n%2==1 and n>=5
    el=[(a,b) for b in range(2) for a in range(n)]
    e=(0,0); r=(1,0); s=(0,1)
    alpha=lambda x: ((2*x[0])%n,x[1])
    assert all(alpha(mul(a,b,n))==mul(alpha(a),alpha(b),n) for a in el for b in el)
    assert len({alpha(a) for a in el})==2*n
    # Inertia in the first/second factors, in H/G identified with D_n.
    first_r=lambda t:mul(t,inv(alpha(r),n),n)
    first_s=lambda t:mul(t,inv(alpha(s),n),n)
    second_r=lambda t:mul(r,t,n)
    second_s=lambda t:mul(s,t,n)
    cy=lambda f:Counter(len(o) for o in orbits([f],el))
    assert cy(first_s)==Counter({2:n})
    assert cy(second_s)==Counter({2:n})
    assert cy(first_r)==Counter({n:2})
    assert cy(second_r)==Counter({n:2})
    assert Counter(map(len,orbits([first_s,second_s],el)))==Counter({2:1,4:(n-1)//2})
    assert Counter(map(len,orbits([first_s,second_r],el)))==Counter({2*n:1})
    assert Counter(map(len,orbits([first_r,second_s],el)))==Counter({2*n:1})
    assert Counter(map(len,orbits([first_r,second_r],el)))==Counter({n:2})
    # H/G permutation kernel: test explicit left-right formula (a,b): t -> b t alpha(a)^-1.
    images=set()
    for a in el:
        for b in el:
            images.add(tuple(el.index(mul(mul(b,t,n),inv(alpha(a),n),n)) for t in el))
    assert len(images)==4*n*n
    return n,len(images)

if __name__=='__main__':
    for n in (5,7,9,11,13):
        print('n=%s, full monodromy order=%s'%(check(n)))
    print('VERIFY_OK')
