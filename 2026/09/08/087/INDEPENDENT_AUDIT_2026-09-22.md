# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/087`  
**Audited source tree:** `0bda41de421272108b681af24610d156903c7147`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — Recompiled enum.c and ran all 35 fixed-first-row classes. The subtotal 1,969,680 times C(7,3)=35 is 68,938,800; every class has minimum 24. The subtotal histogram 412560,181440,725760,483840,90720,51840,22680,840 at permanents 24,25,26,27,30,31,32,54 scales to the stated distribution. Independently checked the row-mask witness [7,7,25,26,100,104,112] by permutation and Ryser counts (24), margins 3, and 24/(4/3)^7=6561/2048. Column-transitivity makes the factor 35 valid. The code is an exhaustive finite computation, not a formal proof assistant certificate.

## Originality

PASS, qualified — Schrijver's 1998 paper proves the general lower bound, and OEIS A001501 already records the labeled matrix count. A Fano-plane incidence matrix is a standard 7-by-7 weight-3 example and directly has permanent 24, so no novelty is attributed to the existence of a 24 witness. The checked sources do not provide the exhaustive D(7,3) minimum proof or this eight-value labeled distribution; originality attaches to that finite census, not the bound or witness value.

## Scientific value

PASS — The exact minimum, full histogram, gaps at 28–29 and 33–53, and a checked minimizer supply a reusable small-parameter benchmark for regular bipartite permanent questions. The number of minimizer orbits is still unknown here.

## Prior work and source access

- https://homepages.cwi.nl/~lex/files/countpms2.pdf
- https://oeis.org/A001501

## Scope of the decision

The verdict concerns “Exact Schrijver-sharpness census of D(7,3): minimum permanent 24, witness orbit, and full distribution” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
