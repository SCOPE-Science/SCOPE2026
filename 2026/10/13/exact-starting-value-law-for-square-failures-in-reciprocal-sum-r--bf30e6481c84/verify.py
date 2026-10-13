from math import gcd
from collections import Counter


def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d; a+=1
            out.append((d,a))
        d += 1 if d==2 else 2
    if n>1: out.append((n,1))
    return out


def T_projective(P,p):
    # P=None is infinity; affine t is represented by integer 0..p-1.
    if P is None:
        return None
    if P==0:
        return None
    return (P + pow(P,-1,p)) % p


def hit_sets(p):
    d={}
    for t in range(1,p):
        x=t
        seen=set()
        for n in range(1,2*p+3):
            x=T_projective(x,p)
            if x==0:
                d.setdefault(n,set()).add(t)
                break
            if x is None or x in seen:
                break
            seen.add(x)
    return d


def local_state(h,p,a,x):
    H=h//(p**a)
    mod=p**(a+1)
    r=x%mod
    # valuation exactly a is necessary.
    if r%(p**a)!=0 or r%(p**(a+1))==0:
        return None
    y=(r//(p**a))%p
    t=(y*pow(H,-1,p))%p
    for n,B in hit_sets(p).items():
        if t in B:
            return n
    return None


def predicted_failures(h,x):
    times=[]
    for p,a in factor(h):
        if p==2 or p%4==1:
            s=local_state(h,p,a,x)
            if s is not None:
                times.append(s+1)
    return sorted(set(times))


def actual_failures(h,x):
    # t_0 = u_0/v_0 in lowest terms.
    g=gcd(h,x)
    u=x//g
    v=h//g
    relevant=[p for p,a in factor(h) if p==2 or p%4==1]
    max_depth=max([max(hit_sets(p), default=0) for p in relevant], default=0)
    failures=[]
    for n in range(1,max_depth+1):
        u,v=u*u+v*v,u*v
        assert gcd(u,v)==1
        if gcd(h,u)>1:
            failures.append(n+1)
    return failures


def modulus(h):
    M=1
    for p,a in factor(h):
        if p==2 or p%4==1:
            M*=p**(a+1)
    return M

# Exhaustive theorem check for all h <= 60 over one full predicted period.
checked=0
for h in range(1,61):
    M=modulus(h)
    for r in range(M):
        x = r if r else M
        a=actual_failures(h,x)
        b=predicted_failures(h,x)
        assert a==b, (h,r,a,b)
        checked += 1

# Exact example h=65.
h=65
M=modulus(h)
cnt=Counter()
for r in range(M):
    x=r if r else M
    fs=actual_failures(h,x)
    assert fs==predicted_failures(h,x)
    cnt[len(fs)] += 1
assert M==4225
assert cnt==Counter({0:3507,1:714,2:4}),cnt

B5={n:sorted(v) for n,v in hit_sets(5).items()}
B13={n:sorted(v) for n,v in hit_sets(13).items()}
assert B5=={1:[2,3],2:[1,4]},B5
assert B13=={1:[5,8]},B13

print(f"VERIFY_OK exhaustive_h_le_60_states={checked} h65_counts=3507,714,4 modulus={M} B5={B5} B13={B13}")
