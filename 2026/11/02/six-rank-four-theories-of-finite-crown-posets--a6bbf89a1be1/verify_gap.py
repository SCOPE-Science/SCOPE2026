#!/usr/bin/env python3
"""Finite stress test of the proved parity-preserving cyclic gap lemma.
Not a substitute for its unrestricted integer proof in RESULT.md.
"""
L = [2,5,11,23]
for r in range(1,4):
    T=L[r-1]
    for d in range(L[r],L[r]+31):
        for e in range(L[r],L[r]+31):
            if d%2 != e%2: continue
            for a in range(1,d):
                b=d-a
                ok=False
                for aa in range(1,e):
                    bb=e-aa
                    if a%2!=aa%2: continue
                    if (a==aa<T or a>=T and aa>=T) and (b==bb<T or b>=T and bb>=T):
                        ok=True;break
                assert ok,(r,d,e,a,b)
    print('GAP_LEMMA_CHECK_OK',r,'threshold',L[r])
