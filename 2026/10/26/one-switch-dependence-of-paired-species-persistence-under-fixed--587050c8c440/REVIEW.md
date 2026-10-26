# Scientific review: fixed-quota pairwise species persistence

## Correctness

**PASS.** Exact counting of uniform retained subsets yields the covariance in equation (1). The key ratio identity (3) is a direct factorial cancellation, and the sign of its increment is controlled by the strictly decreasing affine quantity \(h(N-q)-ab\). This gives a one-turn ratio sequence with initial value one; strict partial overlap guarantees a negative terminal value. Nested and disjoint cases are dealt with separately, and the five-partner cutoff follows from \(ab\ge(h+1)^2\ge4h\). A standard-library program checked the formulas by exhaustive subset enumeration through eight partner species and the resulting phase classification for all feasible parameter quadruples through fifty species. All computations use integer or rational arithmetic; no computation is claimed to prove the infinite result. The theorem excludes empty/full neighborhoods and states the degenerate endpoint behavior.

## Originality

**PASS, with residual bibliographic uncertainty.** Full text was examined in Memmott–Waser–Price (2004) and Burgos–Ceva–Hernandez–Perazzo (2008). Both investigate ecological random partner-loss robustness but discuss attack-tolerance profiles and nestedness rather than the pairwise fixed-quota covariance sign sequence. Joag-Dev–Proschan (1983), available at abstract level, establishes negative association for disjoint coordinate families under sampling without replacement, which explains the disjoint-set portion but not the strict-overlap one-switch transition. Published mathematical-record searches for the explicit binomial ratio, co-survival aliases, and fixed-size hitting events returned superficially close fixed-composition dependence and occupancy-covariance findings, but none in the inspected summaries implies the exact result on overlapping neighborhood-hit indicators, the phase threshold, and its sharp size-five instance. An uninspected general hypergeometric association theorem may nevertheless contain an equivalent formulation; this remains a specific residual risk, and searches do not certify uniqueness.

## Value

**PASS.** Fixed-proportion random extinctions are a standard ecological null model. The natural question is whether two plant species that share pollination partners persist together or compete statistically under a fixed survival quota. The result establishes a sharp dependence phase boundary, proves at most one reversal as the quota changes, and locates the smallest possible network; the independent-deletion comparison isolates the sampling-protocol mechanism. This is a motivated structural distinction between first-moment attack-tolerance curves and pairwise risk, not an arbitrary finite table or a restatement of negative association. It does not infer a whole-community tail ordering from one pairwise covariance.

## Closest literature and limitations

Memmott et al. 2004, DOI 10.1098/rspb.2004.2909; Burgos et al. 2008, arXiv:0809.3681; Joag-Dev and Proschan 1983, DOI 10.1214/aos/1176346079. Full text was available and read for the two ecological sources. The negative-association source was materially accessible at the abstract level, so exact broader coverage in its full text was not ruled out. The result is restricted to uniform fixed-count sampling, immutable bipartite edges, and survival when at least one interaction partner remains. Reproducibility files are included.

Self-review: passed. Independent audit: not yet performed.
