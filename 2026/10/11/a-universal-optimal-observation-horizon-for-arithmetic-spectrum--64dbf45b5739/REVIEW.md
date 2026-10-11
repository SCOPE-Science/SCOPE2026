# Same-model scientific review

## Correctness — PASS
The claim fixes the state dimension, positive arithmetic spectral rates, two sensor rows, temporal grid, and equal-variance noise normalization. Subtracting the scalar offset from each slope row yields value/derivative confluent Vandermonde data at the geometric nodes. Tracking the row factors gives the exponent \(\beta_k\) and product multiplicities. The product is nonzero on \(t>0\), proving recovery. The log-derivative equation has a strictly monotone right side, giving a unique global information-determinant optimum. Uniform Riemann sums and a nonzero limiting derivative justify the \(O(k^{-1})\) scaled-spacing error and universal finite horizon. Exact rational determinant tests at 16 parameter-grid combinations and numerical root checks agree; numerical tests are not the infinite proof.

## Originality — PASS, with residual risk
The source arXiv:2603.20641v1 was inspected in its entirety where relevant (Sections 3.1–3.2 and Appendix A). It proves generic delay representation, not the explicit all-size arithmetic-spectrum determinant or optimal-spacing asymptotic. Classical confluent Vandermonde identities are not claimed as new. Older optimal-design papers consider related exponential models and may hide an equivalent specialized calculation; the available closest 2006 abstract does not demonstrate it. Published-record searches on exponential sums, optimal spacing, geometric-node determinants, and delay observables and comparison against existing mathematical findings found no exact prior statement. This is a bounded literature comparison rather than a proof of global novelty.

## Mathematical value — PASS
Finite-delay reconstructibility alone does not specify how observation timing affects uncertainty. The theorem supplies an exact information-volume objective for arbitrarily many modes, proves uniqueness of the optimal spacing in a natural constrained design, and identifies an offset-independent finite limiting observation horizon. That horizon is an invariant design principle that can be used to initialize and benchmark reconstructions with a growing number of decay modes. It is not a free-parameter recoding of a known special case; the asymptotic constant and sharp uniqueness address a quantitative gap. The noise model, equal mesh, and arithmetic decay spectrum limit transfer to other systems.

## Closest sources and limits
Liu–Xiu, arXiv:2603.20641v1 (full relevant HTML); Bolotnikov, arXiv:1505.03574 (abstract, classical determinant background); Dette–Melas–Wong, Statistica Sinica 16 (2006), 789–803 (abstract only, exponential-regression design context). No claim of publication priority or independent verification.

Same-model review: passed. Independent audit: not yet performed.
