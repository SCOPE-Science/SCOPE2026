# Scientific review

## Correctness — PASS

The stated SPD Lanczos hypothesis implies an irreducible positive-definite tridiagonal \(H\) and nonzero next recurrence coefficient. The off-corner entry of \(H^{-1}\) is nonzero, so the Galerkin numerator cannot cancel its affine denominator on the pole hyperplane. Gaussian regression yields the exact multivariate Student density. Energy-orthogonal Galerkin error decomposition leads to a one-dimensional pole, which gives exactly the threshold \(p=1\); coarea and dominated convergence give a finite strictly positive sharp tail constant. The sketched least-squares normal equations have a full-rank Student perturbation and threshold \(p=\ell-k+1\). The bundled verifier checks exact identities and independent randomized reconstructions; the infinitary claims rely on proof, not simulation.

## Originality — PASS, with residual priority risk

Timsit–Grigori–Balabanov (arXiv:2302.07466) study randomized orthogonal projections in Krylov solvers, including high-probability behavior and observed instabilities. Güttel–Schweitzer (arXiv:2208.11447) state the sketched FOM and GMRES constructions. Nakatsukasa–Tropp (arXiv:2111.00113) prove randomized residual-method accuracy, and Balabanov–Nouy (arXiv:1803.02602) provide sketch-based Galerkin projection for reduced modeling. Their relevant full-text descriptions provide the constructions and conditional/high-probability bounds, but in the inspected material none states the combined arbitrary-moment, all-nonterminal-Krylov-step separation or the sharp hyperplane-tail constant. The Gaussian regression density itself is a standard result and is not presented as a new distribution. A formulation in specialized Gaussian projection or numerical linear algebra literature may remain unidentified.

## Mathematical value — PASS

The two projected solvers use the same fixed Krylov approximation space and the same random sketch budget, but have different and exact unconditional error integrability cutoffs. This provides a rigorous structural distinction that cannot be inferred from embedding-success bounds: oversampling alone does not create a finite mean for unsafeguarded sketched Galerkin, whereas two extra rows suffice for finite second moment of sketched minimal residual. The sharp positive tail constant quantifies the mechanism; no general or downstream theorem is required for this method-specific boundary to be useful.

## Risks and verification limits

The result is a statement about expectations over all Gaussian sketches, not an assertion of common catastrophic failures. It does not include finite-precision effects or other sampling distributions. Independent publication-priority and scientific review have not been performed. The supplied software checks finite examples only.

Self-review: passed. Independent audit: not yet performed.
