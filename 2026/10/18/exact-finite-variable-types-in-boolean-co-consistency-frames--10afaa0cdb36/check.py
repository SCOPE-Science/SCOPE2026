"""Finite replay checks for color compression in co-consistency models.

This script is supplementary: it tests finite instances of a general proof.
"""
from itertools import product, combinations
from random import Random


def nonempty_masks(n):
    return range(1, 1 << n)


def eval_ast(phi, worlds, value_sets):
    # Returns a set of bitmask worlds satisfying the formula.
    op = phi[0]
    if op == 'atom':
        return {a for a in worlds if not (a & ~value_sets[phi[1]])}
    if op == 'top':
        return set(worlds)
    if op == 'not':
        return set(worlds) - eval_ast(phi[1], worlds, value_sets)
    if op == 'and':
        return eval_ast(phi[1], worlds, value_sets) & eval_ast(phi[2], worlds, value_sets)
    if op == 'or':
        return eval_ast(phi[1], worlds, value_sets) | eval_ast(phi[2], worlds, value_sets)
    if op == 'dia':
        t = eval_ast(phi[1], worlds, value_sets)
        return {a for a in worlds if any(a & b for b in t)}
    if op == 'box':
        t = eval_ast(phi[1], worlds, value_sets)
        return {a for a in worlds if all((not(a & b)) or (b in t) for b in worlds)}
    raise ValueError(op)


def colors_of_atoms(n, value_sets):
    k = len(value_sets)
    return [sum(((value_sets[i] >> j) & 1) << i for i in range(k)) for j in range(n)]


def compression(n, value_sets):
    colors = colors_of_atoms(n, value_sets)
    types = sorted(set(colors))
    relabel = {t:i for i,t in enumerate(types)}
    induced = tuple(sum((t >> i & 1) << j for j,t in enumerate(types)) for i in range(len(value_sets)))
    def f(a):
        return __import__("functools").reduce(lambda acc,j: acc | (1 << relabel[colors[j]]), (j for j in range(n) if (a >> j)&1), 0)
    return types, induced, f


def random_formula(rng, k, depth):
    if depth == 0 or rng.randrange(4)==0:
        return ('atom',rng.randrange(k)) if rng.randrange(3) else ('top',)
    op=rng.choice(['not','and','or','dia','box'])
    if op in ('and','or'):
        return (op,random_formula(rng,k,depth-1),random_formula(rng,k,depth-1))
    return (op,random_formula(rng,k,depth-1))


def delta(t,k):
    f=('top',)
    for i in range(k):
        term=('atom',i) if (t >> i)&1 else ('not',('dia',('atom',i)))
        f=('and',f,term)
    return f


def separator(types,k):
    p=('top',)
    for t in types:
        p=('and',p,('dia',('dia',delta(t,k))))
    return ('not',p)


def test_compression():
    rng=Random(20261013)
    checks=0
    for k in range(1,4):
      for n in range(1,5):
        assignments=list(product(range(1<<n),repeat=k))
        if len(assignments)>200:
            assignments=[assignments[rng.randrange(len(assignments))] for _ in range(200)]
        formulas=[('atom',i) for i in range(k)]+[random_formula(rng,k,rng.randrange(1,5)) for _ in range(35)]
        for values in assignments:
            types,compact_values,f=compression(n,values)
            ws=list(nonempty_masks(n)); cws=list(nonempty_masks(len(types)))
            assert set(f(a) for a in ws)==set(cws)
            for a in ws:
              for b in cws:
                if f(a)&b:
                  assert any((a&v) and f(v)==b for v in ws)
            for phi in formulas:
              src=eval_ast(phi,ws,values)
              dst=eval_ast(phi,cws,compact_values)
              assert all((a in src)==(f(a) in dst) for a in ws), (k,n,values,phi)
              checks+=len(ws)
    return checks


def test_separators():
    checks=0
    for k in range(1,4):
      for r in range(2,min((1<<k),5)+1):
        types=tuple(range(r))
        phi=separator(types,k)
        for n in range(1,min(r+1,5)):
          for values in product(range(1<<n),repeat=k):
            result=eval_ast(phi,list(nonempty_masks(n)),values)
            if n < r:
                assert len(result)==(1<<n)-1
            else:
                cols=colors_of_atoms(n,values)
                expected = len(set(types)&set(cols))<r
                assert (len(result)==(1<<n)-1)==expected
            checks+=1
    return checks

if __name__=='__main__':
    c=test_compression()
    s=test_separators()
    print('PASS color compression, individual formula-world comparisons:',c)
    print('PASS separator tests:',s)


def test_type_signatures():
    count=0
    for k in range(1,4):
        for n in range(1,5):
            if n*k>10: continue
            signatures=set()
            for values in product(range(1<<n),repeat=k):
                ws=list(nonempty_masks(n))
                atom_colors=colors_of_atoms(n,values)
                T=frozenset(atom_colors)
                d={t:eval_ast(delta(t,k),ws,values) for t in range(1<<k)}
                present={t:eval_ast(('dia',delta(t,k)),ws,values) for t in range(1<<k)}
                global_presence={t:eval_ast(('dia',('dia',delta(t,k))),ws,values) for t in range(1<<k)}
                for a in ws:
                    S=frozenset(atom_colors[j] for j in range(n) if (a>>j)&1)
                    for t in range(1<<k):
                        assert (a in d[t]) == (S=={t})
                        assert (a in present[t]) == (t in S)
                        assert (a in global_presence[t]) == (t in T)
                    signatures.add((T,S))
                    count+=1
            m=1<<k
            expected=sum(__import__('math').comb(m,j)*((1<<j)-1) for j in range(1,min(n,m)+1))
            assert len(signatures)==expected, (n,k,len(signatures),expected)
    return count

if __name__=='__main__':
    print('PASS exact type signatures:',test_type_signatures())
