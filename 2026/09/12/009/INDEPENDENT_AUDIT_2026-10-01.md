# Independent mathematical audit — SCOPE-20260912-009

Outcome: **PASSED**.

## Correctness

**PASS** — I independently rebuilt the quadratic Poisson tensor and Schouten linearization. Constant bivector cocycles have dimension 2 with basis d01,d23; Pi+t d01 remains Poisson and has rank 2 for t!=0. The degree<=2 cocycle system has 90 unknowns, rank 56 and kernel dimension 34; affine-vector-field coboundaries have rank 16, leaving an 18-dimensional quotient slice, and d01 is not an affine coboundary. The smooth-origin obstruction follows because Pi is quadratic, so every smooth coboundary [Pi,X] vanishes at 0 whereas d01 does not. The stored exact radial-minor route is consistent with these checks.

## Originality

**PASS** — Resultary returned only this exact record for the combined constant/radial/polynomial localization obstruction. Searches of relevant Poisson-cohomology literature, including work on b-Poisson structures, did not cover this rank-zero hyperbolic-hyperbolic quadratic germ or the stated 34/16/18 polynomial slice. No broader inspected theorem implied the complete package.

Equivalent formulations: The localization question is the nontriviality/localizability of the constant Poisson-cohomology class d01, tested in constant, radial and degree-two subcomplexes.

Broader coverage: General Poisson-cohomology literature inspected concerns different degeneracy classes; no stronger theorem covered this package.

Database/table comparison: Resultary top-30 semantic search: exact record only for this hyperbolic-hyperbolic localization package.

Claim-vs-prior implication: Resultary returned only this exact record for the combined constant/radial/polynomial localization obstruction. Searches of relevant Poisson-cohomology literature, including work on b-Poisson structures, did not cover this rank-zero hyperbolic-hyperbolic quadratic germ or the stated 34/16/18 polynomial slice. No broader inspected theorem implied the complete package.

## Value

**PASS** — The package isolates several structurally distinct obstructions to localizing a natural infinitesimal Poisson deformation and explicitly leaves the general nonradial smooth problem open. The constant, radial and low-degree cohomology calculations are mutually reinforcing and mathematically useful boundary information rather than a one-off computation.

## Source inspections

- **Guillemin-Miranda-Pires, Symplectic and Poisson geometry on b-manifolds, Adv. Math. 264 (2014)** — Material read: bibliographic record and abstract/full-text availability description. Finding: studies codimension-one b-Poisson degeneracy and Poisson cohomology, not the rank-zero hyperbolic-hyperbolic quadratic germ.
- **Resultary semantic search** — Material read: top 30 results for hyperbolic-hyperbolic Poisson localization/cohomology. Finding: only exact hit was this record; nearby Poisson entries concern different structures.
- **record-cited Poisson/Nambu background sources** — Material read: titles/source metadata and targeted web searches. Finding: no located theorem covered the constant/radial/degree-two combined obstruction package.

## Residual risks

- The general nonradial smooth compact-support localization problem is open and is not inferred from the finite polynomial slice.
- The radial obstruction relies on the stored exact-minor derivation in addition to the independently rebuilt constant/polynomial calculations.
