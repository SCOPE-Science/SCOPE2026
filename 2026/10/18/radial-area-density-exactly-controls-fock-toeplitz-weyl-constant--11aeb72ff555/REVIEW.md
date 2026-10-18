# Scientific review: Radial area density exactly controls Fock Toeplitz Weyl constants

## Correctness — PASS

The theorem specifies the radial \(C^2\) weight, strict two-sided real-Hessian bounds and the fixed symbol \(f(z)=(1+|z|^2)^{-\beta/2}\). Angular moment diagonalization and covariance order the eigenvalues. The second derivative of the logarithmic moment density bounds its mass by a Gaussian uniformly around its unique saddle, and its denominator from below; thus the symbol expectation differs by relative \(O(n^{-1/2})\). The saddle mesh, convex secants and monotone counting-function inversion establish all asymptotic/iff conclusions. The numerical verifier checks finite moment identities only; it does not prove the infinite theorem. Boundary cases \(m>0\), \(\beta>0\) and the two contrasting examples were checked against the explicit derivatives.

## Originality — PASS, with residual risk

Xu–Dong (arXiv:2609.16970v1, §5) gives quadratic sufficient Weyl laws and a radial uniformly Hessian-bounded counterexample, and explicitly asks for weaker necessary geometric hypotheses. The all-radial iff, complete cluster interval and uniform saddle remainder are not those statements or an immediate corollary. Bdarneh (arXiv:2609.20652, Theorem 6.2), inspected in the full text of the relevant theorem and later counterexample, gives the general moment formula but no Weyl coefficient iff. Searches of published mathematical records for the moment-ratio, slope, curvature-density, spectral counting and cluster-set aliases found no identified covering theorem. Own previous claims involving symbol oscillations on fixed Gaussian Fock spaces have different assumptions. The self-review cannot eliminate undiscovered broader Weyl literature; arxiv:2603.10879 was accessible at abstract level only. Independent expert review has not occurred.

## Value — PASS

An explicit primary question asks what replaces quadratic asymptotic geometry in this spectral law. The theorem supplies a natural exact invariant (half the limiting disk-averaged Laplacian), necessary and sufficient under the whole radial bounded-Hessian class, with pointwise singular-value tracking and a complete nonconvergent cluster-set description. These are structural rather than arbitrary special-case computations.

## Scope and reproducibility

The result concerns one complex variable, positive strictly decaying radial symbol and uniformly convex radial weights. Finite numerical checks are supplementary and do not certify universal claims. The bibliography and fully analytic argument appear in `RESULT.md`; independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
