# Scientific review

## Correctness — PASS

For every real positive-definite two-coordinate Hessian the update maps are derived from exact coordinate minimization; their two sampled-path Gram expectations simplify to a scalar positive gap. Strictness follows from the Hessian determinant inequality. A three-coordinate rational Hessian has positive leading minors \(1,7/16,3/32\), and complete enumeration of its six permutation paths and 27 independent paths gives the strict Euclidean gap \(1949/55296\) and opposite energy gap \(-1309/55296\). The independent standalone script checks the generic symbolic identity and all rational path totals. The finite certificate proves the particular counterexample; the universal two-coordinate assertion follows from the symbolic calculation and its displayed proof.

## Originality — PASS, with residual risk

The source paper arXiv:1803.08200 develops exact coordinate descent with uniform permutation versus independent sampling, but its sections on one-epoch operators and convergence-rate comparisons concern specialized diagonally dominant matrix families and upper bounds. arXiv:1706.00908v4 studies a different special Hessian class. Oswald–Zhou's SOR comparison addresses energy norm bounds. Lai–Lim's positive-semidefinite matrix-product inequality has different factor symmetry and a different target; it does not imply Euclidean comparison of these oblique coordinate maps. Accessible historic claims about relaxed two-coordinate objective differences, two-component gradient reshuffling, and two-line Kaczmarz do not contain the dimension-two Euclidean identity combined with the explicit three-coordinate objective/Euclidean reversal. The relevant exact-phrase and semantic searches did not expose a covering theorem; search incompleteness and uncatalogued equivalent examples remain residual priority risks.

## Value — PASS

The literature explicitly distinguishes expected iterate, expected squared Euclidean distance, and expected objective as three separate convergence criteria. The result supplies an exact all-start one-epoch Euclidean gap in the smallest nontrivial dimension and the smallest-dimension counterexample to extending its sign. The same three-coordinate instance improves expected objective while worsening expected Euclidean error. This establishes a real measurement-dependent boundary for choosing sampling schemes, rather than a merely different wording of a scalar convergence bound or an arbitrary numerical slice.

## Scope and residual risks

The statement is not about multiple epochs, asymptotic convergence-rate dominance, or all higher dimensions. Published literature not indexed by the searches may contain an equivalent special-case calculation. The self-contained rational arithmetic and algebra support the stated theorem but do not constitute independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
