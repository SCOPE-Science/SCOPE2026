#!/usr/bin/env python3
"""Standalone reproducibility checks for edgewise linear-spline projection constants."""
from decimal import Decimal, localcontext
from fractions import Fraction

checks = 0

def ensure(condition, note):
    global checks
    if not condition:
        raise AssertionError(note)
    checks += 1

def tree_parameters(d):
    with localcontext() as context:
        context.prec = 70
        x = Decimal(d)
        q = Decimal(1)/(x+(x*x-x+1).sqrt())
        lam = 3*(1+q*q)/(1+q)**2
        return q,lam

def area(a,b):
    """Exact integral of |(1-t)a+tb| on [0,1]."""
    if a*b >= 0:
        return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))

def invert(a):
    n=len(a)
    aug=[[Fraction(a[i][j]) for j in range(n)]+[Fraction(i==j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if aug[i][col])
        aug[col],aug[pivot]=aug[pivot],aug[col]
        p=aug[col][col]
        aug[col]=[x/p for x in aug[col]]
        for i in range(n):
            if i==col:continue
            f=aug[i][col]
            if f:aug[i]=[aug[i][k]-f*aug[col][k] for k in range(2*n)]
    return [row[n:] for row in aug]

def finite_norm(n,edges):
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    A=[[int((i,j) in edges or (j,i) in edges) for j in range(n)] for i in range(n)]
    B=[[2*deg[i]*(i==j)+A[i][j] for j in range(n)] for i in range(n)]
    inv=invert(B)
    for i in range(n):
        for j in range(n):
            ensure(sum(Fraction(B[i][k])*inv[k][j] for k in range(n)) == int(i==j),f'matrix inverse {n},{i},{j}')
    rows=[]
    for v in range(n):
        z=[6*inv[v][u] for u in range(n)]
        rows.append(sum((area(z[u],z[w]) for u,w in edges),Fraction(0)))
        ensure(rows[-1]>=1, f'projection norm at vertex {v}')
        ensure(rows[-1]<3, f'universal finite bound {v}')
    return max(rows)

def cycle(n): return [(i,(i+1)%n) for i in range(n)]
def complete(n): return [(i,j) for i in range(n) for j in range(i+1,n)]
def cube(): return [(i,i^(1<<b)) for i in range(8) for b in range(3) if i < (i^(1<<b))]
def bipartite(a,b): return [(i,a+j) for i in range(a) for j in range(b)]
def petersen():return cycle(5)+[(i,i+5) for i in range(5)]+[(i+5,((i+2)%5)+5) for i in range(5)]

def truncated_norm_cycle(n,k):
    edges=cycle(n)
    d=2
    walk=[Fraction(int(i==0)) for i in range(n)]
    coeff=[Fraction(0) for _ in range(n)]
    for depth in range(k+1):
        for i in range(n):coeff[i] += Fraction(3,d)*Fraction((-1)**depth,(2*d)**depth)*walk[i]
        walk=[walk[(i-1)%n]+walk[(i+1)%n] for i in range(n)]
    return sum((area(coeff[i],coeff[j]) for i,j in edges),Fraction(0))

def truncated_norm_line(k):
    r=k+2
    walk={0:Fraction(1)}
    coeff={i:Fraction(0) for i in range(-r,r+1)}
    for depth in range(k+1):
        for i,val in walk.items():coeff[i] += Fraction(3,2)*Fraction((-1)**depth,4**depth)*val
        walk={i:walk.get(i-1,0)+walk.get(i+1,0) for i in range(-r,r+1)}
    return sum((area(coeff[i],coeff[i+1]) for i in range(-r,r)),Fraction(0))

def main():
    prev=None
    with localcontext() as context:
        context.prec=70
        for d in range(2,40):
            q,lam=tree_parameters(d)
            ensure(Decimal(0)<q<1/Decimal(d-1),'summability')
            ensure(abs((d-1)*q*q-2*d*q+1)<Decimal('1e-60'),'Green recurrence')
            ensure(abs(1-(d-1)*q-(1+q)/(2-q))<Decimal('1e-60'),'geometric simplification')
            # Independent edge-shell absolute integration and summation.
            local=(1+q*q)/(2*(1+q))
            c=Decimal(6)/(Decimal(d)*(2-q))
            formula=c*d*local/(1-(d-1)*q)
            ensure(abs(formula-lam)<Decimal('1e-60'),'closed-form agreement')
            ensure(Decimal(1)<lam<3,'norm range')
            if prev is not None:ensure(lam>prev,'strict increase in degree')
            prev=lam
            for R in (3,9,25):
                total=Decimal(0)
                for s in range(R):total += c*d*((d-1)*q)**s*local
                error=lam-total
                tail=c*d*local*((d-1)*q)**R/(1-(d-1)*q)
                ensure(error>=0 and abs(error-tail)<Decimal('1e-60'),'exact shell tail')
        ensure(abs(tree_parameters(2)[1]-2)<Decimal('1e-60'),'line constant 2')
        for d in (100,500,1000,10000):
            q,lam=tree_parameters(d)
            ensure(abs(Decimal(d)*(3-lam)-3)<Decimal('0.1'),'3-3/d asymptotic')
    families=[(n,cycle(n)) for n in range(3,14)]+[(4,complete(4)),(6,bipartite(3,3)),(8,cube()),(10,petersen())]
    for n,edges in families:
        norm=finite_norm(n,edges)
        ensure(norm<3,f'finite {n} bound')
        if n>=9 and edges==cycle(n):
            ensure(abs(Decimal(norm.numerator)/Decimal(norm.denominator)-tree_parameters(2)[1])<Decimal('0.05'),'cycle approximates line')
    for k in range(5):
        line=truncated_norm_line(k)
        for n in range(2*k+6,2*k+10):
            ensure(truncated_norm_cycle(n,k)==line,'local high-girth equality')
    print('PASS',checks,'exact arithmetic/independent shell checks')

if __name__=='__main__':main()
