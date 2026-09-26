# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/001`  
**Audited source tree:** `49b1fa16eef71039c72157ee6270e08824d0bd32`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — For odd eligible part sizes, each factor (1+q^m)/(1−q^m)=1+2q^m/(1−q^m); modulo four, products with two nonconstant factors vanish. The odd coefficient is 2 times the count of 3-free odd divisors. The largest-part overline flip pairs every nonempty overpartition; on nonrectangular odd-size objects it and the all-bit flip generate four-element orbits. Rectangles contribute 2t(m), and t(m) is odd exactly when the 3-free part is a square. Thus the odd criterion holds for all m, not merely the N=120 replay, which reproduced coefficients and examples.

## Originality

PASS, qualified — Sang–Shi identify the singular overpartition object and establish mod-four dissections, including S(4n+2)=0. That congruence is prior art. The full odd square criterion and the simple four-orbit witness are not among the checked paper's stated congruences; the claim is limited to this refinement of a known product.

## Scientific value

PASS — An explicit all-odd mod-four classification with a bijective explanation is a reusable exact congruence, despite overlap of one even subcase. It does not supply an equidistributing crank beyond the described involutions.

## Prior work and source access

- https://arxiv.org/pdf/1712.08930
- https://arxiv.org/abs/1405.3626

## Scope of the decision

The verdict concerns “Exact mod-4 classification of singular overpartitions with parts prime to 3” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
