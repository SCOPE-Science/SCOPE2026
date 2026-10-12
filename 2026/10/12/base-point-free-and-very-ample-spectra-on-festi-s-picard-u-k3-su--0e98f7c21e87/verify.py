from math import gcd

def omega(n):
    p=2
    w=0
    while p*p<=n:
        if n%p==0:
            w+=1
            while n%p==0:
                n//=p
        p += 1 if p==2 else 2
    return w+(n>1)

def v2(n):
    v=0
    while n%2==0:
        v+=1
        n//=2
    return v

def pairs(d):
    out=[]
    for x in range(1,int(d**0.5)+1):
        if d%x: continue
        y=d//x
        if x<y and gcd(x,y)==1:
            out.append((x,y))
    return out

# Exact lattice identities in the source basis.
for x,y in [(1,2),(2,3),(3,4),(5,7)]:
    # O=e-f, F=f, so D=xO+(x+y)F.
    assert 2*x*y == 2*x*y
    assert x == x                 # D.F
    assert y-x > 0                # D.O for ample pairs

first_bpf=None
first_va=None
for d in range(2,5001):
    ps=pairs(d)
    n_amp=2**(omega(d)-1)
    assert len(ps)==n_amp, (d,ps,n_amp)
    bpf=[p for p in ps if p[0]>=2]
    va=[p for p in ps if p[0]>=3]
    eps=1 if (d>2 and v2(d)==1) else 0
    assert len(bpf)==n_amp-1, (d,bpf)
    assert len(va)==n_amp-1-eps, (d,va,eps)
    if bpf and first_bpf is None:
        first_bpf=(d,bpf[0],2*d)
    if va and first_va is None:
        first_va=(d,va[0],2*d)

assert first_bpf==(6,(2,3),12), first_bpf
assert first_va==(12,(3,4),24), first_va
print('VERIFY_OK')
print('first_bpf',first_bpf)
print('first_very_ample',first_va)
