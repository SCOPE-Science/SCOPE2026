# Self-review

## Correctness — PASS

The generator is fully specified and reversible. Direct block multiplication gives all off-diagonal entries. Distinct-leaf quadratic discriminants are negative; diagonal entries are positive by the spectral theorem and positivity of the degree-four Taylor polynomial on the negative real axis. Weighted Cauchy–Schwarz proves 9AD>4C² for each one-hop cubic, so it decreases and has exactly one positive root. The exact three-state stable-but-nonpositive matrix was reconstructed; the standalone rational checker passed 387 configurations. No finite check is treated as the infinite proof.

## Originality — PASS

The exact all-rate one-edge cutoff and minimal three-state spectral-stability counterexample are not implied by the inspected generic SSP theory. Closest accessible local statement treats symmetric weighted-star graph Laplacians (the special case a_j=b_j); its proof and claim do not cover nonuniform stationary distribution nor the stable-but-negative reversible example. The 2011 two-step SSP study and 2014 explicit SSP study concern general timestep methods and bounds, not these star-generator entrywise identities. Searches of published mathematical records for reversed-edge, birth–death and directed-star equivalents found no stronger claim; this is best-knowledge originality, not a proof of absence.

The closest research backgrounds are Ketcheson–Gottlieb–Macdonald (2011), Gottlieb–Grant–Higgs (2014), and Higueras et al. (2014). The nonuniform bidirected-star claim genuinely extends the reversible-but-uniform-stationary specialization. The exact equivalence to the symmetric case only holds when inward and outward rates coincide. An unindexed stronger prior theorem remains a residual risk; comparison is based on actually inspected texts, not title matching.

## Mathematical value — PASS

The arbitrary bidirected star is a natural minimal model of hub-mediated state transitions with nonuniform stationary weights, rather than an arbitrary parameter slice. The theorem gives a complete all-rate positivity interval, identifies which matrix entries alone control failure, and exhibits the smallest reversible Markov chain where scalar RK4 spectral stability fails to protect probabilistic nonnegativity. These are motivated qualitative distinctions relevant to numerical propagation; the proof extends beyond mere computation.

## Limitations

The proof concerns completed linear RK4 only. It does not assert internal-stage positivity, a general-graph criterion, or independent external validation.

Self-review: passed. Independent audit: not yet performed.
