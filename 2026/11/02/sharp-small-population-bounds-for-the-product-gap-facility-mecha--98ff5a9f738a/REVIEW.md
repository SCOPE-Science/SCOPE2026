# Self-review

## Correctness (PASS)

The exact subset-weight factorization \(w_i=P/g_1,P/g_k,P(g_{i-1}^{-1}+g_i^{-1})\) is derived directly from deleting each report; the sum is \(Z_k=2PH\). Every omitted report is served by its neighboring selected report(s), producing the exact expected-cost identity. A pigeonhole and triangle-inequality argument gives the unrestricted optimal comparator \(\delta\). The normalized gap proof handles an endpoint shortest gap and an interior shortest gap, including multiple minimizers, separately. Explicit positive-gap sequences approach the two ratios and the strict inequalities prove nonattainment. Exact independent enumeration of 87,376 finite profiles agrees with the formula and bounds; the infinite argument is analytical.

## Originality (PASS, qualified by residual risk)

Jia, arXiv:2608.19633v1, Sections 3–5, and Chan–Lin–Wang, arXiv:2608.22484v1, Section 5, establish the full-population \(2k\) bound and its large-population tightness. Their statements do not entail the sharp \(k+1\)-agent factor, its interior shortest-gap refinement, or the exact omitted-agent probabilities. The literature also contains small-population results for alternative mechanisms, including Inverse-Square and Pick the Loser, which do not imply these Product-Gap equalities. A previously deposited two-facility finding covers \(k=2,n=3\), so this theorem intentionally starts at \(k=3\). Bibliographic, equivalent-formulation, and stronger-implication searches found no direct prior equivalent; unindexed earlier work remains possible.

## Value (PASS)

Exactly one more agent than facilities is the first nonzero-optimum population size for distinct reports. A mechanism whose unrestricted guarantee is \(2k\) exhibits a substantially smaller sharp bound, with a further nontrivial distinction between endpoint and interior shortest gaps. The full omission distribution supplies exact risk probabilities and clarifies how spacing rather than population multiplicity drives efficiency. This is a natural, parameter-uniform structural boundary, not a numerical check at an arbitrary fixed size.

## Research limits

The result is for true distinct positions on a line, fixed \(k\), nearest-facility utilitarian cost, and the named Product-Gap mechanism. It neither improves the global \(2k\) bound nor claims strategyproofness for \(k\ge4\). The related work's other mechanisms are not being reanalyzed.

Self-review: passed. Independent audit: not yet performed.
