#!/usr/bin/env python3
"""Direct finite tests for the one-relation equality-free disjoint-union example."""
import itertools
import random


def relation(n, edges):
    return (n, frozenset(edges))


def R(M, x, y):
    return (x, y) in M[1]


def P(M, x):
    n, _ = M
    return any(R(M, x, y) and not R(M, y, y) for y in range(n))


def Q(M, x):
    return R(M, x, x) and not P(M, x)


def phi(M):
    n, _ = M
    ps = [x for x in range(n) if P(M, x)]
    qs = [x for x in range(n) if Q(M, x)]
    return bool(ps) and (
        all(R(M, x, y) for x in qs for y in qs)
        or any(not R(M, x, y) for x in ps for y in ps)
    )


def disjoint_union(A, B):
    return relation(A[0] + B[0], A[1] | {(x + A[0], y + A[0]) for x, y in B[1]})


def models(n):
    edges = [(x, y) for x in range(n) for y in range(n)]
    for bits in range(1 << (n*n)):
        yield relation(n, [e for i, e in enumerate(edges) if bits >> i & 1])


def check_preservation():
    valid = {n: [M for M in models(n) if phi(M)] for n in (1, 2, 3)}
    cases = 0
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for a in valid[i]:
                for b in valid[j]:
                    cases += 1
                    assert phi(disjoint_union(a, b)), (a, b)
    return cases, {n:len(v) for n,v in valid.items()}


def evaluate(ast, M, env):
    op = ast[0]
    if op == 'r': return R(M, env[ast[1]], env[ast[2]])
    if op == '!r': return not R(M, env[ast[1]], env[ast[2]])
    if op == '&': return evaluate(ast[1], M, env) and evaluate(ast[2], M, env)
    if op == '|': return evaluate(ast[1], M, env) or evaluate(ast[2], M, env)
    if op == 'ex':
        return any(evaluate(ast[2], M, env | {ast[1]:v}) for v in range(M[0]))
    if op == 'allf':
        z, y = ast[1:3]
        return all(not R(M, env[z], v) or evaluate(ast[3], M, env | {y:v})
                   for v in range(M[0]))
    if op == 'allb':
        z, y = ast[1:3]
        return all(not R(M, v, env[z]) or evaluate(ast[3], M, env | {y:v})
                   for v in range(M[0]))
    raise RuntimeError(op)


def random_ast(rng, depth=0, vars=('x',)):
    if depth >= 4 or rng.random() < 0.28:
        return (rng.choice(('r','!r')), rng.choice(vars), rng.choice(vars))
    op = rng.choice(('&','|','ex','allf','allb'))
    if op in ('&','|'):
        return (op, random_ast(rng,depth+1,vars), random_ast(rng,depth+1,vars))
    y = ('y','z','t','u')[depth]
    if op == 'ex':
        return ('ex', y, random_ast(rng,depth+1,vars+(y,)))
    return (op,rng.choice(vars),y,random_ast(rng,depth+1,vars+(y,)))


def check_fragment():
    A = relation(3, ((0,0),(0,1),(2,2)))
    B = relation(4, ((0,0),(0,1),(2,2),(3,3)))
    assert phi(A) and not phi(B)
    rng=random.Random(20261015)
    tested=0
    for _ in range(15000):
        ast=random_ast(rng)
        if all(evaluate(ast,A,{'x':a}) for a in range(A[0])):
            assert all(evaluate(ast,B,{'x':b}) for b in range(B[0])), ast
        tested+=1
    return tested,A,B


if __name__ == '__main__':
    count, valid=check_preservation()
    formulas,A,B=check_fragment()
    assert [x for x in range(A[0]) if P(A,x)]==[0]
    assert [x for x in range(A[0]) if Q(A,x)]==[2]
    assert [x for x in range(B[0]) if P(B,x)]==[0]
    assert [x for x in range(B[0]) if Q(B,x)]==[2,3]
    print(f'UNION_PRESERVATION_OK {count} ordered small-model pairs; satisfying_counts={valid}')
    print(f'FRAGMENT_TRANSFER_OK {formulas} randomly generated formulas')
    print('SEPARATION_OK A_size=3 B_size=4')
