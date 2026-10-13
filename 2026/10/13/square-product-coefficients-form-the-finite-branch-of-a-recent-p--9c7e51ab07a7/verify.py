from math import isqrt


def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:
                out.append(n//d)
    return sorted(out)


def diff_square_solutions(N):
    # All integer (w,v) with w^2-v^2=N, N>0, by signed factor pairs.
    sol=set()
    for r0 in divisors(N):
        for r in (r0,-r0):
            s=N//r
            if (r-s)%2==0:
                w=(r+s)//2
                v=(s-r)//2
                sol.add((w,v))
    return sol


def brute_diff(N):
    # Factorization implies |w| <= (N+1)//2 for N>0; N+1 is a safe exhaustive bound.
    B=N+1
    return {(w,v) for w in range(-B,B+1) for v in range(-B,B+1) if w*w-v*v==N}

for N in range(1,501):
    assert diff_square_solutions(N)==brute_diff(N), N

# Source-boundary witness: a=b=1,c=3,n=1,d=2 gives N=3.
s3=diff_square_solutions(3)
assert s3=={(2,1),(2,-1),(-2,1),(-2,-1)}
assert 1*4*4 == 1*(5**2-3**2)


def is_nth_power_int(X,n):
    # Return all integer x with x^n=X for small exact verification cases.
    if n%2==0 and X<0:
        return []
    sign=-1 if X<0 else 1
    A=abs(X)
    lo,hi=0,A+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**n<=A: lo=mid
        else: hi=mid
    if lo**n!=A:
        return []
    if n%2:
        return [sign*lo]
    if lo==0:
        return [0]
    return [-lo,lo]


def classified(a,b,c,n):
    S=isqrt(a*b)
    assert S*S==a*b
    C=c**(2*n)
    ans=set()
    for r0 in divisors(C):
        for r in (r0,-r0):
            s=C//r
            if (r-s)%2: continue
            X=(r+s)//2
            z=(s-r)//2
            if (S*z)%a: continue
            y=S*z//a
            for x in is_nth_power_int(X,n):
                ans.add((x,y))
    return ans


def brute_original(a,b,c,n):
    # Any classified factor pair has |x^n| <= (c^(2n)+1)/2.
    C=c**(2*n)
    xmax=C+1
    ans=set()
    for x in range(-xmax,xmax+1):
        rhs=b*(x**(2*n)-c**(2*n))
        if rhs<0 or rhs%a: continue
        y2=rhs//a
        y=isqrt(y2)
        if y*y==y2:
            ans.add((x,y)); ans.add((x,-y))
    return ans

cases=0
for a in range(1,9):
    for b in range(1,9):
        S=isqrt(a*b)
        if S*S!=a*b: continue
        for c in range(1,5):
            for n in (1,2):
                A=classified(a,b,c,n)
                B=brute_original(a,b,c,n)
                assert A==B,(a,b,c,n,A,B)
                cases+=1

print(f"VERIFY_OK diff_square_N=500 square_ab_cases={cases} witness_aux_solutions={len(s3)} witness=(a,b,c,n,x,y)=(1,1,3,1,5,4)")
