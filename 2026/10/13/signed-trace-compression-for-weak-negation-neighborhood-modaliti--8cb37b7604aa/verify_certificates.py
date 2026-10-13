#!/usr/bin/env python3
"""Independent finite signed-truth-table certificate tests for modal CLoN.

Randomized checking cannot establish any infinite theorem. Symbolic proofs
of the certificate equivalence and the classical hardness translation accompany
this file.
"""
import random
from verify_polarity import generate, family, evaluate, OPS

def certificate_ok(nodes,cols,n):
    allmask=(1<<n)-1
    for node in nodes:
        k=node[0]; p=cols[node][0]
        if k=='not' and p!=cols[node[1]][1]: return False
        if k in ('and','or','imp'):
            a,b=(cols[c][0] for c in node[1:])
            expected={'and':a&b,'or':a|b,'imp':(allmask^a)|b}[k]
            if p!=expected: return False
    modal=[node for node in nodes if node[0] in OPS]
    for a in modal:
        for b in modal:
            if a[0]!=b[0]: continue
            for j in range(2):
                if cols[a[1]][j]==cols[b[1]][j] and cols[a][j]!=cols[b][j]:
                    return False
    return True

def check_hardness(g,fbit):
    k=g[0]
    if k=='p': return g[1]
    if k=='not':return not check_hardness(g[1],fbit)
    if k=='and':return check_hardness(g[1],fbit) and check_hardness(g[2],fbit)
    if k=='or':return check_hardness(g[1],fbit) or check_hardness(g[2],fbit)

def tr_eval(g,values,f):
    k=g[0]
    if k=='p':return values[g[1]]
    if k=='not':return (not tr_eval(g[1],values,f)) or f
    if k=='and':return tr_eval(g[1],values,f) and tr_eval(g[2],values,f)
    if k=='or':return tr_eval(g[1],values,f) or tr_eval(g[2],values,f)

def generate_bool(rng,sz):
    pool=[('p',str(i)) for i in range(4)]
    for _ in range(sz):
        k=rng.choice(['not','and','or']);pool.append((k,rng.choice(pool)) if k=='not' else (k,rng.choice(pool),rng.choice(pool)))
    return pool[-1]

def boolval(g,v):
    k=g[0]
    if k=='p':return v[g[1]]
    if k=='not':return not boolval(g[1],v)
    if k=='and':return boolval(g[1],v) and boolval(g[2],v)
    if k=='or':return boolval(g[1],v) or boolval(g[2],v)

def main():
    rng=random.Random(83491)
    for i in range(1500):
        n=rng.randrange(1,8)
        formula=generate(rng,rng.randrange(3,26))
        nodes=family(formula)
        values,_=evaluate(nodes,n,rng)
        assert certificate_ok(nodes,values,n)
        # Every extensionality violation must be rejected.
        modal=[a for a in nodes if a[0] in OPS]
        for a in modal:
            for b in modal:
                if a!=b and a[0]==b[0] and a[1]!=b and values[a[1]][0]==values[b[1]][0]:
                    modified=values.copy();modified[b]=(values[b][0] ^ 1,values[b][1])
                    if modified[a][0]!=modified[b][0]:
                        assert not certificate_ok(nodes,modified,n)
                    break
    for i in range(600):
        g=generate_bool(rng,rng.randrange(2,30))
        for bitpattern in range(16):
            v={str(j):bool((bitpattern>>j)&1) for j in range(4)}
            expected=boolval(g,v)
            assert tr_eval(g,v,False)==expected
            assert (tr_eval(g,v,True) or True)
            assert (tr_eval(g,v,False) or False)==expected
    print('VERIFY_OK certificates=1500 boolean_translation_instances=9600')
if __name__=='__main__':main()
