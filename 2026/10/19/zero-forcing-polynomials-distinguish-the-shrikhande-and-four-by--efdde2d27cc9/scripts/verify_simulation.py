"""Exact standard zero forcing census on the two order-sixteen strongly regular graphs."""
from itertools import product
from collections import Counter
from pathlib import Path
import sys

P=[(a,b) for a in range(4) for b in range(4)]

def graph(kind):
    A=[]
    for a,b in P:
        if kind=='shrikhande':
            D={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            A.append(tuple(i for i,(c,d) in enumerate(P) if ((c-a)%4,(d-b)%4) in D))
        elif kind=='rook':
            A.append(tuple(i for i,(c,d) in enumerate(P) if ((c==a) != (d==b))))
        else: raise ValueError(kind)
    assert all(len(v)==6 for v in A)
    assert all(len(set(A[a])&set(A[b]))==2 for a in range(16) for b in range(16) if a!=b)
    return A

def closure(blue,adj):
    time=0
    while True:
        to_force=set()
        for v in range(16):
            if blue&(1<<v):
                w=[u for u in adj[v] if not(blue&(1<<u))]
                if len(w)==1: to_force.add(w[0])
        if not to_force: return blue,time
        for u in to_force:blue|=1<<u
        time+=1

def census(adj):
    coeff=Counter();minimal=Counter();propagation=Counter();successful=[]
    for S in range(1<<16):
        reached,t=closure(S,adj)
        if reached==0xffff:
            k=S.bit_count();coeff[k]+=1;propagation[(k,t)]+=1;successful.append(S)
    good=set(successful)
    for S in successful:
        if all((S^(1<<v)) not in good for v in range(16) if S&(1<<v)):
            minimal[S.bit_count()]+=1
    signature=0xcbf29ce484222325
    for S in successful:
        for j in range(4):
            signature^=(S>>(8*j))&255
            signature=(signature*1099511628211)&((1<<64)-1)
    return coeff,minimal,propagation,signature,good

def verify():
    expected={
      'shrikhande':{10:3616,11:3600,12:1760,13:560,14:120,15:16,16:1},
      'rook':{10:3456,11:3504,12:1760,13:560,14:120,15:16,16:1}}
    groups={}
    for kind in ('shrikhande','rook'):
        A=graph(kind)
        c,m,t,sig,good=census(A)
        assert dict(c)==expected[kind] and dict(m)=={10:c[10]}
        groups[kind]=(c,m,t,sig,good)
        print('SIMULATION_OK',kind,'polynomial',sorted(c.items()),'minimal',dict(m),
              'min_time',{t0:v for (k,t0),v in t.items() if k==10},'FNV64',f'{sig:016x}')
    path=Path(__file__).resolve().parent.parent/'certificates'/'forcing_truth_tables.bin'
    tables=[]
    for kind in ('shrikhande','rook'):
        good=groups[kind][4]
        tables.append(bytes(sum((1<<j) if (8*i+j) in good else 0 for j in range(8))
                            for i in range(8192)))
    if '--write-certificate' in sys.argv:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(b''.join(tables))
    assert path.read_bytes()==b''.join(tables)
    print('VERIFY_TRUTH_TABLE_OK every_one_of_131072_graph_mask_decisions_matches_exact_binary_certificate')
    assert groups['shrikhande'][0][10]-groups['rook'][0][10]==160
    assert groups['shrikhande'][0][11]-groups['rook'][0][11]==96
    print('VERIFY_SIMULATION_OK cospectral_zero_forcing_polynomial_difference=160z10+96z11')
    return groups

if __name__=='__main__':verify()
