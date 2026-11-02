# Scientific review: cut-information geometry of Gaussian Brownian endpoint bridges

## Correctness — PASS

The statement is fully quantified for any positive-semidefinite endpoint covariance and every interior deterministic cut. Conditioned Brownian bridge decomposition shows that the *whole left/right path* conditional mutual information reduces exactly to that of the two endpoint variables, with no mesh limit. In the positive-definite case, the posterior precision matrix is explicit and gives the claimed finite information formula. A single AM–GM inequality proves the unique maximizing cut, with the flat Markov case treated separately. For rank-one coupled endpoints, their conditional joint law is concentrated on a line even though both conditional marginals are diffuse; hence the conditional KL is infinite. For pinned singular endpoints, the conditional information vanishes. The KL chain rule proves the exact single-cut independent-gluing projection, not a claim of global Markovization. The packaged checker executes 10,704 exact-rational assertions and an analytic example; the proof, not finite testing, supports the infinite-path theorem.

## Originality — PASS, qualified

The October 24, 2026 Brownian-process bestiary motivates the boundary-condition family and describes independent splitting for ordinary Brownian motion, but does not quantify conditional information for the general two-endpoint Gaussian mixture or optimize its cut. The October 27 endpoint classification separately proves the qualitative Markov criterion (which is explicitly credited), while InfoBridge supplies general endpoint-information path-KL ideas and Gaussian-field literature supplies other relative-entropy identities. None of the primary full texts inspected states or dominates the joint package of the full conditional path-information profile, unique covariance-independent cut optimizer, and sharp finite/infinite degeneration. Search results for relevant mathematical records likewise did not directly cover the statement. This is not proof of absolute historical priority: Baker's 1970 article could only be inspected at abstract level, and broader older reciprocal-process information identities remain possible precedent.

## Mathematical value — PASS

A qualitative Markov/non-Markov division leaves unanswered *how much* the full continuous past and future communicate after the present is observed and which observation cut detects that dependence most strongly. The theorem supplies an exact natural relative-entropy diagnostic over an entire parameter cone, an optimizer depending only on endpoint marginal standard deviations rather than their correlation, and an abrupt infinite-information boundary at deterministically coupled nonzero endpoints. It is an intrinsic, sharply optimized path-level classification and exact information cost, rather than an arbitrary parameter substitution or standalone finite arithmetic check. Its single-cut KL-optimal gluing gives a concrete interpretation, while the narrow domain and information metric are clearly disclosed.

## Closest literature and limitations

- L. L. Raket, *A Bestiary of Brownian Processes* (arXiv:2610.33747v1; first posted 2026-10-24), Sections 3–4 and 6.1: motivating family and a Markov splitting example; no conditional information optimum.
- L. L. Raket, *Brownian covariances on an interval: a complete endpoint classification* (arXiv:2610.36762v1; first posted 2026-10-27), Theorem 2.1 and Proposition 3.2: explicit endpoint covariance representation and the known Markov criterion, not this quantitative information result.
- S. Kholkin et al., *InfoBridge* (arXiv:2502.01383), Sections 2, 4.1 and Appendix B.4: general reciprocal-bridge KL/MI; no optimal-cut classification of this endpoint cone.
- M. Schröfl and S. Floerchinger, *Relative Entropy and Mutual Information in Gaussian Statistical Field Theory* (DOI 10.1007/s00023-024-01522-2), especially Section 4.3: information between spatial subregions in a different setup.
- C. R. Baker, *Mutual Information for Gaussian Processes* (DOI 10.1137/0119044): abstract accessible, complete article inaccessible here; possible historical-priority risk explicitly retained.

Singular endpoint measures do not admit a finite conditional KL unless an endpoint is pinned. General non-Gaussian endpoint laws and the null-space pseudoinverse operator family are not covered. Finite checks are not independent certification.

Self-review: passed. Independent audit: not yet performed.
