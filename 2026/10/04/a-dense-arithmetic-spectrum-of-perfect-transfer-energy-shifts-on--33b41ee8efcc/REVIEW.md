# Same-model review

## Correctness

**PASS.** The marked complete graph splits exactly into one antisymmetric eigenstate and a two-dimensional symmetric block. Perfect transfer first forces the symmetric block to return to its initial line, hence \(t=2\pi k/\alpha\). The remaining phase condition is exactly \(e^{-i\pi k\beta}=(-1)^{k+1}\). Reducing \(\beta=p/q\) shows that transfer is possible exactly when \(p,q\) have opposite parity, and then \(k/q\) must be odd. The inverse parametrization follows from \(\alpha^2=(\Delta-2n)^2+16\Delta\), while strict monotonicity of \(\beta(\Delta)\) proves the density statement. A standalone checker replays the reduced dynamics for many parameters.

## Originality

**PASS, narrowly scoped.** The direct source gives the exact spectrum and transition amplitudes and exhibits \(\Delta=2n\), but does not state a classification of all positive equal shifts. The weighted-join paper gives sufficient rational/parity constructions while allowing several weights to vary simultaneously, not the iff classification with every edge coupling fixed at \(2\). Later graph-potential work proves broad existence results in a larger potential space and likewise does not state this arithmetic one-parameter spectrum.

Targeted semantic-database and web searches for equal potentials on complete graphs, weighted self-loops, the Casaccino tuning, rational eigenphase conditions, and necessary-and-sufficient transfer conditions did not locate the displayed classification. The residual literature risk is that it may be an unstated specialization of a later general criterion.

## Value

**PASS.** The result changes the design picture of the source family: the published tuning is one simple member of a countable dense exact-transfer set. The theorem gives every admissible positive shift, every exact transfer time, and the minimum time, while keeping all physical couplings fixed. This is a natural complete classification of the source's one-parameter control problem rather than a routine recomputation of one fidelity value.

Same-model review: passed. Independent audit: not yet performed.
