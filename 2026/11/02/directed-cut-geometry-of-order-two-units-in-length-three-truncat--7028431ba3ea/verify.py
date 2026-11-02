#!/usr/bin/env python3
"""Independent finite-field checks of order-two unit counts in length-three truncated quiver algebras.

Each point is checked by multiplying a full path-basis element by itself;
finite checks are corroboration, not a proof of the unrestricted theorem.
"""
from itertools import product

def mul(x, y, q):
    if q == 2:
        return x & y
    poly = {4: 0b111, 8: 0b1011}[q]
    bits = q.bit_length()-1
    raw = 0
    for i in range(bits):
        if (y >> i) & 1:
            raw ^= x << i
    for d in range(2*bits-2, bits-1, -1):
        if (raw >> d) & 1:
            raw ^= poly << (d-bits)
    return raw

def path_algebra(n, arrows):
    paths = [()] # sentinel; actual basis assembled below
    basis = [(v, v, ()) for v in range(n)]
    basis += [(s,t,(a,)) for a,(s,t) in enumerate(arrows)]
    pairs = [(i,j) for i,(_,t) in enumerate(arrows)
                   for j,(s,_) in enumerate(arrows) if t==s]
    basis += [(arrows[i][0],arrows[j][1],(i,j)) for i,j in pairs]
    index = {(s,t,p):i for i,(s,t,p) in enumerate(basis)}
    table = []
    for s,t,p in basis:
        row = []
        for u,v,r in basis:
            if t != u or len(p)+len(r)>2:
                row.append(-1)
            else:
                row.append(index[(s,v,p+r)])
        table.append(row)
    return basis, pairs, table

def finite_census(n, arrows, q):
    basis,pairs,prod = path_algebra(n,arrows)
    nrad = len(basis)-n
    one = tuple([1]*n+[0]*nrad)
    observed=0
    for v in product(range(q),repeat=nrad):
        coeff=one[:n]+v
        sq=[0]*len(basis)
        for i,x in enumerate(coeff):
            if not x: continue
            for j,y in enumerate(coeff):
                k=prod[i][j]
                if k>=0 and y:
                    sq[k]^=mul(x,y,q)
        observed += (tuple(sq)==one)
    permitted=0
    for mask in range(1<<len(arrows)):
        supports=[i for i in range(len(arrows)) if mask>>i&1]
        if all(arrows[i][1]!=arrows[j][0] for i in supports for j in supports):
            permitted+=(q-1)**len(supports)
    predicted=q**len(pairs)*permitted
    if observed!=predicted:
        raise AssertionError((n,arrows,q,observed,predicted))
    return observed, len(basis), len(pairs)

def geometry_check(n,arrows):
    m=len(arrows)
    indep = [s for s in range(1<<m)
             if all(arrows[i][1]!=arrows[j][0]
                    for i in range(m) for j in range(m)
                    if (s>>i)&1 and (s>>j)&1)]
    mx = max((s.bit_count() for s in indep), default=0)
    directed_cut = max((sum((mask>>u)&1 and not ((mask>>v)&1) for u,v in arrows)
                        for mask in range(1<<n)),default=0)
    if mx!=directed_cut: raise AssertionError((n,arrows,mx,directed_cut))
    maximal = [s for s in indep if not any(s!=t and (s&t)==s for t in indep)]
    max_cut_sets = {sum(1<<a for a,(u,v) in enumerate(arrows)
                        if (mask>>u)&1 and not ((mask>>v)&1))
                    for mask in range(1<<n)}
    if not all(s in max_cut_sets for s in maximal):
        raise AssertionError(('maximal not a cut',n,arrows,maximal))
    return mx,len(maximal)

def main():
    cases=[
        ('empty',1,[],[2,4,8]),
        ('path2',3,[(0,1),(1,2)],[2,4,8]),
        ('path3',4,[(0,1),(1,2),(2,3)],[2,4]),
        ('path4',5,[(0,1),(1,2),(2,3),(3,4)],[2,4]),
        ('triangle',3,[(0,1),(1,2),(2,0)],[2,4]),
        ('parallel',3,[(0,1),(0,1),(1,2)],[2,4]),
        ('one_loop',1,[(0,0)],[2,4,8]),
        ('two_loops',1,[(0,0),(0,0)],[2,4]),
        ('two_cycle',2,[(0,1),(1,0)],[2,4]),
        ('source_fork',4,[(0,1),(0,2),(2,3)],[2,4]),
        ('disjoint',4,[(0,1),(2,3)],[2,4]),
        ('loop_out',2,[(0,0),(0,1)],[2,4]),
    ]
    total=0
    for title,n,arrows,fields in cases:
        alpha,ncomp=geometry_check(n,arrows)
        for q in fields:
            count,dim,np=finite_census(n,arrows,q)
            print(title,q,'units_order_dividing_two',count,'basis',dim,
                  'length2',np,'max_cut',alpha,'components',ncomp)
            total+=1
    print('CUBIC_QUIVER_INVOLUTION_OK',total,'complete finite-field multiplications',len(cases),'geometry comparisons')
if __name__=='__main__':main()
