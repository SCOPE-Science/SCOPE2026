"""Finite exhaustive tests for the unary classicality-obstruction theorem.

Stand-alone Python 3, standard library only. Finite checks corroborate but do
not replace the unrestricted constructive mathematical proof.
"""
from itertools import product


def graph_check(parents):
    """Check every set of positive/negative unary literals on a finite core forest."""
    n = len(parents)
    assert all(-1 <= p < i for i, p in enumerate(parents))
    full = 0
    literals = [0] * (2*n)
    for assignment in range(1 << (2*n)):
        t = [(assignment >> (2*i)) & 1 for i in range(n)]
        f = [(assignment >> (2*i+1)) & 1 for i in range(n)]
        if any(p >= 0 and t[i] and t[p]+f[p] != 1 for i,p in enumerate(parents)):
            continue
        mask = 1 << assignment
        full |= mask
        for i in range(n):
            if t[i]: literals[2*i] |= mask
            if f[i]: literals[2*i+1] |= mask
    checked = 0
    for selection in range(1 << (2*n)):
        surviving = full
        required = [bool(selection & (1 << b)) for b in range(2*n)]
        for b, val in enumerate(required):
            if val: surviving &= literals[b]
        forbidden = any(par >= 0 and required[2*i]
                        and required[2*par] and required[2*par+1]
                        for i, par in enumerate(parents))
        assert (surviving == 0) == forbidden, (parents, selection)
        checked += 1
    return checked


def all_ordered_forests(n):
    for parents in product(*[range(-1,i) for i in range(n)]):
        yield parents


def syntax_checks():
    # Formula represented by a string of unary signs, outermost sign first.
    # 'C' means circle, 'N' negation, 'P' primitive variable.
    formulas = ['P','NP','NNP','NNNP','CP','CNP','CNNP',
                'NCP','NNCP','CCP','NCCP']
    def normalize(expr):
        parity=0
        while expr.startswith('N'):
            parity ^= 1
            expr=expr[1:]
        return expr, parity
    cores = {'P'}
    def all_cores_of(expr):
        expr,_ = normalize(expr)
        yield expr
        if expr.startswith('C'):
            yield from all_cores_of(expr[1:])
    for formula in formulas:
        cores.update(all_cores_of(formula))
    cores=sorted(cores, key=lambda s:(len(s),s))
    index={c:i for i,c in enumerate(cores)}
    parents=[-1 if not c.startswith('C') else index[normalize(c[1:])[0]] for c in cores]
    # Every subset of the actual list of distinct syntactic formulas.
    n=len(cores)
    legit=[]
    for assignment in range(1 << (2*n)):
        t=[(assignment>>(2*i))&1 for i in range(n)]
        f=[(assignment>>(2*i+1))&1 for i in range(n)]
        if any(p>=0 and t[i] and t[p]+f[p]!=1 for i,p in enumerate(parents)):
            continue
        legit.append(assignment)
    assert legit
    for select in range(1 << len(formulas)):
        requirements=[set() for _ in cores]
        for j,formula in enumerate(formulas):
            if (select>>j)&1:
                core,parity=normalize(formula)
                requirements[index[core]].add(parity)
        pattern_bad=any(0 in requirements[i] and {0,1}.issubset(requirements[p])
                       for i,p in enumerate(parents) if p>=0)
        satisfiable=False
        for assignment in legit:
            if all(((assignment >> (2*i+parity))&1) for i,rs in enumerate(requirements)
                   for parity in rs):
                satisfiable=True
                break
        assert satisfiable != pattern_bad, (select, requirements)
    # No replacement of circle(NNP) by circle(P): both truth bits independent.
    assert normalize('CNNP')[0] != normalize('CP')[0]
    return len(formulas), len(cores), 1 << len(formulas)


def main():
    graphs = 0
    tested_sets = 0
    for n in range(1,6):
        for parent in all_ordered_forests(n):
            tested_sets += graph_check(parent)
            graphs += 1
    print('CORE_FORESTS', graphs, 'SUBSETS', tested_sets)
    print('SYNTAX_CASE', syntax_checks())
    print('ALL_CHECKS_OK')

if __name__=='__main__':
    main()
