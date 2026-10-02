# Independent audit — SCOPE-20260909-059

Date: 2026-09-30 UTC

## Final claim

For the stated product of an Inoue–Bombieri Oeljeklaus–Toma surface and an elliptic curve, the class represented by the elliptic \((1,1)\) form has a nonzero first Bott–Chern deformation obstruction in the specified Beltrami direction; the extendability germ is proper along that direction and the nearby Bott–Chern number drops by at least one.

## Correctness

**PASS.** The package definitions were reconstructed from the source tree rather than accepted from its success log. Fresh algebra on the companion polynomial \(x^3-x-1\) gives \(2\log|\beta|/\log\alpha=-1\), so the displayed \(\bar\partial\)-coefficient of the test form vanishes. The contraction pairs nontrivially with a \(\bar\partial\)-closed complementary form, proving its Dolbeault class nonzero. Lin–Ye Theorems 1.1–1.2 and the natural Bott–Chern-to-Dolbeault map then turn this nonzero first-order class into an obstruction and a dimension jump. Angella–Dubickas–Otiman–Stelzig Corollary 3 and Theorem 15 support the pluriclosed type condition and the Hodge-number calculation used for the surface factor.

Residual risk: The deformation-obstruction step relies on the cited relative Bott–Chern theory rather than a formalized proof in the package; the fresh computation checks the concrete nonvanishing input, not the full analytic machinery.

## Originality

**PASS.** A semantic published-results search for the exact product, class and deformation direction returned this record as the only direct match. Lin–Ye supplies the general obstruction/jump formalism, while Angella–Dubickas–Otiman–Stelzig supplies Oeljeklaus–Toma pluriclosed and cohomological structure; neither source states or implies this explicit product witness without the record’s nonzero pairing calculation.

Equivalent formulations: Searched by the exact product geometry, Bott–Chern class, Beltrami direction, Aeppli/Serre pairing and jump formulation; no external equivalent statement was found.

Broader coverage: Lin–Ye covers general Bott–Chern/Aeppli deformation obstructions and Angella et al. covers Oeljeklaus–Toma cohomology/pluriclosed metrics, but neither gives this product-direction nonvanishing witness.

Exact database or table: No exact database/table is naturally applicable to this geometric deformation claim; semantic published-results search found no separate record encoding the same explicit witness.

Claim versus prior implication: The prior general theorems require a nonzero obstruction input. They do not themselves imply the specific contraction/pairing nonvanishing for this \(X_0,\alpha_0,\mu\).

Residual risk: An unindexed specialized deformation computation for the same solvmanifold product could exist.

## Value

**PASS.** An explicit Bott–Chern jumping direction on a named pluriclosed non-Kähler threefold is a motivated boundary example in deformation theory. It converts general obstruction machinery into a concrete, checkable witness and isolates how a natural elliptic-fibre class fails to persist.

Residual risk: The result gives a one-direction local jump and not a full Kuranishi-space classification or exact Bott–Chern table.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/059/RESULT.md — Full scientific statement, definitions, proof sketch and limitations inspected from the source blob.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/059/artifacts/verify_target.py — Actual symbolic verifier source inspected; it checks the \(b=-1\) condition, the nonzero wedge pairing and the \(H^{0,2}\) count but does not itself prove the cited analytic obstruction theorem.
- https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE059 — Semantic exact-claim search; this record was the direct match.
- https://arxiv.org/html/1403.0285v2 — Lin–Ye full text inspected, especially Theorems 1.1–1.2 and Remark 2.3 on obstruction-induced jumps and the natural Bott–Chern/Dolbeault maps.
- https://arxiv.org/html/2201.06377v2 — Angella–Dubickas–Otiman–Stelzig full text inspected, especially Corollary 3 (\(s=t\) pluriclosed condition) and Theorem 15 (pluriclosed Oeljeklaus–Toma Hodge numbers).

## Disposition

**PASS.** Correctness, originality and value all pass the review bar.
