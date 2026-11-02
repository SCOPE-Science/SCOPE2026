# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed kernel according to longest initial coordinate agreement and mismatch proportions (q-1)/q^j, giving row absolute norm r_n+Σ|r_{k+1}-r_k| with r_{k+1}=r_k/q+(1-1/q)b_k; kernel symmetric so L1 equals Linfinity. Dynamic programming V_t(r) obeys max{c r+V_(t-1)(λr), c(1-r)+V_(t-1)(λr+c)} and reduces by induction to affine candidates crossing only at λ for even remaining depth and c for odd remaining depth (n>=2); c>λ assures rigidity, with depth-one exception. Pairwise bit-interaction expansion and finite geometric sums give exact formulas and slope. Independently enumerated all 2^n masks at q=3..7, n=1..10, computing signed kernel class rows with exact rational fractions and matching every norm, optimizer and parity formula. This finite enumeration corroborates but does not replace the Bellman induction.

## originality

PASS

PASS best-of-knowledge: The existing q=2 whole-level mask result is excluded. Osękowski 2013 establishes martingale/Haar sharp restricted weak-type inequalities, not these q>=3 finite strong endpoints and equality masks; Semenov–Uksusov 2012 and Wark 2015 study Haar multiplier spaces for binary Haar systems. No checked primary statement dominates this nonbinary full-mask optimization; full texts of two close multiplier papers remained unavailable, so priority remains qualified.

## value

PASS

PASS: Projection norm amplification under deleting entire levels of a branching martingale filtration is an intrinsic and motivated endpoint invariant. Closed norms, limit slope and full equality-mask rigidity quantify genuinely different behavior between binary and q>=3 branchings, valuable without a larger infinite-filtration result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
