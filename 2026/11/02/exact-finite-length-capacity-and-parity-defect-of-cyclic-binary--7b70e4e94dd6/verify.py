#!/usr/bin/env python3
"""Exact independent checks for finite cyclic binary (3,2) read capacity."""
from itertools import product


def direct_image(m):
    seen = set()
    fibers = {}
    for bits in product((0, 1), repeat=2*m):
        y = tuple(bits[2*i] + bits[(2*i+1) % (2*m)] + bits[(2*i+2) % (2*m)] for i in range(m))
        seen.add(y)
        fibers[y] = fibers.get(y,0)+1
    return seen, fibers

T=((2,1,1),(1,1,1),(1,1,1))

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def trace_pow(m):
    A=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(m):
        A=mul(A,T)
    return sum(A[i][i] for i in range(3))


def recurrence_value(m):
    # Eigenvalue power sum: s_0=2, s_1=4, s_m=4s_{m-1}-2s_{m-2}
    if m==0: return 2
    u,v=2,4
    for _ in range(2,m+1):
        u,v=v,4*v-2*u
    return v


def transition(s,label):
    options={'*':(0,1),'0':(0,), '1':(1,)}
    successors={b for a in options[s] for b in (0,1) if 0<=label-a-b<=1}
    if not successors: return None
    return '*' if len(successors)==2 else str(next(iter(successors)))


def cyclic_deterministic_walk_count(y):
    count=0
    for first in ('*','0','1'):
        s=first
        for label in y:
            s=transition(s,label)
            if s is None: break
        if s==first:
            count += 1
    return count


def predicted(m):
    return recurrence_value(m)-1-(-1)**m


def main():
    for m in range(1,11):
        outputs, fibers=direct_image(m)
        trace=trace_pow(m)
        expected=predicted(m)
        assert len(outputs)==expected, (m,len(outputs),expected)
        assert trace==recurrence_value(m),(m,trace)
        assert sum(fibers.values())==4**m
        # Independent, exact cyclic-state multiplicity count, by output word.
        assert sum(cyclic_deterministic_walk_count(y) for y in outputs)==trace
        assert all(cyclic_deterministic_walk_count(y)==(2 if (m%2==0 and set(y)=={1,2} and all(y[i]!=y[(i+1)%m] for i in range(m))) else 1) for y in outputs)
        print('m=%2d  N=%6d  trace=%6d  binary_inputs=%8d  OK' % (m,len(outputs),trace,4**m))
    for m in range(1,201):
        assert predicted(m)==trace_pow(m)-1-(-1)**m
    print('VERIFY_OK')


if __name__=='__main__':
    main()
