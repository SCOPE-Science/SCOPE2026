# Scientific review: inverse fractional-delegation feasibility

## Correctness

**PASS, subject to the explicitly stated fixed-retention model.** The quantity delegated by agent \(j\) is \(c_j=(1-\tau_j)w_j/\tau_j\), and the amount of external delegation required at agent \(i\) is \(r_i=w_i/\tau_i-1\). Mass conservation forces \(\sum_iw_i=n\). These are precisely the supply and demand marginals of a bipartite edge-supported transport problem; max-flow/min-cut proves necessity and sufficiency of every neighborhood inequality. Since all \(\tau_j>0\) and all target weights satisfy \(w_j\ge\tau_j\), the transport-to-delegation quotient is defined, and the forward resolvent is unique. The complete-loopless specialization and the bidirectional-star extremizer follow by exact algebra. The self-contained exact-rational checks passed; they do not establish the infinite claim on their own.

## Originality

**PASS, with residual priority risk.** The closest model is Bersetche (2022, arXiv:2209.14128), which formulates forward fractional voting weights and equilibrium analysis but not target feasibility under fixed self-retention. Berend (2020, DOI 10.1140/epjds/s13688-020-00240-z, especially §5.3) asks a neighboring inverse-PageRank design question, but supplies an approximate optimizer, particular necessary obstructions and a self-loop-inclusive complete-graph construction, not this exact arbitrary-trust-network criterion. Gölz et al. (2018) use fully delegated/terminal voter flows rather than mandatory fractional casting at every transit vertex. Utke and Schmidt-Kraepelin (2023) use designated casting sinks and branching-based randomized rules. Garcia and Romance (2021) pursue unweighted graph realization of ordinal rankings rather than fixed-support quantitative weights. Alouf-Heffetz et al. (2024) study redirecting edges to manipulate the approval-election winner rather than exact fractional weight-vector realization. This comparison concerns the actual implications of their models, not merely differing titles. The classical max-flow transportation criterion itself is not claimed as a new standalone lemma. Related specialist reverse-Markov or delegation work may contain an equivalent formulation not found in the inspected literature.

## Mathematical value

**PASS.** The map from edge delegation parameters to final weights is nonlinear through a resolvent, and its exact image matters for mechanism designers seeking to calibrate vote concentration subject to interpersonal trust. The theorem identifies that image for every finite directed network using a finite collection of cut inequalities and a constructive polynomial-time test. The all-size sharp ceiling shows that mandatory common self-retention together with the ban on direct self-delegation prevents any single voter from capturing more than half the ballot mass, with a concrete extremal protocol. The disconnected-triangle example proves why individual concentration bounds alone cannot replace the collective cut conditions.

## Qualifications and references

The mathematical claim is conditional on fixed positive retention, conservation, one original vote per agent, and zero allowed forwarding probabilities. It does not characterize power indices, winner outcomes, strategic incentives, or strict positivity on every trust arc. Direct comparisons were made against the full accessible primary texts of Bersetche (2022), Berend (2020), Gölz et al. (2018), Garcia and Romance (2021), Utke and Schmidt-Kraepelin (2023), and Alouf-Heffetz et al. (2024). An exhaustive publication-priority proof is not possible from literature searching, and no independent external scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.
