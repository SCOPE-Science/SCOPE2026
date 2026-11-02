"""Standalone exact checks for star-graph coalescence-time identities.

No external packages. The direct subset-state Markov generator checks are
independent of the particle-count geometric-stage derivation.
"""
from fractions import Fraction
from math import factorial, gamma, log, pi


def solve(matrix, rhs):
    """Exact rational Gaussian elimination."""
    n=len(rhs)
    a=[list(matrix[i])+[rhs[i]] for i in range(n)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        d=a[col][col]
        a[col]=[x/d for x in a[col]]
        for i in range(n):
            if i!=col and a[i][col]:
                factor=a[i][col]
                a[i]=[a[i][j]-factor*a[col][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]


def generator_transitions(n, mask):
    """Transitions of individual occupied particle clocks on labeled star."""
    jumps={}
    for v in range(n+1):
        if not (mask >> v)&1:
            continue
        for dest,rate in ([(i,Fraction(1,n)) for i in range(1,n+1)] if v==0 else [(0,Fraction(1))]):
            successor=(mask & ~(1<<v)) | (1<<dest)
            jumps[successor]=jumps.get(successor,Fraction(0))+rate
    assert sum(jumps.values())==mask.bit_count()
    return jumps


def direct_value(n,s=None):
    """Solve all subset-state first-step equations, by increasing occupancy."""
    vals={1<<v:(Fraction(1) if s is not None else Fraction(0)) for v in range(n+1)}
    for r in range(2,n+2):
        states=[m for m in range(1,1<<(n+1)) if m.bit_count()==r]
        indices={m:i for i,m in enumerate(states)}
        mat=[[Fraction(0) for _ in states] for _ in states]
        rhs=[Fraction(0) for _ in states]
        for i,mask in enumerate(states):
            mat[i][i]=r+(s or 0)
            if s is None: rhs[i]=1
            for dest,rate in generator_transitions(n,mask).items():
                if dest in indices:
                    mat[i][indices[dest]]-=rate
                else:
                    rhs[i]+=rate*vals[dest]
        results=solve(mat,rhs)
        vals.update(dict(zip(states,results)))
    return vals[(1<<(n+1))-1]


def product(n,s):
    ans=Fraction(n+1,n+1+s)
    for r in range(2,n+1):
        ans *= Fraction((r-1)*((n+1)*r+n*s),n*(r+s)**2-r*(n-r+1))
    return ans


def expected(n):
    H=sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))
    return H+1-(H+2)/Fraction(n+1)


def variance(n):
    v=Fraction(0)
    b=Fraction(1,n+1)
    for r in range(2,n+2):
        q=Fraction(n-r+1,n*r)
        v+=(1+4*q-q*q)/(r*r*(1-q)**2)
        if r<=n:
            v+=(2*b-b*b)/r**2
    return v


def direct_second_moment(n):
    """Independent Markov-state recursion L m1=-1, L m2=-2m1."""
    means={1<<v:Fraction(0) for v in range(n+1)}
    seconds={1<<v:Fraction(0) for v in range(n+1)}
    for r in range(2,n+2):
        states=[m for m in range(1,1<<(n+1)) if m.bit_count()==r]
        indices={m:i for i,m in enumerate(states)}
        mat=[[Fraction(0) for _ in states] for _ in states]
        rhs1=[Fraction(1) for _ in states]
        for i,mask in enumerate(states):
            mat[i][i]=r
            for dest,rate in generator_transitions(n,mask).items():
                if dest in indices: mat[i][indices[dest]]-=rate
                else: rhs1[i]+=rate*means[dest]
        found1=solve(mat,rhs1)
        for st,m in zip(states,found1):means[st]=m
        rhs2=[2*means[st] for st in states]
        for i,mask in enumerate(states):
            for dest,rate in generator_transitions(n,mask).items():
                if dest not in indices:rhs2[i]+=rate*seconds[dest]
        found2=solve(mat,rhs2)
        for st,m in zip(states,found2):seconds[st]=m
    full=(1<<(n+1))-1
    return seconds[full]-means[full]**2


def finite_stage_mean(n):
    result=Fraction(0)
    for r in range(2,n+2):
        q=Fraction(n-r+1,n*r)
        result+=(1+q)/(r*(1-q))
        if r<=n: result+=Fraction(1,(n+1)*r)
    return result


def variance_float(n):
    b=1/(n+1)
    return sum((1+4*q-q*q)/(r*r*(1-q)**2)+(2*b-b*b)/r**2 * (r<=n) for r in range(2,n+2) for q in [(n-r+1)/(n*r)])

def limiting_variance_moment(N):
    return sum(( (r*r+4*r-1)/(r*r*(r-1)**2) for r in range(2,N+2)))


if __name__=='__main__':
    assertions=0
    for n in range(1,7):
        m=direct_value(n)
        assert m==expected(n)==finite_stage_mean(n), (n,m,expected(n)); assertions+=2
        for s in (Fraction(1),Fraction(2),Fraction(1,2)):
            got=direct_value(n,s)
            exp=product(n,s)
            assert got==exp,(n,s,got,exp)
            assert Fraction(0)<got<Fraction(1)
            assertions+=2
    for n in range(1,6):
        dv=direct_second_moment(n)
        var=variance(n)
        assert dv==var,(n,dv,var)
        assert var>0
        assertions+=2
    for n in range(1,201):
        assert expected(n)>0
        assert variance(n)>0
        assertions+=2
    limit=pi*pi/2-1
    for n in (200,1000,3000,10000):
        vn=variance_float(n)
        assert abs(vn-limit)<15/(n+1), (n,vn,limit)
        assertions+=1
    for n in (50,100,1000,10000):
        mu=float(expected(n))
        assert abs((mu-log(n))-(0.5772156649015328606+1))<8*log(n)/n
        assertions+=1
    assert abs((pi*pi/2-1)-pi*pi/6)>1
    assertions+=1
    print('PASS',assertions,'exact-state and numerical assertions')
    print('means n=2,3,10:', [float(expected(n)) for n in (2,3,10)])
    print('limiting variance:',limit)
