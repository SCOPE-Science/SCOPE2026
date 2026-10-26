# Self-review

## Correctness — PASS
The Dirichlet covariance identifies the reproducing kernel exactly. Convexity reduces the negative kernel mass to a vertex; positivity of the interior density supplies strictness. Beta recurrences give the all-parameter exact formula. For the fixed-total-mass scaling, beta-normalizer expansion, a digamma tail identity and a separate truncated first moment derive both the logarithmic and constant terms; Dirichlet/gamma central limits with second-moment control establish the other limits. The checker's exact rational tests verify kernel moment identities and beta integrations but are not substitutes for proofs of infinite limits.

## Originality — PASS (provisional historical priority)
Griffiths–Spanò 2010 develops Dirichlet polynomial kernels, not the sharp L1/L-infinity affine projector norm or concentration boundary. Xu 2013 develops multivariate Jacobi bases but not the endpoint norm. The public 2026 simplex projector result covers alpha=1 only; that already-known case is expressly not the new contribution. The exact alpha=lambda/n double scaling and explicit log(n)/n digamma correction do not follow from the alpha=1 theorem or from the kernel representation without further beta-tail analysis. Separate searches for aliases, stronger multivariate Jacobi Lebesgue constants, and parameter limits found no demonstrated covering theorem. Residual risk: older equivalent weighted orthogonal polynomial Lebesgue constants under other names.

## Mathematical value — PASS
For weighted local least-squares approximation, the full sharp amplification determines whether rare boundary-mass data can generate negative fitted values and how that risk varies with concentration. The fixed-total-mass regime yields bounded endpoint instability despite increasing dimension; the fixed-coordinate-concentration regime yields linear instability. The logarithmic boundary correction identifies the precise finite-size approach in the sparse Dirichlet regime, not merely a routine special-value computation.

## Limitations and closest literature
The result is limited to symmetric Dirichlet measures and degree-one orthogonal projection. It neither asserts a uniform-in-lambda error nor covers higher degrees. Closest sources: Griffiths–Spanò, arXiv:1003.5131 (full introduction, kernel framework and Proposition 2.1 examined); Xu, arXiv:1309.1510 (Jacobi/Hahn framework examined); Aktaş–Xu, arXiv:1111.2994 (Jacobi simplex setting examined); *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (2026), full RESULT.md examined (alpha=1 case covered). Bibliographic priority requires independent review.

Self-review: passed. Independent audit: not yet performed.
