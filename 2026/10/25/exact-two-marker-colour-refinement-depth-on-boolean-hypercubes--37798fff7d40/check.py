"""Finite computational checks of colour refinement of two marked binary cubes.
Standard library only. No dependence on any proof formulas except the targets tested.
"""
from collections import Counter
from math import comb

def canonical(colors):
    keys = {}; out = []
    for x in colors:
        if x not in keys:
            keys[x] = len(keys)
        out.append(keys[x])
    return out

def one_step(colors, neighborhoods):
    return canonical([(colors[i],tuple(sorted(Counter(colors[j] for j in neighbors).items())))
                      for i,neighbors in enumerate(neighborhoods)])

def same_partition(x,y):
    xy={}; yx={}
    for a,b in zip(x,y):
        if (a in xy and xy[a]!=b) or (b in yx and yx[b]!=a):
            return False
        xy[a]=b; yx[b]=a
    return True

def check_full(d,t):
    vertices=list(range(1<<d)); N=len(vertices)
    b=(1<<t)-1
    neighbours=[[v^(1<<k) for k in range(d)] for v in vertices]
    colors=canonical([1 if v==0 else 2 if v==b else 0 for v in vertices])
    for r in range(d+1):
        want=canonical([(min(v.bit_count(),r+1),min((v^b).bit_count(),r+1)) for v in vertices])
        assert same_partition(colors,want),(d,t,r,'round')
        if r==0: initial=len(set(colors))
        next_colors=one_step(colors,neighbours)
        if r==d:
            assert same_partition(colors,next_colors)
        if len(set(colors))==len(set(next_colors)):
            rounds=r; break
        colors=next_colors
    expected=(d-1 if t==1 else (d-2 if t<d else (d-1)//2))
    assert rounds==expected,(d,t,rounds,expected)
    assert len(set(colors))==(t+1)*(d-t+1)
    freq=Counter(colors)
    sizes=sorted(freq.values())
    expected_sizes=sorted(comb(t,i)*comb(d-t,j) for i in range(t+1) for j in range(d-t+1))
    assert sizes==expected_sizes,(d,t,sizes,expected_sizes)
    return rounds

def check_quotient(d,t):
    u=d-t
    states=[(i,j) for i in range(t+1) for j in range(u+1)]
    index={q:k for k,q in enumerate(states)}
    transitions=[]
    for i,j in states:
        v=[]
        if i: v.extend([index[(i-1,j)]]*i)
        if i<t: v.extend([index[(i+1,j)]]*(t-i))
        if j:v.extend([index[(i,j-1)]]*j)
        if j<u:v.extend([index[(i,j+1)]]*(u-j))
        assert len(v)==d
        transitions.append(v)
    colors=canonical([1 if (i,j)==(0,0) else 2 if (i,j)==(t,0) else 0 for i,j in states])
    for r in range(d+1):
        target=canonical([(min(i+j,r+1),min(t-i+j,r+1)) for i,j in states])
        assert same_partition(colors,target),(d,t,r,'quotient')
        new=one_step(colors,transitions)
        if len(set(colors))==len(set(new)):
            expected=d-1 if t==1 else (d-2 if t<d else (d-1)//2)
            assert r==expected,(d,t,r,expected)
            assert len(set(colors))==(t+1)*(u+1)
            return r
        colors=new
    raise AssertionError(('never stable',d,t))

if __name__=='__main__':
    n_full=0
    for d in range(1,10):
        for t in range(1,d+1):
            check_full(d,t);n_full+=1
    n_quot=0
    for d in range(1,41):
        for t in range(1,d+1):
            check_quotient(d,t);n_quot+=1
    print('Full-graph marked-pair configurations:',n_full)
    print('Separately computed weighted quotient configurations:',n_quot)
    print('Roundwise clipped-distance partitions and sharp stable rounds: ALL_PASS')
