"""Direct FO^3 finite-type refinement on ternary quandle operation graphs.
Constructs full truth tables and quantifier projections, not anharmonic formulas.
Finite checks supplement but do not replace the theorem's infinite proof.
"""
from itertools import product
from check_patterns import Field

SAMPLES=[
 ('T3_3',3,2,1),('T3_9',3,2,2),
 ('Hhalf_5',5,3,1),('Hhalf_7',7,4,1),
 ('Htwo_5',5,2,1),('Htwo_7',7,2,1),
 ('Hminus_5',5,4,1),('Hminus_7',7,6,1),
 ('E_4',4,2,1),('E_7',7,3,1),
 ('G_8',8,2,1),('G_9',9,3,1),
 ('G_11',11,4,1),('G_13',13,3,1),
 ('E2_7',7,5,1),('G2_9',9,4,1)
]
def construct(q,t,d):
    specs={4:(2,[1,1,1]),8:(2,[1,1,0,1]),9:(3,[1,0,1])}
    f=Field(*specs[q]) if q in specs else Field(q)
    pts=list(product(range(q),repeat=d)); pos={x:i for i,x in enumerate(pts)}
    op=[]
    for x in pts:
        op.append([])
        for y in pts:
            out=tuple(f.add(f.mul(f.sub(1,t),xi),f.mul(t,yi)) for xi,yi in zip(x,y))
            op[-1].append(pos[out])
    return len(pts),op

def classify(models,rounds=4):
    tuples=[list(product(range(n),repeat=3)) for n,op in models]
    atom=[]
    for (n,op),ts in zip(models,tuples):
        atoms=[]
        for a in ts:
            eq=tuple(int(a[i]==a[j]) for i in range(3) for j in range(i+1,3))
            rel=tuple(int(op[a[i]][a[j]]==a[k]) for i in range(3) for j in range(3) for k in range(3))
            atoms.append((eq,rel))
        atom.append(atoms)
    def colors(sigs):
        table={};ret=[]
        for group in sigs:
            arr=[]
            for sig in group:
                if sig not in table:table[sig]=len(table)
                arr.append(table[sig])
            ret.append(arr)
        return ret,len(table)
    curr,ntypes=colors(atom)
    for r in range(rounds+1):
        fingerprints=[frozenset(c) for c in curr]
        num=len(set(fingerprints))
        print(f'rank={r} global_tuple_colors={ntypes} distinct_realized_color_sets={num}')
        if r==rounds:return fingerprints
        more=[]
        for k,((n,op),ts,col) in enumerate(zip(models,tuples,curr)):
            index={a:i for i,a in enumerate(ts)}
            signatures=[]
            for a,c in zip(ts,col):
                sets=[]
                for j in range(3):
                    nxt=[]
                    for val in range(n):
                        tmp=list(a);tmp[j]=val
                        nxt.append(col[index[tuple(tmp)]])
                    sets.append(frozenset(nxt))
                signatures.append((c,*sets))
            more.append(signatures)
        curr,ntypes=colors(more)

if __name__=='__main__':
    mods=[construct(q,t,d) for name,q,t,d in SAMPLES]
    sigs=classify(mods,rounds=4)
    groups={}
    for (name,q,t,d),sig in zip(SAMPLES,sigs):groups.setdefault(sig,[]).append(name)
    assert len(groups)==12,[(len(v),v) for v in groups.values()]
    expected_pairs=[('G_9','G_11'),('G_9','G_13'),('G_9','G2_9'),('E_7','E2_7')]
    ss=dict(zip([row[0] for row in SAMPLES],sigs))
    assert all(ss[a]==ss[b] for a,b in expected_pairs)
    # Explicit width-four separator: R(x,y,z) & R(z,y,w) & R(x,w,y).
    # With distinct x,y its scalar equation is (t-1)(t*t-t-1)=0.
    def separator(q,t,d):
        n,op=construct(q,t,d)
        for x in range(n):
            for y in range(n):
                if x==y:continue
                z=op[x][y];w=op[z][y]
                if len({x,y,z,w})==4 and op[x][w]==y:return True
        return False
    assert separator(11,4,1) and not separator(9,3,1)
    print('PASS: 12 FO^3 types and all expected inter-instance equalities')
    print('PASS: four-variable sentence separates generic-outside instances of orders 9 and 11')
