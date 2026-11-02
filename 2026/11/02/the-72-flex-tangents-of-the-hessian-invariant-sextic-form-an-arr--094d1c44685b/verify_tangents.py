#!/usr/bin/env python3
"""Exact incidence certificate for 72 inflection tangents of Maschke's sextic.

All incidence equalities are proved over Z[omega,r], with omega^2+omega+1=0.
Reduction at (omega,r)=(14,29) modulo 211 is only used to EXCLUDE
additional coincidences: an exact equality must survive good reduction.
"""
from collections import defaultdict, Counter, deque
from math import gcd
from functools import reduce
P = 211
W = 14
R = 29
assert (W*W+W+1)%P == 0
assert (R**6 - 10*R**3 + 1)%P == 0

# a+b*omega in Z[omega].
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b):
    A,B=a; C,D=b
    return (A*C-B*D, A*D+B*C-B*D)
zero=(0,0); one=(1,0); omega=(0,1); omega2=(-1,-1)
# a+b*r with coefficients in Z[omega], r sextic.
def ladd(a,b): return (add(a[0],b[0]),add(a[1],b[1]))
def lmul(a,b):
    v=[zero]*3
    v[0]=mul(a[0],b[0]);v[1]=add(mul(a[0],b[1]),mul(a[1],b[0]));v[2]=mul(a[1],b[1]);return v

def dot2(M,v):
    return tuple((sumprod(M[i],v,0),sumprod(M[i],v,1)) for i in range(3))
def sumprod(row,v,k):
    ans=zero
    for j in range(3): ans=add(ans,mul(row[j],v[j][k]))
    return ans

def reduct(v):
    coef=[abs(z) for pair in v for w in pair for z in w]
    q=reduce(gcd,coef)
    assert q>0
    return tuple(tuple(tuple(z//q for z in w) for w in pair) for pair in v)
def evaluate(v):
    return tuple((a[0]+a[1]*W + R*(b[0]+b[1]*W))%P for a,b in v)
def normalize(v):
    assert any(t%P for t in v)
    s=pow(next(t%P for t in v if t%P),P-2,P)
    return tuple(t*s%P for t in v)
def cross(a,b):
    return normalize((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))

def pmul(a,b):
    # degree ≤ 3 polynomial in r with Z[omega] coefficients.
    out=[zero]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]=add(out[i+j],mul(v,w))
    return out
def padd(a,b):
    n=max(len(a),len(b));return [add(a[i] if i<len(a) else zero,b[i] if i<len(b) else zero) for i in range(n)]
def pneg(a):return [neg(t) for t in a]
def det(a,b,c):
    def f(i,j,k):return pmul(pmul(a[i],b[j]),c[k])
    out=[zero]*4
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:out=padd(out,f(i,j,k))
    for i,j,k in [(0,2,1),(1,0,2),(2,1,0)]:out=padd(out,pneg(f(i,j,k)))
    return out

def main():
    D=[[[zero,one,zero],[zero,zero,one],[one,zero,zero]],
       [[one,zero,zero],[zero,omega2,zero],[zero,zero,omega]],
       [[one,one,one],[one,omega2,omega],[one,omega,omega2]],
       [[one,zero,zero],[zero,omega2,zero],[zero,zero,omega2]]]
    z=(zero,zero)
    initial=((zero,zero),(zero,(-1,0)),(one,zero))
    lines=[initial]
    seen={normalize(evaluate(initial)):0}
    todo=deque([0])
    while todo:
        idx=todo.popleft()
        for M in D:
            v=reduct(dot2(M,lines[idx]))
            key=normalize(evaluate(v))
            if key not in seen:
                seen[key]=len(lines);lines.append(v);todo.append(len(lines)-1)
    assert len(lines)==72, len(lines)
    keys=list(seen)
    pairs=defaultdict(set)
    for i in range(72):
        for j in range(i):
            pairs[cross(keys[i],keys[j])].update((i,j))
    profile=Counter(map(len,pairs.values()))
    assert profile==Counter({2:1728,3:216,6:12}),profile
    exact_tests=0
    for inds in pairs.values():
        ids=sorted(inds)
        if len(ids)<=2:continue
        for k in ids[2:]:
            ans=det(lines[ids[0]],lines[ids[1]],lines[k])
            assert all(c==zero for c in ans),(ids[:2],k,ans)
            exact_tests+=1
    assert exact_tests==264,exact_tests
    by_line=[Counter() for _ in range(72)]
    for ids in pairs.values():
        for j in ids: by_line[j][len(ids)]+=1
    assert all(c==Counter({2:48,3:9,6:1}) for c in by_line)
    assert sum(n*(n-1)//2 * count for n,count in profile.items())==2556
    print('MASCHKE_72_TANGENTS_INCIDENCE_OVER_CHARACTERISTIC_ZERO_PASS')
    print('modular_good_reduction=211; root=29; cube_root_unity=14')
    print('line_count=72; exact_concurrency_identities=',exact_tests)
    print('projective_singular_points_profile=',dict(sorted(profile.items())))
    print('total_singular_points=',len(pairs),'total_pair_count=2556')
if __name__=='__main__': main()
