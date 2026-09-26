# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/002`  
**Audited source tree:** `66ee2d1068e32f095151235ba10dca73d05a68ed`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — The Fraction-only verifier builds ten degree-six Jacobi polynomials at the five rational beta values. Sixty disjoint rational brackets each have a Sturm variation drop of one, and the total drop is six per polynomial. The ordered brackets show BREAK at −19/10 and −17/10 and HOLD at −3/2, −13/10, −11/10; two X zeros and no Y zero occur in each displayed break interval. The independently published criterion δ<x₂ is consistent with these signs. This is a five-point bracket, not a continuous transition theorem.

## Originality

PASS, very narrow — Driver–Jordaan already give a necessary and sufficient interlacing criterion for exactly this parameter regime and numerical examples at n=5, alpha=2.35. The n=6, alpha=0 rational Sturm certificates are new finite evaluated witnesses as far as checked; the qualitative criterion and existence of breakdown are prior results.

## Scientific value

PASS, limited — Exact break and hold certificates provide test cases and a concrete rational bracket for the known criterion. They do not determine a critical beta or prove monotonicity.

## Prior work and source access

- https://arxiv.org/abs/1510.08599
- https://dlmf.nist.gov/18.16

## Scope of the decision

The verdict concerns “Askey-pair interlacing breakdown bracket for quasi-orthogonal Jacobi degree 6 at alpha = 0” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
