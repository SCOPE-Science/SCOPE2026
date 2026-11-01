# Scientific review

## Correctness — PASS

For \(1/2<a<1\) and \(0<c<1/2\), each branch sends points to the opposite half, so two-step dynamics reduces exactly to the continuous increasing polynomial \(G_{k,c}(u)=1-2c(1-2ku^2)^2\). Fixed points solve \(c=(1-u)/[2(1-2ku^2)^2]\). Its derivative has exactly the asserted one-minimum, one-maximum geometry once \(k>3/8\), and gives one, two, or three distinct roots according to the strict fold comparisons. Since every iterate of a continuous increasing self-map of an interval is monotone after its first step, all trajectories approach such a root and no higher periods exist. Return derivative signs classify all hyperbolic orbits. The exact cusp factorization and quartic recurrence give a rigorous reciprocal-square proof of the signed \(n^{-1/2}\) asymptotic. Symbolic identities and a broad rational exact-root sample passed in the embedded verifier; samples only support the proof, not replace it.

## Originality — PASS within inspected evidence

The complete author-accessible text of Lawnik, Moysis and Volos (2023), DOI 10.3390/sym15071311, was examined at its defining equation (15), fixed-point lemma, phase diagrams, Lyapunov diagrams and conclusions. It proves fixed-point freedom and presents numerical parameter experiments, but does not give the exact two-cycle census or cusp asymptotics. Published studies of piecewise-smooth unimodal bistability address different defining families. Comparable indexed results on a fractional-exponent fixed-point diagram of the same paper, a rational neuron map, and planar Duffing/Bogdanov maps do not imply this claim. An author's related 2024 article was accessible only through abstract and catalog information; its full-text comparison remains a priority risk, as does unindexed literature.

## Mathematical value — PASS

The source treats absence of equilibria and Lyapunov diagrams as evidence relevant to chaotic behavior. The present theorem identifies a natural parameter rectangle where all orbits instead converge to two-cycles, and separates a physically meaningful bistability wedge from a codimension-two cubic cusp. It supplies global dynamics, basin separation, exact algebraic transition boundaries, and an unusual universal critical clock, rather than a numerical refinement of a known example. The rational two-attractor witness makes the structural feature independently reproducible.

## Closest literature and limitations

The defining paper [1], 2005 piecewise-smooth bistability study [2], and 2024 follow-up [3] are cited in RESULT.md. The present proof is self-contained but establishes no statements for other powers, other partitions, stochastic perturbations or cryptographic security. The later paper's full manuscript was inaccessible, and an independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
