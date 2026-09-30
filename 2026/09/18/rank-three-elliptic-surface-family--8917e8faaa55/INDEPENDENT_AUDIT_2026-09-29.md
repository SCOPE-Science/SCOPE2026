# Independent audit — A one-parameter maximal-rank family with a rank-two middle summand

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/rank-three-elliptic-surface-family--8917e8faaa55`
**Audited tree:** `0c88b5fa3e3cfe7010ea5133c8e8e568d71ba1b7`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** The family satisfies Bao's rank criteria exactly. Independent symbolic algebra gives Delta=64(u^2+3)^3, Delta/(4A)=(u^2+3)^3, and the two middle-summand cube identities [2(u+sqrt(-3))]^3 and [2(u-sqrt(-3))]^3. The third-summand condition reduces to 16/(u^2-1)^2 being a rational cube, equivalently u^2-1=4r^3; setting X=4r,Y=4u gives Y^2=X^3+16. LMFDB 27.a4 records rank zero and torsion Z/3 on this curve, leaving only the two affine rational torsion points (0,+/-4), corresponding to the excluded u=+/-1. Hence the decomposition ranks are (1,2,0), total rank 3, and Bao's Proposition 6.1 confirms rank 3 is maximal in the class.

### Independent checks

- Recomputed B^2-4AC=64(u^2+3)^3 and the first-summand cube condition exactly.
- Expanded both Q(sqrt(-3)) cube identities and verified Bao's rank-two middle criterion.
- Verified the algebraic equivalence 16/(u^2-1)^2 in Q^3 iff u^2-1=4r^3.
- Checked the substitution X=4r,Y=4u into Y^2=X^3+16.
- Checked both displayed rational sections by exact substitution into the surface equation.
- Checked Bao v1 Proposition 6.1 (rank <=3) and Example 6.4, which contains only the numerical (16,280,-972) (1,2,0) example.
- Checked LMFDB 27.a4: simplified model y^2=x^3+16, rank 0, torsion Z/3, with affine rational torsion points (0,+/-4).

## Originality

**PASS.** PASS to the best of current searchable knowledge. Bao's v1 proves the general rank formula and Proposition 6.1, and Example 6.4 gives one numerical (1,2,0) example with (A,B,C)=(16,280,-972). It does not state the assigned rational one-parameter family. Targeted Resultary/repository searches for the coefficient formulas and a parametric (1,2,0) family found no earlier equivalent record.

### Literature and chronology checked

- https://arxiv.org/abs/2609.16349v1 — Zhengheng Bao, A formula for the rank over Q(t) of the elliptic curve y^2=x^3+At^6+Bt^3+C; v1 contains Proposition 6.1 and the isolated Example 6.4.
- https://www.lmfdb.org/EllipticCurve/Q/27/a/4 — LMFDB elliptic curve 27.a4 (Cremona 27a3), simplified model y^2=x^3+16, rank 0 and torsion Z/3.
- https://arxiv.org/abs/2506.19423 — Remke Kloosterman, Determining explicitly the Mordell--Weil group of certain rational elliptic surfaces; surrounding two-coefficient literature.

## Scientific value

**PASS.** The result promotes an isolated maximal-rank mechanism in Bao's classification to an explicit infinite rational family. The construction is structurally informative: conjugate cube identities force the rank-two middle summand, while a single fixed rank-zero Mordell curve globally suppresses the third summand.

## Limitations

- The rank conclusion uses Bao's Theorem 1.3 and Proposition 6.1 as established inputs rather than reproving the global rank formula.
- The final E3 exclusion relies on the established Mordell--Weil data for LMFDB 27.a4.
- No claim is made that the parametrization exhausts all rank-three triples or that different u always give non-isomorphic surfaces.
- Bao's source preprint is very recent, so unindexed parallel constructions remain a residual originality risk.

## Publication guard

The current source tree on `main` matched the assignment tree `0c88b5fa3e3cfe7010ea5133c8e8e568d71ba1b7` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
