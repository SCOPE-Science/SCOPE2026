"""Independent exact-integer checks of a two-car torus traffic theorem.

Run: python3 verify_two_car.py
Does not replace the all-size mathematical proof.
"""
from math import gcd, lcm

def direct_step(h, v, m, n):
    hr, hc = h
    vr, vc = v
    hnext = (hr, (hc + 1) % m)
    blocked_h = (hnext == v)
    if not blocked_h:
        h = hnext
    vnext = ((vr + 1) % n, vc)
    blocked_v = (vnext == h)
    if not blocked_v:
        v = vnext
    assert h != v
    return h, v, 'H' if blocked_h else ('V' if blocked_v else '.')

def forecast(m, n):
    g = gcd(m, n)
    L = lcm(m, n)
    if g >= 3:
        return {'mode':'free', 'period':L}
    if g == 2:
        return {'mode':'alternating', 'period':L + 1}
    r = pow(m,-1,n)
    if 2*r > n:
        return {'mode':'H', 'period':m*(n-r) + 1}
    return {'mode':'V', 'period':m*r}

def verify(m,n):
    expected = forecast(m,n)
    L = lcm(m,n)
    count_once=0
    for vr in range(n):
      for vc in range(m):
        if vr==0 and vc==0: continue
        h,v=(0,0),(vr,vc)
        seen={}; bl=[]; steps=0
        while (h,v) not in seen:
            seen[h,v] = steps
            h,v,b = direct_step(h,v,m,n)
            bl.append(b)
            steps+=1
            assert steps < 5*m*n + 100, (m,n,vr,vc)
        transient=seen[h,v]
        cyc=bl[transient:]
        assert len(cyc)==expected['period'], (m,n,vr,vc,len(cyc),expected)
        H,V=cyc.count('H'),cyc.count('V')
        if expected['mode']=='free':
            assert H==V==0
            assert bl.count('H') + bl.count('V') <=1
            if bl.count('H') + bl.count('V') == 1:
                count_once+=1
        elif expected['mode']=='alternating':
            assert H==V==1, (m,n,vr,vc,H,V)
        elif expected['mode']=='H':
            assert (H,V)==(1,0), (m,n,vr,vc,H,V)
        else:
            assert (H,V)==(0,1), (m,n,vr,vc,H,V)
    if expected['mode']=='free':
        assert count_once==2*L-1, (m,n,count_once,2*L-1)
    return expected

if __name__=='__main__':
    cases=0
    for m in range(2,17):
        for n in range(2,17):
            verify(m,n)
            cases+=1
    print('PASS:',cases,'lattice dimensions, all',sum(m*n-1 for m in range(2,17) for n in range(2,17)),'valid relative placements, full physical-state cycles, all arithmetic predictions.')
    for m,n in [(3,3),(4,6),(3,5),(5,3),(8,9),(89,55)]:
        print((m,n),forecast(m,n))
