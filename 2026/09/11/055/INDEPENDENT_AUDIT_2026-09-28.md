# Independent audit — 2026-09-29

Record: `2026/09/11/055`  
Audited tree: `784e3734142bb928063d1f70c472f0f2f92b6fe4`  
Disposition: **repaired**

## Correctness

I independently enumerated the stated partition-gap function through 80 and expanded the eta-product quotient through 80. The first mismatch is exactly `n=3`, with `C(3)=1` and product coefficient `0`; there are 77 mismatches in `0..80`. I also recomputed `C(4)=1`, so the proposed `C(5n+4)=0 mod 5` family fails at `n=0`. For the five residue classes, the first nonzero coefficients modulo 5 occur at indices `0,6,2,3,4`, respectively.

The core negative result is correct. The published sentence and slogan saying every residue class is inhabited "from its first term" is inaccurate for residue 1, whose coefficient at index 1 is zero and whose first nonzero occurs at index 6. The staged repair changes only that wording and leaves the disproof and data intact.

## Originality

This is a target-specific falsification rather than a new general Rogers–Ramanujan theorem. The cited surveys provide the surrounding mod-18/Bailey-pair literature; targeted searches did not locate the exact proposed `(2, 7, 12)` candidate, which is not enough by itself to assert broad novelty.

## Scientific value

The short obstruction at `n=3` and the first-term congruence failure at `n=0` are useful because they decisively terminate an otherwise expensive candidate identity and modularity route.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/055 ; https://www.combinatorics.org/files/Surveys/ds15/ds15v1-2008.pdf ; https://www.wcupa.edu/sciences-mathematics/mathematics/jMcLaughlin/documents/RamSlatJuly25.pdf
