# Scientific review

## Correctness — PASS
The exact orthogonal projection kernel is the coefficient of the two-coordinate mean-zero tensor product: \(K_{n,q}(d)=\sum_{i<j}u_i u_j\). Its Hamming-distance rows have binomial multiplicities, and the signs form a single strictly negative integer interval. A signed binomial CDF second difference shows that the absolute row sum equals four boundary masses. An explicit polynomial rescaling and fourth-moment uniform integrability prove the Gaussian and Poisson limits. The first Poisson cusp is an absolute-value sign change at index \(2\) and parameter \(2-\sqrt2\), with a nonzero exact derivative jump. The standalone exact checker passed all finite checks listed in `VERIFICATION.md`; those checks are supplementary, not a substitute for the proof.

## Originality — PASS, with residual risk
The 2007 primary source of the Hamming homogeneous-space representation (Scarabotti–Tolli, arXiv:math/0701533) gives decomposition machinery, not a sharp absolute endpoint norm or an alphabet-varying limit profile. Polyanskiy (arXiv:1309.3014) treats binary Fourier projections in \(L^p\to L^2\) contexts; Kirshner–Samorodnitsky (arXiv:1909.11929) treats binary Krawtchouk moment ratios for \(p\ge2\). Neither inspected statement is an endpoint \(\ell^1\) / \(\ell^\infty\) norm identity over \(q\ge3\) with a nonconstant Poisson–Charlier crossover and cusp. A previously recorded Boolean degree-two norm asymptotic does not imply the growing-alphabet crossover. Historical Krawtchouk/Charlier \(L^1\) calculations may contain a differently formulated identity; that is a genuine remaining risk, not disproved by search failure. A 2026 expository note on Hamming primitive idempotents was encountered only through indexed snippets; complete coverage was not established.

## Value — PASS
The invariant is the endpoint amplification of the canonical degree-two Hamming primitive idempotent, a central object in harmonic analysis of product alphabets. A full absolute Krawtchouk sum collapses to four boundary probabilities for every finite parameter. The two-parameter asymptotic identifies the exact regime in which Gaussian amplification universality fails, supplies the explicit Poisson replacement, and exhibits its first genuine nonsmooth threshold. This is more than extending the binary formula by substitution: the sparse-alphabet regime and its cusp are absent at fixed alphabet size.

## Closest literature and limits
Scarabotti–Tolli (2007), Sections 5.1–5.4; Polyanskiy (2013), Section 2; Kirshner–Samorodnitsky (2019), Sections 1–3. Classical Gaussian, Poisson, Krawtchouk and Charlier facts are used, not claimed as discoveries. The result is limited to degree two; equivalent historical representations under orthogonal-polynomial terminology remain plausible.

Same-model review: passed. Independent audit: not yet performed.
