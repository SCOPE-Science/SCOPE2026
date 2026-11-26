# Independent mathematical audit

## correctness

PASS

Re-audited the repaired theorem. A flip acts on the cut bonds. Maximal contiguous pieces have disjoint cut bonds, so checking allowed intervals is equivalent to checking all allowed subsets. A wall at j must evade both end intervals and be strictly lighter than all bonds at distance at most r; conversely such eligible walls cannot coexist on a block boundary, and a single such wall has lighter coupling than the opposite boundary. Whole-chain flip costs zero. For iid atomless bonds, the stationary indicators have mean 1/m (m=2r+1), are 2r-dependent, and have overlapping joint probability 2/[m(m+d)] for r<d≤2r by conditioning on the location of the union minimum. The variance sum verifies the displayed v_r, with v_r≥2r/[m²(4r+1)]>0; the finite-dependence CLT and ergodic theorem apply at fixed r. For N≥m the +1 in log₂ B exactly cancels the boundary correction in the mean. When N≤3r+2 the eligible interval has diameter at most r or is empty, giving the asserted Bernoulli law from its expectation. New independent script /workspace/reproductions/05_ising.py passed exact all-order, all-state and all-budget small checks (N=3..7, every coupling permutation) and exact rank checks for r=1,2; these corroborate, not replace, the proof. Frozen VERIFICATION.md and verify.py were inspected without running the supplied code.

## originality

PASS

The repaired claim expressly limits its advance to the explicit all-fixed-radius variance and the proportional-budget result in the specified open-chain range. The strongest inspected prior coverage is the one-spin weak-bond representation and the periodic r=1,2 marginal variance and Gaussian limits. Those ingredients are credited and not claimed distinct. The fixed-range table neither gives the arbitrary-r joint minimum formula nor covers the growing-r open-chain regime. The conclusion is limited to inspected evidence and does not certify priority.

## value

PASS

The repaired result gives quantitative information in two different regimes of a natural metastability count. The exact variance across all fixed cooperative budgets goes beyond the mere existence of a CLT or the first two previously calculated variances. In a separate proportional-budget range the open count has a fully specified non-Gaussian finite law rather than just a growth exponent. This is a useful boundary classification and does not assert results for all proportional budgets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
