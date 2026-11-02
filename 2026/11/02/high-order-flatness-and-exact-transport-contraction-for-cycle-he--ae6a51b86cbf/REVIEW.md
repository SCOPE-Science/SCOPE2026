# Scientific review

## Correctness — PASS
The all-time identity follows from a sharp Dirac-edge reduction of the Wasserstein operator norm, the established circular transport median identity, strict radial ordering of the cycle heat kernel under an irreducible cooperative linear system, and a direct median shell count. Expanding the resulting nonnegative defect into distance shells yields the exact first nonzero derivative of order \(\lfloor(N+2)/4\rfloor\) and its residue-class coefficient. Fourier diagonalization gives the stated long-time profile. The finite checker supplies 140 separate LP comparisons, 589 exact-integer Taylor identities, and additional spectral checks. These computations do not replace the proof.

## Originality — PASS, qualified
The circular-histogram median minimization is **not** new: Delon–Rabin–Gousseau explicitly give it in arXiv:0906.5499, Eq. (12), and this step is credited as prior. Münch–Wojciechowski's arXiv:1712.00875v1, Theorem 3.8, concerns curvature lower bounds equivalent to exponential Lipschitz contraction; it does not calculate the complete cycle time profile or a high-order nonzero Taylor coefficient. Pedrotti's arXiv:2308.00516 concerns general coupling-based contraction bounds, not this cycle-dependent flatness law. Relevant published cycle results about \(\ell_4\) heat norms, finite-cycle Riesz transforms and cycle transport-space geometry treat distinct invariants. The assessed distinctive contribution is the sharp formula for how many initial derivatives of the cycle transport-contraction norm vanish as the circumference grows, with the explicit first coefficient and the all-time heat specialization. Older cycle-specific coupling results might overlap; this historical-priority limitation remains.

## Mathematical value — PASS
The exact order \(\lfloor(N+2)/4\rfloor\) is a natural graph-scale invariant measuring the first time the opposite side of a finite cycle can influence the best transport coupling. It explains strict eventual smoothing despite zero first-order coarse curvature on all sufficiently long cycles, and yields a family of exact benchmarks with arbitrarily high short-time flatness. The computation holds for every cycle size, not an arbitrary finite table or parameter slice.

## Scope and limitations
The graph is finite, unweighted and undirected, with generator \(L=2I-S-S^{-1}\), graph-distance \(W_1\), and real Lipschitz dual. The asymptotic error estimates keep \(N\) fixed. No conclusion is asserted for inhomogeneous cycles, other metrics or higher Wasserstein exponents, and historical priority has not received independent review.

Self-review: passed. Independent audit: not yet performed.
