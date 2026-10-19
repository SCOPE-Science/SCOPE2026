# Scientific review: sharp bridge placement in two-community SIS networks

## Correctness — PASS

The statement fixes simple, undirected, unweighted complete communities of identical size and exactly \(k\) distinct cross edges, \(1\le k\le n\). The matching lower bound follows directly from two Perron mass inequalities \(\lambda(\lambda-n+1)Y\ge kX\) and its converse, with equality precisely at degree-one incident vertices. The star upper bound follows from the Schur complement, the trace bound \(\operatorname{tr}(RBRB^{\mathsf T})\), and exact \(k^2+k\) extremal bridge-degree square sum. A rank-one star saturates both inequalities, and the positive resolvent determines a unique spectral root. The asymptotic bridge-density window is obtained by taking limits in these exact equations. For the deterministic SIS map, monotonicity, a Perron Lyapunov inequality at equality, strict radial subhomogeneity, and sandwich iterates establish the extinction/endemic dichotomy. The decisive rational four-site comparison is \(43/169>0\) for the matching polynomial and \(-128151/28561<0\) for the star polynomial. Numerical checker: 5,421 graph configurations plus nine asymptotic comparisons passed. Finite checking alone does not prove arbitrary-size claims.

## Originality — PASS, qualified

The full available text of Hoang–Nguyen (2026), arXiv:2607.14048, supplies a community-level spectral threshold set and the universal inequality \(\tau_g\ge\tau\). Neither that theorem nor its numerical evaluations proves extremizers over all placements of a prescribed cross-edge budget. A published work on fastest-mixing chains explicitly compares the same matching/source clique connection patterns but analyzes stochastic-walk conductance and optimized mixing gaps, not the unnormalized adjacency Perron threshold. A 2026 spectral-supersaturation study uses stars/matchings in Turán parts, which is not the fixed pair-of-cliques contact network. published-finding corpus searches for the source, the alternative spectral statements and exact bridge formulas did not reveal a dominating equivalent record. The conclusion is a best-knowledge literature comparison rather than certified global novelty; unindexed spectral extremal results remain a real residual risk.

## Mathematical value — PASS

The fixed-budget optimization resolves a concrete missing dimension in the community-threshold perspective: identical local thresholds and identical cross-edge counts can produce sharply different global transition ratios. Both sharp extremizers are classified, all intermediate placements are bounded, a nonvanishing large-size excess-spectral gap is identified, and an exact small counterexample exhibits opposite long-term mean-field SIS behavior at the same rational rates. These are structural applied-network results rather than a mere recomputation of a single adjacency eigenvalue. In particular, the proof explains *why* bridge concentration increases SIS risk through a sharp degree-overlap bound.

## Prior-art proximity and limits

Closest material: Hoang–Nguyen, arXiv:2607.14048 (2026-07-15); *Geometric bounds on the fastest mixing Markov chain*, DOI:10.1007/s00440-023-01257-x; *Strict spectral supersaturation for cliques*, arXiv:2610.03337. Generic spectral graph inequalities and SIS stability theory are established prior art. A specialized prior theorem for this exact constrained class might be unindexed. The result assumes complete equal communities and a deterministic mean-field map, not infinite persistence of finite-population Markov epidemics.

Self-review: passed. Independent audit: not yet performed.
