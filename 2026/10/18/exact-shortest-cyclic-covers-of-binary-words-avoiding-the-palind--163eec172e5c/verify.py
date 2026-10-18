#!/usr/bin/env python3
"""Independent finite checks of a shortest cyclic cover theorem for 010-avoiding binary words.
Uses only Python standard library. The infinite argument is mathematical, not computational.
"""
from itertools import product
from collections import Counter, defaultdict

def words(m):
    return (''.join(p) for p in product('01', repeat=m))

def required(k):
    return [w for w in words(k) if '010' not in w]

def sources_sinks(k):
    n = k - 1
    ds = [v for v in words(n) if '010' not in v and v.endswith('01') and not v.startswith('10')]
    ss = [v for v in words(n) if '010' not in v and v.startswith('10') and not v.endswith('01')]
    return ds, ss

def routing(v):
    n = len(v)
    j = v.find('10')
    if j < 0:
        assert v == '0'*(n-1)+'1'
        addition = '0'*(n-1)
    else:
        p, s = v[:j], v[j:]
        assert s.startswith('10') and s.endswith('01') and '010' not in s
        a = len(p) - len(p.lstrip('0'))
        b = len(p)-a
        assert b >= 1 and p == '0'*a+'1'*b
        addition = '1'*b+'0'*a
    assert len(addition) == (j if j >= 0 else n-1)
    return addition, (v + addition)[-n:]

def cyclic_windows(cycle, k):
    return {''.join(cycle[(i+t)%len(cycle)] for t in range(k)) for i in range(len(cycle))}

def construct(k):
    n=k-1
    need=required(k)
    ds, ss = sources_sinks(k)
    incoming = Counter()
    out = defaultdict(list)
    for w in need:
        out[w[:-1]].append((w[1:], w[-1]))
    e = 0
    for d in ds:
        suffix,target = routing(d)
        assert target in ss
        incoming[target] += 1
        for b in suffix:
            target2 = d[1:] + b
            out[d].append((target2,b))
            d = target2
            e+=1
    assert set(incoming) == set(ss) and all(z==1 for z in incoming.values())
    E=sum(len(x) for x in out.values())
    assert E==len(need)+e
    # Hierholzer: edge character order is the cyclic host.
    current = next(iter(out))
    stack=[(current, None)]
    chars=[]
    while stack:
        v,_=stack[-1]
        if out[v]:
            t,c=out[v].pop()
            stack.append((t,c))
        else:
            v,c=stack.pop()
            if c is not None:chars.append(c)
    cyc=''.join(reversed(chars))
    assert len(cyc)==E
    windows=cyclic_windows(cyc,k)
    assert set(need).issubset(windows)
    assert '010' in cyclic_windows(cyc,3)
    assert sum(map(len,out.values()))==0
    return len(need),e,len(cyc)

def distance(a,b):
    n=len(a)
    for t in range(1,n+1):
        if a[t:]==b[:n-t]:return t
    raise AssertionError

def hungarian(cost):
    # Square minimum-cost assignment via dual potentials, O(m^3).
    n=len(cost)
    u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i;j0=0;minv=[10**9]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True
            i0=p[j0];delta=10**9;j1=0
            for j in range(1,n+1):
                if not used[j]:
                    cur=cost[i0-1][j-1]-u[i0]-v[j]
                    if cur<minv[j]:minv[j]=cur;way[j]=j0
                    if minv[j]<delta:delta=minv[j];j1=j
            for j in range(n+1):
                if used[j]:u[p[j]]+=delta;v[j]-=delta
                else:minv[j]-=delta
            j0=j1
            if p[j0]==0:break
        while True:
            j1=way[j0];p[j0]=p[j1];j0=j1
            if j0==0:break
    return -v[0]

def formula_sequence(maxk):
    # Formal series: E(z)(1-z)^2(1-2z+z^2-z^3)=z^3(1-2z+2z^2).
    d=[1,-4,6,-5,3,-1]
    target={3:1,4:-2,5:2}
    vals=[]
    for k in range(maxk+1):
        vals.append(target.get(k,0)-sum(d[j]*vals[k-j] for j in range(1,len(d)) if k-j>=0))
    return vals

def A_seq(maxk):
    a=[1,2,4]
    for j in range(3,maxk+1):a.append(2*a[j-1]-a[j-2]+a[j-3])
    return a

def main():
    es=formula_sequence(18)
    a=A_seq(18)
    for k in range(3,14):
        req,e,C=construct(k)
        assert req==a[k],(k,req,a[k])
        assert e==es[k],(k,e,es[k])
        ds,ss=sources_sinks(k)
        assert e==sum(len(routing(v)[0]) for v in ds)
        assert len({routing(v)[1] for v in ds})==len(ss)
        for v in ds:
            assert len(routing(v)[0])==min(distance(v,s) for s in ss)
        if k<=10:
            opt=hungarian([[distance(d,s) for s in ss] for d in ds])
            assert opt==es[k],(k,opt,es[k])
        print(f'k={k} required={req} overhead={e} cycle={C}')
    print('VERIFY_OK cyclic_hosts_k=3..13 independent_assignment_optimality_k=3..10 generating_function_coefficients=3..13')
if __name__=='__main__':main()
