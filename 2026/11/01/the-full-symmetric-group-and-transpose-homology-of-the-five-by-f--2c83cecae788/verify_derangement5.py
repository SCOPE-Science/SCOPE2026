#!/usr/bin/env python3
"""Exact integral chain reduction and equivariant character verification for the 5x5 diagonal-deleted rook complex. Standard library only."""
from collections import Counter, defaultdict
from itertools import permutations
from math import comb

N = 5
P = 101


def build_faces(n=N):
    squares = [(i,j) for i in range(n) for j in range(n) if i != j]
    levels = [[()]]
    def visit(start, rows, cols, chosen):
        if chosen:
            while len(levels) <= len(chosen): levels.append([])
            levels[len(chosen)].append(tuple(chosen))
        for k in range(start, len(squares)):
            i, j = squares[k]
            if rows & (1 << i) or cols & (1 << j): continue
            chosen.append(k)
            visit(k+1, rows | (1 << i), cols | (1 << j), chosen)
            chosen.pop()
    visit(0, 0, 0, [])
    return squares, levels


def boundary_columns(upper, lower):
    index = {face:i for i,face in enumerate(lower)}
    return [{index[face[:j]+face[j+1:]]: (-1)**j
             for j in range(len(face))} for face in upper]


def chain_squared_is_zero(D):
    for d in D:
        if d-1 not in D: continue
        for col in D[d].values():
            v = {}
            for middle, coeff in col.items():
                for lower, c in D[d-1][middle].items():
                    v[lower] = v.get(lower,0) + coeff*c
            assert all(x == 0 for x in v.values()), ('d_squared', d)


def integer_unit_cancellation(levels):
    # All coefficients remain exact Python integers. At each unit pivot the
    # Schur complement eliminates one contractible two-term subcomplex.
    cells = {d:dict(enumerate(level)) for d,level in enumerate(levels,start=-1)}
    indices = {d:{face:k for k,face in faces.items()} for d,faces in cells.items()}
    D = {d:{k:{indices[d-1][f[:j]+f[j+1:]]:(-1)**j for j in range(len(f))}
           for k,f in cells[d].items()} for d in cells if d >= 0}
    chain_squared_is_zero(D)
    R = {d:defaultdict(dict) for d in D}
    for d, cols in D.items():
        for c,vals in cols.items():
            for r,a in vals.items(): R[d][r][c] = a
    pivots = Counter()
    while True:
        candidate = None
        for d in sorted(D,reverse=True):
            for c, entries in D[d].items():
                for r, a in entries.items():
                    if a not in (-1,1): continue
                    score = ((len(entries)-1)*(len(R[d][r])-1),-d,
                             len(entries)+len(R[d][r]),c,r)
                    if candidate is None or score < candidate[0]:
                        candidate = (score,d,c,r,a)
        if candidate is None: break
        _, d, c, r, unit = candidate
        col = D[d][c]
        for cc, coeff in list(R[d][r].items()):
            if cc == c: continue
            multiple = coeff // unit
            assert multiple * unit == coeff
            for rr, val in col.items():
                new = D[d][cc].get(rr,0)-multiple*val
                if new:
                    D[d][cc][rr] = new
                    R[d][rr][cc] = new
                else:
                    D[d][cc].pop(rr,None)
                    R[d][rr].pop(cc,None)
        for rr in list(col): R[d][rr].pop(c,None)
        del D[d][c]
        assert not R[d][r]
        del R[d][r]
        cells[d].pop(c)
        cells[d-1].pop(r)
        if d-1 in D:
            outgoing = D[d-1].pop(r)
            for rr in outgoing: R[d-1][rr].pop(r,None)
        if d+1 in D:
            incoming = R[d+1].pop(c,{})
            for cc in incoming: D[d+1][cc].pop(c,None)
        pivots[d] += 1
    chain_squared_is_zero(D)
    residual = {d:len(c) for d,c in cells.items()}
    nonzero = {d:sum(map(len,D[d].values())) for d in D}
    assert not any(nonzero.values()), nonzero
    assert residual == {-1:0,0:0,1:0,2:1,3:13,4:0}, residual
    assert sum(pivots.values()) == 383, pivots
    return residual, dict(sorted(pivots.items())), nonzero


def mod_reduce(vec,pivots,p=P):
    v={k:a%p for k,a in vec.items() if a%p}
    while v:
        k=min(v)
        if k not in pivots: break
        a=v[k]
        for j,b in pivots[k].items():
            new=(v.get(j,0)-a*b)%p
            if new:v[j]=new
            else:v.pop(j,None)
    return v


def mod_add(vec,pivots,p=P):
    v=mod_reduce(vec,pivots,p)
    if not v:return False
    k=min(v)
    s=pow(v[k],-1,p)
    pivots[k]={j:(a*s)%p for j,a in v.items()}
    return True


