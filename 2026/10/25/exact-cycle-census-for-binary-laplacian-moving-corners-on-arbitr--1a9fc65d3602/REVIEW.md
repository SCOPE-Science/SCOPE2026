# Scientific review: binary moving-corner cycle census

## Correctness — PASS

The claimed result concerns precisely the finite binary corner map \(T=(I+U^2)(I+V^2)\). Frobenius reduces its power-of-two fixed spaces to multiplication by \(u^a+v^a+u^av^a\) in a truncated polynomial ring. Decomposition by exponents modulo \(a\), a unit-preserving substitution, and a quotient-algebra rank identity prove that each pair of residue chains contributes \(\min(d_i,e_j)\) to the nullity. Summing chain levels gives the stated finite sum. Distinct surviving monomials prove the operator order, and nested fixed sets give exact periods and zeta. The dyadic probability follows from an exact half-dimension calculation. Pure-Python checker results: 405 binary matrix ranks and 60 exhaustive orbit counts passed. No probabilistic computation is used as an infinite proof.

## Originality — PASS on inspected evidence, with priority risk

The motivating paper supplies the binary corner factorization and full-operator order, but stops short of counting individual seed periods. Classical unipotent tensor-product results supply background linear algebra, not an all-rectangle moving-corner orbit census; the specific quotient-algebra synthesis and the exact dyadic period fraction were not identified in the inspected sources. Related public modular-Laplacian records concern full-space Frobenius dilation or cross-modulus parity, not finite corner cycle distributions. A standard tensor-product theorem combined with the source's factorization points toward this derivation, so originality is necessarily confined to the explicit dynamical census and may require wider historical checking.

## Value — PASS

The source explicitly distinguishes the operator's period from potentially shorter periods of individual seeds. An exact count for all window shapes resolves that natural quantitative gap, gives a complete finite dynamical zeta function, and quantifies how rarely dyadic seeds fail to attain maximal period. Rectangular uniformity and the surprising half-rank formula are structural, not an arbitrary computed small case. The calculation can guide selection of corner seeds where full-period behavior matters, but makes no claim about security or full-lattice recurrence.

## Limitations and closest literature

Closest source: Nowak-Kępczyk, arXiv:2511.17389v2, Section 3.5, Theorems 1–2. Algebraic background: Glasby–Praeger–Xia, arXiv:1711.06860v2, Sections 1–2. Full-lattice modular-Laplacian records from September 2026 were read and address different objects. Historical-priority risk persists, especially from pre-existing modular Jordan-product techniques. The conclusion is for an autonomous co-moving corner, not a whole-lattice return. Only characteristic two and the diagonal mask are covered.

Self-review: passed. Independent audit: not yet performed.
