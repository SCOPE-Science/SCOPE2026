#!/usr/bin/env python3
"""Complete finite-state census of unary modal term functions on 2-world frames."""
from itertools import combinations

def rows(mask):
    return tuple(sum(1 << j for j in range(2) if mask & (1 << (2*i+j))) for i in range(2))

def image_box(value, row):
    return sum(1 << i for i in range(2) if value & row[i] == row[i])

def image_dia(value, row):
    return sum(1 << i for i in range(2) if value & row[i])

def close(row, neg=False):
    universe = 3
    known = {(0,0,0,0), (3,3,3,3), (0,1,2,3)}
    frontier = list(known)
    while frontier:
        x = frontier.pop()
        generated = [tuple(image_box(v,row) for v in x), tuple(image_dia(v,row) for v in x)]
        if neg:
            generated.append(tuple(universe ^ v for v in x))
        for y in list(known):
            generated.append(tuple(a & b for a,b in zip(x,y)))
            generated.append(tuple(a | b for a,b in zip(x,y)))
        for z in generated:
            if z not in known:
                known.add(z); frontier.append(z)
    return known

def monotone(f):
    return all((a & b != a) or (f[a] & f[b] == f[a]) for a in range(4) for b in range(4))

def flip_rows(row):
    r = [(row[i] >> j) & 1 for i in range(2) for j in range(2)]
    return tuple(sum(r[(1-i)*2+(1-j)] << j for j in range(2)) for i in range(2))

def witness(row):
    out=[]
    for p in range(4):
        d=image_dia(p,row)
        b=image_box(p,row)
        out.append(d & (b | (3 ^ p)))
    return tuple(out)

def simulation(row):
    Z=((0,0),(0,1),(1,0))
    A=2  # p = {1}
    B=1  # p = {0}
    for u,v in Z:
        if A & (1<<u) and not B & (1<<v): return False
        su=[a for a in range(2) if row[u] & (1<<a)]
        sv=[b for b in range(2) if row[v] & (1<<b)]
        if any(not any((a,b) in Z for b in sv) for a in su):return False
        if any(not any((a,b) in Z for a in su) for b in sv):return False
    return True

def main():
    rows_by_mask={mask: rows(mask) for mask in range(16)}
    reprs={}
    full_bad=[]
    records=[]
    for mask,row in rows_by_mask.items():
        p=close(row)
        t=close(row,True)
        m={f for f in t if monotone(f)}
        assert p<=m<=t
        bad=m-p
        records.append((mask,row,len(p),len(t),len(m),len(bad)))
        if bad: full_bad.append(mask)
        orbit_rep=min(mask, next(k for k,r in rows_by_mask.items() if r==flip_rows(row)))
        if orbit_rep == mask: reprs[orbit_rep]=(row,len(p),len(t),len(m),len(bad))
        assert (not bad)==(not (row[0]&2 and row[1]&1 and (row[0]&1 or row[1]&2)))
    print('ALL LABELED FRAMES:')
    for rec in records: print(*rec)
    print('NON-ISOMORPHIC REPRESENTATIVES:')
    for key,rec in sorted(reprs.items()): print(key,*rec)
    print('NON-POSITIVE MONOTONE LABELED FRAMES',full_bad)
    assert full_bad==[7,14,15]
    assert len(reprs)==10
    for key in (7,15):
        row=rows_by_mask[key]
        assert simulation(row)
        assert witness(row)==(0,2,1,3)
        assert witness(row) in (close(row,True)-close(row))
        print('WITNESS',key,'rows',row,'term operation',witness(row),'simulation True')
    one=[]
    for row in ((0,),(1,)):
        def closure1(neg=False):
            s={(0,0),(1,1),(0,1)};work=list(s)
            while work:
                x=work.pop()
                box=lambda a: int((a&row[0])==row[0]);dia=lambda a:int(bool(a&row[0]))
                y=[tuple(box(a) for a in x),tuple(dia(a) for a in x)]
                if neg:y.append(tuple(1-a for a in x))
                for z in list(s):
                    y.extend([tuple(a&b for a,b in zip(x,z)),tuple(a|b for a,b in zip(x,z))])
                for k in y:
                    if k not in s:s.add(k);work.append(k)
            return s
        p=closure1();m={f for f in closure1(True) if (f[0]<=f[1])}
        assert p==m
        one.append((row,len(p),len(m)))
    print('ONE WORLD',one)
    print('PASS exhaustive term-operation fixed-point census, counterexamples, simulations, and 1-world minimality')

if __name__=='__main__':main()
