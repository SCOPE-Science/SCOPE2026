#!/usr/bin/env python3
"""Independent finite checks for synchronous binary majority on wheel graphs."""
from collections import Counter, defaultdict
from math import comb


def wheel_step(state, n):
    hub=(state>>n)&1
    rim=[(state>>i)&1 for i in range(n)]
    a=sum(rim)
    new_hub=(1 if 2*a>n else 0 if 2*a<n else hub)
    new_rim=[int(rim[(i-1)%n]+rim[(i+1)%n]+hub>=2) for i in range(n)]
    return (new_hub<<n) | sum(bit<<i for i,bit in enumerate(new_rim))


def cyclic_polynomial_formula(m):
    p=Counter({(0,0):1,(m,m):1})
    for a in range(2,m):
        for q in range(1,min(a//2,m-a)+1):
            numerator=m*comb(a-q-1,q-1)*comb(m-a-1,q-1)
            assert numerator%q==0
            p[(a,a-q)]+=numerator//q
    return p


def cyclic_polynomial_direct(m):
    p=Counter()
    for w in range(1<<m):
        bits=[(w>>i)&1 for i in range(m)]
        if any(bits[i] and not(bits[(i-1)%m] or bits[(i+1)%m]) for i in range(m)):
            continue
        a=sum(bits)
        b=sum(bits[i] and bits[(i+1)%m] for i in range(m))
        p[(a,b)]+=1
    return p



def matrix_trace_polynomial(m):
    # Entry polynomials are dictionaries from (u-degree, v-degree) to coefficients.
    def add(a,b):
        c=Counter(a)
        c.update(b)
        return +c
    def mul(a,b):
        c=Counter()
        for (i,j),x in a.items():
            for (k,l),y in b.items():
                c[(i+k,j+l)]+=x*y
        return c
    base=[
        [{(0,0):1},{(1,0):1},{}],
        [{},{},{(1,1):1}],
        [{(0,0):1},{},{(1,1):1}],
    ]
    mat=[[{(0,0):int(i==j)} if i==j else {} for j in range(3)] for i in range(3)]
    for _ in range(m):
        mat=[[sum_poly(mul(mat[i][k],base[k][j]) for k in range(3))
              for j in range(3)] for i in range(3)]
    return sum_poly(mat[i][i] for i in range(3))


def sum_poly(parts):
    out=Counter()
    for item in parts:
        out.update(item)
    return +out

def predicted(n):
    m=n if n%2 else n//2
    p=cyclic_polynomial_formula(m)
    if n%2==0:
        pp=Counter()
        for (a,b),x in p.items():
            for (c,d),y in p.items():
                pp[(a+c,b+d)]+=x*y
        p=pp
    flipping=sum(num for (a,b),num in p.items() if 2*a>n and 2*b<n)
    return (2 if n%2==0 else 0)+flipping, flipping


def brute(n):
    fixed=0
    fixed_hub_two=0
    flipping_hub_two=0
    for state in range(1<<(n+1)):
        b=wheel_step(state,n)
        c=wheel_step(b,n)
        if c != state: continue
        if b==state:
            fixed+=1
        elif ((b>>n)&1)==((state>>n)&1):
            fixed_hub_two+=1
        else:
            flipping_hub_two+=1
    assert fixed_hub_two%2==0 and flipping_hub_two%2==0
    return (fixed, fixed_hub_two//2, flipping_hub_two//2)


def main():
    for m in range(2,13):
        a=cyclic_polynomial_formula(m)
        b=cyclic_polynomial_direct(m)
        assert a==b, ('cyclic-run polynomial',m,a,b)
    for m in range(2,11):
        assert matrix_trace_polynomial(m)==cyclic_polynomial_formula(m)
    print('Checked run polynomial directly at lengths 2 through 12 and 3-state transfer traces at lengths 2 through 10.')
    sum_examined=0
    print('n fixed orbits_with_constant_hub orbits_with_flipping_hub total_orbits')
    for n in range(3,17):
        f, const, flip=brute(n)
        pred, pred_flip=predicted(n)
        assert f==2 and const==(2 if n%2==0 else 0)
        assert flip==pred_flip and const+flip==pred, (n,flip,pred_flip)
        sum_examined += 1<<(n+1)
        print(n,f,const,flip,pred)
    print(f'Checked {sum_examined} wheel configurations and all their two-step periodicity tests.')
    print('WHEEL_MAJORITY_ORBITS_VERIFY_OK')

if __name__=='__main__':
    main()
