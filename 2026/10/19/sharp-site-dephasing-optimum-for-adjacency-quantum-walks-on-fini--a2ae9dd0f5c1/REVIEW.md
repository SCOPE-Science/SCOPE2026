# Scientific review: exact optimal star dephasing

## Correctness
PASS. For a star with \(m\ge3\) leaves, hub–leaf block equations decompose into one trace mode, a trivial three-dimensional mode, \(m-1\) copies of two- and three-dimensional standard modes, and a residual off-diagonal leaf sector. Their characteristic polynomials give the full spectrum with the correct total dimension. An exact sign identity on the standard cubic gives a strict upper bound for every nonoptimal dephasing rate; a shifted Routh–Hurwitz test places all competing eigenvalues strictly behind the optimal root. The two-leaf path is handled separately using the quadratic exceptional point and a shifted cubic check. Symbolic cases \(m=2,3,4\) and full-matrix numerical checks through \(m=8\) corroborate the proof. Finite checks are not used as infinite-dimensional proof.

## Originality
PASS in self-review, with residual risk. The 2022 Bressanini–Benedetti–Paris and 2025 Adithya–Nokkala–Piilo–Meena investigations use the star and site dephasing, but employ the *Laplacian* Hamiltonian and study quantum–classical distance or initial-state-sensitive stability, without the tight-binding adjacency generator's full Liouvillian spectrum or its exact unique noise optimum. Caruso's 2014 optimization involves a quantum stochastic walk with edge-jump noise and a trapping-efficiency objective. A different exact complete-graph calculation does not imply the star's multi-sector spectrum or its opposite size dependence. Relevant research-database, terminology, equivalence, and literature searches found no stronger identified coverage. The remaining risk is an implicit exact computation in older star-network Haken–Strobl spectral literature; search absence is not a proof of uniqueness.

## Scientific value
PASS. The known qualitative inversion of relaxation speed under strong dephasing motivates a quantitative noise-design question. The result uniquely optimizes the full Liouvillian asymptotic rate at every star degree, identifies a genuine low-degree exceptional point, and establishes the opposing \(\sqrt m\) and \(m^{-1/2}\) scaling laws for optimal noise and attainable relaxation rate. This is not a fixed-size numerical table or a replacement of a graph parameter in a universal formula: the proof handles multiple competing invariant spectral sectors. The result does not optimize any particular finite-time observable.

## Closest literature and limitations
Bressanini et al., arXiv:2204.01836; Adithya et al., arXiv:2507.17880; Caruso, DOI:10.1088/1367-2630/16/5/055015. The specific result requires a uniform adjacency Hamiltonian and uniform site-dephasing; it is not a theorem for onsite-detuned, Laplacian, weighted, or non-Markovian quantum walks. Independent originality and correctness assessment remain pending.

Self-review: passed. Independent audit: not yet performed.
