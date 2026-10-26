"""Exact Fourier fourth-moment census for a center-punctured three-by-three aperture.
All arithmetic is integer-valued; no numerical transforms or external packages.
"""
from collections import Counter, defaultdict, deque
from itertools import product

# Fixed published coordinate convention: increasing first coordinate, then second.
SUPPORT = tuple((i,j) for i in (-1,0,1) for j in (-1,0,1) if i or j)
assert len(SUPPORT)==8 and len(set(SUPPORT))==8
INDEX = {p:i for i,p in enumerate(SUPPORT)}
HIST_EXPECTED = {
 3: {72:6, 88:96, 104:48, 120:48, 168:40, 216:16, 456:2},
 4: {88:16, 104:80, 120:80, 136:16, 168:8, 184:16, 200:16, 216:16, 296:8},
 5: {88:24, 104:96, 120:80, 136:16, 152:16, 168:16, 216:8},
}
ORBIT_EXPECTED = sorted([
 (88,8,'----+-+-'), (88,16,'----++-+'),
 (104,16,'-----+-+'), (104,16,'--+--++-'), (104,64,'------++'),
 (120,8,'--+--+--'), (120,8,'--+-+++-'),
 (120,32,'-------+'), (120,32,'----+-++'),
 (136,16,'------+-'), (152,16,'-----+++'),
 (168,16,'----++++'), (216,8,'--------'),
])

def key(v,n):
    return v if n is None else (v[0]%n,v[1]%n)

def convolution_moment(signs,n):
    sums=defaultdict(int)
    for a,u in enumerate(SUPPORT):
        for b,v in enumerate(SUPPORT):
            sums[key((u[0]+v[0],u[1]+v[1]),n)] += signs[a]*signs[b]
    return sum(t*t for t in sums.values())

def autocorrelation_moment(signs,n):
    # Independent difference-index contraction, not the convolution routine above.
    differences=defaultdict(int)
    for i,(x,y) in enumerate(SUPPORT):
        for j,(a,b) in enumerate(SUPPORT):
            differences[key((x-a,y-b),n)] += signs[i]*signs[j]
    return sum(t*t for t in differences.values())

def symmetries(v):
    # The following generators preserve the continuous/aperiodic fourth moment.
    yield tuple(v[INDEX[(-j,i)]] for i,j in SUPPORT) # quarter turn
    yield tuple(v[INDEX[(-i,j)]] for i,j in SUPPORT) # reflection
    yield tuple(-t for t in v)                  # common sign
    yield tuple(t*(-1 if i else 1) for t,(i,j) in zip(v,SUPPORT))
    yield tuple(t*(-1 if j else 1) for t,(i,j) in zip(v,SUPPORT))

def orbit(v):
    seen={v};q=deque([v])
    while q:
        for w in symmetries(q.popleft()):
            if w not in seen:
                seen.add(w);q.append(w)
    return seen

def sign_text(v): return ''.join('+' if z==1 else '-' for z in v)

def main():
    vectors=list(product((-1,1),repeat=8))
    assert len(vectors)==256
    data={}
    for n in (3,4,5):
        hist=Counter()
        for v in vectors:
            m=convolution_moment(v,n)
            assert m==autocorrelation_moment(v,n), (n,v)
            hist[m]+=1
        assert dict(hist)==HIST_EXPECTED[n],(n,hist)
        assert sum(hist.values())==256
        data[n]=hist
        print('CHECK_PASS n=%s min=%s count=%s max=%s values=%s'
              %(n,min(hist),hist[min(hist)],max(hist),sorted(hist.items())))
    for v in vectors:
        assert convolution_moment(v,None)==convolution_moment(v,5)
        assert autocorrelation_moment(v,None)==autocorrelation_moment(v,5)
    allv=set(vectors);reps=[]
    while allv:
        v=min(allv);group=orbit(v)
        assert group <= allv
        val=convolution_moment(v,None)
        assert all(convolution_moment(w,None)==val for w in group)
        reps.append((val,len(group),sign_text(v)))
        allv-=group
    assert sorted(reps)==ORBIT_EXPECTED,(sorted(reps),ORBIT_EXPECTED)
    assert sum(s for _,s,_ in reps)==256
    assert sum(s for e,s,_ in reps if e==88)==24
    print('CHECK_PASS 13 aperiodic symmetry orbits; exact representatives:')
    for e,s,t in sorted(reps): print(' ',e,s,t)
    print('CHECK_PASS all 256 masks independently checked for each modulus 3,4,5 '
          'and for the aperiodic case')

if __name__=='__main__': main()
