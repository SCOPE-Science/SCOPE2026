#!/usr/bin/env python3
"""Reproduce two complete Sp(6,2) censuses and independently certify 18 witnesses."""
import csv, pathlib, subprocess, tempfile
P=pathlib.Path(__file__).resolve().parent
expect=[]
with (P/'counts.csv').open(newline='',encoding='utf-8') as f:
    expect=[tuple(int(x) for x in z.values()) for z in csv.DictReader(f)]
assert len(expect)==18 and sum(n for r,b,n in expect)==1451520

def B(x,y):
    return sum((((x>>i)&1)&((y>>(i+1))&1))^((((x>>(i+1))&1)&((y>>i)&1))) for i in (0,2,4))%2

def Q(x):
    return sum(((x>>i)&1)&((x>>(i+1))&1) for i in (0,2,4))%2

def rank(xs):
    rows=list(xs);k=0
    for col in range(6):
        p=next((p for p in range(k,6) if (rows[p]>>col)&1),None)
        if p is None: continue
        rows[k],rows[p]=rows[p],rows[k]
        for j in range(6):
            if j!=k and ((rows[j]>>col)&1):rows[j]^=rows[k]
        k+=1
    return k

with (P/'witnesses.csv').open(newline='',encoding='utf-8') as f:
    z=list(csv.DictReader(f))
assert len(z)==18
for row in z:
    r,b,n=int(row['fixed_two_torsion_rank']),int(row['rational_bitangents']),int(row['matrix_multiplicity'])
    code=int(row['matrix_columns_hex'],16)
    c=[(code>>(6*i))&63 for i in range(6)]
    def M(x):
        return __import__('functools').reduce(lambda a,j:a^(c[j] if (x>>j)&1 else 0),range(6),0)
    assert all(B(M(x),M(y))==B(x,y) for x in range(64) for y in range(64))
    assert 6-rank([M(1<<j)^(1<<j) for j in range(6)])==r
    assert sum(Q(t)==1 and all(Q(M(x))^B(t,M(x))==Q(x)^B(t,x) for x in range(64)) for t in range(64))==b
    assert (r,b,n) in expect
print('INDEPENDENT_ALL_64_VECTORS_WITNESSES_OK',len(z))
with tempfile.TemporaryDirectory(prefix='bitangent_symplectic_') as t:
    a=pathlib.Path(t)/'basis';b=pathlib.Path(t)/'bfs'
    for src,out in [('symplectic_bases.c',a),('transvections_bfs.c',b)]:
        subprocess.run(['cc','-std=c11','-O3','-o',str(out),str(P/src)],check=True)
    atext=subprocess.check_output([str(a)],text=True)
    btext=subprocess.check_output([str(b)],text=True)
    assert 'TOTAL=1451520 ODD=28' in atext
    assert 'GROUP_SIZE=1451520' in btext
    at=[tuple(map(int,line.split(','))) for line in atext.splitlines()[2:] if line.strip()]
    bt=[tuple(map(int,line.split(',')[:3])) for line in btext.splitlines()[1:] if line.strip()]
    assert at==expect
    assert bt==expect
    print('TWO_INDEPENDENT_FULL_GROUP_ENUMERATIONS_AGREE',len(at),sum(n for _,_,n in at))
print('VERIFY_OK')
