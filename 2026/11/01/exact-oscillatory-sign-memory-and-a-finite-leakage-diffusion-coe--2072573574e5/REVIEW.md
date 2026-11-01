# Scientific review: exact signed correlations of a paired tent map

## Correctness — PASS

The map and stationary density are explicitly defined on the full real interval. The six branch images induce a stochastic matrix with entries in \(\mathbb Q(\sqrt3)\). Symbolic direct checks confirm that the matrix has unit row sums, that the stationary weights are invariant, that \(P^5\) is strictly positive, and that the restriction to odd observables has characteristic polynomial \(\lambda(\lambda^2-2q\lambda+2q^2)\). The three initial covariance values satisfy the quadratic recurrence, yielding the all-lag formula and the rational generating function. Summability gives the exact finite-time correction and Green–Kubo variance. The ordinary stationary primitive finite-state Markov-chain CLT then establishes the Gaussian limit. The attached checker successfully verified all crucial nonstandard algebraic identities. Endpoint exceptions have zero stationary mass.

Risk: the CLT relies on the well-established finite-state Markov-chain theorem and the proof that uniform conditional densities on cells produce a Markov itinerary. These steps are described rather than independently re-proved from first principles.

## Originality — PASS within inspected evidence

Horan, *Asymptotics for the second-largest Lyapunov exponent for some Perron–Frobenius operator cocycles* (arXiv:1910.12112), Definition 4.1 and Section 4.6/Proposition 4.16 already provide this map, the exact \(n=1\) postcritical Markov partition, transfer-matrix framework and eigenvalue information. The present claim gives **different, observable-weighted** data: the exact coefficient and phase in each sign covariance, its rational all-lag generating function, the precise finite-leakage long-run variance and finite-time offset, and an explicit quantitative failure of a two-state Markov description. Those are not stated in the inspected source. Eigenvalues of the original six-cell transfer matrix do not by themselves supply the stationary sign projections or the coefficients.

Dolgopyat–Wright (arXiv:1011.5330) treats a vanishing-leakage approximation to diffusion coefficients; González-Tokman–Peters (arXiv:2406.09672) treats random driving and averaging; the later *Jumping for Diffusion in Random Metastable Systems* treats small-leakage limiting diffusion. Their accessible statements and pertinent sections do not give the exact specified finite-parameter sign law. The closest recoverable earlier mathematical findings address skew tent, baker, or affine maps with distinct transfer relations. Search failure is not a proof of novelty.

Residual risk: the result may be obtainable by straightforward algebra from Horan's pre-existing matrix, and another publication may have performed this exact sign-observable calculation without indexing it under the terms searched.

## Mathematical value — PASS

Left/right residence is the defining physically meaningful two-region observable in paired tent metastability. The exact finite-leakage fluctuation strength \(1+2/\sqrt3\), sign-changing lag response and failure of a one-step two-state reduction are quantitative calibration data not supplied by asymptotic small-leakage approximations. In particular, the two-state surrogate matches lag one yet fails already at lag two; this is an explicit observable-relevant boundary of coarse Markov models. Its complete all-lag law and finite-time correction make it more than a numerical point estimate or a restatement of pre-existing eigenvalues. The claim is deliberately restricted to a natural already-recognized Markov resonance rather than an arbitrary grid or parameter slice.

Limitations: no general finite-leakage parameter formula and no claim to a new general central limit theorem or newly discovered Markov partition. The priority risk from derivability within prior transfer-matrix machinery remains relevant to originality and value.

Self-review: passed. Independent audit: not yet performed.
