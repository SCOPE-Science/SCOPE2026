# Scientific review

## Correctness — PASS

For a fixed orthonormal input \((U,z)\), Gaussian rotational invariance reduces the sketched residual and coefficient to independent \(\chi^2_d\) and multivariate Student components. The coefficient identity uses a Schur complement of an actual Gaussian design: \(\|c\|_2^2\overset{\mathrm d}=\chi^2_k/\chi^2_{d+1}\), independently of the residual. Selecting the maximum of \(L\) independent residuals gives a separate \(\chi^2_d\) order-statistic inverse moment, so the complete norm integrability iff statement, both sharp boundaries, and the saturated \(d+1\) barrier follow by exact density behavior at zero. The angular Beta law and \(m(k+1)\log 2\) instance follow without simulation. The embedded verifier independently replays Gaussian least-squares identities and diagnostic comparisons, but the proof—not finite sampling—supports infinite-moment assertions.

## Originality — PASS, qualified

The closest motivating primary literature is Balabanov–Grigori arXiv:2011.05090v1; its Algorithm 2 supplies sketched regression and residual normalization, but its verified body focuses on embedding/stability rather than selection among independent sketches or an exact residual-only moment frontier. Jang–Grigori DOI:10.1002/nla.70029 instead uses Euclidean reorthogonalization. General Gaussian regression/Student inverse-moment identities, including a related prior result about an inverse-Wishart factor in Gaussian low-rank reconstruction, cover the coefficient lemma; they do not imply the max-residual selection rule's sharp two-part cutoff or its angular invariance without a new independence and selection argument. The searched published-results index contains no matching joint assertion, but search failure cannot guarantee novelty. Residual risk: specialized unpublished/unindexed work, or a more general published theorem with this as a corollary, may exist; an inaccessible related linear-system source was not excluded by full-text inspection.

## Value — PASS

Gaussian-sketch normalization can create a finite-sketch heavy-tail error even with orthonormal input columns. The theorem quantifies exactly how a cheap, observable screening statistic rescues moments and proves the limit of that rescue: no number of norm-only candidate restarts fixes the coefficient tail or average angular leakage. The distinction between moment stability and Euclidean orthogonality is actionable when choosing between resketching and actual reorthogonalization. It is a natural full-parameter result for a single orthogonalization step, not a claim about complete GMRES behavior or measured runtime.

## Scope and residual risks

Proof requires independent real Gaussian sketches, fixed Euclidean-orthonormal past basis, unit perpendicular new column, exact arithmetic, and selection restricted to sketched residual magnitudes. Floating-point stability, correlated sketches, adaptive input vectors, alternative screening features, and multi-step propagation remain unproved. Literature priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
