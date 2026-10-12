"""Standalone exact verification for total-forcing counts of sunlet graphs.
Run with Python 3.10+; no third-party dependencies.
"""
from collections import defaultdict
from itertools import product
from math import comb

LETTERS = ('A','B','D')
WEIGHT = {'A':2, 'B':1, 'D':0}
STATES = [(previous, current, start)
          for previous in LETTERS for current in LETTERS
          for start in ((None,) if current == 'B' else ('A','D'))]


def permitted(u, v):
    previous, current, beginning = u
    preceding, nxt, begin_next = v
    if preceding != current:
        return False
    # Root B would be isolated among initial selected vertices.
    if previous == 'D' and current == 'B' and nxt == 'D':
        return False
    # Continue a component of the alternating A--D auxiliary graph.
    if current in ('A','D') and nxt in ('A','D') and current != nxt:
        return beginning == begin_next
    # Ending a component with both endpoint labels D is forbidden.
    if current in ('A','D') and beginning == current == 'D':
        return False
    return begin_next == (None if nxt == 'B' else nxt)


EDGES = [[(j, WEIGHT[STATES[j][1]])
          for j in range(len(STATES)) if permitted(STATES[i], STATES[j])]
         for i in range(len(STATES))]


def raw_trace(n):
    """Coefficient dictionary of tr(M(z)^n); exact integer arithmetic."""
    total = defaultdict(int)
    for start in range(len(STATES)):
        current = {(start, 0): 1}
        for _ in range(n):
            new = defaultdict(int)
            for (i, degree), multiplicity in current.items():
                for j, degree_shift in EDGES[i]:
                    new[j, degree + degree_shift] += multiplicity
            current = new
        for (i, degree), multiplicity in current.items():
            if i == start:
                total[degree] += multiplicity
    return dict(total)


def from_transfer(n):
    counts = raw_trace(n)
    if n % 2 == 0:
        counts[n] = counts.get(n, 0) - 4
    return {k:v for k,v in sorted(counts.items()) if v}


def from_forcing(n):
    """Directly simulate ordinary forcing on the 2n-vertex labeled graph.
    This does not use the A/B/D characterization or the matrix.
    """
    neighborhoods = [set() for _ in range(2*n)]
    for i in range(n):
        for j in ((i+1)%n, n+i):
            neighborhoods[i].add(j)
            neighborhoods[j].add(i)
    counts = defaultdict(int)
    checked = 0
    for mask in range(1<<(2*n)):
        checked += 1
        selected = {i for i in range(2*n) if (mask>>i)&1}
        if any(not (neighborhoods[i] & selected) for i in selected):
            continue
        blue = set(selected)
        while True:
            forced = set()
            for v in blue:
                white_neighbors = neighborhoods[v] - blue
                if len(white_neighbors) == 1:
                    forced.update(white_neighbors)
            if not forced:
                break
            blue.update(forced)
        if len(blue) == 2*n:
            counts[len(selected)] += 1
    return dict(counts), checked


def structural(n):
    """Independently test the auxiliary alternating-component criterion."""
    counts = defaultdict(int)
    for letters in product(LETTERS, repeat=n):
        if any(letters[i]=='B' and letters[(i-1)%n]=='D'
               and letters[(i+1)%n]=='D' for i in range(n)):
            continue
        remaining = {i for i,c in enumerate(letters) if c=='D'}
        while True:
            next_delete = set()
            for i,c in enumerate(letters):
                if c!='A':continue
                white = remaining.intersection({(i-1)%n, (i+1)%n})
                if len(white)==1:
                    next_delete.update(white)
            if not next_delete:break
            remaining-=next_delete
        if not remaining:
            counts[sum(WEIGHT[c] for c in letters)] += 1
    return dict(counts)


def poly_add(a,b,scale=1):
    out = dict(a)
    for i, coefficient in b.items():
        out[i] = out.get(i,0)+scale*coefficient
    return {i:v for i,v in out.items() if v}


def poly_mul(a,b):
    out = defaultdict(int)
    for i,va in a.items():
        for j,vb in b.items():
            out[i+j]+=va*vb
    return {i:v for i,v in out.items() if v}


def check_characteristic_polynomial():
    # Newton identities reconstruct the characteristic polynomial exactly
    # from the graph-theoretically constructed 15x15 transfer matrix.
    powers = [None]+[raw_trace(k) for k in range(1,16)]
    c = [{0:1}]
    for k in range(1,16):
        subtotal = {}
        for j in range(1,k+1):
            subtotal=poly_add(subtotal,poly_mul(c[k-j],powers[j]))
        assert all(v%k==0 for v in subtotal.values()), ('nonintegral Newton coefficient',k)
        c.append({d:-v//k for d,v in subtotal.items() if v})
    wanted = {1:{1:-1,2:-1}, 2:{2:-2}, 3:{4:1}, 5:{5:1}}
    for k in range(1,16):
        assert c[k] == wanted.get(k,{}), (k,c[k],wanted.get(k,{}))
    return True


def main():
    print('states',len(STATES),'weighted_transitions',sum(map(len,EDGES)))
    assert check_characteristic_polynomial()
    print('characteristic_identity_exact',True)
    n_checked = 0
    for n in range(3,9):
        a=from_transfer(n)
        b, checked=from_forcing(n)
        c=structural(n)
        assert a==b==c, (n,a,b,c)
        assert min(a)==n
        n_checked+=checked
        print('n',n,'checked_subsets',checked,'total_forcing_coefficients',a)
    # Larger lengths: independent A/B/D peeling vs transfer polynomial.
    for n in (9,10,11):
        assert from_transfer(n)==structural(n), n
        print('n',n,'transfer_vs_alternating_peeling',True,
              'minimum_count',from_transfer(n)[n])
    print('DIRECT_SUBSETS',n_checked)
    print('ALL_CHECKS_PASS')


if __name__=='__main__':
    main()
