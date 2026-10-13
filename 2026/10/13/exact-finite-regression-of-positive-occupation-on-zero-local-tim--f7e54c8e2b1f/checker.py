from fractions import Fraction
from itertools import product
from math import comb

def a(k):
    return Fraction(comb(2*k,k), 4**k)

def mu(n):
    return (2*n+1)*a(n)-1

def var_z(n):
    m=mu(n)
    return 2*n-3*m-m*m

def stats_path(bits):
    s=0
    z=0
    A=0
    abs_path=[0]
    for b in bits:
        s += 1 if b else -1
        if s==0:
            z+=1
        elif s>0:
            A+=1
        abs_path.append(abs(s))
    return z,A,tuple(abs_path)

def run():
    paths=0
    moment_checks=0
    local_conditional_checks=0
    reflected_fiber_checks=0
    for n in range(1,9):
        N=2**(2*n)
        rows=[]
        by_z={}
        by_abs={}
        for bits in product((0,1), repeat=2*n):
            z,A,r=stats_path(bits)
            rows.append((z,A))
            by_z.setdefault(z,[]).append(A)
            by_abs.setdefault(r,[]).append((z,A))
            paths+=1
        Ez=sum(Fraction(z,N) for z,A in rows)
        Ea=sum(Fraction(A,N) for z,A in rows)
        Ez2=sum(Fraction(z*z,N) for z,A in rows)
        EzA=sum(Fraction(z*A,N) for z,A in rows)
        assert Ez==mu(n)
        assert Ez2-Ez*Ez==var_z(n)
        assert EzA-Ez*Ea == -var_z(n)/2
        moment_checks += 3
        for z,vals in by_z.items():
            assert Fraction(sum(vals),len(vals)) == n-Fraction(z,2)
            local_conditional_checks += 1
        for r,vals in by_abs.items():
            zs={z for z,A in vals}
            assert len(zs)==1
            z=next(iter(zs))
            assert Fraction(sum(A for z,A in vals),len(vals)) == n-Fraction(z,2)
            reflected_fiber_checks += 1

    identity_checks=0
    s=Fraction(1)
    for n in range(1,501):
        s += a(n)
        assert s==(2*n+1)*a(n)
        conv=sum((a(i)*a(n-i) for i in range(n+1)),Fraction(0))
        assert conv==1
        # Independent reconstruction of factorial second moment.
        if n<=120:
            fac=2*sum((a(i)*a(j-i) for j in range(2,n+1) for i in range(1,j)),Fraction(0))
            assert fac==2*n-4*mu(n)
        assert var_z(n)>=0
        identity_checks += 3 if n<=250 else 2

    print("VERIFY_OK")
    print(f"paths_enumerated={paths}")
    print(f"moment_checks={moment_checks}")
    print(f"local_conditional_checks={local_conditional_checks}")
    print(f"reflected_fiber_checks={reflected_fiber_checks}")
    print(f"exact_identity_checks={identity_checks}")
    print("max_exhaustive_half_horizon=8")
    print("max_closed_identity_n=500")

if __name__=="__main__":
    run()
