#!/usr/bin/env python3
"""Independent finite-field irreducibility census for linearly shifted monic cubics."""

def field(p, k=None):
    q = p if k is None else p*p
    def parts(z):
        return (z % p, z // p)
    def plus(x,y):
        if k is None: return (x+y)%p
        a,b=parts(x); c,d=parts(y)
        return (a+c)%p+p*((b+d)%p)
    def minus(x,y):
        if k is None: return (x-y)%p
        a,b=parts(x); c,d=parts(y)
        return (a-c)%p+p*((b-d)%p)
    def prod(x,y):
        if k is None: return (x*y)%p
        a,b=parts(x);c,d=parts(y)
        return (a*c+k*b*d)%p+p*((a*d+b*c)%p)
    return q, plus, minus, prod

def inspect(p,k,shifts):
    q,plus,minus,mul=field(p,k)
    Q=range(q)
    squares=[mul(x,x) for x in Q]
    cubes=[mul(squares[x],x) for x in Q]
    # Independent root-set algorithm: for each quadratic and linear coefficient,
    # mark all possible constant coefficients giving a root in the base field.
    irreducible=[]
    for a in Q:
        row=[]
        for b in Q:
            roots=set()
            for x in Q:
                roots.add(minus(0,plus(cubes[x],plus(mul(a,squares[x]),mul(b,x)))))
            row.append(frozenset(set(Q)-roots))
        irreducible.append(row)
    for u,v in shifts:
        assert u != 0
        direct=0
        for a in Q:
            for b in Q:
                nextb=plus(b,u)
                next_consts=irreducible[a][nextb]
                for c in irreducible[a][b]:
                    if plus(c,v) in next_consts:direct+=1
        formula=((q-2)*(q+1)**2 if q%3==2 else (q+2)*(q-1)**2)//9
        if direct!=formula:
            raise AssertionError((p,k,u,v,direct,formula))
    return len(shifts),q**3

def main():
    trials=[(5,None),(7,None),(11,None),(13,None),(17,None),(19,None),
            (5,2),(7,3)]  # 2 nonsquare mod 5; 3 nonsquare mod 7
    tested=0
    total_polys=0
    for p,k in trials:
        q=p if k is None else p*p
        shifts=[(1,0),(1,1),(2,3)]
        if q<=7:
            shifts=[(u,v) for u in range(1,q) for v in range(q)]
        if k is not None:
            shifts.extend([(p,0),(p+1,p+2)])
        n,t=inspect(p,k,shifts)
        tested+=n;total_polys+=t
        print(f'PASS q={q} shift_cases={n} monic_cubics={t}')
    print(f'VERIFY_OK fields={len(trials)} cases={tested} monic_cubics={total_polys}')

if __name__ == '__main__': main()
