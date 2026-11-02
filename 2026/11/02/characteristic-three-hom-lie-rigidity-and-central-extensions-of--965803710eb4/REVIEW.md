# Scientific review: characteristic-three type-A2 Hom–Lie spaces

## Correctness

**PASS.** The domain is every field of characteristic \(3\), including nonperfect and finite fields. For the seven-dimensional central quotient, the complete Hom–Jacobi system is linear. Its displayed exact \(48\times48\) minor has determinant \(1\) over \(\mathbb F_3\), proving that the only structures are scalar. The submatrix is reconstructed directly from elementary matrix commutators by `verify.py`, not quoted from a numerical log; `crosscheck.py` independently computes the nullities in different bases. For the eight-dimensional Lie algebra, perfection forces a Hom–Lie map to preserve the center and descend, and the central-valued maps supply exactly eight further dimensions. The triangular composition algebra, radical, and finite-field counts follow by block multiplication. The certificate can be rerun over the prime field; its unit determinant remains nonzero over all extensions.

## Originality

**PASS, with bounded historical risk.** The central comparison is Sun–Zhang–Zhu, arXiv:2610.25056v1 (2026-10-18), especially the statement of Theorem 1.1, Section 3.2, and Remark 3.4. Its assumptions exclude characteristic \(3\), so its scalar theorem for higher-rank simple Lie algebras neither entails nor contradicts the present seven-dimensional quotient result. Makhlouf–Zusmanovich, arXiv:1805.00187, explicitly work in characteristic unequal to \(2,3\) and do not cover it. Xie–Jin–Liu's 2015 paper treats characteristic zero. Targeted queries for Hom–Lie/\(\mathfrak{psl}_3\)/characteristic-three formulations and mathematical-record similarity results did not locate the exact pair of classifications or its composition-algebra structure. The main residual risk is an unlocated small-characteristic treatment or a general theorem that implicitly yields this special case; search nonappearance is not a proof of historical novelty.

## Value

**PASS.** This is a complete, naturally defined Hom–Lie classification at a specific bad prime omitted from a recent classification theorem, and it separates a rigid centerless quotient from its nine-dimensional Hom–Lie central extension. The fact that the nine-dimensional solution space is itself an associative algebra, with a seven-dimensional square-zero radical and exact finite-field unit/idempotent counts, is a structural distinction relevant to the literature's question about algebra structures on Hom–Lie spaces. This is not merely an isolated numerical rank or a general assertion about all modular Lie algebras.

## Scope and source limits

The theorem is for type \(A_2\) in characteristic \(3\) only. The source inspections cover the relevant theorem statements, proof sections, and assumptions of the 2026 and 2018 open-access full texts, and the stated scope of the 2015 paper; they do not constitute an exhaustive search of historical literature. The matrix minor supplies a reproducible arithmetic certificate but not a uniform proof for other root systems.

Self-review: passed. Independent audit: not yet performed.
