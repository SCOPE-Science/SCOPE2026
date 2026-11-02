# Self-review

## Correctness — PASS

The object is the scalar first-step sketched harmonic Ritz quotient for a fixed real SPD matrix, a fixed non-eigenvector and iid real Gaussian sketches. Orthogonal Gaussian projections produce the exact translated/rescaled Student distribution for the reciprocal, with independent chi-square and normal factors. Its smooth positive density at the origin yields exactly the \(t^{-1}\) two-sided tail, separate divergent positive/negative means, and the sharp order-one moment boundary. Symmetric density-tail decomposition yields the small-characteristic-function expansion, which proves the nondegenerate Cauchy limit for averages. All boundary cases are explicit: a genuine eigenvector gives a constant positive quotient, while every finite sketch dimension is covered. A standalone extracted verifier executes 1,562 algebraic, numerical, probability and limit-law checks; this is corroboration, not a substitute for the proof.

## Originality — PASS, with residual priority risk

The nearest primary article is Güttel--Liu--Nyman, arXiv:2607.10354v1, Section 5.3, equation (23), where the sketched reciprocal and a sufficient positivity condition are present. Those statements do not imply the claimed nonintegrable first moments and nondegenerate averaged Cauchy limit without additional distributional and heavy-tail analysis. Nakatsukasa--Tropp, arXiv:2111.00113, addresses the nonharmonic sketched Rayleigh--Ritz projection and embedding-based accuracy; Simoncini--Wang (2025) addresses sketched recurrence stabilization, not this scalar exact law. Classical Student and Cauchy attraction theory provide ingredients and are not claimed as new. Residual risk: an older specialized study of Gaussian ratios or sketched harmonic methods may already have explicitly stated this consequence. The result is offered as self-reviewed, not historically certified.

## Mathematical value — PASS

The precise reliability issue is substantive: no finite Gaussian sketch dimension gives a finite mean magnitude for a non-eigeninput harmonic Ritz scalar, and replication by naive averaging fails even when a negative Ritz event is rare. The explicit Pareto coefficient and Cauchy scale quantify the failure, while the ordinary Rayleigh--Ritz comparison isolates inversion of the sketched harmonic product as the mechanism. This informs the use of truncation, denominator safeguards, or conditional embedding requirements in harmonic sketch algorithms, without claiming any global-method breakdown.

## Scope and limitations

Real SPD data; fixed non-eigenvector direction; finite integer Gaussian sketch width; independent exact-arithmetic runs; one harmonic Ritz scalar. No statement is made about other sketch distributions, adaptively selected vectors, higher-order Krylov reductions, finite precision, or convergence of complete restarted schemes. Numerical checks do not establish historical priority or an independent audit.

Self-review: passed. Independent audit: not yet performed.
