# Scientific review: finite Charlier--Hermite cutoff transition

## Correctness

**PASS.** The finite Hermite representation follows by the ladder identities and a diagonal gauge. A bidiagonal factorization proves strict positive definiteness. The tridiagonal determinant recurrence gives exactly \(D_N(1;t)=t^{N-1}(t-N)\); min--max interlacing with the displaced oscillator ensures only the bottom eigenvalue can cross \(1\). The triangular inverse produces an exact reciprocal spectral trace. In the subcritical regime a Poisson expectation, exponential concentration and the spectral gap \(\lambda_{j,N}\ge j\) for \(j\ge1\) yield the prefactor with relative \(O_\rho(N^{-1})\) error. In the supercritical regime a singular-value lower bound and a top-edge sine trial vector give a matching scaled limit. The standalone arithmetic checker passed 250 supplementary assertions, but correctness does not rely on finite sampling.

## Originality

**PASS under the inspected scientific evidence, subject to historical coverage risk.** The closest motivating work, Williams--Ortelli--Silva (arXiv:2609.17970), develops the infinite displaced-oscillator spectrum, but does not study the finite-cutoff zero crossing or the \(t=\rho N\) least-eigenvalue regimes. Dominici's fixed-parameter Charlier asymptotics (arXiv:1406.6193 and the 2018 sequel) have different quantifiers and cannot directly imply the simultaneous degree/parameter laws. Nilsson's Charlier--Hermite transition (arXiv:1202.2557) addresses critical parameter-degree matching, rather than either outer regime. Recent mass-modified Charlier asymptotics (arXiv:2608.27495) concern another object. The Kuijlaars--Van Assche discrete zero-distribution study concerns bulk and maximal zeros; Krasikov--Zarkh treats inequalities for extreme zeros, but full equivalence to any present exact statement could not be resolved solely from the accessible abstract. Knessl--van Leeuwaarden (2015) gives exact immigration--death first-passage transforms and a critical Halfin--Whitt scaling, which shares the underlying polynomial but does not state the sharp fixed-ratio spectral laws. Actual semantic mathematical-record searches and accessible historical claim inspection yielded no same or dominating statement. Unindexed queueing or birth--death analyses remain a risk; failed searching is not proof of global novelty.

## Value

**PASS.** Finite Hermite cutoffs are the canonical spectral approximation to the displaced oscillator. The exact equality \(\mu_N(N)=1\) locates a natural phase boundary with no asymptotic uncertainty. The sharp exponentially small prefactor below the threshold and the scaled spectral edge above it quantify very different finite-dimensional approximation regimes for a single family. The exact reciprocal trace supplies a reusable formula for estimating the spectral floor. The finding does not purport to resolve the near-critical window or product-uncertainty minimization.

## Closest work and limitations

The full relevant passages of arXiv:2609.17970, arXiv:1406.6193, arXiv:2608.27495, and the Charlier-to-Hermite article arXiv:1202.2557 were inspected. The 2018 Dominici article was consulted at its actual PDF pages. The 2015 Knessl--van Leeuwaarden first-passage and Halfin--Whitt sections were read in full HTML. The 1999 Kuijlaars--Van Assche and 2008 Krasikov--Zarkh comparisons were limited by material accessibility. Parameter-uniform critical-window asymptotics and arbitrary Hermite masks remain unproved. The finding is a mathematical proof with self-review, not independent validation.

Self-review: passed. Independent audit: not yet performed.
