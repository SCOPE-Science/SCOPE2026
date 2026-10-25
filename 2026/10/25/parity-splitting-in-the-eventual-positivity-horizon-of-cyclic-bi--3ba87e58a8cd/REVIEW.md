# Scientific assessment

## Correctness

**PASS (self-review).** The claim is restricted to sufficiently large integer cycle orders, the unnormalized graph Laplacian, and the *last* negativity threshold. Direct Fourier diagonalization gives the exact finite kernel, weighted first-mode domination makes the antipode its unique spatial minimum after a fixed scaled time, and derivative domination ensures a single final crossing. Uniform Taylor expansion of the discrete dispersion relation produces the even/odd correction; the separate term for odd cycles is the quadratic loss from sampling one half-step short of the antipode. The analytical proof includes controls of Fourier tails and does not extrapolate finite numerics to infinitely many cycles. The standalone checker passed 1,425 assertions. Risk: the proof invokes standard dominated-convergence/tail arguments rather than an explicit numerical lower bound on the sufficient cycle order.

## Originality

**PASS within available source comparison.** The closest source is Daners–Glück–Kennedy (arXiv:1511.05294v1, full text inspected), which gives general semigroup positivity criteria and examples but no quantitative cycle-family horizon or parity defect. The 2008 Ferrero–Gazzola–Grunau paper addresses biharmonic eventual local positivity in Euclidean domains; its inspected abstract does not determine finite-cycle crossover times. Related existing finite-graph results for bipartite, rook, triangular, and cocktail-party graph Laplacians concern other graph families and do not imply a cycle's \(n^4\) scaling coefficient or arithmetic correction. Dedicated similarity and literature searches did not identify statement-level coverage. Risk: specialized unindexed periodic-kernel or numerical-analysis literature has not been exhaustively ruled out; the 2008 paper was compared via its abstract rather than full text.

## Value

**PASS.** Eventual positivity of higher-order diffusion is a natural stability property not predicted by positivity of ordinary heat flow. The theorem quantifies exactly how the last negative entry disappears under graph-to-circle refinement, with a dimensionally correct fourth-power time scale and a nontrivial parity splitting induced by the discrete antipodal sampling geometry. The coefficient gap is a structural effect for infinitely many cycle orders rather than a single small-table constant. No claim is made for unrelated graphs or all early-time sign patterns.

Self-review: passed. Independent audit: not yet performed.
