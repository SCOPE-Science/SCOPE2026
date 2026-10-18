"""Independent explicit stabilizer action and class-cardinality verification."""
from collections import defaultdict
from itertools import combinations, permutations


def orbit_partition(m, n, markers):
    elements = [(r, c) for r in range(m) for c in range(n)]
    admissible = []
    for a in permutations(range(m)):
        for b in permutations(range(n)):
            if all((a[r],b[c]) == (r,c) for r,c in markers):
                admissible.append((a,b,False))
            if m == n and all((a[c],b[r]) == (r,c) for r,c in markers):
                admissible.append((a,b,True))
    classes = set()
    for r,c in elements:
        classes.add(frozenset((a[c],b[r]) if flip else (a[r],b[c])
                              for a,b,flip in admissible))
    assert sum(len(z) for z in classes) == m*n
    return frozenset(classes)


def formula_partition(m, n, markers):
    rows = {r: tuple(k for k,(x,y) in enumerate(markers) if x==r) for r in range(m)}
    cols = {c: tuple(k for k,(x,y) in enumerate(markers) if y==c) for c in range(n)}
    flip = m==n and len(set(x for x,_ in markers))==len(markers) and len(set(y for _,y in markers))==len(markers)
    D=defaultdict(set)
    for r in range(m):
        for c in range(n):
            key = (rows[r],cols[c]); key = min(key,key[::-1]) if flip else key
            D[key].add((r,c))
    a=len(set(x for x,y in markers));b=len(set(y for x,y in markers))
    R=a+int(m>a);C=b+int(n>b)
    predicted_count=R*(R+1)//2 if flip else R*C
    assert len(D)==predicted_count
    return frozenset(frozenset(z) for z in D.values())


def run():
    tests=0
    for m,n in [(2,2),(2,3),(3,3),(2,4),(3,4),(4,4)]:
        board=[(r,c) for r in range(m) for c in range(n)]
        for t in range(0, min(3,len(board))+1):
            for markers in combinations(board,t):
                found=orbit_partition(m,n,markers)
                expected=formula_partition(m,n,markers)
                assert found==expected, (m,n,markers)
                tests+=1
    print('VERIFY_ORBITS_OK explicit_group_instances=%d' % tests)

if __name__=='__main__':
    run()
