# Independent mathematical audit — SCOPE-20260917-40f2bbfdd125

Audit date: 2026-10-01 (UTC) UTC.

Outcome: **PASSED**.

## Final claim assessed

Weak off-diagonal necessity for monomial-curve commutators in every dimension.

## Correctness

**PASS** — Li–Zeng's full proof supplies the all-dimensional companion-cube geometry, Jacobian normalization, error absorption, and a finite logarithmic average of commutator outputs. For \(1<q<\infty\), the Marcinkiewicz norm \(\sup_E |E|^{-1/q'}\int_E|F|\) is a Banach norm equivalent to weak \(L^q\), so Minkowski remains valid. Replacing only the final \(L^p\) output norm therefore gives \(m_Q|Q|^{1/q}\lesssim \|[b,H_\gamma]\|_{L^p\to L^{q,\infty}}|Q|^{1/p}\), exactly the stated Campanato scaling; the complementary-major-subset case uses Li–Zeng's bounded mean-zero test function unchanged.

## Originality

**PASS** — Oikari's full 2023 paper proves all-dimensional off-diagonal sufficiency but explicitly restricts necessity to the plane and asks in Question 1.22 for higher-dimensional necessity. Li–Zeng's 2026 theorem proves only diagonal \(L^p\to L^p\) necessity in all dimensions. Resultary and web searches found no prior all-dimensional weak-\(L^q\) necessity statement. The new statement is therefore not implied by either source alone.

## Value

**PASS** — The theorem settles the boundedness-necessity side of Oikari's explicit higher-dimensional question in the known sufficiency region and strengthens the target from strong to weak \(L^q\). This is a motivated structural extension with a clean function-space consequence.

## Source inspections

- **K. Li and Y. Zeng, Curved commutators in higher dimensions, arXiv:2609.18613v1 (2026).** Complete nine-page full text inspected. Theorem 1.2 is diagonal strong \(L^p\to L^p\); Sections 2–3 provide the companion-cube/Jacobian/telescoping argument, and Remark 2.4 states the geometry extends to higher dimensions. Consequence: Supplies the geometric engine but not off-diagonal or weak-target necessity.
- **T. Oikari, On the Lp-to-Lq boundedness and compactness of commutators along monomial curves, arXiv:2304.00621v2 (2023).** Primary full text inspected through the main theorem and Question 1.22. Off-diagonal sufficiency is all-dimensional, necessity is restricted to the plane, and Question 1.22 asks for higher-dimensional necessity. Consequence: The assigned theorem answers a stated gap rather than restating Oikari.
- **Resultary and current web searches for higher-dimensional weak off-diagonal monomial-curve commutator necessity.** No independent published statement matching \(L^p\to L^{q,\infty}\) necessity in all dimensions was located. Consequence: No covering result found; this is supporting evidence, not a novelty proof by itself.

## Residual risks

- The argument inherits Li–Zeng's asserted extension of the companion-cube geometry from the detailed three-dimensional proof to arbitrary dimension.
- The Li–Zeng preprint is very recent, so contemporaneous unindexed observations remain possible.

The accompanying JSON audit records the implication comparisons and exact coverage analysis in structured form.
