#!/usr/bin/env python3
"""Exact finite consistency checks for sums of restricted-base digit sets."""
from itertools import product
from math import prod


def run_blocks(W):
    w=sorted(W)
    result=[]
    start=prev=w[0]
    for k in w[1:]:
        if k==prev+1:
            prev=k
        else:
            result.append((start,prev))
            start=prev=k
    result.append((start,prev))
    return result


def check(g,W):
    W=set(W)
    digits=tuple(range(g))
    base={sum(d*g**i for i,d in zip(sorted(W), coeffs))
          for coeffs in product(digits, repeat=len(W))}
    A=base-{0}
    actual={0}
    for _ in range(g):
        actual={a+b for a in actual for b in A}
    blocks=run_blocks(W)
    block_range=[range(g*(g**(hi-lo+1)-1)+1) for lo,hi in blocks]
    expanded={sum(t*g**lo for t,(lo,hi) in zip(ts,blocks))
              for ts in product(*block_range)}
    assert len(expanded)==prod(len(r) for r in block_range)
    assert {sum(t*g**lo for t,(lo,hi) in zip(ts,blocks))
            for ts in product(*block_range) if sum(ts)>=g}==actual
    assert {sum(t*g**lo for t,(lo,hi) in zip(ts,blocks))
            for ts in product(*block_range) if sum(ts)<g}==expanded-actual
    assert len(expanded)==prod(g*(g**(hi-lo+1)-1)+1 for lo,hi in blocks)
    q=g**(blocks[-1][1]+2)
    assert len(expanded)<q
    factor_num=prod(g**(hi-lo+1+1)-g+1 for lo,hi in blocks)
    assert len(expanded)==factor_num
    # Directly test the carry obstruction for all smaller summand counts.
    small={0}
    for h in range(1,g):
        small={a+b for a in small for b in A}
        for n in small:
            for j in range(max(W)+3):
                if j not in W:
                    assert (n // g**j)%g < h
    return (g,len(W),len(blocks),len(expanded),len(actual),q)


def main():
    cases=[(2,[0,1,3,4,6]),(2,[1,3,4,6,8]),
           (3,[0,1,3]),(3,[0,2,3]),(3,[1,2,4,5]),
           (4,[0,2,3]),(4,[1,3,4])]
    totals=[check(*case) for case in cases]
    for k,(g,n,b,full,pos,q) in enumerate(totals):
        print(f'CASE {k+1} base={g} selected_positions={n} runs={b} block_values={full} positive_sums={pos} window={q}')
    print(f'VERIFY_OK finite_cases={len(cases)} independent_forms=3 exact_integer_arithmetic=yes')


if __name__=='__main__':
    main()
