# Scientific assessment

## Correctness — PASS

Every eigenmode of the open path has strictly positive endpoint weight. The cyclic-space return identity follows from an exact finite-dimensional telescoping operator sum and the strict contraction of the no-click evolution on the cyclic subspace. A cyclotomic minimal-polynomial argument proves rational independence of all \((p-1)/2\) positive eigenvalues. Classification of the resulting nonproportional spectral-gap coefficient vectors establishes all possible phase collisions and their exact multiplicities for **every** \(\tau>0\), not merely numerically sampled times. The proof handles \(p=3\), which has no two-pair resonance. The packaged verifier checks 220 ladders and 43 direct Lyapunov means but is not treated as a universal proof.

## Originality — PASS, qualified

Grünbaum, Velázquez and the Werners (arXiv:1202.3903) already prove the general mean-return/spectral-support identity, which **implies the form** of the answer once the distinct sampled phases are known. It does not classify the prime-path eigenvalue gap resonances. The new assessed contribution is the exact, exhaustive arithmetic description and proof that all \(((p-1)/2)^2\) exceptional time ladders are disjoint, yielding precisely three possible mean values for primes at least five (two for the smallest odd prime). Sinkovicz et al. (arXiv:1411.0568) and Friedman et al. (arXiv:1603.02046) address broader monitored dynamics and different graph geometries; Riddell and Bertini (arXiv:2404.12100) treat cyclotomic independence in another model. Targeted searches found no exact matching prime-open-path classification. This is a scoped originality assessment, **not** a proof of priority; unlocated equivalent literature remains possible.

## Value — PASS

For monitored quantum transport, the exact location and possible overlap of resonant sampling times control abrupt jumps in expected first-return counts. Prime path sizes provide a natural, non-arbitrary regime in which a new rational-independence lemma makes a complete classification possible. The finding settles **all** positive sampling intervals and exact jump sizes for that family, unlike an isolated numerical example or merely restating integer quantization. Its value is mathematical/structural; no experimental gain or quantitative relaxation improvement is claimed.

## Limits and antecedent

The source that most closely dominates general methodology is arXiv:1202.3903. The classification is for endpoint-return measurements on uniform open paths only. The verifier requires NumPy and SciPy and is not independent formal verification. The first public motivating source date is 2012-02-17.

Self-review: passed. Independent audit: not yet performed.
