from math import isqrt

def in_semigroup(n,a,b):
    if n < 0:
        return False
    # exact finite test
    for i in range(n//a + 1):
        if (n - i*a) % b == 0:
            return True
    return False

def fletcher_qs(r,a,b):
    D=r+a+b
    # coordinate identities: r distinct unit variables, plus A,B
    W=[1]*r+[a,b]
    A=r; B=r+1
    # I={A}
    okA=any(D-W[e] >= 0 and (D-W[e])%a==0 for e in range(r+2))
    if not okA: return False
    # I={B}
    okB=any(D-W[e] >= 0 and (D-W[e])%b==0 for e in range(r+2))
    if not okB: return False
    # I={A,B}: injection e on two elements; remaining degree must lie in <a,b>
    okAB=False
    for eA in range(r+2):
        if not in_semigroup(D-W[eA],a,b):
            continue
        for eB in range(r+2):
            if eB==eA: continue
            if in_semigroup(D-W[eB],a,b):
                okAB=True; break
        if okAB: break
    return okAB

def divcrit(r,a,b):
    d=b-a
    return ((r%a==0) or ((r+d)%a==0) or ((r+d-1)%a==0)) and \
           ((r%b==0) or ((r-d)%b==0) or ((r-d-1)%b==0))

def chart_canonical(m,q,r):
    if m<=1: return True
    q%=m
    for k in range(1,m):
        if r*k + ((k*q)%m) < m:
            return False
    return True

def canonical_bruteforce(r,a,b):
    return chart_canonical(a,b,r) and chart_canonical(b,a,r)

def canonical_formula(r,a,b):
    d=b-a
    return 0<=d<=r and a<=r+d

def tau(n):
    s=0
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            s += 1 if d*d==n else 2
    return s

# 1. Fletcher criterion vs closed divisibility criterion, including noncanonical boxes.
for r in range(2,31):
    for a in range(1,3*r+1):
        for b in range(a,3*r+1):
            x=fletcher_qs(r,a,b)
            y=divcrit(r,a,b)
            assert x==y,("QS_MISMATCH",r,a,b,x,y)
print("DIVISIBILITY_EQUIVALENCE_OK full boxes r<=30, 1<=a<=b<=3r")

# 2. Independent local Reid-Tai replay of the canonical strip formula.
for r in range(2,61):
    for a in range(1,4*r+1):
        for b in range(a,4*r+1):
            x=canonical_bruteforce(r,a,b)
            y=canonical_formula(r,a,b)
            assert x==y,("CANON_MISMATCH",r,a,b,x,y)
print("CANONICAL_STRIP_OK full boxes r<=60, 1<=a<=b<=4r")

# 3. Exact counts and asserted upper bound on the canonical strip.
for r in range(2,201):
    Q=0; total=0
    for d in range(0,r+1):
        for a in range(1,r+d+1):
            b=a+d
            total += 1
            Q += int(divcrit(r,a,b))
    assert total==3*r*(r+1)//2
    U=(r+1)*tau(r) + sum(tau(n) for n in range(r,2*r+1)) + sum(tau(n) for n in range(r-1,2*r))
    assert Q<=U,("BOUND_FAIL",r,Q,U)
print("CANONICAL_COUNT_BOUND_OK r<=200")
for r in [2,3,4,5,10,20,50,100,200]:
    Q=sum(divcrit(r,a,a+d) for d in range(r+1) for a in range(1,r+d+1))
    print(f"r={r} Q={Q} total={3*r*(r+1)//2}")
print("VERIFY_OK")
