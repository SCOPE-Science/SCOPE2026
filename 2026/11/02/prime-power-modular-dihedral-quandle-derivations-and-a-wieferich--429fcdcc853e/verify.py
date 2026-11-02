"""Independent finite-field checks for prime-power dihedral-quandle derivations.

Run: python3 verify.py. Only Python's standard library is required.
This is a finite verification, not a replacement for the unrestricted proof.
"""
from itertools import product
from math import lcm


def direct_derivation_nullity(n, p):
    """Row-reduce all n^3 independent Leibniz coefficient equations."""
    assert n % 2 and n % p == 0
    inverse_two = pow(2, -1, n)
    pivots = {}
    for i in range(n):
        for j in range(n):
            target = (2*j-i) % n
            for k in range(n):
                equation = {}
                # Coefficient of e_k in D(e_i*e_j) - D(e_i)*e_j - e_i*D(e_j).
                entries = ((target*n+k, 1),
                           (i*n+(2*j-k)%n, -1),
                           (j*n+((k+i)*inverse_two)%n, -1))
                for pos, val in entries:
                    updated = (equation.get(pos, 0) + val) % p
                    if updated:
                        equation[pos] = updated
                    else:
                        equation.pop(pos, None)
                while equation:
                    head = min(equation)
                    if head not in pivots:
                        scale = pow(equation[head], -1, p)
                        pivots[head] = {k: v*scale % p for k,v in equation.items()}
                        break
                    scalar = equation[head]
                    for col, value in pivots[head].items():
                        updated = (equation.get(col, 0) - scalar*value) % p
                        if updated:
                            equation[col] = updated
                        else:
                            equation.pop(col, None)
    return n*n-len(pivots)


def orbit_basis(n,p):
    """Construct signed doubling eigenvectors independently by finite permutation orbits."""
    inv2 = pow(2,-1,p)
    seen = {0}
    basis = []
    for seed in range(1,n):
        if seed in seen:
            continue
        coeff = {seed:1}
        todo = [seed]
        while todo:
            r = todo.pop()
            for nr,nc in (((2*r)%n, coeff[r]*inv2%p),
                          ((-r)%n, -coeff[r]%p)):
                if nr in coeff:
                    assert coeff[nr] == nc, (n,p,seed,r,nr)
                else:
                    coeff[nr] = nc
                    todo.append(nr)
        seen.update(coeff)
        vector = [0]*n
        for idx,value in coeff.items():
            vector[idx]=value
        basis.append(vector)
    return basis


def arithmetic_expected(p,a):
    h=1
    while pow(2,h,p)!=1:
        h+=1
    L=lcm(2,h)
    s=1
    while pow(2,h,p**(s+1)) == 1:
        s+=1
    m=(p-1)//L
    return 2*m*sum(p**min(j-1,s-1) for j in range(1,a+1)),(h,L,s,m)


def apply_D(u,v,x,p):
    n=len(u)
    out=[0]*n
    for i,c in enumerate(x):
        if not c: continue
        for r in range(n):
            out[(i+r)%n] = (out[(i+r)%n] + c*(u[r]+i*v[r]))%p
    return out


def convolution(x,y,p):
    n=len(x)
    out=[0]*n
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b:out[(i+j)%n] = (out[(i+j)%n]+a*b)%p
    return out


def test_closed_normal_form(p,a):
    n=p**a
    basis=orbit_basis(n,p)
    expected,details=arithmetic_expected(p,a)
    assert 2*len(basis)==expected
    for k,vec in enumerate(basis):
        assert all(vec[(-i)%n]==-vec[i]%p and vec[(2*i)%n]==(vec[i]*pow(2,-1,p))%p for i in range(n)),(n,k)
    zero=[0]*n
    for b in basis[:min(3,len(basis))]:
        for u,v in [(b,zero),(zero,b),(b,b)]:
            images=[apply_D(u,v,[int(j==i) for j in range(n)],p) for i in range(n)]
            for i,j in product(range(n), repeat=2):
                target=(2*j-i)%n
                lhs=images[target]
                rhs=[0]*n
                for r,coeff in enumerate(images[i]):
                    rhs[(2*j-r)%n]=(rhs[(2*j-r)%n]+coeff)%p
                for r,coeff in enumerate(images[j]):
                    rhs[(2*r-i)%n]=(rhs[(2*r-i)%n]+coeff)%p
                assert lhs==rhs,(n,p,i,j)
    if len(basis)>1:
        u=basis[0];v=basis[1];w=basis[-1];z=basis[0]
        d=lambda t:[(i*c)%p for i,c in enumerate(t)]
        uout=[(a-b)%p for a,b in zip(convolution(v,d(w),p),convolution(z,d(u),p))]
        vout=[(a-b)%p for a,b in zip(convolution(v,d(z),p),convolution(z,d(v),p))]
        for i in range(n):
            ei=[int(j==i) for j in range(n)]
            left=apply_D(u,v,apply_D(w,z,ei,p),p)
            right=apply_D(w,z,apply_D(u,v,ei,p),p)
            observed=[(x-y)%p for x,y in zip(left,right)]
            assert observed==apply_D(uout,vout,ei,p),(n,i)
    return len(basis),details


def main():
    cases=[(3,2),(3,3),(5,2)]
    for p,a in cases:
        n=p**a
        orbit_dim,details=test_closed_normal_form(p,a)
        nullity=direct_derivation_nullity(n,p)
        assert nullity==2*orbit_dim==arithmetic_expected(p,a)[0],(n,nullity,orbit_dim)
        print(f'PASS: n={n}, characteristic={p}, {n**3} direct equations; derivation dimension={nullity}; eigenspace dimension={orbit_dim}; order data={details}')
    p=7;a=2
    orb,details=test_closed_normal_form(p,a)
    assert 2*orb==arithmetic_expected(p,a)[0]
    print(f'PASS: n=49, characteristic=7, explicit normal-form checks; dimension={2*orb}')
    p=1093
    d,details=arithmetic_expected(p,2)
    assert details==(364,364,2,3) and d==6564
    print(f'PASS: arithmetic exceptional case p=1093, exponent=2, predicted dimension={d}')
    print('VERIFY_OK: independent constraint ranks, explicit Leibniz identities, Lie brackets, and arithmetic checks')

if __name__=='__main__':
    main()
