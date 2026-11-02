# Scientific review

## Correctness: PASS

For the claimed affine parent law, the total weight is exactly \(s_m=(1+\alpha)m-\alpha\). When the root is already nonleaf, a direct root attachment implies that the newly arrived node increases the leaf count by one. The joint one-step identity \(I_{m+1}(L_{m+1}-L_m)=I_{m+1}\) closes all conditional covariance calculations. The two mean recurrences and one global covariance recurrence yield the stated formula by induction. Propagating each root-attachment indicator through later leaf updates gives its individual exact covariance; the algebraic telescoping identity for successive birth times proves strict positivity of the gap for all \(\alpha>0\), with exact equality at \(\alpha=0\). The Gamma products prove the asymptotic at fixed positive reinforcement. Independent full parent-history enumeration at sizes 2–8 and additional exact rational assertions passed (2,777 checks in `verify.py`). Finite tests do not constitute the all-size proof; that is provided in `RESULT.md`.

## Originality: PASS (bounded)

The closest accessible source is Janson, Kuba and Panholzer, arXiv:0805.4084, Sections 3 and 6. It identifies generalized affine insertion families and their *marginal* leaf distributions, as well as Stirling-block marginals (which encode classical plane-tree root degree at the ordinary parameter), but not root-attachment-time versus total-leaf covariance gaps. Mahmoud, Smythe and Szymański (1993) also provide marginal root and leaf formulas; Janson, arXiv:0803.1129, covers the plane tree/Stirling-permutation relationship and leaf statistics. A publicly available uniform-recursive-tree exact equal-share identity covers the \(\alpha=0\) boundary, which is expressly excluded as an independently new result. Neither that special case nor the marginal literature implies, without a further mixed-moment analysis, the stated exact \(\alpha>0\) arrival hierarchy. The search included alternative language involving Stirling-permutation blocks, ascents, degree and leaves, and compared the effects of stronger marginal enumerators. The residual priority risk is that a general bivariate generating function or multicolor urn calculation could implicitly establish the same strict hierarchy; an independent historical audit is still warranted.

## Mathematical value: PASS

The property separates uniform attachment from every positive amount of reinforcement by an exact and strict qualitative law. The result is motivated by comparing local exposure to the root with the global leaf population, and answers which arrival dates contribute more to their positive dependence. The exact gradient, its boundary case, full parameter-family statement, and nontrivial sublinear covariance growth for positive reinforcement give content beyond a routine marginal moment calculation.

## Scientific limitations

No stochastic monotonicity of conditional leaf-count distributions or result for nonlinear attachment kernels is claimed. All statements concern the original probability law, not a causal intervention. The public source date used for archival eligibility is the verified March 7, 2008 arXiv submission; a 1993 source is also acknowledged by publication year without inventing its day of first release.

Self-review: passed. Independent audit: not yet performed.