def mod_nullspace(cols,p=P):
    image,representatives,solutions={},{},[]
    for ci,col in enumerate(cols):
        v={j:x%p for j,x in col.items() if x%p}
        coeff={ci:1}
        while v:
            k=min(v)
            if k not in image: break
            a=v[k]
            for j,b in image[k].items():
                new=(v.get(j,0)-a*b)%p
                if new:v[j]=new
                else:v.pop(j,None)
            for j,b in representatives[k].items():
                new=(coeff.get(j,0)-a*b)%p
                if new:coeff[j]=new
                else:coeff.pop(j,None)
        if v:
            k=min(v)
            s=pow(v[k],-1,p)
            image[k]={j:(x*s)%p for j,x in v.items()}
            representatives[k]={j:(x*s)%p for j,x in coeff.items()}
        else: solutions.append(coeff)
    return solutions,len(image)


def sign_sort(sequence):
    inversion_count=sum(a>b for i,a in enumerate(sequence) for b in sequence[i+1:])
    return -1 if inversion_count%2 else 1


def cycle_type(sigma):
    visited=set(); lengths=[]
    for i in range(len(sigma)):
        if i in visited:continue
        x=i; length=0
        while x not in visited:
            visited.add(x);length+=1;x=sigma[x]
        lengths.append(length)
    return tuple(sorted(lengths,reverse=True))


def group_characters(squares,levels):
    # Identify the one-dimensional H_2 module by a 101-modular cycle, then
    # use exact signed simplicial Lefschetz traces to determine H_3.
    lower=boundary_columns(levels[3],levels[2])
    upper=boundary_columns(levels[4],levels[3])
    boundaries={}
    for col in upper: mod_add(col,boundaries)
    nullspace, rank = mod_nullspace(lower)
    assert (rank,len(nullspace),len(boundaries)) == (111,209,208)
    enlarged={k:v.copy() for k,v in boundaries.items()}
    reps=[]
    for vec in nullspace:
        if mod_add(vec,enlarged): reps.append(vec)
    assert len(reps)==1
    cycle=reps[0]
    face_index={f:i for i,f in enumerate(levels[3])}
    square_index={s:i for i,s in enumerate(squares)}
    class_values=defaultdict(set)
    checked=0
    for flipped in (False,True):
        for sigma in permutations(range(N)):
            image_of_square=[square_index[(sigma[j],sigma[i]) if flipped
                                           else (sigma[i],sigma[j])]
                             for i,j in squares]
            chi=-1  # Reduced augmented empty simplex.
            for d,faces in enumerate(levels[1:]):
                fixed_signed=0
                for face in faces:
                    image=tuple(image_of_square[k] for k in face)
                    if tuple(sorted(image))==face:
                        fixed_signed+=sign_sort(image)
                chi+=(-1)**d*fixed_signed
            im_cycle={}
            for k,a in cycle.items():
                image=tuple(image_of_square[j] for j in levels[3][k])
                target=face_index[tuple(sorted(image))]
                im_cycle[target]=(im_cycle.get(target,0)+a*sign_sort(image))%P
            expected_h2=-1 if flipped else 1
            difference={j:(im_cycle.get(j,0)-expected_h2*cycle.get(j,0))%P
                        for j in set(im_cycle)|set(cycle)}
            assert not mod_reduce(difference,boundaries),('H2action',flipped,sigma)
            fixed=sum(i==sigma[i] for i in range(N))
            twos=cycle_type(sigma).count(2)
            sigma_sign=sign_sort(sigma)
            standard=fixed-1
            two_subset=comb(fixed,2)+twos-fixed
            expected_h3=standard*(1+(-1 if flipped else 1)*sigma_sign)+two_subset
            actual_h3=expected_h2-chi
            assert actual_h3==expected_h3, ('character', flipped,sigma,actual_h3,expected_h3)
            class_values[(int(flipped),cycle_type(sigma))].add((expected_h2,actual_h3))
            checked+=1
    assert checked==240
    assert all(len(a)==1 for a in class_values.values())
    return {k:next(iter(v)) for k,v in sorted(class_values.items())},checked


def main():
    squares,levels=build_faces()
    counts=[len(a) for a in levels]
    assert counts==[1,20,130,320,265,44],counts
    residual,pivots,nonzero=integer_unit_cancellation(levels)
    classes,nchecked=group_characters(squares,levels)
    assert classes[(0,(1,1,1,1,1))]==(1,13)
    assert classes[(1,(1,1,1,1,1))]==(-1,5)
    print('face_counts='+repr(counts))
    print('unit_pivots='+repr(pivots)+'; total='+str(sum(pivots.values())))
    print('remaining_cells='+repr(residual)+'; remaining_differential_entries='+repr(nonzero))
    for key,value in classes.items():
        print('layer_swap='+str(key[0])+'; cycle_type='+repr(key[1])+'; (trace_H2,trace_H3)='+repr(value))
    print('automorphisms_checked='+str(nchecked))
    print('VERIFY_OK')

if __name__=='__main__':main()
