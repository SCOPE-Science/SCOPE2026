# Review of strict last-coupon likelihood-ratio ordering

## Correctness

**PASS.** The multinomial coefficient formula enumerates the joint event exactly. Convolution closure of log-concavity is proved through finite Cauchy--Binet sums of Toeplitz \(2\)-by-\(2\) minors; the determinant expansion proves monotonicity. Its boundary term \(c_r c_{k-1}\) makes the comparison strict at every supported draw count for at least three types. The two-type case and equal-probability equality cases are handled separately. Independent rational EGF and state-DP implementations match for seven examples through completion time 22; the infinite theorem depends on the analytic argument.

## Originality

**PASS under currently accessible literature, with explicit priority risk.** Brown--Peköz--Ross (2008), Proposition 1(f), knows the joint law of completion time and last type, and Section 4 directly studies conditional tails by simulation. The present theorem does not pretend to discover that law: it proves an all-parameter strict pairwise likelihood-ratio order absent from the inspected results. Aki--Hirano (2012) give still broader waiting-time/rank formulas, while their likelihood-ratio test compares model parameters. Boneh--Hofri (1989) and Anceaume--Busnel--Sericola (2014) address general coupon collecting. An undiscovered equivalent ordering remains a realistic residual risk.

## Mathematical value

**PASS.** The result provides complete relative posterior-odds movement after any observed completion time in an unequal-probability coupon collector, a motivated question because exact conditional-tail estimation is a known problem. Strict likelihood-ratio order controls all increasing conditional completion-time functionals, not just averages or selected numerical instances; the theorem holds regardless of the other category probabilities.

## Limits

The result is limited to finite iid positive categorical probabilities and first-seen completion. Numerical checks are finite and independence of the scientific audit is not asserted. Some unknown literature may contain this particular implication in alternate terminology.

Self-review: passed. Independent audit: not yet performed.
