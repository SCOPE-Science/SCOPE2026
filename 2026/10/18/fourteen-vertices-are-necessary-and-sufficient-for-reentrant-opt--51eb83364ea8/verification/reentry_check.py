"""Exact, standalone certificate for reentrant optimal single-vertex vaccination.

Only the Python standard library is needed. Every enumeration and sign decision is
exact. Run: python reentry_check.py
"""
from fractions import Fraction
from itertools import product


def compositions(n):
    if n == 0:
        yield ()
    else:
        for first in range(1, n + 1):
            for rest in compositions(n-first):
                yield (first,) + rest


def profiles(size):
    if size == 1:
        yield (1,)
    else:
        for c in compositions(size - 1):
            yield (1,) + c


def trim(f):
    z = list(f)
    while z and z[-1] == 0:
        z.pop()
    return z


def rem(f,g):
    f, g = trim(f), trim(g)
    assert g
    if not f:
        return []
    f = list(map(Fraction, f))
    g = list(map(Fraction, g))
    while len(f) >= len(g):
        t = f[-1] / g[-1]
        k = len(f) - len(g)
        for j in range(len(g)):
            f[k+j] -= t*g[j]
        f = trim(f)
    return f


def sturm(f):
    f = list(map(Fraction, trim(f)))
    if len(f) <= 1:
        return [f]
    out = [f, [j*f[j] for j in range(1, len(f))]]
    out[1] = trim(out[1])
    while out[-1]:
        r = [-x for x in rem(out[-2],out[-1])]
        if not r:
            break
        out.append(r)
    return out


def signs_at_endpoint(f, endpoint):
    # One-sided sign from within the open interval (0,1).
    if endpoint == 0:
        for c in f:
            if c:
                return 1 if c > 0 else -1
    else:
        g = f[:]
        for k in range(len(f)):
            value = sum(g)
            if value:
                value *= (-1)**k
                return 1 if value > 0 else -1
            g = [j*g[j] for j in range(1,len(g))]
    raise AssertionError('zero polynomial')


def variations(signs):
    return sum(a != b for a,b in zip(signs, signs[1:]))


def interval_root_count(f):
    f = trim(f)
    if len(f)<=1:
        return 0
    seq=sturm(f)
    return variations([signs_at_endpoint(z,0) for z in seq])-variations([signs_at_endpoint(z,1) for z in seq])


def poly_difference(a,b):
    # B_A(p)-B_B(p) = p^2*Q(p); Q coefficients by increasing degree.
    return trim([(a[j] if j<len(a) else 0)-(b[j] if j<len(b) else 0)
                 for j in range(1,max(len(a),len(b)))])


def sign_variations(f):
    signs=[1 if z>0 else -1 for z in f if z]
    return variations(signs)


def exact_small_tree_exhaustion():
    cache = {n: tuple(profiles(n)) for n in range(1,12)}
    pairs = 0
    sturm_tests = 0
    zero_roots = 0
    one_root = 0
    for size_a in range(1,12):
        for size_b in range(1,13-size_a):
            if 1+size_a+size_b>13:
                continue
            for a in cache[size_a]:
                for b in cache[size_b]:
                    pairs+=1
                    f=poly_difference(a,b)
                    if sign_variations(f)>=2:
                        sturm_tests+=1
                        roots=interval_root_count(f)
                        if roots>=2:
                            raise AssertionError((a,b,f,roots))
                        if roots==0:
                            zero_roots+=1
                        else:
                            one_root+=1
    # Formula for all ordered profile pairs under 13 vertices.
    assert pairs == 6144, pairs
    print('ALL TREES <=13: profile pairs =', pairs,
          'Sturm candidates =',sturm_tests, '0 roots =',zero_roots,
          '1 root =',one_root, '>=2 roots = 0')


def witness():
    a,b=(1,1,4),(1,2,1,1,1,1)
    f=poly_difference(a,b)
    assert f==[-1,3,-1,-1,-1]
    assert interval_root_count(f)==2
    def evalp(f,p):
        return sum(Fraction(c)*p**i for i,c in enumerate(f))
    assert evalp(f,Fraction(1,2))==Fraction(1,16)
    assert evalp(f,Fraction(0))==-1
    assert evalp(f,Fraction(1))==-1
    assert sum(a)+sum(b)+1==14
    print('14-VERTEX WITNESS: profiles =',a,b,'Q coefficients =',f,
          'Q(1/2) =',evalp(f,Fraction(1,2)),
          'two exact roots in (0,1)')


def network_crosscheck():
    # Build a tree with two branches whose depth profiles are (1,1,4),
    # (1,2,1,1,1,1). One representative attached all vertices of every
    # successive layer to the same ancestor in the prior layer.
    parents={1:0,2:1,3:2,4:2,5:2,6:2,
             7:0,8:7,9:7,10:8,11:10,12:11,13:12}
    edges=list(parents.items())
    assert len(edges)==13
    # Exhaust all 2^13 Bernoulli percolation configurations on each parameter;
    # independently recompute infection reduction after removing vertices.
    def infected_count(mask, removed):
        adj={v:[] for v in range(14) if v!=removed}
        for i,(u,v) in enumerate(edges):
            if mask>>i & 1 and u!=removed and v!=removed:
                adj[u].append(v);adj[v].append(u)
        seen={0};queue=[0]
        for x in queue:
            for y in adj[x]:
                if y not in seen:
                    seen.add(y);queue.append(y)
        return len(seen)
    for p in (Fraction(1,10),Fraction(1,2),Fraction(9,10)):
        avoided={v:Fraction(0) for v in (1,7,3,8)}
        for mask in range(1<<13):
            weight=p**mask.bit_count()*(1-p)**(13-mask.bit_count())
            base=infected_count(mask,-1)
            for v in avoided:
                avoided[v]+=weight*(base-infected_count(mask,v))
        score_a=p+p**2+4*p**3
        score_b=p+2*p**2+p**3+p**4+p**5+p**6
        assert avoided[1]==score_a
        assert avoided[7]==score_b
        assert avoided[3]<score_a and avoided[8]<score_b
        print('BOND ENUMERATION at',str(p),'scores',str(score_a),str(score_b),
              'optimal', 'A' if score_a>score_b else 'B')


if __name__=='__main__':
    exact_small_tree_exhaustion()
    witness()
    network_crosscheck()
    print('ALL EXACT CHECKS PASSED')
