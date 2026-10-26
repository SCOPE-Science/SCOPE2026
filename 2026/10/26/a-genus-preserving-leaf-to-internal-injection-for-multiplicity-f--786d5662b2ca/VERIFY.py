"""Finite, independent checks of a multiplicity-four numerical-semigroup theorem.

Run: python3 VERIFY.py. The mathematical proof is in RESULT.md.
"""

def kunz_valid(a, b, c):
    return min(a,b,c) >= 1 and b <= 2*a and c <= a+b and a <= b+c+1 and b <= 2*c+1


def family(a,b,c):
    if a == b+c+1: return 'A'
    if c == a+b: return 'B'
    if b == 2*a and c <= b-2: return 'C'
    if b == 2*c+1 and a <= b-1: return 'D'
    return None


def minimal_generators(a,b,c):
    ap = (0, 4*a+1, 4*b+2, 4*c+3)
    def inside(v):
        return v >= 0 and v >= ap[v%4]
    candidates = (4, ap[1], ap[2], ap[3])
    return [x for x in candidates if not any(inside(i) and inside(x-i) for i in range(1,x))]


def is_leaf(a,b,c):
    F = max(4*a+1,4*b+2,4*c+3)-4
    return all(x <= F for x in minimal_generators(a,b,c))


def map_leaf(a,b,c,k):
    if k == 'A': return (a-1,b,c+1)
    if k == 'B': return (a+1,b,c-1)
    return (a+1,b-1,c)


def ceildiv(x,d):
    return -((-x)//d)


def predicted(g):
    A = ( (g-1)//2 - ceildiv((g-1)//2-1,3) ) if g>=5 and g%2 else 0
    B = ( g//2 - ceildiv(g//2,3) ) if g>=4 and not g%2 else 0
    C = max(0,g//4 - ceildiv(g+2,5) +1)
    D = max(0,(g-2)//4 - ceildiv(g-1,5) +1)
    return dict(zip('ABCD',(A,B,C,D)))


def run():
    for g in range(3,81):
        counts = dict.fromkeys('ABCD',0)
        images = {}
        total = 0
        for a in range(1,g-1):
            for b in range(1,g-a):
                c = g-a-b
                if not kunz_valid(a,b,c):
                    continue
                total += 1
                k = family(a,b,c)
                assert is_leaf(a,b,c) == (k is not None), ('classification',g,a,b,c)
                if k is None: continue
                counts[k] += 1
                u = map_leaf(a,b,c,k)
                assert sum(u)==g and kunz_valid(*u) and not is_leaf(*u), ('invalid image',g,a,b,c,u)
                assert u not in images, ('collision',g,a,b,c,images.get(u))
                images[u] = (a,b,c)
        assert counts == predicted(g), ('formula',g,counts,predicted(g))
        assert len(images)<=total-len(images), ('dominance',g)
    print('VERIFY_OK: independent minimal-generator test, exact four-family counts, ' 
          'and collision-free genus-preserving injection for genus 3 through 80')

if __name__=='__main__':run()
