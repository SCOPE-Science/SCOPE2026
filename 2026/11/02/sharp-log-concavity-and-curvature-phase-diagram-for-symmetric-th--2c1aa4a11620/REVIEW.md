# Scientific assessment: symmetric three-normal curvature and log-concavity

## Correctness — PASS

For positive satellite and center weights and any positive common variance, direct Gaussian factorization reduces the log Hessian to \(-1+bF_k(u)\) with \(u\ge k>0\) and \(F_k(u)=(u+k^2)/(1+u)^2\). The derivative \(F_k'(u)=(1-u-2k^2)/(1+u)^3\) gives the exact global supremum and every location attaining it. Solving the zero-curvature equation separately on \(k\ge1/2\) and \(k\le1/2\) gives two strictly decreasing, disjoint root parametrizations that meet at \(r_*=e^{3/2}/2\), establishing one sharp crossing and the principal-branch Lambert formulas without assumptions about local extrema. An elementary power-series bound proves the \(r=1,b=4\) example strictly unimodal, despite positive log curvature. Orthogonal Gaussian factorization verifies the multivariate extension. The accompanying checker produced 283 passing symbolic/numerical assertions; the universal claims rely on the explicit algebra and inequalities, not parameter sampling. Scientific limitations: no claims for asymmetric locations, general weights or heteroscedasticity.

## Originality — PASS, subject to historical priority

The motivating Okahara–Kobayashi paper proves a sharp *number of modes* upper bound, not a sharp *global curvature* or *log-concavity* classification. Its Sec. 6 contains the general posterior-variance Hessian identity, and its Appendix D treats curvature of free-energy branch functions; neither constitutes the explicit optimizer switch and two-piece Lambert phase boundary proved here. Earlier Okuno–Kabata and Ray–Lindsay works likewise concern modal counts and ridgeline geometry. Claims are separated at the level of their mathematical implications, not title similarity. Searches using three-normal log-concavity, Gaussian posterior variance, symmetrical satellite weights, Lambert branches, and unimodal/non-log-concave witnesses found no equivalent exact two-parameter theorem. Prior general Gaussian-mixture curvature identities are not claimed new. The literature search was targeted, not exhaustive; a further specialized source or an implicit specialization of a general result could alter historical priority, and independent scholarly review is outstanding.

## Mathematical value — PASS

A shared-variance Gaussian mixture is a basic statistical model, but modal count alone does not identify whether its density is globally log-concave or give a quantitative strong-concavity constant. The result completely classifies this natural symmetric three-component family, including the optimizer-location bifurcation and the precise sharp transition as satellite weight and separation vary. This supplies exact curvature information relevant to density shape and log-concavity-based inference/sampling assumptions, and the concrete strictly unimodal non-log-concave law shows why the two notions cannot be interchanged. The classification is self-contained and covers continuous two-dimensional parameter ranges rather than an arbitrary numerical slice. It does not imply new global results for general three-component mixtures.

## Closest literature and limitations

- R. Okahara and K. Kobayashi, arXiv:2610.15369v1 (2026-10-11): at most four modes for three common-covariance Gaussian components; at most three for collinear means. Section 6 gives posterior-variance Hessian identity; does not give global maximum-curvature or Lambert log-concavity boundary.
- A. Okuno and Y. Kabata, arXiv:2607.17506v1 (2026-07-20): unconditional eight-mode bound; no identified implication giving this exact curvature phase diagram.
- S. Ray and B. G. Lindsay, arXiv:math/0602238 (2006), *Annals of Statistics* 33 (2005): ridgeline and curvature tools for modal geometry; general framework is not equated with the claimed exact symmetric three-normal classification.

Residual priority risk concerns unlocated specialized Gaussian-convolution log-concavity results. The proof's symbolic checker is ancillary; no independent verification or historical-priority certification has occurred.

Self-review: passed. Independent audit: not yet performed.
