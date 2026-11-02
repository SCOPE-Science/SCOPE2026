"""Independent finite checks for point-block incidence of affine resolvable 2-designs.

The infinite statement is proved separately. This file checks exact pair-extension
support on small affine spaces and a non-geometric Hadamard design.
"""
from itertools import product
from collections import defaultdict

def geometry(d,q):
    if not all(q % p for p in range(2,int(q**0.5)+1)):
        raise ValueError('prime q required')
    pts=list(product(range(q), repeat=d))
    dirs=set()
    for a in product(range(q),repeat=d):
        if any(a):
            lead=next(x for x in a if x)
            dirs.add(tuple(z*pow(lead,-1,q)%q for z in a))
    blocks=[]
    for a in sorted(dirs):
        for t in range(q):
            blocks.append(frozenset(i for i,p in enumerate(pts) if sum(v*w for v,w in zip(a,p))%q==t))
    return (len(pts),blocks,q,f'AG({d},{q}) hyperplanes')

def hadamard12():
    q=11
    chi=lambda x: 0 if x%q==0 else (1 if pow(x%q,(q-1)//2,q)==1 else -1)
    h=[[1]*12]
    for i in range(q):
        h.append([1]+[-1 if i==j else chi(i-j) for j in range(q)])
    assert all(sum(a*b for a,b in zip(h[i],h[j]))==(12 if i==j else 0)
               for i in range(12) for j in range(12))
    blocks=[]
    for row in h[1:]:
        for s in (+1,-1):
            blocks.append(frozenset(i for i,v in enumerate(row) if v==s))
    return (12,blocks,2,'Hadamard 2-(12,6,5)')

def pair_color(a,b,nb,blocks):
    # points are 0..nb-1 and blocks are nb..nb+b-1
    pa=a<nb; pb=b<nb
    if pa and pb:
        return 'PP=' if a==b else 'PP!='
    if not pa and not pb:
        if a==b:return 'BB='
        return 'BB_disj' if not (blocks[a-nb]&blocks[b-nb]) else 'BB_cross'
    if pa:
        return 'PB_I' if a in blocks[b-nb] else 'PB_N'
    return 'BP_I' if b in blocks[a-nb] else 'BP_N'

def check(design):
    nb,blocks,q,label=design
    blocksize=len(blocks[0]);assert all(len(b)==blocksize for b in blocks)
    cls=defaultdict(list)
    for a in range(len(blocks)):
        for b in range(a+1,len(blocks)):
            cls[len(blocks[a]&blocks[b])].append((a,b))
    assert set(cls)=={0,blocksize//q}  # affine: cross-class intersection is constant
    lambdas={sum(a in B and b in B for B in blocks) for a in range(nb) for b in range(a+1,nb)}
    assert len(lambdas)==1 and next(iter(lambdas))>=1
    n=nb+len(blocks)
    colors={(a,b):pair_color(a,b,nb,blocks) for a in range(n) for b in range(n)}
    supports=defaultdict(set)
    for a in range(n):
        for b in range(n):
            supports[colors[a,b]].add(frozenset((colors[a,z],colors[z,b]) for z in range(n)))
    assert len(supports)==9 and all(len(v)==1 for v in supports.values()), (label, {k:len(v) for k,v in supports.items()})
    table={k:next(iter(v)) for k,v in supports.items()}
    cover=any(len(A|B)==nb and A!=B for A in blocks for B in blocks)
    assert cover==(q==2)
    print(label, 'points',nb,'blocks',len(blocks),'pair-intersections',sorted(cls),
          'lambda',next(iter(lambdas)),'pair extension colors',len(table),
          'two-block-cover',cover)
    return table

def main():
    choices=[geometry(2,2),geometry(3,2),geometry(4,2),hadamard12(),
             geometry(2,3),geometry(3,3),geometry(2,5)]
    tables={}
    for D in choices:
        table=check(D)
        branch=('binary' if D[2]==2 else 'nonbinary')
        if branch in tables: assert table==tables[branch],(D[3],branch)
        else:tables[branch]=table
    assert tables['binary']!=tables['nonbinary']
    print('STABLE PAIR-EXTENSION SUPPORT VERIFIED ON ALL SEVEN DESIGNS')
    print('BINARY VS NONBINARY SUPPORT TABLES DIFFER')
    for branch,table in tables.items():
        print('class',branch)
        for k in sorted(table):
            print(' ',k, ':', ','.join(f'{a}/{b}' for a,b in sorted(table[k])))
if __name__=='__main__':main()
