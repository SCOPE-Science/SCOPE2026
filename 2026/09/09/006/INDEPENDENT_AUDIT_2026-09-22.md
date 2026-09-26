# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/006`  
**Audited source tree:** `3196fcb4a9d42a5637ff9463eba49d939308b903`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — Replayed graph constructions and SRG incidence checks, exact card characteristic polynomials, exhaustive clique/coloring checks and integer Laplacian cofactors. Every graph is vertex transitive, so its deletion cards are isomorphic; the two 16-vertex parents have the same spectrum, and the derivative identity P_{G−v}=P'_G/16 for walk-regular graphs also explains their equal card polynomials. Shrikhande cards have no K4 while rook cards have six; their tree counts are 2,177,280,000 and 2,176,782,336. Thus the decks differ despite card cospectrality. Numerical Hoffman ratios are secondary to the exact polynomial identity.

## Originality

PASS, narrow data — Parent cospectrality and the graph families are standard. The card cospectrality itself follows from a known walk-regular/vertex-transitive deletion identity and is not a new phenomenon. The precise combined card polynomials, tree counts and separator census are the finite contribution not supplied by the checked graph tables.

## Scientific value

PASS, bounded — The exact clique and Kirchhoff separation provides a reproducible example of information retained by deletion cards beyond their common spectra. It is a case study, not a general reconstruction theorem.

## Prior work and source access

- https://aeb.win.tue.nl/drg/graphs/Shrikhande.html
- https://www.win.tue.nl/~aeb/graphs/srg/srgtab.html

## Scope of the decision

The verdict concerns “Singleton vertex-deletion decks of four canonical SRGs: exact card polynomials, persistent Shrikhande/rook card cospectrality, and a clique/Kirchhoff deck separator” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
