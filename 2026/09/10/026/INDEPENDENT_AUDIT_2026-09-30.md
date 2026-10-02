# Independent scientific audit — SCOPE-20260910-026

Audited: 2026-09-30 UTC

Disposition: **passed**

## Correctness

**PASS** — Fresh arithmetic verifies all eight listed rational x-values and their square values, including f(-7/4)=4489/1024 and f(4/9)=139129/59049, hence 16 affine points plus infinity. Independent finite-field enumeration gives #C(F_7)=14 and #J(F_p)=27,71,120,136 for p=3,5,7,11; gcd(71,136)=1 supports torsion triviality. Independent factorization patterns [5], [1,4], [1,1,3], [2,3] at p=2,7,11,19 support the S5 Galois argument. An independent exhaustive coprime search through H(x)<=2000 finds exactly the eight listed x-values. With the cited Coleman bound for rank 1 at p=7, 17 exhibited rational points exceed the ceiling 16, so rank at least 2 follows.

## Originality

**PASS** — The curve itself and several rational divisor examples were public before this finding, but the inspected prior material does not state the corrected 17-point floor, rank-at-least-two consequence, or bounded height census. The final combined claim therefore survives the implication comparison.

## Value

**PASS** — This is a substantive correction of a false exact rational-point/rank target on a concrete genus-2 curve: explicit counterpoints force a different rank regime and invalidate the proposed rank-one method. The corrected floor and bounded census are mathematically useful even though full rational-point completeness remains open.

## Sources and residual risk

- https://math.mit.edu/~edgarc/files/slides/rigendos-unsw-2019.pdf — Pages 36-40 were inspected, including rendered page 37 showing the exact curve and divisors D1 and D2. Text search found no Mordell-Weil rank statement. Assessment: Partial prior coverage of the curve and four displayed rational points; not the 17-point/rank>=2 result.
- https://www.lmfdb.org/Genus2Curve/Q/ — Search results surfaced by exact equation/discriminant queries. Assessment: No checked entry covering the final claim.

Residual risks:
- An isomorphic LMFDB model or older computational notebook may contain more information than surfaced by text search; this is recorded as residual originality risk.

The detailed machine-readable audit is in `INDEPENDENT_AUDIT_2026-09-30.json`.
