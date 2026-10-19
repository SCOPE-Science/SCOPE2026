# Scientific review: additive-lag burst-deletion cumulants

## Correctness — PASS

The theorem explicitly specifies independent uniform \(q\)-ary letters, integers \(n\ge3\), and three distinct lengths \(1\le a<b<c<n\). The established classical burst-deletion formula (equation (1) in RESULT.md) converts the centered diversity into sums of centered equality/disagreement indicators along lag edges. The forest lemma is valid because new leaf colors are independent and uniform, and so all three-edge forests have zero centered-product expectation. Three distinct edges make a cycle only as a triangle, requiring \(a+b=c\). At each of the \(n-c\) admissible left endpoints there are two distinct middle vertices; the exact one-triangle contribution is \(-(q-1)/q^3\). This proves the specified coefficient and the zero case. Two-edge forests also prove pairwise zero covariance. Full enumeration across all words for \(q=2,3\) and \(3\le n\le7\), using direct deletion output sets and independent closed-form comparison, returned `VERIFY_OK`. The finite check is not presented as a substitute for proof.

## Originality — PASS against accessible evidence, with limitations

Schoeny et al. (2016), Section IV equation (2), explicitly attribute the burst-deletion ball-size formula to Levenshtein and give the binary marginal distribution in Appendix A; these are **excluded from the new contribution**. Their principal claims are burst-correcting code bounds and constructions. Xi et al. (2025) study a different equal-length deletion-plus-insertion ball and its extremal/expected sizes and concentration, not joint mixed moments across different deletion-burst lengths. Searches of accessible research records using both the burst-deletion terminology and random lag-correlation terminology found no formula equivalent to the stated mixed third-cumulant resonance. Closest related database records address arbitrary two-symbol-deletion sphere variance or fixed-length Levenshtein ball variance, not three distinct *consecutive-burst* deletion sizes. Generic equality-graph cycle methods and unindexed probabilistic literature may contain an implication; that residual risk does not constitute an identified covering theorem.

## Mathematical value — PASS

The natural observable is a vector of deletion-ball sizes for a communication or storage string exposed to multiple candidate burst lengths. Separate ball-size distributions cannot characterize its joint fluctuations. The exact covariance vanishes for every distinct pair, which makes the first nonzero three-length interaction both surprising and informative; its complete classification by \(a+b=c\) reveals which simultaneous burst-length uncertainties interact and with what finite-size amplitude. The result is an all-length, all-alphabet-size structural theorem, not a finite table or renamed marginal enumeration. Full multivariate laws and nonuniform-source analogues are not established.

## Source comparison and residual risks

Reviewed the 2016 arXiv full-text Sections II and IV and Appendix A's marginal count, and the 2025 arXiv full-text introductory scope and relevant deletion-ball background. The former's classical formula is not claimed as new. Searches may miss equivalent higher-order moment formulas expressed as triangle cumulants of autocorrelation observables; independent literature review remains desirable. No claim of independent certification is made.

Self-review: passed. Independent audit: not yet performed.
