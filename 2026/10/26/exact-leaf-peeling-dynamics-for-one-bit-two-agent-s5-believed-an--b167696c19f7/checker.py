#!/usr/bin/env python3
"""Finite verification of believed-announcement stabilization and witness families."""
from itertools import product

def atom(w,bit): return bool((w>>bit)&1)
def mk_s5(n): return [(1<<n)-1]*n
def step(R,v,phi):
    n=len(R)
    truth=sum(1<<w for w in range(n) if phi(w,R,v))
    return [r&truth for r in R]
def trajectory(R,v,phi,lim=200):
    states=[tuple(R)]
    for _ in range(lim):
        R=step(R,v,phi)
        if tuple(R)==states[-1]: return len(states)-1,states
        states.append(tuple(R))
    raise AssertionError('did not stabilize')
def witness_one(k):
    m=1<<k
    vals=tuple(range(m))
    R=mk_s5(m)
    def phi(w,R,v):
        x=v[w]
        return x < m-1 and bool(R[w] & (1<<(x+1)))
    t,states=trajectory(R,vals,phi)
    assert t==m,(k,t,m)
    for i,S in enumerate(states):
        mask=(1<<(m-i))-1
        assert all(row==mask for row in S),(k,i,S,mask)
    return t

def witness_two(n):
    # Agent a pairs (0,1),(2,3), ...; agent b pairs (1,2),(3,4), ...
    vals=tuple(i%2 for i in range(n))
    R=[]
    for start in (0,1):
        a=[0]*n
        for u in range(n):
            pair=u-1 if (u-start)%2 else u+1
            if 0 <= pair<n: a[u]=(1<<u)|(1<<pair)
            else: a[u]=(1<<u)
        R.append(a)
    def phi(w,relations,v):
        return all(any(((mask>>z)&1) and v[z]!=v[w] for z in range(n)) for mask in (relations[0][w],relations[1][w]))
    t=0
    states=[tuple(tuple(r) for r in R)]
    while True:
        truth=sum(1<<w for w in range(n) if phi(w,R,vals))
        new=[[mask&truth for mask in a] for a in R]
        if new==R: break
        R=new; t+=1
        states.append(tuple(tuple(a) for a in R))
        assert t<=n
        remaining=sum(1<<u for u in range(t,n-t))
        assert all(mask==original&remaining for arr0,arr in zip(states[0],R) for original,mask in zip(arr0,arr)),(n,t)
    assert t==(n+1)//2,(n,t)
    return t

def K45(R):
    n=len(R)
    for x in range(n):
        for y in range(n):
            if (R[x]>>y)&1:
                if R[y]&~R[x]:return False # transitive
                if R[x]&~R[y]:return False # euclidean
    return True

def test_one_general():
    # Exhaust initial K45 relations on 1..3 points, 1 variable, with modal-depth 1 and 2 cases.
    candidates=[]
    def ev(w,R,v):
        one=1<<w
        p=bool(v[w])
        has_p=any(((R[w]>>z)&1) and v[z] for z in range(len(R)))
        has_not=any(((R[w]>>z)&1) and not v[z] for z in range(len(R)))
        all_p=not has_not
        # variety includes depth two
        any_not_box_p=any(((R[w]>>z)&1) and any(((R[z]>>q)&1) and not v[q] for q in range(len(R))) for z in range(len(R)))
        return p,has_p,has_not,all_p,any_not_box_p
    for n in range(1,4):
      count=0
      for bits in range(1<<(n*n)):
        R=[(bits>>(i*n))&((1<<n)-1) for i in range(n)]
        if not K45(R): continue
        for vals in product((False,True),repeat=n):
          for z in range(11):
            def phi(w,S,v):
              p,a,b,c,d=ev(w,S,v)
              return (p,a,b,c,d,p and a,p or b, a and b,a!=b,d and not p,a or d)[z]
            t,_=trajectory(R,list(vals),phi,7)
            assert t<=2,(n,vals,z,t)
            count+=1
      candidates.append((n,count))
    return candidates

if __name__=='__main__':
    assert [witness_one(k) for k in range(1,6)]==[2,4,8,16,32]
    assert [witness_two(n) for n in range(2,41)]==[(n+1)//2 for n in range(2,41)]
    print('K45 exhaustive:',test_one_general())
    print('ALL_CHECKS_OK')

def involutions(n):
    def rec(avail,p):
        if not avail:
            yield tuple(p);return
        u=avail[0]
        pp=p.copy();pp[u]=u
        yield from rec(avail[1:],pp)
        for j in range(1,len(avail)):
            v=avail[j];pp=p.copy();pp[u]=v;pp[v]=u
            yield from rec(avail[1:j]+avail[j+1:],pp)
    yield from rec(tuple(range(n)),[None]*n)

def exact_profile(a,b,vals):
    n=len(vals); adj=[]
    for u in range(n):
        adj.append((a[u] if a[u]!=u and vals[a[u]]!=vals[u] else None,
                    b[u] if b[u]!=u and vals[b[u]]!=vals[u] else None))
    seen=set();L=[]; cycles=[]
    for u in range(n):
        if u in seen:continue
        group=set();todo=[u]
        while todo:
            v=todo.pop()
            if v in group:continue
            group.add(v)
            todo.extend(x for x in adj[v] if x is not None and x not in group)
        seen.update(group)
        if all(None not in adj[v] for v in group): cycles.append(group)
        else:
            # each connected component with missing colored partner is a path (possibly singleton)
            assert sum((x is None) for v in group for x in adj[v])==2
            L.append(len(group))
    return max([(x+1)//2 for x in L],default=0),adj

def exhaustive_matching():
    nums=[]
    for n in range(1,7):
      inv=list(involutions(n));checked=0
      for a in inv:
       for b in inv:
        A=[(1<<u)|(1<<a[u]) for u in range(n)]
        B=[(1<<u)|(1<<b[u]) for u in range(n)]
        for valmask in range(1<<n):
          vals=tuple((valmask>>j)&1 for j in range(n))
          predicted,adj=exact_profile(a,b,vals)
          R=[A[:],B[:]]; steps=0;S=(1<<n)-1
          for _ in range(n+1):
            T=0
            for v in range(n):
              if all(any(((R[c][v]>>u)&1) and vals[u]!=vals[v] for u in range(n)) for c in range(2)):
                T|=1<<v
            S2=S&T
            nxt=[[row&S2 for row in part] for part in (A,B)]
            if nxt==R:break
            steps+=1;S=S2;R=nxt
          assert steps==predicted,(n,a,b,vals,steps,predicted)
          checked+=1
      nums.append((n,checked))
    return nums

if __name__=='__main__':
    print('All involution-pair models:',exhaustive_matching())
    print('ALL_CHECKS_OK')
