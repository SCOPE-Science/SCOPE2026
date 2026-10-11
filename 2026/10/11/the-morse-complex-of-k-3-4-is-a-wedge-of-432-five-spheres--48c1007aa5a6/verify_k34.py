"""Exact reproducible simplicial discrete Morse and integral cellular-boundary check.

The complex is the ordinary Morse complex of the graph K_(3,4).
Every simplex is represented by a bitset of oriented graph edges (arcs).
Uses only the Python 3 standard library. All tests are exhaustive and exact.
"""
from itertools import product
from collections import Counter, defaultdict, deque
from functools import lru_cache


def build():
    p, q = 3, 4
    choices, arcs = [], []
    for u in range(p+q):
        choices.append([])
        for v in (range(p, p+q) if u < p else range(p)):
            choices[-1].append((v, len(arcs)))
            arcs.append((u,v))
    faces = set()
    for c in product(*([[(None, None)] + opts for opts in choices])):
        target = [v for v, _ in c]
        acyclic = True
        for start in range(p+q):
            x, seen = start, set()
            while x is not None:
                if x in seen:
                    acyclic = False
                    break
                seen.add(x)
                x = target[x]
            if not acyclic:
                break
        if acyclic:
            faces.add(sum(1 << bit for v,bit in c if bit is not None))
    return arcs, faces


def boundary(simplex):
    bits, pos = simplex, 0
    while bits:
        bit = bits & -bits
        bits ^= bit
        yield simplex ^ bit, 1 if pos % 2 == 0 else -1
        pos += 1


def matching(faces, n_arcs):
    remaining, pairs = set(faces), []
    for index in range(n_arcs):
        bit = 1 << index
        selected = [(s,s|bit) for s in sorted(remaining)
                    if not s & bit and (s|bit) in remaining]
        for lower,upper in selected:
            remaining.remove(lower)
            remaining.remove(upper)
            pairs.append((lower,upper))
    return pairs, remaining


def acyclic_matching_check(faces, pairs):
    paired = set(pairs)
    outgoing = defaultdict(list)
    indegree = {s:0 for s in faces}
    num_incidence = 0
    for big in faces:
        for small, _ in boundary(big):
            if (small,big) in paired:
                a,b=small,big
            else:
                a,b=big,small
            outgoing[a].append(b)
            indegree[b] += 1
            num_incidence += 1
    q = deque(s for s,d in indegree.items() if d == 0)
    visited = 0
    while q:
        s=q.popleft(); visited += 1
        for t in outgoing[s]:
            indegree[t] -= 1
            if not indegree[t]:
                q.append(t)
    assert visited == len(faces), (visited, len(faces))
    return num_incidence


def reduced_boundary(pairs, critical):
    crit4 = sorted(s for s in critical if s.bit_count()==5)
    crit5 = sorted(s for s in critical if s.bit_count()==6)
    paired_lower = {s:t for s,t in pairs if s.bit_count()==5}
    paired_upper = {t for s,t in pairs if t.bit_count()==5}
    index = {s:i for i,s in enumerate(crit4)}

    @lru_cache(None)
    def proj(s):
        if s in index:
            return {index[s]:1}
        if s in paired_upper:
            return {}
        assert s in paired_lower, ('unexpected 4-cell',s)
        big=paired_lower[s]
        epsilon = next(sign for face,sign in boundary(big) if face==s)
        result=defaultdict(int)
        for face,sign in boundary(big):
            if face==s:
                continue
            for i,a in proj(face).items():
                result[i] -= epsilon*sign*a
        return {i:a for i,a in result.items() if a}

    rows=[{} for _ in crit4]
    for j,s in enumerate(crit5):
        image=defaultdict(int)
        for face,sign in boundary(s):
            for i,a in proj(face).items():
                image[i] += sign*a
        for i,a in image.items():
            if a:
                rows[i][j]=a
    return rows, len(crit5)


def unit_pivots(rows, ncolumns):
    rows={i:dict(row) for i,row in enumerate(rows)}
    columns={j:set() for j in range(ncolumns)}
    for i,row in rows.items():
        for j in row:
            columns[j].add(i)
    pivot_count,largest=0,0
    while rows:
        candidates=[]
        for i,row in rows.items():
            cols=[j for j,a in row.items() if abs(a)==1]
            if cols:
                j=min(cols, key=lambda c:len(columns[c]))
                candidates.append((len(row)*len(columns[j]),len(row),len(columns[j]),i,j))
        if not candidates:
            break
        *_,i,j=min(candidates)
        pivotrow=rows[i]
        sign=pivotrow[j]
        for r in list(columns[j]-{i}):
            row=rows[r]
            multiplier=row[j]*sign
            for c,a in pivotrow.items():
                new=row.get(c,0)-multiplier*a
                if new:
                    if c not in row:
                        columns[c].add(r)
                    row[c]=new
                    largest=max(largest,abs(new))
                else:
                    row.pop(c,None)
                    columns[c].discard(r)
        for c in pivotrow:
            columns[c].discard(i)
        del rows[i]
        pivot_count += 1
    return pivot_count,len(rows),largest


def main():
    arcs,faces=build()
    assert len(arcs)==24 and len(faces)==12800
    counts=Counter(s.bit_count()-1 for s in faces)
    assert counts=={-1:1,0:24,1:234,2:1192,3:3357,4:4968,5:3024},counts
    pairs,critical=matching(faces,len(arcs))
    assert len(pairs)==5887
    assert Counter(s.bit_count()-1 for s in critical)=={4:297,5:729}
    assert (0,1) in pairs
    inc=acyclic_matching_check(faces,pairs)
    assert inc==60480
    matrix,ncols=reduced_boundary(pairs,critical)
    assert len(matrix)==297 and ncols==729
    assert sum(len(row) for row in matrix)==4162
    assert max(abs(a) for row in matrix for a in row.values())==1
    pivots,remainders,max_entry=unit_pivots(matrix,ncols)
    assert pivots==297 and remainders==0 and max_entry<=2
    assert 729-pivots==432
    print('VERIFY_OK faces=12799_nonempty pairs=5886_ordinary critical=1x0+297x4+729x5 incidences=60480 integer_unit_pivots=297 wedge_S5=432')


if __name__=='__main__':
    main()
