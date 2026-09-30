# Independent audit — 2026-09-29

**Record:** `2026/09/18/kummer-deck-normalizer-even-maximal-curves--ba7ecfcdf760`  
**Title:** Normalizer rigidity for the Kummer deck group of the even Ma–Wang maximal curves  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `73fab0a13f47fc3e797c3420dde4ca32711f5780`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The branch-label normalizer argument checks. For even n, gcd(r,q^n+1)=1, the finite F_q points and infinity have Kummer exponent 1 modulo m, while the remaining F_{q^2}-points have exponent r; the two classes have unequal sizes. A normalizing automorphism preserves k(u), acts by a Möbius transformation, and sends z to h(u)z^t, so multiplication by t must preserve the two labeled classes. Unequal multiplicities rule out swapping and force t=1; the base transformation stabilizes P^1(F_q), hence lies in PGL_2(q). Ma–Wang's lifts then saturate the m·|PGL_2(q)| upper bound. The center conclusion follows because C is central and PGL_2(q) is centerless for q≥2.

## Originality

**PASS** — Ma–Wang construct the subgroup of the same order but, in the located current source metadata and searches, do not identify it as the full normalizer/centralizer of the Kummer deck group. Older Beelen–Montanucci work determines the full automorphism group for the odd-n family, not this even-n normalizer. General superelliptic literature supplies normalizer/uniqueness machinery but no located statement specializes to this branch-labeled even family with the displayed equality.

## Scientific value

**PASS** — Identifying the exact normalizer isolates all automorphisms preserving the distinguished Kummer quotient and proves that any additional automorphism must move that structure. This is a useful rigidity statement for the newly introduced even family even though it stops short of the full automorphism group.

## Findings

- The Kummer valuation labels are 1 on P^1(F_q) and r on its F_{q^2}-complement, with infinity also labeled 1.
- The unequal label-class cardinalities q+1 and q^2-q force a normalizer element to preserve both classes and act trivially on the deck group.
- The stabilizer of P^1(F_q) inside PGL_2(k) is PGL_2(q), giving the sharp normalizer-size bound.
- The q=2 edge case does not break the label argument; an independent F_256 count for n=4 also reproduced the maximal point count 1025, though the source's advertised new non-Hermitian even family is stated for q>2.

## Independent checks

- Verified gcd((q^{n-1}-1)/(q-1),q^n+1)=1 numerically across representative even n and algebraically through the branch-exponent argument.
- Recomputed the valuations at F_q, F_{q^2}\F_q, and infinity.
- Checked the Möbius stabilizer and center arguments, including q=2.
- Compared with Ma–Wang's current abstract metadata, Beelen–Montanucci's odd-n full-automorphism theorem, and generalized-superelliptic normalizer literature.

## Sources

- https://arxiv.org/abs/2609.19546 — Ma–Wang source for the Kummer model and explicit subgroup; current indexed version is v1.
- https://doi.org/10.1112/jlms.12144 — Beelen–Montanucci full automorphism group for the earlier odd-n maximal curves.
- https://arxiv.org/abs/1609.09576 — Generalized-superelliptic normalizer/uniqueness context.

## Limitations

- The result determines only the normalizer/centralizer of the displayed deck group, not the full automorphism group.
- Ma–Wang's headline even maximal/non-Hermitian construction is advertised for q>2; the normalizer proof itself is algebraic and includes q=2, but the audit does not broaden unrelated source claims.
- The source is very recent, so near-simultaneous unindexed work remains a priority risk.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
