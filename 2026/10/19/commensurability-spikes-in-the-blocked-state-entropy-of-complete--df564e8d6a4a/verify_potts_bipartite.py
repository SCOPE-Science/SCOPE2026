#!/usr/bin/env python3
"""Independent finite-state checks of a color-conflict-energy classification."""
from itertools import product, combinations
from collections import Counter
from math import factorial, comb, pi, log


def energy(state, a, b):
    return sum(state[i] == state[j] for i in range(a) for j in range(a, a+b))


def is_stable(state, a, b, q, move_size):
    e = energy(state, a, b)
    n = a+b
    for size in range(1, move_size+1):
        for sites in combinations(range(n), size):
            choices = [[v for v in range(q) if v != state[i]] for i in sites]
            for targets in product(*choices):
                new = list(state)
                for i, c in zip(sites, targets):
                    new[i] = c
                if energy(new, a, b) < e:
                    return False
    return True


def predicted_one(state, a, b, q):
    A = Counter(state[:a]); B = Counter(state[a:])
    proper = all(A[i]*B[i] == 0 for i in range(q))
    balanced = a % q == 0 and b % q == 0 and all(A[i] == a//q and B[i] == b//q for i in range(q))
    return proper or balanced


def onto(n,k):
    return sum((-1)**j*comb(k,j)*(k-j)**n for j in range(k+1))


def exact_counts(a,b,q):
    proper = sum(comb(q,s)*onto(a,s)*(q-s)**b for s in range(1,q))
    balanced = 0
    if a%q == b%q == 0:
        balanced = factorial(a)//(factorial(a//q)**q)*factorial(b)//(factorial(b//q)**q)
    return proper,balanced

cases=0; configurations=0; move2=0
for q in (2,3,4):
    limit={2:5,3:4,4:3}[q]
    for a in range(1,limit+1):
      for b in range(1,limit+1):
        count1=count2=countpos=0
        for state in product(range(q),repeat=a+b):
          configurations+=1
          s1=is_stable(state,a,b,q,1)
          pred=predicted_one(state,a,b,q)
          assert s1==pred,(q,a,b,state,s1,pred)
          if s1:
              count1+=1
              if energy(state,a,b)>0: countpos+=1
              s2=is_stable(state,a,b,q,2)
              assert s2==(energy(state,a,b)==0),(q,a,b,state,s2)
              count2+=int(s2)
              move2+=1
        prop,bal=exact_counts(a,b,q)
        assert count1==prop+bal and count2==prop and countpos==bal,(q,a,b,count1,count2,prop,bal)
        cases+=1
print(f'PASS: {cases} parameter cases; {configurations} labelled colourings; {move2} 2-move checks')
for q in range(2,8):
    for n in (q,2*q,3*q):
        pro,bal=exact_counts(n,n,q)
        asym=q**(2*n+q)/(2*pi*n)**(q-1)
        assert pro>=0 and bal>0 and (bal/asym)>0
        print(f'q={q}, n={n}: P={pro}, M={bal}, ratio_to_asym={bal/asym:.6f}')
print('ALL CHECKS PASSED')
